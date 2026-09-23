# F075PXT - Ligação Produto x Transação

> **Fonte:** F075PXT - Ligação Produto x Transação — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075pxt.htm  
> **Trilha:** Ajuda por telas > Cadastros > Produtos e Serviços > Ligações  
> **Telas citadas:** F012FXT, F075PXT, F075SPF  
> **Identificadores de regras:** —

---
Ajuda por telas > Cadastros > Produtos e Serviços > Ligações > Produto X Transação

Tela Destinada a ligação
de produto e transação.

## Processo

Na geração de notas fiscais, caso exista a
necessidade de limitar a geração de notas fiscais com produtos
destinados a clientes e fornecedores específicos é possível configurar
as transações para que consista a ligação de produtos a clientes e
fornecedores sem ligação.

A validação é realizada
verificando se as transações de compras ou vendas obrigam as ligações
entre família, produto e serviço com a transação(campo Obrig.
Família/Produto/Serviço X Transação na aba "Outros"). Caso exista a
ligação da “família com a transação” na tela “F012FXT” não há a
necessidade de ligar o produto, e a validação será realizada através
da ligação com a família.

## Opções

Incluir

Carrega as combinações de produtos e transações disponíveis, exceto as combinações já configuradas. É possível filtrar os registros por meio do botão Seleção. Apenas o campo referente ao Código de Enquadramento Legal do IPI pode ser alterado. Por padrão, o enquadramento do IPI é sugerido do cadastro do respectivo produto.

Alterar

Carrega as combinações de produtos e transações cadastradas. Apenas o campo referente ao Código de Enquadramento Legal do IPI pode ser alterado.

Excluir

Carrega as combinações de produtos e transações cadastradas, permitindo a exclusão das combinações selecionadas.

## Campos

Código de Enquadramento Legal do IPI

Define a ligação do Código de Enquadramento de IPI entre produto e transação. Este valor pode ser sugerido nos itens das notas fiscais de entrada e saída . Para mais informações, consulte a documentação do Enquadramento de IPI.

Código do dispositivo fiscal

Dispositivo fiscal que será sugerido nas notas fiscais de entrada e saída, com base na ligação do produto com determinada transação.  
Ao incluir novas ligações, se o produto possuir um código de dispositivo cadastrado, este será sugerido para a ligação.

## Botões

Seleção

Disponibiliza os filtros da tela Parâmetros Fiscais dos Produtos - Seleção (F075SPF).

Observação

1. Além dos filtros selecionados pelo botão Seleção, os registros são apresentados de acordo com os seguintes filtros fixos:
   * Produtos:
     + Tipo de produto diferente de **S - Serviços**;
     + Situação do produto diferente de **I - Inativo**.
   * Transações
     + Situação da transação diferente de **I - Inativa**;
     + Transação não bloqueada para o usuário;
     + Transação de módulo **COF - Compras (NF Entrada Produto)** e **VEF - Vendas (NF Saída Produtos)**.

Marcar

Permite marcar todos os registros da grade.

Desmarcar

Permite desmarcar todos os registros da grade.

Aplicar

Permite a aplicação dos valores de um registro para os demais.

Observação

Só é possível aplicar o valor do campo Código de Enquadramento Legal do IPI.

## Páginas relacionadas

* [Ajuda por telas](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/ajuda-telas.htm)
* [Enquadramento de IPI](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/enquadramento-de-ipi.htm)
