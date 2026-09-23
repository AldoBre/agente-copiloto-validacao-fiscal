# Regras para atualização do pedido no processo de cobranças e remessas

> **Fonte:** F140PRE - Preparação da Nota Fiscal de Saída — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f140pre.htm  
> **Trilha:** Ajuda por telas > Mercado > Gestão de Faturamento e Outras Saídas > Notas Fiscais de Saída  
> **Telas citadas:** F140PRE  
> **Identificadores de regras:** —

---
**Importante**

Ao dar início no processo por meio da tela F140PRE, ele **não pode** ser continuado por meio de outra tela.

Faça a geração de uma nota de cobrança pela tela F140PRE, utilizando uma transação de cobrança e a opção para não atualizar o pedido que existe na tela. Neste momento o pedido é atualizado com a chave da nota fiscal de cobrança, mas nenhuma quantidade é consumida do pedido, que permanece aberto total.

A partir de então podem ser feitas remessas que devem ser geradas a partir do pedido e não da nota fiscal de cobrança. Porém, caso a nota fiscal de cobrança tenha sido feita pela tela F140PRE, obrigatoriamente a nota fiscal de remessa também terá que ser feita por esta tela.

Além disso, é possível gerar análises/cargas a partir do pedido e faturar essas cargas. O faturamento delas será a remessa das mercadorias. E o pedido será atualizado.
