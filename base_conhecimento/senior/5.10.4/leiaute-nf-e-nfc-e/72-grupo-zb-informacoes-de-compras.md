# Grupo ZB - Informações de Compras

> **Fonte:** Leiautes NF-e e NFC-e — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/leiaute-nf-e-nfc-e.htm  
> **Trilha:** Segmentos > Compliance > Documentos Eletrônicos > NF-e | NFC-e (Nota Fiscal Eletrônica) > Nota Fiscal Eletrônica 4.0  
> **Telas citadas:** —  
> **Identificadores de regras:** VEN-140NEDGE01

---
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação | Origem |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 405 | ZB01 | compra | Grupo Compra | G | A01 |  | 0-1 |  | Informação adicional de compra | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 406 | ZB02 | xNEmp | Nota de Empenho | E | ZB01 | C | 0-1 | 1 - 22 | Identificação da Nota de Empenho, quando se tratar de compras públicas (NT2011/004) | Tag gerada via identificador de regra VEN-140NEDGE01 através da variável VSIntCprNte. |
| 407 | ZB03 | xPed | Pedido | E | ZB01 | C | 0-1 | 1 - 60 | Informar o pedido | Tag gerada via identificador de regra VEN-140NEDGE01 através da variável VSIntCprPed. |
| 408 | ZB04 | xCont | Contrato | E | ZB01 | C | 0-1 | 1 - 60 | Informar o contrato de compra | Tag gerada via identificador de regra VEN-140NEDGE01 através da variável VSIntCprCtr. |

## Páginas relacionadas

* [VEN-140NEDGE01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_140nedge01.htm)
