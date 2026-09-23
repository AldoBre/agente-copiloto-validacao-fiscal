# Grupo T - COFINS ST

> **Fonte:** Leiautes NF-e e NFC-e — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/leiaute-nf-e-nfc-e.htm  
> **Trilha:** Segmentos > Compliance > Documentos Eletrônicos > NF-e | NFC-e (Nota Fiscal Eletrônica) > Nota Fiscal Eletrônica 4.0  
> **Telas citadas:** —  
> **Identificadores de regras:** —

---
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação | Origem |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 313 | T01 | COFINSST | Grupo COFINS Substituição Tributária | G | M01 |  | 0-1 |  |  | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 313.1 | T01.1 | -x- | Sequência XML | CG | T01 |  | 1-1 |  | Informar os campos T02 e T03 para cálculo da COFINS Substituição Tributária em percentual | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 314 | T02 | vBC | Valor da Base de Cálculo da COFINS | E | T01.1 | N | 1-1 | 13v2 |  | Gera por padrão o valor do campo E140Ipv.VlrBpi. |
| 315 | T03 | pCOFINS | Alíquota da COFINS (em percentual) | E | T01.1 | N | 1-1 | 3v2-4 |  | Gera por padrão o valor do campo E140Ipv.PerCim. |
| 315.1 | T03.1 | -x- | Sequência XML | CG | T01 |  | 1-1 |  | Informar os campos T04 e T05 para cálculo da COFINS Substituição Tributária em valor | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 316 | T04 | qBCProd | Quantidade Vendida | E | T03.1 | N | 1-1 | 12v0-4 |  | Gera por padrão o valor do campo E140Ipv.QtdBcf. |
| 317 | T05 | vAliqProd | Alíquota da COFINS (em reais) | E | T03.1 | N | 1-1 | 11v0-4 |  | Gera por padrão o valor do campo E140Ipv.AliCff. |
| 318 | T06 | vCOFINS | Valor da COFINS | E | T01 | N | 1-1 | 13v2 |  | Gera por padrão o valor do campo E140Ipv.VlrPis. |
