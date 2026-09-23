# Grupo F - Identificação do Local de Retirada

> **Fonte:** Leiautes NF-e e NFC-e — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/leiaute-nf-e-nfc-e.htm  
> **Trilha:** Segmentos > Compliance > Documentos Eletrônicos > NF-e | NFC-e (Nota Fiscal Eletrônica) > Nota Fiscal Eletrônica 4.0  
> **Telas citadas:** F070EMP, F070RET  
> **Identificadores de regras:** —

---
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação | Origem |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 80 | F01 | retirada | Identificação do Local de retirada | G | A01 |  | 0-1 |  | Informar somente se diferente do endereço do remetente. | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 81 | F02 | CNPJ | CNPJ | CE | F01 | N | 1-1 | 0 ou 14 | Informar CNPJ ou CPF. Preencher os zeros não significativos. | Gera a tag conforme o campo CNPJ/CPF Retirada da tela F070RET. |
| 81a | F02a | CPF | CPF | CE | F01 | N | 1-1 | 11 |  | Gera a tag conforme o campo CNPJ/CPF Retirada da tela F070RET. |
| 81b | F02b | xNome | Razão Social ou Nome do Expedidor | E | F01 | C | 0-1 | 2-60 | (Criado na NT 2018.005) | Gera a tag conforme o campo Razão social da tela F070RET. |
| 82 | F03 | xLgr | Logradouro | E | F01 | C | 1-1 | 2 - 60 |  | Gera a tag conforme o campo End. Retirada da tela F070RET. |
| 83 | F04 | nro | Número | E | F01 | C | 1-1 | 1 - 60 |  | Gera a tag conforme o campo Número Endereço da tela F070RET. |
| 84 | F05 | xCpl | Complemento | E | F01 | C | 0-1 | 1 - 60 |  | Gera a tag conforme o campo Complemento da tela F070RET. |
| 85 | F06 | xBairro | Bairro | E | F01 | C | 1-1 | 2 - 60 |  | Gera a tag conforme o campo Bairro da tela F070RET. |
| 86 | F07 | cMun | Código do município | E | F01 | N | 1-1 | 7 | Utilizar a Tabela do IBGE (Seção 8.2 do MOC – Visão Geral, Tabela de UF, Município e País). Informar ‘9999999 ‘para operações com o exterior. | Gera a tag conforme o campo Cidade da tela F070RET, considerando a tabela IBGE. |
| 87 | F08 | xMun | Nome do município | E | F01 | C | 1-1 | 2 - 60 | Informar ‘EXTERIOR ‘para operações com o exterior. | Gera a tag conforme o campo Cidade da tela F070RET, considerando a tabela IBGE. |
| 88 | F09 | UF | Sigla da UF | E | F01 | C | 1-1 | 2 | Informar ‘EX’ para operações com o exterior. | Gera a tag conforme o campo Estado da tela F070RET. |
| 88a | F10 | CEP | Código do CEP | E | F01 | N | 0-1 | 8 | Informar os zeros não significativos. (Criado na NT 2018.005) | Gera a tag conforme o campo CEP da tela F070RET. |
| 88b | F11 | cPais | Código do País | E | F01 | N | 0-1 | 4 | Utilizar a Tabela do BACEN (Seção 8.3 do MOC – Visão Geral,Tabela de UF, Município e País). (Criado na NT 2018.005) | Gera a tag conforme o campo País do cadastro da empresa, tela F070EMP. |
| 88c | F12 | xPais | Nome do País | E | F01 | C | 0-1 | 2 - 60 | (Criado na NT 2018.005) | Gera a tag conforme o campo País do cadastro da empresa, tela F070EMP. |
| 88d | F13 | fone | Telefone | E | F01 | N | 0-1 | 6 - 14 | Preencher com o Código DDD + número do telefone. Nas operações com exterior é permitido informar o código do país + código da localidade + número do telefone (v2.0) (Criado na NT 2018.005) | Gera a tag conforme o campo Telefone da tela F070RET. |
| 88e | F14 | email | Endereço de e-mail do Expedidor | E | F01 | C | 0-1 | 1 - 60 | (Criado na NT 2018.005) | Gera a tag conforme o campo E-mail da tela F070RET. |
| 88f | F15 | IE | Inscrição Estadual do Estabelecimento Expedidor | E | F01 | N | 0-1 | 2 - 14 | Informar somente os algarismos, sem os caracteres de formatação (ponto, barra, hífen, etc.). (Criado na NT 2018.005) | Gera a tag conforme o campo Inscrição Estadual da tela F070RET. |
