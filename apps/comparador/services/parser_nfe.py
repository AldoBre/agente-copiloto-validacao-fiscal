"""
Parser de documentos fiscais eletrônicos.

Suporta:
  * NF-e / NFC-e layout 4.00  (``nfeProc`` → ``NFe`` → ``infNFe``)
  * NFS-e nacional            (``NFSe`` / ``DPS`` → ``infNFSe`` / ``infDPS``)

O parser é **tolerante a namespace** (compara sempre o nome local da tag) e
**genérico dentro dos grupos de imposto**: em vez de mapear campo a campo, ele
achata todos os nós-folha do grupo. Isso faz com que campos novos do layout
(p.ex. os grupos IBS/CBS da reforma tributária) apareçam na comparação sem
precisar mexer no código.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from decimal import Decimal, InvalidOperation
from typing import Any
from xml.etree import ElementTree as ET

# --------------------------------------------------------------------------- #
#  Helpers de árvore XML
# --------------------------------------------------------------------------- #


class ErroDeParse(ValueError):
    """XML inválido ou de um layout que não sabemos ler."""


def _nome(elem: ET.Element) -> str:
    """Nome local da tag, sem o namespace."""
    tag = elem.tag
    return tag.split("}", 1)[1] if "}" in tag else tag


def _filho(elem: ET.Element | None, nome: str) -> ET.Element | None:
    if elem is None:
        return None
    for c in elem:
        if _nome(c) == nome:
            return c
    return None


def _filhos(elem: ET.Element | None, nome: str) -> list[ET.Element]:
    if elem is None:
        return []
    return [c for c in elem if _nome(c) == nome]


def _descendente(raiz: ET.Element, nome: str) -> ET.Element | None:
    if _nome(raiz) == nome:
        return raiz
    for elem in raiz.iter():
        if _nome(elem) == nome:
            return elem
    return None


def _texto(elem: ET.Element | None, nome: str | None = None, padrao: str = "") -> str:
    alvo = _filho(elem, nome) if nome else elem
    if alvo is None or alvo.text is None:
        return padrao
    return alvo.text.strip()


def _achatar(elem: ET.Element, prefixo: str = "") -> dict[str, str]:
    """
    Converte a subárvore em ``{"caminho.pontilhado": "valor"}``.

    Só nós-folha viram entrada. Grupos aninhados (gIBSUF, gCBS, IPITrib...)
    entram com o caminho completo separado por ponto.
    """
    saida: dict[str, str] = {}
    for filho in elem:
        chave = f"{prefixo}{_nome(filho)}"
        if len(filho):
            saida.update(_achatar(filho, prefixo=f"{chave}."))
        else:
            saida[chave] = (filho.text or "").strip()
    return saida


def para_decimal(valor: Any) -> Decimal | None:
    if valor is None:
        return None
    texto = str(valor).strip()
    if not texto:
        return None
    texto = texto.replace(" ", "")
    # Formato brasileiro eventual: 1.234,56
    if "," in texto:
        texto = texto.replace(".", "").replace(",", ".")
    try:
        return Decimal(texto)
    except (InvalidOperation, ValueError):
        return None


# --------------------------------------------------------------------------- #
#  Estruturas
# --------------------------------------------------------------------------- #

#: Grupos de imposto extraídos de cada item (nome do nó dentro de <imposto>).
GRUPOS_IMPOSTO = (
    "ICMS",
    "IPI",
    "II",
    "PIS",
    "PISST",
    "COFINS",
    "COFINSST",
    "ISSQN",
    "ICMSUFDest",
    "IBSCBS",  # reforma tributária
)

#: Grupos de totalizadores lidos de <total>.
GRUPOS_TOTAIS = ("ICMSTot", "ISSQNtot", "retTrib", "IBSCBSTot")


@dataclass
class ItemNota:
    numero: int
    codigo: str = ""
    ean: str = ""
    descricao: str = ""
    ncm: str = ""
    nve: str = ""
    cest: str = ""
    cfop: str = ""
    unidade: str = ""
    quantidade: str = ""
    valor_unitario: str = ""
    valor_produto: str = ""
    valor_desconto: str = ""
    valor_frete: str = ""
    valor_seguro: str = ""
    valor_outros: str = ""
    ind_total: str = ""
    cbenef: str = ""
    #: ``{"ICMS": {"_variante": "ICMS00", "orig": "0", "CST": "00", ...}, ...}``
    impostos: dict[str, dict[str, str]] = field(default_factory=dict)
    informacoes_adicionais: str = ""

    @property
    def rotulo(self) -> str:
        partes = [f"item {self.numero}"]
        if self.codigo:
            partes.append(self.codigo)
        if self.descricao:
            partes.append(self.descricao[:60])
        return " · ".join(partes)

    def campos_produto(self) -> dict[str, str]:
        return {
            "cProd": self.codigo,
            "cEAN": self.ean,
            "xProd": self.descricao,
            "NCM": self.ncm,
            "NVE": self.nve,
            "CEST": self.cest,
            "CFOP": self.cfop,
            "uCom": self.unidade,
            "qCom": self.quantidade,
            "vUnCom": self.valor_unitario,
            "vProd": self.valor_produto,
            "vDesc": self.valor_desconto,
            "vFrete": self.valor_frete,
            "vSeg": self.valor_seguro,
            "vOutro": self.valor_outros,
            "indTot": self.ind_total,
            "cBenef": self.cbenef,
        }

    def para_dicionario(self) -> dict[str, Any]:
        return {
            "numero": self.numero,
            "codigo": self.codigo,
            "descricao": self.descricao,
            "ncm": self.ncm,
            "cest": self.cest,
            "cfop": self.cfop,
            "unidade": self.unidade,
            "quantidade": self.quantidade,
            "valor_unitario": self.valor_unitario,
            "valor_produto": self.valor_produto,
            "impostos": self.impostos,
        }


@dataclass
class DocumentoFiscal:
    origem: str  # "cliente" | "senior"
    tipo: str = "NFe"  # NFe | NFCe | NFSe
    nome_arquivo: str = ""
    chave: str = ""
    modelo: str = ""
    serie: str = ""
    numero: str = ""
    data_emissao: str = ""
    #: Campos do grupo <ide> achatados.
    ide: dict[str, str] = field(default_factory=dict)
    emitente: dict[str, str] = field(default_factory=dict)
    destinatario: dict[str, str] = field(default_factory=dict)
    itens: list[ItemNota] = field(default_factory=list)
    #: ``{"ICMSTot": {...}, "IBSCBSTot": {...}}``
    totais: dict[str, dict[str, str]] = field(default_factory=dict)
    pagamentos: list[dict[str, str]] = field(default_factory=list)
    informacoes_adicionais: dict[str, str] = field(default_factory=dict)
    avisos: list[str] = field(default_factory=list)

    @property
    def identificacao(self) -> str:
        partes = []
        if self.modelo:
            partes.append(f"mod. {self.modelo}")
        if self.serie:
            partes.append(f"série {self.serie}")
        if self.numero:
            partes.append(f"nº {self.numero}")
        return " / ".join(partes) or self.tipo

    def campos_cabecalho(self) -> dict[str, str]:
        """Campos do cabeçalho que influenciam a tributação."""
        interessantes = (
            "natOp",
            "mod",
            "serie",
            "tpNF",
            "idDest",
            "indPres",
            "indFinal",
            "indIntermed",
            "finNFe",
            "tpEmis",
            "cMunFG",
        )
        saida = {f"ide.{k}": self.ide.get(k, "") for k in interessantes if k in self.ide}
        for chave in ("CRT", "UF", "IE", "CNPJ"):
            if chave in self.emitente:
                saida[f"emit.{chave}"] = self.emitente[chave]
        for chave in ("indIEDest", "UF", "IE", "CNPJ", "CPF", "idEstrangeiro"):
            if chave in self.destinatario:
                saida[f"dest.{chave}"] = self.destinatario[chave]
        return saida

    def para_dicionario(self) -> dict[str, Any]:
        return {
            "origem": self.origem,
            "tipo": self.tipo,
            "nome_arquivo": self.nome_arquivo,
            "chave": self.chave,
            "modelo": self.modelo,
            "serie": self.serie,
            "numero": self.numero,
            "data_emissao": self.data_emissao,
            "identificacao": self.identificacao,
            "emitente": self.emitente,
            "destinatario": self.destinatario,
            "quantidade_itens": len(self.itens),
            "totais": self.totais,
            "avisos": self.avisos,
        }


# --------------------------------------------------------------------------- #
#  Parse — ponto de entrada
# --------------------------------------------------------------------------- #
def parse_documento(conteudo: bytes | str, origem: str, nome_arquivo: str = "") -> DocumentoFiscal:
    """
    Lê o XML e devolve um :class:`DocumentoFiscal`.

    ``origem`` é apenas um rótulo ("cliente" ou "senior") usado nos relatórios.
    """
    if isinstance(conteudo, str):
        conteudo = conteudo.encode("utf-8")

    # Remove BOM e espaços antes do prólogo (comum em XMLs exportados no Windows).
    conteudo = conteudo.lstrip(b"\xef\xbb\xbf").strip()
    if not conteudo:
        raise ErroDeParse("Arquivo vazio.")

    try:
        raiz = ET.fromstring(conteudo)
    except ET.ParseError as exc:
        raise ErroDeParse(f"XML malformado: {exc}") from exc

    if _descendente(raiz, "infNFe") is not None:
        return _parse_nfe(raiz, origem, nome_arquivo)
    if _descendente(raiz, "infNFSe") is not None or _descendente(raiz, "infDPS") is not None:
        return _parse_nfse(raiz, origem, nome_arquivo)

    raise ErroDeParse(
        "Não foi possível identificar o layout. Esperado NF-e/NFC-e (infNFe) ou "
        f"NFS-e nacional (infNFSe/infDPS); o elemento raiz é '{_nome(raiz)}'."
    )


# --------------------------------------------------------------------------- #
#  NF-e / NFC-e
# --------------------------------------------------------------------------- #
def _parse_nfe(raiz: ET.Element, origem: str, nome_arquivo: str) -> DocumentoFiscal:
    inf = _descendente(raiz, "infNFe")
    if inf is None:  # pragma: no cover — guardado por parse_documento
        raise ErroDeParse("Elemento infNFe não encontrado.")

    doc = DocumentoFiscal(origem=origem, nome_arquivo=nome_arquivo)

    chave = (inf.get("Id") or "").replace("NFe", "").strip()
    doc.chave = chave

    ide = _filho(inf, "ide")
    doc.ide = _achatar(ide) if ide is not None else {}
    doc.modelo = doc.ide.get("mod", "")
    doc.serie = doc.ide.get("serie", "")
    doc.numero = doc.ide.get("nNF", "")
    doc.data_emissao = doc.ide.get("dhEmi", "") or doc.ide.get("dEmi", "")
    doc.tipo = "NFCe" if doc.modelo == "65" else "NFe"

    emit = _filho(inf, "emit")
    if emit is not None:
        doc.emitente = _achatar(emit)
    dest = _filho(inf, "dest")
    if dest is not None:
        doc.destinatario = _achatar(dest)

    for det in _filhos(inf, "det"):
        doc.itens.append(_parse_item_nfe(det))

    total = _filho(inf, "total")
    if total is not None:
        for grupo in GRUPOS_TOTAIS:
            no = _filho(total, grupo)
            if no is not None:
                doc.totais[grupo] = _achatar(no)

    pag = _filho(inf, "pag")
    if pag is not None:
        for det_pag in _filhos(pag, "detPag"):
            doc.pagamentos.append(_achatar(det_pag))

    inf_adic = _filho(inf, "infAdic")
    if inf_adic is not None:
        doc.informacoes_adicionais = _achatar(inf_adic)

    if not doc.itens:
        doc.avisos.append("O documento não possui itens (det).")

    return doc


def _parse_item_nfe(det: ET.Element) -> ItemNota:
    numero_txt = det.get("nItem") or "0"
    try:
        numero = int(numero_txt)
    except ValueError:
        numero = 0

    item = ItemNota(numero=numero)

    prod = _filho(det, "prod")
    if prod is not None:
        item.codigo = _texto(prod, "cProd")
        item.ean = _texto(prod, "cEAN")
        item.descricao = _texto(prod, "xProd")
        item.ncm = _texto(prod, "NCM")
        item.nve = _texto(prod, "NVE")
        item.cest = _texto(prod, "CEST")
        item.cfop = _texto(prod, "CFOP")
        item.unidade = _texto(prod, "uCom")
        item.quantidade = _texto(prod, "qCom")
        item.valor_unitario = _texto(prod, "vUnCom")
        item.valor_produto = _texto(prod, "vProd")
        item.valor_desconto = _texto(prod, "vDesc")
        item.valor_frete = _texto(prod, "vFrete")
        item.valor_seguro = _texto(prod, "vSeg")
        item.valor_outros = _texto(prod, "vOutro")
        item.ind_total = _texto(prod, "indTot")
        item.cbenef = _texto(prod, "cBenef")

    imposto = _filho(det, "imposto")
    if imposto is not None:
        item.impostos = _extrair_impostos(imposto)

    inf_ad_prod = _filho(det, "infAdProd")
    if inf_ad_prod is not None:
        item.informacoes_adicionais = (inf_ad_prod.text or "").strip()

    return item


def _extrair_impostos(imposto: ET.Element) -> dict[str, dict[str, str]]:
    """
    Achata cada grupo de imposto do item.

    Grupos como ICMS/PIS/COFINS/IPI possuem um nó intermediário que identifica a
    regra (ICMS00, ICMSSN102, PISAliq, IPITrib...). Esse nó **não** entra no
    caminho dos campos — assim ``CST`` é comparável entre notas com regras
    diferentes — mas fica registrado em ``_variante``, que por si só já é uma
    divergência relevante.
    """
    saida: dict[str, dict[str, str]] = {}

    for nome_grupo in GRUPOS_IMPOSTO:
        no = _filho(imposto, nome_grupo)
        if no is None:
            continue

        # Nó de variante: um filho que também é grupo e cujo nome começa com o
        # nome do grupo (ICMS→ICMS20, PIS→PISAliq, IPI→IPITrib/IPINT…).
        # Ele é REMOVIDO do caminho dos campos para que `CST` seja comparável
        # entre notas que usaram regras diferentes — sem isso, `IPINT.CST` e
        # `IPITrib.CST` viram dois achados distintos quando são o mesmo campo.
        # A troca da regra em si fica registrada em `_variante`.
        variante = None
        for filho in no:
            if len(filho) and _nome(filho).startswith(nome_grupo):
                variante = filho
                break

        if variante is None:
            dados = _achatar(no)
        else:
            # Irmãos do nó de variante (ex.: cEnq/CNPJProd do IPI) ficam no
            # nível do grupo; os campos da variante entram sem o prefixo dela.
            dados = {}
            for filho in no:
                if filho is variante:
                    continue
                if len(filho):
                    dados.update(_achatar(filho, prefixo=f"{_nome(filho)}."))
                else:
                    dados[_nome(filho)] = (filho.text or "").strip()
            dados.update(_achatar(variante))
            dados["_variante"] = _nome(variante)

        saida[nome_grupo] = dados

    # vTotTrib fica solto dentro de <imposto>.
    v_tot_trib = _filho(imposto, "vTotTrib")
    if v_tot_trib is not None:
        saida.setdefault("TOTAL", {})["vTotTrib"] = (v_tot_trib.text or "").strip()

    return saida


# --------------------------------------------------------------------------- #
#  NFS-e nacional (suporte básico)
# --------------------------------------------------------------------------- #
def _parse_nfse(raiz: ET.Element, origem: str, nome_arquivo: str) -> DocumentoFiscal:
    doc = DocumentoFiscal(origem=origem, nome_arquivo=nome_arquivo, tipo="NFSe")
    doc.avisos.append(
        "Documento lido como NFS-e nacional. A cobertura de campos é menor que a "
        "de NF-e; confira as divergências de ISSQN manualmente."
    )

    inf_nfse = _descendente(raiz, "infNFSe")
    inf_dps = _descendente(raiz, "infDPS")
    base = inf_nfse if inf_nfse is not None else inf_dps
    if base is None:  # pragma: no cover
        raise ErroDeParse("Nem infNFSe nem infDPS encontrados.")

    doc.chave = (base.get("Id") or "").strip()
    doc.numero = _texto(base, "nNFSe") or _texto(base, "nDPS")
    doc.serie = _texto(base, "serie")
    doc.data_emissao = _texto(base, "dhEmi") or _texto(base, "dhProc")

    prest = _filho(base, "prest") or _descendente(base, "emit")
    if prest is not None:
        doc.emitente = _achatar(prest)
    toma = _filho(base, "toma")
    if toma is not None:
        doc.destinatario = _achatar(toma)

    serv = _descendente(base, "serv")
    valores = _descendente(base, "valores")
    trib = _descendente(base, "trib")

    item = ItemNota(numero=1)
    if serv is not None:
        campos = _achatar(serv)
        item.descricao = campos.get("cServ.xDescServ", "") or campos.get("xDescServ", "")
        item.codigo = campos.get("cServ.cTribNac", "") or campos.get("cTribNac", "")
        item.cfop = campos.get("cServ.cTribMun", "")
        item.impostos.setdefault("SERVICO", {}).update(campos)
    if valores is not None:
        campos = _achatar(valores)
        item.valor_produto = campos.get("vServPrest.vServ", "") or campos.get("vServ", "")
        item.impostos.setdefault("VALORES", {}).update(campos)
    if trib is not None:
        campos = _achatar(trib)
        item.impostos["ISSQN"] = campos

    doc.itens.append(item)

    total = _descendente(base, "valoresNFSe")
    if total is not None:
        doc.totais["NFSeTot"] = _achatar(total)

    return doc


# --------------------------------------------------------------------------- #
#  Utilitário para a camada web
# --------------------------------------------------------------------------- #
_RE_ARQUIVO_XML = re.compile(r"\.xml$", re.IGNORECASE)


def parece_xml(nome_arquivo: str) -> bool:
    return bool(_RE_ARQUIVO_XML.search(nome_arquivo or ""))
