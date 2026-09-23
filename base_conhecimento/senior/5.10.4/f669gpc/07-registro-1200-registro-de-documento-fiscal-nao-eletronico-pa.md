# REGISTRO 1200: REGISTRO DE DOCUMENTO FISCAL NÃO-ELETRÔNICO PARA FINS
DE RESSARCIMENTO DE SUBSTITUIÇÃO TRIBUTÁRIA – SP

> **Fonte:** F669GPC - Geração da Portaria CAT 42/2018 — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f669gpc.htm  
> **Trilha:** Ajuda por telas > Controladoria > Gestão de Tributos > Arquivos Fiscais > Estaduais  
> **Telas citadas:** E020SNF, E022CLF, E660INC, E660INV, E660NFC, E660NFV  
> **Identificadores de regras:** —

---
| Nº | CAMPO | DESCRIÇÃO | Tipo | Tam. | Dec. | Obrig. | Origem do Valor |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 01 | REG | Texto fixo contendo 1200 | N | 002 |  | O |  |
| 02 | COD\_PART | Código de identificação do participante no arquivo conforme Registro 0150 | C | 060 |  | OC | Mesmo código do registro 0150 |
| 03 | COD\_MOD | Código do modelo do documento fiscal, conforme a tabela 4.1.1 do SPED | C | 002 |  | O | E660NFC.CODEDC / E660NFV.CODEDC |
| 04 | ECF\_FAB | Número de série de fabricação do equipamento ECF | C | 21 |  | OC | Fixo 000000000000000000000 |
| 05 | SER | Série do documento fiscal | C | 003 |  | OC | E660NFC.CODSEL / E020SNF.CODSE |
| 06 | NUM\_DOC | Número do documento fiscal | N | 003 |  | O | E660INC.NUMNFI / E660INV.NUMNFI |
| 07 | NUM\_ITEM | Número sequencial do item do documento | N | 003 |  | O | E660INC.SEQITE / E660INV.SEQITE |
| 08 | IND\_OPER | Indicador do tipo de operação: 0 - Entrada; 1 - Saída | N | 001 |  | O |  |
| 09 | Data | Data de entrada da mercadoria ou da saída | N | 008 |  | O | E660NFC.DATENT / E660NFV.DATEMI |
| 10 | CFOP | Código Fiscal de Operação e Prestação | N | 004\* |  | O | E660NFC.NOPOPE / E660NFV.NOPOPE |
| 11 | COD\_ITEM | Código o item conforme Registro 0200 | C | 060 |  | O | Mesmo código do registro 0200 |
| 12 | QTD | Quantidade do Item | N |  | 3 | O | E660INV.QTDENT / E660INC.QTDENT |
| 13 | ICMS\_TOT | Valor total do ICMS suportado pelo contribuinte nas operações de entrada (v. observação feita para o Registro 1050) | N |  | 2 | OC | (E660INC.VLRICM, E660INC.VLRSIC, E660INC.VLRFCP) |
| 14 | VL\_CONFR | Valor de confronto nas operações de saída. | N |  | 2 | OC | (E660INC.VLRICM, E660INC.VLRSIC, E660INC.VLRFCP) ou (E660INV.VLRCTB \* Aliquota Interna) |
| 15 | COD\_LEGAL | Código de enquadramento Legal do Ressarcimento ou Complemento | N | 001 |  | OC | E022CLF.CODENQ |
