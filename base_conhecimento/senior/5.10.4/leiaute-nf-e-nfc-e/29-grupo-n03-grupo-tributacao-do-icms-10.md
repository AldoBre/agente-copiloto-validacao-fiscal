# Grupo N03 - Grupo Tributação do ICMS= 10

> **Fonte:** Leiautes NF-e e NFC-e — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/leiaute-nf-e-nfc-e.htm  
> **Trilha:** Segmentos > Compliance > Documentos Eletrônicos > NF-e | NFC-e (Nota Fiscal Eletrônica) > Nota Fiscal Eletrônica 4.0  
> **Telas citadas:** F019TST  
> **Identificadores de regras:** VEN-140NEITE01

---
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação | Origem |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 172 | N03 | ICMS10 | Grupo Tributação do ICMS = 10 | CG | N01 |  | 1-1 |  | Tributada e com cobrança do ICMS por substituição tributária | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 173 | N11 | orig | Origem da mercadoria | E | N03 | N | 1-1 | 1 | 0 - Nacional, exceto as indicadas nos códigos 3, 4, 5 e 8; 1 - Estrangeira - Importação direta, exceto a indicada no código 6; 2 - Estrangeira - Adquirida no mercado interno, exceto a indicada no código 7; 3 - Nacional, mercadoria ou bem com Conteúdo de Importação superior a 40% e inferior ou igual a 70%; 4 - Nacional, cuja produção tenha sido feita em conformidade com os processos produtivos básicos de que tratam as legislações citadas nos Ajustes; 5 - Nacional, mercadoria ou bem com Conteúdo de Importação inferior ou igual a 40%; 6 - Estrangeira - Importação direta, sem similar nacional, constante na lista da CAMEX e gás natural; 7 - Estrangeira - Adquirida no mercado interno, sem similar nacional, constante na lista CAMEX e gás natural; 8 - Nacional, mercadoria ou bem com Conteúdo de Importação superior a 70% | Gera por padrão o valor do campo E140Ipv.OriMer. Pode ser alterado utilizando o identificador de regra VEN-140NEITE01 através da variável VSIntImpOri. |
| 174 | N12 | CST | Tributação do ICMS = 10 | E | N03 | N | 1-1 | 2 | 10= Tributada e com cobrança do ICMS por substituição tributária | Gera por padrão o valor do campo E140Ipv.OriMer + E140Ipv.CodStr. Pode ser alterado utilizando o identificador de regra VEN-140NEITE01 através da variável VSIntImpCst. |
| 175 | N13 | modBC | Modalidade de determinação da BC do ICMS | E | N03 | N | 1-1 | 1 | 0=Margem Valor Agregado (%); 1=Pauta (Valor); 2=Preço Tabelado Máx. (valor); 3=Valor da operação | Verifica o valor do campo E140Ipv.CodBic para buscar o valor do campo E019Tst.CalSub e gerar na tag. Pode ser alterado utilizando o identificador de regra VEN-140NEITE01 através da variável VSIntImpMbc. |
| 176 | N15 | vBC | Valor da BC do ICMS | E | N03 | N | 1-1 | 13v2 |  | Gera a informação que consta no campo E140Ipv.VlrBic. |
| 177 | N16 | pICMS | Alíquota do imposto | E | N03 | N | 1-1 | 3v2-4 | Alíquota do ICMS sem o FCP. Quando for o caso, informar a alíquota do FCP no campo pFCP | Gera a informação que consta no campo E140Ipv.PerIcm. |
| 178 | N17 | vICMS | Valor do ICMS | E | N03 | N | 1-1 | 13v2 |  | Gera a informação que consta no campo E140Ipv.VlrIcm. |
| 178.01 | N17.0 | -x- | Sequência de XML | G | N03 |  | 0-1 |  |  | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 178.02 | N17.a | vBCFCP | Valor da Base de Cálculo do FCP | E | N17.0 | N | 1-1 | 13v2 | Informar o valor da Base de Cálculo do FCP | Gera a informação que consta no campo E140Pvd.BasFcp. |
| 178.03 | N17.b | pFCP | Percentual do Fundo de Combate à Pobreza (FCP) | E | N17.0 | N | 1-1 | 3v2-4 | Percentual relativo ao Fundo de Combate à Pobreza (FCP) | Gera a informação que consta no campo E140Pvd.AliFcp |
| 178.04 | N17.c | vFCP | Valor do Fundo de Combate à Pobreza (FCP) | E | N17.0 | N | 1-1 | 13v2 | Valor do ICMS relativo ao Fundo de Combate à Pobreza (FCP) | Gera a informação que consta no campo E140Pvd.VlrFcp. |
| 179 | N18 | modBCST | Modalidade de determinação da BC do ICMS ST | E | N03 | N | 1-1 | 1 | 0=Preço tabelado ou máximo sugerido; 1=Lista Negativa (valor); 2=Lista Positiva (valor); 3=Lista Neutra (valor); 4=Margem Valor Agregado (%); 5=Pauta (valor); 6=Valor da Operação (NT 2019.001) | Se ((ValorBaseICMS > 0) E (ValorBaseICMS) = (ValorBaseICMSST)) OU ((ValorLiquido - ValorICMSST) = (ValorBaseICMSST)) E a data de emissão da NF-e for maior ou igual a data do parâmetro global NT2019001, então gera o valor 6.  Senão, se o campo Critério Cálculo Substituição do cadastro do ICMS ST da tela F019TST for igual a 1, então gera o valor padrão igual a 4.  Se as condições anteriores não forem atendidas, então gera o valor padrão igual a 5. |
| 180 | N19 | pMVAST | Percentual da margem de valor Adicionado do ICMS ST | E | N03 | N | 0-1 | 3v2-4 |  | Gera a informação que consta no campo E019Sub.MarLuc do código do ICMS ST que está no item da nota fiscal. Pode ser alterado utilizando o identificador de regra VEN-140NEITE01 através da variável VSIntMarLuc. |
| 181 | N20 | pRedBCST | Percentual de Redução de BC do ICMS ST | E | N03 | N | 0-1 | 3v2-4 |  | Gera a informação que consta no campo E019Sub.MarLuc do código do ICMS ST que está no item da nota fiscal. Pode ser alterado utilizando o identificador de regra VEN-140NEITE01 através da variável VSIntMarLuc. |
| 182 | N21 | vBCST | Valor da BC do ICMS ST | E | N03 | N | 1-1 | 13v2 |  | Gera a informação que consta no campo E140Ipv.VlrBsi. |
| 183 | N22 | pICMSST | Alíquota do imposto do ICMS ST | E | N03 | N | 1-1 | 3v2-4 | Alíquota do ICMS ST sem o FCP. Quando for o caso, informar a alíquota do FCP no campo pFCP. | Gera a informação que consta no campo E019Sub.IcmEst do código do ICMS ST que está no item da nota fiscal. Pode ser alterado utilizando o identificador de regra VEN-140NEITE01 através da variável VSIntImpPcs. |
| 184 | N23 | vICMSST | Valor do ICMS ST | E | N03 | N | 1-1 | 13v2 | Valor do ICMS ST retido | Gera a informação que consta no campo E140Ipv.VlrIcs. |
| 184.0 | N23.1 | -x- | Sequência de XML | G | N03 |  | 0-1 |  | Grupo opcional. (Incluído na NT2016.002) | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 184.1 | N23a | vBCFCPST | Valor da Base de Cálculo do FCP retido por Substituição Tributária | E | N23.1 | N | 1-1 | 13v2 | Informar o valor da Base de Cálculo do FCP retido por Substituição Tributária | Gera a informação que consta no campo E140Pvd.BstFcp. |
| 184.2 | N23b | pFCPST | Percentual do FCP retido por Substituição Tributária | E | N23.1 | N | 1-1 | 3v2-4 | Percentual relativo ao Fundo de Combate à Pobreza (FCP) retido por substituição tributária | Gera a informação que consta no campo E140Pvd.AstFcp. |
| 184.4 | N23d | vFCPST | Valor do FCP retido por Substituição Tributária | E | N23.1 | N | 1-1 | 13v2 | Valor do ICMS relativo ao Fundo de Combate à Pobreza (FCP) retido por substituição tributária | Gera a informação que consta no campo E140Pvd.VstFcp. |

## Páginas relacionadas

* [VEN-140NEITE01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_140neite01.htm)
* [F019TST](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f019tst.htm)
