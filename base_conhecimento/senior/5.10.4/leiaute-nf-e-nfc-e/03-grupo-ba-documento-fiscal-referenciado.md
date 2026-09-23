# Grupo BA - Documento Fiscal Referenciado

> **Fonte:** Leiautes NF-e e NFC-e — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/leiaute-nf-e-nfc-e.htm  
> **Trilha:** Segmentos > Compliance > Documentos Eletrônicos > NF-e | NFC-e (Nota Fiscal Eletrônica) > Nota Fiscal Eletrônica 4.0  
> **Telas citadas:** E140NFV, F050EQF, F070FVE, F140NSR, F440GNE, F440NFR  
> **Identificadores de regras:** —

---
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação | Origem |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 29x.1 | BA01 | NFref | Informação de Documentos Fiscais referenciados | G | B01 |  | 0-500 |  | Grupo com informações de Documentos Fiscais referenciados. Informação utilizada nas hipóteses previstas na legislação. (Ex.: Devolução de mercadorias, Substituição de NF cancelada, Complementação de NF, etc.). | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 29x.2 | BA02 | refNFe | Chave de acesso da NF-e referenciada | CE | BA01 | N | 1-1 | 44 | Referencia uma NF-e (modelo 55) emitida anteriormente, vinculada a NF-e atual, ou uma NFC-e (modelo 65) | NF de saída tipo "2- NF Devolução" gera nessa tag a informação do campo Chave NF-e da tela F440GNE da NF de entrada que está sendo devolvida. Para outros tipos de NF de saída, caso o parâmetro Gera NFRef da tela F070FVE, guia Vendas 2, estiver como "S - Sim", gera a tag com as NF que foram referenciadas na tela F140NSR.   Para NF de entrada do tipo 3 gera nessa tag a informação do campo Chave do documento eletrônico (ChvDoe) da tabela Vendas - Notas Fiscais de Saída - Dados Gerais (E140NFV) da NF de saída que foi vinculada na NF de entrada. Para os outros tipos de NF, caso o parâmetro Gera NFRef da tela F070FVE, guia Vendas 2, estiver como "S - Sim", gera a tag com as NF que foram referenciadas na tela F440NFR. |
| 29x.3 | BA03 | refNF | Informação da NF modelo 1/1A ou NF modelo 2 referenciada (alterado pela NT2016.002) | CG | BA01 |  | 1-1 |  |  | Esse grupo é gerado quando a série da NF que está sendo vinculada tem o campo Espécie Documento como" 01" ou "02". |
| 29x.4 | BA04 | cUF | Código da UF do emitente | E | BA03 | N | 1-1 | 2 | Utilizar a Tabela do IBGE (Seção 8.1 do MOC Visão Geral- Tabela de UF, Município e País) | Verifica a UF do cliente/fornecedor emitente da NF referenciada.   Baseado na UF é gerado o código conforme tabela de UF do código IBGE. |
| 29x.5 | BA05 | AAMM | Ano e Mês de emissão da NF-e | E | BA03 | N | 1-1 | 4 | AAMM da emissão da NF | Ano e mês de emissão da NF de entrada/saída que está sendo devolvida/referenciada. |
| 29x.6 | BA06 | CNPJ | CNPJ do emitente | E | BA03 | N | 1-1 | 14 | Informar o CNPJ do emitente da NF | CNPJ do emitente da NF de entrada/saída que está sendo devolvida/referenciada. |
| 29x.7 | BA07 | mod | Modelo do Documento Fiscal | E | BA03 | N | 1-1 | 2 | 01=modelo 01 02=modelo 02 (incluído na NT2016.002) | Espécie de documento que consta na NF de entrada/saída que está sendo devolvida/referenciada. |
| 29x.8 | BA08 | serie | Série do Documento Fiscal | E | BA03 | N | 1-1 | 1 - 3 | Informar zero se não utilizada Série do documento fiscal. | Campo Série/Subsérie Legal que está informado na NF de entrada/saída que está sendo devolvida/referenciada. |
| 29x.9 | BA09 | nNF | Número do Documento Fiscal | E | BA03 | N | 1-1 | 1 - 9 | Faixa: 1–999999999 | Número da NF que está sendo devolvida/referenciada. |
| 29x.10 | BA10 | refNFP | Informações da NF de produtor rural referenciada | CG | BA01 |  | 1-1 |  |  | Esse grupo é gerado quando existir uma NF de produtor (modelo 04) referenciada a NF que está sendo emitida. As informações que são enviadas nas tags abaixo desse grupo podem ser verificadas no botão NFP Referenciada da tela F440GNE. |
| 29x.11 | BA11 | cUF | Código da UF do emitente | E | BA10 | N | 1-1 | 2 | Utilizar a Tabela do IBGE (Seção 8.1 do MOC – Visão Geral, Tabela de UF, Município e País) (v2.0) | Verifica o campo Estado Produtor Rural e gera o código da UF. |
| 29x.12 | BA12 | AAMM | Ano e Mês de emissão da NF-e | E | BA10 | N | 1-1 | 4 | AAMM da emissão da NF de produtor (v2.0) | Campo Data Emissão. |
| 29x.13 | BA13 | CNPJ | CNPJ do emitente | CE | BA10 | N | 1-1 | 14 | Informar o CNPJ do emitente da NF de produtor (v2.0) | Verifica o fornecedor que foi informado no campo Fornecedor Documento Fiscal e busca o CNPJ desse fornecedor, caso for pessoa jurídica. |
| 29x.14 | BA14 | CPF | CPF do emitente | CE | BA10 | N | 1-1 | 11 | Informar o CPF do emitente da NF de produtor (v2.0) | Verifica o fornecedor que foi informado no campo Fornecedor Documento Fiscal e busca o CPF desse fornecedor, caso for pessoa física. |
| 29x.15 | BA15 | IE | IE do emitente | E | BA10 | N | 1-1 | 2 - 14 | Informar a IE do emitente da NF de Produtor ou o literal “ISENTO” (v2.0) | Se o fornecedor informado no campo Fornecedor Documento Fiscal possuir IE, envia essa informação na tag do XML. |
| 29x.16 | BA16 | mod | Modelo do Documento Fiscal | E | BA10 | N | 1-1 | 2 | 04=NF de Produtor; 01=NF (v2.0) | Por padrão, envia o valor "04" nessa tag. |
| 29x.17 | BA17 | serie | Série do Documento Fiscal | E | BA10 | N | 1-1 | 1 - 3 | Informar a série do documento fiscal (informar zero se inexistente) (v2.0). | Gera a tag com o valor que consta no campo Série Doc. Fiscal. |
| 29x.18 | BA18 | nNF | Número do Documento Fiscal | E | BA10 | N | 1-1 | 1 - 9 | Faixa: 1–999999999 | Gera a tag com o valor que consta no campo Número Doc. Fiscal. |
| 29x.19 | BA19 | refCTe | Chave de acesso do CT-e referenciada | CE | BA01 | N | 1-1 | 44 | Utilizar esta TAG para referenciar um CT-e emitido anteriormente, vinculada a NF-e atual - (v2.0). | Nos casos de emissão de uma NF de saída de anulação de frete, gera essa tag com a chave do CT-e que está sendo anulado. |
| 29x.20 | BA20 | refECF | Informações do Cupom Fiscal referenciado | CG | BA01 |  | 1-1 |  | Grupo do Cupom Fiscal vinculado à NF-e (v2.0). | Gerado conforme o padrão do leiaute da SEFAZ. |
| 29x.21 | BA21 | mod | Modelo do Documento Fiscal | E | BA20 | C | 1-1 | 2 | "2B"=Cupom Fiscal emitido por máquina registradora (não ECF); "2C"=Cupom Fiscal PDV; "2D"=Cupom Fiscal (emitido por ECF) (v2.0). | Verifica o campo Tipo Equipamento da tela F050EQF do Código Equipamento que está informado na série do documento referenciado.   Se for "2", gera nessa tag o valor "2B". E se for "1", gera nessa tag o valor "2C". Caso contrário, gera o valor "2D". |
| 29x.22 | BA22 | nECF | Número de ordem sequencial do ECF | E | BA20 | N | 1-1 | 3 | Informar o número de ordem sequencial do ECF que emitiu o Cupom Fiscal vinculado à NF-e (v2.0). | Essa tag só é gerada quando o Tipo Equipamento for diferente de 1 e 2. Envia para a tag o valor do campo Código Equipamento da tela F050EQF. |
| 29x.23 | BA23 | nCOO | Número do Contador de Ordem de Operação - COO | E | BA20 | N | 1-1 | 6 | Informar o Número do Contador de Ordem de Operação - COO vinculado à NF-e (v2.0). | A tag é gerada com o número do cupom fiscal que fica gravado no campo Número do cupom fiscal da redução Z da tabela E140NFV. |
| 29x.24 | BA24 | refNfeSig | Chave de acesso da NF-e referenciada com código numérico zerado | CE | BA01 | N | 1-1 | 44 | Referencia uma NF-e (modelo 55) emitida anteriormente vinculada à NF-e atual ou a uma NFC-e (modelo 65) | NF de saída tipo "1 - Normal", gera nessa tag a informação de cada chave das NF-es referenciadas, zerando o código numérico (campo 8). Para gerar a tag é necessário informar uma transação de produtos ou serviços no cabeçalho da nota fiscal com a opção "Utiliza Sigilo Fiscal NF-e Ref." habilitada. |

## Páginas relacionadas

* [código IBGE](https://www.ibge.gov.br/explica/codigos-dos-municipios.php)
