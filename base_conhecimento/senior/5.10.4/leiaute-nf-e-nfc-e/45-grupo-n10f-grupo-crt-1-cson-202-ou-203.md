# Grupo N10f - Grupo CRT=1 (CSON 202 ou 203)

> **Fonte:** Leiautes NF-e e NFC-e — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/leiaute-nf-e-nfc-e.htm  
> **Trilha:** Segmentos > Compliance > Documentos Eletrônicos > NF-e | NFC-e (Nota Fiscal Eletrônica) > Nota Fiscal Eletrônica 4.0  
> **Telas citadas:** F019TST  
> **Identificadores de regras:** VEN-140NEITE01

---
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação | Origem |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 245.38 | N10f | ICMSSN202 | Grupo CRT=1 - Simples Nacional e CSON=202 ou 203 | CG | N01 |  | 1-1 |  | Tributação ICMS pelo Simples Nacional, CSON=202 ou 203 (v2.0) | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 245.39 | N11 | orig | Origem da mercadoria | E | N10f | N | 1-1 | 1 | 0 - Nacional, exceto as indicadas nos códigos 3, 4, 5 e 8; 1 - Estrangeira - Importação direta, exceto a indicada no código 6; 2 - Estrangeira - Adquirida no mercado interno, exceto a indicada no código 7; 3 - Nacional, mercadoria ou bem com Conteúdo de Importação superior a 40% e inferior a 70%; 4 - Nacional, cuja produção tenha sido feita em conformidade com os processos produtivos básicos de que tratam as legislações citadas nos Ajustes; 5 - Nacional, mercadoria ou bem com Conteúdo de Importação inferior ou igual a 40%; 6 - Estrangeira - Importação direta, sem similar nacional, constante em lista da CAMEX e gás natural; 7 - Estrangeira - Adquirida no mercado interno, sem similar nacional, constante lista CAMEX e gás natural; 8 - Nacional, mercadoria ou bem com Conteúdo de Importação superior a 70%. | Gera por padrão o valor do campo E140Ipv.OriMer. Pode ser alterado utilizando o identificador de regras VEN-140NEITE01 através da variável VSIntImpOri. |
| 245.40 | N12a | CSOSN | Código de Situação da Operação - Simples Nacional | E | N10f | N | 1-1 | 3 | 202=Tributada pelo Simples Nacional sem permissão de crédito e com cobrança do ICMS por Substituição Tributária; 203=Isenção do ICMS nos Simples Nacional para faixa de receita bruta e com cobrança do ICMS por Substituição Tributária (v2.0) | Gera a informação que consta no campo E140Ipv.CodStr. |
| 245.41 | N18 | modBCST | Modalidade de determinação da BC do ICMS ST | E | N10f | N | 1-1 | 1 | 0=Preço tabelado ou máximo sugerido; 1=Lista Negativa (valor); 2=Lista Positiva (valor); 3=Lista Neutra (valor); 4=Margem Valor Agregado (%); 5=Pauta (valor) | Se ((ValorBaseICMS > 0) E (ValorBaseICMS) = (ValorBaseICMSST)) OU ((ValorLiquido - ValorICMSST) = (ValorBaseICMSST)) E a data de emissão da NF-e for maior ou igual a data do parâmetro global NT2019001, então gera o valor 6. Senão.  Se o campo Critério Cálculo Substituição do cadastro do ICMS ST da tela F019TST for 1, então gera o valor padrão igual a 4.  Se as condições anteriores não forem atendidas, então gera o valor padrão igual a 5. |
| 245.42 | N19 | pMVAST | Percentual da margem de valor Adicionado do ICMS ST | E | N10f | N | 0-1 | 3v2-4 | (v2.0) | Gera a informação que consta no campo E019Sub.MarLuc do código do ICMS ST que está no item da nota fiscal. Pode ser alterado utilizando o identificador de regra VEN-140NEITE01 através da variável VSIntMarLuc. |
| 224.43 | N20 | pRedBCST | Percentual da Redução de BC do ICMS ST | E | N10f | N | 0-1 | 3v2-4 | (v2.0) | Gera a informação que consta no campo E019Sub.MarLuc do código do ICMS ST que está no item da nota fiscal. Pode ser alterado utilizando o identificador de regra VEN-140NEITE01 através da variável VSIntMarLuc. |
| 245.44 | N21 | vBCST | Valor da BC do ICMS ST | E | N10f | N | 1-1 | 13v2 | (v2.0) | Gera a informação que consta no campo E140Ipv.VlrBsi. |
| 245.45 | N22 | pICMSST | Alíquota do imposto do ICMS ST | E | N10f | N | 1-1 | 3v2-4 | Alíquota do ICMS ST sem o FCP. Quando for o caso, informar a alíquota do FCP no campo pFCP (Atualizado NT2016.002) | Gera a informação que consta no campo E019Sub.IcmEst do código do ICMS ST que está no item da nota fiscal. Pode ser alterado utilizando o identificador de regra VEN-140NEITE01 através da variável VSIntImpPcs. |
| 245.46 | N23 | vICMSST | Valor do ICMS ST | E | N10f | N | 1-1 | 13v2 | Valor do ICMS ST retido (v2.0) | Gera a informação que consta no campo E140Ipv.VlrIcs. |
| 245.46.0 | N23.1- | -x- | Sequência XML | G | N10.f |  | 0-1 |  | Grupo opcional (Incluído na NT 2016.002) | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 245.46w | N23a | vBCFCPST | Valor da Base de Cálculo do FCP | E | N23.1 | N | 1-1 | 13v2 | Informar o valor da Base de Cálculo do FCP retido por Substituição Tributária | Gera a informação que consta no campo E140Pvd.BstFcp. |
| 245.46x | N23b | pFCPST | Percentual do FCP retido por Substituição Tributária | E | N23.1 | N | 1-1 | 3v2-4 | Percentual relativo ao Fundo de Combate à Pobreza (FCP) retido por substituição tributária. Obs.: Percentual máximo de 2%, conforme a legislação. | Gera a informação que consta no campo E140Pvd.AstFcp. |
| 245.46y | N23d | vFCPST | Valor do FCP retido por Substituição Tributária | E | N23.1 | N | 1-1 | 13v2 | Valor do ICMS relativo ao Fundo de Combate à Pobreza (FCP) retido por substituição tributária | Gera a informação que consta no campo E140Pvd.VstFcp. |

## Páginas relacionadas

* [VEN-140NEITE01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_140neite01.htm)
