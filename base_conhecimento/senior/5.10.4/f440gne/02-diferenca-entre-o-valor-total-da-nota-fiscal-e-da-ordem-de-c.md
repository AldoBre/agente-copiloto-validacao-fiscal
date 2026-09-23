# “Diferença entre o valor total da Nota Fiscal e da Ordem de Compra é maior que o valor permitido para o usuário.”

> **Fonte:** F440GNE - Nota Fiscal de Entrada Agrupada — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f440gne.htm  
> **Trilha:** Ajuda por telas > Suprimentos > Gestão de Recebimento > Notas Fiscais de Entrada  
> **Telas citadas:** F099UCP  
> **Identificadores de regras:** —

---
Essa mensagem ocorrerá, sempre que as seguintes condições estiverem atendidas:

* O campo Aprovar NFE Diferença, da tela F099UCP, estiver diferente de "S - Sim";
* O campo Valor Aceito Dif. NFE, da tela F099UCP, tem que ser diferente de "999999999";
* Soma do Valor Líquido de todos os itens da Nota de Entrada, e deduz, desse valor, a soma do Valor Líquido de todos os itens da Ordem de Compra:
  + Se o resultado dessa subtração for maior que 0 e maior que o campo Valor Aceito Dif. NFE.
