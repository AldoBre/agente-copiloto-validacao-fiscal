# As tabelas envolvidas são

> **Fonte:** F000INE - Via Recebimento de Documento Eletrônico — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f000ine.htm  
> **Trilha:** Ajuda por telas > Suprimentos > Gestão de Recebimento > Notas Fiscais de Entrada  
> **Telas citadas:** E000NFC, E440DLS, E440EXF, E440IPC, E440IPR, E440ISC, E440ISR, E440LNP, E440LNS, E440NFC, E440PAR, F027SCR  
> **Identificadores de regras:** CPR-000INECN01

---
* E440NFC - Compras - Notas Fiscais de Entrada - Dados Gerais
* E440IPC - Compras - Notas Fiscais de Entrada - Itens de Produto
* E440ISC - Compras - Notas Fiscais de Entrada - Itens de Serviço
* E440PAR - Compras - Notas Fiscais de Entrada - Parcelas
* E440DLS - Compras - Notas Fiscais de Entrada - Entrada, Vencimento, Lote, Série
* E440EXF - Compras - Notas Fiscais de Entrada - Ligação Notas de Frete
* E440LNP - Compras - Ligação Entre Itens de Produto de Notas Fiscais de Entrada
* E440LNS - Compras - Ligação Entre Itens de Serviço de Notas Fiscais de Entrada
* E440IPR - Compras - Notas Fiscais de Entrada - Itens de Produto- Reforma Tributária
* E440ISR - Compras - Notas Fiscais de Entrada - Itens de Serviço - Reforma Tributária

  Nota

  Os dados relacionados à Reforma Tributária, somente serão armazenados se previamente o código CClass tiver sido cadastrado na tela F027SCR.

  Atenção

  Nos casos onde o xml importado possuir cClassTrib de isenção, exemplo 410008 ou 410999, ao realizar a importação do mesmo, se o sistema estiver parametrizado para calcular CBS/IBS, será possível perceber que nas tabelas intermediárias a base do item ficará com o valor zerado, porém, ao clicar em processar no sistema, mesmo que o código cClassTrib parametrizado seja de isenção, o sistema irá calcular uma base, e por conta disso irá gerar uma inconsistência na tela dizendo: Sugerido um valor base de XX, diferente do valor recebido 0,00.

  Nesse caso, a solução indicada é utilizar o I.R. CPR-000INECN01 podendo optar tanto por utilizar a variável CprACBSIBSProduto/Servico ou CprATransfereCBSIBSDoXMLProduto/Servico. A primeira mantem o cálculo gerado pelo sistema e a segunda matem os valores do xml respectivos à reforma.

Elas têm uma correspondência direta. Por exemplo: a tabela E440NFC (Compras - Notas Fiscais de Entrada - Dados Gerais) corresponde à tabela E000NFC (Recebimento de Documentos Eletrônicos - Notas Fiscais de Entrada - Dados Gerais).

Quando cancelada, a nota é excluída das tabelas intermediárias e também das tabelas principais de nota. Quando a nota já foi processada, o sistema faz todas as validações padrões para reabilitação e exclusão da nota.

Observação

A alteração do tipo da nota fiscal para um tipo que não considera nota fiscal de origem para valorização de estoques fará com que os registros destas NF de origem, presentes na tabela Compras - Notas Fiscais de Entrada - Ligação Notas de Frete (E440EXF), sejam ignorados, e processará o registro.

## Páginas relacionadas

* [F027SCR](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f027scr.htm)
