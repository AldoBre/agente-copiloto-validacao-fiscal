# REGISTRO 0200: TABELA DE IDENTIFICAÇÃO DO ITEM

> **Fonte:** F669GPC - Geração da Portaria CAT 42/2018 — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f669gpc.htm  
> **Trilha:** Ajuda por telas > Controladoria > Gestão de Tributos > Arquivos Fiscais > Estaduais  
> **Telas citadas:** E015MED, E022CLF, E075DER, E075PRO, E660RSC, F009PPE, F019TIE, F019TIS, F070PSE, F075GFP, F075PRO  
> **Identificadores de regras:** —

---
| Nº | Campo | Descrição | Tipo | Tam. | Dec. | Obrig. | Origem do Valor |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 01 | REG | Texto fixo contendo "0200" | C | 004 |  | O |  |
| 02 | COD\_ITEM | Código do item | C | 060 |  | O | E660RSC.CODPRO, E660RSC.CODER, E075DER.ITEFIS |
| 03 | DESCR\_ITEM | Descrição do item | C |  |  | O | E075DER.DESFIS, E075PRO.DESNFV |
| 04 | COD\_BARRA | Representação alfanumérica do código de barra do produto | C |  |  | OC | E075DER.CODBAR |
| 05 | UNID\_INV | Unidade de medida utilizada na quantificação de estoques | C | 006 |  | O | E015MED.UNIFIS |
| 06 | COD\_NCM | Código da Nomenclatura Comum do MERCOSUL | C | 008 |  | O | E022CLF.CLAFIS |
| 07 | ALIQ\_ICMS | Alíquota de ICMS aplicável ao item nas operações internas | N |  | 02 | OC | Será listado conforme a regra:  * Produto ter ICMS (conforme tela F075PRO ou F075GFP * Percentual de ICMS interno da ligação do produto/serviço com o estado (conforme tela F070PSE) * Percentual do ICMS de contribuinte na entrada ou percentual do ICMS de contribuinte na saída do cadastro do ICMS especial (conforme tela F019TIE) * Percentual do imposto do estado do cadastro do ICMS ST (conforme tela F019TIS) * Percentual de ICMS interno da UF destino cadastrado nos parâmetros por estado (conforme tela F009PPE) |
| 08 | CEST | Código Especificador da Substituição Tributária | N | 007\* |  | OC | E022CLF.CODCES |

## Páginas relacionadas

* [F075PRO](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075pro.htm)
* [F075GFP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075gfp.htm)
* [F070PSE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070pse.htm)
* [F019TIE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f019tie.htm)
* [F019TIS](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f019tis.htm)
* [F009PPE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f009ppe.htm)
