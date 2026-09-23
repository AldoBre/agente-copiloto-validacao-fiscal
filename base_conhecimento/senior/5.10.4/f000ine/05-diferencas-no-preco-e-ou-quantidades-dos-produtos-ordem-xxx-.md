# “Diferenças no preço e/ou quantidades dos Produtos : Ordem: XXX - Sequência: XXX”

> **Fonte:** F000INE - Via Recebimento de Documento Eletrônico — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f000ine.htm  
> **Trilha:** Ajuda por telas > Suprimentos > Gestão de Recebimento > Notas Fiscais de Entrada  
> **Telas citadas:** F070EMP, F099UCP  
> **Identificadores de regras:** —

---
Essa mensagem ocorrerá, sempre que as seguintes condições estiverem atendidas:

* O campo Aprovar NFE Diferença, da tela F099UCP, estiver diferente de "S - Sim";
* Ou o campo % Diferença Qtde. NFE X OC OU o campo % Diferença Valor NFE X OC, ambos da tela F099UCP, deve ser diferente de "999";
* O campo Permite ligar item OC em sit. 8 à NF de ent., tela F070EMP, estar igual à "N";
* Ou se valor do Preço Unitário do item da Nota de Entrada for maior que:
  + O valor do Preço Unitário UM Fornecedor do item da Ordem de Compra já composto do adicional do campo % Diferença Valor NFE X OC;
* Ou se a quantidade do campo Qtde. Recebida do item da Nota de Entrada for maior que:
  + O resultado do campo % Diferença Qtde. NFE X OC aplicado sobre o campo Qtde. Pedida do item da Ordem de Compra somado no campo Qtde. Aberto do item da Ordem de Compra.
