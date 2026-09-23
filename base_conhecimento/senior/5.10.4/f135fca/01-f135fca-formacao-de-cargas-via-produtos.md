# F135FCA - Formação de Cargas Via Produtos

> **Fonte:** F135FCA - Formação de Cargas Via Produtos — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f135fca.htm  
> **Trilha:** Ajuda por telas > Mercado > Gestão de Distribuição > Cargas > Formação  
> **Telas citadas:** E120IPD, E120PED, E135PES, E135PFA, E135PLA, F000CRT, F000DLS, F135FCA, F135ROT, F135SCA, F135TRA  
> **Identificadores de regras:** COM-135CRIFE01, VEN-135PPETI01

---
Ajuda por telas > Mercado > Gestão de Distribuição > Cargas > Formação > Via Produtos

Tela destinada à formação de cargas pela análise dos produtos

## Processos

* A seleção dos itens do pedido será efetuado na filial ativa, permitindo porém definir outras filiais. Ao processar a carga, esta será gerada na filial ativa, porém as tabelas de pré-fatura (E135PES) guardarão no campo FilPed (filial do pedido) a filial definida do pedido. O critério de formação de estoques, os parâmetros por estado, as impressões e a análise de embarque geradas, continuarão a ser geradas apenas para a filial ativa no momento da inclusão.
* Também na execução da rotina, há a possibilidade de utilizar o processo de pendências que poderão ser atribuídas a carga. Para realizar a ligação das pendências que serão geradas à carga, verifique em: Pendências para a Carga.

**Reforma Tributária – Consulta de Impostos**

Esta tela permite o acesso à Consulta de Impostos da Reforma Tributária (F000CRT), o qual pode ser feito das seguintes formas:

* Por meio do botão CBS e IBS, disponível nos botões de Cálculo para telas de Pedido, Ordem de Compra, Cotação e Nota Fiscal;
* Ou diretamente pelo botão CBS e IBS para as telas de consulta.

Para conferir todas as rotinas impactadas pela Reforma Tributária, acesse esta documentação.

## Campos

Previsão Faturamento

Período inicial e final da previsão faturamento.

Transp/placa

Transportadora e placa do veículo. É obrigatório informar uma transportadora. Ao clique do botão Processar, se este campo não possuir informação será exibida mensagem ao usuário. Pode-se informá-la no cabeçalho e pelo botão Veículos. Uma vez informada, a rotina busca o peso e o volume máximo que está no cadastro da transportadora e mostra no cabeçalho da tela. A rotina também verifica se a capacidade de peso e volume da transportadora atendem ao peso e volume total da carga. Caso não atenda será exibida uma mensagem de aviso e permitirá ao usuário, selecionar outra transportadora, cancelar o processo ou continuar com a mesma transportadora.

Transp/Motorista

Código da transportadora e motorista que farão parte da carga.

Transp redespacho

Código da transportadora de redespacho para a carga.

Crit.Disp.p/fat

Código do critério de formação da quantidade disponível em estoque. Ao acessar a tela, trará para o campo o padrão definido nos parâmetros de estoques da filial. Ao clicar em "Mostrar", a rotina obedecerá o critério que o usuário informou na tela, visualizando as informações para os campos "Qtd. Disponível" e "Saldo em Estoque". Ver documentação do identificador de regras COM-135CRIFE01, para desabilitar e habilitar este campo.

Mostra só com estoque

Indicativo se deverá exibir somente itens com estoque. Se selecionado com "S" e com o identificador de regras VEN-135PPETI01 ativo, permitirá gerar carga somente se o pedido possuir estoque para todos os itens, caso contrário o pedido não será carregado para a formação da carga.

Ordenação de Produtos

Indicativo de ordenação para visualizar os itens na grade.

Analisar Crédito

Indicativo de análise de crédito do cliente no fechamento. Quando marcado e se o cliente tiver problemas de crédito será exibida mensagem questionando a continuidade ou bloqueio do processo.

Peso Máximo

Será visualizado o peso máximo que a transportadora ou o veículo poderá conter. Na seguinte situação, se nos parâmetros para vendas da filial, possuir a indicação no campo Controla Veículos igual "N", será exibida a informação do peso máximo cadastrado na transportadora, caso contrario, a informação exibida será o peso máximo cadastrado no veículo (Cadastro>Transportadora>Veículos>Cadastros).

Volume Máximo

Será visualizado o volume máximo que a transportadora ou o veículo poderá conter. Na seguinte situação, se nos parâmetros para vendas da
filial, possuir a indicação no campo Controla Veículos igual "N", será exibida a informação do volume máximo cadastrado na transportadora, caso contrario, a informação exibida será o volume máximo cadastrado no veículo (Cadastro>Transportadora>Veículos>Cadastros).

Mostrar itens de pedidos em preparação

Indicativo para considerar os itens de pedido com situação "8" (em preparação) e que a diferença entre as quantidades em aberto (E120IPD.QTDABE) e em análise (E120IPD.QTDRAE) seja maior que zero.

Observação

Recebe o conteúdo do campo observação do pedido (E120PED.OBSPED) e grava no campo observação da pré-fatura (E135PFA.OBSPFA).3

Data reserva 

Buscará a data da reserva do veículo.

## Botões

Seleção

Acesso à tela F135SCA para os filtros complementares.

Cancelar

Cancela os valores informados e retorna o valor existente antes da digitação, posicionando o cursor no primeiro campo da *grid*. Não
cancela um processamento efetuado.

Pedido/Rota

Acesso à tela F135ROT com o resumo dos pedidos de vendas selecionados, agrupados por rota.

Dist.Lote

Acesso à tela F000DLS para a distribuição de lotes para um item controlado por lote.

Veículos

Acesso à tela F135TRA pata a seleção dos veículos para o transporte da carga. Os veículos selecionados serão utilizados na formação da carga. Havendo mais de um veículo selecionado, os demais veículos serão gravados na tabela "E135PLA". Os campos "Transp./Placa" e "Transp./Motorista" serão gravados da tabela "E135PFA" com o primeiro registro selecionado na tela "F135TRA".

## Grades

Produtos

Serão visualizados todos os produtos e suas derivações disponíveis para a geração da carga. Se o mesmo produto/derivação estiver presente em múltiplos pedidos, será exibido apenas uma vez na grade, exibindo de forma acumulada as suas quantidades, pedida e faturar, e demais informações como: quantidade em estoque, peso bruto, peso líquido e volume da carga formada, permitindo que os pedidos possam ser analisados e se necessário alterar as quantidades.

Pedidos

Serão visualizados todos os pedidos ligados ao item na grade superior, permitindo os seguintes ajustes: rota, sequência de entrega, quantidade a faturar, unidade de venda, quantidade de venda e cancelamento do saldo do pedido. Ao efetuar a alteração da quantidade de venda, quando a unidade de medida de estoque e a unidade de venda forem diferentes, será exibida uma mensagem questionando ao usuário se deseja alterar também a quantidade referente a unidade de medida de estoque. Caso não seja alterada, é convertido o preço de venda de modo a ficar compatível com o preço unitário. Ao efetuar a alteração na quantidade a faturar será automaticamente atualizada a quantidade a faturar na grade superior.

Todos os itens presentes nas grade virão marcados, podendo ser desmarcados, influenciando assim na quantidade a ser faturada.

## Parâmetros Globais

| Nome | Descrição |
| --- | --- |
| GerParCar | Indicativo se as parcelas das pré-faturas serão geradas ao formar as cargas. |

## Identificadores de Regras

| Módulo | Código |
| --- | --- |
| COM | 135CGFCA01 |
| COM | 135CRIFE01 |
| COM | 135OBUSU01 |
| EST | 135BLOTE01 |
| GER | 000EUDLE01 |
| GER | 073NAOMT01 |
| GER | 073NAOMT02 |
| VEN | 000ALICM01 |
| VEN | 000ALIRF01 |
| VEN | 000COMIS01 |
| VEN | 000DLSUM01 |
| VEN | 000TNSDE01 |
| VEN | 135CASLD01 |
| VEN | 135CRECL01 |
| VEN | 135NAOTR01 |
| VEN | 135PAEST01 |
| VEN | 135PPETI01 |
| VEN | 135TNSPD01 |
| VEN | 135NAOIP01 |
| VEN | 135LOTPA01 |
| VEN | 140PERTO01 |

## Páginas relacionadas

* [Ajuda por telas](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/ajuda-telas.htm)
* [Mercado](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/menu_mercado.htm)
* [Gestão de Distribuição](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/menu_mercado_gestao_distribuicao.htm)
* [Cargas](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/fluxos/fluxograma_distribuicao_processo_cargas.htm)
* [Pendências para a Carga](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f135pen.htm)
* [F000CRT](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000crt.htm)
* [documentação](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/reforma-tributaria/rotinas-impactadas.htm)
* [COM-135CRIFE01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/com_135crife01.htm)
* [VEN-135PPETI01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_135ppeti01.htm)
* [F135SCA](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f135sca.htm)
* [F135ROT](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f135rot.htm)
* [F000DLS](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000dls.htm)
* [F135TRA](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f135tra.htm)
* [GerParCar](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#GerParCar)
* [135CGFCA01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/com_135cgfca01.htm)
* [135OBUSU01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/com_135obusu01.htm)
* [135BLOTE01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/est_135blote01.htm)
* [000EUDLE01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ger_000eudle01.htm)
* [073NAOMT01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ger_073naomt01.htm)
* [073NAOMT02](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ger_073naomt02.htm)
* [000ALICM01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_000alicm01.htm)
* [000ALIRF01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_000alirf01.htm)
* [000COMIS01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_000comis01.htm)
* [000DLSUM01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_000dlsum01.htm)
* [000TNSDE01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_000tnsde01.htm)
* [135CASLD01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_135casld01.htm)
* [135CRECL01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_135crecl01.htm)
* [135NAOTR01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_135naotr01.htm)
* [135PAEST01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_135paest01.htm)
* [135TNSPD01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_135tnspd01.htm)
* [135NAOIP01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_135naoip01.htm)
* [135LOTPA01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_135lotpa01.htm)
* [140PERTO01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_140perto01.htm)
