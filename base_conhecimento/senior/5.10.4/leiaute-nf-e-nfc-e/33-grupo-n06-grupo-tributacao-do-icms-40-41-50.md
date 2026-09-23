# Grupo N06 - Grupo Tributação do ICMS= 40, 41, 50

> **Fonte:** Leiautes NF-e e NFC-e — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/leiaute-nf-e-nfc-e.htm  
> **Trilha:** Segmentos > Compliance > Documentos Eletrônicos > NF-e | NFC-e (Nota Fiscal Eletrônica) > Nota Fiscal Eletrônica 4.0  
> **Telas citadas:** E001TVE, E140IPV  
> **Identificadores de regras:** VEN-140NEITE01

---
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação | Origem |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 202 | N06 | ICMS40 | Grupo Tributação do ICMS = 40, 41, 50 | CG | N01 |  | 1-1 |  | Tributação Isenta, Não Tributada ou Suspensão | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 203 | N11 | orig | Origem da mercadoria | E | N06 | N | 1-1 | 1 | 0 - Nacional, exceto as indicadas nos códigos 3, 4, 5 e 8; 1 - Estrangeira - Importação direta, exceto a indicada no código 6; 2 - Estrangeira - Adquirida no mercado interno, exceto a indicada no código 7; 3 - Nacional, mercadoria ou bem com Conteúdo de Importação superior a 40% e inferior ou igual a 70%; 4 - Nacional, cuja produção tenha sido feita em conformidade com os processos produtivos básicos de que tratam as legislações citadas nos Ajustes; 5 - Nacional, mercadoria ou bem com Conteúdo de Importação inferior ou igual a 40%; 6 - Estrangeira - Importação direta, sem similar nacional, constante na lista da CAMEX e gás natural; 7 - Estrangeira - Adquirida no mercado interno, sem similar nacional, constante na lista CAMEX e gás natural; 8 - Nacional, mercadoria ou bem com Conteúdo de Importação superior a 70% | Gera por padrão o valor do campo E140Ipv.OriMer. Pode ser alterado utilizando o identificador de regra VEN-140NEITE01 através da variável VSIntImpOri. |
| 204 | N12 | CST | Tributação do ICMS = 40, 41 ou 50 | E | N06 | N | 1-1 | 2 | 40=Isenta; 41=Não Tributada; 50=Suspensão | Gera por padrão o valor do campo E140Ipv.OriMer + E140Ipv.CodStr. Pode ser alterado utilizando o identificador de regra VEN-140NEITE01 através da variável VSIntImpCst. |
| 204.00 | N27.1 | -x- | Sequência XML | G | N06 |  | 0-1 |  | Grupo Opcional | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 204.01 | N28a | vICMSDeson | Valor do ICMS | E | N27.1 | N | 1-1 | 13v2 | Informar nas operações: a) com produtos beneficiados com a desoneração condicional do ICMS; b) destinados à SUFRAMA, informando-se o valor que seria devido se não houvesse isenção; c) de venda à órgão da administração pública direta e suas fundações e autarquias com isenção do ICMS (NT 2011/004); d) demais casos solicitados pelo Fisco (NT2016.002) | Gera a informação que consta no campo E140Ipv.VlrIcd. |
| 204.02 | N28 | motDesICMS | Motivo da desoneração do ICMS | E | N27.1 | N | 1-1 | 2 | Campo será preenchido quando o campo anterior estiver preenchido. Informar o motivo da desoneração: 1=Táxi; 3=Produtor Agropecuário; 4=Frotista/Locadora; 5=Diplomático/Consular; 6=Utilitários e Motocicletas da Amazônia Ocidental e Áreas de Livre Comércio (Resolução 714/88 e 790/94 - CONTRAN e suas alterações); 7=SUFRAMA; 8=Venda a Órgão Público; 9=Outros (NT 2011/004); 10=Deficiente Condutor (Convênio ICMS 38/12); 11=Deficiente Não Condutor (Convênio ICMS 38/12); 16=Olimpíadas Rio 2016 (NT 2015.002); 90=Solicitado pelo Fisco (NT2016.002); Revogada a partir da versão 3.10 a possibilidade de usar o motivo 2=Deficiente Físico | Gera a informação que consta no campo E140ipv.MotDes. |
| 204.03 | N28b | indDeduzDeson | Indica se o valor do ICMS desonerado (vICMSDeson) deduz do valor do item (vProd). | E | N27.1 | N | 0-1 | 1 | O campo só pode ser preenchido com: 0=Valor do ICMS desonerado (vICMSDeson) não deduz do valor do item (vProd) / total da NF-e. 1=Valor do ICMS desonerado (vICMSDeson) deduz do valor do item (vProd) / total da NF-e. | Gera a informação conforme o E001TVE.IcmDes e campo E140IPV.MotDes. E001TVE.IcmDes = "S - Sim" ou campo E140IPV.MotDes = "7 - Suframa" a tag vICMSDeson = 1, E001TVE.IcmDes = "N - Não" e campo E140IPV.MotDes <> "7 - Suframa" a tag vICMSDeson = 2. |

## Páginas relacionadas

* [VEN-140NEITE01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_140neite01.htm)
