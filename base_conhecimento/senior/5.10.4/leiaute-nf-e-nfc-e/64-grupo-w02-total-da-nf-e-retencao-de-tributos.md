# Grupo W02 - Total da NF-e / Retenção de Tributos

> **Fonte:** Leiautes NF-e e NFC-e — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/leiaute-nf-e-nfc-e.htm  
> **Trilha:** Segmentos > Compliance > Documentos Eletrônicos > NF-e | NFC-e (Nota Fiscal Eletrônica) > Nota Fiscal Eletrônica 4.0  
> **Telas citadas:** —  
> **Identificadores de regras:** —

---
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação | Origem |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 348 | W23 | retTrib | Grupo Retenções de Tributos | G | W01 |  | 0-1 |  |  | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 349 | W24 | vRetPIS | Valor Retido de PIS | E | W23 | N | 0-1 | 13v2 |  | Gera o valor, conforme consta no campo E140Nfv.VlrPit. |
| 350 | W25 | vRetCOFINS | Valor Retido de COFINS | E | W23 | N | 0-1 | 13v2 |  | Gera o valor, conforme consta no campo E140Nfv.VlrCrt. |
| 351 | W26 | vRetCSLL | Valor Retido de CSLL | E | W23 | N | 0-1 | 13v2 |  | Gera o valor, conforme consta no campo E140Nfv.VlrCsl. |
| 352 | W27 | vBCIRRF | Base de Cálculo do IRRF | E | W23 | N | 0-1 | 13v2 |  | Gera o valor, conforme consta no campo E140Nfv.VlrBir. |
| 353 | W28 | vIRRF | Valor Retido do IRRF | E | W23 | N | 0-1 | 13v2 |  | Gera o valor, conforme consta no campo E140Nfv.VlrIrf. |
| 354 | W29 | vBCRetPrev | Base de Cálculo da retenção da Previdência Social | E | W23 | N | 0-1 | 13v2 |  | Gera o valor, conforme consta no campo E140Nfv.VlrBfu. |
| 355 | W30 | vRetPrev | Valor da Retenção da Previdência Social | E | W23 | N | 0-1 | 13v2 |  | Gera o valor, conforme consta no campo E140Nfv.VlrFun. |
