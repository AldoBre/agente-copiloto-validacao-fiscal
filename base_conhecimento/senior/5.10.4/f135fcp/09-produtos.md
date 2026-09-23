# Produtos

> **Fonte:** F135FCP - Formação de Cargas (via Pedidos) — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f135fcp.htm  
> **Trilha:** Ajuda por telas > Mercado > Gestão de Distribuição > Cargas > Formação  
> **Telas citadas:** E135PES, E135PFA, E135PLA, E140IPV, F000DLS, F135CIF, F135FCS, F135LCR, F135ROT, F135TRA  
> **Identificadores de regras:** —

---
Serão visualizados todos os produtos e suas derivações disponíveis pertencentes aos pedidos presentes na grade superior.

A quantidade de venda é herdada do pedido ao carregar. Qualquer alteração em relação a quantidade a faturar ou unidade de medida será recalculado sugerindo o valor de conversão cadastrado na unidade de medida de venda.

Observação

* Se a unidade de medida de venda for diferente da unidade de medida, sempre será efetuado o cálculo de conversão aplicando o valor calculado sobre o campo Quantidade da Unidade de Medida de venda;
* Todos os itens presentes nas grades virão marcados, podendo ser desmarcados, influenciando assim na quantidade a ser faturada.

Valor líquido do pedido

Representa o valor da quantidade dos produtos em aberto.

Valor financeiro

Representa o valor financeiro dos produtos em aberto.

Valor Produto

Representa o valor da quantidade total dos produtos.

Vlr. Líquido Produto

Representa o valor da quantidade total dos produtos.

% Desc., % Desc.1, % Desc.2, % Desc.3, % Desc.4

Percentuais de desconto.

Valor Desconto   
Valor do desconto.

Nota

* Quando existe o percentual de desconto informado no pedido, a pré-fatura gerada com base nesse pedido não grava o Valor Desconto na tabela de Vendas - Análise de Embarque - itens de Produto e Serviço (E135PES). Isso ocorre, pois o valor de desconto da pré-fatura pode alterar de acordo com a manipulação efetuada nesta;
* Na tela F135CIF referente à consulta de itens de pré-fatura, ao pesquisá-la, o valor de desconto é calculado automaticamente de acordo com o percentual desconto gravado na tabela E135PES;
* Quando gerado uma nota fiscal via pedido ou via pré-fatura, o valor de desconto é gravado na tabela de Vendas - Notas Fiscais de Saída - Itens de Produtos (E140IPV), pois trata-se de um documento fiscal;
* Quando é gerado um pedido apenas com valor de desconto, a pré-fatura gerada com base nesse pedido, herda este valor. O valor não é alterado, pois não existe percentual de desconto;
* A nota fiscal gerada com base em uma pedido ou pré-fatura, com valor de desconto e sem percentual de desconto, também herda o valor de desconto.

Endereçamento

Apresenta o código do endereçamento do produto. O valor apresentado segue a seguinte ordem:

1. Relacionamento produto X depósito;
2. Derivação;
3. Cadastro produto.

Também é utilizado e apresenta o mesmo comportamento na tela Formação de Cargas Simplificada (via Pedidos) - F135FCS.

### Campos

Dist.Lote

Acesso à tela F000DLS para a distribuição de lotes para um item controlado por lote.

Veículos

Acesso à tela F135TRA pata a seleção dos veículos para o transporte da carga. Os veículos selecionados serão utilizados na formação da carga. Havendo mais de um veículo selecionado, os demais veículos serão gravados na tabela E135PLA. Os campos Transp./Placa e Transp./Motorista
serão gravados da tabela E135PFA com o primeiro registro selecionado na tela F135TRA.

Pedido/Rota

Acesso à tela  F135ROT com o resumo dos pedidos de vendas selecionados, agrupados por rota.

Observação

Esse botão tem como objetivo exibir as rotas, a quantidade de pedidos e a quantidade de entregas da rota.

O sistema exibirá a quantidade de pedidos para cada rota e a quantidade de entregas será definida conforme a data de previsão. Para cada data de previsão diferente em uma mesma rota, será considerada uma entrega.

Na geração de Pré-Fatura com base em um Pedido que possui Parcelas especais, o sistema irá gerar as Parcelas da Seguinte forma quando o Parâmetro estiver igual a:

S:  
O sistema refaz o calculo do valor das parcelas da Pré-Fatura com base no Valor Financeiro da Pré-Fatura x o Percentual de cada Parcela herdado do Pedido.

Esse recalculo é necessário pois muitas vezes o valor financeiro da PFA é alterado, uma vez que a transação da PFA é diferente da transação de Pedido.

Atualmente não existe uma forma de manter o valor de cada parcela da PFA igual as Parcelas do Pedido.

N:  
Esse parâmetro indica se as parcelas das pré-faturas devem ser geradas na formação das Cargas.

Quando esse parâmetro está igual a N, o sistema não gera parcelas para as PFAs e gera as parcelas da Nota com base nas parcelas do Pedido.

O único efeito colateral do uso desse parâmetro com valor igual a N é que não existirão parcelas na carga.

## Exemplo

| Ped | Rota | Data prev. |
| --- | --- | --- |
| 1 | 02 | 01/01/2015 |
| 2 | 02 | 01/01/2015 |
| 3 | 02 | 02/02/2015 |
| 4 | 05 | 01/01/2015 |

O pedido 3 alterou a data de previsão, então, é gerado um novo valor de entrega. Caso fosse 01/01/2015, a quantidade de entregas seria 1.

Na tela de pedido/rotas, a informação será apresentada da seguinte maneira:

| Rota | Qtd. Entregas | Qtd. Pedidos |
| --- | --- | --- |
| 02 | 2 | 3 |
| 05 | 1 | 1 |

Lacres

Ao clicar neste botão, a tela Controle de Lacres (F135LCR) é aberta. A tela Controle de Lacres, por sua vez, possui o objetivo de controlar e efetuar os apontamentos dos números de lacres dos veículos. Os lacres são, basicamente, cadeados maleáveis com numeração própria e servem para lacrar as portas dos caminhões envolvidos no processo. É a garantia de que nenhuma porta foi aberta ou violada desde a saída do Depósito até a chegada ao destino.

## Páginas relacionadas

* [F135CIF](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f135cif.htm)
* [Formação de Cargas Simplificada (via Pedidos) - F135FCS](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f135fcs.htm)
* [F000DLS](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000dls.htm)
* [F135TRA](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f135tra.htm)
* [F135ROT](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f135rot.htm)
* [Controle de Lacres (F135LCR)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f135lcr.htm)
