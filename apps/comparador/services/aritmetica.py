"""
Conferência aritmética de uma NF-e — sem legislação, sem tabela, sem modelo.

Boa parte do que se chama de "imposto errado" é, na verdade, **incoerência
interna da própria nota**: a base vezes a alíquota não bate com o valor
destacado, a soma dos itens não bate com o total, o valor da nota não fecha com
suas parcelas. Isso é verificável só com o XML, e tem três propriedades que
nenhuma outra camada tem:

* **não depende de nada externo** — nem de tabela, nem de provedor de IA;
* **nunca fica desatualizado** — aritmética não muda com decreto;
* **é reprodutível** — a mesma nota dá sempre o mesmo resultado.

Por isso esta camada roda ANTES de qualquer outra e seu resultado é entregue
pronto ao modelo: o LLM explica e contextualiza, mas não faz a conta.

## Sobre arredondamento

A legislação manda arredondar em duas casas, e cada software faz isso num
momento diferente do cálculo — daí divergências de centavos que NÃO são erro.
Aceitamos uma tolerância por item e uma tolerância proporcional nos somatórios;
o que passa disso é diferença real, não arredondamento.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal, InvalidOperation

#: Diferença tolerada num valor individual. Um centavo cobre a divergência
#: legítima de arredondamento entre dois softwares.
TOLERANCIA_ITEM = Decimal("0.01")

#: Em somatórios o erro de arredondamento se acumula: com N itens, N centavos
#: ainda podem ser arredondamento honesto. O piso de 1 centavo evita que uma
#: nota de item único fique sem folga nenhuma.
def tolerancia_soma(quantidade_itens: int) -> Decimal:
    return max(Decimal("0.01"), Decimal(quantidade_itens) * TOLERANCIA_ITEM)


@dataclass
class Achado:
    """
    Uma divergência aritmética.

    ``esperado`` e ``encontrado`` ficam explícitos para o operador conferir na
    mão — e para o modelo redigir a explicação sem precisar recalcular nada.
    """

    escopo: str          # "item 3" | "totais"
    campo: str           # "vICMS"
    titulo: str
    esperado: Decimal
    encontrado: Decimal
    formula: str
    severidade: str = "alta"   # alta | media

    @property
    def diferenca(self) -> Decimal:
        return (self.encontrado - self.esperado).quantize(Decimal("0.01"))

    def para_dicionario(self) -> dict:
        return {
            "escopo": self.escopo,
            "campo": self.campo,
            "titulo": self.titulo,
            "esperado": str(self.esperado),
            "encontrado": str(self.encontrado),
            "diferenca": str(self.diferenca),
            "formula": self.formula,
            "severidade": self.severidade,
        }


@dataclass
class Conferencia:
    achados: list[Achado] = field(default_factory=list)
    verificacoes: int = 0
    #: Campos que não puderam ser conferidos por ausência de dado no XML.
    nao_verificado: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.achados

    def para_dicionario(self) -> dict:
        return {
            "ok": self.ok,
            "verificacoes": self.verificacoes,
            "total_achados": len(self.achados),
            "achados": [a.para_dicionario() for a in self.achados],
            "nao_verificado": self.nao_verificado,
        }


def _dec(valor) -> Decimal | None:
    """
    Converte o texto do XML em Decimal.

    Decimal e não float: 0.1 + 0.2 em float não dá 0.3, e aqui estamos
    conferindo centavo. Devolve None quando o campo não existe ou não é
    numérico — ausência de dado não é zero.
    """
    if valor is None or valor == "":
        return None
    try:
        return Decimal(str(valor).strip().replace(",", "."))
    except (InvalidOperation, ValueError, AttributeError):
        return None


def _centavos(valor: Decimal) -> Decimal:
    return valor.quantize(Decimal("0.01"))


def _conferir(
    conf: Conferencia,
    *,
    escopo: str,
    campo: str,
    titulo: str,
    esperado: Decimal | None,
    encontrado: Decimal | None,
    formula: str,
    tolerancia: Decimal = TOLERANCIA_ITEM,
    severidade: str = "alta",
) -> None:
    """Compara um valor calculado com o declarado, respeitando a tolerância."""
    if esperado is None or encontrado is None:
        return
    conf.verificacoes += 1
    esperado = _centavos(esperado)
    if abs(encontrado - esperado) > tolerancia:
        conf.achados.append(
            Achado(
                escopo=escopo,
                campo=campo,
                titulo=titulo,
                esperado=esperado,
                encontrado=_centavos(encontrado),
                formula=formula,
                severidade=severidade,
            )
        )


def _conferir_percentual(
    conf: Conferencia,
    *,
    escopo: str,
    grupo: dict,
    campo_base: str,
    campo_aliquota: str,
    campo_valor: str,
    rotulo: str,
) -> None:
    """
    base × alíquota ÷ 100 = valor.

    Vale para ICMS, IPI, PIS e COFINS — todos seguem a mesma forma, mudando só
    o nome dos campos.
    """
    base = _dec(grupo.get(campo_base))
    aliquota = _dec(grupo.get(campo_aliquota))
    valor = _dec(grupo.get(campo_valor))

    if base is None or aliquota is None or valor is None:
        return

    esperado = base * aliquota / Decimal(100)
    _conferir(
        conf,
        escopo=escopo,
        campo=campo_valor,
        titulo=f"{rotulo}: valor não corresponde à base e à alíquota declaradas",
        esperado=esperado,
        encontrado=valor,
        formula=f"{base} × {aliquota}% = {_centavos(esperado)}",
    )


# --------------------------------------------------------------------------- #
#  Itens
# --------------------------------------------------------------------------- #
def _conferir_item(conf: Conferencia, item) -> None:
    escopo = f"item {item.numero}"

    # Quantidade × unitário = total do produto. É a conta mais básica da nota e,
    # quando falha, costuma indicar erro de digitação ou conversão de unidade.
    quantidade = _dec(item.quantidade)
    unitario = _dec(item.valor_unitario)
    produto = _dec(item.valor_produto)
    if quantidade is not None and unitario is not None and produto is not None:
        esperado = quantidade * unitario
        # A tolerância aqui é maior: o XML permite até 10 casas no unitário, e o
        # produto é arredondado em 2 — a diferença cresce com a quantidade.
        _conferir(
            conf,
            escopo=escopo,
            campo="vProd",
            titulo="Valor do produto não corresponde a quantidade × valor unitário",
            esperado=esperado,
            encontrado=produto,
            formula=f"{quantidade} × {unitario} = {_centavos(esperado)}",
            tolerancia=max(TOLERANCIA_ITEM, abs(esperado) * Decimal("0.0001")),
        )

    impostos = item.impostos or {}
    icms = impostos.get("ICMS") or {}
    ipi = impostos.get("IPI") or {}
    pis = impostos.get("PIS") or {}
    cofins = impostos.get("COFINS") or {}

    _conferir_percentual(conf, escopo=escopo, grupo=icms, campo_base="vBC",
                         campo_aliquota="pICMS", campo_valor="vICMS", rotulo="ICMS")
    _conferir_percentual(conf, escopo=escopo, grupo=icms, campo_base="vBCST",
                         campo_aliquota="pICMSST", campo_valor="vICMSST", rotulo="ICMS-ST")
    _conferir_percentual(conf, escopo=escopo, grupo=ipi, campo_base="vBC",
                         campo_aliquota="pIPI", campo_valor="vIPI", rotulo="IPI")
    _conferir_percentual(conf, escopo=escopo, grupo=pis, campo_base="vBC",
                         campo_aliquota="pPIS", campo_valor="vPIS", rotulo="PIS")
    _conferir_percentual(conf, escopo=escopo, grupo=cofins, campo_base="vBC",
                         campo_aliquota="pCOFINS", campo_valor="vCOFINS", rotulo="COFINS")

    # Redução de base: a base declarada tem que refletir o percentual de redução.
    reducao = _dec(icms.get("pRedBC"))
    base_icms = _dec(icms.get("vBC"))
    if reducao is not None and base_icms is not None and produto is not None and reducao > 0:
        esperado = produto * (Decimal(100) - reducao) / Decimal(100)
        _conferir(
            conf,
            escopo=escopo,
            campo="vBC",
            titulo="Base de ICMS não reflete o percentual de redução declarado",
            esperado=esperado,
            encontrado=base_icms,
            formula=f"{produto} × (100 − {reducao})% = {_centavos(esperado)}",
            severidade="media",  # frete/despesas legitimamente compõem a base
        )


# --------------------------------------------------------------------------- #
#  Totais
# --------------------------------------------------------------------------- #
#: (campo do total, nome no grupo do item, grupo do imposto, rótulo)
SOMATORIOS = [
    ("vProd", "valor_produto", None, "produtos"),
    ("vICMS", "vICMS", "ICMS", "ICMS"),
    ("vST", "vICMSST", "ICMS", "ICMS-ST"),
    ("vIPI", "vIPI", "IPI", "IPI"),
    ("vPIS", "vPIS", "PIS", "PIS"),
    ("vCOFINS", "vCOFINS", "COFINS", "COFINS"),
]


def _somar_itens(itens, campo: str, grupo: str | None) -> Decimal | None:
    """Soma um campo em todos os itens. None quando nenhum item o declara."""
    total = Decimal(0)
    achou = False
    for item in itens:
        if grupo is None:
            valor = _dec(getattr(item, campo, None))
        else:
            valor = _dec((item.impostos or {}).get(grupo, {}).get(campo))
        if valor is not None:
            total += valor
            achou = True
    return total if achou else None


def _conferir_totais(conf: Conferencia, doc) -> None:
    totais = (doc.totais or {}).get("ICMSTot") or {}
    if not totais:
        conf.nao_verificado.append("Totais da nota (grupo ICMSTot ausente)")
        return

    tolerancia = tolerancia_soma(len(doc.itens))

    for campo_total, campo_item, grupo, rotulo in SOMATORIOS:
        declarado = _dec(totais.get(campo_total))
        somado = _somar_itens(doc.itens, campo_item, grupo)
        _conferir(
            conf,
            escopo="totais",
            campo=campo_total,
            titulo=f"Total de {rotulo} não bate com a soma dos itens",
            esperado=somado,
            encontrado=declarado,
            formula=f"soma dos {len(doc.itens)} itens = {_centavos(somado)}" if somado is not None else "",
            tolerancia=tolerancia,
        )

    # Composição do valor da nota. O ICMS próprio NÃO entra: ele é imposto por
    # dentro, já embutido no valor do produto. Somam-se ST, IPI e as despesas
    # acessórias, e subtrai-se o desconto.
    componentes = {
        "vProd": _dec(totais.get("vProd")),
        "vST": _dec(totais.get("vST")),
        "vIPI": _dec(totais.get("vIPI")),
        "vFrete": _dec(totais.get("vFrete")),
        "vSeg": _dec(totais.get("vSeg")),
        "vOutro": _dec(totais.get("vOutro")),
        "vDesc": _dec(totais.get("vDesc")),
    }
    nota = _dec(totais.get("vNF"))

    if componentes["vProd"] is not None and nota is not None:
        z = Decimal(0)
        esperado = (
            componentes["vProd"]
            + (componentes["vST"] or z)
            + (componentes["vIPI"] or z)
            + (componentes["vFrete"] or z)
            + (componentes["vSeg"] or z)
            + (componentes["vOutro"] or z)
            - (componentes["vDesc"] or z)
        )
        _conferir(
            conf,
            escopo="totais",
            campo="vNF",
            titulo="Valor total da nota não fecha com suas parcelas",
            esperado=esperado,
            encontrado=nota,
            formula="vProd + vST + vIPI + vFrete + vSeg + vOutro − vDesc",
            tolerancia=tolerancia,
        )


# --------------------------------------------------------------------------- #
#  Entrada pública
# --------------------------------------------------------------------------- #
def conferir_aritmetica(doc) -> Conferencia:
    """
    Confere a coerência numérica interna de um ``DocumentoFiscal``.

    Não julga se a alíquota aplicada é a correta perante a legislação — isso
    depende de tabela e de contexto. Julga apenas se as contas da nota fecham
    entre si, o que é verdade ou mentira independente de qualquer norma.
    """
    conf = Conferencia()

    if not doc.itens:
        conf.nao_verificado.append("Itens da nota (nenhum item lido)")
        return conf

    for item in doc.itens:
        _conferir_item(conf, item)

    _conferir_totais(conf, doc)
    return conf
