# Carga dos pedidos

> **Fonte:** F135FCP - Formação de Cargas (via Pedidos) — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f135fcp.htm  
> **Trilha:** Ajuda por telas > Mercado > Gestão de Distribuição > Cargas > Formação  
> **Telas citadas:** —  
> **Identificadores de regras:** —

---
Somente com estoque

Indicativo se antes de mostrar os itens na grade deve verificar o saldo em estoque, conforme o parâmetro para vendas da filial, se a quantidade vinda do pedido for superior a quantidade em estoque será ainda verificado se o pedido aceita faturamento parcial. Caso o pedido não aceita faturamento parcial e a quantidade disponível no estoque for inferior a quantidade do item do pedido, este item ou pedido, conforme a situação, não será carregado para seleção.

## Exemplo

* Estoque disponível do produto X com quantidade 100 em estoque.
* Pedido 1 aceita faturamento parcial com quantidade 200 para o produto X.
* Pedido 2 não aceita faturamento parcial com quantidade 200 para o produto X.
* Somente o pedido 1 será exibido e a quantidade máxima permitida para a formação da carga será o saldo disponível em estoque, ou seja, quantidade 100.

Com quantidade disponível

Indicativo se deve permitir que a quantidade a faturar seja o saldo do produto descontadas as quantidades já utilizadas do produto carregados na tela. Somente estará habilitado se o parâmetro Mostra só com estoque estiver desmarcado. Este parâmetro será gravado por usuário.

## Exemplo

* Estoque disponível do produto X com quantidade 300 em estoque.
* Pedido 1 aceita faturamento parcial com quantidade 200 para o produto X.
* Pedido 2 não aceita faturamento parcial com quantidade 200 para o produto X.
* Ambos os pedidos serão carregados na grade, porém somente será possível selecionar o primeiro pedido, tendo em vista que o segundo pedido não aceita faturamento parcial e o saldo disponível descontada a quantidade utilizada pelo primeiro pedido é igual a 100, ou seja, inferior a quantidade solicitada no pedido 2.
* Para selecionar o pedido 2 será necessário desmarcar o item do produto X do pedido 1. Dessa forma, ao desmarcar o item com o produto X do pedido 1 o saldo disponível deste passará a ser 300.
* Após selecionar o pedido 2, o saldo será de 100. Neste caso o pedido 1 também poderá ser selecionado, pois aceita faturamento parcial, porém a quantidade possível será 100.

Sem estoque

Indicativo se permitirá formar cargas com itens sem estoque disponível. Esta opção não leva em consideração o saldo disponível do produto no estoque. Também não será realizado nenhum cálculo de abatimento das quantidades já utilizadas do produto. Existindo mais de um pedido com o mesmo produto, o estoque disponível será sempre o mesmo.

## Exemplo

* Estoque disponível do produto X com quantidade 5 em estoque.
* Pedido 1 com quantidade 4 para o produto X. Saldo Estoque exibido na linha será 1 (5 - 4)
* Pedido 2 com quantidade 5 para o produto X. Saldo Estoque exibido na linha será 0 (5 - 4)
* Pedido 3 com quantidade 7 para o produto X. Saldo Estoque exibido na linha será -2 (5 - 7)
* OU seja, para cada item de pedido com o mesmo produto X a quantidade disponível será sempre a mesma que, neste exemplo é 5.

Com estoque embalado

Irá fazer praticamente o que a opção Somente com estoque, só ao invés de considerar os itens irá considerar somente os itens que já foram embalados e que esta embalagem já esteja com a situação de Fechada ou Conferida, caso não houver ao menos um item do pedido que seja atendido, o pedido não irá aparecer para formar a carga.

**Observação**

O campo Vlr líquido apresenta a soma do valor líquido da quantidade a faturar/aberta.
