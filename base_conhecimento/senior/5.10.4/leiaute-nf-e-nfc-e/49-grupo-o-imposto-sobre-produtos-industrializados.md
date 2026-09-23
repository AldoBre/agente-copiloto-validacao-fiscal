# Grupo O - Imposto sobre Produtos Industrializados

> **Fonte:** Leiautes NF-e e NFC-e — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/leiaute-nf-e-nfc-e.htm  
> **Trilha:** Segmentos > Compliance > Documentos Eletrônicos > NF-e | NFC-e (Nota Fiscal Eletrônica) > Nota Fiscal Eletrônica 4.0  
> **Telas citadas:** —  
> **Identificadores de regras:** —

---
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação | Origem |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 246 | O01 | IPI | Grupo IPI | CG | M01 |  | 0-1 |  | Informar apenas quando o item for sujeito ao IPI | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 248 | O03 | CNPJProd | CNPJ do produtor da mercadoria, quando for diferente do emitente. Somente para os casos de exportação direta ou indireta | E | O01 | N | 0-1 | 14 | Informar os zeros não significativos | Essa tag não é gerada pelo ERP. |
| 249 | O04 | cSelo | Código do selo de controle IPI | E | O01 | C | 0-1 | 1 - 60 | Preenchimento conforme Anexo II -- A da Instrução Normativa RFB Nº 770/2007 (atualizado na NT 2016.002):  | Tipo de selo | Código | Cor do selo | | --- | --- | --- | | Produto Nacional | 9710-01 | Verde combinado com marrom | | Produto Nacional para Exportação - Tipo "1" | 9710-10 | Verde Escuro combinado com marrom | | Produto Nacional para Exportação - Tipo "2" | 9710-11 | Verde Escuro combinado com marrom | | Produto Nacional para Exportação - Tipo "3" | 9710-12 | Verde Escuro combinado com marrom | | Produto Estrangeiro | 8610-09 | Vermelho combinado com azul | | Essa tag não é gerada pelo ERP. |
| 250 | O05 | qSelo | Quantidade de selo de controle | E | O01 | N | 0-1 | 1 - 12 |  | Essa tag não é gerada pelo ERP. |
| 251 | O06 | cEnq | Código de Enquadramento Legal do IPI | E | O01 | N | 1-1 | 1 - 3 | Preenchimento conforme seção 8.9 do MOC - Visão Geral (Tabela do Código de Enquadramento do IPI) | Gera a tag conforme o valor do campo E140Ipv.CodEnq. |
| 252 | O07 | IPITrib | Grupo do CST 00, 49, 50 e 99 | CG | O01 |  | 1-1 |  | Informar apenas um dos grupos O07 ou O08 com base no valor atribuído ao campo O09 - CST do IPI | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 253 | O09 | CST | Código da situação tributária do IPI | E | O07 | N | 1-1 | 2 | 00=Entrada com recuperação de crédito; 49=Outras entradas; 50=Saída tributada; 99=Outras saídas | Gera por padrão o valor do campo E140Ipv.CstIpi. |
| 253,1 | O09.1 | -x- | Sequência XML | CG | O07 |  | 1-1 |  | Informar os campos O10 e O13 se o cálculo do IPI for por alíquota | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 254 | O10 | vBC | Valor da BC do IPI | E | O09.1 | N | 1-1 | 13v2 |  | Gera por padrão o valor do campo E140Ipv.VlrBip. |
| 257 | O13 | pIPI | Alíquota do IPI | E | O09.1 | N | 1-1 | 3v2-4 |  | Gera por padrão o valor do campo E140Ipv.VlrIpi. |
| 257,1 | O13.1 | -x- | Sequência XML | CG | O07 |  | 1-1 |  | Informar os campos O11 e O12 se o cálculo do IPI for de valor por unidade | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 255 | O11 | qUnid | Quantidade total na unidade padrão para tributação (somente para os produtos tributados por unidade) | E | O13.1 | N | 1-1 | 12v0-4 | Informar os campos O11 e O12 se o cálculo do IPI for de valor por unidade | Gera por padrão o valor do campo E140Ipv.QtdBip. |
| 256 | O12 | vUnid | Valor por Unidade Tributável | E | O13.1 | N | 1-1 | 11v0-4 | Informar os campos O11 e O12 se o cálculo do IPI for de valor por unidade | Gera por padrão o valor do campo E140Ipv.AliIpi. |
| 259 | O14 | vIPI | Valor do IPI | E | O07 | N | 1-1 | 13v2 | Informar os campos O11 e O12 se o cálculo do IPI for de valor por unidade | Gera por padrão o valor do campo E140Ipv.VlrIpi. |
| 260 | O08 | IPINT | Grupo CST 01, 02, 03, 04, 51, 52, 53 | CG | O01 |  | 1-1 |  |  | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 261 | O09 | CST | Código da situação tributária do IPI | E | O08 | C | 1-1 | 2 | Código da situação tributária do IPI: 01=Entrada tributada com alíquota zero; 02=Entrada isenta; 03=Entrada não tributada; 04=Entrada imune; 05=Entrada com suspensão; 51=Saída tributada com alíquota zero; 52=Saída isenta; 53=Saída não-tributada; 54=Saída imune; 55=Saída com suspensão. | Gera por padrão o valor do campo E140Ipv.CstIpi. |
