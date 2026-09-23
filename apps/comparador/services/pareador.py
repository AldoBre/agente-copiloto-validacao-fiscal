"""
Pareamento automático de notas entre dois conjuntos de XMLs — sem IA.

O problema: o consultor emitiu no Senior as mesmas 100 operações que existem no
sistema atual do cliente. Os arquivos têm nomes diferentes, as notas têm série e
numeração diferentes e a chave de acesso é obrigatoriamente diferente. Só o
**conteúdo fiscal** liga uma à outra.

A solução é uma *assinatura* por nota (destinatário, valor total, conjunto de
produtos, NCMs, data, quantidade de itens) e um escore de similaridade entre
todas as combinações, resolvido por atribuição gulosa: o par de maior escore é
fixado primeiro, e cada nota só pode ser usada uma vez.

Escore máximo = 100. Composição:

    destinatário idêntico ................ 30
    valor total idêntico ................. 28   (ou 14 se estiver a ≤2%)
    produtos em comum ................... 25 × Jaccard
        (pelo código OU pelo EAN — vale o sinal que casar melhor)
    NCMs em comum ........................  8 × Jaccard
    mesma data de emissão ................  6
    mesma quantidade de itens ............  5
    mesmo número de nota .................  3

Chave de acesso idêntica curto-circuita em 100 (acontece quando o consultor
exporta a mesma nota nos dois lados por engano — vale sinalizar).
"""
from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass, field
from decimal import Decimal

from .parser_nfe import DocumentoFiscal, para_decimal

LIMIAR_PADRAO = 30.0
LIMIAR_ALTA = 70.0
LIMIAR_MEDIA = 45.0

_RE_NAO_DIGITO = re.compile(r"\D+")

#: CNPJ genérico usado pela SEFAZ em ambiente de homologação. Não identifica
#: estabelecimento nenhum — é o mesmo em todas as notas de teste.
CNPJS_HOMOLOGACAO = {"00000000000191", "99999999000191"}

#: A SEFAZ obriga esta razão social nas notas de homologação. Como ela é idêntica
#: em TODAS as notas de teste, usá-la como sinal de "mesmo destinatário" casaria
#: qualquer nota com qualquer outra.
_RE_HOMOLOGACAO = re.compile(r"ambiente\s+de\s+homologac", re.IGNORECASE)


def _somente_digitos(valor: str) -> str:
    return _RE_NAO_DIGITO.sub("", valor or "")


def _normalizar(texto: str) -> str:
    texto = unicodedata.normalize("NFKD", (texto or "").strip())
    texto = "".join(c for c in texto if not unicodedata.combining(c))
    return re.sub(r"\s+", " ", texto).casefold()


#: Comprimentos válidos de GTIN (EAN-8, UPC-A, EAN-13, GTIN-14).
_TAMANHOS_GTIN = {8, 12, 13, 14}


def _ean_utilizavel(valor: str) -> str:
    """
    Devolve o GTIN normalizado, ou "" se ele não identifica produto nenhum.

    O XSD da NF-e permite o literal ``SEM GTIN`` no ``cEAN``, e ele é MUITO
    comum. Aceitá-lo seria desastroso para o pareamento: todo produto sem
    código de barras teria o mesmo "EAN", e qualquer nota casaria com qualquer
    outra pelo produto. Mesma lógica para o preenchimento com zeros.

    Não conferimos o dígito verificador de propósito: um GTIN inválido mas
    IGUAL nos dois sistemas ainda é evidência de que é o mesmo produto — é o
    cadastro do cliente que veio assim, e ele foi migrado como estava.
    """
    digitos = _somente_digitos(valor)
    if len(digitos) not in _TAMANHOS_GTIN or not digitos.strip("0"):
        return ""
    return digitos


def _jaccard(a: set[str], b: set[str]) -> float:
    if not a or not b:
        return 0.0
    intersecao = len(a & b)
    if not intersecao:
        return 0.0
    return intersecao / len(a | b)


@dataclass
class Assinatura:
    """Resumo comparável de uma nota, usado só para o pareamento."""

    nome_arquivo: str
    chave: str = ""
    identificacao: str = ""
    tipo: str = ""
    numero: str = ""
    serie: str = ""
    data: str = ""
    destinatario_doc: str = ""
    destinatario_nome: str = ""
    emitente_doc: str = ""
    valor_total: Decimal | None = None
    quantidade_itens: int = 0
    codigos_produto: set[str] = field(default_factory=set)
    #: GTINs utilizáveis. Numa migração o código interno costuma MUDAR entre
    #: os sistemas, e o EAN não — é o que liga os dois lados quando o
    #: cadastro foi recriado com numeração nova.
    eans: set[str] = field(default_factory=set)
    ncms: set[str] = field(default_factory=set)
    descricoes: set[str] = field(default_factory=set)
    cfops: set[str] = field(default_factory=set)

    def para_dicionario(self) -> dict:
        return {
            "nome_arquivo": self.nome_arquivo,
            "chave": self.chave,
            "identificacao": self.identificacao,
            "tipo": self.tipo,
            "numero": self.numero,
            "serie": self.serie,
            "data": self.data,
            "destinatario_doc": self.destinatario_doc,
            "destinatario_nome": self.destinatario_nome,
            "valor_total": str(self.valor_total) if self.valor_total is not None else "",
            "quantidade_itens": self.quantidade_itens,
            "produtos": sorted(self.codigos_produto)[:8],
            "eans": sorted(self.eans)[:8],
            "cfops": sorted(self.cfops)[:6],
        }


def montar_assinatura(doc: DocumentoFiscal) -> Assinatura:
    dest = doc.destinatario or {}
    emit = doc.emitente or {}

    documento_dest = _somente_digitos(
        dest.get("CNPJ", "") or dest.get("CPF", "") or dest.get("idEstrangeiro", "")
    )

    nome_dest = dest.get("xNome", "")
    if _RE_HOMOLOGACAO.search(_normalizar(nome_dest)):
        nome_dest = ""  # razão social de homologação não identifica ninguém

    total = ""
    for grupo in ("ICMSTot", "NFSeTot"):
        campos = doc.totais.get(grupo) or {}
        total = campos.get("vNF") or campos.get("vLiq") or campos.get("vServ") or total
        if total:
            break
    valor = para_decimal(total)
    if valor is None:
        soma = Decimal("0")
        achou = False
        for item in doc.itens:
            parcela = para_decimal(item.valor_produto)
            if parcela is not None:
                soma += parcela
                achou = True
        valor = soma if achou else None

    data = (doc.data_emissao or "")[:10]

    return Assinatura(
        nome_arquivo=doc.nome_arquivo,
        chave=doc.chave,
        identificacao=doc.identificacao,
        tipo=doc.tipo,
        numero=doc.numero,
        serie=doc.serie,
        data=data,
        destinatario_doc=documento_dest,
        destinatario_nome=nome_dest,
        emitente_doc=_somente_digitos(emit.get("CNPJ", "") or emit.get("CPF", "")),
        valor_total=valor,
        quantidade_itens=len(doc.itens),
        codigos_produto={i.codigo.strip().upper() for i in doc.itens if i.codigo.strip()},
        eans={g for i in doc.itens if (g := _ean_utilizavel(i.ean))},
        ncms={i.ncm.strip() for i in doc.itens if i.ncm.strip()},
        descricoes={_normalizar(i.descricao) for i in doc.itens if i.descricao.strip()},
        cfops={i.cfop.strip() for i in doc.itens if i.cfop.strip()},
    )


def pontuar(a: Assinatura, b: Assinatura) -> tuple[float, list[str]]:
    """Escore de similaridade (0–100) entre duas notas + os motivos legíveis."""
    if a.chave and a.chave == b.chave:
        return 100.0, ["chave de acesso idêntica nos dois arquivos"]

    pontos = 0.0
    motivos: list[str] = []

    # --- destinatário -------------------------------------------------------
    # Quando os dois lados informam o documento e eles DIFEREM, são operações de
    # clientes diferentes: penaliza forte. Sem essa penalidade, duas notas que só
    # compartilham o produto casariam por engano.
    if a.destinatario_doc and b.destinatario_doc:
        if a.destinatario_doc == b.destinatario_doc:
            pontos += 30
            motivos.append("mesmo destinatário (CNPJ/CPF)")
        else:
            pontos -= 25
            motivos.append("destinatários diferentes")
    elif a.destinatario_nome and _normalizar(a.destinatario_nome) == _normalizar(
        b.destinatario_nome
    ):
        pontos += 18
        motivos.append("mesmo destinatário (razão social)")

    # --- emitente -----------------------------------------------------------
    # Numa implantação o emitente é o MESMO estabelecimento nos dois sistemas.
    # O CNPJ genérico de homologação é ignorado — ele não identifica ninguém.
    emit_a, emit_b = a.emitente_doc, b.emitente_doc
    if (
        emit_a
        and emit_b
        and emit_a != emit_b
        and emit_a not in CNPJS_HOMOLOGACAO
        and emit_b not in CNPJS_HOMOLOGACAO
    ):
        pontos -= 15
        motivos.append("emitentes diferentes")

    # --- valor total --------------------------------------------------------
    if a.valor_total is not None and b.valor_total is not None:
        diferenca = abs(a.valor_total - b.valor_total)
        if diferenca <= Decimal("0.01"):
            pontos += 28
            motivos.append("valor total idêntico")
        elif a.valor_total and (diferenca / abs(a.valor_total)) <= Decimal("0.02"):
            pontos += 14
            motivos.append("valor total a menos de 2% de diferença")

    # --- produtos -----------------------------------------------------------
    # Código interno E EAN disputam os MESMOS 25 pontos, e vale o que casar
    # melhor. Somar os dois inflaria o escore e obrigaria a recalibrar os
    # limiares; do jeito abaixo, quem já casava por código pontua igual a antes,
    # e quem não casava por código passa a ter uma segunda chance.
    #
    # Os conjuntos são separados de propósito: juntar tudo num só faria um
    # código interno "789" casar com um EAN "789" de outro produto.
    jaccard_codigos = _jaccard(a.codigos_produto, b.codigos_produto)
    jaccard_eans = _jaccard(a.eans, b.eans)

    if jaccard_codigos >= jaccard_eans and jaccard_codigos > 0:
        pontos += 25 * jaccard_codigos
        motivos.append(f"{round(jaccard_codigos * 100)}% dos códigos de produto em comum")
    elif jaccard_eans > 0:
        pontos += 25 * jaccard_eans
        motivos.append(f"{round(jaccard_eans * 100)}% dos EAN/GTIN em comum")
    else:
        jaccard_descricoes = _jaccard(a.descricoes, b.descricoes)
        if jaccard_descricoes > 0:
            pontos += 20 * jaccard_descricoes
            motivos.append(f"{round(jaccard_descricoes * 100)}% das descrições em comum")

    # --- NCM ----------------------------------------------------------------
    jaccard_ncm = _jaccard(a.ncms, b.ncms)
    if jaccard_ncm > 0:
        pontos += 8 * jaccard_ncm

    # --- data ---------------------------------------------------------------
    if a.data and a.data == b.data:
        pontos += 6
        motivos.append("mesma data de emissão")

    # --- estrutura ----------------------------------------------------------
    if a.quantidade_itens and a.quantidade_itens == b.quantidade_itens:
        pontos += 5

    if a.numero and a.numero == b.numero:
        pontos += 3
        motivos.append("mesmo número de nota")

    return max(0.0, min(pontos, 99.0)), motivos


def classificar(score: float) -> str:
    if score >= LIMIAR_ALTA:
        return "alta"
    if score >= LIMIAR_MEDIA:
        return "media"
    return "baixa"


@dataclass
class Par:
    cliente: Assinatura
    senior: Assinatura
    score: float
    motivos: list[str]

    @property
    def confianca(self) -> str:
        return classificar(self.score)


def parear(
    assinaturas_cliente: list[Assinatura],
    assinaturas_senior: list[Assinatura],
    *,
    limiar: float = LIMIAR_PADRAO,
) -> tuple[list[Par], list[Assinatura], list[Assinatura]]:
    """
    Atribuição gulosa: calcula todos os escores acima do limiar, ordena do maior
    para o menor e vai fixando os pares — cada nota entra em no máximo um par.

    Devolve ``(pares, sem_par_cliente, sem_par_senior)``.
    """
    candidatos: list[tuple[float, int, int, list[str]]] = []

    for i, a in enumerate(assinaturas_cliente):
        for j, b in enumerate(assinaturas_senior):
            score, motivos = pontuar(a, b)
            if score >= limiar:
                candidatos.append((score, i, j, motivos))

    # Empate no escore: preferimos o par cujos índices estão mais próximos —
    # arquivos exportados em sequência tendem a corresponder na mesma ordem.
    candidatos.sort(key=lambda c: (-c[0], abs(c[1] - c[2])))

    usados_cliente: set[int] = set()
    usados_senior: set[int] = set()
    pares: list[Par] = []

    for score, i, j, motivos in candidatos:
        if i in usados_cliente or j in usados_senior:
            continue
        usados_cliente.add(i)
        usados_senior.add(j)
        pares.append(
            Par(
                cliente=assinaturas_cliente[i],
                senior=assinaturas_senior[j],
                score=score,
                motivos=motivos,
            )
        )

    pares.sort(key=lambda p: (-p.score, p.cliente.nome_arquivo))

    sem_par_cliente = [a for i, a in enumerate(assinaturas_cliente) if i not in usados_cliente]
    sem_par_senior = [b for j, b in enumerate(assinaturas_senior) if j not in usados_senior]

    return pares, sem_par_cliente, sem_par_senior
