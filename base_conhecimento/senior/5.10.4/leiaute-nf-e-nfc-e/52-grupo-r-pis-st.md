# Grupo R - PIS ST

> **Fonte:** Leiautes NF-e e NFC-e — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/leiaute-nf-e-nfc-e.htm  
> **Trilha:** Segmentos > Compliance > Documentos Eletrônicos > NF-e | NFC-e (Nota Fiscal Eletrônica) > Nota Fiscal Eletrônica 4.0  
> **Telas citadas:** —  
> **Identificadores de regras:** —

---
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação | Origem |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 287 | R01 | PISST | Grupo PIS Substituição Tributária | G | M01 |  | 0-1 |  |  | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 287.1 | R01.1 | -x- | Sequência XML | CG | R01 |  | 1-1 |  | Informar os campos R02 e R03 para cálculo do PIS em percentual | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 288 | R02 | vBC | Valor da Base de Cálculo do PIS | E | R01.1 | N | 1-1 | 13v2 |  | Gera a informação que consta no campo E140Ipv.VlrBsp. |
| 289 | R03 | pPIS | Alíquota do PIS (em percentual) | E | R01.1 | N | 1-1 | 3v2-4 |  | Gera a informação que consta no campo E019Sub.IcmEst. |
| 289.1 | R03.1 | -x- | Sequência XML | CG | R01 |  | 1-1 |  | Informar os campos R04 e R05 para cálculo do PIS em valor | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 290 | R04 | qBCProd | Quantidade Vendida | E | R031. | N | 1-1 | 12v0-4 |  | Gera a informação que consta no campo E140Ipv.QtdFat. |
| 291 | R05 | vAliqprod | Alíquota do PIS (em reais) | E | E03.1 | N | 1-1 | 11v0-4 |  | Gera a informação que consta no campo E140Ipv.VlrCid. |
| 292 | R06 | vPIS | Valor do PIS | E | R01 | N | 1-1 | 13v2 |  | Gera a informação que consta no campo E140Ipv.VlrStp. |
