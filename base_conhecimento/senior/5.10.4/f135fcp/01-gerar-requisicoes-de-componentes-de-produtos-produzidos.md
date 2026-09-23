# Gerar requisições de componentes de produtos produzidos

> **Fonte:** F135FCP - Formação de Cargas (via Pedidos) — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f135fcp.htm  
> **Trilha:** Ajuda por telas > Mercado > Gestão de Distribuição > Cargas > Formação  
> **Telas citadas:** E207EME, E700CMM, F070FES, F135MPF  
> **Identificadores de regras:** —

---
A geração automática de requisições dos componentes de produtos manufaturados, registrados na tabela Ficha - Modelo - Componentes (E700CMM), está subordinada ao parâmetro Gerar requisição
ao fechar carga, dos parâmetros da filial para vendas e faturamento.

Os registros serão gerados na tabela de Estoques - Requisições (E207EME), sendo que a requisição do produto pai (produzido) não pode ser gerada.

Se o parâmetro Indicativo se manipula req. na carga (dos parâmetros de
usuário para vendas e faturamento) estiver definido igual a "S - Sim", na tela Manutenção de Pré-faturas (F135MPF) serão
disponibilizados os botões Liberar Carga e Gerar Req.. O botão Liberar Carga altera a situação das pré-faturas que geraram requisições para a situação "
3 - Para faturar". O botão Gerar Req. permite gerar novamente as requisições.

Observação

O campo Qtd. Disp. tem a funcionalidade de mostrar o que há em estoque (conforme o critério de formação de estoque da filial) somado ao que há em estoque reserva normal para o pedido cuja carga está sendo formada.

## Exemplo 1

* Critério para formação na tela F070FES igual a 8 - Estoque - Análise/Carga - Bloqueio - Reserva;
* Produto possui 10 quantidades em estoque;
* Produto possui 8 pedidos, sendo 1 quantidade para cada pedido e todos com reserva de estoque;
* Dos 8 pedidos, 2 já possuem formação de carga fechados;
* Neste cenário, temos então para o produto: 10 quantidades em estoque, 6 quantidades em reserva normal e 2 quantidades em reserva exclusiva (referentes ao pedidos que já têm carga formada) e devido ao fato de o critério para formação de estoque ser 8 - Estoque - Análise/Carga - Bloqueio - Reserva, a quantidade disponível para faturamento será 2 (10 - 6 - 2 = 2), porém o campo Qtd. Disp será mostrado com 3, pois será somado 2 (quantidade disponível para faturamento) mais 1 (quantidade de estoque reserva para o pedido que está sendo faturado);
* Caso o critério para formação de carga não fosse 3, 4, 7 ou 8, a quantidade de estoque em reserva normal para o item do pedido não seria somado na quantidade para o campo Qtd. Dis

## Exemplo 2

* Critério para formação na tela F070FES igual a 8 - Estoque - Análise/Carga - Bloqueio - Reserva;
* Produto possui 2 quantidades em estoque;
* Existe um pedido feito com o produto com quantidade igual a 1, porém não possui reserva normal; nesse cenário, quando o item estiver selecionado, o campo Qtd. Disp será mostrado com quantidade 1, pois como o pedido não possuía reserva normal, a quantidade a faturar será subtraída. Com o item não selecionado, o campo Qtd. Disp ficará com a quantidade 2.

## Páginas relacionadas

* [Manutenção de Pré-faturas (F135MPF)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f135mpf.htm)
* [F070FES](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070fes.htm)
