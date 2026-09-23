# Grupo N08 - Grupo Tributação do ICMS= 60

> **Fonte:** Leiautes NF-e e NFC-e — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/leiaute-nf-e-nfc-e.htm  
> **Trilha:** Segmentos > Compliance > Documentos Eletrônicos > NF-e | NFC-e (Nota Fiscal Eletrônica) > Nota Fiscal Eletrônica 4.0  
> **Telas citadas:** E440RCI  
> **Identificadores de regras:** VEN-140NEITE01

---
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação | Origem |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 213 | N08 | ICMS60 | Grupo Tributação do ICMS = 60 | CG | N01 |  | 1-1 |  | Tributação ICMS cobrado anteriormente por substituição tributária | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ |
| 214 | N11 | orig | Origem da mercadoria | E | N08 | N | 1-1 | 1 | 0 - Nacional, exceto as indicadas nos códigos 3, 4, 5 e 8; 1 - Estrangeira - Importação direta, exceto a indicada no código 6; 2 - Estrangeira - Adquirida no mercado interno, exceto a indicada no código 7; 3 - Nacional, mercadoria ou bem com Conteúdo de Importação superior a 40% e inferior ou igual a 70%; 4 - Nacional, cuja produção tenha sido feita em conformidade com os processos produtivos básicos de que tratam as legislações citadas nos Ajustes; 5 - Nacional, mercadoria ou bem com Conteúdo de Importação inferior ou igual a 40%; 6 - Estrangeira - Importação direta, sem similar nacional, constante na lista da CAMEX e gás natural; 7 - Estrangeira - Adquirida no mercado interno, sem similar nacional, constante na lista CAMEX e gás natural; 8 - Nacional, mercadoria ou bem com Conteúdo de Importação superior a 70% | Gera por padrão o valor do campo E140Ipv.OriMer. Pode ser alterado utilizando o identificador de regra VEN-140NEITE01 através da variável VSIntImpOri |
| 215 | N12 | CST | Tributação do ICMS = 60 | E | N08 | N | 1-1 | 2 | 60=ICMS cobrado anteriormente por substituição tributária | Gera por padrão o valor do campo E140Ipv.OriMer + E140Ipv.CodStr. Pode ser alterado utilizando o identificador de regra VEN-140NEITE01 através da variável VSIntImpCst |
| 215.1 | N25.1 | -x- | Sequência XML | G | N08 |  | 0-1 |  | Grupo opcional | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 216 | N26 | vBCSTRet | Valor da BC do ICMS ST retido | E | N25.1 | N | 1-1 | 13v2 | Valor da BC do ICMS ST cobrado anteriormente por ST (v2.0). O valor pode ser omitido quando a legislação não exigir a sua informação. (NT 2011/004) | Gera a informação que consta no campo E140Ipv.VlrBsd. |
| 216.1 | N26a | pST | Alíquota suportada pelo Consumidor Final | E | N25.1 | N | 1-1 | 3v2-4 | Deve ser informada a alíquota do cálculo do ICMS-ST, já incluso o FCP caso incida sobre a mercadoria. Exemplo: alíquota da mercadoria na venda ao consumidor final = 18% e 2% de FCP. A alíquota a ser informada no campo pST deve ser 20%. (Atualizado NT2016.002) | Gera a informação que consta no campo E140Pvd.AreFcp |
| 216.2 | N26b | vICMSSubstituto | Valor do ICMS próprio do Substituto | E | N25.1 | N | 0-1 | 13v2 | Valor do ICMS próprio do Substituto cobrado em operação anterior (Criado na NT 2018.005. Atualizado na NT 2018.005 v1.20) | Gera a informação que consta nos campos E140Ipv.VlrBsd, E140Ipv.VlrIsd , E140Pvd.AreFcp |
| 217 | N27 | vICMSSTRet | Valor do ICMS ST retido | E | N25.1 | N | 1-1 | 13v2 | Valor do ICMS ST cobrado anteriormente por ST (v2.0). O valor pode ser omitido quando a legislação não exigir a sua informação. (NT 2011/004) | Gera a informação que consta no campo E140Ipv.VlrIsd. |
| 217.0 | N27.1 - | -x- | Sequência XML | G | N08 |  | 0-1 |  | Grupo opcional. (Incluído na NT2016.002) | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ |
| 217.w | N27a | vBCFCPSTRet | Valor da Base de Cálculo do FCP retido anteriormente | E | N27.1 | N | 1-1 | 13v2 | Informar o valor da Base de Cálculo do FCP retido anteriormente por ST | Gera a informação que consta no campo E140Pvd.BreFcp |
| 217.x | N27b | pFCPSTRet | Percentual do FCP retido anteriormente por Substituição Tributária | E | N27.1 | N | 1-1 | 3v2-4 | Percentual relativo ao Fundo de Combate à Pobreza (FCP) retido por substituição tributária | Gera a informação que consta no campo E140Pvd.AreFcp |
| 217.y | N27d | vFCPSTRet | Valor do FCP retido por Substituição Tributária | E | N27.1 | N | 1-1 | 13v2 | Valor do ICMS relativo ao Fundo de Combate à Pobreza (FCP) retido por substituição tributária | Gera a informação que consta no campo E140Pvd.VreFcp |
| 217.1 | N33 | -x- | Sequência XML | G | N08 |  | 0-1 |  | Grupo opcional para informações do ICMS Efetivo (Incluído na NT2016.002) | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ |
| 217.2 | N34 | pRedBCEfet | Percentual de redução da base de cálculo efetiva | E | N33 | N | 1-1 | 3v2-4 | Percentual de redução, caso estivesse submetida ao regime comum de tributação, para obtenção da base de cálculo efetiva (vBCEfet). OBS.: opcional a critério da UF | Gera a informação que consta no campo E085Cli.UfsCli |
| 217.3 | N35 | vBCEfet | Valor da base de cálculo efetiva | E | N33 | N | 1-1 | 13v2 | Valor da base de cálculo que seria atribuída à operação própria do contribuinte substituído, caso estivesse submetida ao regime comum de tributação, obtida pelo produto do Vprod por (1- pRedBCEfet). Obs.: opcional a critério da UF | Gera o valor realizando o cálculol a seguir: (E140Ipv.VlrBru \* (1 - (E019Sub.RedIcm / 100)) |
| 217.4 | N36 | pICMSEfet | Alíquota do ICMS efetiva | E | N33 | N | 1-1 | 3v2-4 | Alíquota do ICMS na operação a consumidor final, caso estivesse submetida ao regime comum de tributação. Obs.: opcional a critério da UF | Essa tag não é gerada, pois é opcional |
| 217.5 | N37 | vICMSEfet | Valor do ICMS efetivo | E | N33 | N | 1-1 | 13v2 | Obtido pelo produto do valor do campo pICMSEfet pelo valor do campo vBCEfet, caso estivesse submetida ao regime comum de tributação. Obs.: opcional a critério da UF | Gera o valor realizando o cálculo a seguir: Valor da tag vBCEfet \* (E440RCI.PerIcs / 100) |

## Páginas relacionadas

* [VEN-140NEITE01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_140neite01.htm)
