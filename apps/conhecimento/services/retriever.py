"""
Recuperação de contexto para o agente.

Busca híbrida:
  * **semântica** — cosseno entre o embedding da pergunta e os dos trechos
    (só quando existe provedor de embeddings cadastrado);
  * **textual** — BM25 sobre um **índice invertido em memória**.

Os dois rankings são combinados por *Reciprocal Rank Fusion*, robusto a escalas
de score diferentes. Sem embeddings, o resultado é o ranking textual puro.

## Por que existe um índice em cache

A versão ingênua (tokenizar todos os trechos a cada pergunta) é O(n) por
consulta: mediu-se 281 ms com 540 trechos, o que projeta ~10 s com 20 mil.
Como a base de suporte da Senior tem milhares de artigos, isso deixaria o chat
inutilizável.

O índice é construído uma vez e reaproveitado; a versão é conferida por uma
única query agregada (contagem + maior id), barata o bastante para rodar a cada
pergunta. Qualquer ingestão ou reindexação muda a versão e dispara a
reconstrução automaticamente.
"""
from __future__ import annotations

import logging
import math
import threading
import time
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from typing import Any, Iterable

from django.conf import settings
from django.db import connection
from django.db.models import BooleanField, Count, ExpressionWrapper, Max, Q

from apps.provedores.factory import construir_embeddings
from apps.provedores.models import ProvedorIA, TipoModelo

from ..models import RegraParametrizacao, Trecho
from .fts import ranking_fts
from .sinonimos import SINONIMOS_CANONICOS
from .texto import tokenizar  # noqa: F401 — pipeline canônico; reexportado

logger = logging.getLogger(__name__)


def _semantica_ativa() -> bool:
    """
    TEMPORÁRIO — remover quando o pgvector for habilitado no banco.

    A busca semântica em RAM (matriz de embeddings por worker) derrubou o plano
    compartilhado em 31/07/2026, e a versão pgvector está bloqueada até o admin
    rodar CREATE EXTENSION. Desligada por padrão; ligue com
    AGENTE_BUSCA_SEMANTICA=on (ambiente local) para testar.
    """
    return bool(settings.AGENTE.get("BUSCA_SEMANTICA"))

#: Pesos relativos de cada ranking na fusão RRF — normalizados sobre os que
#: existirem na consulta (o FTS só roda no Postgres; o semântico, com provedor
#: e flag). textual = BM25 em memória (IDF, título do documento); fts = GIN do
#: Postgres (stemming oficial, escala com a base); semantico = embeddings.
PESOS_RRF = {"textual": 0.4, "fts": 0.35, "semantico": 0.6}
K_RRF = 60

# Parâmetros BM25
K1 = 1.5
B = 0.75

#: Token de título conta como este nº de ocorrências no índice (BM25F
#: simplificado): quem busca "rotinas de ICMS" precisa achar a página cujo
#: TÍTULO é esse, mesmo que o corpo não repita a expressão.
PESO_TITULO = 2
#: Peso do termo adicionado por sinônimo, relativo ao digitado (1.0) — amplia
#: o casamento sigla ↔ extenso sem atropelar o que o usuário escreveu.
PESO_SINONIMO = 0.5


# --------------------------------------------------------------------------- #
#  Índice em memória
# --------------------------------------------------------------------------- #
@dataclass
class _Trecho:
    """Cópia enxuta do registro — guardar o model inteiro custa memória à toa."""

    id: int
    texto: str
    documento: str
    secao: str
    url: str
    fonte: str
    tem_embedding: bool


@dataclass
class _Indice:
    versao: tuple
    trechos: list[_Trecho] = field(default_factory=list)
    #: termo → [(posição do trecho, frequência)]
    postings: dict[str, list[tuple[int, int]]] = field(default_factory=dict)
    comprimentos: list[int] = field(default_factory=list)
    comprimento_medio: float = 1.0
    #: id do Trecho → posição — ponte entre rankings que voltam do banco com
    #: ids (FTS) e o restante do pipeline, que trabalha por posição.
    posicao_por_id: dict[int, int] = field(default_factory=dict)
    construido_em: float = 0.0

    @property
    def total(self) -> int:
        return len(self.trechos)


_indice: _Indice | None = None
_trava = threading.Lock()


def _versao_atual() -> tuple:
    """Assinatura barata da base — muda a cada ingestão ou reindexação."""
    agregado = Trecho.objects.aggregate(n=Count("id"), maior=Max("id"))
    return (agregado["n"] or 0, agregado["maior"] or 0)


def _construir_indice(versao: tuple) -> _Indice:
    inicio = time.perf_counter()
    indice = _Indice(versao=versao)

    postings: dict[str, list[tuple[int, int]]] = defaultdict(list)

    # O índice em memória guarda SÓ o que a busca textual precisa. Os vetores
    # ficam no banco e são comparados lá (ver _ranking_semantico_do_vetor):
    # carregá-los aqui custava ~51 MB residentes por worker e um pico de
    # ~466 MB na construção — o que derrubou o plano compartilhado em 31/07.
    #
    # A coluna `embedding` NÃO é selecionada em nenhum caso: só transferi-la
    # custa ~12 KB por trecho. `sem_vetor` preserva o que a UI mostra.
    consulta = (
        Trecho.objects.select_related("documento", "documento__fonte")
        .annotate(
            sem_vetor=ExpressionWrapper(
                Q(embedding__isnull=True), output_field=BooleanField()
            )
        )
        .values_list(
            "id",
            "texto",
            "sem_vetor",
            "titulo_secao",
            "documento__titulo",
            "documento__url",
            "documento__fonte__nome",
        )
    )

    for posicao, (id_, texto, sem_vetor, secao, doc, url, fonte) in enumerate(
        consulta.iterator(chunk_size=500)
    ):
        indice.trechos.append(
            _Trecho(
                id=id_,
                texto=texto,
                documento=doc or "",
                secao=secao or "",
                url=url or "",
                fonte=fonte or "",
                tem_embedding=not sem_vetor,
            )
        )
        indice.posicao_por_id[id_] = posicao

        tokens = tokenizar(texto)
        # Títulos (da seção e do documento) entram no índice com peso — antes
        # nem eram indexados, então "Rotinas de ICMS" só era encontrada se o
        # corpo repetisse o título.
        tokens_titulo = tokenizar(f"{secao or ''} {doc or ''}")
        indice.comprimentos.append(len(tokens) + len(tokens_titulo) * PESO_TITULO)
        contagem = Counter(tokens)
        for termo, freq_titulo in Counter(tokens_titulo).items():
            contagem[termo] += freq_titulo * PESO_TITULO
        for termo, frequencia in contagem.items():
            postings[termo].append((posicao, frequencia))

    indice.postings = dict(postings)
    total_tokens = sum(indice.comprimentos)
    indice.comprimento_medio = (total_tokens / len(indice.comprimentos)) if indice.comprimentos else 1.0

    indice.construido_em = time.perf_counter() - inicio
    logger.info(
        "Índice textual reconstruído: %s trechos, %s termos, %.0f ms "
        "(os vetores ficam no banco)",
        indice.total,
        len(indice.postings),
        indice.construido_em * 1000,
    )
    return indice


def obter_indice() -> _Indice:
    """Devolve o índice atual, reconstruindo se a base mudou."""
    global _indice
    versao = _versao_atual()
    if _indice is not None and _indice.versao == versao:
        return _indice
    with _trava:
        if _indice is None or _indice.versao != versao:  # outra thread pode ter feito
            _indice = _construir_indice(versao)
    return _indice


def invalidar_indice() -> None:
    """Força a reconstrução na próxima busca (usado após ingestão/reindexação)."""
    global _indice
    with _trava:
        _indice = None


# --------------------------------------------------------------------------- #
#  Rankings
# --------------------------------------------------------------------------- #
def _ranking_textual(consulta: str, indice: _Indice, limite: int) -> list[tuple[int, float]]:
    """
    BM25 pelo índice invertido: só os trechos que contêm algum termo da
    pergunta são pontuados, em vez da base inteira.
    """
    tokens = tokenizar(consulta)
    if not tokens or not indice.total:
        return []

    # Termo digitado pesa 1.0; sinônimos entram com PESO_SINONIMO (sigla ↔
    # extenso, "tributação" ↔ "tributária") só do lado da consulta.
    pesos: dict[str, float] = {t: 1.0 for t in tokens}
    for t in tokens:
        for sinonimo in SINONIMOS_CANONICOS.get(t, ()):
            pesos.setdefault(sinonimo, PESO_SINONIMO)

    n = indice.total
    pontuacoes: dict[int, float] = defaultdict(float)

    for termo, peso_termo in pesos.items():
        lista = indice.postings.get(termo)
        if not lista:
            continue
        df = len(lista)
        idf = math.log(1 + (n - df + 0.5) / (df + 0.5))
        for posicao, frequencia in lista:
            comprimento = indice.comprimentos[posicao] or 1
            denominador = frequencia + K1 * (1 - B + B * comprimento / indice.comprimento_medio)
            pontuacoes[posicao] += peso_termo * idf * (frequencia * (K1 + 1)) / denominador

    return sorted(pontuacoes.items(), key=lambda p: p[1], reverse=True)[:limite]


def _vetores_das_consultas(consultas: list[str]) -> list[Any] | None:
    """
    Embute **todas** as consultas numa única chamada ao provedor.

    Com N causas divergentes o agente faz N buscas dirigidas. Uma chamada por
    consulta custaria N × ~500 ms de rede; em lote é um round-trip só.
    """
    if not _semantica_ativa():
        return None
    provedor = ProvedorIA.obter_padrao(TipoModelo.EMBEDDING)
    if provedor is None:
        return None
    try:
        import numpy as np

        modelo = construir_embeddings(provedor)
        brutos = modelo.embed_documents(consultas)
        return [np.asarray(v, dtype="float32") for v in brutos]
    except Exception as exc:  # noqa: BLE001
        logger.warning(
            "Busca semântica indisponível (%s: %s). Usando só busca textual.",
            type(exc).__name__,
            exc,
        )
        return None


def _ranking_semantico_do_vetor(vetor, indice: _Indice, limite: int) -> list[tuple[int, float]]:
    """
    Similaridade de cosseno resolvida NO BANCO, via pgvector.

    Antes a matriz inteira vivia na RAM de cada worker e a conta era feita em
    numpy: ~51 MB residentes por worker, pico de ~466 MB ao montar o índice e
    quase um minuto de partida. Aqui o Postgres faz a conta onde o dado já está,
    e o processo não guarda vetor nenhum.

    A busca é **exata**: não há índice HNSW, de propósito. Índice aproximado
    troca acerto por tempo, e com a base atual a varredura completa custa
    dezenas de milissegundos — irrelevante perto dos segundos que o modelo leva
    para responder. Além disso, `vector` puro só indexa até 2.000 dimensões, e
    as nossas são 3.072: exigiria o cast para halfvec, perdendo precisão.
    """
    if vetor is None:
        return []

    # Mesmo guard do ranking_fts: `<=>` e `vector_dims` são do PostgreSQL, e no
    # SQLite (o modo "rodar sem infra") viram erro de sintaxe. Sem isto a suíte
    # fica vermelha fora do Postgres, e — pior — o teste de dimensão divergente
    # passava pelo motivo errado: recebia [] por erro de SQL, não por filtro.
    if connection.vendor != "postgresql":
        return []

    # `.tolist()` e não `list()`: no NumPy 2 o repr do escalar virou
    # "np.float32(0.024)", e `str(list(vetor))` produz um literal que o pgvector
    # recusa ("invalid input syntax for type vector"). O sintoma seria busca
    # semântica devolvendo vazio em silêncio, com um warning — o modo de falha
    # mais caro que existe aqui. Medido: quebra com numpy 2.5.
    try:
        consulta = vetor.tolist() if hasattr(vetor, "tolist") else [float(x) for x in vetor]
        # `<=>` é a distância de cosseno do pgvector (0 = idêntico), e é o mesmo
        # operador no ORDER BY para o planejador poder usar índice se um dia
        # houver um.
        with connection.cursor() as cursor:
            # A distância é calculada UMA vez, na subconsulta, e reaproveitada
            # no SELECT e na ordenação. Escrever `<=>` nos dois lugares faz o
            # Postgres avaliar duas vezes por linha — e com 3.072 dimensões o
            # vetor tem 12 KB e vive em TOAST externo, então cada avaliação é um
            # detoast completo. Medido: 68 ms contra 44 ms, ~35% do tempo jogado
            # fora, multiplicado por até 9 consultas num turno de chat.
            #
            # Se um dia houver índice (HNSW), ele precisa de
            # `ORDER BY embedding <=> const` na forma literal — reverter esta
            # subconsulta faz parte de adicionar o índice.
            cursor.execute(
                """
                SELECT id, 1 - distancia AS similaridade
                  FROM (
                        SELECT id, embedding <=> %s::vector AS distancia
                          FROM conhecimento_trecho
                         WHERE embedding IS NOT NULL
                           AND vector_dims(embedding) = %s
                         ORDER BY distancia
                         LIMIT %s
                       ) AS vizinhos
                """,
                [str(consulta), len(consulta), limite],
            )
            linhas = cursor.fetchall()
    except Exception as exc:  # noqa: BLE001
        # A mensagem é cortada de propósito: erro de sintaxe do pgvector ecoa o
        # vetor inteiro, e 3.072 floats viram uma linha de log de ~460 KB.
        logger.warning(
            "Falha no ranking semântico (%s: %.300s).", type(exc).__name__, exc
        )
        return []

    # O filtro por vector_dims descarta vetores de outro modelo (troca de
    # embeddings no meio da base). Sem ele o banco levanta erro de dimensão em
    # vez de simplesmente ignorar o que não dá para comparar.
    if not linhas:
        logger.info(
            "Busca semântica sem resultados — não há vetor de %s dimensões na base. "
            "Se o modelo de embeddings mudou, rode 'python manage.py reindexar'.",
            len(vetor),
        )
        return []

    # O resto do pipeline trabalha por POSIÇÃO no índice textual; o banco devolve
    # id. `posicao_por_id` é a ponte — a mesma que o ranking do FTS já usa.
    return [
        (indice.posicao_por_id[id_], float(similaridade))
        for id_, similaridade in linhas
        if id_ in indice.posicao_por_id
    ]


def _ranking_semantico(consulta: str, indice: _Indice, limite: int) -> list[tuple[int, float]]:
    vetores = _vetores_das_consultas([consulta])
    return _ranking_semantico_do_vetor(vetores[0] if vetores else None, indice, limite)


def _combinar(
    textual: list[tuple[int, float]],
    fts: list[tuple[int, float]],
    semantico: list[tuple[int, float]],
) -> list[tuple[int, float, str]]:
    """Junta os rankings disponíveis: RRF ponderada quando há mais de um."""
    rankings = [
        (rotulo, lista, PESOS_RRF[rotulo])
        for rotulo, lista in (("textual", textual), ("fts", fts), ("semantico", semantico))
        if lista
    ]
    if not rankings:
        return []
    if len(rankings) == 1:
        rotulo, lista, _peso = rankings[0]
        return [(i, s, rotulo) for i, s in lista]

    total_pesos = sum(peso for _r, _l, peso in rankings)
    scores: dict[int, float] = defaultdict(float)
    origem: dict[int, set[str]] = defaultdict(set)

    for rotulo, ranking, peso in rankings:
        for posicao, (indice_trecho, _score) in enumerate(ranking):
            scores[indice_trecho] += (peso / total_pesos) / (K_RRF + posicao + 1)
            origem[indice_trecho].add(rotulo)

    combinado = [
        (i, s, "hibrido" if len(origem[i]) > 1 else next(iter(origem[i])))
        for i, s in scores.items()
    ]
    combinado.sort(key=lambda x: x[1], reverse=True)
    return combinado


# --------------------------------------------------------------------------- #
#  API pública
# --------------------------------------------------------------------------- #
@dataclass
class TrechoRecuperado:
    trecho_id: int
    texto: str
    documento: str
    secao: str
    url: str
    fonte: str
    score: float
    origem_ranking: str  # "semantico" | "textual" | "hibrido"

    def para_dicionario(self) -> dict[str, Any]:
        return {
            "trecho_id": self.trecho_id,
            "documento": self.documento,
            "secao": self.secao,
            "url": self.url,
            "fonte": self.fonte,
            "score": round(self.score, 4),
            "origem": self.origem_ranking,
            "preview": self.texto[:300],
        }


def buscar_contexto(consulta: str, *, top_k: int = 6) -> list[TrechoRecuperado]:
    """Devolve os ``top_k`` trechos mais relevantes da base de conhecimento."""
    if not (consulta or "").strip():
        return []

    indice = obter_indice()
    if not indice.total:
        return []

    janela = max(top_k * 4, 20)
    textual = _ranking_textual(consulta, indice, janela)
    fts = ranking_fts(consulta, indice.posicao_por_id, janela)
    semantico = _ranking_semantico(consulta, indice, janela)

    combinado = _combinar(textual, fts, semantico)
    return [_montar(indice, p, s, o) for p, s, o in combinado[:top_k]]


def _montar(indice: _Indice, posicao: int, score: float, origem: str) -> TrechoRecuperado:
    trecho = indice.trechos[posicao]
    return TrechoRecuperado(
        trecho_id=trecho.id,
        texto=trecho.texto,
        documento=trecho.documento,
        secao=trecho.secao,
        url=trecho.url,
        fonte=trecho.fonte,
        score=score,
        origem_ranking=origem,
    )


def buscar_por_consultas(
    consultas: list[str],
    *,
    por_consulta: int = 3,
    teto: int = 14,
    limites: dict[str, int] | None = None,
) -> dict[str, list[TrechoRecuperado]]:
    """
    Roda **várias buscas dirigidas** e devolve o resultado agrupado por consulta.

    Por que não uma consulta só: quando o lote tem 7 causas distintas — ICMS,
    CFOP, IPI, PIS, COFINS, cadastro de produto — concatená-las num texto único
    produz um vetor que não é parecido com nada. Medido em 24/07/2026 na base de
    3.934 trechos: a consulta concatenada devolveu *"Vlr ICMS Dif Aliq a menor"*
    e *"eDocs — Críticas de Integração"*; as mesmas causas perguntadas uma a uma
    devolveram *"Rotinas de ICMS"*, *"Validação CFOP — Natureza de Operação"* e
    *"Como efetuar a parametrização dos impostos PIS/COFINS"*.

    ``teto`` limita o total de trechos distintos que entram no prompt; a
    distribuição é justa (rodízio entre as consultas), para que nenhuma causa
    fique sem documentação porque outra trouxe muitos resultados bons.

    ``limites`` reduz a cota de consultas específicas. **Isso precisa acontecer
    dentro do rodízio, não depois.** Aparar o resultado de uma consulta depois
    de montada a lista não devolve as vagas: o trecho já entrou em ``vistos`` e
    fica bloqueado para as outras consultas, mesmo tendo sido descartado. Foi
    um bug real — a pergunta genérica do consultor reservava 3 trechos, ficava
    com 1, e as 2 vagas queimadas derrubavam causas para "não localizado". Como
    a pergunta muda a cada envio, o mesmo lote dava respostas diferentes.
    """
    consultas = [c for c in dict.fromkeys(c.strip() for c in consultas) if c]
    if not consultas:
        return {}

    relogio = time.perf_counter
    t0 = relogio()
    indice = obter_indice()
    if not indice.total:
        return {}
    t_indice = relogio() - t0

    janela = max(por_consulta * 4, 20)
    t0 = relogio()
    vetores = _vetores_das_consultas(consultas) or [None] * len(consultas)
    t_vetores = relogio() - t0

    t_bm25 = t_fts = t_semantico = 0.0
    por_pergunta: dict[str, list[TrechoRecuperado]] = {}
    for consulta, vetor in zip(consultas, vetores):
        t0 = relogio()
        textual = _ranking_textual(consulta, indice, janela)
        t1 = relogio()
        fts = ranking_fts(consulta, indice.posicao_por_id, janela)
        t2 = relogio()
        semantico = _ranking_semantico_do_vetor(vetor, indice, janela)
        t3 = relogio()
        t_bm25, t_fts, t_semantico = t_bm25 + t1 - t0, t_fts + t2 - t1, t_semantico + t3 - t2
        combinado = _combinar(textual, fts, semantico)
        por_pergunta[consulta] = [
            _montar(indice, posicao, score, origem)
            for posicao, score, origem in combinado[:por_consulta]
        ]

    # Uma linha por busca, com o tempo de cada perna. Existe porque a lentidão
    # desta função só aparece em produção e sem isto ela é indistinguível, no
    # log, de lentidão do modelo. Foi esta linha que mostrou, em 20/09/2026, que
    # `semantico` e `fts` oscilam de 0,4 s a 6,5 s para as MESMAS 3 consultas:
    # o banco é um B1ms Burstable compartilhado, com crédito de CPU zerado e
    # `read_iops` em 0 — é estrangulamento de CPU, não leitura de disco.
    logger.info(
        "[tempo] busca: %d consulta(s) · indice %.2fs · embeddings %.2fs · "
        "bm25 %.2fs · fts %.2fs · semantico %.2fs",
        len(consultas), t_indice, t_vetores, t_bm25, t_fts, t_semantico,
    )

    # Rodízio: pega o 1º de cada consulta, depois o 2º de cada, e assim por
    # diante. Corta no teto sem deixar nenhuma causa a descoberto.
    limites = limites or {}
    vistos: set[int] = set()
    escolhidos: dict[str, list[TrechoRecuperado]] = {c: [] for c in consultas}
    total = 0
    for posicao in range(por_consulta):
        for consulta in consultas:
            if total >= teto:
                break
            if len(escolhidos[consulta]) >= limites.get(consulta, por_consulta):
                continue
            candidatos = por_pergunta.get(consulta, [])
            if posicao < len(candidatos) and candidatos[posicao].trecho_id not in vistos:
                vistos.add(candidatos[posicao].trecho_id)
                escolhidos[consulta].append(candidatos[posicao])
                total += 1

    return {c: t for c, t in escolhidos.items() if t}


def buscar_regras(campos: Iterable[str]) -> list[dict[str, Any]]:
    """
    Busca as regras de parametrização cadastradas para os campos divergentes.

    Aceita tanto ``GRUPO.campo`` quanto só ``campo`` — devolve o match mais
    específico disponível.
    """
    campos = [c for c in dict.fromkeys(campos) if c]
    if not campos:
        return []

    folhas = {c.rsplit(".", 1)[-1] for c in campos}
    chaves = set(campos) | folhas

    regras = RegraParametrizacao.objects.filter(campo__in=chaves)
    por_chave = {r.campo: r for r in regras}

    saida: list[dict[str, Any]] = []
    for campo in campos:
        regra = por_chave.get(campo) or por_chave.get(campo.rsplit(".", 1)[-1])
        if regra is None:
            continue
        saida.append(
            {
                "campo": campo,
                "regra_de": regra.campo,
                "categoria": regra.categoria,
                "area": regra.area,
                "orientacao": regra.orientacao,
                "referencia_url": regra.referencia_url,
                "observacoes": regra.observacoes,
            }
        )
    return saida
