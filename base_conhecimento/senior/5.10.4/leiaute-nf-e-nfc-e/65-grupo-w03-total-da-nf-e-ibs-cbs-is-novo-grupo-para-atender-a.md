# Grupo W03 - Total da NF-e - IBS / CBS / IS - Novo grupo para atender a Reforma Tributária!

> **Fonte:** Leiautes NF-e e NFC-e — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/leiaute-nf-e-nfc-e.htm  
> **Trilha:** Segmentos > Compliance > Documentos Eletrônicos > NF-e | NFC-e (Nota Fiscal Eletrônica) > Nota Fiscal Eletrônica 4.0  
> **Telas citadas:** E001TVE, E027SCR, E070IMP, E140IPR, E140ISR, E140NFV  
> **Identificadores de regras:** —

---
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação | Origem |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 355.4 | W34 | IBSCBSTot | Totais da NF-e com IBS e CBS | G | W01 | - | 0-1 | - | O grupo de valores totais da NF-e deve ser informado com o somatório do campo correspondente dos itens. O IBS e a CBS são “por fora”, por isso seus valores devem ser adicionados ao valor total da NF. |  |
| 355.5 | W35 | vBCIBSCBS | Valor total da BC do IBS e da CBS | E | W34 | N | 1-1 | 13v2 | Considera apenas os CSTs que geram o grupo gIBSCBS: 000, 010, 011, 200, 220, 221, 222, 510, 515, 550 e 830. | Gera por padrão o valor do campo a soma do campo E140IPR.BASCAL para produtos e E140ISR.BASCAL para serviços |
| 355.6 | W36 | gIBS | Grupo total do IBS | G | W34 | - | 0-1 | - |  |  |
| 355.7 | W37 | gIBSUF | Grupo total do IBS da UF | G | W36 | - | 1-1 | - |  |  |
| 355.8 | W38 | vDif | Valor total do diferimento | E | W37 | N | 1-1 | 13v2 |  | Gera por padrão o valor do campo a soma do campo E140IPR.VLRDIF quando E140IPR.CODIMP = IBU para produtos e E140ISR.VLRDIF quando E140ISR.CODIMP = IBU para serviços |
| 355.11 | W41 | vIBSUF | Valor total do IBS da UF | E | W37 | N | 1-1 | 13v2 |  | Gera por padrão o valor do campo a soma do campo E140IPR.VLRIMP quando E140IPR.CODIMP = IBU para produtos e E140ISR.VLRIMP quando E140ISR.CODIMP = IBU para serviços |
| 355.12 | W42 | gIBSMun | Grupo total do IBS do Município | G | W36 | - | 1-1 | - |  |  |
| 355.13 | W43 | vDif | Valor total do diferimento | E | W42 | N | 1-1 | 13v2 |  | Gera por padrão o valor do campo a soma do campo E140IPR.VLRDIF quando E140IPR.CODIMP = IBM para produtos e E140ISR.VLRDIF quando E140ISR.CODIMP = IBM para serviços |
| 355.16 | W46 | vIBSMun | Valor total do IBS do Município | E | W42 | N | 1-1 | 13v2 |  | Gera por padrão o valor do campo a soma do campo E140IPR.VLRIMP quando E140IPR.CODIMP = IBM para produtos e E140ISR.VLRIMP quando E140ISR.CODIMP = IBM para serviços |
| 355.17 | W47 | vIBS | Valor total do IBS | E | W36 | N | 1-1 | 13v2 |  | Gera por padrão o valor do campo a soma do campo E140IPR.VLRIMP quando E140IPR.CODIMP = IBM e E140IPR.CODIMP = IBU para produtos e E140ISR.VLRIMP quando E140ISR.CODIMP = IBM e E140ISR.CODIMP = IBU para serviços |
| 355.18 | W48 | vCredPres | Valor total do crédito presumido | E | W36 | N | 1-1 | 13v2 |  | Gera por padrão o valor do campo a soma do campo E140IPR.VLRPCI quando E140IPR.CODIMP = IBM e E140IPR.CODIMP = IBU para produtos e E140ISR.VLRPCI quando E140ISR.CODIMP = IBM e E140ISR.CODIMP = IBU para serviços |
| 355.19 | W49 | vCredPresCondSus | Valor total do crédito presumido em condição suspensiva. | E | W36 | N | 1-1 | 13v2 |  | Gera por padrão o valor do campo a soma do campo E140IPR.VLRPCI quando E140IPR.CONSUS = 'S', E140IPR.CODIMP = IBM e E140IPR.CODIMP = IBU para produtos e E140ISR.VLRPCI quando E140ISR.CONSUS = 'S', E140ISR.CODIMP = IBM e E140ISR.CODIMP = IBU para serviços |
| 355.20 | W50 | gCBS | Grupo total da CBS | G | W34 | - | 0-1 | - |  |  |
| 355.23 | W53 | vDif | Valor total do diferimento | E | W50 | N | 1-1 | 13v2 |  | Gera por padrão o valor do campo a soma do campo E140IPR.VLRDIF quando E140IPR.CODIMP = CBS para produtos e E140ISR.VLRDIF quando E140ISR.CODIMP = CBS para serviços |
| 355.26 | W56 | vCBS | Valor total da CBS | E | W50 | N | 1-1 | 13v2 |  | Gera por padrão o valor do campo a soma do campo E140IPR.VLRIMP quando E140IPR.CODIMP = CBS para produtos e E140ISR.VLRIMP quando E140ISR.CODIMP = CBS para serviços |
| 355.26a | W56a | vCredPres | Valor total do crédito presumido | E | W50 | N | 1-1 | 13v2 |  | Gera por padrão o valor do campo a soma do campo E140IPR.VLRPCI quando E140IPR.CODIMP = CBS para produtos e E140ISR.VLRPCI quando E140ISR.CODIMP = CBS para serviços |
| 355.26b | W56b | vCredPresCondSus | Valor total do crédito presumido em condição suspensiva. | E | W50 | N | 1-1 | 13v2 |  | Gera por padrão o valor do campo a soma do campo E140IPR.VLRPCI quando E140IPR.CONSUS = 'S' e E140IPR.CODIMP = CBS para produtos e E140ISR.VLRPCI quando E140ISR.CONSUS = 'S' e E140ISR.CODIMP = CBS para serviços |
| 355.29e | W59e | gEstornoCredW59e | Grupo total do Estorno de Crédito | G | W34 | - | 0-1 | - |  | Grupo é gerado apenas quando a transação indicar que é um estorno de crédito E001TVE.ESTCRE = 'S' e a data do documento for igual ou superior à Data Inicial Estorno Crédito CBS/IBS (E070IMP.DATIEC) ou quando a cClassTrib indicar que é um estorno de crédito E027SCR.ESTCRE = 'S' |
| 355.29f | W59f | vIBSEstCred | Valor total do IBS estornado | E | W59e | N | 1-1 | 13v2 |  | Gera a soma do valor do campo E140IPR.VLRIMP quando E140IPR.CODIMP = IBU ou IBM para produtos e E140ISR.VLRIMP quando E140ISR.CODIMP = IBU ou IBM para serviços |
| 355.29g | W59g | vCBSEstCred | Valor total da CBS estornada | E | W59e | N | 1-1 | 13v2 |  | Gera a soma do valor do campo E140IPR.VLRIMP quando E140IPR.CODIMP = CBS para produtos e E140ISR.VLRIMP quando E140ISR.CODIMP = CBS para serviços |
| 355.30 | W60 | vNFTot | Valor total da NF-e com IBS / CBS / IS | E | W01 | N | 1-1 | 13v2 |  | Gera por padrão o valor do campo E140NFV.VLRLIQ |
