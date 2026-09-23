"""
Classificação dos campos fiscais: categoria, severidade, tipo de dado e a
"pista de parametrização" — onde, no ERP Senior, o consultor deve olhar.

⚠️ Sobre as pistas
------------------
As pistas abaixo são descritas por **conceito de parametrização**, não por
código de tela, justamente para não chutar identificadores. Elas existem para
dar um ponto de partida determinístico ao consultor e para ancorar o prompt do
agente.

Elas são **enriquecíveis**: o modelo ``RegraParametrizacao`` (app conhecimento)
é semeado com este mesmo mapa e pode ser editado no /admin ou sobrescrito pelo
conteúdo raspado da documentação oficial. Quando existe regra cadastrada para
um campo, ela tem prioridade sobre o valor daqui.
"""
from __future__ import annotations

import re

# --------------------------------------------------------------------------- #
#  Severidades
# --------------------------------------------------------------------------- #
CRITICA = "critica"
ALTA = "alta"
MEDIA = "media"
BAIXA = "baixa"

ORDEM_SEVERIDADE = {CRITICA: 0, ALTA: 1, MEDIA: 2, BAIXA: 3}

ROTULO_SEVERIDADE = {
    CRITICA: "Crítica",
    ALTA: "Alta",
    MEDIA: "Média",
    BAIXA: "Baixa",
}

# --------------------------------------------------------------------------- #
#  Escopo da comparação
# --------------------------------------------------------------------------- #
#  O sistema compara **imposto**: a parametrização (CST, CFOP, NCM, alíquota…)
#  e o valor apurado de cada imposto (vICMS, vBC, vPIS…). Cadastro e dado
#  comercial — CNPJ, razão social, datas, número/série da nota, código de
#  barras, código/descrição/quantidade/valor do PRODUTO — são usados apenas
#  para PAREAR as notas (descobrir qual compara com qual) e nunca entram no
#  relatório de divergências. Valor do PRODUTO fica de fora; valor do IMPOSTO
#  entra — são coisas diferentes.
# --------------------------------------------------------------------------- #

#: Grupos de imposto dentro de <det><imposto>. É isto que é comparado.
GRUPOS_IMPOSTO_COMPARAVEIS = {
    "ICMS",
    "IPI",
    "II",
    "PIS",
    "PISST",
    "COFINS",
    "COFINSST",
    "ISSQN",
    "ICMSUFDest",
    "IBSCBS",
}

#: Campos de <prod> que definem a tributação do item. Não são "imposto", mas são
#: o que a regra fiscal usa para decidir o imposto — divergir aqui é divergência
#: fiscal, e normalmente é a causa raiz.
CAMPOS_FISCAIS_DO_PRODUTO = {
    "CFOP",
    "NCM",
    "NVE",
    "CEST",
    "EXTIPI",
    "cBenef",
}

#: Grupos deliberadamente fora da comparação no escopo "impostos".
#: ``TOTAL`` guarda o vTotTrib (tributos aproximados da Lei da Transparência),
#: que é estimativa da tabela IBPT e não parametrização fiscal.
GRUPOS_FORA_DO_ESCOPO_FISCAL = {"TOTAL", "SERVICO", "VALORES"}

#: Campos que começam com "v" mas são **alíquota**, não valor praticado:
#: ISS por percentual, PIS/COFINS por quantidade e IPI por unidade. Eles vêm da
#: parametrização e por isso entram na comparação.
ALIQUOTAS_COM_PREFIXO_V = {"vAliq", "vAliqProd", "vUnid"}


# --------------------------------------------------------------------------- #
#  Categorias
# --------------------------------------------------------------------------- #
CATEGORIA_POR_GRUPO = {
    "ICMS": "ICMS",
    "ICMSUFDest": "ICMS-DIFAL",
    "IPI": "IPI",
    "II": "II",
    "PIS": "PIS",
    "PISST": "PIS-ST",
    "COFINS": "COFINS",
    "COFINSST": "COFINS-ST",
    "ISSQN": "ISSQN",
    "IBSCBS": "IBS/CBS (reforma)",
    "TOTAL": "Totais do item",
    "SERVICO": "Serviço",
    "VALORES": "Valores do serviço",
    # Totalizadores da nota
    "ICMSTot": "Totais da nota",
    "ISSQNtot": "Totais de ISSQN",
    "retTrib": "Retenções",
    "IBSCBSTot": "Totais IBS/CBS",
    "NFSeTot": "Totais da NFS-e",
    "PRODUTO": "Produto",
}

# --------------------------------------------------------------------------- #
#  Campos estruturantes — divergiram, a nota inteira muda de tributação
# --------------------------------------------------------------------------- #
CAMPOS_CRITICOS = {
    "_variante",  # a regra tributária usada mudou (ICMS00 x ICMS20 etc.)
    "CST",
    "CSOSN",
    "CFOP",
    "NCM",
    "CEST",
    "orig",
    "cClassTrib",
    "modBC",
    "modBCST",
    "indIncentivo",
    "indPres",
    "indFinal",
    "tpNF",
    "idDest",
    "CRT",
    "indIEDest",
    "natOp",
    "cListServ",
    "cTribNac",
    "indISS",
}

#: Alíquotas — divergência aqui gera valor errado em todas as notas do CFOP.
_RE_ALIQUOTA = re.compile(r"^p[A-Z]")
#: Valores monetários.
_RE_MONETARIO = re.compile(r"^v[A-Z]")
#: Quantidades.
_RE_QUANTIDADE = re.compile(r"^q[A-Z]")

CAMPOS_INFORMATIVOS = {
    "xProd",
    "cEAN",
    "cEANTrib",
    "infAdProd",
    "infCpl",
    "infAdFisco",
    "xPed",
    "nItemPed",
    "cProd",
    "nFCI",
    "vTotTrib",
}


def tipo_do_campo(nome_campo: str) -> str:
    """Devolve ``codigo`` | ``percentual`` | ``monetario`` | ``quantidade`` | ``texto``."""
    folha = nome_campo.rsplit(".", 1)[-1]
    if folha in ALIQUOTAS_COM_PREFIXO_V:
        return "percentual"
    if folha in CAMPOS_CRITICOS or folha.startswith("C") and folha.isupper():
        return "codigo"
    if _RE_ALIQUOTA.match(folha):
        return "percentual"
    if _RE_MONETARIO.match(folha):
        return "monetario"
    if _RE_QUANTIDADE.match(folha):
        return "quantidade"
    return "texto"


def campo_do_escopo_fiscal(nome_campo: str) -> bool:
    """
    ``True`` para os campos que entram na comparação no escopo ``impostos``:
    a **parametrização** do imposto (CST, CFOP, NCM, alíquota, modalidade de
    base, benefício…) **e o valor apurado** de cada imposto (vBC, vICMS, vPIS…).

    Fica de fora só a **quantidade** (``qCom``, ``qBCProd``…): ela é o volume da
    nota, não parametrização nem imposto. Como a validação de implantação compara
    a **mesma** nota reemitida, a quantidade é idêntica por construção — divergir
    ali seria erro de digitação do teste, não de implantação.

    O valor apurado entra porque é o que o consultor enxerga primeiro ("o ICMS
    deu 10 aqui e 8 lá"). Ele é consequência de base × alíquota, então costuma
    aparecer junto da causa (alíquota/CST divergente); mas quando diverge
    **sozinho** — base de cálculo montada diferente, redução de base não
    parametrizada — é a única pista de que a composição do valor mudou, e antes
    esse caso era invisível.
    """
    return tipo_do_campo(nome_campo) != "quantidade"


def severidade_do_campo(nome_campo: str, grupo: str = "") -> str:
    folha = nome_campo.rsplit(".", 1)[-1]
    if folha in CAMPOS_CRITICOS:
        return CRITICA
    if folha in CAMPOS_INFORMATIVOS:
        return BAIXA
    tipo = tipo_do_campo(nome_campo)
    if tipo == "percentual":
        return CRITICA  # alíquota errada = imposto errado em toda a operação
    if tipo == "monetario":
        return ALTA
    if tipo == "quantidade":
        return MEDIA
    return MEDIA


def categoria_do_grupo(grupo: str) -> str:
    return CATEGORIA_POR_GRUPO.get(grupo, grupo or "Outros")


# --------------------------------------------------------------------------- #
#  Pistas de parametrização no ERP Senior
# --------------------------------------------------------------------------- #
#: Chave = "GRUPO.campo" ou apenas "campo" (fallback).
PISTAS: dict[str, str] = {
    # ---- Estrutura da operação -------------------------------------------
    "ide.natOp": (
        "Natureza de operação: descrição/finalidade divergente. Revise o cadastro de "
        "Natureza de Operação e a regra que a associa ao tipo de pedido/venda."
    ),
    "ide.tpNF": "Sentido da operação (entrada/saída) definido pela Natureza de Operação.",
    "ide.idDest": (
        "Destino da operação (interna/interestadual/exterior) é derivado da UF do "
        "emitente x UF do destinatário. Confira o endereço do cliente e do estabelecimento."
    ),
    "ide.indFinal": (
        "Indicador de consumidor final. Vem do cadastro do cliente (tipo/perfil) e "
        "influencia DIFAL e ICMS-ST."
    ),
    "ide.indPres": "Indicador de presença do comprador — parametrizado na Natureza de Operação.",
    "ide.finNFe": "Finalidade da NF-e (normal/complementar/ajuste/devolução) — Natureza de Operação.",
    "emit.CRT": (
        "Código de Regime Tributário do estabelecimento. Regime errado troca CST por "
        "CSOSN (e vice-versa) em todos os itens. Confira o cadastro do estabelecimento/filial."
    ),
    "dest.indIEDest": (
        "Indicador de contribuinte do destinatário. Vem do cadastro do cliente e "
        "determina ST, DIFAL e a própria CST aplicada."
    ),
    # ---- Produto ----------------------------------------------------------
    "NCM": (
        "Classificação fiscal (NCM) do produto. Corrija no cadastro do produto — a NCM "
        "é a chave que seleciona a regra de tributação, então ela erra 'em cascata'."
    ),
    "CEST": (
        "CEST do produto — obrigatório quando há substituição tributária. Ajuste no "
        "cadastro do produto / vínculo NCM-CEST."
    ),
    "CFOP": (
        "CFOP do item. É resultado da combinação Natureza de Operação + destino "
        "(interna/interestadual) + tipo de cliente + regra de tributação do produto. "
        "Revise a regra de determinação de CFOP antes de mexer no item."
    ),
    "uCom": "Unidade de medida comercial — cadastro do produto / conversão de unidades.",
    "cBenef": (
        "Código de benefício fiscal (cBenef). Cadastrado na regra de tributação/exceção "
        "fiscal por UF. Estado que exige e não recebe rejeita a nota."
    ),
    "indTot": "Indicador de composição do total da nota — parametrização do tipo de item.",
    # ---- ICMS -------------------------------------------------------------
    "ICMS._variante": (
        "A REGRA de ICMS aplicada é outra (ex.: tributado integralmente x redução de base "
        "x isento). Este é o achado mais importante: revise a regra de tributação de ICMS "
        "para a combinação NCM/produto + UF origem-destino + perfil do cliente."
    ),
    "ICMS.CST": (
        "CST de ICMS. Definida pela regra/exceção de tributação para a combinação "
        "produto + UF + finalidade da operação + perfil do destinatário."
    ),
    "ICMS.CSOSN": (
        "CSOSN (Simples Nacional). Verifique o CRT do estabelecimento e a regra de "
        "tributação do Simples para o produto."
    ),
    "ICMS.orig": "Origem da mercadoria (0-8) — cadastro do produto.",
    "ICMS.modBC": "Modalidade de determinação da base de cálculo — regra de tributação de ICMS.",
    "ICMS.pRedBC": (
        "Percentual de redução da base de ICMS. Cadastrado na exceção fiscal por "
        "NCM/produto e UF. Diferença aqui costuma ser benefício não parametrizado."
    ),
    "ICMS.pICMS": (
        "Alíquota de ICMS. Confira a alíquota interna da UF de destino, a alíquota "
        "interestadual e eventual exceção por produto."
    ),
    "ICMS.vBC": (
        "Base de cálculo de ICMS divergente. É consequência de modBC/pRedBC e da "
        "composição do valor — se a base mudou sem a alíquota mudar, procure "
        "redução de base ou inclusão de frete/desconto na regra de tributação."
    ),
    "ICMS.vICMS": (
        "Valor do ICMS divergente. É base × alíquota: confira antes a alíquota "
        "(pICMS) e a base (vBC) do item; o valor acompanha a causa."
    ),
    "ICMS.modBCST": "Modalidade da base de ST — regra de substituição tributária.",
    "ICMS.pMVAST": (
        "MVA/IVA-ST. Cadastrado por NCM/CEST e UF de destino, muitas vezes com MVA "
        "ajustada. Diferença aqui indica tabela de MVA desatualizada."
    ),
    "ICMS.pICMSST": "Alíquota de ICMS-ST (alíquota interna da UF de destino).",
    "ICMS.vBCST": "Base de ST — consequência de MVA + modalidade + composição do valor.",
    "ICMS.vICMSST": "Valor do ICMS-ST — consequência da base de ST.",
    "ICMS.pFCP": "Percentual do Fundo de Combate à Pobreza da UF de destino.",
    "ICMS.pFCPST": "Percentual de FCP retido por ST — tabela por UF de destino.",
    "ICMS.vICMSDeson": "Valor de ICMS desonerado — exige motivo (motDesICMS) coerente.",
    "ICMS.motDesICMS": (
        "Motivo da desoneração do ICMS. Precisa estar cadastrado junto com o benefício "
        "na exceção fiscal, senão a SEFAZ rejeita."
    ),
    "ICMS.pCredSN": "Percentual de crédito do Simples Nacional — parametrizado no regime da empresa.",
    "ICMS.vCredICMSSN": "Crédito de ICMS do Simples — consequência do pCredSN.",
    # ---- DIFAL ------------------------------------------------------------
    "ICMSUFDest.pICMSUFDest": "Alíquota interna da UF de destino usada no DIFAL.",
    "ICMSUFDest.pICMSInter": "Alíquota interestadual (4%/7%/12%) — depende da origem da mercadoria.",
    "ICMSUFDest.pFCPUFDest": "Percentual de FCP da UF de destino no DIFAL.",
    "ICMSUFDest.vBCUFDest": "Base do DIFAL — depende da regra de cálculo (base única/dupla) da UF.",
    # ---- IPI --------------------------------------------------------------
    "IPI._variante": "A regra de IPI mudou (tributado x não tributado). Revise a tributação de IPI do produto.",
    "IPI.CST": "CST de IPI — regra de tributação de IPI por NCM/produto.",
    "IPI.pIPI": "Alíquota de IPI — vem da TIPI pela NCM. Confira a tabela TIPI carregada.",
    "IPI.cEnq": "Código de enquadramento legal do IPI — obrigatório; cadastrado na regra de IPI.",
    "IPI.vBC": "Base de IPI — composição do valor do item conforme regra.",
    "IPI.vIPI": "Valor do IPI — consequência de base x alíquota.",
    # ---- PIS/COFINS -------------------------------------------------------
    "PIS._variante": "A regra de PIS mudou (alíquota x quantidade x não tributado x outras).",
    "PIS.CST": (
        "CST de PIS. Definida pela regra de tributação de PIS/COFINS para o produto e a "
        "operação (regime cumulativo/não cumulativo, monofásico, ST)."
    ),
    "PIS.pPIS": "Alíquota de PIS — regra de tributação PIS/COFINS.",
    "PIS.vBC": "Base de PIS — depende da CST e da composição do valor.",
    "PIS.vPIS": "Valor do PIS — consequência de base x alíquota.",
    "COFINS._variante": "A regra de COFINS mudou (alíquota x quantidade x não tributado x outras).",
    "COFINS.CST": "CST de COFINS — mesma regra de tributação que rege o PIS.",
    "COFINS.pCOFINS": "Alíquota de COFINS — regra de tributação PIS/COFINS.",
    "COFINS.vBC": "Base de COFINS — depende da CST e da composição do valor.",
    "COFINS.vCOFINS": "Valor da COFINS — consequência de base x alíquota.",
    # ---- ISSQN ------------------------------------------------------------
    "ISSQN.cListServ": "Item da lista de serviços (LC 116) — cadastro do serviço.",
    "ISSQN.vAliq": "Alíquota de ISS — cadastro por município + item da lista de serviços.",
    "ISSQN.cMunFG": "Município de incidência do ISS — regra de local da prestação.",
    "ISSQN.indISS": "Exigibilidade do ISS — regra de tributação do serviço.",
    "ISSQN.vISSQN": "Valor do ISS — consequência de base x alíquota.",
    "ISSQN.vBC": "Base do ISS — deduções e composição do valor do serviço.",
    # ---- IBS/CBS (reforma tributária) -------------------------------------
    "IBSCBS.CST": (
        "CST de IBS/CBS (reforma tributária). Definida pela nova regra de tributação; "
        "precisa estar coerente com o cClassTrib."
    ),
    "IBSCBS.cClassTrib": (
        "Código de classificação tributária de IBS/CBS. É o campo que amarra CST + "
        "tratamento. Divergência aqui invalida os grupos gIBSUF/gIBSMun/gCBS."
    ),
    "IBSCBS.gIBSCBS.vBC": "Base de cálculo de IBS/CBS.",
    "IBSCBS.gIBSCBS.gIBSUF.pIBSUF": "Alíquota de IBS estadual — tabela da UF.",
    "IBSCBS.gIBSCBS.gIBSMun.pIBSMun": "Alíquota de IBS municipal — tabela do município.",
    "IBSCBS.gIBSCBS.gCBS.pCBS": "Alíquota de CBS — tabela federal.",
    # ---- Totais -----------------------------------------------------------
    "ICMSTot.vNF": (
        "Valor total da nota divergente. Some as causas de item antes de olhar o total — "
        "o total é sempre consequência."
    ),
    "ICMSTot.vProd": "Somatório dos produtos — verifique itens ausentes ou valores unitários.",
    "ICMSTot.vDesc": "Total de descontos — regra de rateio de desconto por item.",
    "ICMSTot.vFrete": "Total de frete — regra de rateio e de inclusão do frete na base.",
    "ICMSTot.vTotTrib": (
        "Total de tributos aproximados (Lei da Transparência) — tabela IBPT carregada."
    ),
}

#: Fallback por sufixo quando a chave completa não existir.
PISTAS_POR_CAMPO: dict[str, str] = {
    "CST": "CST divergente — revise a regra/exceção de tributação aplicável ao item.",
    "CSOSN": "CSOSN divergente — revise o regime tributário e a regra do Simples Nacional.",
    "CFOP": "CFOP divergente — revise a determinação de CFOP (natureza + destino + cliente).",
    "NCM": "NCM divergente — corrija a classificação fiscal no cadastro do produto.",
    "_variante": "A regra tributária aplicada é outra — revise a regra de tributação do item.",
}

PISTA_GENERICA = (
    "Campo divergente sem pista mapeada. Verifique a regra de tributação que gera este "
    "campo e o cadastro do produto/cliente envolvido."
)


# --------------------------------------------------------------------------- #
#  Títulos legíveis
# --------------------------------------------------------------------------- #
#  O consultor não precisa decorar que `pICMS` é alíquota. O nome técnico
#  continua visível (ele existe no XML e nas telas do ERP), mas quem manda no
#  título é a linguagem do problema.
# --------------------------------------------------------------------------- #
TITULOS: dict[str, str] = {
    # ICMS
    "ICMS._variante": "Regra de ICMS diferente",
    "ICMS.CST": "CST de ICMS divergente",
    "ICMS.CSOSN": "CSOSN divergente",
    "ICMS.orig": "Origem da mercadoria divergente",
    "ICMS.pICMS": "Alíquota de ICMS divergente",
    "ICMS.pRedBC": "Redução de base de ICMS divergente",
    "ICMS.modBC": "Modalidade da base de ICMS divergente",
    "ICMS.modBCST": "Modalidade da base de ICMS-ST divergente",
    "ICMS.pMVAST": "MVA / IVA-ST divergente",
    "ICMS.pICMSST": "Alíquota de ICMS-ST divergente",
    "ICMS.pFCP": "Percentual de FCP divergente",
    "ICMS.pFCPST": "Percentual de FCP-ST divergente",
    "ICMS.motDesICMS": "Motivo de desoneração do ICMS divergente",
    "ICMS.pCredSN": "Percentual de crédito do Simples divergente",
    # Valores apurados (base tem tratamento próprio em titulo_da_divergencia)
    "ICMS.vICMS": "Valor do ICMS divergente",
    "ICMS.vICMSST": "Valor do ICMS-ST divergente",
    "ICMS.vICMSDeson": "Valor do ICMS desonerado divergente",
    "ICMS.vFCP": "Valor do FCP divergente",
    "IPI.vIPI": "Valor do IPI divergente",
    "PIS.vPIS": "Valor do PIS divergente",
    "COFINS.vCOFINS": "Valor da COFINS divergente",
    "ISSQN.vISSQN": "Valor do ISS divergente",
    # DIFAL
    "ICMSUFDest.pICMSUFDest": "Alíquota interna da UF de destino (DIFAL) divergente",
    "ICMSUFDest.pICMSInter": "Alíquota interestadual (DIFAL) divergente",
    "ICMSUFDest.pFCPUFDest": "FCP da UF de destino (DIFAL) divergente",
    # IPI
    "IPI._variante": "Regra de IPI diferente",
    "IPI.CST": "CST de IPI divergente",
    "IPI.pIPI": "Alíquota de IPI divergente",
    "IPI.cEnq": "Enquadramento legal do IPI divergente",
    # PIS / COFINS
    "PIS._variante": "Regra de PIS diferente",
    "PIS.CST": "CST de PIS divergente",
    "PIS.pPIS": "Alíquota de PIS divergente",
    "COFINS._variante": "Regra de COFINS diferente",
    "COFINS.CST": "CST de COFINS divergente",
    "COFINS.pCOFINS": "Alíquota de COFINS divergente",
    # ISS
    "ISSQN.cListServ": "Item da lista de serviços divergente",
    "ISSQN.vAliq": "Alíquota de ISS divergente",
    "ISSQN.indISS": "Exigibilidade do ISS divergente",
    "ISSQN.cMunFG": "Município de incidência do ISS divergente",
    # Reforma tributária
    "IBSCBS.CST": "CST de IBS/CBS divergente",
    "IBSCBS.cClassTrib": "Classificação tributária de IBS/CBS divergente",
    # Classificação fiscal do produto
    "PRODUTO.CFOP": "CFOP divergente",
    "PRODUTO.NCM": "NCM divergente",
    "PRODUTO.CEST": "CEST divergente",
    "PRODUTO.NVE": "NVE divergente",
    "PRODUTO.cBenef": "Código de benefício fiscal divergente",
}

#: Títulos por tipo de divergência estrutural (não é campo, é presença).
TITULOS_POR_TIPO = {
    "item_ausente_no_senior": "Item não emitido na nota do Senior",
    "item_ausente_no_cliente": "Item a mais na nota do Senior",
    "grupo_ausente_no_senior": "Imposto não calculado pelo Senior",
    "grupo_ausente_no_cliente": "Imposto calculado a mais pelo Senior",
}

_PREFIXO_LEGIVEL = {
    "p": "Alíquota",
    "v": "Valor",
    "q": "Quantidade",
    "mod": "Modalidade",
    "ind": "Indicador",
    "c": "Código",
}


def titulo_da_divergencia(grupo: str, campo: str, tipo: str = "") -> str:
    """Frase curta que descreve o problema, em vez do nome do campo no XML."""
    if tipo in TITULOS_POR_TIPO:
        return TITULOS_POR_TIPO[tipo]

    chave = f"{grupo}.{campo}" if grupo else campo
    if chave in TITULOS:
        return TITULOS[chave]

    folha = campo.rsplit(".", 1)[-1]
    chave_folha = f"{grupo}.{folha}" if grupo else folha
    if chave_folha in TITULOS:
        return TITULOS[chave_folha]

    categoria = categoria_do_grupo(grupo) if grupo else ""

    # Base de cálculo, não valor do imposto. Sem este ramo, o fallback de
    # prefixo abaixo lê o "v" de vBC como "Valor" e rotula a BASE como se fosse o
    # VALOR do imposto — dois campos distintos que o consultor ajusta em telas
    # diferentes. Cobre vBC, vBCST, vBCUFDest, vBCFCP de uma vez.
    if folha.startswith("vBC"):
        sufixo = "-ST" if "ST" in folha[3:] else ""
        base = f"Base de cálculo de {categoria}{sufixo}" if categoria else "Base de cálculo"
        return f"{base} divergente"

    for prefixo, rotulo in _PREFIXO_LEGIVEL.items():
        if folha.startswith(prefixo) and len(folha) > len(prefixo):
            return f"{rotulo} de {categoria} divergente" if categoria else f"{rotulo} divergente"
    return f"{categoria} · {folha} divergente" if categoria else f"{folha} divergente"


#: Termos extras por grupo, para aproximar a consulta do vocabulário da
#: documentação. O corpus fala "substituição tributária", nunca "pMVAST".
_SINONIMOS_DE_BUSCA = {
    "ICMSST": "substituição tributária ICMS-ST",
    "ICMSUFDest": "DIFAL diferencial de alíquota partilha",
    "PISST": "PIS substituição tributária",
    "COFINSST": "COFINS substituição tributária",
    "IPI": "IPI enquadramento TIPI",
    "ISSQN": "ISS serviço",
    "IBSCBS": "IBS CBS reforma tributária",
}

_RUIDO_NA_BUSCA = ("divergente", "diferente", "no Senior", "da nota")

#: Divergências estruturais não são "parametrização de um campo" — a frase
#: montada a partir do título ("parametrização Item não emitido na nota do
#: Senior cadastro tela") não casa com nada. Aqui a consulta é escrita à mão.
_CONSULTAS_ESTRUTURAIS = {
    "item_ausente_no_senior": (
        "cadastro de produto vínculo produto transação item não gerado na nota fiscal"
    ),
    "item_ausente_no_cliente": (
        "cadastro de produto item gerado a mais na nota fiscal transação"
    ),
    "grupo_ausente_no_senior": (
        "imposto não calculado na nota fiscal parametrização tributação produto transação"
    ),
    "grupo_ausente_no_cliente": (
        "imposto calculado indevidamente na nota fiscal parametrização tributação"
    ),
}


def consulta_de_parametrizacao(grupo: str, campo: str, tipo: str = "") -> str:
    """
    Monta a pergunta em **linguagem natural** que recupera a documentação do
    campo.

    O nome do campo no XML (``pCOFINS``, ``pMVAST``) não aparece em lugar nenhum
    da documentação da Senior, que é escrita em prosa: "alíquota de COFINS",
    "MVA". Buscar pela tag é buscar por um termo que não existe no corpus — o
    lado textual do ranking não casa nada e sobra só o vetorial, sem âncora.

    **A consulta é uma frase nominal, sem palavras de ligação.** Testado em
    24/07/2026 na base de 3.934 trechos: *"em qual tela do ERP Senior se
    parametriza alíquota de ICMS"* devolveu "Ordens de Compra — DIFAL"; a mesma
    intenção como *"parametrização alíquota ICMS cadastro tela"* devolveu
    "Rotinas de ICMS", a página oficial. As palavras vazias ("em qual", "se",
    "do") entram no BM25 como termos comuns e puxam o vetor para o centro do
    corpus — quanto mais curta e específica a consulta, melhor.
    """
    if tipo in _CONSULTAS_ESTRUTURAIS:
        return _CONSULTAS_ESTRUTURAIS[tipo]

    titulo = titulo_da_divergencia(grupo, campo, tipo)
    for ruido in _RUIDO_NA_BUSCA:
        titulo = titulo.replace(ruido, "")
    assunto = " ".join(titulo.split()).strip(" ·")

    extra = _SINONIMOS_DE_BUSCA.get(grupo, "")
    if grupo and grupo not in ("PRODUTO", "CABECALHO") and grupo not in assunto:
        extra = f"{grupo} {extra}".strip()

    return " ".join(f"parametrização {assunto} {extra} cadastro tela".split())


def pista_de_parametrizacao(grupo: str, campo: str) -> str:
    """
    Busca a pista do mais específico para o mais genérico:

        GRUPO.caminho.completo → caminho.completo → GRUPO.folha → folha
    """
    folha = campo.rsplit(".", 1)[-1]
    candidatos = [
        f"{grupo}.{campo}" if grupo else campo,
        campo,
        f"{grupo}.{folha}" if grupo else folha,
        folha,
    ]
    for chave in candidatos:
        if chave in PISTAS:
            return PISTAS[chave]
    if folha in PISTAS_POR_CAMPO:
        return PISTAS_POR_CAMPO[folha]
    return PISTA_GENERICA


def todas_as_pistas() -> dict[str, str]:
    """Usado pelo comando ``seed_regras`` para popular RegraParametrizacao."""
    combinado = dict(PISTAS)
    for campo, texto in PISTAS_POR_CAMPO.items():
        combinado.setdefault(campo, texto)
    return combinado
