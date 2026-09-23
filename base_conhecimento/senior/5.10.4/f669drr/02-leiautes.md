# Leiautes

> **Fonte:** F669DRR - ADRC-ST (PR) — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f669drr.htm  
> **Trilha:** Ajuda por telas > Controladoria > Gestão de Tributos > Arquivos Fiscais > Estaduais  
> **Telas citadas:** E001TNS, E015MED, E022CLF, E070FIL, E075BAR, E075DER, E075PRO, E085CLI, E085HCL, E095FOR, E660IDE, E660INC, E660INV, E660NFC, E660NFV, E660RSC, E660RSV, F070FVE, F075GFP, F075PRO  
> **Identificadores de regras:** —

---
## Centro de Distribuição

### 0001 - Registro de abertura e identificação do contribuinte

|  |  |  |  |
| --- | --- | --- | --- |
| Campo | Descrição | Tamanho | Documentação |
| REG | 0001 | 4 | Fixo 0001 |
| COD\_VERSAO | Código da versão | 3 | Conforme tela, sendo que o padrão é 100 |
| MES\_ANO | Mês e ano de referência | 6 | Conforme tela (formato MMAAAA) |
| CNPJ | CNPJ do declarante | 14 | E070FIL.NumCgc (formato 00000000000000) |
| IE | Inscrição estadual | 10 | E070FIL.InsEst (somente números) |
| NOME | Nome empresarial | 100 | E070FIL.NomFil |
| CD\_FIN | Código da finalidade | 1 | Conforme tela (0 ou 1) |

### 1001 - Registro analítico do produto

|  |  |  |  |
| --- | --- | --- | --- |
| Campo | Descrição | Tamanho | Descrição |
| REG | 1001 | 4 | Fixo 1001 |
| IND\_FECOP | Indicador de produto sujeito ao FCP | 1 | E660RSC.PerFcp > 0, campo recebe 1 - Não sujeito, senão 0 - Sujeito |
| COD\_ITEM | Código do item | 60 | E075DER.IteFis ou PRO + E075PRO.CodPro + '-' + E075DER.CodDer |
| COD\_BARRAS | Código GTIN/EAN Tributável do produto | 14 | O sistema listará nesse campo o conteúdo de: - E075DER.CodBar - Código de barras ou - E075DER.CodBa2 - Código de barras livre ou - E075DER.CodGtn - GTIN unidade tributável - E075BAR.CodGtn - GTIN unidade tributável  Os campos acima serão buscados conforme parametrização do campo **OriGti - Forma de busca do código GTIN**, disponível nas telas F075PRO/F075GFP - Cadastro do Produto ou F070FVE - Vendas, Faturamento e Transporte |
| COD\_ANP | Código conforme tabela ANP | 9 | E075PRO.CodAnp |
| NCM | Código da NCM | 8 | E075PRO.CodClf > E022CLF.ClaFis |
| CEST | Código Especificador da Substituição Tributária | 7 | E075DER.CodCes ou E075PRO.CodCes ou E022CLF.CodCes |
| DESCR\_ITEM | Descrição do item | 150 | E075DER.DesFis ou E075DER.DesNfv |
| UNID\_ITEM | Unidade de medida do estoque | 10 | E075PRO.UniMed > E015MED.UniFis |
| ALIQ\_ICMS\_ITEM | Alíquota do ICMS aplicável ao item nas operações internas |  | E660RSC.PerIcs (máscara Z9,99) |
| ALIQ\_FECOP | Alíquota do FECOP |  | E660RSC.PerFcp (máscara 9,99) |

### 1101 - Registro totalizador das entradas do produto

|  |  |  |  |
| --- | --- | --- | --- |
| Campo | Descrição | Tamanho | Documentação |
| REG | 1101 | 4 | Fixo 1101 |
| QTD\_TOT\_ENTRADA | Quantidade total do item adquirido no período |  | 1111.QTD\_ENTRADA (máscara ZZZZZZZZ9,999) |
| VL\_BC\_ICMSST\_UNIT\_MED | Valor unitário médio da base de cálculo do ICMS ST |  | 1111.VL\_BC\_ICMS\_ST / 1110.QTD\_TOT\_ENTRADA (máscara ZZZZZZZZ9,99) |
| VL\_TOT\_ICMS\_SUPORT\_ENTR | Valor total do ICMS do item suportado na entrada |  | 1111.VL\_ICMS\_SUPORT\_ENT (máscara ZZZZZZZZ9,99) |
| VL\_UNIT\_MED\_ICMS\_SUPORT\_ENTR | Valor unitário médio do ICMS suportado na entrada |  | 1101.VL\_TOT\_ICMS\_SUPORT\_ENTR / 1101.QTD\_TOT\_ENTRADA (máscara ZZZZZZZZ9,99) |
| QTD\_TRANF | Quantidade transferida para as filiais |  | E660RSC > E660RSV.QtdFat O sistema listará as quantidades de transferências entre filiais cujas entradas possuam ICMS ST gravado no Controle de Entrada e Saída de Produtos |

### 1111 - Registro das notas fiscais de entrada

|  |  |  |  |
| --- | --- | --- | --- |
| Campo | Descrição | Tamanho | Documentação |
| REG | 1111 | 4 | Fixo 1111 |
| DT\_DOC | Data de Emissão do documento fiscal | 8 | E660NFC.DatEmi |
| COD\_RESP\_RET | Código que indica o responsável pela retenção do ICMS-ST | 1 | - Será **3 - Próprio declarante** quando E660INC.VlrRis > 0, senão - Será **1 - Direto** quando CST do ICMS for igual a X10, X30 ou X70 senão, - Será **2 - Indireto** |
| CST\_CSOSN | Código da Situação Tributária | 3 | E660RSC.CodStr |
| CHAVE | Chave da NF-e | 44 | E660NFC.ChvNel |
| N\_NF | Número do documento fiscal | 9 | E660RSC.NumNfc |
| CNPJ\_EMIT | CNPJ Emitente | 14\* | E095FOR.CgcCpf |
| UF\_EMIT | UF emitente | 2\* | E095FOR.SigUfs |
| CNPJ\_DEST | CNPJ do destinatário | 14\* | E070FIL.NumCgc |
| UF\_DEST | UF do Destinatário | 2\* | E070FIL.SigUfs |
| CFOP | Código fiscal de operação e prestação | 4\* | E660RSC.NopOpe |
| N\_ITEM | Número do item do produto no documento fiscal | 3 | E660RSC.SeqIpc |
| UNID\_ITEM | Unidade de medida do item | 10 | 1001.UNID\_ITEM |
| QTD\_ENTRADA | Quantidade do item adquirido |  | E660RSC.QtdEnt (máscara ZZZZZZZZ9,999) |
| VL\_UNIT\_ITEM | Valor unitário do item |  | E660RSC.VlrTot / E660RSC.QtdEnt (máscara ZZZZZZZZ9,99) |
| VL\_BC\_ICMS\_ST | Base de cálculo do ICMS ST |  | E660RSC.VlrBsi (máscara ZZZZZZZZ9,99) |
| VL\_ICMS\_SUPORT\_ENTR | Valor do ICMS do item suportado na entrada |  | E660RSC.VlrIcm + E660RSC.VlrIcs + E660RSC.VlrFcp (máscara ZZZZZZZ9,99) |

O sistema listará as notas fiscais de entrada de produtos que tiveram alguma transferência entre filiais no período de geração da ADRCST seguindo os critérios abaixo:

* Modelo 55 (E660NFV.CodEdc = '55')
* Situação da NF-e Autorizada (E660IDE.SitDoe = 3)
* Aplicação da transação de saída igual T-Transferência (E001TNS.VenTcf = 'T')

### 9999 - Registro de encerramento do arquivo

|  |  |  |  |
| --- | --- | --- | --- |
| Campo | Descrição | Tamanho | Documentação |
| REG | 9999 | 4 | Fixo 9999 |
| QTD\_LIN | Quantidade total de linhas |  | Quantidade de linhas do arquivo |

## Filial

As quantidades dos itens da nota fiscal apresentadas nos registros 1120, 1210, 1220, 1310, 1320, 1410, 1420, 1510 e 1520 serão convertidos para a unidade de medida do estoque quando necessário. O sistema buscará o fator de conversão e aplicará sobre a quantidade do item da nota fiscal. Exemplo:

* Produto: 1101-1
* Unidade medida inventário: KG
* Unidade medida do item da nota fiscal: TN
* Fator de conversão: 1000
* Quantidade exibida no registro: 10 (TN) = 10000

O sistema listará as notas fiscais de entrada de produtos que tiveram alguma venda no período de geração da ADRCST seguindo os critérios abaixo:

**Registros 1100 e filhos:**

* NF-e autorizada (E660IDE.SitDoe = 3)
* Nota Fiscal modelo 55 ou 65 (E660NFV.CodEdc = 55 ou 65)
* Consumidor final (E085HCL.ConFin = S)
* CST do ICMS da saída igual a X60
* CFOP da saída iniciada em 5
* ICMS ST complementar/restituir preenchido no sistema (E660RSV.VlrIsc > 0)

**Registro 1200 e filhos:**

* NF-e autorizada (E660IDE.SitDoe = 3)
* Nota Fiscal modelo 55 ou 65 (E660NFV.CodEdc = 55 ou 65)
* Consumidor final (E085HCL.ConFin = S)
* CST do ICMS da saída igual a X60
* CFOP da saída iniciada em 5

**Registro 1300 e filhos:**

* NF-e autorizada (E660IDE.SitDoe = 3)
* Nota Fiscal modelo 55 (E660NFV.CodEdc = 55)
* CFOP da saída iniciada em 6
* Ressarcimento do ICMS ST calculado na nota fiscal de saída ligada ao Controle de Entrada e Saída de Produtos (E660RSV.VlrIcs > 0)

**Registro 1400 e filhos:**

* NF-e autorizada (E660IDE.SitDoe = 3)
* Nota Fiscal modelo 55 (E660NFV.CodEdc = 55)
* CFOP da saída iniciada em 5
* NCM ou Produto indicarem enquadramento no Art 119 do RICMS/2017 do PR (E022CLF.Art119 ou E075PRO.Art119 igual a **S-Sim**)

**Registro 1500 e filhos:**

* NF-e autorizada (E660IDE.SitDoe = 3)
* Nota Fiscal modelo 55 (E660NFV.CodEdc = 55)
* CFOP da saída iniciada em 5
* Regime tributário do cliente for do Simples (E085CLI.CodRtr)

### 0000 - Registro de abertura e identificação do contribuinte

|  |  |  |  |
| --- | --- | --- | --- |
| Campo | Descrição | Tamanho | Documentação |
| REG | 0000 | 4 | Fixo 0000 |
| COD\_VERSAO | Código da versão | 3 | Conforme tela de entrada, sendo que o padrão é 110 |
| MES\_ANO | Mês e ano de referência | 6 | Conforme tela de entrada (formato MMAAAA) |
| CNPJ | CNPJ do declarante | 14 | E070FIL.NumCgc (formato 00000000000000) |
| IE | Inscrição estadual | 10 | E070FIL.InsEst (somente números) |
| NOME | Nome empresarial | 100 | E070FIL.NomFil |
| CD\_FIN | Código da finalidade | 1 | Conforme tela de entrada (0 ou 1) |
| N\_REG\_ESPECIAL | Número do regime especial | 10 | Conforme tela de entrada |
| CNPJ\_CD | CNPJ do centro de distribuição | 14 | CNPJ da filial do CD informado na tela (E070FIL.NumCgc; formato 00000000000000) |
| IE\_CD | IE do centro de distribuição | 10 | IE da filial do CD informado na tela (E070FIL.InsEst; somente números) |
| OPÇÃO\_R1200 | Código para reaver ou recolher imposto no R1200 | 1 | Conforme tela de entrada |
| OPÇÃO\_R1300 | Código para reaver imposto no R1300 | 1 | Conforme tela de entrada |
| OPÇÃO\_R1400 | Código para reaver imposto no R1400 | 1 | Conforme tela de entrada |
| OPÇÃO\_R1500 | Código para reaver imposto no R1500 | 1 | Conforme tela de entrada |

### 1000 - Registro analítico do produto

|  |  |  |  |
| --- | --- | --- | --- |
| Campo | Descrição | Tamanho | Documentação |
| REG | 1000 | 4 | Fixo 1000 |
| IND\_FECOP | Indicador de produto sujeito ao FCP | 1 | E660RSC.PerFcp > 0, campo recebe 1 - Não sujeito, senão 0 - Sujeito |
| COD\_ITEM | Código do item | 60 | E075DER.IteFis ou PRO + E075PRO.CodPro + '-' + E075DER.CodDer |
| COD\_BARRAS | Código GTIN/EAN Tributável do produto | 14 | O sistema listará nesse campo o conteúdo de: - E075DER.CodBar - Código de barras ou - E075DER.CodBa2 - Código de barras livre ou - E075DER.CodGtn - GTIN unidade tributável - E075BAR.CodGtn - GTIN unidade tributável  Os campos acima serão buscados conforme parametrização do campo **OriGti - Forma de busca do código GTIN**, disponível nas telas F075PRO/F075GFP - Cadastro do Produto ou F070FVE - Vendas, Faturamento e Transporte |
| COD\_ANP | Código conforme tabela ANP | 9 | E075PRO.CodAnp |
| NCM | Código da NCM | 8 | E075PRO.CodClf > E022CLF.ClaFis |
| CEST | Código Especificador da Substituição Tributária | 7 | E075DER.CodCes ou E075PRO.CodCes ou E022CLF.CodCes |
| DESCR\_ITEM | Descrição do item | 150 | E075DER.DesFis ou E075DER.DesNfv |
| UNID\_ITEM | Unidade de medida do estoque | 10 | E075PRO.UniMed > E015MED.UniFis |
| ALIQ\_ICMS\_ITEM | Alíquota do ICMS aplicável ao item nas operações internas |  | E660RSC.PerIcs (máscara Z9,99) |
| ALIQ\_FECOP | Alíquota do FECOP |  | E660RSC.PerFcp (máscará 9,99) |
| QTD\_TOT\_ENTRADA | Quantidade total adquirida |  | E660RSC.QtdEnt (máscara ZZZZZZZZ9,999) |
| QTD\_TOT\_SAÍDA | Quantidade total saídas |  | E660RSV.QtdFat (máscara ZZZZZZZZ9,999) |

### 1010 - Inventário total do produto (somente quando E070Fil.CodCrt for igual a 1 ou 2)

Serão buscados todos os registros da tabela E660RSV até o último dia do mês anterior ao do período inicial. Além disso, serão descontadas as quantidades e o valor total das saídas da entrada relacionada, dessa forma compondo o inventário de produtos comercializados.  

O registro servirá de base para justificar as quantidades comercializadas no registro 1200 e filhos. Dessa forma, será considerado apenas o inventário dos produtos que tiveram vendas destinadas a consumidor final.

|  |  |  |  |
| --- | --- | --- | --- |
| Campo | Descrição | Tamanho | Documentação |
| REG | 1010 | 4 | Fixo 1010 |
| COD\_ITEM | Código do item | 60 | Registro 1000.COD\_ITEM |
| UNID\_ITEM | Unidade de medida do estoque | 10 | Registro 1000.UNID\_ITEM |
| QTD | Quantidade do produto no estoque |  | E660RSC.QtdEnt - E660RSV.QtdFat (máscara ZZZZZZZZ9,999) |
| VL\_TOT\_ITEM | Valor total do produto |  | (E660RSC.VlrTot / E660RSC.QtdEnt) \* (E660RSC.QtdEnt - E660RSV.QtdFat) (máscara ZZZZZZZZ9,99) |
| TXT\_COMPL | Descrição complementar | 100 | Conteúdo pode ser alterado via SQL por meio do campo TXTCPL |

### 1100 - Registro totalizador das entradas

**Observação**

É possível ter o controle das vendas ligadas às entradas pelo método UEPS descrito no início desta página, dessa forma rastreando as vendas do período e relacionando-as às notas fiscais de compra mais recentes sem haver duplicidade ou repetição de notas no decorrer dos períodos.

|  |  |  |  |
| --- | --- | --- | --- |
| Campo | Descrição | Tamanho | Documentação |
| REG | 1100 | 4 | Fixo 1100 |
| QTD\_TOT\_ENTRADA | Quantidade total do item adquirido no período |  | 1110.QTD\_ENTRADA - 1120.QTD\_DEVOLVIDA (máscara ZZZZZZZZ9,999) |
| MENOR\_VL\_UNIT\_ITEM | Menor valor unitário do item adquirido no período |  | Menor valor dos campos 1110.VL\_UNIT\_ITEM e 1120.VL\_UNIT\_ITEM |
| VL\_BC\_ICMSST\_UNIT\_MED | Valor unitário médio da base de cálculo do ICMS ST |  | (1110.VL\_BC\_ICMS\_ST - 1120.VL\_BC\_ICMS\_ST) / 1100.QTD\_TOT\_ENTRADA (máscara ZZZZZZZZ9,99) |
| VL\_TOT\_ICMS\_SUPORT\_ENTR | Valor total do ICMS do item suportado na entrada |  | 1110.VL\_ICMS\_SUPORT\_ENTR - 1120.VL\_ICMS\_SUPORT\_ENTR (máscara ZZZZZZZZ9,99) |
| VL\_UNIT\_MED\_ICMS\_SUPORT\_ENTR | Valor unitário médio do ICMS suportado na entrada |  | 1100.VL\_TOT\_ICMS\_SUPORT\_ENTR / 1100.QTD\_TOT\_ENTRADA (máscara ZZZZZZZZ9,99) |

### 1110 - Registro das notas fiscais de entrada

|  |  |  |  |
| --- | --- | --- | --- |
| Campo | Descrição | Tamanho | Documentação |
| REG | 1110 | 4 | Fixo 1110 |
| DT\_DOC | Data de Emissão do documento fiscal | 8 | E660NFC.DatEmi |
| COD\_RESP\_RET | Código que indica o responsável pela retenção do ICMS-ST | 1 | - Será **3 - Próprio declarante** quando E660INC.VlrRis > 0, senão - Será **1 - Direto** quando CST do ICMS for igual a X10, X30 ou X70, senão - Será **2 - Indireto** |
| CST\_CSOSN | Código da Situação Tributária | 3 | E660RSC.CodStr |
| CHAVE | Chave da NF-e | 44 | E660NFC.ChvNel |
| N\_NF | Número do documento fiscal | 9 | E660RSC.NumNfc |
| CNPJ\_EMIT | CNPJ Emitente | 14\* | E095FOR.CgcCpf |
| UF\_EMIT | UF emitente | 2\* | E095FOR.SigUfs |
| CNPJ\_DEST | CNPJ do destinatário | 14\* | E070FIL.NumCgc |
| UF\_DEST | UF do Destinatário | 2\* | E070FIL.SigUfs |
| CFOP | Código fiscal de operação e prestação | 4\* | E660RSC.NopOpe |
| N\_ITEM | Número do item do produto no documento fiscal | 3 | E660RSC.SeqIpc |
| UNID\_ITEM | Unidade de medida do item | 10 | 1000.UNID\_ITEM |
| QTD\_ENTRADA | Quantidade do item adquirido |  | E660RSC.QtdEnt (máscara ZZZZZZZZ9,999) |
| VL\_UNIT\_ITEM | Valor unitário do item |  | E660RSC.VlrTot / E660RSC.QtdEnt (máscara ZZZZZZZZ9,99) |
| VL\_BC\_ICMS\_ST | Base de cálculo do ICMS ST |  | E660RSC.VlrBsi (máscara ZZZZZZZZ9,99) |
| VL\_ICMS\_SUPORT\_ENTR | Valor do ICMS do item suportado na entrada |  | E660RSC.VlrIcm + E660RSC.VlrIcs + E660RSC.VlrFcp (máscara ZZZZZZZ9,99) |

### 1120 - Registro das notas fiscais de devolução das entradas

|  |  |  |  |
| --- | --- | --- | --- |
| Campo | Descrição | Tamanho | Documentação |
| REG | 1120 | 4 | Fixo 1120 |
| DT\_DOC | Data de Emissão do documento fiscal | 8 | E660NFV.DatEmi |
| CST\_CSOSN | Código da Situação Tributária | 3 | E660INV.CodStr |
| CHAVE | Chave da NF-e | 44 | E660IDE.ChvDoe |
| N\_NF | Número do documento fiscal | 9 | E660NFV.NumNfi |
| CNPJ\_EMIT | CNPJ Emitente | 14\* | E070FIL.NumCgc |
| UF\_EMIT | UF emitente | 2\* | E070FIL.SigUfs |
| CNPJ\_DEST | CNPJ do destinatário | 14\* | E085CLI.CgcCpf |
| UF\_DEST | UF do Destinatário | 2\* | E085CLI.SigUfs |
| CFOP | Código fiscal de operação e prestação | 4\* | E660NFV.NopOpe |
| N\_ITEM | Número do item do produto no documento fiscal | 3 | E660INV.SeqIpv |
| UNID\_ITEM | Unidade de medida do item | 10 | 1000.UNID\_ITEM |
| QTD\_DEVOLVIDA | Quantidade do item adquirido |  | E660INV.QtdEnt (máscara ZZZZZZZZ9,999, convertido para unidade medida estoque) |
| VL\_UNIT\_ITEM | Valor unitário do item |  | E660INV.VlrMrc / QTD\_DEVOLVIDA (máscara ZZZZZZZZ9,99) |
| VL\_BC\_ICMS\_ST | Base de cálculo do ICMS ST |  | (E660RSC.VlrBsi / E660RSC.QtdEnt) \* QTD\_DEVOLVIDA (máscara ZZZZZZZZ9,99) |
| VL\_ICMS\_SUPORT\_ENTR | Valor do ICMS do item suportado na entrada |  | ((E660RSC.VlrIcm + E660RSC.VlrIcs + E660RSC.VlrFcp) / E660RSC.QtdEnt) \* QTD\_DEVOLVIDA (máscara ZZZZZZZ9,99) |
| CHAVE\_REF | Chave de acesso do documento fiscal referenciado | 44 | E660NFC.ChvNel |
| N\_ITEM\_REF | Número do item no documento fiscal referenciado | 3 | E660RSC.SeqIpc |

### 1200 - Registro totalizador das saídas internas para consumidor final

|  |  |  |  |
| --- | --- | --- | --- |
| Campo | Descrição | Tamanho | Documentação |
| REG | 1200 | 4 | Fixo 1200 |
| QTD\_TOT\_SAIDA | Quantidade total de saídas | 9v3 | 1210.QTD\_SAIDA - 1220.QTD\_DEVOLVIDA |
| VL\_TOT\_ICMS\_EFETIVO | Valor total do ICMS efetivo nas saídas para consumidor final | 9v2 | 1210.VL\_ICMS\_EFET - 1220.VL\_ICMS\_EFETIVO |
| VL\_CONFRONTO\_ICMS\_ENTRADA | Valor de confronto do ICMS das entradas | 9v2 | 1200.QTD\_TOT\_SAIDA \* 1100.VL\_UNIT\_MED\_ICMS\_SUPORT\_ENTR |
| RESULT\_RECUPERAR\_RESSARCIR | Resultado do valor a recuperar ou a ressarcir | 9v2 | Se (1200.VL\_CONFRONTO\_ICMS\_ENTRADA - 1200.VL\_TOT\_ICMS\_EFETIVO) > 0, então 1200.VL\_CONFRONTO\_ICMS\_ENTRADA - 1200.VL\_TOT\_ICMS\_EFETIVO, senão 0 |
| RESULT\_COMPLEMENTAR | Resultado do valor a complementar | 9v2 | Se (1200.VL\_TOT\_ICMS\_EFETIVO - 1200.VL\_CONFRONTO\_ICMS\_ENTRADA) > 0, então 1200.VL\_TOT\_ICMS\_EFETIVO - 1200.VL\_CONFRONTO\_ICMS\_ENTRADA, senão 0 |
| APUR\_ICMSST\_RECUPERAR\_RESSARCIR | Apuração do ICMS ST a recuperar ou a ressarcir | 9v2 | 1200.RESULT\_RECUPERAR\_RESSARCIR \* ((1000.ALIQ\_ICMS\_ITEM - 1000.ALIQ\_FECOP) / 1000.ALIQ\_ICMS\_ITEM) |
| APUR\_ICMSST\_COMPLEMENTAR | Apuração do ICMS ST a complementar |  | 1200.RESULT\_COMPLEMENTAR \* ((1000.ALIQ\_ICMS\_ITEM - 1000.ALIQ\_FECOP) / 1000.ALIQ\_ICMS\_ITEM) |
| APUR\_FECOP\_RESSARCIR | Apuração do FECOP a ressarcir |  | 1200.RESULT\_RECUPERAR\_RESSARCIR \* (1000.ALIQ\_FECOP / 1000.ALIQ\_ICMS\_ITEM) |
| APUR\_FECOP\_COMPLEMENTAR | Apuração do FECOP a complementar |  | 1200.RESULT\_COMPLEMENTAR \* (1000.ALIQ\_FECOP / 1000.ALIQ\_ICMS\_ITEM) |

### 1210 - Registro das notas fiscais de saída interna para consumidor final

|  |  |  |  |
| --- | --- | --- | --- |
| Campo | Descrição | Tamanho | Documentação |
| REG | 1210 | 4 | Fixo 1210 |
| DT\_DOC | Data de Emissão do documento fiscal | 8 | E660NFV.DatEmi |
| CST\_CSOSN | Código da Situação Tributária | 3 | E660INV.CodStr |
| CHAVE | Chave da NF-e | 44 | E660NFV > E660IDE.ChvDoe |
| N\_NF | Número do documento fiscal | 9 | E660NFV.NumNfi |
| CNPJ\_EMIT | CNPJ Emitente | 14\* | E070FIL.NumCgc |
| UF\_EMIT | UF emitente | 2\* | E070FIL.SigUfs |
| CNPJ\_CPF\_DEST | CNPJ/CPF do destinatário | 14/11 | E085CLI.CgcCpf |
| UF\_DEST | UF do Destinatário | 2\* | E085CLI.SigUfs |
| CFOP | Código fiscal de operação e prestação | 4\* | E660NFV.NopOpe |
| N\_ITEM | Número do item do produto no documento fiscal | 3 | E660INV.SeqIpv |
| UNID\_ITEM | Unidade de medida do item | 10 | 1000.UNID\_ITEM |
| QTD\_SAIDA | Quantidade do item adquirido |  | E660INV.QtdEnt (máscara ZZZZZZZZ9,999, convertido para unidade medida estoque) |
| VL\_UNIT\_ITEM | Valor unitário do item |  | E660INV.VlrMrc / QTD\_SAIDA (máscara ZZZZZZZZ9,99) |
| VL\_ICMS\_EFET | Valor do ICMS efetivo na saída |  | E660INV.VlrMrc \* (ICMS Interno + FCP) / 100) |

### 1220 - Registro das notas fiscais de devolução das saídas internas para consumidor final

|  |  |  |  |
| --- | --- | --- | --- |
| Campo | Descrição | Tamanho | Documentação |
| REG | 1220 | 4 | Fixo 1220 |
| DT\_DOC | Data de Emissão do documento fiscal | 8 | E660NFC.DatEmi |
| CST\_CSOSN | Código da Situação Tributária | 3 | E660INC.CodStr |
| CHAVE | Chave da NF-e | 44 | E660NFC.ChvNel |
| N\_NF | Número do documento fiscal | 9 | E660NFC.NumNfi |
| CNPJ\_EMIT | CNPJ Emitente | 14\* | E095FOR.CgcCpf |
| UF\_EMIT | UF emitente | 2\* | E095FOR.SigUfs |
| CNPJ\_DEST | CNPJ do destinatário | 14\* | E070FIL.NumCgc |
| UF\_DEST | UF do Destinatário | 2\* | E070FIL.SigUfs |
| CFOP | Código fiscal de operação e prestação | 4\* | E660NFC.NopOpe |
| N\_ITEM | Número do item do produto no documento fiscal | 3 | E660INC.SeqIpc |
| UNID\_ITEM | Unidade de medida do item | 10 | 1000.UNID\_ITEM |
| QTD\_DEVOLVIDA | Quantidade do item adquirido |  | E660INC.QtdEnt (máscara ZZZZZZZZ9,999, Convertido para unidade medida estoque) |
| VL\_UNIT\_ITEM | Valor unitário do item |  | E660INC.VlrMrc / QTD\_DEVOLVIDA (máscara ZZZZZZZZ9,99) |
| VL\_ICMS\_EFET | Valor do ICMS efetivo na saída |  | E660INC.VlrMrc \* (E660RSC.PerIcs / 100) (máscara ZZZZZZZZ9,99) |
| CHAVE\_REF | Chave de acesso do documento fiscal referenciado | 44 | E660IDE.ChvDoe |
| N\_ITEM\_REF | Número do item no documento fiscal referenciado | 3 | E660INV.SeqIpv \* (ICMS Interno + FCP) / 100) |

### 1300 - Registro totalizador das saídas para outros estados

|  |  |  |  |
| --- | --- | --- | --- |
| Campo | Descrição | Tamanho | Documentação |
| REG | 1300 | 4 | Fixo 1300 |
| QTD\_TOT\_SAIDA | Quantidade total de saídas |  | 1310.QTD\_SAIDA - 1320.QTD\_DEVOLVIDA (máscara ZZZZZZZZ9,999) |
| VL\_TOT\_ICMS\_EFETIVO | Valor total do ICMS efetivo nas saídas para consumidor final |  | 1310.VL\_ICMS\_EFET - 1320.VL\_ICMS\_EFETIVO (máscara ZZZZZZZZ9,99) |
| VL\_CONFRONTO\_ICMS\_ENTRADA | Valor de confronto do ICMS das entradas |  | 1300.QTD\_TOT\_SAIDA \* 1100.VL\_UNIT\_MED\_ICMS\_SUPORT\_ENTR (máscara ZZZZZZZZ9,99) |
| RESULT\_RECUPERAR\_RESSARCIR | Resultado do valor a recuperar ou a ressarcir | 9v2 | Caso A12 = 0 (Recuperação), será obtido pelo valor do campo H04. Caso A12 = 1 (Ressarcimento), será a diferença positiva ou zero do valor do campo H04 - (menos) o campo H03 |
| APUR\_ICMSST\_RECUPERAR\_RESSARCIR | Apuração do ICMS ST a recuperar ou a ressarcir |  | 1300.RESULT\_RECUPERAR\_RESSARCIR - 1300.APUR\_FECOP\_RESSARCIR (máscara ZZZZZZZZ9,99) |
| APUR\_FECOP\_RESSARCIR | Apuração do FECOP a ressarcir |  | (1100.VL\_BC\_ICMSST\_UNIT\_MED \* (1000.ALIQ\_FECOP / 100)) \* 1300.QTD\_TOT\_SAIDA (máscara ZZZZZZZZ9,99) |

### 1310 - Registro das notas fiscais de saída para outros estados

|  |  |  |  |
| --- | --- | --- | --- |
| Campo | Descrição | Tamanho | Documentação |
| REG | 1310 | 4 | Fixo 1310 |
| DT\_DOC | Data de Emissão do documento fiscal | 8 | E660NFV.DatEmi |
| CST\_CSOSN | Código da Situação Tributária | 3 | E660INV.CodStr |
| CHAVE | Chave da NF-e | 44 | E660NFV > E660IDE.ChvDoe |
| N\_NF | Número do documento fiscal | 9 | E660INV.NumNfi |
| CNPJ\_EMIT | CNPJ Emitente | 14\* | E070FIL.NumCgc |
| UF\_EMIT | UF emitente | 2\* | E070FIL.SigUfs |
| CNPJ\_CPF\_DEST | CNPJ/CPF do destinatário | 14/11 | E085CLI.CgcCpf |
| UF\_DEST | UF do Destinatário | 2\* | E085CLI.SigUfs |
| CFOP | Código fiscal de operação e prestação | 4\* | E660NFV.NopOpe |
| N\_ITEM | Número do item do produto no documento fiscal | 3 | E660INV.SeqIpv |
| UNID\_ITEM | Unidade de medida do item | 10 | 1000.UNID\_ITEM |
| QTD\_SAIDA | Quantidade do item adquirido |  | E660INV.QtdEnt (máscara ZZZZZZZZ9,999, convertido para unidade medida estoque) |
| VL\_UNIT\_ITEM | Valor unitário do item |  | E660INV.VlrMrc / QTD\_SAIDA (máscara ZZZZZZZZ9,99) |
| VL\_ICMS\_EFET | Valor do ICMS efetivo na saída |  | E660INV.VlrIcm (máscara ZZZZZZZZ9,99) |

### 1320 - Registro das notas fiscais de devolução das saídas para outros estados

|  |  |  |  |
| --- | --- | --- | --- |
| Campo | Descrição | Tamanho | Documentação |
| REG | 1320 | 4 | Fixo 1320 |
| DT\_DOC | Data de Emissão do documento fiscal | 8 | E660NFC.DatEmi |
| CST\_CSOSN | Código da Situação Tributária | 3 | E660INC.CodStr |
| CHAVE | Chave da NF-e | 44 | E660NFC.ChvNel |
| N\_NF | Número do documento fiscal | 9 | E660NFC.NumNfi |
| CNPJ\_EMIT | CNPJ Emitente | 14\* | E095FOR.CgcCpf ou E070FIL.NumCgc |
| UF\_EMIT | UF emitente | 2\* | E095FOR.SigUfs ou E070FIL.SigUfs |
| CNPJ\_DEST | CNPJ do destinatário | 14\* | E070FIL.NumCgc |
| UF\_DEST | UF do Destinatário | 2\* | E070FIL.SigUfs |
| CFOP | Código fiscal de operação e prestação | 4\* | E660NFC.NopOpe |
| N\_ITEM | Número do item do produto no documento fiscal | 3 | E660INC.SeqIpc |
| UNID\_ITEM | Unidade de medida do item | 10 | 1000.UNID\_ITEM |
| QTD\_DEVOLVIDA | Quantidade do item adquirido |  | E660INC.QtdEnt (máscara ZZZZZZZZ9,999, convertido para unidade medida estoque) |
| VL\_UNIT\_ITEM | Valor unitário do item |  | E660INC.VlrMrc / QTD\_DEVOLVIDA (máscara ZZZZZZZZ9,99) |
| VL\_ICMS\_EFET | Valor do ICMS efetivo na saída |  | E660INC.VlrIcm (máscara ZZZZZZZZ9,99) |
| CHAVE\_REF | Chave de acesso do documento fiscal referenciado | 44 | E660IDE.ChvDoe |
| N\_ITEM\_REF | Número do item no documento fiscal referenciado | 3 | E660INV.SeqIpv |

### 1400 - Registro totalizador das saídas internas que trata o art. 119 do RICMS/17

|  |  |  |  |
| --- | --- | --- | --- |
| Campo | Descrição | Tamanho | Documentação |
| REG | 1400 | 4 | Fixo 1400 |
| QTD\_TOT\_SAIDA | Quantidade total de saídas |  | 1410.QTD\_SAIDA - 1420.QTD\_DEVOLVIDA (máscara ZZZZZZZZ9,999) |
| VL\_TOT\_ICMS\_EFETIVO | Valor total do ICMS efetivo nas saídas para consumidor final |  | 1410.VL\_ICMS\_EFET - 1420.VL\_ICMS\_EFETIVO (máscara ZZZZZZZZ9,99) |
| VL\_CONFRONTO\_ICMS\_ENTRADA | Valor de confronto do ICMS das entradas |  | 1400.QTD\_TOT\_SAIDA \* 1100.VL\_UNIT\_MED\_ICMS\_SUPORT\_ENTR (máscara ZZZZZZZZ9,99) |
| APUR\_ICMSST\_RECUPERAR\_RESSARCIR | Apuração do ICMS ST a recuperar ou a ressarcir | 9v2 | Caso A13 = 0 (Recuperação), será obtido pelo valor do campo J04. Caso A13 = 1 (Ressarcimento), será obtido pela diferença positiva ou zero do valor do campo J04 - (menos) o campo J03 |

### 1410 - Registro das notas fiscais de saídas internas que trata o art. 119 do RICMS/17

|  |  |  |  |
| --- | --- | --- | --- |
| Campo | Descrição | Tamanho | Documentação |
| REG | 1410 | 4 | Fixo 1410 |
| DT\_DOC | Data de Emissão do documento fiscal | 8 | E660NFV.DatEmi |
| CST\_CSOSN | Código da Situação Tributária | 3 | E660INV.CodStr |
| CHAVE | Chave da NF-e | 44 | E660NFV > E660IDE.ChvDoe |
| N\_NF | Número do documento fiscal | 9 | E660INV.NumNfi |
| CNPJ\_EMIT | CNPJ Emitente | 14\* | E070FIL.NumCgc |
| UF\_EMIT | UF emitente | 2\* | E070FIL.SigUfs |
| CNPJ\_CPF\_DEST | CNPJ/CPF do destinatário | 14/11 | E085CLI.CgcCpf |
| UF\_DEST | UF do Destinatário | 2\* | E085CLI.SigUfs |
| CFOP | Código fiscal de operação e prestação | 4\* | E660NFV.NopOpe |
| N\_ITEM | Número do item do produto no documento fiscal | 3 | E660INV.SeqIpv |
| UNID\_ITEM | Unidade de medida do item | 10 | 1000.UNID\_ITEM |
| QTD\_SAIDA | Quantidade do item adquirido |  | E660INV.QtdEnt (máscara ZZZZZZZZ9,999, convertido para unidade medida estoque) |
| VL\_UNIT\_ITEM | Valor unitário do item |  | E660INV.VlrMrc / QTD\_SAIDA (máscara ZZZZZZZZ9,99) |
| VL\_ICMS\_EFET | Valor do ICMS efetivo na saída |  | E660INV.VlrIsd (máscara ZZZZZZZZ9,99) |

### 1420 - Registro das notas fiscais de devolução das saídas internas que trata o art. 119 do RICMS/17

|  |  |  |  |
| --- | --- | --- | --- |
| Campo | Descrição | Tamanho | Documentação |
| REG | 1420 | 4 | Fixo 1420 |
| DT\_DOC | Data de Emissão do documento fiscal | 8 | E660NFC.DatEmi |
| CST\_CSOSN | Código da Situação Tributária | 3 | E660INC.CodStr |
| CHAVE | Chave da NF-e | 44 | E660NFC.ChvNel |
| N\_NF | Número do documento fiscal | 9 | E660NFC.NumNfi |
| CNPJ\_EMIT | CNPJ Emitente | 14\* | E095FOR.CgcCpf |
| UF\_EMIT | UF emitente | 2\* | E095FOR.SigUfs |
| CNPJ\_DEST | CNPJ do destinatário | 14\* | E070FIL.NumCgc |
| UF\_DEST | UF do Destinatário | 2\* | E070FIL.SigUfs |
| CFOP | Código fiscal de operação e prestação | 4\* | E660NFC.NopOpe |
| N\_ITEM | Número do item do produto no documento fiscal | 3 | E660INC.SeqIpc |
| UNID\_ITEM | Unidade de medida do item | 10 | 1000.UNID\_ITEM |
| QTD\_DEVOLVIDA | Quantidade do item adquirido |  | E660INC.QtdEnt (máscara ZZZZZZZZ9,999, convertido para unidade medida estoque) |
| VL\_UNIT\_ITEM | Valor unitário do item |  | E660INC.VlrMrc / QTD\_DEVOLVIDA (máscara ZZZZZZZZ9,99) |
| VL\_ICMS\_EFET | Valor do ICMS efetivo na saída |  | E660INC.VlrIsd (máscara ZZZZZZZZ9,99) |
| CHAVE\_REF | Chave de acesso do documento fiscal referenciado | 44 | E660IDE.ChvDoe |
| N\_ITEM\_REF | Número do item no documento fiscal referenciado | 3 | E660INV.SeqIpv |

### 1500 - Registro totalizador das saídas internas destinadas a contribuinte do Simples Nacional

|  |  |  |  |
| --- | --- | --- | --- |
| Campo | Descrição | Tamanho | Documentação |
| REG | 1500 | 4 | Fixo 1500 |
| QTD\_TOT\_SAIDA | Quantidade total de saídas | 9v3 | 1410.QTD\_SAIDA - 1420.QTD\_DEVOLVIDA (máscara ZZZZZZZZ9,999) |
| VL\_ICMSST\_UNIT\_ENTR | É o valor do ICMS ST a recuperar por unidade | 9v4 | (D04 /(1+MVA)) x (Coeficiente da MVA x (vezes) Percentual de Redução) x (B10) |
| APUR\_ICMSST\_RECUPERAR\_RESSARCIR | Apuração do ICMS ST a recuperar ou a ressarcir. | 9v2 | 1500.QTD\_TOT\_SAIDA \* 1500.VL\_ICMSST\_UNIT\_ENTR (máscara ZZZZZZZZ9,99) |
| MVA\_ICMSST | MVA da operação | 9v2 | E660RSC.PerMva |

### 1510 - Registro das notas fiscais de saídas internas destinadas a contribuinte do Simples Nacional

|  |  |  |  |
| --- | --- | --- | --- |
| Campo | Descrição | Tamanho | Documentação |
| REG | 1510 | 4 | Fixo 1510 |
| DT\_DOC | Data de Emissão do documento fiscal | 8 | E660NFV.DatEmi |
| CST\_CSOSN | Código da Situação Tributária | 3 | E660INV.CodStr |
| CHAVE | Chave da NF-e | 44 | E660NFV > E660IDE.ChvDoe |
| N\_NF | Número do documento fiscal | 9 | E660INV.NumNfi |
| CNPJ\_EMIT | CNPJ Emitente | 14\* | E070FIL.NumCgc |
| UF\_EMIT | UF emitente | 2\* | E070FIL.SigUfs |
| CNPJ\_CPF\_DEST | CNPJ/CPF do destinatário | 14/11 | E085CLI.CgcCpf |
| UF\_DEST | UF do Destinatário | 2\* | E085CLI.SigUfs |
| CFOP | Código fiscal de operação e prestação | 4\* | E660NFV.NopOpe |
| N\_ITEM | Número do item do produto no documento fiscal | 3 | E660INV.SeqIpv |
| UNID\_ITEM | Unidade de medida do item | 10 | 1000.UNID\_ITEM |
| QTD\_SAIDA | Quantidade do item adquirido |  | E660INV.QtdEnt (máscara ZZZZZZZZ9,999, convertido para unidade medida estoque) |
| VL\_UNIT\_ITEM | Valor unitário do item |  | E660INV.VlrMrc / QTD\_SAIDA (máscara ZZZZZZZZ9,99) |

### 1520 - Registro das notas fiscais de devolução das saídas internas destinadas a contribuinte do Simples Nacional

|  |  |  |  |
| --- | --- | --- | --- |
| Campo | Descrição | Tamanho | Documentação |
| REG | 1520 | 4 | Fixo 1520 |
| DT\_DOC | Data de Emissão do documento fiscal | 8 | E660NFC.DatEmi |
| CST\_CSOSN | Código da Situação Tributária | 3 | E660INC.CodStr |
| CHAVE | Chave da NF-e | 44 | E660NFC.ChvNel |
| N\_NF | Número do documento fiscal | 9 | E660NFC.NumNfi |
| CNPJ\_EMIT | CNPJ Emitente | 14\* | E095FOR.CgcCpf |
| UF\_EMIT | UF emitente | 2\* | E095FOR.SigUfs |
| CNPJ\_DEST | CNPJ do destinatário | 14\* | E070FIL.NumCgc |
| UF\_DEST | UF do Destinatário | 2\* | E070FIL.SigUfs |
| CFOP | Código fiscal de operação e prestação | 4\* | E660NFC.NopOpe |
| N\_ITEM | Número do item do produto no documento fiscal | 3 | E660INC.SeqIpc |
| UNID\_ITEM | Unidade de medida do item | 10 | 1000.UNID\_ITEM |
| QTD\_DEVOLVIDA | Quantidade do item adquirido |  | E660INC.QtdEnt (máscara ZZZZZZZZ9,999, convertido para unidade medida estoque) |
| VL\_UNIT\_ITEM | Valor unitário do item |  | E660INC.VlrMrc / QTD\_DEVOLVIDA (máscara ZZZZZZZZ9,99) |
| CHAVE\_REF | Chave de acesso do documento fiscal referenciado | 44 | E660IDE.ChvDoe |
| N\_ITEM\_REF | Número do item no documento fiscal referenciado | 3 | E660INV.SeqIpv |

### 1999 - Registro de encerramento do bloco 1

|  |  |  |  |
| --- | --- | --- | --- |
| Campo | Descrição | Tamanho | Documentação |
| REG | Registro 1999 | 4 | Fixo 1999 |
| QTD\_LIN | Quantidade total de linhas | 9 | A quantidade de linhas a ser informada deve considerar também o próprio registro 1999. |

### 9000 - Apuração do Total do Arquivo

|  |  |  |  |
| --- | --- | --- | --- |
| Campo | Descrição | Tamanho | Documentação |
| REG | 9000 | 4 | Fixo 9000 |
| REG1200\_ICMSST\_RECUPERAR\_RESSARCIR | Valor a recuperar ou a ressarcir nas saídas para consumidor final |  | 1200.APUR\_ICMSST\_RECUPERAR\_RESSARCIR - 1200.APUR\_ICMSST\_COMPLEMENTAR (sempre que positivo, máscara ZZZZZZZZ9,99) |
| REG1200\_ICMSST\_COMPLEMENTAR | Valor a complementar nas saídas para consumidor final |  | 1200.APUR\_ICMSST\_COMPLEMENTAR - 1200.APUR\_ICMSST\_RECUPERAR\_RESSARCIR (sempre que positivo, máscara ZZZZZZZZ9,99) |
| REG1300\_ICMSST\_RECUPERAR\_RESSARCIR | Valor a recuperar ou a ressarcir nas saídas para outros estados |  | 1300.APUR\_ICMSST\_RECUPERAR\_RESSARCIR (máscara ZZZZZZZZ9,99) |
| REG1400\_ICMSST\_RECUPERAR\_RESSARCIR | Valor a recuperar ou a ressarcir nas saidas de que trata o art. 119 |  | 1400.APUR\_ICMSST\_RECUPERAR\_RESSARCIR (máscara ZZZZZZZZ9,99) |
| REG1500\_ICMSST\_RECUPERAR\_RESSARCIR | Valor a recuperar ou a ressarcir nas saídas destinadas a contribuinte do Simples Nacional |  | 1500.APUR\_ICMSST\_RECUPERAR\_RESSARCIR (máscara ZZZZZZZZ9,99) |
| REG9000\_FECOP\_RESSARCIR | Valor a ressarcir do FECOP |  | (1200.APUR\_FECOP\_RESSARCIR + 1200.APUR\_FECOP\_RESSARCIR) - 1300.APUR\_FECOP\_COMPLEMENTAR (sempre que positivo, máscara ZZZZZZZZ9,99) |
| REG9000\_FECOP\_COMPLEMENTAR | Valor a complementar do FECOP |  | 1300.APUR\_FECOP\_COMPLEMENTAR - (1200.APUR\_FECOP\_RESSARCIR + 1200.APUR\_FECOP\_RESSARCIR) (sempre que positivo, máscara ZZZZZZZZ9,99) |

### 9999 - Registro de encerramento do arquivo

|  |  |  |  |
| --- | --- | --- | --- |
| Campo | Descrição | Tamanho | Documentação |
| REG | 9999 | 4 | Fixo 9999 |
| QTD\_LIN | Quantidade total de linhas |  | Quantidade de linhas do arquivo |
