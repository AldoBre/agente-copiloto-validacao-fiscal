# Grupo S - COFINS

> **Fonte:** Leiautes NF-e e NFC-e — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/leiaute-nf-e-nfc-e.htm  
> **Trilha:** Segmentos > Compliance > Documentos Eletrônicos > NF-e | NFC-e (Nota Fiscal Eletrônica) > Nota Fiscal Eletrônica 4.0  
> **Telas citadas:** —  
> **Identificadores de regras:** —

---
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação | Origem |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 293 | S01 | COFINS | Grupo COFINS | G | M01 |  | 0-1 |  | Informar apenas um dos grupos S02, S03, S04 ou S04 com base valor atribuído ao campo de CST da COFINS | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 294 | S02 | COFINSAliq | Grupo COFINS tributado pela alíquota | CG | S01 |  | 1-1 |  |  | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 295 | S06 | CST | Código de Situação Tributária da COFINS | E | S02 | N | 1-1 | 2 | * 01 = Operação Tributável (base de cálculo = valor da operação alíquota normal (cumulativo/não cumulativo)) * 02 = Operação Tributável (base de cálculo = valor da operação (alíquota diferenciada)) | Gera por padrão o valor do campo E140Ipv.CstCof. |
| 296 | S07 | vBC | Valor da Base de Cálculo da COFINS | E | S02 | N | 1-1 | 13v2 |  | Gera por padrão o valor do campo E140Ipv.VlrBpi. |
| 297 | S08 | pCOFINS | Alíquota da COFINS (em percentual) | E | S02 | N | 1-1 | 3v2-4 |  | Gera por padrão o valor do campo E440Ipc.PerCim. |
| 298 | S11 | vCOFINS | Valor da COFINS | E | S02 | N | 1-1 | 13v2 |  | Gera por padrão o valor do campo E140Ipv.VlrPis. |
| 299 | S03 | COFINSQtde | Grupo de COFINS tributado por Qtde | CG | S01 |  | 1-1 |  |  | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 300 | S06 | CST | Código de Situação Tributária da COFINS | E | S03 | N | 1-1 | 2 | 03 = Operação Tributável (base de cálculo = quantidade vendida x alíquota por unidade de produto) | Gera por padrão o valor do campo E140Ipv.CstCof. |
| 301 | S09 | qBCProd | Quantidade Vendida | E | S03 | N | 1-1 | 12v0-4 |  | Gera por padrão o valor do campo E140Ipv.QtdBcf. |
| 302 | S10 | vAliqProd | Alíquota da COFINS (em reais) | E | S03 | N | 1-1 | 11v0-4 |  | Gera por padrão o valor do campo E140Ipv.AliCff. |
| 303 | S11 | vCOFINS | Valor da COFINS | E | S03 | N | 1-1 | 13v2 |  | Gera por padrão o valor do campo E140Ipv.VlrPis. |
| 304 | S04 | COFINSNT | Grupo COFINS não tributado | CG | S01 |  | 1-1 |  |  | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 305 | S06 | CST | Código de Situação Tributária da COFINS | E | S04 | N | 1-1 | 2 | * 04 = Operação Tributável (tributação monofásica, alíquota zero) * 05 = Operação Tributável (Substituição Tributária) * 06 = Operação Tributável (alíquota zero) * 07 = Operação Isenta da Contribuição * 08 = Operação Sem Incidência da Contribuição * 09 = Operação com Suspensão da Contribuição | Gera por padrão o valor do campo E140Ipv.CstCof. |
| 306 | S05 | COFINSOutr | Grupo COFINS Outras Operações | CG | S01 |  | 1-1 |  |  | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 307 | S06 | CST | Código de Situação Tributária da COFINS | E | S05 | N | 1-1 | 2 | Lista * 49 = Outras Operações de Saída * 50 = Operação com Direito a Crédito - Vinculada Exclusivamente a Receita Tributada no Mercado Interno * 51 = Operação com Direito a Crédito - Vinculada Exclusivamente a Receita Não Tributada no Mercado Interno * 52 = Operação com Direito a Crédito - Vinculada Exclusivamente a Receita de Exportação * 53 = Operação com Direito a Crédito - Vinculada a Receitas Tributadas e Não-Tributadas no Mercado Interno * 54 = Operação com Direito a Crédito - Vinculada a Receitas Tributadas no Mercado Interno e de Exportação * 55 = Operação com Direito a Crédito - Vinculada a Receitas Não-Tributadas no Mercado Interno e de Exportação * 56 = Operação com Direito a Crédito - Vinculada a Receitas Tributadas e Não-Tributadas no Mercado Interno, e de Exportação * 60 = Crédito Presumido - Operação de Aquisição Vinculada Exclusivamente a Receita Tributada no Mercado Interno * 61 = Crédito Presumido - Operação de Aquisição Vinculada Exclusivamente a Receita Não-Tributada no Mercado Interno * 62 = Crédito Presumido - Operação de Aquisição Vinculada Exclusivamente a Receita de Exportação * 63=Crédito Presumido - Operação de Aquisição Vinculada a Receitas Tributadas e Não-Tributadas no Mercado Interno * 64 = Crédito Presumido - Operação de Aquisição Vinculada a Receitas Tributadas no Mercado Interno e de Exportação * 65 = Crédito Presumido - Operação de Aquisição Vinculada a Receitas Não-Tributadas no Mercado Interno e de Exportação * 66 = Crédito Presumido - Operação de Aquisição Vinculada a Receitas Tributadas e Não-Tributadas no Mercado Interno, e de Exportação * 67 = Crédito Presumido - Outras Operações * 70 = Operação de Aquisição sem Direito a Crédito * 71 = Operação de Aquisição com Isenção * 72 = Operação de Aquisição com Suspensão * 73 = Operação de Aquisição a Alíquota Zero * 74 = Operação de Aquisição, sem incidência da Contribuição * 75 = Operação de Aquisição por Substituição Tributária * 98 = Outras Operações de Entrada * 99 = Outras Operações | Gera por padrão o valor do campo E140Ipv.CstCof. |
| 307.1 | S06.1 | -x- | Sequência XML | CG | S05 |  | 1-1 |  | Informar os campos S07 e S08 para cálculo da COFINS em percentual | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 308 | S07 | vBC | Valor da Base de Cálculo da COFINS | E | S06.1 | N | 1-1 | 13v2 |  | Gera por padrão o valor do campo E140Ipv.VlrBpi. |
| 309 | S08 | pCOFINS | Alíquota da COFINS (em percentual) | E | S06.1 | N | 1-1 | 3v2-4 |  | Gera por padrão o valor do campo E440Ipc.PerCim. |
| 309.1 | S08.1 | -x- | Sequência XML | CG | S05 |  | 1-1 |  | Informar os campos S09 e S10 para cálculo da COFINS em valor | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 310 | S09 | qBCProd | Quantidade Vendida | E | S08.1 | N | 1-1 | 12v0-4 |  | Gera por padrão o valor do campo E140Ipv.QtdBcf. |
| 311 | S10 | vAliqProd | Alíquota da COFINS (em reais) | E | S08.1 | N | 1-1 | 11v0-4 |  | Gera por padrão o valor do campo E140Ipv.AliCff. |
| 312 | S11 | vCOFINS | Valor da COFINS | E | S05 | N | 1-1 | 13v2 |  | Gera por padrão o valor do campo E140Ipv.VlrPis. |
