# Grupo N10a - Grupo de Partilha do ICMS

> **Fonte:** Leiautes NF-e e NFC-e — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/leiaute-nf-e-nfc-e.htm  
> **Trilha:** Segmentos > Compliance > Documentos Eletrônicos > NF-e | NFC-e (Nota Fiscal Eletrônica) > Nota Fiscal Eletrônica 4.0  
> **Telas citadas:** F019TST  
> **Identificadores de regras:** VEN-140NEITE01

---
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação | Origem |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 245.01 | N10a | ICMSPart | Grupo de Partilha do ICMS entre a UF de origem e UF de destino ou a UF definida na legislação | CG | N01 |  | 1-1 |  | Operação interestadual para consumidor final com partilha do ICMS devido na operação entre a UF de origem e a do destinatário, ou a UF definida na legislação. (Ex. UF da concessionária de entrega do veículo) (v2.0) | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 245.02 | N11 | orig | Origem da mercadoria | E | N10a | N | 1-1 | 1 | 0 - Nacional, exceto as indicadas nos códigos 3, 4, 5 e 8; 1 - Estrangeira - Importação direta, exceto a indicada no código 6; 2 - Estrangeira - Adquirida no mercado interno, exceto a indicada no código 7; 3 - Nacional, mercadoria ou bem com Conteúdo de Importação superior a 40% e inferior a 70%; 4 - Nacional, cuja produção tenha sido feita em conformidade com os processos produtivos básicos de que tratam as legislações citadas nos Ajustes; 5 - Nacional, mercadoria ou bem com Conteúdo de Importação inferior ou igual a 40%; 6 - Estrangeira - Importação direta, sem similar nacional, constante em lista da CAMEX e gás natural; 7 - Estrangeira - Adquirida no mercado interno, sem similar nacional, constante lista CAMEX e gás natural; 8 - Nacional, mercadoria ou bem com Conteúdo de Importação superior a 70%. | Gera por padrão o valor do campo E140Ipv.OriMer. Pode ser alterado utilizando o identificador de regra VEN-140NEITE01 através da variável VSIntImpOri. |
| 245.03 | N12 | CST | Tributação do ICMS | E | N10a | N | 1-1 | 2 | 10=Tributada e com cobrança do ICMS por substituição tributária; 90=Outros. | Gera por padrão o valor do campo E140Ipv.OriMer + E140Ipv.CodStr. Pode ser alterado utilizando o identificador de regra VEN-140NEITE01 através da variável VSIntImpCst. |
| 245.04 | N13 | modBC | Modalidade de determinação da BC do ICMS | E | N10a | N | 1-1 | 1 | 0=Margem Valor Agregado (%); 1=Pauta (Valor); 2=Preço Tabelado Máx. (valor); 3=Valor da operação | Verifica o valor do campo E140Ipv.CodBic para buscar o valor do campo E019Tst.CalSub e gerar na tag. Pode ser alterado utilizando o identificador de regra VEN-140NEITE01 através da variável VSIntImpMbc. |
| 245.05 | N15 | vBC | Valor da BC do ICMS | E | N10a | N | 1-1 | 13v2 | (v2.0) | Gera a informação que consta no campo E140Ipv.VlrBsd. |
| 245.06 | N14 | pRedBC | Percentual de Redução de BC | E | N10a | N | 0-1 | 3v2-4 | (v2.0) | Gera a informação que consta no campo E019Red.RedEnt. Pode ser alterado utilizando o identificador de regra VEN-140NEITE01 variável VSIntImpRbc. |
| 245.07 | N16 | pICMS | Alíquota do imposto | E | N10a | N | 1-1 | 3v2-4 | (v2.0) | Gera a informação que consta no campo E140Ipv.PerIcm. |
| 245.08 | N17 | vICMS | Valor do ICMS | E | N10a | N | 1-1 | 13v2 |  | Gera a informação que consta no campo E140Ipv.VlrIcm. |
| 245.09 | N18 | modBCST | Modalidade de determinação da BC do ICMS ST | E | N10a | N | 1-1 | 1 | 0=Preço tabelado ou máximo sugerido; 1=Lista Negativa (valor); 2=Lista Positiva (valor); 3=Lista Neutra (valor); 4=Margem Valor Agregado (%); 5=Pauta (valor) | Se ((ValorBaseICMS > 0) E (ValorBaseICMS) = (ValorBaseICMSST)) OU ((ValorLiquido - ValorICMSST) = (ValorBaseICMSST)) E a data de emissão da NF-e for maior ou igual a data do parâmetro global NT2019001, então gera o valor igual a 6.  Senão, se o campo Critério Cálculo Substituição do cadastro do ICMS ST da tela F019TST for igual a 1, então gera o valor padrão igual a 4.  Se as condições anteriores não forem atendidas, então gera o valor padrão igual a 5. |
| 245.10 | N19 | pMVAST | Percentual da margem de valor Adicionado do ICMS ST | E | N10a | N | 0-1 | 3v2-4 | (v2.0) | Gera a informação que consta no campo E019Sub.MarLuc do código do ICMS ST que está no item da nota fiscal. Pode ser alterado utilizando o identificador de regra VEN-140NEITE01 através da variável VSIntMarLuc. |
| 245.11 | N20 | pRedBCST | Percentual da Redução de BC do ICMS ST | E | N10a | N | 0-1 | 3v2-4 | (v2.0) | Gera a informação que consta no campo E019Sub.MarLuc do código do ICMS ST que está no item da nota fiscal. Pode ser alterado utilizando o identificador de regra VEN-140NEITE01 através da variável VSIntMarLuc. |
| 245.12 | N21 | vBCST | Valor da BC do ICMS ST | E | N10a | N | 1-1 | 13v2 | (v2.0) | Gera a informação que consta no campo E140Ipv.VlrBsi. |
| 245.13 | N22 | pICMSST | Alíquota do imposto do ICMS ST | E | N10a | N | 1-1 | 3v2-4 | (v2.0) | Gera a informação que consta no campo E019Sub.IcmEst do código do ICMS ST que está no item da nota fiscal. Pode ser alterado utilizando o identificador de regra VEN-140NEITE01 através da variável VSIntImpPcs. |
| 245.14 | N23 | vICMSST | Valor do ICMS ST | E | N10a | N | 1-1 | 13v2 | Valor do ICMS ST (v2.0) | Gera a informação que consta no campo E140Ipv.VlrIcs. |
| 245.15 | N25 | pBOp | Percentual da BC operação própria | E | N10a | N | 1-1 | 3v2-4 | Percentual para determinação do valor da Base de Cálculo da operação própria (v2.0) | Esta tag não é gerada pelo ERP. |
| 245.16 | N24 | UFST | UF para qual é devido o ICMS ST | E | N10a | C | 1-1 | 2 | Sigla da UF para qual é devido o ICMS ST da operação. Informar "EX" para Exterior. (v2.0) | Esta tag não é gerada pelo ERP. |

## Páginas relacionadas

* [VEN-140NEITE01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_140neite01.htm)
* [F019TST](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f019tst.htm)
