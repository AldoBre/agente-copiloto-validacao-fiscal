"""
Valores válidos extraídos dos próprios XSD da NF-e (layout 4.00, PL 010b
NT 2025.002 v1.30).

Ficam em código, e não no banco, por dois motivos: são pequenos e só mudam
quando o layout muda — junto com uma nova versão do schema, que é evento de
deploy, não de sincronização de tabela. Assim a validação estrutural funciona
mesmo com o banco vazio.

Regenerar com ``python manage.py importar_tabelas_fiscais --so-enumerados``
depois de baixar um pacote de schemas novo.
"""
from __future__ import annotations

VERSAO_LAYOUT = "4.00"
PACOTE_SCHEMAS = "PL_010b_NT2025_002_v1.30"

#: CST de ICMS — regime normal.
ICMS_CST = {
    "00", "02", "10", "15", "20", "30", "40", "41",
    "50", "51", "53", "60", "61", "70", "90",
}

#: CSOSN — Simples Nacional. Nota é ou CST ou CSOSN, nunca os dois.
CSOSN = {"101", "102", "103", "201", "202", "203", "300", "400", "500", "900"}

IPI_CST = {
    "00", "01", "02", "03", "04", "05",
    "49", "50", "51", "52", "53", "54", "55", "99",
}

PIS_CST = COFINS_CST = {
    "01", "02", "03", "04", "05", "06", "07", "08", "09",
    "49", "50", "51", "52", "53", "54", "55", "56",
    "60", "61", "62", "63", "64", "65", "66", "67",
    "70", "71", "72", "73", "74", "75", "98", "99",
}

#: Origem da mercadoria (simpleType Torig).
ORIGEM = {"0", "1", "2", "3", "4", "5", "6", "7", "8"}

#: Código de Regime Tributário do emitente. 4 = MEI (NT 2024.001).
CRT = {"1", "2", "3", "4"}

#: CST de ICMS que indicam mercadoria sujeita a substituição tributária —
#: seja retendo agora (10, 30, 70), seja já retida antes (60). São esses que
#: tornam o CEST esperado no item.
ICMS_CST_COM_ST = {"10", "30", "60", "70", "201", "202", "203", "500"}

#: CST de ICMS em que não há débito próprio a destacar.
ICMS_CST_SEM_DEBITO = {"40", "41", "50", "60"}


def cst_ou_csosn_valido(valor: str, *, simples: bool) -> bool:
    """
    Valida o código de situação tributária do ICMS conforme o regime.

    O ``simples`` importa: 102 é CSOSN válido para optante do Simples e não
    existe no regime normal, e 00 é o contrário. Validar contra a união dos
    dois conjuntos deixaria passar a troca de regime, que é erro real.
    """
    if not valor:
        return False
    return valor in (CSOSN if simples else ICMS_CST)
