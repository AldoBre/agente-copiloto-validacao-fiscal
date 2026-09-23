"""
Motor de comparação fiscal — 100% determinístico, sem IA.

Recebe dois :class:`DocumentoFiscal` (o do sistema atual do cliente e o gerado
pelo ERP Senior) e devolve a lista de divergências dos campos de imposto,
classificadas por severidade e já anotadas com a pista de parametrização.

O resultado deste módulo é o insumo do agente de IA — a IA **não** decide o que
está divergente, ela só explica como corrigir.
"""
from __future__ import annotations

import re
import unicodedata
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from decimal import Decimal
from typing import Any, Iterable

from .mapa_campos import (
    ALTA,
    BAIXA,
    CAMPOS_FISCAIS_DO_PRODUTO,
    CRITICA,
    GRUPOS_FORA_DO_ESCOPO_FISCAL,
    GRUPOS_IMPOSTO_COMPARAVEIS,
    MEDIA,
    ORDEM_SEVERIDADE,
    ROTULO_SEVERIDADE,
    campo_do_escopo_fiscal,
    categoria_do_grupo,
    pista_de_parametrizacao,
    severidade_do_campo,
    tipo_do_campo,
    titulo_da_divergencia,
)
from .parser_nfe import DocumentoFiscal, ItemNota, para_decimal

try:  # permite usar o módulo fora do Django (testes, scripts)
    from django.conf import settings

    _CFG = getattr(settings, "COMPARADOR", {})
except Exception:  # pragma: no cover
    _CFG = {}

TOLERANCIA_MONETARIA = Decimal(str(_CFG.get("TOLERANCIA_MONETARIA", 0.01)))
TOLERANCIA_PERCENTUAL = Decimal(str(_CFG.get("TOLERANCIA_PERCENTUAL", 0.01)))

#: ``impostos`` (padrão) → só grupos de imposto + classificação fiscal do item.
#: ``completo``          → também cabeçalho, totais e campos comerciais.
ESCOPO_IMPOSTOS = "impostos"
ESCOPO_COMPLETO = "completo"
ESCOPO_PADRAO = _CFG.get("ESCOPO", ESCOPO_IMPOSTOS)

# Tipos de divergência
DIVERGENTE = "valor_divergente"
AUSENTE_CLIENTE = "ausente_no_cliente"
AUSENTE_SENIOR = "ausente_no_senior"
GRUPO_AUSENTE_CLIENTE = "grupo_ausente_no_cliente"
GRUPO_AUSENTE_SENIOR = "grupo_ausente_no_senior"
ITEM_AUSENTE_CLIENTE = "item_ausente_no_cliente"
ITEM_AUSENTE_SENIOR = "item_ausente_no_senior"

ROTULO_TIPO = {
    DIVERGENTE: "Valor divergente",
    AUSENTE_CLIENTE: "Não informado no XML do cliente",
    AUSENTE_SENIOR: "Não informado no XML da Senior",
    GRUPO_AUSENTE_CLIENTE: "Grupo de imposto ausente no XML do cliente",
    GRUPO_AUSENTE_SENIOR: "Grupo de imposto ausente no XML da Senior",
    ITEM_AUSENTE_CLIENTE: "Item existe só no XML da Senior",
    ITEM_AUSENTE_SENIOR: "Item existe só no XML do cliente",
}

#: Campos ignorados na comparação — variam legitimamente entre sistemas.
CAMPOS_IGNORADOS = {
    "cNF",  # código numérico aleatório da chave
    "cDV",
    "dhEmi",
    "dhSaiEnt",
    "dEmi",
    "dSaiEnt",
    "nNF",
    "chNFe",
    "Id",
    "verProc",
    "procEmi",
    "nProt",
    "dhRecbto",
    "digVal",
    "nItemPed",
    "xPed",
    # Identificação do produto. O código e a descrição vêm do cadastro de cada
    # sistema e divergem por natureza ("PRD-001" × "000001", "CHAPA ACO 2MM" ×
    # "Chapa de aço galvanizado 2,00mm") sem que nada esteja mal parametrizado.
    # Eles servem para *parear* o item entre as duas notas — ver `parear_itens` —
    # nunca como divergência.
    "cProd",
    "xProd",
}


# --------------------------------------------------------------------------- #
#  Estruturas de saída
# --------------------------------------------------------------------------- #
@dataclass
class Divergencia:
    categoria: str
    grupo: str
    campo: str
    caminho: str
    escopo: str  # "documento" | "item" | "totais"
    tipo: str
    severidade: str
    valor_cliente: str
    valor_senior: str
    diferenca: str = ""
    item_numero: int | None = None
    item_codigo: str = ""
    item_descricao: str = ""
    pista: str = ""
    titulo: str = ""

    @property
    def severidade_rotulo(self) -> str:
        return ROTULO_SEVERIDADE.get(self.severidade, self.severidade)

    def para_dicionario(self) -> dict[str, Any]:
        dados = asdict(self)
        dados["severidade_rotulo"] = self.severidade_rotulo
        dados["tipo_rotulo"] = ROTULO_TIPO.get(self.tipo, self.tipo)
        if not dados.get("titulo"):
            dados["titulo"] = titulo_da_divergencia(self.grupo, self.campo, self.tipo)
        return dados


@dataclass
class ResultadoComparacao:
    documento_cliente: dict[str, Any]
    documento_senior: dict[str, Any]
    divergencias: list[Divergencia] = field(default_factory=list)
    pareamento: list[dict[str, Any]] = field(default_factory=list)
    avisos: list[str] = field(default_factory=list)
    gerado_em: str = ""
    escopo: str = ""

    # ------------------------------------------------------------------ util
    def ordenar(self) -> None:
        self.divergencias.sort(
            key=lambda d: (
                ORDEM_SEVERIDADE.get(d.severidade, 9),
                d.item_numero if d.item_numero is not None else -1,
                d.categoria,
                d.campo,
            )
        )

    @property
    def conforme(self) -> bool:
        return not any(d.severidade in (CRITICA, ALTA) for d in self.divergencias)

    def resumo(self) -> dict[str, Any]:
        por_severidade = {s: 0 for s in (CRITICA, ALTA, MEDIA, BAIXA)}
        por_categoria: dict[str, int] = {}
        itens_afetados: set[int] = set()

        for d in self.divergencias:
            por_severidade[d.severidade] = por_severidade.get(d.severidade, 0) + 1
            por_categoria[d.categoria] = por_categoria.get(d.categoria, 0) + 1
            if d.item_numero is not None:
                itens_afetados.add(d.item_numero)

        return {
            "total_divergencias": len(self.divergencias),
            "por_severidade": por_severidade,
            "por_categoria": dict(
                sorted(por_categoria.items(), key=lambda kv: kv[1], reverse=True)
            ),
            "itens_pareados": sum(1 for p in self.pareamento if p["tipo"] == "pareado"),
            "itens_somente_cliente": [
                p for p in self.pareamento if p["tipo"] == "somente_cliente"
            ],
            "itens_somente_senior": [p for p in self.pareamento if p["tipo"] == "somente_senior"],
            "itens_afetados": sorted(itens_afetados),
            "conforme": self.conforme,
        }

    def para_dicionario(self) -> dict[str, Any]:
        self.ordenar()
        return {
            "gerado_em": self.gerado_em,
            "escopo": self.escopo,
            "documentos": {"cliente": self.documento_cliente, "senior": self.documento_senior},
            "resumo": self.resumo(),
            "divergencias": [d.para_dicionario() for d in self.divergencias],
            "pareamento": self.pareamento,
            "avisos": self.avisos,
        }


# --------------------------------------------------------------------------- #
#  Normalização e comparação de valores
# --------------------------------------------------------------------------- #
_RE_ESPACOS = re.compile(r"\s+")


def _normalizar_texto(valor: str) -> str:
    texto = _RE_ESPACOS.sub(" ", (valor or "").strip())
    texto = unicodedata.normalize("NFKD", texto)
    return "".join(c for c in texto if not unicodedata.combining(c)).casefold()


def _vazio(valor: str | None) -> bool:
    return valor is None or str(valor).strip() == ""


def comparar_valores(
    valor_a: str, valor_b: str, tipo: str
) -> tuple[bool, str]:
    """
    Compara dois valores conforme o tipo do campo.

    Devolve ``(iguais, descricao_da_diferenca)``.
    """
    a, b = (valor_a or "").strip(), (valor_b or "").strip()

    if a == b:
        return True, ""

    if tipo in ("monetario", "percentual", "quantidade"):
        da, db = para_decimal(a), para_decimal(b)
        if da is not None and db is not None:
            if tipo == "monetario":
                tolerancia = TOLERANCIA_MONETARIA
            elif tipo == "percentual":
                tolerancia = TOLERANCIA_PERCENTUAL
            else:
                tolerancia = Decimal("0.0001")
            delta = db - da
            if abs(delta) <= tolerancia:
                return True, ""
            sinal = "+" if delta > 0 else ""
            descricao = f"{sinal}{delta.normalize()}"
            if da != 0:
                percentual = (delta / abs(da)) * 100
                descricao += f" ({sinal}{percentual.quantize(Decimal('0.01'))}%)"
            return False, descricao
        # Um dos lados não é numérico → cai para comparação textual.

    if tipo == "texto":
        if _normalizar_texto(a) == _normalizar_texto(b):
            return True, ""

    return False, ""


# --------------------------------------------------------------------------- #
#  Pareamento de itens
# --------------------------------------------------------------------------- #
def _chave_codigo(item: ItemNota) -> str:
    return (item.codigo or "").strip().upper()


def _chave_ean(item: ItemNota) -> str:
    ean = (item.ean or "").strip().upper()
    return "" if ean in ("", "SEM GTIN", "SEMGTIN") else ean


def _chave_ncm_valor(item: ItemNota) -> str:
    valor = para_decimal(item.valor_produto)
    valor_txt = str(valor.quantize(Decimal("0.01"))) if valor is not None else ""
    return f"{(item.ncm or '').strip()}|{valor_txt}"


def _chave_descricao(item: ItemNota) -> str:
    return _normalizar_texto(item.descricao)


def parear_itens(
    itens_cliente: list[ItemNota], itens_senior: list[ItemNota]
) -> tuple[list[tuple[ItemNota, ItemNota, str]], list[ItemNota], list[ItemNota]]:
    """
    Pareia itens entre os dois documentos.

    Estratégia em cascata (a primeira que casar vence):
      1. código do produto (cProd)
      2. GTIN/EAN
      3. NCM + valor total do item
      4. descrição normalizada
      5. ordem (nItem) entre os que sobraram

    Devolve ``(pares, sobras_cliente, sobras_senior)``, onde cada par é
    ``(item_cliente, item_senior, criterio)``.
    """
    restantes_cliente = list(itens_cliente)
    restantes_senior = list(itens_senior)
    pares: list[tuple[ItemNota, ItemNota, str]] = []

    estrategias: list[tuple[str, Any]] = [
        ("codigo", _chave_codigo),
        ("ean", _chave_ean),
        ("ncm+valor", _chave_ncm_valor),
        ("descricao", _chave_descricao),
    ]

    for nome_criterio, funcao_chave in estrategias:
        if not restantes_cliente or not restantes_senior:
            break

        indice_senior: dict[str, list[ItemNota]] = {}
        for item in restantes_senior:
            chave = funcao_chave(item)
            if chave and chave.strip("|"):
                indice_senior.setdefault(chave, []).append(item)

        casados_cliente: list[ItemNota] = []
        casados_senior: list[ItemNota] = []
        for item in restantes_cliente:
            chave = funcao_chave(item)
            if not chave or not chave.strip("|"):
                continue
            candidatos = indice_senior.get(chave)
            if candidatos:
                par = candidatos.pop(0)
                pares.append((item, par, nome_criterio))
                casados_cliente.append(item)
                casados_senior.append(par)

        restantes_cliente = [i for i in restantes_cliente if i not in casados_cliente]
        restantes_senior = [i for i in restantes_senior if i not in casados_senior]

    # 5. Sobras na ordem original — só quando as duas listas sobraram iguais em
    #    tamanho; do contrário o pareamento posicional gera ruído.
    if restantes_cliente and restantes_senior and len(restantes_cliente) == len(restantes_senior):
        restantes_cliente.sort(key=lambda i: i.numero)
        restantes_senior.sort(key=lambda i: i.numero)
        for a, b in zip(restantes_cliente, restantes_senior):
            pares.append((a, b, "ordem"))
        restantes_cliente, restantes_senior = [], []

    pares.sort(key=lambda p: p[0].numero)
    return pares, restantes_cliente, restantes_senior


# --------------------------------------------------------------------------- #
#  Comparação de dicionários de campos
# --------------------------------------------------------------------------- #
def _comparar_mapa(
    campos_cliente: dict[str, str],
    campos_senior: dict[str, str],
    *,
    grupo: str,
    escopo: str,
    item: ItemNota | None = None,
    prefixo_caminho: str = "",
    ignorar: Iterable[str] = (),
    escopo_fiscal: bool = False,
) -> list[Divergencia]:
    ignorados = set(CAMPOS_IGNORADOS) | set(ignorar)
    divergencias: list[Divergencia] = []

    for campo in sorted(set(campos_cliente) | set(campos_senior)):
        folha = campo.rsplit(".", 1)[-1]
        if folha in ignorados:
            continue
        # No escopo fiscal entram a parametrização E o valor apurado de cada
        # imposto (o "10 vs 8" que o consultor enxerga primeiro). Só a
        # quantidade fica de fora — é volume da nota, não imposto.
        if escopo_fiscal and not campo_do_escopo_fiscal(campo):
            continue

        valor_cliente = campos_cliente.get(campo, "")
        valor_senior = campos_senior.get(campo, "")

        presente_cliente = campo in campos_cliente and not _vazio(valor_cliente)
        presente_senior = campo in campos_senior and not _vazio(valor_senior)

        if not presente_cliente and not presente_senior:
            continue

        tipo_campo = tipo_do_campo(campo)

        # Campo numérico ausente de um lado e zerado do outro é a mesma coisa —
        # `<pIPI>0</pIPI>` e a ausência da tag significam "sem IPI". Reportar
        # "(ausente) → 0" só gera ruído.
        if presente_cliente != presente_senior and tipo_campo in (
            "percentual",
            "monetario",
            "quantidade",
        ):
            valor_presente = valor_cliente if presente_cliente else valor_senior
            numero = para_decimal(valor_presente)
            if numero is not None and numero == 0:
                continue

        if presente_cliente and not presente_senior:
            tipo_div = AUSENTE_SENIOR
            iguais, diferenca = False, ""
        elif presente_senior and not presente_cliente:
            tipo_div = AUSENTE_CLIENTE
            iguais, diferenca = False, ""
        else:
            iguais, diferenca = comparar_valores(valor_cliente, valor_senior, tipo_campo)
            tipo_div = DIVERGENTE

        if iguais:
            continue

        severidade = severidade_do_campo(campo, grupo)
        # Campo ausente só de um lado é sempre pelo menos "alta": costuma ser
        # grupo/regra não parametrizado.
        if tipo_div in (AUSENTE_CLIENTE, AUSENTE_SENIOR) and severidade == MEDIA:
            severidade = ALTA

        divergencias.append(
            Divergencia(
                categoria=categoria_do_grupo(grupo) if grupo else "Cabeçalho",
                grupo=grupo,
                campo=campo,
                caminho=f"{prefixo_caminho}{campo}",
                escopo=escopo,
                tipo=tipo_div,
                severidade=severidade,
                valor_cliente=valor_cliente,
                valor_senior=valor_senior,
                diferenca=diferenca,
                item_numero=item.numero if item else None,
                item_codigo=item.codigo if item else "",
                item_descricao=item.descricao if item else "",
                pista=pista_de_parametrizacao(grupo, campo),
                titulo=titulo_da_divergencia(grupo, campo, tipo_div),
            )
        )

    return divergencias


def _filtrar_campos_fiscais(campos: dict[str, str]) -> dict[str, str]:
    """Do grupo <prod>, mantém só o que determina a tributação."""
    return {k: v for k, v in campos.items() if k in CAMPOS_FISCAIS_DO_PRODUTO}


def _comparar_item(
    item_cliente: ItemNota, item_senior: ItemNota, *, escopo: str = ESCOPO_PADRAO
) -> list[Divergencia]:
    divergencias: list[Divergencia] = []
    prefixo = f"det[{item_senior.numero or item_cliente.numero}]/"

    # ---- classificação fiscal do produto ----------------------------------
    # No escopo "impostos" ficam só CFOP/NCM/CEST/cBenef/NVE — unidade, quantidade
    # e valor do PRODUTO são dado comercial, não fiscal (o valor do IMPOSTO, esse
    # sim, entra, mas ele vive nos grupos de imposto abaixo). Código e descrição
    # (cProd/xProd) ficam de fora em qualquer escopo, via CAMPOS_IGNORADOS.
    campos_cliente = item_cliente.campos_produto()
    campos_senior = item_senior.campos_produto()
    if escopo == ESCOPO_IMPOSTOS:
        campos_cliente = _filtrar_campos_fiscais(campos_cliente)
        campos_senior = _filtrar_campos_fiscais(campos_senior)

    divergencias += _comparar_mapa(
        campos_cliente,
        campos_senior,
        grupo="PRODUTO",
        escopo="item",
        item=item_senior,
        prefixo_caminho=f"{prefixo}prod/",
        escopo_fiscal=escopo == ESCOPO_IMPOSTOS,
    )

    # ---- grupos de imposto ------------------------------------------------
    grupos = sorted(set(item_cliente.impostos) | set(item_senior.impostos))
    if escopo == ESCOPO_IMPOSTOS:
        grupos = [
            g
            for g in grupos
            if g in GRUPOS_IMPOSTO_COMPARAVEIS and g not in GRUPOS_FORA_DO_ESCOPO_FISCAL
        ]

    for grupo in grupos:
        campos_cliente = item_cliente.impostos.get(grupo)
        campos_senior = item_senior.impostos.get(grupo)

        if campos_cliente and not campos_senior:
            divergencias.append(
                Divergencia(
                    categoria=categoria_do_grupo(grupo),
                    grupo=grupo,
                    campo="_grupo",
                    caminho=f"{prefixo}imposto/{grupo}",
                    escopo="item",
                    tipo=GRUPO_AUSENTE_SENIOR,
                    severidade=CRITICA,
                    valor_cliente=campos_cliente.get("_variante", "presente"),
                    valor_senior="",
                    item_numero=item_senior.numero,
                    item_codigo=item_senior.codigo,
                    item_descricao=item_senior.descricao,
                    pista=(
                        f"O grupo {grupo} existe na nota do cliente e não foi gerado pela "
                        "Senior. Isso indica regra de tributação inexistente ou não "
                        "vinculada ao produto/operação."
                    ),
                    titulo=titulo_da_divergencia(grupo, "_grupo", GRUPO_AUSENTE_SENIOR),
                )
            )
            continue

        if campos_senior and not campos_cliente:
            divergencias.append(
                Divergencia(
                    categoria=categoria_do_grupo(grupo),
                    grupo=grupo,
                    campo="_grupo",
                    caminho=f"{prefixo}imposto/{grupo}",
                    escopo="item",
                    tipo=GRUPO_AUSENTE_CLIENTE,
                    severidade=CRITICA,
                    valor_cliente="",
                    valor_senior=campos_senior.get("_variante", "presente"),
                    item_numero=item_senior.numero,
                    item_codigo=item_senior.codigo,
                    item_descricao=item_senior.descricao,
                    pista=(
                        f"A Senior gerou o grupo {grupo} que a nota do cliente não possui. "
                        "Verifique se a regra de tributação está aplicando um imposto "
                        "indevido para esta operação."
                    ),
                    titulo=titulo_da_divergencia(grupo, "_grupo", GRUPO_AUSENTE_CLIENTE),
                )
            )
            continue

        divergencias += _fundir_variante_e_cst(
            _comparar_mapa(
                campos_cliente or {},
                campos_senior or {},
                grupo=grupo,
                escopo="item",
                item=item_senior,
                prefixo_caminho=f"{prefixo}imposto/{grupo}/",
                escopo_fiscal=escopo == ESCOPO_IMPOSTOS,
            )
        )

    return divergencias


def _fundir_variante_e_cst(divergencias: list[Divergencia]) -> list[Divergencia]:
    """
    ``_variante`` e ``CST``/``CSOSN`` divergindo juntos são **um** achado, não dois:
    trocar de ICMS00 para ICMS20 *é* trocar a CST de 00 para 20.

    Mantém a CST (o código que o consultor procura na parametrização) e anexa a
    troca de regra na descrição da diferença. Se só a variante mudou, ela fica.
    """
    codigo = next(
        (d for d in divergencias if d.campo in ("CST", "CSOSN") and d.tipo == DIVERGENTE), None
    )
    variante = next((d for d in divergencias if d.campo == "_variante"), None)

    if codigo is None or variante is None:
        return divergencias

    troca = f"regra {variante.valor_cliente or '(ausente)'} → {variante.valor_senior or '(ausente)'}"
    codigo.diferenca = f"{codigo.diferenca}; {troca}" if codigo.diferenca else troca
    return [d for d in divergencias if d is not variante]


# --------------------------------------------------------------------------- #
#  Ponto de entrada
# --------------------------------------------------------------------------- #
def comparar_documentos(
    doc_cliente: DocumentoFiscal,
    doc_senior: DocumentoFiscal,
    *,
    escopo: str = ESCOPO_PADRAO,
    analisar_itens_nao_simulados: bool = True,
) -> ResultadoComparacao:
    """
    Compara os dois documentos e devolve o resultado.

    ``escopo='impostos'`` (padrão) restringe a comparação aos grupos de imposto
    e à classificação fiscal do item. Dados cadastrais (CNPJ, razão social,
    IE), do documento (número, série, data, chave) e comerciais (quantidade,
    preço, valor da nota) **não são divergência fiscal** — eles servem apenas
    para o pareamento das notas.

    ``escopo='completo'`` inclui cabeçalho, totalizadores e campos comerciais.

    ``analisar_itens_nao_simulados=False`` deixa de apontar como divergência os
    itens que existem na nota do cliente e o Senior não emitiu. Numa validação
    de implantação é comum simular só parte dos itens: esses "faltantes" viram
    dezenas de achados CRÍTICOS que o consultor já sabe que não são erro, e que
    afogam as divergências reais de parametrização.

    O par continua registrado em ``pareamento`` como ``somente_cliente`` — o
    fato de o item não ter contraparte não deixa de ser verdade, só deixa de ser
    tratado como problema.
    """
    resultado = ResultadoComparacao(
        documento_cliente=doc_cliente.para_dicionario(),
        documento_senior=doc_senior.para_dicionario(),
        gerado_em=datetime.now(timezone.utc).isoformat(),
        escopo=escopo,
    )
    resultado.avisos.extend(doc_cliente.avisos)
    resultado.avisos.extend(doc_senior.avisos)

    if doc_cliente.tipo != doc_senior.tipo:
        resultado.avisos.append(
            f"Os documentos são de tipos diferentes ({doc_cliente.tipo} x {doc_senior.tipo}). "
            "A comparação prossegue, mas confira se os arquivos foram trocados."
        )

    # ---- cabeçalho --------------------------------------------------------
    if escopo != ESCOPO_IMPOSTOS:
        resultado.divergencias += _comparar_mapa(
            doc_cliente.campos_cabecalho(),
            doc_senior.campos_cabecalho(),
            grupo="",
            escopo="documento",
            prefixo_caminho="infNFe/",
        )

    # ---- itens ------------------------------------------------------------
    pares, sobras_cliente, sobras_senior = parear_itens(doc_cliente.itens, doc_senior.itens)

    for item_cliente, item_senior, criterio in pares:
        resultado.pareamento.append(
            {
                "tipo": "pareado",
                "criterio": criterio,
                "cliente": {
                    "numero": item_cliente.numero,
                    "codigo": item_cliente.codigo,
                    "descricao": item_cliente.descricao,
                },
                "senior": {
                    "numero": item_senior.numero,
                    "codigo": item_senior.codigo,
                    "descricao": item_senior.descricao,
                },
            }
        )
        resultado.divergencias += _comparar_item(item_cliente, item_senior, escopo=escopo)

    for item in sobras_cliente:
        resultado.pareamento.append(
            {
                "tipo": "somente_cliente",
                "criterio": "",
                "cliente": {
                    "numero": item.numero,
                    "codigo": item.codigo,
                    "descricao": item.descricao,
                },
                "senior": None,
            }
        )
        if not analisar_itens_nao_simulados:
            continue
        resultado.divergencias.append(
            Divergencia(
                categoria="Itens",
                grupo="PRODUTO",
                campo="_item",
                caminho=f"det[{item.numero}]",
                escopo="item",
                tipo=ITEM_AUSENTE_SENIOR,
                severidade=CRITICA,
                valor_cliente=item.rotulo,
                valor_senior="",
                item_numero=item.numero,
                item_codigo=item.codigo,
                item_descricao=item.descricao,
                pista=(
                    "Item presente na nota do cliente e ausente na nota da Senior. "
                    "Verifique o cadastro/vínculo do produto e se ele foi migrado."
                ),
                titulo=titulo_da_divergencia("PRODUTO", "_item", ITEM_AUSENTE_SENIOR),
            )
        )

    for item in sobras_senior:
        resultado.pareamento.append(
            {
                "tipo": "somente_senior",
                "criterio": "",
                "cliente": None,
                "senior": {
                    "numero": item.numero,
                    "codigo": item.codigo,
                    "descricao": item.descricao,
                },
            }
        )
        resultado.divergencias.append(
            Divergencia(
                categoria="Itens",
                grupo="PRODUTO",
                campo="_item",
                caminho=f"det[{item.numero}]",
                escopo="item",
                tipo=ITEM_AUSENTE_CLIENTE,
                severidade=CRITICA,
                valor_cliente="",
                valor_senior=item.rotulo,
                item_numero=item.numero,
                item_codigo=item.codigo,
                item_descricao=item.descricao,
                pista=(
                    "Item gerado pela Senior que não existe na nota do cliente. "
                    "Verifique itens automáticos (frete, brinde, composição de kit)."
                ),
                titulo=titulo_da_divergencia("PRODUTO", "_item", ITEM_AUSENTE_CLIENTE),
            )
        )

    # ---- totais -----------------------------------------------------------
    # Totalizadores são soma dos itens: divergir aqui é *consequência*, nunca
    # causa. No escopo fiscal eles ficam de fora para não duplicar o achado.
    if escopo != ESCOPO_IMPOSTOS:
        grupos_totais = sorted(set(doc_cliente.totais) | set(doc_senior.totais))
        for grupo in grupos_totais:
            resultado.divergencias += _comparar_mapa(
                doc_cliente.totais.get(grupo, {}),
                doc_senior.totais.get(grupo, {}),
                grupo=grupo,
                escopo="totais",
                prefixo_caminho=f"total/{grupo}/",
            )

    resultado.ordenar()
    return resultado
