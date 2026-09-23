# Grupo N10c - Grupo CRT=1 (CSON 101)

> **Fonte:** Leiautes NF-e e NFC-e — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/leiaute-nf-e-nfc-e.htm  
> **Trilha:** Segmentos > Compliance > Documentos Eletrônicos > NF-e | NFC-e (Nota Fiscal Eletrônica) > Nota Fiscal Eletrônica 4.0  
> **Telas citadas:** —  
> **Identificadores de regras:** VEN-140NEITE01

---
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação | Origem |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 245.24 | N10c | ICMSSN101 | Grupo CRT=1 - Simples Nacional e CSON=101 | CG | N01 |  | 1-1 |  | Tributação ICMS pelo Simples Nacional, CSON=101 (v2.0) | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 245.25 | N11 | orig | Origem da mercadoria | E | N10c | N | 1-1 | 1 | 0 - Nacional, exceto as indicadas nos códigos 3, 4, 5 e 8; 1 - Estrangeira - Importação direta, exceto a indicada no código 6; 2 - Estrangeira - Adquirida no mercado interno, exceto a indicada no código 7; 3 - Nacional, mercadoria ou bem com Conteúdo de Importação superior a 40% e inferior a 70%; 4 - Nacional, cuja produção tenha sido feita em conformidade com os processos produtivos básicos de que tratam as legislações citadas nos Ajustes; 5 - Nacional, mercadoria ou bem com Conteúdo de Importação inferior ou igual a 40%; 6 - Estrangeira - Importação direta, sem similar nacional, constante em lista da CAMEX e gás natural; 7 - Estrangeira - Adquirida no mercado interno, sem similar nacional, constante lista CAMEX e gás natural; 8 - Nacional, mercadoria ou bem com Conteúdo de Importação superior a 70%. | Gera por padrão o valor do campo E140Ipv.OriMer. Pode ser alterado utilizando o identificador de regra VEN-140NEITE01 através da variável VSIntImpOri. |
| 245.26 | N12a | CSOSN | Código de Situação da Operação - Simples Nacional | E | N10c | N | 1-1 | 3 | 101=Tributada pelo Simples Nacional com permissão de crédito (v2.0) | Gera a informação que consta no campo E140Ipv.CodStr. |
| 245.27 | N29 | pCredSN | Alíquota aplicável de cálculo do crédito (Simples Nacional) | E | N10c | N | 1-1 | 3v2-4 | (v2.0) | Gera a informação que consta no campo E140Ipv.PerIsn. |
| 245.28 | N30 | vCredICMSSN | Valor crédito do ICMS que pode ser aproveitado nos termos ao art. 23 da LC 123 (Simples Nacional) | E | N10c | N | 1-1 | 13v2 | (v2.0) | Gera a informação que consta no campo E140Ipv.VlrIsn. |

## Páginas relacionadas

* [VEN-140NEITE01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_140neite01.htm)
