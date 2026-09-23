# Grupo YB - Informações do Intermediador da Transação

> **Fonte:** Leiautes NF-e e NFC-e — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/leiaute-nf-e-nfc-e.htm  
> **Trilha:** Segmentos > Compliance > Documentos Eletrônicos > NF-e | NFC-e (Nota Fiscal Eletrônica) > Nota Fiscal Eletrônica 4.0  
> **Telas citadas:** —  
> **Identificadores de regras:** —

---
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação | Origem |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 398.26 | YB01 | infIntermed | Grupo de Informações do Intermediador da Transação | G | A01 |  | 0-1 |  | Obrigatório o preenchimento do Grupo de Informações do Intermediador da Transação nos casos de "operação não presencial pela internet em site de terceiros (intermediadores) (Incluído na NT2020.006) | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 398.27 | YB02 | CNPJ | CNPJ do Intermediador da Transação (agenciador, plataforma de delivery, marketplace e similar) de serviços e de negócios | E | YB01 | N | 1-1 | 14 | Informar o CNPJ do Intermediador da Transação (agenciador, plataforma de delivery, marketplace e similar) de serviços e de negócios | Gera por padrão o valor do campo E140Tnf.CgcItm. |
| 398.28 | YB03 | idCadIntTran | Identificador cadastrado no intermediador | R | YB01 | C | 1-1 | 60 | Nome do usuário ou identificação do perfil do vendedor no site do intermediador (agenciador, plataforma de delivery, marketplace e similar) de serviços e de negócios | Gera por padrão o valor do campo E000Tnf.CadItm. |
