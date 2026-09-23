# Grupo ZC - Informações do Registro de Aquisição de Cana

> **Fonte:** Leiautes NF-e e NFC-e — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/leiaute-nf-e-nfc-e.htm  
> **Trilha:** Segmentos > Compliance > Documentos Eletrônicos > NF-e | NFC-e (Nota Fiscal Eletrônica) > Nota Fiscal Eletrônica 4.0  
> **Telas citadas:** —  
> **Identificadores de regras:** VEN-140NECAN01

---
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação | Origem |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 409 | ZC01 | cana | Grupo Cana | G | A01 |  | 0-1 |  | Informações de registro aquisições de cana v2.0 | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 410 | ZC02 | safra | Identificação da safra | E | ZC01 | C | 1-1 | 4 - 9 | Informar a safra, no formato: "AAAA" ou "AAAA/AAAA". v2.0 | Gera por padrão utilizando a variável VSIntCanSaf do identificador de regras VEN-140NECAN01. |
| 411 | ZC03 | ref | Mês e ano de referência | E | ZC01 | C | 1-1 | 7 | Informar o mês e ano de referência, no formato: "MM/AAAA". v2.0 | Gera por padrão utilizando a variável VSIntCanMre do identificador de regras VEN-140NECAN01. |
| 412 | ZC04 | forDia | Grupo Fornecimento diário de cana | G | ZC01 |  | 1-31 |  | Informar os fornecimentos diários de cana v2.0 | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 427 | ZC05 | dia | Dia | A | ZC04 | N | 1-1 | 1 - 2 | v2.0 | Gera por padrão utilizando a variável VSIntFcdDia do identificador de regras VEN-140NECAN01. |
| 414 | ZC06 | qtde | Quantidade | E | ZC04 | N | 1-1 | 11v10 | Quantidade em KG v2.0 | Gera por padrão utilizando a variável VSIntFcdQtd do identificador de regras VEN-140NECAN01. |
| 415 | ZC07 | qTotMes | Quantidade Total do Mês | E | ZC01 | N | 1-1 | 11v10 | v2.0 | Gera por padrão utilizando a variável VSIntCanTme do identificador de regras VEN-140NECAN01. |
| 416 | ZC08 | qTotAnt | Quantidade Total Anterior | E | ZC01 | N | 1-1 | 11v10 | v2.0 | Gera por padrão utilizando a variável VSIntCanTma do identificador de regras VEN-140NECAN01. |
| 417 | ZC09 | qTotGer | Quantidade Total Geral | E | ZC01 | N | 1-1 | 11v10 | v2.0 | Gera por padrão utilizando a variável VSIntCanTge do identificador de regras VEN-140NECAN01. |
| 418 | ZC10 | deduc | Grupo Deduções - Taxas e Contribuições | G | ZC01 |  | 0-10 |  | Informar as Deduções - Taxas e Contribuições v2.0 | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 419 | ZC11 | xDed | Descrição da Dedução | E | ZC10 | C | 1-1 | 1 - 60 | Informar a Descrição da Dedução v2.0 | Gera por padrão utilizando a variável VSIntDcaDes do identificador de regras VEN-140NECAN01. |
| 420 | ZC12 | vDed | Valor da Dedução | E | ZC10 | N | 1-1 | 13v2 | v2.0 | Gera por padrão utilizando a variável VSIntDcaVlr do identificador de regras VEN-140NECAN01. |
| 421 | ZC13 | vFor | Valor dos Fornecimentos | E | ZC01 | N | 1-1 | 13v2 | Valor dos Fornecimentos v2.0 | Gera por padrão utilizando a variável VSIntCanVfo do identificador de regras VEN-140NECAN01. |
| 422 | ZC14 | vTotDed | Valor Total da Dedução | E | ZC01 | N | 1-1 | 13v2 | Valor das deduções v2.0 | Gera por padrão utilizando a variável VSIntCanTde do identificador de regras VEN-140NECAN01. |
| 423 | ZC15 | vLiqFor | Valor Líquido dos Fornecimentos | E | ZC01 | N | 1-1 | 13v2 | Valor Líquido dos Fornecimentos v2.0 | Gera por padrão utilizando a variável VSIntCanTge do identificador de regras VEN-140NECAN01. |

## Páginas relacionadas

* [VEN-140NECAN01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_140necan01.htm)
