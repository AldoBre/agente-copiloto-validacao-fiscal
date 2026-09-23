# Grupo I01 - Produtos e Serviços / Declaração de Importação

> **Fonte:** Leiautes NF-e e NFC-e — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/leiaute-nf-e-nfc-e.htm  
> **Trilha:** Segmentos > Compliance > Documentos Eletrônicos > NF-e | NFC-e (Nota Fiscal Eletrônica) > Nota Fiscal Eletrônica 4.0  
> **Telas citadas:** F440GNE  
> **Identificadores de regras:** —

---
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação | Origem |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 117 | I18 | DI | Declaração de Importação | G | I01 |  | 0-100 |  | Informar dados da importação | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 118 | I19 | nDI | Número do Documento de Importação (DI, DSI, DIRE, ...) | E | I18 | C | 1-1 | 1 - 12 | (NT 2011/004) | Gera a tag conforme informação do campo Número DI da tela F440GNE. |
| 119 | I20 | dDI | Data de Registro do documento | E | I18 | D | 1-1 |  | Formato: “AAAA-MM-DD” | Gera a tag conforme informação do campo Data Registro DI da tela F440GNE. |
| 120 | I21 | xLocDesemb | Local de desembaraço | E | I18 | C | 1-1 | 1 - 60 |  | Gera a tag conforme informação do campo Local de desembaraço da tela F440GNE. |
| 121 | I22 | UFDesemb | Sigla da UF onde ocorreu o Desembaraço Aduaneiro | E | I18 | C | 1-1 | 2 |  | Gera a tag conforme informação do campo Estado desembaraço da tela F440GNE. |
| 122 | I23 | dDesemb | Data do Desembaraço Aduaneiro | E | I18 | D | 1-1 |  | Formato: “AAAA-MM-DD” | Gera a tag conforme informação do campo Data desembaraço da tela F440GNE. |
| 122a | I23a | tpViaTransp | Via de transporte internacional informada na Declaração de Importação (DI) | E | I18 | N | 1-1 | 2 | 1=Marítima; 2=Fluvial; 3=Lacustre; 4=Aérea; 5=Postal; 6=Ferroviária; 7=Rodoviária; | Gera a tag conforme informação do campo Via transp. inter da tela F440GNE. |
| 122b | I23b | vAFRMM | Valor da AFRMM - Adicional ao Frete para Renovação da Marinha Mercante | E | I18 | N | 0-1 | 13v2 | A tag deve ser informada no caso da via de transporte marítima. | Gera a tag conforme informação do campo Valor AFRMM da tela F440GNE, botão Valores. |
| 122c | I23c | tpIntermedio | Forma de importação quanto a intermediação | E | I18 | N | 1-1 | 1 | 1=Importação por conta própria; 2=Importação por conta e ordem; 3=Importação por encomenda; | Gera a tag conforme informação do campo Intermediação Imp da tela F440GNE. |
| 122d | I23d | CNPJ | CNPJ do adquirente ou do encomendante | E | I18 | N | 0-1 | 14 | Obrigatória a informação no caso de importação por conta e ordem ou por encomenda. Informar os zeros não significativos | Gera a tag conforme informação do campo CNPJ Adq./Encom da tela F440GNE. |
| 122.05 | I23d1 | CNPJ | CNPJ do adquirente ou do encomendante | CE | I18 | N | 0-1 | 11 | Obrigatória a informação no caso de importação por conta e ordem ou por encomenda. Informar os zeros não significativos. | Gera a tag conforme informação do campo CNPJ/CPF Adq./Encom quando o campo Tipo Adq./Encom. da tela F440GNE estiver preenchido com "J - Pessoa Jurídica". |
| 122.05 | I23d1 | CPF | CPF do adquirente ou do encomendante | CE | I18 | N | 0-1 | 11 | Obrigatória a informação no caso de importação por conta e ordem ou por encomenda. Informar os zeros não significativos. | Gera a tag conforme informação do campo CNPJ/CPF Adq./Encom quando o campo Tipo Adq./Encom. da tela F440GNE estiver preenchido com "F - Pessoa Física". |
| 122e | I23e | UFTerceiro | Sigla da UF do adquirente ou do encomendante | E | I18 | C | 0-1 | 2 | Obrigatória a informação no caso de importação por conta e ordem ou por encomenda. Não aceita o valor "EX". | Gera a tag conforme informação do campo UF Adq./Encom da tela F440GNE. |
| 123 | I24 | cExportador | Código do Exportador | E | I18 | C | 1-1 | 1 - 60 | Código do Exportador, usado nos sistemas internos de informação do emitente da NF-e | Gera a tag conforme informação do campo Código exportador da tela F440GNE. |
| 124 | I25 | adi | Adições | G | I18 |  | 1-100 |  | (NT 2011/004) | Gerado conforme o padrão do leiaute da SEFAZ. |
| 125 | I26 | nAdicao | Numero da Adição | E | I25 | N | 1-1 | 1 - 3 |  | Gera a tag conforme informação do campo Número adição da tela F440GNE, guia Produtos. |
| 126 | I27 | nSeqAdic | Numero sequencial do item dentro da Adição | E | I25 | N | 1-1 | 1 - 3 |  | Gera a tag conforme informação do campo Número seq. item adição da tela F440GNE, guia Produtos. |
| 127 | I28 | cFabricante | Código do fabricante estrangeiro | E | I25 | C | 1-1 | 1 - 60 | Código do fabricante estrangeiro, usado nos sistemas internos de informação do emitente da NF-e | Gera a tag conforme informação do campo Fabricante estrangeiro da tela F440GNE, guia Produtos. |
| 128 | I29 | vDescDI | Valor do desconto do item da DI – Adição | E | I25 | N | 0-1 | 13v2 |  | Gera a tag conforme informação do campo Valor desconto item DI da tela F440GNE, guia Produtos. |
| 128.01 | I29a | nDraw | Número do ato concessório de Drawback | E | I25 | N | 0-1 | 0, 9 ou 11 | O número do Ato Concessório de Suspensão deve ser preenchido com 11 dígitos (AAAANNNNNND) e o número do Ato Concessório de Drawback Isenção deve ser preenchido com 9 dígitos (AANNNNNND). (Observação incluída na NT 2013/005 v. 1.10) | Gera a tag conforme informação do campo Num. Drawback da tela F440GNE, guia Produtos. |
