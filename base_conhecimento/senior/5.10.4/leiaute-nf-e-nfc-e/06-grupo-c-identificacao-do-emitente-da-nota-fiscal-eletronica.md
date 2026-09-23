# Grupo C - Identificação do Emitente da Nota Fiscal eletrônica

> **Fonte:** Leiautes NF-e e NFC-e — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/leiaute-nf-e-nfc-e.htm  
> **Trilha:** Segmentos > Compliance > Documentos Eletrônicos > NF-e | NFC-e (Nota Fiscal Eletrônica) > Nota Fiscal Eletrônica 4.0  
> **Telas citadas:** E051FCI, E070FIL, F070EMP, F070FCA, F070FCP, F070FEF, F099PPE  
> **Identificadores de regras:** VEN-140NEDGE02

---
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação | Origem |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 30 | C01 | emit | Identificação do emitente da NF-e | G | A01 |  | 1-1 |  |  | Gerado conforme o padrão do leiaute da SEFAZ. |
| 31 | C02 | CNPJ | CNPJ do emitente | CE | C01 | N | 1-1 | 14 | Informar o CNPJ do emitente. Na emissão de NF-e avulsa pelo Fisco, as informações do remetente serão informadas neste grupo. O CNPJ ou CPF deverão ser informados com os zeros não significativos. | Gera a tag com o valor do campo CNPJ da tela F070FCA quando o campo Tipo Empresa for diferente de "07-Produtor Rural". |
| 31a | C02a | CPF | CPF do remetente | CE | C01 | N | 1-1 | 11 |  | Gera a tag com o valor do campo CPF da tela F070FCA quando o campo Tipo Empresa for diferente de "07 - Produtor Rural". |
| 32 | C03 | xNome | Razão Social ou Nome do emitente | E | C01 | C | 1-1 | 2 - 60 |  | Gera a tag com o valor do campo Filial da tela F070FCA. |
| 33 | C04 | xFant | Nome fantasia | E | C01 | C | 0-1 | 1 - 60 |  | Gera a tag com o valor do campo Fantasia da tela F070FCA. |
| 34 | C05 | enderEmit | Endereço do emitente | G | C01 |  | 1-1 |  |  | Gerado conforme o padrão do leiaute da SEFAZ. |
| 35 | C06 | xLgr | Logradouro | E | C05 | C | 1-1 | 2 - 60 |  | Gera a tag com o valor do campo Endereço/Número da tela da F070FCA. |
| 36 | C07 | nro | Número | E | C05 | C | 1-1 | 1 - 60 |  | Gera a tag com o valor do campo Endereço/Número da tela F070FCA. |
| 37 | C08 | xCpl | Complemento | E | C05 | C | 0-1 | 1 - 60 |  | Gera a tag com o valor do campo Complemento da tela F070FCA. |
| 38 | C09 | xBairro | Bairro | E | C05 | C | 1-1 | 2 - 60 |  | Gera a tag com o valor do campo Bairro da tela F070FCA. |
| 39 | C10 | cMun | Código do município | E | C05 | N | 1-1 | 7 | Utilizar a Tabela do IBGE (Seção 8.2 do MOC – Visão Geral, Tabela de UF, Município e País). | Gera a tag com o código IBGE do município, com base no valor do campo Cidade da tela F070FCA. |
| 40 | C11 | xMun | Nome do município | E | C05 | C | 1-1 | 2 - 60 |  | Gera a tag com o nome IBGE do município, com base no valor do campo Cidade da tela F070FCA. |
| 41 | C12 | UF | Sigla da UF | E | C05 | C | 1-1 | 2 |  | Gera a tag com o código IBGE do estado, com base no valor do campo Estado da tela F070FCA. |
| 42 | C13 | CEP | Código do CEP | E | C05 | N | 1-1 | 8 | Informar os zeros não significativos. (NT 2011/004) | Gera a tag com o valor informado no campo CEP da tela F070FCA. |
| 43 | C14 | cPais | Código do País | E | C05 | N | 0-1 | 4 | 1058=Brasil | Gera a tag com o código do país que consta no campo País da tela F070EMP. |
| 44 | C15 | xPais | Nome do País | E | C05 | C | 0-1 | 1 - 60 | Brasil ou BRASIL | Gera a tag com o nome do país que consta na tela F070EMP. |
| 45 | C16 | fone | Telefone | E | C05 | N | 0-1 | 6 - 14 | Preencher com o Código DDD + número do telefone. Nas operações com exterior é permitido informar o código do país + código da localidade + número do telefone (v2.0) | Gera a tag com o valor do campo Telefone da tela F070FCA. |
| 46 | C17 | IE | Inscrição Estadual do Emitente | E | C01 | C | 1-1 | 2 - 14 | Informar somente os algarismos, sem os caracteres de formatação (ponto, barra, hífen, etc.). | Gera a tag com o valor do campo Inscrição Estadual da tela F070FCA. |
| 47 | C18 | IEST | IE do Substituto Tributário | E | C01 | N | 0-1 | 2 - 14 | IE do Substituto Tributário da UF de destino da mercadoria, quando houver a retenção do ICMS ST para a UF de destino. | Gera a tag com o valor do campo Inscrição Estadual da tela F099PPE. |
| 47.1 | C18.1 | -x- | Sequência XML | G | C01 |  | 0-1 |  | Grupo opcional. | Gerado conforme o padrão do leiaute da SEFAZ. |
| 48 | C19 | IM | Inscrição Municipal do Prestador de Serviço | E | C18.1 | C | 1-1 | 1 - 15 | Informado na emissão de NF-e conjugada, com itens de produtos sujeitos ao ICMS e itens de serviços sujeitos ao ISSQN. | Gera a tag com o valor do campo Inscrição Municipal da tela F070FCA. |
| 49 | C20 | CNAE | CNAE fiscal | E | C18.1 | N | 0-1 | 7 | Campo Opcional. Pode ser informado quando a Inscrição Municipal (id:C19) for informada. | Gera a tag com o valor do campo CNAE Fiscal da tela F070FCP, guia Contábil 2.   Pode ser manipulado o valor dessa tag através da variável VSIntCodCna do identificador VEN-140NEDGE02. |
| 49a | C21 | CRT | Código de Regime Tributário | E | C01 | N | 1-1 | 1 | 1=Simples Nacional; 2=Simples Nacional, excesso sublimite de receita bruta; 3=Regime Normal. (v2.0). | Gera a tag com o valor do campo Código do Regime Tributária da tela F070FEF, guia Impostos 2. |
| 49d | C22 | ISUFEmit | Inscrição do emitente da Suframa | E | C01 | C | 0-1 | 8-9 | Campo obrigatório nas operações que se beneficiam de incentivos fiscais existentes nas áreas sob controle da SUFRAMA com alíquota zero da CBS referente aos arts. 451 e 466 da LC 214/25 | Gera a tag conforme o valor informado no campo E070FIL.CODSUF quando houver ao menos um item com classificação tributária vinculada a uma aplicação com indicativo de Zona Incentivada (E051FCI.ZONINC = 'S') e a data de emissão da NF-e for maior ou igual à data definida no parâmetro global NT2025002. |

## Páginas relacionadas

* [VEN-140NEDGE02](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_140nedge02.htm)
