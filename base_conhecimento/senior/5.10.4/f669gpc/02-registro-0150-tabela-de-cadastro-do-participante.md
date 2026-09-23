# REGISTRO 0150: TABELA DE CADASTRO DO PARTICIPANTE)

> **Fonte:** F669GPC - Geração da Portaria CAT 42/2018 — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f669gpc.htm  
> **Trilha:** Ajuda por telas > Controladoria > Gestão de Tributos > Arquivos Fiscais > Estaduais  
> **Telas citadas:** E008CEP, E085CLI, E095FOR  
> **Identificadores de regras:** —

---
| Nº | Campo | Descrição | Tipo | Tam. | Dec. | Obrig. | Origem do Valor |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 01 | REG | Texto fixo contendo "0150" | C | 004 |  | O | Valor fixo "0150" |
| 02 | COD\_PART | Código de identificação do participante no arquivo | C | 060 |  | O | E095FOR.CODFOR, E085CLI.CODCLI concatenado com o texto CLI/FOR |
| 03 | NOME | Nome pessoal ou empresarial do participante | C |  |  | O | E095FOR.NOMFOR, E085CLI.NOMCLI |
| 04 | COD\_PAI | Código do País participante, conforme a tabela indicada no item 3.2.1 do Ato COTAPE/ICMS nº 09, de 18 de abril de 2008. | C | 005 |  | OC | E095FOR.CODPAI, E085CLI.CODPAI |
| 05 | CNPJ | CNPJ do participante | N | 014 |  | OC | E095FOR.CGCCPF/E095FOR.DOCIDE, E085CLI.CGCCPF/E095FOR.DOCIDE |
| 06 | CPF | CPF do participante | N | 011 |  | OC | E095FOR.CGCCPF, E085CLI.CGCCPF |
| 07 | IE | Inscrição Estadual do participante | C | 014 |  | OC | E095FOR.INSEST, E085CLI.INSEST |
| 08 | COD\_MUN | Código do município, conforme a tabela IBGE | N | 007 |  | OC | E008CEP.CODIBG |
