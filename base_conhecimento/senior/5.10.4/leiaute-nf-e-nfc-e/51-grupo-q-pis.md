# Grupo Q - PIS

> **Fonte:** Leiautes NF-e e NFC-e — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/leiaute-nf-e-nfc-e.htm  
> **Trilha:** Segmentos > Compliance > Documentos Eletrônicos > NF-e | NFC-e (Nota Fiscal Eletrônica) > Nota Fiscal Eletrônica 4.0  
> **Telas citadas:** —  
> **Identificadores de regras:** —

---
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação | Origem |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 267 | Q01 | PIS | Grupo PIS | G | M01 |  | 0-1 |  | Informar apenas um dos grupos Q02, Q03, Q04 ou Q05 com base valor atribuído ao campo Q06 - CST do PIS | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 268 | Q02 | PISAliq | Grupo PIS tributado pela alíquota | CG | Q01 |  | 1-1 |  |  | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 269 | Q06 | CST | Código de Situação Tributária do PIS | E | Q02 | N | 1-1 | 2 | 01=Operação Tributável (base de cálculo = valor da operação alíquota normal (cumulativo/não cumulativo)); 02=Operação Tributável (base de cálculo = valor da operação (alíquota diferenciada)). | Gera a informação que consta no campo E140Ipv.CstPis. |
| 270 | Q07 | vBC | Valor da Base de Cálculo do PIS | E | Q02 | N | 1-1 | 13v2 |  | Gera a informação que consta no campo E140Ipv.VlrBpi. |
| 271 | Q08 | pPIS | Alíquota do PIS (em percentual) | E | Q02 | N | 1-1 | 3v2-4 |  | Gera a informação que consta no campo E440Ipc.PerPim. |
| 272 | Q09 | vPIS | Valor do PIS | E | Q02 | N | 1-1 | 13v2 |  | Gera a informação que consta no campo E140Ipv.VlrPis. |
| 273 | Q03 | PISQtde | Grupo PIS tributado por Qtde | CG | Q01 |  | 1-1 |  |  | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 274 | Q06 | CST | Código de Situação Tributária do PIS | E | Q03 | N | 1-1 | 2 | 03=Operação Tributável (base de cálculo = quantidade vendida x alíquota por unidade de produto) | Gera a informação que consta no campo E140Ipv.CstPis. |
| 275 | Q10 | qBCProd | Quantidade Vendida | E | Q03 | N | 1-1 | 12v0-4 |  | Gera a informação que consta no campo E140Ipv.QtdBpe. |
| 276 | Q11 | vAliqProd | Alíquota do PIS (em reais) | E | Q03 | N | 1-1 | 11v0-4 |  | Gera a informação que consta no campo E140Ipv.AliPif. |
| 277 | Q09 | vPIS | Valor do PIS | E | Q03 | N | 1-1 | 13v2 |  | Gera a informação que consta no campo E140Ipv.VlrPis. |
| 278 | Q04 | PISNT | Grupo PIS não tributado | CG | Q01 |  | 1-1 |  |  | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 279 | Q06 | CST | Código de Situação Tributária do PIS | E | Q04 | N | 1-1 | 2 | 04=Operação Tributável (tributação monofásica (alíquota zero)); 05=Operação Tributável (Substituição Tributária); 06=Operação Tributável (alíquota zero); 07=Operação Isenta da Contribuição; 08=Operação Sem Incidência da Contribuição; 09=Operação com Suspensão da Contribuição | Gera a informação que consta no campo E140Ipv.CstPis. |
| 280 | Q05 | PISOutr | Grupo PIS Outras Operações | CG | Q01 |  | 1-1 |  |  | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 281 | Q06 | CST | Código de Situação Tributária do PIS | E | Q05 | N | 1-1 | 2 | 49=Outras Operações de Saída; 50=Operações com Direito a Crédito - Vinculada Exclusivamente a Receita Tributada no Mercado Interno; 51=Operação com Direito a Crédito - Vinculada Exclusivamente a Receita Não Tributada no Mercado Interno; 52=Operação com Direito a Crédito - Vinculada Exclusivamente a Receita de Exportação; 53=Operação com Direito a Crédito - Vinculada a Receitas Tributadas e Não-Tributadas no Mercado Interno; 54=Operação com Direito a Crédito - Vinculada a Receitas Tributadas no Mercado Interno e de Exportação; 55=Operação com Direito a Crédito - Vinculada a Receitas Não-Tributadas no Mercado Interno e de Exportação; 56=Operação com Direito a Crédito - Vinculada a Receitas Tributadas e Não-Tributadas no Mercado Interno, e de Exportação; 60=Crédito Presumido - Operação de Aquisição Vinculada Exclusivamente a Receita Tributada no Mercado Interno; 61=Crédito Presumido - Operação de Aquisição Vinculada Exclusivamente a Receita Não-Tributada no Mercado Interno; 62=Crédito Presumido - Operação de Aquisição Vinculada Exclusivamente a Receita de Exportação; 63=Crédito Presumido - Operação de Aquisição Vinculada a Receitas Tributadas e Não-Tributadas no Mercado Interno; 64=Crédito Presumido - Operação de Aquisição Vinculada a Receitas Tributadas no Mercado Interno e de Exportação; 65=Crédito Presumido - Operação de Aquisição Vinculada a Receitas Não-Tributadas no Mercado Interno e de Exportação; 66=Crédito Presumido - Operação de Aquisição Vinculada a Receitas Tributadas e Não-Tributadas no Mercado Interno, e de Exportação; 67=Crédito Presumido - Outras Operações; 70=Operação de Aquisição sem Direito a Crédito; 71=Operação de Aquisição com Isenção; 72=Operação de Aquisição com Suspensão; 73=Operação de Aquisição a Alíquota Zero; 74=Operação de Aquisição, sem incidência da Contribuição; 75=Operação de Aquisição por Substituição Tributária; 98=Outras Operações de Entrada; 99=Outras Operações. | Gera a informação que consta no campo E140Ipv.CstPis. |
| 281.1 | Q06.1 | -x- | Sequência XML | CG | Q05 |  | 1-1 |  | Informar os campos Q07 e Q08 se o cálculo do PIS for em percentual | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 282 | Q07 | vBC | Valor da Base de Cálculo do PIS | E | Q06.1 | N | 1-1 | 13v2 |  | Gera a informação que consta no campo E140Ipv.VlrBpi. |
| 283 | Q08 | pPis | Alíquota do PIS (em percentual) | E | Q06.1 | N | 1-1 | 3v2-4 |  | Gera a informação que consta no campo E440Ipc.PerPim. |
| 283.1 | Q08.1 | -x- | Sequência XML | CG | Q05 |  | 1-1 |  | Informar os campos Q10 e Q11 se o cálculo do PIS for em valor | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
