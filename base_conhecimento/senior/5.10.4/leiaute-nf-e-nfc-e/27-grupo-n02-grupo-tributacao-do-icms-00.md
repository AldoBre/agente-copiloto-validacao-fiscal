# Grupo N02 - Grupo Tributação do ICMS= 00

> **Fonte:** Leiautes NF-e e NFC-e — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/leiaute-nf-e-nfc-e.htm  
> **Trilha:** Segmentos > Compliance > Documentos Eletrônicos > NF-e | NFC-e (Nota Fiscal Eletrônica) > Nota Fiscal Eletrônica 4.0  
> **Telas citadas:** —  
> **Identificadores de regras:** VEN-140NEITE01

---
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação | Origem |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 165 | N02 | ICMS00 | Grupo Tributação ICMS= 00 | CG | N01 |  | 1-1 |  | Tributada integralmente | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ |
| 166 | N11 | orig | Origem da mercadoria | E | N02 | N | 1-1 | 1 | 0 - Nacional, exceto as indicadas nos códigos 3, 4, 5 e 8; 1 - Estrangeira - Importação direta, exceto a indicada no código 6; 2 - Estrangeira - Adquirida no mercado interno, exceto a indicada no código 7; 3 - Nacional, mercadoria ou bem com Conteúdo de Importação superior a 40% e inferior ou igual a 70%; 4 - Nacional, cuja produção tenha sido feita em conformidade com os processos produtivos básicos de que tratam as legislações citadas nos Ajustes; 5 - Nacional, mercadoria ou bem com Conteúdo de Importação inferior ou igual a 40%; 6 - Estrangeira - Importação direta, sem similar nacional, constante na lista CAMEX e gás natural; 7 - Estrangeira - Adquirida no mercado interno, sem similar nacional, constante na lista CAMEX e gás natural; 8 - Nacional, mercadoria ou bem com Conteúdo de Importação superior a 70%. | Gera por padrão o valor do campo E140Ipv.OriMer. Pode ser alterado utilizando o identificador de regra VEN-140NEITE01 através da variável VSIntImpOri. |
| 167 | N12 | CST | Tributação do ICMS = 00 | E | N02 | N | 1-1 | 2 | 00= Tributada integralmente | Gera por padrão o valor do campo E140Ipv.OriMer + E140Ipv.CodStr. Pode ser alterado utilizando o identificador de regra VEN-140NEITE01 através da variável VSIntImpCst. |
| 168 | N13 | modBC | Modalidade de determinação da BC do ICMS | E | N02 | N | 1-1 | 1 | 0=Margem Valor Agregado (%); 1=Pauta; 2=Preço Tabelado Máx. (valor); 3=Valor da operação | Verifica o valor do campo E140Ipv.CodBic para buscar o valor do campo E019Tst.CalSub e gerar na tag. Pode ser alterado utilizando o identificador de regra VEN-140NEITE01 através da variável VSIntImpMbc. |
| 169 | N15 | vBC | Valor da BC do ICMS | E | N02 | N | 1-1 | 13v2 |  | Gera a informação que consta no campo E140Ipv.VlrBic. |
| 170 | N16 | pICMS | Alíquota do imposto | E | N02 | N | 1-1 | 3v2-4 | Alíquota do ICMS sem o FCP. Quando for o caso, informar a alíquota do FCP no campo pFCP | Gera a informação que consta no campo E140Ipv.PerIcm. |
| 171 | N17 | vICMS | Valor do ICMS | E | N02 | N | 1-1 | 13v2 |  | Gera a informação que consta no campo E140Ipv.VlrIcm. |
| 171.01 | N17.1 | -x- | Sequência de XML | G | N02 |  | 0-1 |  | (Criada na NT2016.002) | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 171.02 | N17b | pFCP | Percentual do ICMS relativo ao Fundo de Combate à Pobreza (FCP) | E | N17.1 | N | 1-1 | 3v2-4 | Percentual relativo ao Fundo de Combate à Pobreza (FCP) | Gera a informação que consta no campo E140Pvd.AliFcp. |
| 171.03 | N17c | vFCP | Valor do Fundo de Combate à Pobreza (FCP) | E | N17.01 | N | 1-1 | 13v2 | Valor do ICMS relativo ao Fundo de Combate à Pobreza (FCP) | Gera a informação que consta no campo E140Pvd.VlrFcp. |

## Páginas relacionadas

* [VEN-140NEITE01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_140neite01.htm)
