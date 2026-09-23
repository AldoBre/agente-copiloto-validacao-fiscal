# REGISTRO 1100: REGISTRO DE DOCUMENTO FISCAL ELETRÔNICO PARA FINS DE
RESSARCIMENTO DE SUBSTITUIÇÂO TRIBUTÁRIA OU ANTECIPAÇÃO

> **Fonte:** F669GPC - Geração da Portaria CAT 42/2018 — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f669gpc.htm  
> **Trilha:** Ajuda por telas > Controladoria > Gestão de Tributos > Arquivos Fiscais > Estaduais  
> **Telas citadas:** E022CLF, E660IDE, E660INC, E660INV, E660NFC, E660NFV  
> **Identificadores de regras:** —

---
| Nº | Campo | Descrição | Tipo | Tam. | Dec. | Obrig. | Origem do Valor |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 01 | REG | Texto fixo contendo "1100" | N | 002 |  | O |  |
| 02 | CHV\_DOC | Chave do Documento Fiscal Eletrônico | N | 044 |  | O | E660NFC.CHVNEL, E660NFV.CHVNEL  Lista a chave da NF-e (E660NFC.ChvNel ou E660IDE.ChvDoe) |
| 03 | DATA | Data da entrada da mercadoria ou da saída | N | 008 |  | O | E660NFC.DATENT, E660NFV.DATEMI |
| 04 | NUM\_ITEM | Número sequencial do item no Documento Fiscal Eletrônico | N | 003 |  | O | E660INC.SEQIPC, E660INV.SEQIPV |
| 05 | IND\_OPER | Indicador do tipo de operação: 0- Entrada; 1- Saída | N | 001 |  | O |  |
| 06 | COD\_ITEM | Código do item conforme Registro 0200 | C | 060 |  | O | Código do registro 0200 |
| 07 | CFOP | Código Fiscal de Operação e Prestação | N | 004 |  | O | E660NFC.NOPOPE / E660NFV.NOPOPE |
| 08 | QTD. | Quantidade do Item | N |  | 3 | O | E660INC.QTDENT / E660INV.QTDENT |
| 09 | ICMS\_TOT | Valor total do ICMS suportado pelo contribuinte nas operações de entrada (v. observação feita para o Registro 1050) | N |  | 2 | OC | (E660INC.VLRICM, E660INC.VLRSIC, E660INC.VLRFCP)  Irá listar o valor do crédito do ICMS ST nas operações de entrada |
| 10 | VL\_CONFR | Valor de confronto nas operações de saída | N |  | 2 | OC | (E660INC.VLRICM, E660INC.VLRSIC, E660INC.VLRFCP) ou (E660INV.VLRCTB \* Aliquota Interna)  Irá listar o conteúdo de E660INV.VlrCtb \* 0200.Campo07 |
| 11 | COD\_LEGAL | Código de Enquadramento Legal da hipótese de Ressarcimento ou Complemento de ICMS ST | N | 001 |  | OC | E022CLF.CODENQ  Lista conforme abaixo:   * 4 - Nota fiscal de saída com CFOP iniciada em 6; * 3 - Nota fiscal de saída com CST ICMS igual a X40 ou X41; * 2 - Devolução de compra ou CFOP 5927; * 1 - Venda a consumidor final e CFOP iniciado em 5; * 0 - Demais casos. |
