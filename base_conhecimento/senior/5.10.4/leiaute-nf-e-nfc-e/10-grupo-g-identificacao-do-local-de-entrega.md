# Grupo G - Identificação do Local de Entrega

> **Fonte:** Leiautes NF-e e NFC-e — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/leiaute-nf-e-nfc-e.htm  
> **Trilha:** Segmentos > Compliance > Documentos Eletrônicos > NF-e | NFC-e (Nota Fiscal Eletrônica) > Nota Fiscal Eletrônica 4.0  
> **Telas citadas:** E085CLI, E085ENT, F085ENT  
> **Identificadores de regras:** —

---
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação | Origem |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 89 | G01 | entrega | Identificação do Local de entrega | G | A01 |  | 0-1 |  | Informar somente se diferente do endereço destinatário. | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 90 | G02 | CNPJ | CNPJ | CE | G01 | N | 1-1 | 0 ou 14 | Informar CNPJ ou CPF. Preencher os zeros não significativos. (v2.0) | Gera a tag conforme o campo CNPJ/CPF Entrega da tela F085ENT. |
| 90a | G02a | CPF | CPF | CE | G01 | N | 1-1 | 11 |  | Gera a tag conforme o campo CNPJ/CPF Entrega da tela F085ENT. |
| 90b | G02b | xNome | Razão Social ou Nome do Recebedor | E | G01 | C | 0-1 | 2-60 | (Criado na NT 2018.005) | Gera a tag conforme o campo Nome do Cliente da tela F085ENT. |
| 91 | G03 | xLgr | Logradouro | E | G01 | C | 1-1 | 2 - 60 |  | Gera a tag conforme o campo Endereço da tela F085ENT. |
| 92 | G04 | nro | Número | E | G01 | C | 1-1 | 1 - 60 |  | Gera a tag conforme o campo Número Endereço da tela F085ENT. |
| 93 | G05 | xCpl | Complemento | E | G01 | C | 0-1 | 1 - 60 |  | Gera a tag conforme o campo Complemento da tela F085ENT. |
| 94 | G06 | xBairro | Bairro | E | G01 | C | 1-1 | 2 - 60 |  | Gera a tag conforme o campo Bairro Entrega da tela F085ENT. |
| 95 | G07 | cMun | Código do município | E | G01 | N | 1-1 | 7 | Utilizar a Tabela do IBGE (Seção 8.2 do MOC – Visão Geral,Tabela de UF, Município e País). Informar ‘9999999 ‘para operações com o exterior. | Gera a tag com base no campo Cidade da tela F085ENT, considerando a tabela IBGE. |
| 96 | G08 | xMun | Nome do município | E | G01 | C | 1-1 | 2 - 60 | Informar ‘EXTERIOR ‘para operações com o exterior. | Gera a tag com base no campo Cidade da tela F085ENT, considerando a tabela IBGE. |
| 97 | G09 | UF | Sigla da UF | E | G01 | C | 1-1 | 2 | Informar ‘EX’ para operações com o exterior. | Gera a tag conforme o campo Estado da tela F085ENT. |
| 97a | G10 | CEP | Código do CEP | E | G01 | N | 0-1 | 8 | Informar os zeros não significativos. (Criado na NT 2018.005) | Gera a tag conforme o campo CEP da tela F085ENT. |
| 97b | G11 | cPais | Código do País | E | G01 | N | 0-1 | 4 | Utilizar a Tabela do BACEN (Seção 8.3 do MOC – Visão Geral, Município e País). (Criado na NT 2018.005) | Gera a tag conforme o campo País Ent. da tela F085ENT. |
| 97c | G12 | xPais | Nome do País | E | G01 | C | 0-1 | 2 - 60 | (Criado na NT 2018.005) | Gera a tag conforme o campo País Ent. da tela F085ENT. |
| 97d | G13 | fone | Telefone | E | G01 | N | 0-1 | 6 - 14 | Preencher com o Código DDD + número do telefone. Nas operações com exterior é permitido informar o código do país + código da localidade + número do telefone (v2.0) (Criado na NT 2018.005) | Gera a tag conforme o campo Telefone da tela F085ENT. |
| 97e | G14 | email | Endereço de e-mail do Recebedor | E | G01 | C | 0-1 | 1 - 60 | (Criado na NT 2018.005) | Gera a tag conforme o campo E-mail para contato da tela F085ENT. |
| 97f | G15 | IE | Inscrição Estadual do Estabelecimento Recebedor | E | G01 | N | 0-1 | 2 - 14 | Informar somente os algarismos, sem os caracteres de formatação (ponto, barra, hífen, etc.). (Criado na NT 2018.005) | Gera a tag conforme o campo Inscrição Estadual da tela F085ENT. |

**Observação**

A geração da tag endereço de entrega é condicionada pelos campos que seguem descritos abaixo:

* ENDCLI: Endereço principal no cadastro do cliente (Tabela: E085CLI).
* ENDENT: Código do endereço de entrega do cliente, caso exista na nota fiscal (Tabela: E085ENT).
* NenCli: Número do Endereço do Cliente no cadastro do cliente (Tabela: E085CLI).
* NenEnt: Número do Endereço de Entrega do Cliente caso exista na nota fiscal (Tabela: E085ENT).

A Tag Entrega será gerada na nota fiscal apenas se:

* O endereço de entrega (ENDENT) for diferente do endereço principal (ENDCLI);  

  ou,
* O número de endereço (NENENT) for diferente do endereço principal (NENCLI).
