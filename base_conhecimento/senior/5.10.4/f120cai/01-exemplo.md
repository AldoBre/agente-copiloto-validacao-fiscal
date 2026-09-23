# Exemplo

> **Fonte:** F120CAI - Cálculos dos Itens de Produto do Pedido — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f120cai.htm  
> **Trilha:** Ajuda por telas > Mercado > Gestão de Vendas > Pedidos > Pedido Agrupado  
> **Telas citadas:** —  
> **Identificadores de regras:** —

---
Itens  
Quantidade Preço Perc.IPI Total  
10 10,00 5,00 105,00  
10 10,00 0,00 100,00

Valor Frete: 10,00

Rateio Frete:  
Item 1: (10/(105+100))\*105 = 5,12  
Item 2: (10/(105+100))\*100 = 4,88

Valor do IPI após cálculo do frete: (105,12 \* 0,05) = 5,26  
Itens  
Quantidade Preço Perc.IPI Total  
10 10,00 5,00 105,26  
10 10,00 0,00 100,00

Total da nota: 205,26

Detalhe sobre a fórmula: Primeiramente, é calculado o valor do frete sobre 205,00(105 + 100). Uma vez que o frete foi
calculado, o sistema recalcula o valor do IPI.
