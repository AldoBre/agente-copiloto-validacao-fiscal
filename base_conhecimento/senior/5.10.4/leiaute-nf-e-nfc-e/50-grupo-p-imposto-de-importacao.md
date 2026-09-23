# Grupo P - Imposto de Importação

> **Fonte:** Leiautes NF-e e NFC-e — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/leiaute-nf-e-nfc-e.htm  
> **Trilha:** Segmentos > Compliance > Documentos Eletrônicos > NF-e | NFC-e (Nota Fiscal Eletrônica) > Nota Fiscal Eletrônica 4.0  
> **Telas citadas:** E440IPC  
> **Identificadores de regras:** —

---
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação | Origem |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 262 | P01 | II | Grupo Imposto de Importação | CG | M01 |  | 0-1 |  | Informar apenas quando o item for sujeito ao II | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 263 | P02 | vBC | Valor BC do Imposto de Importação | E | P01 | N | 1-1 | 13v2 |  | Verifica se o valor "TipCdf" é igual a 1, busca o valor base de ICMS caso não seja 1 e soma o valor base de ICMS mais o valor base diferenciado, gerando assim o ImpVbc, variável da tag vBC. |
| 264 | P03 | vDespAdu | Valor despesas aduaneiras | E | P01 | N | 1-1 | 13v2 |  | Gera a informação que consta no campo E440IPC.VlrOui. Nesse caso, será preenchido apenas para os que usam Go Up. Os demais casos que não utilizam recebem 0. |
| 265 | P04 | vII | Valor Imposto de Importação | E | P01 | N | 1-1 | 13v2 |  | Gera a informação que consta no campo E440IPC.VlrIim. |
| 266 | P05 | vIOF | Valor Imposto sobre Operações Financeiras | E | P01 | N | 1-1 | 13v2 |  | Gera 0 por padrão. |
