"""
Alíquotas de ICMS que não vêm de tabela.

Usadas pela ferramenta ``aliquota_icms_interestadual`` do agente, ao explicar
uma divergência de ICMS entre os dois sistemas.
"""
from __future__ import annotations

from decimal import Decimal

#: Alíquotas interestaduais de ICMS. Não vêm de tabela porque não existe fonte
#: oficial em formato consumível — e não precisam: são quatro regras de norma
#: federal, estáveis desde a Resolução do Senado 22/1989, com o acréscimo da
#: 13/2012 para importados. Hardcode com teste vale mais que scraper aqui.
#: (A 22/1989 NÃO foi revogada pela 13/2012, ao contrário do que muito site
#: secundário afirma — a 13 criou a alíquota de 4% só para importado.)
_SUL_SUDESTE = {"SP", "RJ", "MG", "PR", "SC", "RS"}
ALIQUOTA_INTERESTADUAL_GERAL = Decimal("12")
ALIQUOTA_INTERESTADUAL_REDUZIDA = Decimal("7")
ALIQUOTA_INTERESTADUAL_IMPORTADO = Decimal("4")

#: Origens 1, 2, 3, 6 e 7 indicam mercadoria importada ou com conteúdo de
#: importação superior a 40% — nesses casos a interestadual é 4%.
ORIGENS_IMPORTADAS = {"1", "2", "3", "6", "7"}


def aliquota_interestadual(origem_uf: str, destino_uf: str, origem_mercadoria: str) -> Decimal:
    """
    Alíquota de ICMS aplicável numa operação interestadual.

    7% quando sai do Sul/Sudeste (exceto ES) para Norte, Nordeste, Centro-Oeste
    ou ES; 12% nos demais casos; 4% para mercadoria importada, que prevalece
    sobre as duas anteriores.
    """
    if origem_mercadoria in ORIGENS_IMPORTADAS:
        return ALIQUOTA_INTERESTADUAL_IMPORTADO
    if origem_uf in _SUL_SUDESTE and destino_uf not in _SUL_SUDESTE:
        return ALIQUOTA_INTERESTADUAL_REDUZIDA
    return ALIQUOTA_INTERESTADUAL_GERAL
