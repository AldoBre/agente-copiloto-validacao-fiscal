# REGISTRO 0000: ABERTURA DO ARQUIVO DIGITAL E IDENTIFICAÇÃO DO CONTRIBUINTE)

> **Fonte:** F669GPC - Geração da Portaria CAT 42/2018 — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f669gpc.htm  
> **Trilha:** Ajuda por telas > Controladoria > Gestão de Tributos > Arquivos Fiscais > Estaduais  
> **Telas citadas:** E008CEP, E070FIL  
> **Identificadores de regras:** —

---
| Nº | Campo | Descrição | Tipo | Tam. | Dec. | Obrig. | Origem do Valor |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 01 | REG | Texto fixo contendo "0000" | C | 004 |  | O | Valor fixo "0000" |
| 02 | PERIODO | Período das informações contidas no arquivo | N | 006 |  | O | Competência da Tela |
| 03 | NOME | Nome empresarial da entidade | C |  |  | O | E070FIL.SIGFIL |
| 04 | CNPJ | Número | C | 014 |  | O | E070FIL.NUMCGC ou E070FIL.DOCIDE |
| 05 | IE | Inscrição Estadual da entidade. | C | 014 |  | O | E070FIL.INSEST |
| 06 | COD\_MUN | Código do município do domicilio fiscal da entidade, conforme a tabela IBGE | N | 007 |  | O | E008CEP.CODIBG |
| 07 | COD\_VER | Código da versão do leiaute conforme a Tabela de Versão do Leiaute | N | 02 |  | O | Versão informada na tela. |
| 08 | COD\_FIN | Código da finalidade do arquivo conforme a Tabela de Finalidade de Entrega do Arquivo | N | 02 |  | O | Campo finalidade informado na tela. |
