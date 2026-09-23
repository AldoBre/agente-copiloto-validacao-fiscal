# Grupo N04 - Grupo Tributação do ICMS= 20

> **Fonte:** Leiautes NF-e e NFC-e — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/leiaute-nf-e-nfc-e.htm  
> **Trilha:** Segmentos > Compliance > Documentos Eletrônicos > NF-e | NFC-e (Nota Fiscal Eletrônica) > Nota Fiscal Eletrônica 4.0  
> **Telas citadas:** E001TVE, E140IPV  
> **Identificadores de regras:** VEN-140NEITE01

---
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação | Origem |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 185 | N04 | ICMS20 | Grupo Tributação do ICMS = 20 | CG | N01 |  | 1-1 |  | Tributação com redução de base de cálculo | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 186 | N11 | orig | Origem da mercadoria | E | N04 | N | 1-1 | 1 | 0 - Nacional, exceto as indicadas nos códigos 3, 4, 5 e 8; 1 - Estrangeira - Importação direta, exceto a indicada no código 6; 2 - Estrangeira - Adquirida no mercado interno, exceto a indicada no código 7; 3 - Nacional, mercadoria ou bem com Conteúdo de Importação superior a 40% e inferior ou igual a 70%; 4 - Nacional, cuja produção tenha sido feita em conformidade com os processos produtivos básicos de que tratam as legislações citadas nos Ajustes; 5 - Nacional, mercadoria ou bem com Conteúdo de Importação inferior ou igual a 40%; 6 - Estrangeira - Importação direta, sem similar nacional, constante na lista da CAMEX e gás natural; 7 - Estrangeira - Adquirida no mercado interno, sem similar nacional, constante na lista CAMEX e gás natural; 8 - Nacional, mercadoria ou bem com Conteúdo de Importação superior a 70% | Gera por padrão o valor do campo E140Ipv.OriMer. Pode ser alterado utilizando o identificador de regra VEN-140NEITE01 através da variável VSIntImpOri. |
| 187 | N12 | CST | Tributação do ICMS = 20 | E | N04 | N | 1-1 | 2 | 20=Com redução de base de cálculo | Gera por padrão o valor do campo E140Ipv.OriMer + E140Ipv.CodStr. Pode ser alterado utilizando o identificador de regra VEN-140NEITE01 através da variável VSIntImpCst. |
| 188 | N13 | modBC | Modalidade de determinação da BC do ICMS | E | N04 | N | 1-1 | 1 | 0=Margem Valor Agregado (%); 1=Pauta (Valor); 2=Preço Tabelado Máx. (valor); 3=Valor da operação | Verifica o valor do campo E140Ipv.CodBic para buscar o valor do campo E019Tst.CalSub e gerar na tag. Pode ser alterado utilizando o identificador de regra VEN-140NEITE01 através da variável VSIntImpMbc. |
| 189 | N14 | pRedBC | Percentual da Redução de BC | E | N04 | N | 1-1 | 3v2-4 |  | Gera a informação que consta no campo E019Red.RedEnt. Pode ser alterado utilizando o identificador de regra VEN-140NEITE01 variável VSIntImpRbc. |
| 190 | N15 | vBC | Valor da BC do ICMS | E | N04 | N | 1-1 | 13v2 |  | Gera a informação que consta no campo E140Ipv.VlrBic. |
| 191 | N16 | pICMS | Alíquota do imposto | E | N04 | N | 1-1 | 3v2-4 | Alíquota do ICMS sem o FCP. Quando for o caso, informar a alíquota do FCP no campo pFCP | Gera a informação que consta no campo E140Ipv.PerIcm. |
| 192 | N17 | vICMS | Valor do ICMS | E | N04 | N | 1-1 | 13v2 |  | Gera a informação que consta no campo E140Ipv.VlrIcm. |
| 192.0 | N17.1 | -x- | Sequência XML | G | N04 |  | 0-1 |  | Grupo opcional. (Incluído na NT2016.002) | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 192.w | N17a | vBCFCP | Valor da Base de Cálculo do FCP | E | N17.1 | N | 1-1 | 13v2 | Informar o valor da Base de Cálculo do FCP | Gera a informação que consta no campo E140Pvd.BasFcp. |
| 192.x | N17b | pFCP | Percentual do ICMS relativo ao Fundo de Combate à Pobreza (FCP) | E | N17.1 | N | 1-1 | 3v2-4 | Percentual relativo ao Fundo de Combate à Pobreza (FCP) | Gera a informação que consta no campo E140Pvd.AliFcp. |
| 192.y | N17c | vFCP | Valor do ICMS relativo ao Fundo de Combate à Pobreza (FCP) | E | N17.1 | N | 1-1 | 13v2 | Valor do ICMS relativo ao Fundo de Combate à Pobreza (FCP) | Gera a informação que consta no campo E140Pvd.AliFcp. |
| 192.1 | N27.1 | -x- | Sequência XML | G | N04 |  | 0-1 |  | Grupo opcional | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 192.2 | N28a | vICMSDeson | Valor do ICMS desonerado | E | N27.1 | N | 1-1 | 13v2 | Informar apenas nos motivos de desoneração documentados abaixo. | Gera a informação que consta no campo E140Ipv.VlrIcd. |
| 192.3 | N28 | motDesICMS | Motivo da desoneração do ICMS | E | N27.1 | N | 1-1 | 2 | Campo será preenchido quando o campo anterior estiver preenchido. Informar o motivo da desoneração: 3=Uso na agropecuária; 9=Outros; 10=Deficiente Condutor (Convênio ICMS 38/12); 11=Deficiente Não Condutor (Convênio ICMS 38/12); 12=Órgão de fomento e desenvolvimento agropecuário. | Gera a informação que consta no campo E140Ipv.MotDes. |
| 192.4 | N28b | indDeduzDeson | Indica se o valor do ICMS desonerado (vICMSDeson) deduz do valor do item (vProd). | E | N27.1 | N | 0-1 | 1 | O campo só pode ser preenchido com: 0=Valor do ICMS desonerado (vICMSDeson) não deduz do valor do item (vProd) / total da NF-e. 1=Valor do ICMS desonerado (vICMSDeson) deduz do valor do item (vProd) / total da NF-e. | Gera a informação conforme o E001TVE.IcmDes e campo E140IPV.MotDes. E001TVE.IcmDes = "S - Sim" ou campo E140IPV.MotDes = "7 - Suframa" a tag vICMSDeson = 1, E001TVE.IcmDes = "N - Não" e campo E140IPV.MotDes <> "7 - Suframa" a tag vICMSDeson = 2. |

## Páginas relacionadas

* [VEN-140NEITE01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_140neite01.htm)
