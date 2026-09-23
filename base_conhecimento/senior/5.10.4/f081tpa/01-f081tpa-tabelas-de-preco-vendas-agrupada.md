# F081TPA - Tabelas de Preço Vendas Agrupada

> **Fonte:** F081TPA - Tabelas de Preço Vendas Agrupada — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f081tpa.htm  
> **Trilha:** Ajuda por telas > Cadastros > Mercado e Suprimentos > Tabelas de Preço  
> **Telas citadas:** E070VEN, E081ITF, E081ITP, E081LIP, E210MED, F081CLA, F081TPA  
> **Identificadores de regras:** GER-000SUGVR01

---
Ajuda por telas > Cadastros > Mercado e Suprimentos > Tabelas de Preço > Cadastro

A tela tem como objetivo realizar o cadastro das tabelas de preços de venda a serem utilizadas pela área de vendas.

## Processos

* Não será permitido cadastrar uma tabela de preço que possuir
  caracteres especiais em seu código, apresentando a mensagem "Não é
  permitido utilizar caracteres especiais", impedindo o processo.
* Pode-se agrupar preços por Produto, Agrupamento de Derivação,
  Agrupamento + Origem, Agrupamento + Família, Agrupamento de Derivação + Agrupamento de
  Vendas ou Agrupamento + Produto.
* Na grade superior aparecem os itens conforme tipo de agrupamento escolhido, informa-se o
  preço para o produto e o sistema assume o mesmo preço para todas as derivações daquele
  produto.
* Na grade inferior é possível alterar o preço de algum item (produto/derivação) que
  seja uma exceção do grupo, se o campo tipo de visualização do cabeçalho da tela
  estiver como "todos" aparecerão na grade inferior todos os itens do agrupamento, mesmo os
  que possuem preço,  desconto e outros campos com valor padrão. Se o campo estiver
  como "só exceção" então só aparecerão na grade inferior os itens que estiverem
  com algum valor diferenciado.
* Há a possibilidade de geração de itens pela pasta "Gera Itens Produto/Faixa
  Máscara" onde é possível selecionar por Família, Produto ou Faixa de Grade.
* Se informado o campo Faixa da Grade o sistema irá gerar automaticamente
  os itens para a tabela Itens por Faixa de Grade (E081ITF), que somente será visualizada nas telas que constam a
  página "Faixas de Grade" (Tabelas de Vendas, Duplicação de tabelas) caso não
  informada  a faixa, o sistema continua gerando na tabela Itens de Produto (E081ITP), que
  pode ser visualizado nos itens de produto de qualquer uma das telas de tabela de preço.
* É possível gerar um "LOG" (registro das
  operações processadas) ao alterar informações na guia "Itens de Produto". Para tanto implementado o campo Gerar Log Tab. Preço Vendas (E070VEN.LOGTPR) em
  "Cadastros > Filiais > Parâmetros por Gestão > Vendas e Faturamento". O "LOG"
  conterá as informações anteriores à alteração efetuada, referenciando o usuário, a
  data e a hora, sendo o histórico dos registros gravado na tabela Log dos Itens de Produto (E081LIP). A consulta do "LOG" pode ser realizada através da tela F081CLA.
* Ao alterar a data inicial de uma validade na tabela de preço, o sistema registra uma nova validade com a nova data informada, sem modificar a validade original nem os itens associados a ela.

## Campos

Código

Código que identifica a tabela.

Tipo de Agrupamento

Seleção do tipo de agrupamento.

Opção

Produto c/ Excl. Derivações

Ao selecioná-lo irá habilitar uma caixa de marcação na grade das derivações da
guia "Itens Produto", que servirá para selecionar as derivações que não
deverão ser incluídas na referida tabela de preços. Ao marcar uma derivação para
exclusão, automaticamente ela já estará fora da tabela de preços, não
necessitando clicar no botão Processar.

Tipo de Visualização

Seleção do tipo de visualização.

Botão Consulta

Acesso a tela de consulta de tabelas de preço.

## Guia Dados Gerais

### Campos

Descrição

Descrição que identifica a tabela.

Abreviatura

Descrição auxiliar da tabela.

Moeda

Código da moeda da tabela.

Especial Cliente

Indicativo de tabela especial para cliente. Se estiver definido como "S", a tabela em
questão só poderá ser usada pelos clientes que a tiverem configurada nas suas
definições, porém estes clientes poderão usar outras tabelas.

Aplicação

Indicativo da aplicação da tabela.

1. Vendas: utilizado nas rotinas de Mercado, por exemplo, valor do
   produto para pedidos de vendas por unidade.
2. Outros ST: utilizado em situações específicas, por exemplo, para o cálculo do ICMS Retido
   baseado em tabela de preço.
3. Cálculo por Quantidade (Venda): o cálculo dos impostos IPI, Pis e
   Cofins em função do valor-base ( quantidade/valor) para : Pedidos, Nota Fiscal
   de Venda.
4. Cálculo por Quantidade (Compras): o cálculo dos impostos IPI, Pis e
   Cofins em função do valor-base ( quantidade/valor) para : Ordens de Compras e
   Nota Fiscal de Entrada
5. Cálculo por Quantidade (Ambas):o cálculo dos impostos IPI, Pis e
   Cofins em função do valor-base ( quantidade/valor) para : Pedidos, Nota Fiscal
   de Venda e Ordens de Compras e Nota Fiscal de Entrada.

Situação

Indicativo da Situação da tabela.

Preço Médio

Indica se o Gestão Empresarial | ERP deve utilizar o preço médio
registrado para o produto/derivação na respectiva filial quando a tabela
de preço for utilizada. Essa informação está armazenada nas estruturas
de Estoques - Preço médio por filial (E210MED). Caso não exista
informação disponível nessas estruturas, o sistema utilizará o preço
médio registrado no cadastro da derivação do respectivo produto.

Cliente

Quando estiver com valor diferente de "0" (zero),
a tabela será específica para o cliente, caso contrário a tabela será genérica.
O código do cliente estará sempre disponível para edição, porém só
poderá ser alterado para outro código de cliente se não houver
movimentos de notas fiscais, pedidos ou contratos para a tabela de
preço. Caso já existam movimentos o código do cliente só poderá ser
atualizado para "0" (zero).

Integra WMW

Indica se esse registro deve ser integrado para o WMW.

Situação WMW

Indica se esse registro está ativo ou inativo para o WMW.

Observação

Campo aberto para observações, suportando até 100 caracteres.

## Guia Validade

Nesta guia cadastram-se os intervalos de datas com as validades da tabela. A pasta
"Itens Produto"  será aberta conforme o posicionamento nesta pasta.

### Campos

Inicial

Data inicial de validade. Ao alterar a data inicial de uma validade na tabela de preço, o sistema registra uma nova validade com a nova data informada, sem modificar a validade original nem os itens associados a ela.

Final

Data final de validade.

Usa Qtd.

Indicativo que define se a tabela permite o lançamento dos itens a nível de
quantidade.

**Nota**

Quando o campo Usada para ECF da guia Dados Gerais, estiver definido como "S - Sim", o sistema impede que o campo Usa Qtd. seja alterado, e aplica o valor "N" para a coluna.

% Toler. -

Percentual de tolerância a menor aceito na movimentações.

% Toler. +

Percentual de tolerância a maior aceito na movimentações.

% Desc.

Percentual de desconto a ser usado nas movimentações. É sobrescrito pelo percentual
dos itens.

% Comissão

Percentual de comissão a ser usado nas movimentações. É sobrescrito pelo
percentual dos itens.

Situação

Indicativo da situação da validade.

Observação

Campo aberto para observações, suportando até 100 caracteres.

## Guia Itens Produto

### Grade Grupo de Preço Por Produto

Lançamento dos valores dos itens de produto.

#### Campos

Produto

Código do produto.

Até Qtd

Quantidade máxima para aplicação do preço. Cada item poderá ser lançado tantas
vezes quanto necessário, sendo o campo preço base dependente deste campo, por exemplo,
até 10 unidades - R$ 100,00, até 50 unidades - R$ 90,00, até 999.999,99 - R$ 75.00.

Observação

Este campo só será exibido na grade se na pasta validades o campo Usa Qtd
estiver definido como "S - Sim".

Preço Base

Preço do item.

% Desc.

Percentual de desconto a ser usado nas movimentações. Sobrescreve o percentual da
pasta validades.

% Comissão

Percentual de comissão a ser usado nas movimentações. Sobrescreve o percentual da
pasta validades.

% Toler -

Percentual de tolerância a menor aceito na movimentações.

% Toler +

Percentual de tolerância a maior aceito na movimentações.

Situação

Indicativo da situação do item.

### Grade Exceções do Grupo Por Produto/Derivação

#### Campos

Derivação

Código da derivação do produto.

Preço Base

Preço do item.

% Desc.

Percentual de desconto a ser usado nas movimentações. Sobrescreve o percentual da
pasta validades.

% Comissão

Percentual de comissão a ser usado nas movimentações. Sobrescreve o percentual da
pasta validades.

% Toler -

Percentual de tolerância a menor aceito na movimentações.

% Toler +

Percentual de tolerância a maior aceito na movimentações.

Situação

Indicativo da situação do item.

Descrição

Descrição do item.

## Guia Gera Itens Produto/Faixa (Máscara)

Lançamento dos valores dos itens de produto automaticamente.

### Campos

Família

Código da família. Somente para família com máscara de derivação.

Faixa da Grade

Seleção da faixa da grade. Faz consistência com o campo família e somente
disponibiliza as faixas do código de máscara de derivação ligado à família.

Produto

Código do(s)  produto(s)

Agrupamento

Agrupamento definido na derivação do produto. Somente disponibilizado quando não é
utilizada a faixa de grade.

Preço Base

Preço do item.

% Comis.

Percentual de comissão a ser usado nas movimentações. Sobrescreve o percentual da
pasta validades.

% Desc.

Percentual de desconto a ser usado nas movimentações. Sobrescreve o percentual da
pasta validades.

% Toler -

Percentual de tolerância a menor aceito na movimentações.

% Toler +

Percentual de tolerância a maior aceito na movimentações.

Observação

Os campos **Consumo Teórico** e **Consumo Praticado** são utilizados no cadastro da tabela de preços e no identificador de regras GER-000SUGVR01, onde é possível sugerir valores para eles. As rotinas de cálculo e suas formas de utilização, devem ser realizada via regra atendendo às devidas customizações necessárias a cada procedimento/cenário.

## Botões

Seleção

Traz os campos conforme máscara do produto, definido na família. Somente é
habilitado se a família possuir máscara de produto.

Gerar Itens

Gera as informações da tela para a guia de "Itens Produto" (se não for usado
Faixa) ou para a guia "Faixas de Grade" se esta foi utilizada na geração (Ver
observação no topo da tela).

## Identificador de Regras

|  |  |
| --- | --- |
| GER | 081COTPV01 |
| GER | 081COITP01 |
| GER | 000SUGVR01 |
| GER | 000SUGVR02 |
| VEN | 000TABPR03 |

## Páginas relacionadas

* [Ajuda por telas](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/ajuda-telas.htm)
* [F081CLA](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f081cla.htm)
* [GER-000SUGVR01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ger_000sugvr01.htm)
* [081COTPV01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ger_081cotpv01.htm)
* [081COITP01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ger_081coitp01.htm)
* [000SUGVR02](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ger_000sugvr02.htm)
* [000TABPR03](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_000tabpr03.htm)
