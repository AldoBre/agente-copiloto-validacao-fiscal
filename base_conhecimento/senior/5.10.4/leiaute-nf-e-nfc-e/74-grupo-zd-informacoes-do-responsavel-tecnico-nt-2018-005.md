# Grupo ZD - Informações do Responsável Técnico (NT 2018.005)

> **Fonte:** Leiautes NF-e e NFC-e — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/leiaute-nf-e-nfc-e.htm  
> **Trilha:** Segmentos > Compliance > Documentos Eletrônicos > NF-e | NFC-e (Nota Fiscal Eletrônica) > Nota Fiscal Eletrônica 4.0  
> **Telas citadas:** —  
> **Identificadores de regras:** —

---
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação | Origem |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 423a | ZD01 | infRespTec | Informações do Responsável Técnico pela emissão do DF-e | G | A01 |  | 0-1 |  | Grupo para informações do responsável técnico pelo sistema de emissão do DF-e | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 423b | ZD02 | CNPJ | CNPJ da pessoa jurídica responsável pelo sistema utilizado na emissão do documento fiscal eletrônico | E | ZD01 | N | 1-1 | 14 | Informar o CNPJ da pessoa jurídica responsável pelo sistema utilizado na emissão do documento fiscal eletrônico | Tag gerada com valor '00000000000000' padrão pelo sistema. |
| 423c | ZD04 | xContato | Nome da pessoa a ser contatada | E | ZD01 | C | 1-1 | 2-60 | Informar o nome da pessoa a ser contatada na empresa desenvolvedora do sistema utilizado na emissão do documento fiscal eletrônico | Tag gerada com o nome da pessoa padrão no sistema. |
| 423d | ZD05 | email | E-mail da pessoa jurídica a ser contatada | E | ZD01 | C | 1-1 | 6-60 | Informar o e-mail da pessoa a ser contatada na empresa desenvolvedora do sistema | Tag gerada com o e-mail padrão no sistema. |
| 423e | ZD06 | fone | Telefone da pessoa jurídica/física a ser contatada | E | ZD01 | N | 1-1 | 6-14 | Informar o telefone da pessoa a ser contatada na empresa desenvolvedora do sistema. Preencher com o Código DDD + número do telefone | Tag gerada com o telefone padrão no sistema. |
| 423f | ZD07 | -x- | Sequência XML | G | ZD01 |  | 0-1 |  | Grupo de informações do Código de Segurança do Responsável Técnico - CSRT | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 423g | ZD08 | idCSRT | Identificador do CSRT | E | ZD07 | N | 1-1 | 2 | Identificador do CSRT utilizado para montar o hash do CSRT | Tag não é gerada pelo ERP. |
| 423h | ZD09 | hashCSRT | Hash do CSRT | E | ZD07 | C | 1-1 | 28 | O hashCSRT é o resultado da função hash 9SHA-1-Base64) do CSRT fornecido pelo fisco mais a Chave de Acesso da NFe | Tag não é gerada pelo ERP. |
