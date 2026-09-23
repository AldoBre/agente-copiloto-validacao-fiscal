# REGISTRO 1050: REGISTRO DE SALDOS

> **Fonte:** F669GPC - Geração da Portaria CAT 42/2018 — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f669gpc.htm  
> **Trilha:** Ajuda por telas > Controladoria > Gestão de Tributos > Arquivos Fiscais > Estaduais  
> **Telas citadas:** E660INC, E660RRZ, E660RSC, E660RSV, E669CCP  
> **Identificadores de regras:** —

---
| Nº | Campo | Descrição | Tipo | Tam. | Dec. | Obrig. | Origem do Valor |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 01 | REG | Texto fixo contendo "1050" | N | 002 | - | O | - |
| 02 | COD\_ITEM | Código do Item conforme Registro 0200 | C | 060 | - | O | Mesmo código do registro 0200 |
| 03 | QTD\_INI | Quantidade Inicial do item no inicio do primeiro dia do período | N |  | 3 | O | E660RSC.QTDENT da competência anterior |
| 04 | ICMS\_TOT\_INI | Valor Inicial acumulado do total do ICMS suportado pelo contribuinte, relativamente ao item, no inicio do primeiro dia do período | N |  | 3 | O | (E669CCP.ICMFIM, competência anterior) ou (E660INC.VLRICM, E660INC.VLRSIC, E660INC.VLRFCP) |
| 05 | QTD\_FIM | Quantidade final do item no final do último dia do período. | N |  | 3 | O | E660RSC.QTDENT - E660RSV.QTDFAT/E660RRZ.QTDFAT da competência da geração |
| 06 | ICMS\_TOT\_FIM | Valor final acumulado do total do ICMS suportado pelo contribuinte, relativamente ao item, no início do primeiro dia do período. | N |  | 2 | O | (E660INC.VLRICM, E660INC.VLRSIC, E660INC.VLRFCP)  Lista o total do campo "4 - ICMS\_TOT\_INI" do registro em questão mais o total do campo "9 - ICMS\_TOT" do registro 1100 |
