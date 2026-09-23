# Grupo N10d - Grupo CRT=1 (CSON 102, 103, 300 ou 400)

> **Fonte:** Leiautes NF-e e NFC-e — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/leiaute-nf-e-nfc-e.htm  
> **Trilha:** Segmentos > Compliance > Documentos Eletrônicos > NF-e | NFC-e (Nota Fiscal Eletrônica) > Nota Fiscal Eletrônica 4.0  
> **Telas citadas:** —  
> **Identificadores de regras:** VEN-140NEITE01

---
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação | Origem |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 245.24 | n10d | ICMSSN102 | Grupo CRT=1 - Simples Nacional e CSON=102, 103, 300 ou 400 | CG | N01 |  | 1-1 |  | Tributação ICMS pelo Simples Nacional, CSON=102, 103, 300 ou 400 (v2.0) | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 245.25 | N11 | orig | Origem da mercadoria | E | N10d | N | 1-1 | 1 | 0 - Nacional, exceto as indicadas nos códigos 3, 4, 5 e 8; 1 - Estrangeira - Importação direta, exceto a indicada no código 6; 2 - Estrangeira - Adquirida no mercado interno, exceto a indicada no código 7; 3 - Nacional, mercadoria ou bem com Conteúdo de Importação superior a 40% e inferior a 70%; 4 - Nacional, cuja produção tenha sido feita em conformidade com os processos produtivos básicos de que tratam as legislações citadas nos Ajustes; 5 - Nacional, mercadoria ou bem com Conteúdo de Importação inferior ou igual a 40%; 6 - Estrangeira - Importação direta, sem similar nacional, constante em lista da CAMEX e gás natural; 7 - Estrangeira - Adquirida no mercado interno, sem similar nacional, constante lista CAMEX e gás natural; 8 - Nacional, mercadoria ou bem com Conteúdo de Importação superior a 70%. | Gera por padrão o valor do campo E140Ipv.OriMer. Pode ser alterado utilizando o identificador de regra VEN-140NEITE01 através da variável VSIntImpOri. |
| 245.26 | N12a | CSOSN | Código de Situação da Operação - Simples Nacional | E | N10d | N | 1-1 | 3 | 102=Tributada pelo Simples Nacional sem permissão de crédito; 103=Isenção do ICMS no Simples Nacional para faixa de receita bruta; 300=Imune; 400=Não tributada pelo Simples Nacional (v2.0) | Gera a informação que consta no campo E140Ipv.CodStr. |

## Páginas relacionadas

* [VEN-140NEITE01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_140neite01.htm)
