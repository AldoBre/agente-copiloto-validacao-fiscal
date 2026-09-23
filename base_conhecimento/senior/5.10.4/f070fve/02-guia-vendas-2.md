# Guia Vendas 2

> **Fonte:** F070FVE - Parâmetros da Filial para Vendas — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070fve.htm  
> **Trilha:** Ajuda por telas > Cadastros > Filiais > Parâmetros por Gestão  
> **Telas citadas:** E008CEP, E059AGE, E070FIL, E073VEI, E075PRO, E700CMM, F000AGE, F001TVE, F031AIM, F059EMB, F070CFA, F070FCP, F070FVE, F075FCI, F075GFP, F075INF, F075PRO, F083ORI, F085CAD, F099UVE, F113CCA, F113REM, F115CAR, F115COE, F115COS, F115CST, F115TRF, F120DPE, F120FEM, F120GPB, F120GPC, F120GPD, F120GRA, F129PED, F129UFP, F135AEA, F135APF, F135APM, F135FCP, F135FEC, F135FET, F140DIV, F140LOT, F140PRE, F210EMB, F301BCD, F301BMD, F301SUB  
> **Identificadores de regras:** COM-000SEQOR01, VEN-000CRECL01, VEN-120ANAEP01, VEN-120CNFEC02, VEN-135ALQTD01, VEN-135INFQT01, VEN-135LIBPF01, VEN-140MNTTR01

---
Analise Crédito Bonificação

Para mais detalhes sobre a análise de crédito de bonificação, acesse a documentação completa aqui.

Analise Crédito Vendas em Dinheiro

Para mais detalhes sobre a análise de crédito de vendas em dinheiro, acesse a documentação completa aqui.

Permite Fatura acima Quantidade Pedida 

Indicativo se permite faturar uma quantidade acima da quantidade pedida no item de pedido.

Verifica Crédito ao Alterar Pedido/NF 

Indicativo se o crédito do cliente deve ser verificado na alteração de um pedido ou
nota fiscal de saída.

Utiliza Forma de Venda 

Indicativo se a filial utiliza forma de venda. Verificar documentação para Tratamento de Formas de Vendas.

Consiste Agrupamento Embalagem 

Este parâmetro tem como objetivo realizar uma consistência na rotina de formação das embalagens para verificar se o produto e/ou derivação estão ligados a algum agrupamento de embalagens. O código do agrupamento das embalagens é cadastrado na tela Tipos de embalagem (F059EMB), no campo **Agrup. Embalagem.**

## Exemplo

* O parâmetro Consiste Agrupamento Embalagem definido como ''S - Sim''
* O campo Agrup. Embalagem (F059EMB) **não** informado

Na tela de formação de embalagem (F210EMB), ao passar pelo campo **Código da embalagem**, será apresentada a mensagem: ''Esta embalagem não está ligada a nenhum agrupamento de embalagens'', devido ao fato de que no cadastro da embalagem não existe nenhum agrupamento informado no campo Agrup. Embalagem.

Ainda na tela F210EMB, ao passar pelo campo Nr. Emb da grade, o sistema vai verificar:

* O parâmetro Consiste Agrupamento Embalagem definido como ''S - Sim''
* O campo Agrup. Embalagem (F059EMB) **não** informado

Então, o sistema apresentará a seguinte mensagem: ''O tipo da embalagem interna não está ligado a nenhum agrupamento de embalagens''.

Buscar Preço/% Faturamento

Indicativo se deve ou não buscar os percentuais e preço do produto/serviço no faturamento
não respeitando o que está no pedido.

Gerar Pedidos c/ Parcelas Especiais

Indicativo se os pedidos devem ser gerados com parcelas especiais por padrão.
A rotina de duplicação de pedidos não utiliza este parâmetro, será sempre
copiado do pedido de origem.
As demais rotinas automáticas de geração de pedido (Via Pedido de Representante,
Pedido Entre Empresas, e Geração de Ordens de Compra entre Empresas) sempre
recebem N como padrão para o campo Tem Parcelas Especiais.

Tipo busca Últimos Faturamentos

Tipo de busca dos últimos faturamentos para pedidos.

Quantidade p/ Busca Últimos Faturamentos

Quantidade de notas ou meses para busca dos últimos faturamentos.

Tipo Retenção

Indicativo de como será efetuado o cálculo das retenções de impostos
(Cofins/PIS/CSLL) e define a relação com outras retenções.

Controle Valor Mín. Retenção

Indicativo de onde é feito o controle do valor mínimo de retenções de
contribuições sociais.

Ret. Automático Comp. Industrialização

Indicativo se deve ser gerado o retorno de componentes utilizados para
industrialização após a geração da nota do produto beneficiado (Tipo 5).

* S - para indicar a geração automática, esta opção só é possível se a filial
  utilizar o controle dos componentes pela estrutura do produto. Nesta caso a nota será
  emitida e fechada juntamente com a nota do produto principal (pai), sem fazer qualquer
  questionamento ou trazer mensagens ao usuário, conforme detalhado abaixo na
  documentação
* N - para indicar que não gera nota fiscal dos componentes no momento em que
  fecha a nota do produto principal. Pode ser gerada depois via tela de Retorno de
  Componentes Recebidos para industrialização, neste caso pode ser utilizado
  qualquer um dos dois tipos de controle de componentes
* P - no momento do fechamento da nota fiscal, traz uma mensagem perguntando se o usuário
  deseja gerar nota de retorno do componentes e qual o controle a utilizar. Neste caso
  haverá três opções: Gera pela estrutura de produto,   Gera pelo
  lote e Não Chamar, nas duas primeiras opções serão abertas
  automaticamente a tela de retorno de componentes, porém dependendo da escolha virá
  definido a forma de remessa dos componentes

Para mais informações sobre os Tipos de Rateio listados abaixo, acesse a página Rateio do Valor de Outras.

Tipo de Rateio Valor de Frete

Tipo de rateio do valor de frete para os itens de produto.

Tipo de Rateio Valor de Seguro

Tipo de rateio do valor de seguro para os itens de produto.

Tipo de Rateio Valor de Embalagens

Tipo de rateio do valor de embalagens para os itens de produto.

Tipo de Rateio Valor de Encargos

Tipo de rateio do valor de encargos para os itens de produto.

Tipo de Rateio Valor de Outras Despesas

Tipo de rateio do valor de outras despesas para os itens de produto.

Tipo de Rateio Valor de Arredondamento

Tipo de rateio do valor de arredondamento para os itens de produto.

Tipo de Rateio Valor de Frete de Importação

Tipo de rateio do valor de frete para os itens de produto importação

Tipo de Rateio Valor de Seguro de Importação

Tipo de rateio do valor de seguro para os itens de produto importação

Tipo de Rat Valor de Outras de Importação

Tipo de rateio do valor de outras despesas para os itens de produto importação.

Tipo de Rateio Valor de Frete Destacado 

Tipo de rateio do valor de frete destacado para os itens de produto. As seguintes opções estão disponíveis para os campos de tipo de rateio:

* " V - Valor Líquido": efetua o rateio do valor pelo
  valor líquido do item de produto
* " B - Valor Bruto": efetua o rateio do valor pelo valor
  bruto do item de produto (não considera descontos, impostos e acréscimos)
* " P - Peso": Efetua o rateio do valor pelo peso do item
  de produto
* " Q - Quantidade": Efetua o rateio do valor pela
  quantidade do item de produto

Considera Ped. Abertos Análise Crédito Pedido 

Indicativo se considera os pedidos em aberto para análise de crédito do pedido.

Considera Ped. Abertos Análise Crédito NF 

Indicativo se considera os pedidos em aberto para análise de crédito da nota fiscal.

Abate Previsão Fechamento Pedido 

Indicativo se deve ser abatido o pedido de previsão no fechamento dos pedidos normais. Este campo deverá estar como S (sim) e o campo correspondente em Cadastros > Produtos e Serviços > Origens > Cadastro (F083ORI) também deverá estar como S (sim) para haver o abatimento do pedido normal junto ao pedido de previsão. Confira o processo de Geração de Geração de Pedidos de Previsão para Plano Produção.

Bloqueio Pedido por Área

Indicativo se deve ser feito bloqueio de pedido por área. Para mais informações acesse a documentação acerca da Influência dos Campos da Filial do Usuário na liberação do Pedido por Área.

Controla Descontos 1, 2, 3, 4 e 5 

Indicativo se o controle dos descontos 1, 2, 3, 4 e 5 dos pedidos, pré-faturas e notas
fiscais é feito por item ou por dados gerais. Nas telas de pedidos, a informação dos campos a nível de item (cada item receber um percentual diferente de desconto 1, 2, 3, 4, e 5) só é permitido para pedidos gerados através da tela F120GRA, onde os campos estarão disponíveis nos itens quando o parâmetro estiver com o valor "I - Itens". Nas demais telas de pedidos, todos os itens irão receber o mesmo desconto 1, 2, 3, 4, e 5 informado nos dados gerais.

* "D - Dados Gerais": descontos atribuídos para todos os itens do pedido, proporcionalmente
* "I - Itens": define o desconto no item; cada item poderá ter até 5 percentuais diferentes de descontos

**Observação**

Após incluir valores em alguns dos campos de percentuais de desconto nas telas de Valores das telas de pedido e clicar em processar, o ERP validará se o valor de desconto deverá constar apenas nos dados gerais ou se deverá ser controlado a nível de itens por meio do campo Controla Descontos 1, 2, 3, 4, 5 na tela Parâmetros da Filial para Vendas (F070FVE).

Caso um pedido tenha sido criado com desconto controlado a nível de itens, ao duplicar o pedido na tela Duplicação de Pedidos (F120DPE), o desconto sempre será transferido do pedido base para o pedido duplicado, independente da existência de desconto nos dados gerais.

Quando o ERP está configurado para controlar desconto por itens, as telas de pedido permitem optar por aplicar ou não esse desconto nos itens. Uma vez que esse desconto tenha sido aplicado, ele não pode ser removido diretamente pela grade de itens, pois o ERP não disponibiliza esses campos para edição. A única exceção é a tela Entrada de Pedidos via Grade de Produtos - Pedido de Reposição (F120GRA), onde os campos estão disponíveis.

Para remover o desconto dos itens, é possível seguindo as etapas descritas abaixo:

1) Atribuir um percentual de desconto diferente nos dados gerais e indicar ao ERP para aplicá-lo aos itens na mensagem referente a esse controle;

2) Atribuir o percentual zerado aos dados gerais e também indicar ao ERP para aplicá-lo aos itens na mensagem referente a esse controle.

Embora o ERP não permita manipular ou visualizar os percentuais de desconto 1, 2, 3, 4 e 5 na grade de itens, esses valores estão presentes no botão Cálculos, localizado no rodapé das telas de pedido.

Analisa/Gera Embalagens Fechamento Pedido 

Indica a geração de embalagens no fechamento do pedido por grade, aproveitando o estoque de vários depósitos. Também afeta o indicativo de reserva de estoque e quantidade a produzir do pedido. Ao configurá-lo igual a "S - Sim", sugerimos avaliar a necessidade de utilização do identificador de regra VEN-120ANAEP01 que indica se um pedido irá analisar embalagens ou não. A ausência desse identificador indica ao sistema que a análise e geração de embalagens não deve ocorrer e com isso, a reserva de estoque será atualizada para "N - Não" e a quantidade a produzir não será atribuída ao item de pedido.

**Observação**

Após o fechamento do pedido na tela F120GPD, a mensagem "Deseja efetuar a formação de embalagens do pedido?" é apresentada com o intuito de possibilitar a geração das embalagens do pedido de forma manual ou automática através botão Gerar Emb. da tela F120FEM. Ao optar por "N - Não", o valor do campo Reserva será mantido;

Na tela F129PED essa mensagem não é apresentada. Desta forma, o valor do campo ficará igual a "N - Não".

Caso queira apenas abrir a tela de formação de embalagens após o fechamento do pedido, sugerimos utilizar o identificador VEN-120CNFEC02 com a seguinte regra:

## Regra

```
DEFINIR ALFA VSTelaOrigem;  
DEFINIR ALFA VSInteracao;  
DEFINIR ALFA aux_alfa;  
DEFINIR ALFA aRetorno;  
DEFINIR NUMERO nRetorno;

/* desconsidera a tela de duplicação de pedidos e web services / sid */

SE ((VSTelaOrigem <> "F120DPE") E (VSInteracao = "INTERATIVO")) {

nRetorno = mensagem(retorna, "Deseja gerar as embalagens para o pedido? [&Sim, &Não]");

SE (nRetorno = 0){

IntParaAlfa(e120ped.NumPed, aux_alfa);  
AbrirTelaSistema("F120FEM", aux_alfa, nRetorno);

/* AbrirTelaSistema  
0: Tela foi aberta com sucesso.  
-1: Não foi possível abrir a tela.  
*/

SE (nRetorno <> 0)  
{ mensagem(erro, "Não foi possível abrir automaticamente a tela de geração de embalagens para o pedido (F120FEM). A operação deve ser feita manualmente."); }

}

}

x = y;
```

Altera Preço Unit. em Conversões

Indicativo se deve ajustar o preço unitário nas conversões entre
quantidades nas unidades de medida de venda e de estoque
nos itens de produto do pedido e nota fiscal de saída.
O objetivo deste parâmetro é ajustar o preço unitário quando houver alterações
nas quantidades das unidades de medida de estoque e de venda, sem converter,
quando estas unidades de medida forem diferentes, ao invés de ajustar o preço de
venda nessas conversões.  

O ajuste é feito quando não há conversões entre as unidades de medidas, ou seja,
quando se altera a quantidade na unidade de medida de venda e não se deseja
alterar a quantidade na unidade de medida de estoque do produto e vice-versa.
Para manter o valor bruto (preço x quantidade) igual nas duas unidades de
medida, é feito um ajuste no preço de uma das unidades.
Quando não utilizado, o padrão do sistema é
ajustar o preço de venda. Quando o parâmetro está ativo, o preço de venda é
ajustado.

Controla Veículos

Quando este parâmetro estiver definido igual a "S - Sim", o sistema irá habilitar o recurso de pesquisa no campo Placa da tela F140DIV referente ao veículo de transporte, apresentando apenas as placas ligadas a esta.

**Observação**

Com este parâmetro ativo, o sistema começa a consistir de forma mais rígida nos dados referentes aos veículos de inúmeros rotinas dentro do sistema, verificando as placas dos veículos, os motoristas cadastrados para o veículo e também as pesagens.

## Exemplo:

No momento que o sistema solicita que seja informada uma placa, esta deve estar cadastrada na tabela Cadastros - Transportadoras - Veículos (E073VEI). Se não existir registro da placa informada, o sistema indicará que não é uma placa válida e será apresentado erro até o momento que o usuário insira uma placa válida.

O sistema também passa a controlar Pesos e Volumes máximos para o veículo. Além disso, será consistido se os motoristas possuem ligações aos veículos informados para o transporte.

Em resumo o sistema passa a ter um maior controle na rotina de transporte, não deixando que nenhum valor fictício seja utilizado. Todos os valores que serão utilizados devem estar cadastrados corretamente em suas respectivas tabelas.

Controla Reserva Veículos

Indicativo se a filial utiliza reserva de veículos para a formação de cargas.
Onde estarão disponíveis as seguintes opções: N
- não utiliza reserva de veículo, S - reserva o veículo para a data e rota,
sendo possível reservá-lo para a mesma data e rota diferente e
D - reserva o veículo apenas para a data, independente da rota.

Reajusta Preços Contrato Individual

Indicativo se o reajuste dos preços dos contratos de venda deve ser feito
individualmente, cada um com sua data e percentual de reajuste.

Usa Tabela Preço de Frete

Indicativo se usa tabela de preço de frete para as rotinas de pedidos, pré-faturas e
notas fiscais. É importante lembrar que agora além do cliente ter em seu cadastro
informado o campo Tabela Preço Frete ou o campo Transportadora Padrão e esta
transportadora estar informada em alguma tabela de preço de frete, este
parâmetro da filial também deve estar com valor igual a S (sim).

Rateia frete em itens isentos de ICMS 

Indica se o valor do frete deve ser rateado para itens isentos de ICMS no pedido, pré-fatura e nota fiscal de saída. Por padrão, este campo será preenchido com S (Sim), indicando que o rateio deve ser realizado. Quando o parâmetro for alterado para N (Não), o valor do frete apenas será rateado para os itens que possuírem valor de ICMS.   
Caso todos os itens do pedido, pré-fatura ou nota fiscal de saída sejam isentos de ICMS, será apresentada uma mensagem informando ao usuário que não foi possível realizar o rateio do valor do frete.

Não buscar desconto importação pedido 

Indica para não buscar o percentual de desconto da tabela de preço quando for feita a importação de itens de pedidos.

Dt. Cheque maior Vct. Título

Indicativo se consiste a data do cheque com o vencimento do título. Este parâmetro é usado em Mercado > Gestão de Distribuição > Acertos, se este
parâmetro estiver definido com S, o sistema não permitirá informar a data de
vencimento do cheque maior que a data de vencimento do título.

Gera Itens Por Lote

Permite que possa determinar se gera lotes por item na nota fiscal de saída.

**Importante**

Este parâmetro só tem funcionalidade nas telas F135APM, F135FCP, F135AEA e F140PRE.

Comp. Tit. Dev.

Indicativo se faz compensação de títulos na devolução.

Considera Pré-Faturas em aberto p/ análise crédito

Indicativo se são consideradas as pré-faturas em aberto na análise de crédito.

Desc. Ant. Hist.

Indicativo que busca os dados do desconto de antecipação do histórico do cliente na
geração de títulos a partir de notas fiscais. Se definido como S - Sim, serão carregados
os valores dos campos Desconto Antecipação, Percentual de Desconto e Tolerância
Desconto. Ao criar novas filiais, este campo deverá ser preenchido com N - Não.   
Para habilitar a edição deste campo, o parâmetro Permite informar descontos Antecipação deve estar igual a S - Sim na tela F099UVE (Cadastros > Usuários > Parâmetros por Gestão > Vendas e Faturamento).

Desc Pon. Hist.

Indicativo que busca os dados do desconto de antecipação do histórico
do cliente na geração de títulos a partir de notas fiscais.
Se definido como S - Sim a filial irá utilizar de pontualidade nos pedidos e notas de saída.
Ao criar novas filiais, este campo deverá ser preenchido com N - Não.   
Para habilitar a edição deste campo, o parâmetro Permite informar descontos Pontualidade deve estar igual a S - Sim na tela F099UVE (Cadastros > Usuários > Parâmetros por Gestão > Vendas e Faturamento).

Observação

O campo Desconto de Pontualidade é de uso exclusivo do Agronegócio.

Analise crédito para o grupo de clientes

Indicativo se efetua a análise de crédito para o grupo de clientes. Para saber mais sobre a análise de crédito no pedido, acesse a documentação correspondente.

Observação

Para realizar um bloqueio, primeiramente é realizada uma verificação nos dados do cliente, tais como: Atraso Títulos, Limite de crédito do cliente, Pgtos.Cartório, etc. Depois de realizada a verificação dos dados, serão feitas outras verificações utilizando uma rotina que trata o bloqueio pela análise do grupo de clientes. Caso seja encontrada alguma irregularidade durante as verificações, o bloqueio será efetuado. Porém, o identificador de regras VEN-000CRECL01 é executado antes da rotina de análise de grupo de clientes, sendo possível alterar a variável que é utilizada para o bloqueio.

Por exemplo: se na regra a variável VSMOTIVO for igual a Limite de crédito do cliente, a variável VSBLOQUE será registrada como **N - Não**, o que faz com que o procedimento desconsidere esse tratamento do cliente.

Dias atraso médio grupo cliente pedidos

Quantidade máxima de dias de atraso médio aceita na entrada de pedido para o grupo de clientes.

Dias maior atraso grupo cliente pedidos

Quantidade máxima de dias de maior atraso aceita na entrada de pedidos
para o grupo de clientes

Quantidade pagamento cartório grupo cliente pedidos

Quantidade máxima de pagamentos em cartório aceita na entrada de pedidos para o grupo
de clientes.

Quantidade título atraso grupo cliente pedidos

Quantidade máxima de títulos em atraso aceita na entrada de pedidos para o grupo de
clientes.

Observação

O valor "9999" é utilizado pelo sistema como indicativo que a validação não deve ser feita.

Dias atraso título grupo cliente pedidos

Quantidade de dias de atraso de títulos para entrada de pedido para o grupo de
clientes.

Observação

O valor "9999" é utilizado pelo sistema como indicativo que a validação não deve ser feita.

Limite crédito atraso grupo cliente pedidos

Indicativo se aceita pedido com estouro de limite de crédito do grupo de clientes.

Dias atraso médio grupo cliente fatura

Quantidade máxima de dias de atraso médio aceita para o faturamento para o grupo de
clientes.

Dias maior atraso grupo cliente fatura

Quantidade máxima de dias de maior atraso aceita para o faturamento para o grupo de
clientes.

Quantidade pagamento cartório grupo cliente fatura

Quantidade máxima de pagamentos em cartório aceita para o faturamento para o grupo de
clientes.

Quantidade título atraso grupo cliente fatura

Quantidade máxima de títulos em atraso aceita para faturamento para o grupo de
clientes.  
O valor "9999" é utilizado pelo sistema como indicativo que a validação não deve ser feita.

Dias atraso título grupo cliente fatura

Quantidade de dias de atraso de títulos aceito para o faturamento para o grupo de
clientes.  
O valor "9999" é utilizado pelo sistema como indicativo que a validação não deve ser feita.

Limite crédito grupo cliente fatura

Indicativo se aceita ou não faturamento com estouro de limite de crédito do grupos de
clientes.

Transação Padrão Entrada Fatura

Transações padrão para entrada de faturas de vendas. O valor deste campo é sugerido nas telas Baixa por Substituição/Negociação do Contas a Receber (F301SUB), Baixa por Recebimento de Cheque/Diversos do Contas a Receber (F301BCD) e Baixa por Motivos Diversos do Contas a Receber (F301BMD).

Limite da Quantidade de Protestos do Pedido

Quantidade de protestos aceita como limite de crédito do cliente no pedido.

Limite Valor Protestos no Pedido

Valor limite de protestos para crédito do cliente no pedido.

Limite da Quantidade de Protestos da Nota Fiscal

Quantidade de protestos aceita como limite de crédito do cliente na nota fiscal.

Limite Valor Protestos na Nota Fiscal

Valor limite de protestos para crédito do cliente na nota fiscal.

Agrupa Pedidos Cond.Pagto Dif. 

Indicativo se agrupa em notas fiscais pedidos com condições de pagamento
diferentes. Este parâmetro somente é considerado no faturamento agrupado de pedidos (F140LOT)

Transação título crédito Pedido

Transação padrão para geração de títulos sobre o valor de crédito do pedido.

Busca tabela preço por data emissão

Indicativo de que nos pedidos de venda será utilizada a data de emissão do pedido para busca de preço na tabela de
preço, e não a data de entrega do item, tanto para itens de serviço como para itens de
produto. Também, caso o parâmetro seja S, será solicitado o recálculo do
pedido caso seja alterada a data de emissão do mesmo. Por padrão, o valor do parâmetro
é N ou vazio.

Gerar LOG Tab. Preço Vendas

Indicativo se deverá gerar um LOG das alterações efetuadas nas tabelas de
preços de vendas. Se o sistema estiver em execução apontando para uma proprietária liberada
para o ERP Varejo, a configuração deste campo não será considerada, ou
seja, sempre será gerado o LOG.

Análise Pedido Engenharia

Forma de análise do pedido pela engenharia.

Definição Cliente x Marca com sugestão

Indica que as definições informadas na
ligação Cliente x Marca são apenas sugestões, ou seja, podem ser
alteradas, caso conter N não será permitido alterar as sugestões, sendo
visualizada mensagem <campo> foi sugerida da ligação do cliente com a
marca e não pode ser alterada, ao tentar efetuar uma alteração dos campos da
ligação. Se o campo Representante na tabela de usuários tiver zerado o tratamento
deste campo não será efetuado.

Utiliza lista de preços

Indica se a filial utiliza lista de preços, neste caso, as consistências serão
feitas normalmente, senão, desabilita o campo.

Formação de embalagens automática nas PFA

O objetivo é indicar se o sistema deve executar a formação de embalagem
automaticamente com base na estrutura de agrupamento de embalagens (E059AGE).
Para os usuários que fazem formação de embalagem manual, este campo deve estar
com valor igual N - Não. Quando parametrizado com a opção S - Sim, o sistema fará a herança das embalagens do pedido para a pré-fatura. Este campo terá efeito nas telas de geração de
pré-faturas manual e automática.

Últimos faturamentos por Filiais

Será o indicativo de que a busca pode ou não
acontecer fora da filial ativa. Parâmetro usado na tela
F129UFP.

Filiais para últimos faturamentos

É uma abrangência onde o usuário deve informar em quais filias a busca dos
últimos faturamentos deve ocorrer. Parâmetro usado na tela
F129UFP.

Quando informada mais de uma filial, utilize a vírgula para separar os códigos. Por exemplo, 1,2,3.

Balança de Entrada Padrão

Informação do código da balança de entrada que será usado nas telas de
controle de entrada e saída.

Balança de Saída Padrão

Informação do código da balança de saída que será usado nas telas de controle
de entrada e saída.

Buscar alores no Recálculo do Pedido após Fechado

Indicar se o usuário deve ser questionado sobre o recálculo do
pedido com busca de preço/percentuais num pedido já fechado em que as alterações efetuadas afetam os valores do
pedido. Este parâmetro substituirá o parâmetro global PedBprFec, que possuía a mesma
funcionalidade.

Obriga sequência de entrega do cliente

Indicar se as rotinas do sistema, obrigam ao usuário
informar a sequência de entrega do cliente em uma nota fiscal, pré-fatura ou
pedido.

Obriga sequência de cobrança do cliente

Indicar se as rotinas do sistema, obrigam ao usuário informar a sequência de cobrança do
cliente na nota fiscal, pré-fatura e no pedido.

Conferir carga antes do fechamento

Esse campo indica que a carga somente será fechada após conferência. O campo Conferir Qtd. nas Cargas das telas de Cadastro de Produtos (F075PRO) e Cadastro de Produtos Agrupado (F075GFP) ficará habilitado quando esse campo estiver igual a "S - Sim". Quando estiver com valor igual a "N - Não", o campo permanecerá com o valor já informado e apenas em modo de leitura.

Aceita Depósito de Outras Filiais para Ped/PFA/NF

Indicar se podem ser selecionados depósitos de outras filiais além
da ativa. Este campo será considerado nas seguintes rotinas: cadastro de origens, pedidos, pré-faturas e
notas fiscais da gestão de vendas.

Anal. Crédito Vendas em Dinheiro

Indicativo de liberação de vendas a vista com forma de pagamento em
dinheiro para clientes com problemas de crédito. O parâmetro liberará a operação
tanto para pedidos como para notas fiscais.

Cálculo Manual de Impostos N.F.S.

Este campo é utilizado apenas em situações onde torna-se necessária a alteração manual dos valores de impostos calculados pelo sistema. Em vias normais, apenas a alíquota dos impostos pode ser alterada, sendo que a base de cálculo e o valor do imposto serão calculados automaticamente. Com este parâmetro definido como S, é possível informar um valor de impostos independente da base de cálculo ou da alíquota, sendo que o sistema não fará nenhuma alteração. Esta funcionalidade é aplicável em situações onde a nota fiscal de saída já existe fisicamente e precisa ser lançada no ERP mantendo a fidelidade dos valores.

Código Tabela Preço Base

Código da tabela de preço a ser utilizada no registro de medicamentos para NF-e e EFD.

Obriga Contrato Origem para Contrato Adicional

Indicar se o a filial obriga que seja informado o contrato de origem para contratos adicionais. Os valores
permitidos para este campo são:  
S (sim) ou (branco) - obriga que seja informado o número do contrato de
origem, N (não) - não obriga que seja informado o número do contrato de origem e
P (perguntar) - apresenta mensagem quando o contrato de origem não foi
informado, questionando se deseja continuar sem informar.

Buscar valores no recálculo do pedido

Indicar se o usuário deve ser questionado sobre o recálculo do pedido com busca de preço/percentuais num
pedido fechado em alterações efetuadas que afetam os valores do pedido.Este parâmetro substitui o parâmetro global
PedBprFec.

Aplicar Data de entrada do pedido nos itens

Indicar se deverá alterar a data de previsão de entrega nos itens caso seja alterada a data de previsão do pedido.

Controla Reajuste Contrato

Indicativo se o controle de reajuste de contratos é pelos dados gerais ou pelos itens.

Controla Faturamento Contrato

Indicativo se o controle de data de início de faturamento de contratos é pelos dados gerais ou pelos itens.

Busca valores no recálculo das N.F.S.

Parâmetro para quando estiver gerando nota fiscal de saída ao utilizar o botão Recalcular nas rotinas de
geração da nota, seja verificado o critério atribuído. Podendo ser informado:

* P (perguntar) será visualizado uma mensagem ao mandar recalcular se deseja ou
  não buscar os valores
* S (sim), indica que a nota fiscal deve buscar os percentuais atualizados quando for recalculada. Nesse caso, a transação força que a nota fiscal seja recalculada e por isso busca os percentuais atualizados
* N (não), não será buscado os valores ao mandar recalcular a nota fiscal

% Máximo Embalagens PFA

Determinará qual a quantidade em percentual a mais que será permitido na
embalagem, caso este valor seja zero, mesmo com as demais configurações
definidas para permitir o sistema irá permitir informar uma quantidade maior na
embalagem em relação a pré-fatura.
Para quando os identificadores de regra VEN-135ALQTD01 e VEN-135LIBPF01
estiverem ativos e na regra do identificador VEN-135LIBPF01 a variável VSLibPfa
estiver com valor = S, permitirá informar embalagens com quantidade total
maior do que foi definido na pré-fatura, atualizando a pré-fatura, esta
funcionalidade é valida para as telas F135FEC e F135FET.  

Se o identificador de regra VEN-135LIBPF01 estiver inativo ou a variável VSLibPfa
estiver com o valor igual N a pré-fatura será atualizada, mesmo que seja
informada uma quantidade maior ou menor na embalagem.
Exemplo de como o sistema permite informar uma quantidade maior para a embalagem
em relação a quantidade da pré-fatura.
Se a pré-fatura tiver uma quantidade 10 Kg, no parâmetro no cadastro de filial
vendas estiver definido 2%, isto significa que a quantidade total embalada pode
ter até 10,2 Kg e este novo valor vai ser atribuído a pré-fatura.  

Caso seja feita uma leitura de 5 Kg e outra leitura de 5 Kg mesmo tendo ainda
200 gramas como tolerância o sistema não irá permitir fazer outra leitura, isso
porque a quantidade total da pré-futura já foi lida, o que o sistema permite
fazer é o seguinte, ler um item com 5 Kg outro item com 5,1 Kg neste caso o
produto com 5,1 Kg pode ser lido porque a soma de todos os produtos embalados
está dentro do peso informado na pré-fatura mais o peso de tolerância. Para tela F135FEC permitir informar a quantidade o identificador de regra
VEN-135INFQT01 deve estar ativo.

Quando alterado cliente altera tabela de preço

Este parâmetro será utilizado nas telas F120GPD (pedidos agrupado) e
F120GPC (avaliação de produtos) somente nas guias de Produtos. Ao efetuar
a troca do código do cliente no pedido, será levado ou não (conforme
parametrização) para os itens do pedido a tabela de preço padrão cadastrada nas
definições do novo cliente informado.  

Observar que não efetuará a troca do cliente e a tabela de preço no pedido,
quando o cliente não possuir uma tabela de preço padrão cadastrada nas
definições ou a nova tabela de preço a ser atribuída não possuir um produto
cadastrado em relação com a tabela que estava anteriormente no pedido. Será
visualizado mensagem nas rotinas de pedidos informando o ocorrido, voltando o
código do cliente anterior e respectivamente a tabela de preço informada nas
definições do cliente.
Este parâmetro poderá possuir os seguintes valores:

* S = sim , quando estiver com este valor a tabela de preço na guia de
  produtos vai ser trocada sem ser feito nenhum questionamento
* N ou = não ou branco, quando estiver com este valor a tabela de preço
  não vai ser trocada e não vai ser feito nenhum questionamento, seguindo o padrão
  do sistema
* P = perguntar, quando estiver com este valor vai ser exibida uma mensagem e
  desta forma o usuário poderá escolher se quer que altere a tabela de preço dos
  itens do produto ou não

Observação

A alteração do novo parâmetro somente será atualizada no sistema quando
sair do sistema ou quando for feita a troca do usuário, desta forma não basta
sair da tela e entrar novamente para que o novo valor do parâmetro seja
atualizado para o sistema.  

Para que seja executado nas rotinas de pedidos deve sempre ser feita a busca de
valores ou o recalculo conforme o usuário definir, para isto também no cadastro
de filial vendas o parâmetro Buscar valores no recalculo do pedido deve estar
com o valor igual a perguntar = “P” ou igual a sim = “S” que neste caso vai
fazer a busca dos valores automaticamente.

Parcelas com dias especiais

Tem a finalidade de considerar os dias especiais no vencimento das parcelas
das notas fiscais de saída geradas por parcelas especiais de pedidos informadas
em dias, ou seja sem data de vencimento pré-definida, quando definido como S
(sim). Estes dias especiais serão herdados primeiramente dos dias especiais das
definições do cliente, caso existam, do contrário serão considerados os dias
especiais da condição de pagamento.

Alterar Parcelas Especiais com Pedido Fechado

Tem o objetivo de permitir alterar as parcelas especiais do pedido fechado
(situação 1 aberto total) quando o parâmetro estiver com valor igual a S(sim).

Agrupar pré-fatura já embalada

Indicativo se a tela F135APF deverá
considerar pré-faturas já embaladas para a rotina de agrupamento.

CEP ISS

Indicativo se o código da RAIS deverá ser obtido a partir da filial ativa
(E070FIL.CODRAI) ou do cadastro do CEP ligado ao cliente (E008CEP.CODRAI). Este
recurso estará disponível para as telas que geram notas fiscais de saída.

**Manter ICMS do pedido no Faturamento**

Possui as seguintes opções:

* **Sim:** Mantém a alíquota de ICMS do item do pedido independentemente da natureza da operação (transação) da nota fiscal de saída ou da pré-fatura, calculando ICMS ou não. Contudo, os parâmetros para a formação da base de cálculo continuarão sendo buscados a partir da transação da nota fiscal de saída. É utilizada quando o pedido tributou determinado imposto e, em seguida, a parametrização foi alterada para não tributar mais esse imposto. Assim, é possível manter a tributação aplicada ao pedido antes da alteração.

  Observação

  Há o parâmetro global IcmDifFat que indica quais ICMS o parâmetro da filial Manter ICMS do Pedido no Faturamento mantém no faturamento (ICMS Normale/ou ICMS Diferido).
* **Não:** não mantém a alíquota de ICMS do item do pedido, herda a alíquota e calcula o imposto de acordo com a natureza de operação (transação) da nota fiscal de saída ou pré-fatura. Também não sugerirá o código de redução de imposto do item do pedido para o item da nota fiscal de saída ou pré-fatura. É utilizada quando o pedido tributou determinado imposto e em seguida a parametrização foi alterada para não tributar mais esse imposto. Assim, é possível atualizar o cálculo do imposto no momento do faturamento
* **Recalcular:** não mantém a alíquota de ICMS do item do pedido e calcula o imposto de acordo com a natureza de operação (transação) da nota fiscal de saída ou pré-fatura, buscando a alíquota atualizada. Também não sugerirá o código de redução de imposto do item do pedido para o item da nota fiscal de saída ou pré-fatura. É utilizada quando o pedido não tributou determinado imposto, porém a operação de venda da nota fiscal de saída indica que deve ocorrer tributação. Assim, é possível atualizar o cálculo do imposto no momento do faturamento.

Para saber mais sobre o campo Manter ICMS do pedido no Faturamento, clique aqui.

Para manter IPI, PIS Retido, COFINS Retido, CSLL, IRRF, PIS Faturamento e COFINS Faturamento e Outras Retenções do pedido no Faturamento 

Possui as seguintes opções:

Sim: mantém a alíquota do item do pedido, independentemente da natureza de operação (transação) da nota fiscal de saída ou pré-fatura, calculando ou não. Contudo, os parâmetros para formação da base de cálculo continuarão sendo buscados da transação da nota fiscal de saída. É utilizada quando o pedido tributou determinado imposto e, em seguida, a parametrização foi alterada para não tributar mais esse imposto. Assim, é possível manter a tributação utilizada no pedido antes da alteração.

Não: não mantém a alíquota do item do pedido, herda a alíquota e calcula o imposto de acordo com a natureza de operação (transação) da nota fiscal de saída ou pré-fatura. É utilizada quando o pedido tributou determinado imposto e, em seguida, a parametrização foi alterada para não tributar mais esse imposto. Assim, é possível atualizar o cálculo do imposto no momento do faturamento.

Recalcular: não mantém a alíquota do item do pedido e calcula o imposto de acordo com a natureza de operação (transação) da nota fiscal de saída ou pré-fatura, buscando a alíquota atualizada. É utilizada quando o pedido não tributou determinado imposto, contudo a operação de venda da nota fiscal de saída indica que deve ocorrer tributação. Assim, é possível atualizar o cálculo do imposto no momento do faturamento.

**Observação**

Por meio do identificador de regras VEN-140MNTTR01 é possível alterar o valor desses parâmetros.

Pes. deve ser realizada na U.M. estoque produto 

Indicativo se a pesagens rotinas de balança deve ser efetuada na unidade de medida de estoque do produto (E075PRO.UNIMED), em vez da terceira unidade de medida do produto (E075PRO.UNIME3).

**Importante**

Esse parâmetro impacta no cálculo das quantidades de pesagem informadas, onde:

* Ao configurar para "S", somente considera a unidade de medida de estoque, sem fazer conversões
* Ao configurar para “N”, efetua a conversão das quantidades entre a “Unidade Medida (Estoque)” e “3ª Unidade Medida”, informadas no cadastro do produto

Para não haver diferenças de comportamento entre as rotinas, é aconselhável que esse parâmetro seja configurado de forma semelhante ao parâmetro de mesmo nome localizado no cadastro de filiais/compras na tela de Parâmetros da Filial para Compras (F070FCP).

Rotinas onde o parâmetro atua: F115CST, F115COS, F115CAR, F115COE e F115TRF.

Gerar requisição ao fechar a carga

Indicativo se deverá gerar requisições dos componentes de produtos produzidos
(registros na tabela E700CMM).

Buscar Primeiro Número Livre do Pedido

Indicativo se deverá procurar o primeiro número livre na geração de
pedidos, quando a numeração não é sequencial.

**Observação**

Quando esse parâmetro está definido como "S - Sim", pode haver impactos no desempenho da busca do número do pedido em bases com grande volume de registros.

Para bases com grande volume de registros, caso ocorra problema de desempenho após ativação do parâmetro, pode-se ativar o uso do identificador de regras COM-000SEQOR01. Para maiores detalhes acesse a documentação através do link.

Controla Entregas

Indicativo se a filial tem controle de entrega de mercadorias ou não.

Consid. os produtos inat. pelo inventário no pedido

Indica se o pedido deve considerar, ou não, os produtos com estoque
inativado pelo inventário.

Exige conferência volumes?

Indica se a filial exige a conferência de volumes no fechamento de uma carga.
Quando o campo estiver com o valor S (Sim), a tela para a leitura de
conferência e código de barras por volume é habilitada.

Dias para Cálculo Categoria

 Indica a quantidade de dias para cálculo.

Pontuação Fixa Clientes

Indica a pontuação do cliente.

Valor Histórico Compras

Indica o valor do histórico de compras.

Categoria Crédito Novo Cliente

Indica a categoria do novo cliente.

Quantidade Envios Pedido Análise

Indica a quantidade de envios para a análise do pedido.

Tipo Escore para Categoria

* Média ponderada
* Média ponderada apenas atrasos mais 30 dias
* Média ponderada considerando antecipações

Limite de Crédito

C - Calculado; D - Digitado.

Dias Validade Documento Cliente

Indica a quantidade de dias.

Classificação Análise Crédito

Indica a classificação da filial para efetuar a análise de crédito. Esse campo é preenchido automaticamente através da rotina de classificação da filial para análise de crédito (conforme rotina executada na tela F070CFA).

Controla Avalistas

 Indicativo se a filial de vendas permite o controle de avalistas.

Controla Avalistas Pedido

Indicativo se o pedido de venda deve ou não possuir avalistas.

Controla Avalistas Nota Fiscal

Indicativo se a nota fiscal de saída deve ou não possuir avalistas.

Controla Avalistas Contrato

Indicativo se o contrato de venda deve ou não possuir avalistas

Filial Calcula FCI 

Este parâmetro define se a filial irá efetuar o cálculo dos valores da
FCI (Ficha de Conteúdo de Importação) para os produtos produzidos e
também preparar o valor de importação dos produtos comprados.

Faturar sem FCI apurado

Este campo define se a filial fatura ou não produtos sem ter o FCI apurado. Possui os valores "S - Sim" e "N - Não".

Será **obrigatória** a apuração do FCI por meio da tela Cálculo da FCI (F075FCI) para os produtos quando a opção do campo for "N - Não" e, na tela Cadastro do Produto (F075PRO), o campo Origem Fiscal da Mercadoria for diferente de:

* 0 - Nacional, exceto as indicadas nos códigos 3, 4, 5 e 8
* 1 - Estrangeira - Importação direta, exceto a indicada no código 6
* 2 - Estrangeira - Adquirida no mercado interno, exceto a indicada no código 7
* 4 - Nacional, cuja produção tenha sido feita em conformidade com os processos produtivos básicos de que tratam o Decreto-Lei no 288/67 e as Leis nos 8.248/91, 8.387/91, 10.176/01 e 11.484/07
* 6 - Estrangeira - Importação direta, sem similar nacional, constante em lista de Resolução CAMEX e gás natural
* 7 - Estrangeira - Adquirida no mercado interno, sem similar nacional, constante em lista de Resolução CAMEX e gás natural

Listar código da FCI em operações internas 

Indica se o código da FCI será listado para produtos comprados em notas
fiscais de saída, quando houver vendar internas (no mesmo estado).

Impostos Documento Fiscal 

Indica a geração do detalhamento dos impostos no documento fiscal, na
tela F075INF, ele é
inicializado com Não. Caso opte-se em mostrar o detalhamento dos impostos, define se utiliza como base o valor líquido ou valor bruto menos descontos.

Contatos cliente igual a fornecedor

Permite replicar as informações contidas no contado do cliente para
o contato do fornecedor. Este campo só deve ser parametrizado com S
(sim), se o campo
Cliente igual Fornecedor, da guia Vendas 1, também estiver com essa
parametrização.

Ele será inicializado com o valor N por padrão, e só aceitará
alteração depois que a seguinte mensagem for confirmada positivamente:
Existem outras filiais cadastradas utilizando a parametrização
(Contados Cliente igual Fornecedor) anterior. Deseja alterar em todas
as filiais?”. Assim, serão atualizadas as informações dos campos abaixo,
de todas as filiais ligadas à empresa ativa:

Nome, Data Nascimento, Cód. Nível, Setor, Cargo, Telefone, Ramal, Fax,
E-mail, Hobby, Time, Situação, Usuário de Geração, Data da Geração, Hora
da Geração, Usuário Última Alteração, Data Última Alteração e Hora
Última Alteração.

Controle de Pesagem 

A informação deste campo é
utilizada na tela F115COS,
apresentando através de mensagem, qual ação a ser tomada se a
quantidade informada na pesagem for maior que a quantidade em aberto do
produto. Possui as seguintes opções:

1. Interromper Pesagem: Exibe uma mensagem de
   inconsistência para parar o processo;
2. Emitir alerta: Exibe uma mensagem de aviso
   que não paralisa o
   processo;
3. Alterar quantidade pedido: Altera automaticamente a
   quantidade do pedido (não emite alerta);
4. Não consistir: Não tem nenhuma funcionalidade.

Por padrão o campo é inicializado com a opção 4.

Trans. NFS Dev. Balança

Transação padrão da nota fiscal de produto para devolução via balança, efetuada na tela F115COE. Este campo não está disponível, para o Agronegócio.

Indicativo presencial   
Indicador de presença do comprador no estabelecimento comercial no momento da operação.  
As opções de preenchimento são: 0 - Não se aplica; 1 - Operação presencial; 2 - Operação não presencial, pela Internet; 3 - Operação não presencial, Teleatendimento; 4 - NFC-e em operação com entrega a domicílio; 5 - Operação presencial, fora do estabelecimento e 9 - Operação não presencial, outros.

A sugestão automática para as operações de pedido e notas fiscais de saída seguirá o critério abaixo:

1. Utilizar o indicativo presencial informado nas definições do cliente (F085CAD)
2. Se não encontrar nas definições do cliente, irá buscar da transação de produto ou serviço (F001TVE)
3. Se não encontrar nas definições do cliente e nas transações, será
   utilizado o indicativo presencial da filial
4. Se não encontrar valor na sugestão automática, o indicativo deve ser informado manualmente

Cancelar NFC automático

 Indica se a filial permite cancelar/excluir automaticamente as notas de entrada de transferência geradas através da nota fiscal de saída.

* N-Não: Não cancela/exclui automaticamente as notas de entrada quando está ligada a uma nota de saída cancelada
* S-Sim: Cancela/exclui automaticamente as notas de entrada quando está ligada a uma nota de saída cancelada
* Em Branco: Utiliza o mesmo comportamento da opção N-Não

Sit. Trib redução com perc. zerado

Quando este campo estiver parametrizado com “S - Sim” e a situação tributária for com redução, não é verificado se o percentual de redução está zerado, na geração o arquivo XML da nota fiscal eletrônica.

Gera NFRef

Indica, quando preenchido com Sim, que na geração de notas fiscais de saída, a tag <NFRef> será gerada para notas fiscais referenciadas no arquivo XML.

Importante

As notas fiscais referenciadas serão geradas no arquivo XML da nota fiscal para o grupo NFRef, quando são eletrônicas, ou RefNF, quando são de formulário. Este campo apenas é utilizado para notas fiscais referenciadas e nada impacta nas referências já existentes no sistema. Ou seja, mesmo que este campo esteja preenchido com Não, para as notas fiscais de devolução, cobrança e remessa, cupom fiscal, nota de produtor, entre outros documentos, a tag será gerada.

Baixa de Estoque NF Assíncrona

Por padrão, este campo está definido como Não, indicando que a baixa de estoque é realizada no mesmo momento em que a nota fiscal de saída é fechada, conforme padrão do sistema. Quando esta campo está definido como Sim, você deve cadastrar o processo automático 87 - Movimentar pendências de estoque do faturamento na tela Cadastro de Processo Automático (F000AGE), indicando o momento que esse processo deve ser executado pelo sistema. O valor desse campo (Sim ou Não) pode ser alterado a qualquer momento.

Geração Títulos NF Assíncrona

Por padrão, este campo está definido como Não, indicando que a geração de títulos é realizada no mesmo momento em que a nota fiscal de saída é fechada, conforme padrão do sistema. Quando esta campo está definido como Sim, você deve cadastrar o processo automático 88 - Movimentar pendências financeiras do faturamento na tela Cadastro de Processo Automático (F000AGE), indicando o momento que esse processo deve ser executado pelo sistema. O valor desse campo (Sim ou Não) pode ser alterado a qualquer momento.

Sugerir data de emissão em documentos de saída

Indica se a data atual será sugerida para a data de emissão nos documentos de saída.

Tipo Cálculo Diferimento

Indica como deve ser realizado o cálculo do ICMS diferido: por base ou valor.

Venda produto não ligado a cliente

Permite configurar o sistema para que sejam apresentados ou não, os produtos não ligados a clientes ao realizar a pesquisa (B2) em uma venda. Caso seja realizada a digitação manual, uma verificação também é realizada e uma mensagem é apresentada na tela avisando ao usuário que não é possível realizar a venda daquele item.

Esse comportamento será aplicado tanto nas telas de Saídas via Balança, Orçamentos, Contratos, Pedidos e Notas Fiscais de Saída como nos web services com.senior.g5.co.mcm.ven.contratovenda, com.senior.g5.co.mcm.ven.pedidos e com.senior.g5.co.mcm.ven.notafiscal nas ações SID de inclusão de pedido ou nota de venda. Por padrão, esse parâmetro é configurado com a opção S-Sim.

Registro agrícola

Essa informação é utilizada na geração dos relatórios estaduais;  
Este campo pode ser visualizado apenas com a Proprietária do Receituário Agronômico.

Categoria de comercialização de agrotóxico:   
Preencher com a categoria a qual a empresa pertence. As categorias podem ser cadastradas conforme a tela F113CCA, essa informação é utilizada na geração dos relatórios estaduais;  
Este campo pode ser visualizado apenas com a Proprietária do Receituário Agronômico.

Obriga receita agronômica no pedido

Se preenchido com Sim, a tela de Receituário (F113REM) será aberta para impressão da receita agronômica, quando o pedido for fechado nas telas F120GPC e F120GPD,desde que o campo Gerar receituário (F001TVE) também esteja preenchido com Sim. .  
Se preenchido com Não ou em branco, a tela de Receituário (F113REM) não será aberta para impressão da receita agronômica ao fechar um pedido.  

Este campo pode ser visualizado apenas com a Proprietária do Receituário Agronômico.

Data última integração de dados do parceiro e Hora última integração de dados do parceiro  
São preenchidos automaticamente de acordo com o processo de integração à base de dados de terceiro.  
Este campo pode ser visualizado apenas com a Proprietária do Receituário Agronômico.

Número de vias da receita agronômica

Informar quantas vias da receita devem ser impressas. Essa informação é sugerida no campo Qtd. vias impressãoda tela F113REM.  
Este campo pode ser visualizado apenas com a Proprietária do Receituário Agronômico.

Gera Pedido para excesso de peso na devolução

Campo utilizado nas devoluções do Agronegócio. Se este campo estiver preenchido com Sim, na tela de devolução F115COE, será gerado um pedido de venda, caso o produtor rural carregue uma quantidade superior a descrita na nota de devolução. Ou seja, esta quantidade excedente será vendida ao produtor.

Referenciar NFC-e/CF-e

Indica se a NFC-e e CF-e será referenciada no arquivo XML da NF-e caso existir. Na emissão de uma Nota fiscal eletrônica que possua uma NFC-e ou CF-e referênciada a ela, a tag **refNFe** do arquivo XML é gerada com a Chave do Documento Eletrônico da nota referenciada, quando este campo estiver parametrizado como **S - Sim**.

Versão PAF-ECF

Indica a versão da PAF-ECF que a filial está credenciada.

Gerar Boleto NF-e

Indica se é feita a geração automática de boletos da nota fiscal eletrônica.

Gerar Boleto NFS-e

Indica se é feita a geração automática de boletos da nota fiscal de serviço eletrônica.

**Importante**

Para mais informações sobre a geração de boletos e envio do arquivo como anexo no e-mail de emissão do documento, consulte a documentação do eDocs.

Permitir parcelas com venc. menor ou igual parcela anterior

As opções disponíveis são "S - Sim" e "N - Não", sendo "N - Não" o padrão. Quando "S - Sim", é possível informar o vencimento das parcelas independentemente da sequência e com data igual ou inferior ao vencimento da anterior, desde que não seja inferior à data de emissão dos pedidos, nas seguintes rotinas:

* Agrupado (F120GPD)
* Avaliação de Produto (F120GPC)
* Simplificada (F120GPB)
* Televendas (F129PED)
* Web service Com.senior.g5.co.mcm.ven.pedidos, porta GravarPedidos

Valida número do receituário por estado

Este campo é utilizado pelo Receituário Agronômico, para definir se será possível gerar receita que tenha uma ART com estado diferente do estado de entrega do cliente. Veja como é feito este controle em ART com estado diferente do estado de entrega e no Ajuda da tela F113REM.

**Emissão de Nota Fiscal com lotes vencidos**

Permite a emissão de nota fiscal de saída e entrada com itens que possuem lotes vencidos. Por padrão, o campo é preenchido com **N - Não**, mantendo o comportamento atual do sistema que é não faturar itens com lote vencido, sendo necessário alterar a data do vencimento do lote para emitir a nota fiscal. Quando o campo estiver preenchido com **S - Sim**, ao emitir uma nota fiscal que contenha itens com lotes vencidos, ela será processada normalmente.

Fator FCA

Defina o índice de FCA utilizado para a atualização da base de cálculo do ICMS. Este índice é cadastrado na tela Moedas (F031AIM).

Origem do código GTIN

Indica a origem de busca dos códigos GTIN (cEAN e cEANTrib) na geração dos documentos eletrônicos. A opção de preenchimento padrão é **1 - cEANTrib GTIN Unidade Tributável e cEAN do Código de Barras**. Para mais informações consulte a documentação do GTIN.

Integração com cálculo de frete

Indica se a filial tem integração com a Gestão de Fretes para cálculo de frete.

Mensagem - 1, Mensagem - 2, Mensagem - 3 e Mensagem - 4  
Permitem parametrizar um padrão de mensagens fiscais para a nota fiscal de saída, conforme a regra de sugestão.

Utiliza regra arredondamento ABNT

Esse parâmetro indica se o sistema deve utilizar a regra de arredondamento da ABNT para arredondar os valores dos itens de serviço (apenas itens de serviços) dos pedidos, notas fiscais de saída, ordens de compra e notas fiscais de entrada.

Quando o parâmetro estiver ativo, são arredondados os seguintes valores dos itens de serviço: Valor Bruto, PIS Retido, COFINS Retido, CSLL, Outras Retenções, INSS, IRRF e ISS.

A regra de arredondamento ABNT é aplicada apenas aos itens de serviço devido à necessidade de integração das notas fiscais de serviço das prefeituras. Para as notas fiscais eletrônicas que possuem itens de produto, a SEFAZ não obriga a utilização da regra ABNT, sendo válido o uso do arredondamento padrão do ERP.

Cálculo de Desoneração de ICMS

Indica qual fórmula será usada para calcular o ICMS Desonerado e o ICMS Diferido nas notas fiscais de saída e pedidos de venda.

* "0 - Padrão": aplica a fórmula de cálculo padrão do sistema para o ICMS (base de cálculo X % ICMS);
* "1 - Resolução 13/2019 RJ": faz o cálculo do ICMS conforme consta na resolução:

  Para o ICMS **desonerado**, é aplicada a seguinte fórmula: *Preço na Nota Fiscal / (1 - Alíquota) \* Alíquota*, sendo que:  
  Preço da Nota fiscal: base de cálculo do ICMS da operação;  
  Alíquota: Alíquota do ICMS + alíquota do FCP da operação.

  Se o produto possuir redução de base de cálculo, o valor do ICMS desonerado deverá ser: % da Redução de base de cálculo = 1 - Percentual da Base de Cálculo Reduzida, e a fórmula aplicada é *Valor do ICMS desonerado = Preço na Nota Fiscal \* (1 - (Alíquota \* (1 - Percentual de redução da BC))) / (1- Alíquota) - Preço na Nota Fiscal*, sendo que:  
  Percentual da Base de Cálculo Reduzida: percentual de redução de base de cálculo indicado na parametrização da tabela de redução;  
  Preço da Nota fiscal: base de cálculo do ICMS da operação;  
  Alíquota: Alíquota do ICMS + alíquota do FCP da operação.

  Para o ICMS **diferido**, a fórmula é *Valor do ICMS diferido = (Preço na Nota Fiscal / (1 - Alíquota)) \* Alíquota*, onde:  
  Preço da Nota fiscal: base de cálculo do ICMS diferido;  
  Alíquota: percentual do ICMS diferido.

  No caso de diferimento parcial é aplicado o percentual de diferimento, que é o diferimento sobre o valor do imposto.
* "2 - Resolução 79/2022 SC": faz o cálculo do ICMS conforme consta na resolução.

  Seguem os cálculos dos respectivos CSTs. Para os CSTs 30 e 40 de ICMS isento ou não tributado:  
  Preço do produto \* Alíquota.

  Para os CSTs 20 e 70 de redução de ICMS na base de cálculo:  
  (Percentual de redução da BC / (1 - Percentual de redução da BC) \* valor do ICMS.

  CST 50 de suspensão de ICMS:  
  Valor da base de cálculo do ICMS \* Alíquota

  Essa opção foi revogada pelo estado de Santa Catarina e atualmente está em desuso. Recomenda-se o uso da opção "0 - Padrão", que aplica a fórmula de cálculo padrão do sistema para o ICMS (base de cálculo \* % ICMS).

* "2 - Resolução 79/2022 SC": faz o cálculo do ICMS conforme consta na resolução.

  Seguem os cálculos dos respectivos CSTs. Para os CSTs 30 e 40 de ICMS isento ou não tributado:  
  Preço do produto \* Alíquota.

  Para os CSTs 20 e 70 de redução de ICMS na base de cálculo:  
  (Percentual de redução da BC / (1 - Percentual de redução da BC) \* valor do ICMS.

  CST 50 de suspensão de ICMS:  
  Valor da base de cálculo do ICMS \* Alíquota

  CST 51 de suspensão de ICMS:  
  Atenção: O uso do cálculo de desoneração de ICMS tipo 2 em conjunto com a CST 51, pode implicar na busca de valores da tabela de preço de um item de nota fiscal, independente da configuração do Indicativo se deve buscar os percentuais e preço do produto/serviço no faturamento não respeitando o que está no pedido localizado na filial de vendas.

  Essa opção foi revogada pelo estado de Santa Catarina e atualmente está em desuso. Recomenda-se o uso da opção "0 - Padrão", que aplica a fórmula de cálculo padrão do sistema para o ICMS (base de cálculo \* % ICMS).

Confira também a documentação sobre ICMS Diferido.

Observação

1. A Resolução 79/2022 SC estabelece regras para a desoneração do ICMS em determinadas operações.
Quando um cliente possui essa resolução e está enquadrado na Situação Tributária terminada em 51, o sistema realiza um controle específico sobre a precificação dos produtos.

2. Regras de cálculo e comportamento do sistema  
Para clientes com a Resolução 79/2022 SC e Situação Tributária terminada em 51, o sistema impede a alteração do Preço Unitário do item quando uma Tabela de Preço está informada. O preço sempre será baseado no valor cadastrado na tabela, garantindo a correta aplicação da legislação.

3. Parâmetro dinâmico NOTAFISCAL.ICMSDIFERIDO.REMOVERDOPRECOUNITARIO da Filial de Vendas.  
Esse parâmetro interfere diretamente no Preço Unitário do Item de Produto. Para maiores detalhes acesse a documentação aqui.

4. Considerações Finais  
Essa funcionalidade garante a correta aplicação da Resolução 79/2022 SC, assegurando conformidade fiscal e padronização dos valores praticados.

**Utiliza assinatura eletrônica em receituário**

Indica se a filial faz uso da assinatura eletrônica do responsável técnico, na emissão do receituário agronômico.

## Páginas relacionadas

* [aqui](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/campos-analise-credito-pedidos.htm)
* [Tratamento de Formas de Vendas](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/tratamentoformasvendas.htm)
* [Rateio do Valor de Outras](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/webservices/rateio-valor-de-outras.htm)
* [Geração de Pedidos de Previsão para Plano Produção](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f120lpv.htm)
* [Influência dos Campos da Filial do Usuário na liberação do Pedido por Área](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/influencia-campos-liberacao-pedido.htm)
* [F120GRA](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f120gra.htm)
* [F120DPE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f120dpe.htm)
* [F120GPD](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f120gpd.htm)
* [F120FEM](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f120fem.htm)
* [F129PED](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f129ped.htm)
* [VEN-120CNFEC02](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_120cnfec02.htm)
* [Placa](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f140div.htm#placa)
* [F135APM](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f135apm.htm)
* [F135FCP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f135fcp.htm)
* [F135AEA](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f135aea.htm)
* [F140PRE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f140pre.htm)
* [documentação correspondente](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/analise-credito-pedido.htm)
* [F301SUB](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_financas/f301sub.htm)
* [F301BCD](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_financas/f301bcd.htm)
* [F301BMD](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_financas/f301bmd.htm)
* [F140LOT](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f140lot.htm)
* [F129UFP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f129ufp.htm)
* [F075PRO](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075pro.htm)
* [F075GFP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075gfp.htm)
* [F135APF](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f135apf.htm)
* [IcmDifFat](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#IcmDifFat)
* [aqui](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/campo_manter_icms_do_pedido_no_faturamento.htm)
* [VEN-140MNTTR01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_140mnttr01.htm)
* [F070FCP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070fcp.htm)
* [F115CST](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f115cst.htm)
* [F115COS](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f115cos.htm)
* [F115CAR](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f115car.htm)
* [F115COE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f115coe.htm)
* [F115TRF](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f115trf.htm)
* [COM-000SEQOR01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/com_000seqor01.htm)
* [F070CFA](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070cfa.htm)
* [Cálculo da FCI (F075FCI)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075fci.htm)
* [F075INF](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075inf.htm)
* [F085CAD](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f085cad.htm)
* [F001TVE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f001tve.htm)
* [87 - Movimentar pendências de estoque do faturamento](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/processos-automaticos/87-movimentar-pendencias-estoque-faturamento.htm)
* [F000AGE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_recursos/f000age.htm)
* [88 - Movimentar pendências financeiras do faturamento](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/processos-automaticos/88-movimentar-pendencias-financeiras-faturamento.htm)
* [com.senior.g5.co.mcm.ven.contratovenda](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/webservices/com_senior_g5_co_mcm_ven_contratovenda.htm)
* [com.senior.g5.co.mcm.ven.pedidos](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/webservices/com_senior_g5_co_mcm_ven_pedidos.htm)
* [com.senior.g5.co.mcm.ven.notafiscal](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/webservices/com_senior_g5_co_mcm_ven_notafiscal.htm)
* [inclusão de pedido](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/acoes-sid/indice-mercado-pedido-vendas.htm)
* [nota de venda](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/acoes-sid/indice-mercado-nota-fiscal-venda.htm)
* [F113CCA](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f113cca.htm)
* [F113REM](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f113rem.htm)
* [F120GPC](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f120gpc.htm)
* [Gerar receituário](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f001tve.htm#F001TVE_DEVenRca2)
* [integração](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/manuais_processos/receituario_agronomico/inicio.htm#integracao)
* [documentação do eDocs](https://documentacao.senior.com.br/documentoseletronicos/5.8.15/index.htm#html_ajuda/documentacaoprocesso/envio-boleto.htm)
* [ART com estado diferente do estado de entrega](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/manuais_processos/receituario_agronomico/processos/responsavel_tecnico.htm#estado)
* [F113REM](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f113rem.htm#responsavel)
* [F031AIM](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f031aim.htm)
* [GTIN](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/manuais_processos/mercado/nf-e/regras-e-sugestoes-valores.htm#gtin)
* [regra de sugestão](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/manuais_processos/mercado/nf-e/regras-e-sugestoes-valores.htm#mensagens-fiscais)
* [documentação sobre ICMS Diferido](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/impostos-icms.htm#icms-desonerado)
* [aqui](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000ppd.htm)
