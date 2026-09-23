# Grupo UB -  Informações dos tributos IBS / CBS e Imposto Seletivo - Novo grupo para atender a Reforma Tributária!

> **Fonte:** Leiautes NF-e e NFC-e — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/leiaute-nf-e-nfc-e.htm  
> **Trilha:** Segmentos > Compliance > Documentos Eletrônicos > NF-e | NFC-e (Nota Fiscal Eletrônica) > Nota Fiscal Eletrônica 4.0  
> **Telas citadas:** E001TVE, E027SCR, E051CBS, E051FCI, E070IMP, E075PRO, E140IPR, E140IPV, E140ISR, E140TNF  
> **Identificadores de regras:** —

---
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação | Origem |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 324.11 | UB11 | vIS | Valor do Imposto Seletivo | E | UB04 | N |  |  |  |  |
| 324.12 | UB12 | IBSCBS | Informações do Imposto de Bens e Serviços - IBS e da Contribuição de Bens e Serviços - CBS | E | M01 | - | 0-1 | - | Grupo de impostos IBS e CBS | Dados das tabelas E140IPR para produtos e E140ISR para serviços |
| 324.13 | UB13 | CST | Código de Situação Tributária do IBS e CBS | E | UB12 | N | 1-1 | 3 | Utilizar tabela CST do IBS/CBS | Gera por padrão o valor do campo E027SCR.CODSTR fazendo vinculo com o campo E140IPR.IdeScr para produtos e E140ISR.IdeScr para serviços |
| 324.14 | UB14 | cClassTrib | Código de Classificação Tributária do IBS e CBS | E | UB12 | N | 1-1 | 6 | Utilizar tabela cClassTrib | Gera por padrão o valor do campo E027SCR.STRCLA fazendo vinculo com o campo E140IPR.IdeScr para produtos e E140ISR.IdeScr para serviços |
| 324.14a | UB14a | indDoacao | Indica a natureza da operação de doação, orientando a apuração e a geração de débitos ou estornos conforme o cenário | E | UB12 | N | 0-1 | 1 | Informar "1" quando doação | Gera quando a transação indicar operação de doação E001TVE.OPEDOA = 'S' |
| 324.14k | UB14k | x | Sequencia XML | G | UB12 | - | 0-1 |  |  |  |
| 324.15 | UB15 | gIBSCBS | Grupo de Informações do IBS e da CBS | CG | UB14a | - | 1-1 |  | O grupo gIBSCBS é gerado apenas para os CSTs: 000, 010, 011, 200, 220, 221, 222, 510, 515, 550 e 830. |  |
| 324.16 | UB16 | vBC | Base de cálculo do IBS e CBS | E | UB15 | N | 1-1 | 13v2 |  | Gera por padrão o valor do campo E140IPR.BASCAL para produtos e E140ISR.BASCAL para serviços |
| 324.17 | UB17 | gIBSUF | Grupo de Informações do IBS para a UF | G | UB15 | - | 1-1 | - |  |  |
| 324.18 | UB18 | pIBSUF | Alíquota do IBS de competência das UF | E | UB17 | N | 1-1 | 3v2-4 | Alíquota vigente do IBS da UF | Gera por padrão o valor do campo E140IPR.ALIIMP para produtos e E140ISR.ALIIMP para serviços |
| 324.21 | UB21 | gDif | Grupo de Informações do Diferimento | G | UB17 | - | 0-1 | - |  |  |
| 324.22 | UB22 | pDif | Percentual do diferimento | E | UB21 | N | 1-1 | 3v2-4 |  | Gera por padrão o valor do campo E140IPR.PERDIF para produtos e E140ISR.PERDIF para serviços |
| 324.23 | UB23 | vDif | Valor do Diferimento | E | UB21 | N | 1-1 | 13v2 |  | Gera por padrão o valor do campo E140IPR.VLRDIF para produtos e E140ISR.VLRDIF para serviços |
| 324.26 | UB26 | gRed | Grupo de informações da redução da alíquota | G | UB17 | - | 0-1 | - |  |  |
| 324.27 | UB27 | pRedAliq | Percentual da redução de alíquota do cClassTrib | E | UB26 | N | 1-1 | 3v2-4 |  | Gera por padrão o valor do campo E140IPR.PERRED para produtos e E140ISR.PERRED para serviços |
| 324.28 | UB28 | pAliqEfet | Alíquota Efetiva do IBS de competência das UF que será aplicada a Base de Cálculo | E | UB26 | N | 1-1 | 3v2-4 | Alíquota efetiva, após aplicação da redução de alíquota, incluindo o gCompraGov/pRedutor, se houver.  pAliqEfet = pIBSUF\*(1 – pRedAliq)\*(1 - tag: gCompraGov/pRedutor) | Gera por padrão o valor do campo E140IPR.ALIEFE para produtos e E140ISR.ALIEFE para serviços |
| 324.35 | UB35 | vIBSUF | Valor do IBS de competência da UF | E | UB17 | N | 1-1 | 13v2 | Se grupo gRed preenchido: vIBSUF = gRed/pAliqEfet \* vBC (UB16)  Senão: vIBSUF = pIBSUF \* vBC | Gera por padrão o valor do campo E140IPR.VLRIMP para produtos e E140ISR.VLRIMP para serviços |
| 324.36 | UB36 | gIBSMun | Grupo de Informações do IBS para o município | G | UB15 | - | 1-1 | - |  |  |
| 324.37 | UB37 | pIBSMun | Alíquota do IBS de competência do Município | E | UB36 | N | 1-1 | 3v2-4 | Alíquota vigente do IBS do Município | Gera por padrão o valor do campo E140IPR.ALIIMP para produtos e E140ISR.ALIIMP para serviços |
| 324.40 | UB40 | gDif | Grupo de Informações do Diferimento | G | UB36 | - | 0-1 | - |  |  |
| 324.41 | UB41 | pDif | Percentual do diferimento | E | UB40 | N | 1-1 | 3v2-4 |  | Gera por padrão o valor do campo E140IPR.PERDIF para produtos e E140ISR.PERDIF para serviços |
| 324.42 | UB42 | vDif | Valor do Diferimento | E | UB40 | N | 1-1 | 13v2 |  | Gera por padrão o valor do campo E140IPR.VLRDIF para produtos e E140ISR.VLRDIF para serviços |
| 324.45 | UB45 | gRed | Grupo de informações da redução da alíquota | G | UB36 | - | 0-1 | - |  |  |
| 324.46 | UB46 | pRedAliq | Percentual da redução de alíquota do cClassTrib | E | UB45 | N | 1-1 | 3v2-4 |  | Gera por padrão o valor do campo E140IPR.PERRED para produtos e E140ISR.PERRED para serviços |
| 324.47 | UB47 | pAliqEfet | Alíquota Efetiva do IBS de competência das UF que será aplicada a Base de Cálculo | E | UB45 | N | 1-1 | 3v2-4 | Alíquota efetiva, após aplicação da redução de alíquota, incluindo o gCompraGov/pRedutor, se houver.  pAliqEfet = pIBSUF\*(1 – pRedAliq)\*(1 - tag: gCompraGov/pRedutor) | Gera por padrão o valor do campo E140IPR.ALIEFE para produtos e E140ISR.ALIEFE para serviços |
| 324.53 | UB54 | vIBSMun | Valor do IBS de competência do Município | E | UB36 | N | 1-1 | 13v2 | Se grupo gRed preenchido: vIBSMun = gRed/pAliqEfet \* vBC (UB16)  Senão: vIBSMun = pIBSMun \* vBC | Gera por padrão o valor do campo E140IPR.VLRIMP para produtos e E140ISR.VLRIMP para serviços |
| 324.48 | UB48 | vIBS | Grupo de Informações do IBS para o município | G | UB15 | - | 1-1 | - |  |  |
| 324.55 | UB55 | gCBS | Grupo de Informações da CBS | G | UB15 | - | 1-1 | - |  |  |
| 324.56 | UB56 | pCBS | Alíquota do CBS | E | UB55 | N | 1-1 | 3v2-4 | Alíquota vigente do CBS | Gera por padrão o valor do campo E140IPR.ALIIMP para produtos e E140ISR.ALIIMP para serviços |
| 324.59 | UB59 | gDif | Grupo de Informações do Diferimento | G | UB55 | - | 0-1 | - |  |  |
| 324.60 | UB60 | pDif | Percentual do diferimento | E | UB59 | N | 1-1 | 3v2-4 |  | Gera por padrão o valor do campo E140IPR.PERDIF para produtos e E140ISR.PERDIF para serviços |
| 324.61 | UB61 | vDif | Valor do Diferimento | E | UB59 | N | 1-1 | 13v2 |  | Gera por padrão o valor do campo E140IPR.VLRDIF para produtos e E140ISR.VLRDIF para serviços |
| 324.64 | UB64 | gRed | Grupo de informações da redução da alíquota | G | UB55 | - | 0-1 | - |  |  |
| 324.65 | UB65 | pRedAliq | Percentual da redução de alíquota do cClassTrib | E | UB64 | N | 1-1 | 3v2-4 |  | Gera por padrão o valor do campo E140IPR.PERRED para produtos e E140ISR.PERRED para serviços |
| 324.66 | UB66 | pAliqEfet | Alíquota Efetiva do IBS de competência das UF que será aplicada a Base de Cálculo | E | UB64 | N | 1-1 | 3v2-4 | Alíquota efetiva, após aplicação da redução de alíquota, incluindo o gCompraGov/pRedutor, se houver.  pAliqEfet = pIBSUF\*(1 – pRedAliq)\*(1 - tag: gCompraGov/pRedutor) | Gera por padrão o valor do campo E140IPR.ALIEFE para produtos e E140ISR.ALIEFE para serviços |
| 324.66a | UB66a | gALCZFMCBS | Grupo de operações em áreas incentivadas (ALC/ZFM) - CBS (alíquota zero) | G | UB55 | - | 0-1 | - |  | Grupo é gerado quando a cClassTrib possuir a aplicação com indicativo de zona incentivada (E051FCI.ZONINC = 'S' |
| 324.66b | UB66b | tpALCZFMCBS | Tipo de aplicação da alíquota zero da CBS | E | UB66a | N | 1-1 | 1 | 1 - quando o fornecedor e o destinatário estiverem localizados em área incentivada, a operação estiver amparada por alíquota zero da CBS e não se tratar de operação industrial com processo aprovado na Suframa para o item; 2 - quando o fornecedor e o destinatário estiverem localizados em área incentivada, a operação estiver amparada por alíquota zero da CBS e se tratar de operação industrial com processo aprovado na Suframa para o item. | Gera o valor, conforme consta no campo E140TNF.APLAZE |
| 324.66c | UB66c | nProcSuframa | Número do processo na Suframa para o item comercializado | E | UB66a | C | 0-1 | 8-12 |  | Gera o valor do campo E075PRO.PROSUF. Somente gerada quando quando o tpALCZFMCBS=2 |
| 324.66d | UB66d | AliqEfetRegCBS | Percentual efetivo sem a redução | E | UB66a | N | 1-1 | 3v-2-4 |  | Alíquota vigente do CBS E051CBS.PERIMP |
| 324.66e | UB66e | vTribRegCBS | Valor efetivo sem a redução | E | UB66a | N | 1-1 | 13v2 |  | Resultante do cálculo = gIBSCBS/vBC x (pAliqEfetRegCBS) |
| 324.67 | UB67 | vCBS | Valor da CBS | E | UB55 | N | 1-1 | 13v2 | Se grupo gRed preenchido: vCBS = gRed/pAliqEfet \* vBC (UB16)  Senão: vCBS = pCBS \* vBCC | Gera por padrão o valor do campo E140IPR.VLRIMP para produtos e E140ISR.VLRIMP para serviços |
| 324.68 | UB68 | gTribRegular | Grupo de informações da Tributação Regular | G | UB15 | - | 0-1 | - | Grupo de informações da Tributação Regular.Informar como seria a tributação caso não cumprida a condição resolutória/suspensiva.  Exemplo 1: Art. 445, §4 da LC 214/2025. Operações com ZFM e ALC.  Exemplo 2: Operações com suspensão do tributo |  |
| 324.69 | UB69 | CSTReg | Código de Situação Tributária do IBS e CBS | E | UB68 | N | 1-1 | 3 | Utilizar tabela CST do IBS/CBS | Gera por padrão o valor do campo E027SCR.CODSTR vinculando com E140IPR.IDESTR para produtos e E140ISR.IDESTR para serviços |
| 324.70 | UB70 | cClassTribReg | Código de Classificação Tributária do IBS e CBS | E | UB68 | N | 1-1 | 6 | Utilizar tabela cClassTrib | Gera por padrão o valor do campo E027SCR.STRCLA vinculando com E140IPR.IDESTR para produtos e E140ISR.IDESTR para serviços |
| 324.71 | UB71 | pAliqEfetRegIBSUF | Valor da alíquota do IBS da UF | E | UB68 | N | 1-1 | 3v2-4 |  | Gera por padrão o valor do campo E140IPR.PERDES quando E140IPR.CODIMP = IBU para produtos e E140ISR.PERDES quando E140ISR.CODIMP = IBU para serviços |
| 324.72 | UB72 | vTribRegIBSUF | Valor do Tributo do IBS da UF | E | UB68 | N | 1-1 | 13v2 |  | Gera por padrão o valor do campo E140IPR.VLRDES quando E140IPR.CODIMP = IBU para produtos e E140ISR.VLRDES quando E140ISR.CODIMP = IBU para serviços |
| 324.72a | UB72a | pAliqEfetRegIBSMun | Valor da alíquota do IBS do Município | E | UB68 | N | 1-1 | 3v2-4 |  | Gera por padrão o valor do campo E140IPR.PERDES quando E140IPR.CODIMP = IBM para produtos e E140ISR.PERDES quando E140ISR.CODIMP = IBM para serviços |
| 324.72b | UB72b | vTribRegIBSMun | Valor do Tributo do IBS do Município | E | UB68 | N | 1-1 | 13v2 |  | Gera por padrão o valor do campo E140IPR.VLRDES quando E140IPR.CODIMP = IBM para produtos e E140ISR.VLRDES quando E140ISR.CODIMP = IBM para serviços |
| 324.72c | UB72c | pAliqEfetRegCBS | Valor da alíquota da CBS | E | UB68 | N | 1-1 | 3v2-4 |  | Gera por padrão o valor do campo E140IPR.PERDES quando E140IPR.CODIMP = CBS para produtos e E140ISR.PERDES quando E140ISR.CODIMP = CBS para serviços |
| 324.72d | UB72d | vTribRegCBS | Valor do Tributo da CBS | E | UB68 | N | 1-1 | 13v2 |  | Gera por padrão o valor do campo E140IPR.VLRDES quando E140IPR.CODIMP = CBS para produtos e E140ISR.VLRDES quando E140ISR.CODIMP = CBS para serviços |
| 324.82a | UB82a | gTribCompraGov | Grupo de informações da composição do valor do IBS e da CBS em compras governamentais | G | UB15 | - | 0-1 | - | Informar somente para compras governamentais | Dados das tabelas E140IPR para produtos e E140ISR para serviços |
| 324.82b | UB82b | pAliqIBSUF | Alíquota do IBS de competência do Estado | E | UB82a | N | 1-1 | 3v2-4 | - | E140IPR.PerCgo ou E140ISR.PerCgo |
| 324.82c | UB82c | vTribIBSUF | Valor do Tributo do IBS da UF calculado | E | UB82a | N | 1-1 | 13v2 | Valor que seria devido a UF, sem aplicação do Art. 473. da LC 214/2025 | E140IPR.VlrCgo ou E140ISR.VlrCgo |
| 324.82d | UB82d | pAliqIBSMun | Alíquota do IBS de competência do Município | E | UB82a | N | 1-1 | 3v2-4 | - | E140IPR.PerCgo ou E140ISR.PerCgo |
| 324.82e | UB82e | vTribIBSMun | Valor do Tributo do IBS do Município calculado | E | UB82a | N | 1-1 | 13v2 | Valor que seria devido ao Município, sem aplicação do Art. 473. da LC 214/2025 | E140IPR.VlrCgo ou E140ISR.VlrCgo |
| 324.82f | UB82f | pAliqCBS | Alíquota da CBS | E | UB82a | N | 1-1 | 3v2-4 | - | E140IPR.PerCgo ou E140ISR.PerCgo |
| 324.82g | UB82g | vTribCBS | Valor do Tributo da CBS calculado | E | UB82a | N | 1-1 | 13v2 | Valor que seria devido a CBS, sem aplicação do Art. 473. da LC 214/2025 | E140IPR.VlrCgo ou E140ISR.VlrCgo |
| 324.106 | UB106 | gTransfCred | Grupo de Informações das Transferências de Crédito | CG | UB14k | - | 1-1 | - | A obrigatoriedade ou vedação do preenchimento deste grupo está condicionada ao indicador ind\_gTransfCred da tabela CST do IBS e da CBS | Grupo é gerado apenas quando a cClassTrib indicar que é uma transferência de crédito E027SCR.TRACRE = 'S' |
| 324.107 | UB107 | vIBS | Valor do IBS a ser transferido | E | UB106 | N | 1-1 | 13v2 |  | Gera o valor do campo E140IPR.VLRIMP quando E140IPR.CODIMP = IBU ou IBM para produtos |
| 324.108 | UB108 | vCBS | Valor da CBS a ser transferida | E | UB106 | N | 1-1 | 13v2 |  | Gera o valor do campo E140IPR.VLRIMP quando E140IPR.CODIMP = CBS para produtos |
| 324.112 | UB112 | gAjusteCompet | Grupo de Informações do Ajuste de Competência | CG | UB14k | - | 1-1 | - | A obrigatoriedade ou vedação do preenchimento deste grupo está condicionada ao indicador “nd\_gAjusteCompet”” da tabela CST do IBS e da CBS | Grupo é gerado apenas quando a cClassTrib indicar que é um ajuste de competência E027SCR.AJUCOM = 'S' |
| 324.113 | UB113 | competApur | Ano e mês referência do período de apuração (AAAA-MM) | E | UB112 | C | 1-1 | 7 | Informar período atual ou retroativo | Gera a tag conforme o valor que consta no campo E140IPV.CptApu |
| 324.114 | UB114 | vIBS | Valor do IBS | E | UB112 | N | 1-1 | 13v2 |  | Gera o valor do campo E140IPR.VLRIMP quando E140IPR.CODIMP = IBU ou IBM para produtos |
| 324.115 | UB115 | vCBS | Valor da CBS | E | UB112 | N | 1-1 | 13v2 |  | Gera o valor do campo E140IPR.VLRIMP quando E140IPR.CODIMP = CBS para produtos |
| 324.116 | UB116 | gEstornoCred | Grupo de Informações do Estorno de Crédito | CG | UB12 | - | 0-1 | - | A obrigatoriedade ou vedação do preenchimento deste grupo está condicionada ao indicador “ind\_gEstornoCred” da tabela de cClassTrib do IBS e da CBS. | Grupo é gerado apenas quando a transação indicar que é um estorno de crédito E001TVE.ESTCRE = 'S' e a data do documento for igual ou superior à Data Inicial Estorno Crédito CBS/IBS (E070IMP.DATIEC) ou quando a cClassTrib indicar que é um estorno de crédito E027SCR.ESTCRE = 'S' |
| 324.117 | UB117 | vIBSEstCred | Valor do IBS a ser estornado | E | UB116 | N | 1-1 | 13v2 |  | Gera o valor do campo E140IPR.VLRIMP quando E140IPR.CODIMP = IBU ou IBM para produtos e E140ISR.VLRIMP quando E140ISR.CODIMP = IBU ou IBM para serviços |
| 324.118 | UB118 | vCBSEstCred | Valor da CBS a ser estornada | E | UB116 | N | 1-1 | 13v2 |  | Gera o valor do campo E140IPR.VLRIMP quando E140IPR.CODIMP = CBS para produtos e E140ISR.VLRIMP quando E140ISR.CODIMP = CBS para serviços |
