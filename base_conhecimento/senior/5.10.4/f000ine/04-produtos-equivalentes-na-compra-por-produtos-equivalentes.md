# Produtos equivalentes na Compra por Produtos Equivalentes

> **Fonte:** F000INE - Via Recebimento de Documento Eletrônico — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f000ine.htm  
> **Trilha:** Ajuda por telas > Suprimentos > Gestão de Recebimento > Notas Fiscais de Entrada  
> **Telas citadas:** —  
> **Identificadores de regras:** —

---
A rotina de entrada de notas via recebimento eletrônico também permitirá o recebimento de Produtos Equivalentes.

O comportamento da rotina nessa ocasião passa a ser o seguinte:

1. Ao receber uma Nota Fiscal de Entrada com um produto que não possua vínculo à uma Ordem de Compra e realizar seu processamento, o sistema verificará se o produto em questão possui equivalentes;
2. Se possuir, o sistema buscará uma Ordem de Compra que possua o produto equivalente com a situação 1 (aberto total) ou 2 (aberto parcial);
3. Caso encontre, o sistema irá incluir o item atual da Nota Fiscal de Entrada na Ordem de Compra localizada, informando a quantidade recebida e preço unitário, além de realizar o cancelamento do produto equivalente;
4. Por último, o item da Nota Fiscal será atualizado com o vínculo da Ordem de Compra e a nota será fechada.

**Observação**

Essa ação somente será executada caso o campo **Fechar nota após processar**, encontrado no cabeçalho da tela, esteja marcado.

Além disso, a coluna **O.C. Equivalente**, encontrada na guia Itens de Produto, irá apresentar as ordens de compras equivalentes quando as notas fiscais pendentes forem mostradas na tela. Esta coluna é somente leitura.

**Importante**

Esse recurso não deve ser usado para permitir o recebimento de mais de um item da nota de entrada para o mesmo item da ordem de compra. O comportamento padrão do ERP XT é vincular os itens na proporção de 1:1. Caso opte por habilitar o parâmetro para esse propósito, recomendamos fortemente que seja feito um teste em ambiente de homologação, validando todos os processos impactados, especialmente:

* Fechamento ou reabilitação da nota de entrada;
* Atualização de saldo da ordem de compra e declarações fiscais (SPED).

O **ERP XT** não se responsabilizará por eventuais inconsistências geradas por esse desvio de função do parâmetro de produtos equivalentes.
