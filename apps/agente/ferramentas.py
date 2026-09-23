"""
Ferramentas que o agente pode chamar no meio da resposta.

## Por que existem, e o que elas mudam no produto

Até aqui o agente recebia tudo pronto: o relatório da comparação e um punhado de
trechos recuperados **antes** de ele ler a pergunta, com consultas derivadas das
divergências. Isso funciona bem no primeiro turno — e falha no segundo. Quando o
consultor pergunta "e o CEST desse produto?", a recuperação já aconteceu: o
modelo responde com o que sobrou do turno anterior ou não responde.

As ferramentas fecham essa lacuna. São **consultas de leitura**, todas baratas,
todas contra fonte oficial já importada (:mod:`apps.fiscal.models`) ou contra a
base de conhecimento indexada.

## A regra que faz isto ser seguro

Este produto tem um modo de falha caro e documentado: **acusar de errada uma
nota correta**. Ele já aconteceu duas vezes — o modelo afirmando de memória que
CFOP 5405 e 5102 diferem por "interna vs. interestadual" (ambos são 5xxx; a
diferença é substituição tributária), e uma conferência de CFOP acusando códigos
válidos de não existirem porque a tabela estava vazia.

Por isso toda ferramenta aqui distingue **três** respostas, nunca duas:

``ENCONTRADO``
    A tabela responde. Vem com a referência e a data de captura, para o modelo
    poder citar de onde tirou.
``NAO_CONSTA``
    A tabela está carregada e o código não está nela. É afirmação com lastro.
``NAO_VERIFICADO``
    A tabela **não está carregada neste ambiente**. Não é "não existe" — é "não
    sei", e o modelo é instruído a repassar isso ao consultor em vez de
    concluir. A lição saiu de produção.

A diferença entre as duas últimas é a diferença entre orientar e enganar.
"""
from __future__ import annotations

import contextvars
import logging
from typing import Any

from asgiref.sync import sync_to_async
from langchain_core.tools import BaseTool, tool

logger = logging.getLogger(__name__)

#: Teto de caracteres por resultado. Uma ferramenta que devolve 8 KB de texto
#: empurra o contexto útil para fora da janela — e o custo é cobrado em todo
#: turno seguinte, porque o resultado fica no histórico da rodada.
MAX_RESULTADO = 4000


def _cortar(texto: str) -> str:
    return texto if len(texto) <= MAX_RESULTADO else texto[:MAX_RESULTADO] + "\n…(truncado)"


def _pct(valor: Any) -> str:
    """
    Percentual sem zero à toa: ``15.00`` → ``15``, ``3.90`` → ``3.9``.

    ``:g`` não serve: em ``Decimal`` ele preserva os dígitos significativos
    (``15.00`` continua ``15.00``) e, em outros valores, cai em notação
    científica — que num texto sobre alíquota é ruído puro.
    """
    from decimal import Decimal

    if not isinstance(valor, Decimal):
        return str(valor)
    inteiro = valor.to_integral_value()
    return f"{inteiro:f}" if valor == inteiro else f"{valor.normalize():f}"


# --------------------------------------------------------------------------- #
#  Acesso às tabelas oficiais (sync — embrulhado em sync_to_async lá embaixo)
# --------------------------------------------------------------------------- #
def _carimbo(tabela: str) -> str:
    """Referência + data de captura da tabela, para o modelo poder citar."""
    from apps.fiscal.models import VersaoTabela

    versao = VersaoTabela.objects.filter(tabela=tabela).first()
    if not versao:
        return ""
    return f"{versao.referencia} (capturado em {versao.capturado_em:%d/%m/%Y})"


def _indisponivel(tabela: str, rotulo: str) -> str:
    return (
        f"NAO_VERIFICADO — a tabela de {rotulo} não está carregada neste ambiente.\n"
        f"Isto NÃO significa que o código seja inválido: significa que não há base "
        f"para conferir. Diga isso ao consultor e não conclua nada sobre este ponto."
    )


def _tabela_ok(nome: str, model) -> bool:
    from apps.fiscal.models import VersaoTabela

    return VersaoTabela.objects.filter(tabela=nome).exists() and model.objects.exists()


def _ncm_sync(codigo: str) -> str:
    import re

    from apps.fiscal.models import Ncm

    if not _tabela_ok("ncm", Ncm):
        return _indisponivel("ncm", "NCM")

    limpo = re.sub(r"\D", "", codigo or "")
    if not limpo:
        return "Código NCM vazio ou sem dígitos — nada a consultar."

    carimbo = _carimbo("ncm")
    registro = Ncm.objects.filter(codigo=limpo).first()
    if registro:
        linhas = [
            f"ENCONTRADO — NCM {limpo}",
            f"Descrição: {registro.descricao_hierarquica or registro.descricao}",
            f"Nível: {'subitem (8 dígitos, o que vai no XML)' if registro.e_subitem else f'agrupador de {len(limpo)} dígitos — não é NCM de item'}",
        ]
        if registro.inicio_vigencia:
            linhas.append(f"Vigência: desde {registro.inicio_vigencia:%d/%m/%Y}")
        if registro.fim_vigencia:
            linhas.append(f"ENCERRADO em {registro.fim_vigencia:%d/%m/%Y}")
        if registro.ato:
            linhas.append(f"Ato: {registro.ato}")
        linhas.append(f"Fonte: {carimbo}")
        return _cortar("\n".join(linhas))

    # Não achou o código cheio. O prefixo mais longo que existe é a informação
    # mais útil que resta: diz se o produto foi reclassificado dentro da mesma
    # posição ou se o código está simplesmente malformado.
    for tamanho in range(len(limpo) - 1, 1, -1):
        pai = Ncm.objects.filter(codigo=limpo[:tamanho]).first()
        if pai:
            return _cortar(
                f"NAO_CONSTA — o NCM {limpo} não está na tabela vigente.\n"
                f"O agrupador {pai.codigo} existe: {pai.descricao}\n"
                f"Ou seja, a posição existe e o desdobramento declarado não. "
                f"Isso costuma indicar código desatualizado no cadastro do produto.\n"
                f"Fonte: {carimbo}"
            )
    return f"NAO_CONSTA — nem o NCM {limpo} nem nenhum agrupador dele existem.\nFonte: {carimbo}"


def _ipi_sync(ncm: str, ex: int) -> str:
    import re

    from apps.fiscal.models import TipiAliquota

    if not _tabela_ok("tipi", TipiAliquota):
        return _indisponivel("tipi", "TIPI (IPI por NCM)")

    limpo = re.sub(r"\D", "", ncm or "")
    carimbo = _carimbo("tipi")
    if not limpo:
        return "Código NCM vazio — nada a consultar na TIPI."

    def _formatar(reg: TipiAliquota, nota: str = "") -> str:
        if reg.nao_tributado:
            valor = (
                "NT — **não tributado**, ou seja, fora do campo de incidência do IPI. "
                "NT não é 0%: são situações jurídicas diferentes e a CST de IPI "
                "correspondente também é diferente."
            )
        elif reg.aliquota is None:
            valor = "a tabela não traz alíquota para esta linha."
        else:
            valor = f"{_pct(reg.aliquota)}%"
        partes = [
            f"ENCONTRADO — IPI do NCM {reg.ncm}" + (f" Ex {reg.ex:02d}" if reg.ex else ""),
            f"Alíquota: {valor}",
        ]
        if reg.descricao:
            partes.append(f"Descrição na TIPI: {reg.descricao[:300]}")
        if nota:
            partes.append(nota)
        partes.append(f"Fonte: {carimbo}")
        return _cortar("\n".join(partes))

    registro = TipiAliquota.objects.filter(ncm=limpo, ex=ex or 0).first()
    if registro:
        return _formatar(registro)

    if ex:
        # Ex-tarifário inexistente é achado relevante por si só: o Ex reduz a
        # alíquota, então declarar um que não existe muda o imposto devido.
        base = TipiAliquota.objects.filter(ncm=limpo, ex=0).first()
        if base:
            return _formatar(
                base,
                nota=(
                    f"ATENÇÃO: o Ex {ex:02d} NÃO existe para este NCM na TIPI. "
                    f"A linha acima é a linha base (sem Ex)."
                ),
            )
        return (
            f"NAO_CONSTA — não há linha na TIPI para o NCM {limpo} "
            f"(nem com Ex {ex:02d}, nem sem Ex).\nFonte: {carimbo}"
        )

    exs = list(
        TipiAliquota.objects.filter(ncm=limpo).exclude(ex=0).values_list("ex", flat=True)[:10]
    )
    extra = (
        f"\nExistem Ex-tarifários para este NCM: {', '.join(f'{e:02d}' for e in exs)}."
        if exs
        else ""
    )
    return f"NAO_CONSTA — o NCM {limpo} não tem linha base na TIPI.{extra}\nFonte: {carimbo}"


def _cest_sync(ncm: str) -> str:
    import re

    from apps.fiscal.models import Cest

    if not _tabela_ok("cest", Cest):
        return _indisponivel("cest", "CEST (Convênio ICMS 142/2018)")

    limpo = re.sub(r"\D", "", ncm or "")
    carimbo = _carimbo("cest")
    if not limpo:
        return "Código NCM vazio — nada a consultar no CEST."

    # O casamento é por PREFIXO: a tabela traz desde capítulo de 2 dígitos até
    # subitem de 8. Ordenar por COMPRIMENTO do prefixo, não pelo código: o que
    # importa é quão específico foi o casamento.
    prefixos = [limpo[:t] for t in range(len(limpo), 1, -1)]
    achados = sorted(
        Cest.objects.filter(ncm_prefixo__in=prefixos),
        key=lambda c: -len(c.ncm_prefixo),
    )[:15]

    if not achados:
        return (
            f"NAO_CONSTA — nenhum CEST associado ao NCM {limpo} no Convênio 142/2018.\n"
            f"Pela tabela, esta mercadoria não está no universo nacional de substituição "
            f"tributária. Se ela está sujeita a ST depende ainda de protocolo/convênio "
            f"entre as UFs envolvidas, que esta tabela não cobre.\n"
            f"Fonte: {carimbo}"
        )

    def _linha(c: Cest) -> str:
        return (
            f"- {c.codigo} (prefixo {c.ncm_prefixo}) · anexo {c.anexo or '?'} · "
            f"{c.segmento or 'segmento não informado'} — {(c.descricao or '')[:160]}"
        )

    # Um casamento de 2 dígitos vem de célula do tipo "Capítulos 39, 40, …, 84":
    # é o capítulo inteiro da NCM, não a mercadoria. Misturar isso com um
    # casamento de 8 dígitos na mesma lista faz três CEST parecerem três
    # candidatos equivalentes — e sugere ST onde só houve coincidência de
    # capítulo.
    especificos = [c for c in achados if len(c.ncm_prefixo) >= 4]
    amplos = [c for c in achados if len(c.ncm_prefixo) < 4]

    linhas: list[str] = []
    if especificos:
        verbo = "casa" if len(especificos) == 1 else "casam"
        linhas.append(
            f"ENCONTRADO — {len(especificos)} CEST {verbo} com o NCM {limpo} "
            f"em nível de posição ou subitem:"
        )
        linhas.extend(_linha(c) for c in especificos)
        if len(especificos) > 1:
            linhas.append(
                "Mais de um CEST casando é normal: quem desempata é a descrição da "
                "mercadoria, não o código."
            )
    else:
        linhas.append(
            f"NAO_CONSTA em nível específico — nenhum CEST casa com o NCM {limpo} "
            f"por posição (4+ dígitos) ou subitem."
        )

    if amplos:
        linhas.append(
            f"\nCasamentos apenas por CAPÍTULO ({len(amplos)}) — o convênio lista a "
            f"faixa inteira da NCM nestes itens, então eles NÃO identificam a "
            f"mercadoria e não sustentam, sozinhos, uma conclusão sobre ST:"
        )
        linhas.extend(_linha(c) for c in amplos)

    linhas.append(f"\nFonte: {carimbo}")
    return _cortar("\n".join(linhas))


def _cfop_sync(codigo: str) -> str:
    import re

    from apps.fiscal.models import Cfop

    if not _tabela_ok("cfop", Cfop):
        return _indisponivel("cfop", "CFOP")

    limpo = re.sub(r"\D", "", codigo or "")
    carimbo = _carimbo("cfop")
    if len(limpo) != 4:
        return f"'{codigo}' não tem o formato de um CFOP (4 dígitos)."

    registro = Cfop.objects.filter(codigo=limpo).first()
    if not registro:
        return (
            f"NAO_CONSTA — o CFOP {limpo} não está na tabela do Portal Nacional da NF-e.\n"
            f"Fonte: {carimbo}"
        )

    sentido = "entrada" if registro.entrada else "saída"
    grupo = {
        "1": "operação interna (dentro do estado)",
        "2": "operação interestadual",
        "3": "operação com o exterior (importação)",
        "5": "operação interna (dentro do estado)",
        "6": "operação interestadual",
        "7": "operação com o exterior (exportação)",
    }.get(limpo[0], "grupo desconhecido")

    linhas = [
        f"ENCONTRADO — CFOP {limpo} é válido para NF-e.",
        f"Sentido: {sentido} · Abrangência: {grupo}",
    ]
    if registro.descricao:
        linhas.append(f"Descrição: {registro.descricao}")
    else:
        # Isto é importante e precisa ser dito ao modelo em toda resposta: sem
        # essa frase ele "completa" a descrição de memória, que é exatamente o
        # erro do CFOP 5405 registrado em prompts.py.
        linhas.append(
            "Descrição: a tabela oficial da NF-e é de VALIDAÇÃO, não dicionário — "
            "ela não traz o texto do CFOP. NÃO descreva o que este CFOP significa: "
            "você só pode afirmar que ele é aceito pela SEFAZ, o sentido e a abrangência."
        )
    linhas.append(f"Fonte: {carimbo}")
    return _cortar("\n".join(linhas))


def _fcp_sync(uf: str) -> str:
    from apps.fiscal.models import FcpUf

    if not _tabela_ok("fcp", FcpUf):
        return _indisponivel("fcp", "FCP por UF")

    sigla = (uf or "").strip().upper()[:2]
    carimbo = _carimbo("fcp")
    registro = FcpUf.objects.filter(uf=sigla).first()
    if not registro:
        return f"NAO_CONSTA — não há linha de FCP para a UF '{sigla}'.\nFonte: {carimbo}"

    if registro.tipo == FcpUf.Tipo.FIXO:
        conclusao = (
            f"{_pct(registro.aliquota)}% — percentual FIXO. Declarar diferente disso é "
            f"divergência objetiva."
        )
    else:
        conclusao = (
            f"até {_pct(registro.aliquota)}% — a UF define apenas um TETO. Só é possível "
            f"apontar erro se o declarado passar do teto; abaixo dele, depende do "
            f"produto e não dá para concluir por esta tabela."
        )

    linhas = [f"ENCONTRADO — FCP em {sigla} ({registro.nome_uf}): {conclusao}"]
    if registro.aliquota_alternativa is not None:
        linhas.append(f"Segunda faixa publicada pela UF: {_pct(registro.aliquota_alternativa)}%")
    if registro.observacao:
        linhas.append(f"Observação da fonte: {registro.observacao[:300]}")
    linhas.append(f"Fonte: {carimbo}")
    return _cortar("\n".join(linhas))


def _busca_sync(consulta: str, top_k: int, imagens: dict[str, str]) -> dict[str, Any]:
    """
    ``imagens`` é o registro de prints **do turno inteiro**, e é mutado aqui.

    Não pode ser um dicionário novo por busca: ``trocar_por_marcadores`` numera
    por ``len(registro) + 1``, então um mapa zerado devolveria outro
    ``[[print:1]]`` — o mesmo marcador que a recuperação principal já usou para
    outra imagem. O consultor veria a captura de uma tela sob o rótulo de outra,
    que é pior do que não ter print nenhum.
    """
    from apps.conhecimento.services.imagens import trocar_por_marcadores
    from apps.conhecimento.services.retriever import buscar_contexto

    trechos = buscar_contexto(consulta, top_k=top_k)
    if not trechos:
        return {
            "texto": (
                f"NAO_CONSTA — a busca por '{consulta}' não devolveu nenhum trecho da "
                f"documentação Senior. Não afirme tela nem campo de memória: diga que "
                f"o parâmetro não foi localizado na documentação disponível."
            ),
            "fontes": [],
        }

    partes = [f"ENCONTRADO — {len(trechos)} trecho(s) para '{consulta}':"]
    fontes: list[dict[str, Any]] = []
    for indice, t in enumerate(trechos, start=1):
        # Mesmo tratamento do nó de recuperação: a URL da imagem vira [[print:N]].
        texto, _ = trocar_por_marcadores(t.texto, imagens)
        cabecalho = f"### [{indice}] {t.documento}" + (f" — {t.secao}" if t.secao else "")
        rodape = f"_Fonte: {t.fonte}" + (f" · {t.url}" if t.url else "") + "_"
        partes.append(f"{cabecalho}\n\n{texto}\n\n{rodape}")
        dados = t.para_dicionario()
        dados["responde_a"] = consulta
        fontes.append(dados)

    return {"texto": _cortar("\n\n---\n\n".join(partes)), "fontes": fontes}


# --------------------------------------------------------------------------- #
#  As ferramentas propriamente ditas
#
#  A docstring de cada uma É o que o modelo lê para decidir se chama. Por isso
#  elas dizem QUANDO usar, e não só o que a função faz.
# --------------------------------------------------------------------------- #
@tool
async def consultar_ncm(codigo: str) -> str:
    """Confere um código NCM na tabela oficial vigente (Portal Único Siscomex).

    Use sempre que precisar afirmar que um NCM existe, está vigente ou o que ele
    classifica. Devolve a descrição hierárquica completa, a vigência e o ato que
    criou o código. Se o NCM não existir, diz qual agrupador dele existe — o que
    normalmente revela um código desatualizado no cadastro do produto.

    Args:
        codigo: o NCM, com ou sem pontuação (ex.: "8471.30.12" ou "84713012").
    """
    return await sync_to_async(_ncm_sync, thread_sensitive=True)(codigo)


@tool
async def consultar_ipi(ncm: str, ex: int = 0) -> str:
    """Consulta a alíquota de IPI de um NCM na TIPI vigente.

    É a única tabela oficial brasileira que liga código a alíquota. Use antes de
    dizer qualquer coisa sobre o IPI de um produto. Distingue "NT" (fora do campo
    de incidência) de 0% — tratar um como o outro faz o consultor cobrar imposto
    de quem não deve.

    Args:
        ncm: o NCM do produto, com ou sem pontuação.
        ex: o número do Ex-tarifário declarado na nota. Use 0 (padrão) quando não
            houver Ex. Se o Ex informado não existir para o NCM, isso é avisado.
    """
    return await sync_to_async(_ipi_sync, thread_sensitive=True)(ncm, ex)


@tool
async def consultar_cest(ncm: str) -> str:
    """Lista os CEST que casam com um NCM no Convênio ICMS 142/2018.

    Use para saber se a mercadoria está no universo nacional de substituição
    tributária e quais CEST são candidatos. O casamento é por prefixo de NCM, e
    normalmente mais de um CEST casa — quem desempata é a descrição da
    mercadoria, não o código. Esta tabela não diz se há ST entre duas UFs
    específicas: isso depende de protocolo/convênio que ela não cobre.

    Args:
        ncm: o NCM do produto, com ou sem pontuação.
    """
    return await sync_to_async(_cest_sync, thread_sensitive=True)(ncm)


@tool
async def consultar_cfop(codigo: str) -> str:
    """Verifica se um CFOP é aceito na NF-e e diz o sentido e a abrangência dele.

    Use antes de comentar qualquer CFOP. A tabela oficial é de validação, não
    dicionário: ela confirma que a SEFAZ aceita o código, se é entrada ou saída e
    se é interna, interestadual ou com o exterior — mas não traz o texto
    descritivo. Nunca complete a descrição de memória.

    Args:
        codigo: o CFOP de 4 dígitos (ex.: "5405").
    """
    return await sync_to_async(_cfop_sync, thread_sensitive=True)(codigo)


@tool
async def consultar_fcp(uf: str) -> str:
    """Consulta o Fundo de Combate à Pobreza de uma UF.

    Use ao conferir pFCP ou pFCPST. Alguns estados fixam o percentual e outros
    publicam só um teto — a diferença importa: com teto, um valor menor não é
    divergência.

    Args:
        uf: a sigla da unidade federativa (ex.: "RJ").
    """
    return await sync_to_async(_fcp_sync, thread_sensitive=True)(uf)


@tool
async def aliquota_icms_interestadual(
    uf_origem: str, uf_destino: str, origem_mercadoria: str = "0"
) -> str:
    """Calcula a alíquota interestadual de ICMS aplicável a uma operação.

    Regra de norma federal (Resolução do Senado 22/1989, com a 13/2012 para
    importados), não de tabela: 7% saindo do Sul/Sudeste (exceto ES) para
    Norte/Nordeste/Centro-Oeste/ES, 12% nos demais casos, e 4% para mercadoria
    importada, que prevalece sobre as duas anteriores.

    Args:
        uf_origem: sigla da UF do emitente.
        uf_destino: sigla da UF do destinatário.
        origem_mercadoria: o campo `orig` do item (0 a 8). Os códigos 1, 2, 3, 6
            e 7 indicam mercadoria importada e levam a alíquota a 4%.
    """
    from apps.fiscal.services import aliquota_interestadual

    origem = (uf_origem or "").strip().upper()[:2]
    destino = (uf_destino or "").strip().upper()[:2]
    if not origem or not destino:
        return "Informe as duas UFs para calcular a alíquota interestadual."
    if origem == destino:
        return (
            f"{origem} → {destino} é operação INTERNA, não interestadual. A alíquota "
            f"interna é definida por lei estadual e não está nas tabelas disponíveis "
            f"aqui — NAO_VERIFICADO."
        )

    codigo = (str(origem_mercadoria) or "0").strip()[:1]
    aliquota = aliquota_interestadual(origem, destino, codigo)
    if codigo in {"1", "2", "3", "6", "7"}:
        base = f"origem `{codigo}` indica mercadoria importada → Resolução do Senado 13/2012"
    elif aliquota == 7:
        base = f"{origem} (Sul/Sudeste) → {destino} → Resolução do Senado 22/1989, art. 1º, II"
    else:
        base = "Resolução do Senado 22/1989, art. 1º, I"

    return (
        f"ENCONTRADO — alíquota interestadual de ICMS: **{_pct(aliquota)}%**\n"
        f"Operação: {origem} → {destino}, origem da mercadoria `{codigo}`.\n"
        f"Base legal: {base}.\n"
        f"Atenção: isto é a alíquota INTERESTADUAL do ICMS próprio. Benefício, "
        f"redução de base, DIFAL e ST são cálculos separados."
    )


@tool
async def buscar_documentacao(consulta: str) -> str:
    """Busca na documentação do ERP Senior indexada na base de conhecimento.

    É a ferramenta para descobrir **em que tela do Senior um parâmetro é
    mantido**. Use sempre que precisar de uma tela, rotina, campo ou caminho de
    menu que não esteja nos trechos já recebidos — e principalmente quando o
    consultor fizer uma pergunta de acompanhamento sobre outro assunto.

    Escreva a consulta como uma frase nominal do assunto, não como pergunta:
    "parametrização de CFOP por transação" funciona melhor que "onde eu mudo o
    CFOP?".

    Args:
        consulta: o assunto a procurar, em português, em uma frase curta.
    """
    coleta = _COLETA.get()
    if coleta is None:
        # Sem coleta aberta a busca ainda funciona para o modelo; só não alimenta
        # as pastilhas de fonte. Melhor degradar assim do que falhar o turno.
        coleta = {"fontes": [], "imagens": {}}

    dados = await sync_to_async(_busca_sync, thread_sensitive=True)(
        consulta, 4, coleta["imagens"]
    )
    coleta["fontes"].extend(dados["fontes"])
    return dados["texto"]


# --------------------------------------------------------------------------- #
#  Canal lateral da busca documental
# --------------------------------------------------------------------------- #
#: A ferramenta devolve **texto** ao modelo, mas a interface precisa de mais
#: duas coisas: as fontes estruturadas (as pastilhas clicáveis embaixo da
#: resposta) e o mapa ``N → URL`` dos prints. O protocolo de ferramentas do
#: LangChain só carrega a string de volta, então o resto sai por aqui.
#:
#: Um dicionário de módulo seria vazamento entre requisições — dois consultores
#: perguntando ao mesmo tempo e um leva as fontes do outro. É o mesmo bug do
#: mapa global de prints, que fazia uma resposta exibir a captura da anterior.
#: O ContextVar mantém cada turno no seu.
_COLETA: contextvars.ContextVar[dict[str, Any] | None] = contextvars.ContextVar(
    "coleta_busca_documental", default=None
)


def abrir_coleta(imagens: dict[str, str]) -> dict[str, Any]:
    """
    Abre a coleta do turno e devolve o acumulador.

    ``imagens`` entra por referência e continua sendo o registro de prints do
    turno — é o que faz a numeração das buscas seguir de onde a recuperação
    principal parou, em vez de recomeçar do 1 e colidir.

    Precisa ser chamado **na mesma task** que executa as ferramentas: uma task
    filha herda uma cópia do contexto no instante em que nasce, então um ``set``
    feito num nó anterior do grafo não chegaria aqui. Quem chama guarda a
    referência devolvida e lê dela depois — sem depender do ContextVar na volta.
    """
    coleta: dict[str, Any] = {"fontes": [], "imagens": imagens}
    _COLETA.set(coleta)
    return coleta


#: Ordem importa pouco para o modelo, mas mantém o prompt estável entre deploys.
FERRAMENTAS: list[BaseTool] = [
    buscar_documentacao,
    consultar_ncm,
    consultar_ipi,
    consultar_cest,
    consultar_cfop,
    consultar_fcp,
    aliquota_icms_interestadual,
]

POR_NOME: dict[str, BaseTool] = {f.name: f for f in FERRAMENTAS}
