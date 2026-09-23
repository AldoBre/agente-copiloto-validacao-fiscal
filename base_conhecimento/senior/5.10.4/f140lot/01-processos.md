# Processos

> **Fonte:** F140LOT - Faturamento de Pedidos Agrupado — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f140lot.htm  
> **Trilha:** Ajuda por telas > Mercado > Gestão de Faturamento e Outras Saídas > Notas Fiscais de Saída > Via Pedido  
> **Telas citadas:** F001TES, F028GCP, F070FVE, F075APF, F075FCI, F075GFP, F075PFI, F075PRO, F081TCA, F140LOT  
> **Identificadores de regras:** GER-085NGRCE01, VEN-140LIBTR01

---
* Tela de exibição das notas fiscais a imprimir

É possível inserir um produto do tipo Passagem Direta na nota
fiscal de saída. Como produtos de passagem direta não possuem estoque,
não será exigida a informação do depósito, porém, o campo Depósito
poderá ser preenchido com finalidade informativa. Não serão realizadas
consistências relacionadas ao depósito, como por exemplo, saldos
disponíveis e ligações do produto.   
Somente será permitido inserir um produto de passagem direta se a
transação do item de produto não possuir integração com estoques.

Com o identificador de regras VEN-140LIBTR01
cadastrado e ativo,  o processo de geração de notas fiscais de saída não será interrompido quando houver inconsistências em um ou mais pedidos.
No fim deste processo será exibido o aviso Processamento realizado, porém houveram X pedidos com problemas e posteriormente uma lista com as informações das notas fiscais geradas e pedidos com inadequações será apresentada.

Com o identificador de regras GER-085NGRCE01 cadastrado e ativo, o sistema evita que seja alterado o indicativo de endereços de entrega de um cliente para "S - Sim". Com isso, ao realizar o fechamento de uma nota através da tela F140LOT, a rotina irá verificar o campo TemEnt do cliente. Esse campo indica se o cliente tem endereços de entrega diferentes e, se ele estiver diferente de "S", irá ignorar os outros endereços de entrega, zerando o sequencial de endereço de entrega da nota.

Observação

Este procedimento será efetuado apenas quando a opção Agrupar Pedidos estiver desmarcada, caso contrário, o funcionamento atual do sistema será mantido.

* O campo Código da FCI, na grade de Produtos, será preenchido de acordo com o informado no campo Cód. FCI da tela F075FCI, ao efetuar uma operação interestadual ou caso parâmetro Listar código da FCI em operações internas estiver definido como S.
* O percentual de ICMS, definido na estrutura de cálculo da FCI, será filtrado quando a origem da mercadoria do item for 1 (Estrangeira - Importação direta), 2 (Estrangeira - Adquirida no mercado interno), 3 (Nacional - Mercadoria ou bem com Conteúdo de Importação superior a 40%) ou 8 (Nacional - Mercadoria ou bem com Conteúdo de Importação superior a 70%).
* O coeficiente definido nas parametrizações da FCI não será mais considerado. Será utilizado o código da FCI para verificar se o seu percentual e a origem da mercadoria (definida nas parametrizações de FCI) devem ser utilizadas.

Observação

Independentemente da origem fiscal da mercadoria definida nas parametrizações da FCI, ela sempre será atribuída ao item da nota fiscal de saída, desde que exista um código de FCI e seja uma operação interestadual.

Se a nota fiscal de saída eletrônica (série com
o dispositivo autorizado igual 6 - Nota Fiscal Eletrônica) for fechada
com o indicativo presencial em branco, o fechamento do nota fiscal irá
fazer uma sugestão de valor para o campo seguindo o critério:

1. Se for uma nota fiscal de devolução (tipo 2 - Devolução) ou uma
   nota fiscal de acerto (tipo 9 - Acerto), será sugerido o indicativo
   presencial 0 - Outros.
2. Utilizar o indicativo presencial informado nas definições do cliente;
3. Se não encontrar no cadastro do cliente, irá buscar da transação da
   transação de produto, se a nota fiscal não possuir uma transação de
   produto, então será buscado da transação de serviço.
4. Se não encontrar no cadastro do cliente e nas transações, será
   utilizado o indicativo presencial informado nas definições da filial
   para as operações de vendas, tela F070FVE.

Uma nota fiscal de saída com série eletrônica (série com o dispositivo autorizado igual 6 - Nota Fiscal Eletrônica) não pode ser faturada com o indicativo presencial em branco.

Para o cálculo do ICMS Diferido, conheça o processo.

Para que não haja divergência entre o estoque no ERP e o WMS WIS ao faturar uma nota fiscal:

* Em uma nota fiscal de saída que possui itens originados de pedidos de venda, não é possível alterar a quantidade, caso os itens do pedido possuam ordem de separação;
* Em uma nota fiscal de saída que possuí mercadoria separada no WMS WIS (tanto pela geração via pedido separado ou pela separação da nota fiscal), não é possível adicionar novos itens com depósito integrado ao WMS. Isto porque, não existe envio parcial para a separação de itens.

Para gerar uma nota fiscal com 100% de desconto nos itens, a transação de estoque (F001TES) vinculada à transação de venda, deve estar configurada conforme abaixo:

* Forma Valorização Movimento: "F - Fechamento";
* Forma Valorização Movimento: "M - Movimento" e Per. Mov. Ent. sem valor?: "S- Sim".

## Guia Nacional de Recolhimento de Tributos Estaduais - GNRE

É possível gerar as informações da GNRE no momento da emissão da nota fiscal. Para mais informações acesse a documentação da emissão do GNRE.

## Exclusivo para proprietária Agronegócio

Ao gerar pedidos com parcelas especiais e condição de pagamento
parametrizada para considerar juros desde a venda (tela
F028GCP),
a data de vencimento será a de geração, e a data de vencimento
original, calculada a partir da condição de pagamento, será a data provável
do pagamento do
título.

Caso a
transação utilizada possua integração com o financeiro, esse processo
será aplicado também nos títulos gerados no contas a receber.

* As parcelas, na geração de um pedido, podem seguir as definições cadastradas na condição de pagamento (F028GCP), com os dias fixos determinados através dos campos Dia/Mês Fixo ou Dia Fixo.
* As condições de pagamento utilizadas devem estar vinculadas à tabela de preço (Tabelas de Preço x Condição de Pagamento) através da tela F081TCA.

## Controlar produtos com ICMS ST entre filiais em estados diferentes

Quando uma empresa possui duas ou mais filiais em estados diferentes e comercializa produtos com ICMS ST em um estado, enquanto em outro o produto não é controlado pelo ICMS ST, este último não pode ser considerado no Controle de Entrada e Saída; o primeiro, sim.

**Exemplo:** no estado de SC, o produto A não tem ICMS ST. No estado do RS, sim; ou seja, deve passar pelos processos de ressarcimento, restituição e complementação. Como o processo parte do produto registrado nas estruturas de Entrada e Saída, se o produto para determinada filial não estiver no Controle, ele não será apresentado na declaração para o estado. Diante disso, é necessário parametrizar a nível de filial se o produto deve ou não entrar no Controle:

Ao tratar uma nota/cupom fiscal, o sistema analisa o conteúdo do campo **Reg. entradas e saídas para controle de impostos** das telas F075PFI/F075APF, juntamente com as parametrizações das telas F075PRO/F075GFP:

* **Quando não há ligação do produto com a filial**: o sistema gera um registro no Controle de Entrada e Saída de produtos apenas se na derivação for informado **S-Sim** para o campo **Reg. entradas e saídas para controle de impostos**;
* **Quando há ligação do produto com a filial:** o sistema gera um registro no Controle de Entrada e Saída de produtos apenas se na derivação e na ligação for informado **S-Sim** para o campo **Reg. entradas e saídas para controle de impostos**;
* Caso contrário, o sistema não gera um registro no Controle de Entrada e Saída de produtos.

## Referenciar mais de uma NF de entrada para um item da NF de saída

Para saber mais sobre como funciona a referenciação de notas fiscais de entrada em processos de exportação (grupo detExport), acesse a documentação correspondente.

## Páginas relacionadas

* [Tela de exibição das notas fiscais a imprimir](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f140enl.htm)
* [VEN-140LIBTR01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_140libtr01.htm)
* [GER-085NGRCE01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ger_085ngrce01.htm)
* [processo](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/impostos-icms.htm)
* [F001TES](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f001tes.htm)
* [emissão do GNRE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/manuais_processos/mercado/gnre.htm)
* [F028GCP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f028gcp.htm)
* [F081TCA](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f081tca.htm)
* [documentação correspondente](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/referenciacao_nf_entrada_processo_exportacao.htm)
