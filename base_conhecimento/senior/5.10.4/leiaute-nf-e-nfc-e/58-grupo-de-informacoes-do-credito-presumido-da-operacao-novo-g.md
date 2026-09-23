# Grupo de Informações do Crédito Presumido da Operação - Novo grupo para atender a Reforma Tributária!

> **Fonte:** Leiautes NF-e e NFC-e — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/leiaute-nf-e-nfc-e.htm  
> **Trilha:** Segmentos > Compliance > Documentos Eletrônicos > NF-e | NFC-e (Nota Fiscal Eletrônica) > Nota Fiscal Eletrônica 4.0  
> **Telas citadas:** E140IPR, E140ISR  
> **Identificadores de regras:** —

---
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação | Origem |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 324.83a | UB83a | gCredPresOper | Grupo de Informações do Crédito Presumido da Operação | G | UB15 | - | 0-1 | - | Grupo de Informações do Crédito Presumido, quando aproveitado pelo emitente do documento. |  |
| 324.83b | UB83b | vBCCredPres | Valor da Base de Cálculo do Crédito Presumido da Operação | CE | UB83a | N | 1-1 | 13v2 |  | Gera por padrão o valor do campo E140IPR.BASCAL para produtos e E140ISR.BASCAL para serviços |
| 324.83c | UB83c | cCredPres | Código de Classificação do Crédito Presumido | E | UB83a | N | 1-1 | 2 | Utilizar tabela cCredPres (Anexo IV).  Exemplos:  1 - Aquisição de Produtor Rural não contribuinte.  2 - Tomador de serviço de transporte de TAC PF  não contrib.  3 - Aquisição de pessoa física com destino a  reciclagem.  4 - Aquisição de bens móveis de PF não contrib. para revenda (veículos / brechó).  5 - Regime opcional para cooperativa | Gera por padrão o valor do campo E140IPR.CODPCI quando E140IPR.CODIMP = IBU para produtos e E140ISR.CODPCI quando E140ISR.CODIMP = IBU para serviços |
| 324.83d | UB83d | gIBSCredPres | Grupo de Informações do Crédito Presumido referente ao IBS | G | UB83a | - | 0-1 | - | Grupo de Informações do Crédito Presumido do IBS, quando aproveitado pelo emitente do documento. |  |
| 324.83e | UB83e | pCredPres | Percentual do Crédito Presumido | E | UB83d | N | 1-1 | 3v2-4 |  | Gera por padrão o valor do campo E140IPR.PERPCI quando E140IPR.CODIMP = IBU para produtos e E140ISR.PERPCI quando E140ISR.CODIMP = IBU para serviços |
| 324.83f | UB83f | vCredPres | Valor do Crédito Presumido | CE | UB83d | N | 1-1 | 13v2 |  | Gera por padrão o valor do campo E140IPR.VLRPCI quando E140IPR.CODIMP = IBU para produtos e E140ISR.VLRPCI quando E140ISR.CODIMP = IBU para serviços |
| 324.83g | UB83g | vCredPresCondSus | Valor do Crédito Presumido em condição suspensiva. | CE | UB83d | N | 1-1 | 13v2 | Valor do Crédito Presumido Condição Suspensiva. Preencher apenas para cCredPres com indicação de Condição Suspensiva. | Gera por padrão o valor do campo E140IPR.VLRPCI quando E140IPR.CONSUS = 'S' e E140IPR.CODIMP = IBU para produtos e E140ISR.VLRPCI quando E140ISR.CONSUS = 'S' e E140ISR.CODIMP = IBU para serviços |
| 324.83h | UB83h | gCBSCredPres | Grupo de Informações do Crédito Presumido referente a CBS | G | UB83a | - | 0-1 |  | Grupo de Informações do Crédito Presumido da CBS, quando aproveitado pelo emitente do documento. |  |
| 324.83i | UB83i | pCredPres | Percentual do Crédito Presumido | E | UB83h | N | 1-1 | 3v2-4 |  | Gera por padrão o valor do campo E140IPR.PERPCI quando E140IPR.CODIMP = CBS para produtos e E140ISR.PERPCI quando E140ISR.CODIMP = CBS para serviços |
| 324.83j | UB83j | vCredPres | Valor do Crédito Presumido | CE | UB83h | N | 1-1 | 13v2 |  | Gera por padrão o valor do campo E140IPR.VLRPCI quando E140IPR.CODIMP = CBS para produtos e E140ISR.VLRPCI quando E140ISR.CODIMP = CBS para serviços |
| 324.83k | UB83k | vCredPresCondSus | Valor do Crédito Presumido em condição suspensiva. | CE | UB83h | N | 1-1 | 13v2 | Valor do Crédito Presumido Condição Suspensiva. Preencher apenas para cCredPres com indicação de Condição Suspensiva. | Gera por padrão o valor do campo E140IPR.VLRPCI quando E140IPR.CONSUS = 'S' e E140IPR.CODIMP = CBS para produtos e E140ISR.VLRPCI quando E140ISR.CONSUS = 'S' e E140ISR.CODIMP = CBS para serviços |
