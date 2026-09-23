# Grupo N10g - Grupo CRT=1 (CSON 500)

> **Fonte:** Leiautes NF-e e NFC-e — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/leiaute-nf-e-nfc-e.htm  
> **Trilha:** Segmentos > Compliance > Documentos Eletrônicos > NF-e | NFC-e (Nota Fiscal Eletrônica) > Nota Fiscal Eletrônica 4.0  
> **Telas citadas:** E440RCI  
> **Identificadores de regras:** VEN-140NEITE01

---
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação | Origem |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 245.47 | N10g | ICMSSN500 | Grupo CRT=1 - Simples Nacional e CSON=500 | CG | N01 |  | 1-1 |  | Tributação ICMS pelo Simples Nacional, CSON=500 (v2.0) | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 245.48 | N11 | orig | Origem da mercadoria | E | N10g | N | 1-1 | 1 | 0 - Nacional, exceto as indicadas nos códigos 3, 4, 5 e 8; 1 - Estrangeira - Importação direta, exceto a indicada no código 6; 2 - Estrangeira - Adquirida no mercado interno, exceto a indicada no código 7; 3 - Nacional, mercadoria ou bem com Conteúdo de Importação superior a 40% e inferior a 70%; 4 - Nacional, cuja produção tenha sido feita em conformidade com os processos produtivos básicos de que tratam as legislações citadas nos Ajustes; 5 - Nacional, mercadoria ou bem com Conteúdo de Importação inferior ou igual a 40%; 6 - Estrangeira - Importação direta, sem similar nacional, constante em lista da CAMEX e gás natural; 7 - Estrangeira - Adquirida no mercado interno, sem similar nacional, constante lista CAMEX e gás natural; 8 - Nacional, mercadoria ou bem com Conteúdo de Importação superior a 70%. | Gera por padrão o valor do campo E140Ipv.OriMer. Pode ser alterado utilizando o identificador de regras VEN-140NEITE01, através da variável VSIntImpOri. |
| 245.49 | N12a | CSOSN | Código de Situação da Operação - Simples Nacional | E | N10g | N | 1-1 | 3 | 500=ICMS cobrado anteriormente por substituição tributária (substituído) ou por antecipação (v2.0) | Gera a informação que consta no campo E140Ipv.CodStr. |
| 245.50 | N25.1 | -x- | Sequência XML | G | N10g |  | 0-1 |  | Grupo opcional | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 245.50 | N26 | vBCSTRet | Valor da BC do ICMS ST retido | E | N25.1 | N | 1-1 | 13v2 | Valor da BC do ICMS ST cobrado anteriormente por ST (v2.0). O valor pode ser omitido quando a legislação não exigir a sua informação. (NT 2011/004) | Gera a informação que consta no campo E140Ipv.VlrBsd. |
| 245.50.0 | N26a | pST | Alíquota suportada pelo Consumidor Final | E | N25.1 | N | 1-1 | 3v2-4 | Deve ser informada a alíquota do cálculo do ICMS-ST, já incluso o FCP. Exemplo: alíquota da mercadoria na venda ao consumidor final = 18% e 2% de FCP. A alíquota a ser informada no campo pST deve ser 20%. (Atualizada NT2016.002) | Gera a informação que consta no campo E140Pvd.AreFcp. |
| 245.50.1 | N26b | vICMSSubstituto | Valor do ICMS próprio do Substituto | E | N25.1 | N | 0-1 | 13v2 | Valor do ICMS próprio do Substituto cobrado em operação anterior (Criado na NT 2018.005 v1.10. Atualizado na 2018.005 v1.20) | Gera a informação que consta no campo E140Ipv.VlrIsd. |
| 245.51 | N27 | vICMSSTRet | Valor do ICMS ST retido | E | N25.1 | N | 1-1 | 13v2 | Valor do ICMS ST cobrado anteriormente por ST (v2.0). O valor pode ser omitido quando a legislação não exigir a sua informação. 9NT 2011/004) | Gera a informação que consta no campo E140Ipv.VlrIsd. |
| 245.51.0 | N27.1 | -x- | Sequência XML | G | N10g |  | 0-1 |  | Grupo opcional. (Incluído na NT2016/002) | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 245.51w | N27a | vBCFCPSTRet | Valor da Base de Cálculo do FCP retido anteriormente | E | N27.1 | N | 1-1 | 13v2 | Informar o valor da Base de Cálculo do FCP retido anteriormente por ST | Gera a informação que consta no campo E140Pvd.BreFcp. |
| 245.51x | N27b | pFCPSTRet | Percentual do FCP retido anteriormente por Substituição Tributária | E | N27.1 | N | 1-1 | 3v2-4 | Percentual relativo ao Fundo de Combate à Pobreza (FCP) | Gera a informação que consta no campo E140Pvd.AreFcp. |
| 245.51y | N27d | vFCPSTRet | Valor do FCP retido anteriormente por Substituição Tributária | E | N27.1 | N | 1-1 | 13v2 | Valor do ICMS relativo ao Fundo de Combate à Pobreza (FCP) retido por substituição tributária | Gera a informação que consta no campo E140Pvd.VreFcp. |
| 245.51.1 | N33 | -x- | Sequência XML | G | N10g |  | 0-1 |  | Grupo opcional para informações do ICMS efetivo (Incluído na NT2016.002) | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 245.51.2 | N34 | pRedBCEfet | Percentual de redução da base de cálculo efetiva | E | N33 | N | 1-1 | 3v2-4 | Percentual de redução, caso estivesse submetida ao regime comum de tributação, para obtenção da base de cálculo efetiva (vBCEfet). Obs.: opcional a critério da UF. | Gera a informação que consta no campo E085Cli.UfsCli. |
| 245.51.3 | N35 | vBCEfet | Valor da base de cálculo efetiva | E | N33 | N | 1-1 | 13v2 | Valor da base de cálculo que seria atribuída à operação própria do contribuinte substituído, caso estivesse submetida ao regime comum de tributação, obtida pelo produto do Vprod por (1 - pRedBCEfet). Obs.: opcional a critério da UF. | Gera o valor fazendo o seguinte cálculo: (E140Ipv.VlrBru \* (1 - (E019Sub.RedIcm / 100)). |
| 245.51.4 | N36 | pICMSEfet | Alíquota do ICMS efetiva | E | N33 | N | 1-1 | 3v2-4 | Alíquota do ICMS na operação a consumidor final, caso estivesse submetida ao regime comum de tributação. Obs.: opcional a critério da UF. | Essa tag não é gerada, pois é opcional. |
| 245.51.5 | N37 | vICMSEfet | Valor do ICMS efetivo | E | N33 | N | 1-1 | 13v2 | Obtido pelo produto do valor do campo pICMSEfet pelo valor do campo vBCEfet, caso estivesse submetida ao regime comum de tributação. Obs.: opcional a critério da UF. | Gera o valor fazendo o seguinte cálculo: Valor da tag vBCEfet \* (E440RCI.PerIcs / 100). |

## Páginas relacionadas

* [VEN-140NEITE01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_140neite01.htm)
