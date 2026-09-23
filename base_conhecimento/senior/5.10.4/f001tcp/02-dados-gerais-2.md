# Dados Gerais 2

> **Fonte:** F001TCP - Transações de Compras — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f001tcp.htm  
> **Trilha:** Ajuda por telas > Cadastros > Transações > Parâmetros por Gestão > Compras  
> **Telas citadas:** E001TCP, E001TNS, E075DER, E440PCD, F001TES, F001TVE, F001TXF, F012FXF, F012FXT, F051DIS, F075PXT, F080ISV, F080SXT, F095CAD, F113COA, F403FPR, F403FSE, F403LFP, F403LFS, F420GOC, F420OSC, F440GNE, F440NCI, F460PFO  
> **Identificadores de regras:** EST-215VALRE01

---
Calcula Desconto Suframa

 Indica se deverá ser calculado o desconto Suframa para a nota fiscal de entrada.

Gera Pedido

Indica se deve ser exibida uma mensagem ao usuário no fechamento de notas tipos "1, 2, 3 e 7" para geração automática de pedido. Este parâmetro deve estar definido na transação do item. Ver também GerMsgPed.

Observação

O processo de geração de pedido a partir da Ordem de Compra ocorre exclusivamente nas telas Ordem de Compra Agrupada (F420GOC) e Ordens de Compra via Solicitação de Compra (F420OSC), durante o fechamento da ordem.

Origem do valor do movimento de estoque

 Definir o valor do movimento de estoque gerado para as notas fiscais de tipo 2, 3, 4, 5
e 11, desde que baseadas numa nota fiscal de saída.

1. Preço médio atual (multiplica o preço médio pela quantidade de estoque)

Observação

Primeiramente, será realizada a busca do preço médio na tabela E210ME, no campo PREMED. Se o campo estiver com valor igual a zero, uma segunda busca será feita na tabela E075DER, também no campo PREMED. Caso esse segundo também retorne zero, a busca será feita pelo valor do movimento de origem, da mesma forma que ocorre quando o campo está configurado com o valor "2 - Valor do movimento de origem".

2. Valor movimento de origem (a valor do movimento vem do movimento de saída)
3. Calculado pela nota (o valor do movimento é calculado pela nota fiscal de entrada)

Para que seja assumida a opção "2 - Valor do movimento de origem" nos movimentos de estoque gerados a partir de notas de entrada do tipo 4 e 5(Retorno), é necessário ativar o identificador "EST-215VALRE01".

Necessita Conferência

 Indicativo para procedimento na nota fiscal, se informado "S", a nota fiscal
não poderá ser fechada pelas rotinas normais, necessita que seja efetuado a
contagem e posteriormente a conferência, na rotina de conferência é efetuado o
fechamento da nota fiscal automaticamente.

Gerar Conferência Automática

 Indicativo para gerar a conferência automática, se informado "S", quando
optar pelo botão fechar, gera automaticamente um registro de contagem com todos
os itens da nota fiscal.

Nota Herda Rateio Origem

 Indica se a nota deverá herdar o rateio na origem (ordem de compra, nota de saída ou contrato).

NFE Exige Contrato

Indica se a nota deverá exigir contrato. Os parâmetros "Exige Ordem de Compra" (E001TNS.CPRAOC) e "Exige
Contrato" (E001TCP.CPRCTR) podem ser definidos como "S" simultaneamente, porém na nota
fiscal somente um dos documentos envolvidos (ordem de compra ou contrato), poderá
ser informado.

No caso do contrato, deverá ser informado qualquer contrato nos
dados gerais da nota, permitindo alterá-lo na grade. As consistências serão feitas para as
transações dos itens da nota.

Ind.Trans.Bonificação

 Indica se permitirá movimentação sem valor (E001TNS.ESTES) e uma transação que gere movimento de saída de estoque.

Tratamento no Fechamento de Nota Fiscal de Entrada  
Para itens com transação de bonificação, o sistema realiza os seguintes processos no fechamento da nota fiscal de entrada:

* Gera um movimento de entrada no estoque com quantidade, mas sem valor.
* Gera um movimento de saída no estoque apenas com o valor correspondente aos impostos recuperáveis dos itens.

Este cálculo é realizado subtraindo o valor líquido do item na nota fiscal pelo valor que seria utilizado no movimento de estoque (processo padrão para itens normais de entrada). A diferença apurada será o valor atribuído ao movimento de saída. É importante destacar que a movimentação de saída dos impostos só ocorrerá quando a operação for de recuperação de impostos.

Importante

Caso não haja saldo suficiente no estoque:

* Apenas o movimento de entrada será gerado, com a quantidade do item (sem valor).
* Na tela Consulta de Movimentos de Estoque, será apresentada a mensagem no campo Observação (Movimentos): "Imposto a recuperar não lançado por insuficiência de saldo físico do estoque."

Caso haja saldo no estoque

* A movimentação de entrada e saída será realizada normalmente.

Impacto no Custo de Aquisição  
Quando a operação de aquisição gera crédito de impostos recuperáveis (PIS, COFINS, ICMS e IPI), o valor correspondente ao crédito tributário do imposto não faz parte do custo de aquisição da mercadoria, isso porque a entrada não gera valor de custo para a mercadoria, mas é sim uma operação geradora de crédito de ICMS. Dessa forma, o custo total do estoque deve ser impactado com a subtração do crédito de ICMS.

Essa regra de formação do custo de aquisição está detalhada no CPC 02, item 11, conforme abaixo:

11.  
O custo de aquisição dos estoques compreende o preço de compra, os impostos de importação e outros tributos (exceto os recuperáveis junto ao fisco), bem como os custos de transporte, seguro, manuseio e outros diretamente atribuíveis à aquisição de produtos acabados, materiais e serviços. Descontos comerciais, abatimentos e outros itens semelhantes devem ser deduzidos na determinação do custo de aquisição.

Exemplo Prático

1ª Nota Fiscal (100 unidades cobradas pelo fornecedor):

* Valor da mercadoria: 1.000,00
* IPI (imposto não recuperável): 50,00
* ICMS (imposto recuperável): 120,00
* Valor total da NF: 1.050,00

2ª Nota Fiscal (1 unidade bonificada – não cobrada pelo fornecedor):

* Valor da mercadoria: 10,00
* IPI (imposto não recuperável): 0,50
* ICMS (imposto recuperável): 1,20
* Valor total da NF: 10,50

Cálculo do Custo de Aquisição no Estoque:

1. Valor das 100 unidades cobradas pelo fornecedor: 1.050,00  
2. Valor das 1 unidade não cobrada pelo fornecedor: 0,00  
3. ICMS a recuperar da NF de 100 unidades: -120,00  
4. ICMS a recuperar da NF de 1 unidade: -1,20

Custo total das 101 unidades no estoque: \*928,80

Tipo de recebimento 

Indicativo para classificar as transações do
módulo "CÔO" (Compras - Manutenção de Ordem de Compra), que serão utilizadas na
tela F460PFO (Suprimentos > Gestão de Compras > Contratos > Participação de
Fornecedores).

* 0 - Não é recebimento: transação não é utilizada nas rotinas de agronegócio.
  1 - A Fixar: O fornecedor efetua a entrada
  do produto esperando uma melhor negociação no futuro.
  2 - Depósito: Onde o fornecedor deixa o produto em depósito para uma possível negociação.
  3 - Compra Imediata: O fornecedor efetua a entrada do produto e recebe no ato da operação.

Reab. Pedido

Indicativo de reabilitação de pedido. Se atribuído "S", ao gerar notas fiscais de entrada na
tela "F440GNE" que utilizam
notas fiscais de saída que foram geradas via pedido como origem (tipos "2", "3", "4", "5", "7"
e "8"),  a
rotina reabilitará os itens de pedidos ligados à nota fiscal de saída que está
sendo devolvida.

Permite retorno componentes

Indica se a transação permite ou não o retorno de componentes industrializados,
sendo que por padrão todas as transações serão preenchidas com "S - Sim". Ao
gerar notas fiscais de retorno dos componentes utilizados para a
industrialização, serão filtrados os itens das notas fiscais de entrada cuja a
transação possua o indicativo de retorno preenchido com "S - Sim".

Obrigar Cód. Produto/Serviço

Indica se o código do produto ou serviço devem ser obrigatórios no fechamento de notas fiscais.

Obrigar ligação família/produto/serviço X transação

 Indica se a transação obriga a ligação de família e/ou produto e/ou serviço com a transação. As ligações devem ser realizadas pelos seguintes caminhos:

* F012FXT - Cadastros > Produtos e Serviços > Ligações > Família X Transação;
* F075PXT - Cadastros > Produtos e Serviços > Ligações > Produto X Transação;
* F080SXT - Cadastros > Produtos e Serviços > Ligações > Serviço X Transação.

Obrigar ligação família/produto/serviço X fornecedor

 Indicativo se a transação obriga a ligação de família e/ou produto e/ou serviço com o fornecedor. As ligações devem ser realizadas pelos seguintes caminhos:

* F012FXF - Cadastros > Produtos e Serviços > Ligações > Família X Fornecedor
* F403FPR - Cadastros > Clientes e Fornecedores > Fornecedores > Ligações > Fornecedor X Produtos > Individual;
* F403LFP - Cadastros > Clientes e Fornecedores > Fornecedores > Ligações > Fornecedor X Produtos > Agrupado;
* F403FSE - Cadastros > Clientes e Fornecedores > Fornecedores > Ligações > Fornecedor X Serviços > Individual;
* F403LFS - Cadastros > Clientes e Fornecedores > Fornecedores > Ligações > Fornecedor X Serviços > Agrupado.

Ind. O.C. Controle
Cota

Indica se a transação participa ou não do controle de cota de
compra.

Obrigar Transação X Cta. Fin.

Indica se é obrigatória a ligação da transação com conta financeira. A ligação deve ser realizada pelo seguinte caminho:

* F001TXF - Cadastros > Transações > Transação X Conta financeira.

Intermediação de Serviços

Apenas para o Varejo Senior: Este campo indica se a transação é referente a intermediação de serviços, ele está ligado aos campos Realiza Intermediação de Serviços, da tela
F070EMPe à tela
F080ISV.

Tipo Cálculo Devolução

 Define o tipo de cálculo que será obedecido ao efetuar uma devolução. Ao incluir um novo registro, seu valor padrão será P - Cálculo Proporcional. O campo pode ter o preenchimento:

* P - Cálculo Proporcional

  Ao gerar uma nota fiscal de devolução parcial, seus valores (frete, seguro, acréscimo financeiro, base ICMS, base IPI, etc) são recalculados proporcionalmente de acordo com a nota fiscal de origem da devolução, considerando a quantidade que está sendo devolvida, em relação à quantidade da nota fiscal de entrada de origem. Esta rotina não aceita parametrização dos identificadores de regras.
* R - Recálculo de Valores

  Ao gerar uma nota fiscal de devolução parcial, os valores são recalculados sem considerar a nota fiscal de entrada de origem. Nesta rotina as parametrizações feitas manualmente ou através de identificadores de regras são consideradas.

Importante

* Se o preenchimento deste campo for P - Cálculo Proporcional, a transação de entrada utilizada na venda, deve estar parametrizada conforme o leiaute pré-definido da composição do valor líquido. Veja detalhes do preenchimento de campos aqui;
* Caso o preenchimento deste campo for R - Recálculo de Valores e for uma devolução total, o sistema mantém os valores da nota fiscal de saída e não recalcula a nota de entrada, pois o objetivo é devolver os mesmos valores da saída. Para que o recálculo seja feito, é necessário clicar no botão Recalcular(M) e caso queira esse comportamento de forma automática na devolução total, a sugestão é ativar o parâmetro global RecNfcDev.
* Este campo também impacta outras notas fiscais de entrada do tipo 2, 3, 4, 5, 7, 8, e 11.

Código do Dispositivo Fiscal

Código do dispositivo cadastrado na tela F051DIS.

Estado inicial da nota fiscal por transferência

 Indica qual deve ser o estado após a geração da nota fiscal por transferência. Possui as seguintes opções:

* **0 - Não se aplica:** utiliza a configuração existente na tela Parâmetros da Filial para Compras;
* **1 - Digitada:** gera a nota automática de entrada como Digitada;
* **2 - Fechada:** gera a nota automática de entrada Fechada.

Controla ATR Médio

Este campo indica se é possível inserir um item na nota fiscal sem valor unitário.

Cons. integ. terc. Bloco K   
Tem por finalidade definir se a transação de compra permitirá que a nota seja integrada na rotina de integração do bloco K. Essa integração busca dados das notas fiscais de Remessa/Retorno para o módulo de Controladoria, ou seja, quando esse campo estiver definido como **Não** na transação vinculada a nota, esta não será considerada na integração do bloco K.

Operação de Compra

 Este campo identifica o tipo de operação da transação:

* Normal: demais notas que não são de Recebimento ou Pagamento.
* Pagamento: utilizada para notas fiscais que integram apenas com Financeiro, em operações em que o Fornecedor exige adiantamento de pagamento. Nestes casos, podemos ter notas fiscais que não calcula ICMS. Caso seja necessário abater o valor de ICMS da base de PIS e COFINS, o sistema realiza uma simulação de cálculo. Este valor é armazenado nos campos:
  + PerIef - Percentual do ICMS entrega futura;
  + BasIef - Valor base ICMS entrega futura;
  + VlrIef - Valor ICMS entrega futura.

  O valor de ICMS entrega futura é descontado da base de PIS e COFINS se os seguintes requisitos forem atendidos:

  + Item da Nota Fiscal de Entrada utilizar uma transação do tipo Pagamento;
  + Transação deve estar parametrizada para Descontar o ICMS da base de PIS ou COFINS;
  + O Fornecedor utilizado não pode pertencer ao Simples Nacional (F095CAD - Código do Regime Tributário);
  + Item não possui valores para o ICMS.

  Veja detalhes no processo de Redução do ICMS na base de PIS / COFINS.
* Recebimento: utilizada nas Notas Fiscais de Entrada que possuem integração apenas com o Estoque, pois a movimentação financeira já foi efetuada em algum processo anterior.

Para saber mais sobre as configurações para notas de entrada, acesse a documentação Transações de Vendas (F001TVE).

Em caso de dúvidas sobre o processo e as telas de Venda Futura, consulte a seguinte documentação: Processo de Vendas para Entrega Futura.

Exporta Siscoserv

Indica se a informação será exportada para o Siscoserv. Quando o contrato ou pedido for do tipo Siscoserv esse documento será integrado para o módulo Siscoserv e não será integrado para gestão de tributos.

Esse campo é habilitado somente para transação é de serviço, porque para o Siscoserv é exportado somente as aquisições e vendas de serviços. Para transações de compras esse campo fica desabilitado.

% Diário da Adm. Temp. do AFRMM

Neste campo pode ser definido o percentual diário que será utilizado do valor da base original para formar a base de cálculo do imposto, a fim de atender o processo de Admissão Temporária, para produtos importados.

Transação permite Geração de Manifesto

Indica se a transação permite a geração de "Manifestação de destinatário" na geração de Nota fiscal de entrada agrupada.

**Processar Ligação Compra Retorno**

Se o valor do parâmetro for igual a "S - Sim", o processo de conta e ordem será habilitado ao fechar notas de compra tipo "4 - Retorno (Industrialização)". Ele se baseia na relação de notas de compra "1 - NF Entrada" com as notas tipo "4 - Retorno (Industrialização)". Ao fechar a nota, será possível associar as notas de compra por dois modos:

1. **Automática:** o sistema busca as notas de compra em que o **Cliente Recebedor** (CliRcb) é igual ao fornecedor da nota de retorno, partindo das notas mais antigas para as mais recentes;
2. **Manual**: abre uma tela de pesquisa para seleção das notas que devem ser relacionadas. Nesse caso, o Cliente Recebedor (CliRcb) também deve ser igual ao fornecedor da nota de retorno. Serão carregadas apenas as notas fiscais com itens que ainda não foram totalmente retornados para o cliente via NF "4 - Retorno (Industrialização)". Saldo do item da NF compra para retorno = (Qtde. Entrada Estoque - (Qtde. Devolvida + Qtde. Retornada)) ou (E440Ipc.QtdEst - (E440Ipc.QtdDev + E440PCD.QtdRet));
3. **Manual Item:** abre a tela Nota Fiscal de Retorno – Notas Fiscais Compra – Itens (F440NCI) para relacionar cada um dos itens da nota fiscal de retorno que está sendo fechada com itens de notas de compra que compõem o retorno. Nesse caso, o Cliente Recebedor (CliRcb) também deve ser igual ao fornecedor da nota de retorno. Serão carregadas apenas as notas fiscais com itens que ainda não foram totalmente retornados para o cliente via NF "4 - Retorno (Industrialização)". Saldo do item da NF compra para retorno = (Qtde. Entrada Estoque - (Qtde. Devolvida + Qtde. Retornada)) ou (E440Ipc.QtdEst - (E440Ipc.QtdDev + E440PCD.QtdRet)).

Após selecionar um dos modos, serão gerados registros em uma estrutura de relacionamento entre as notas e será atualizada a quantidade retornada ao comprador de cada item das notas de compras que estão sendo retornadas.

**Observação**

Se a quantidade das notas de compra não for suficiente para atender o retorno, será exibida uma mensagem perguntando se o usuário quer prosseguir. Caso sim, a quantidade retornada da compra por notas de retorno (E440PCD.QtdRci) será a mesma quantidade da nota de compra. Caso não, será exibido um log informando a quantidade faltante. A quantidade do retorno será consumida de acordo com a quantidade do item na nota de compra encontrada.

**Importante**

A relação das notas fiscais de remessa que são enviadas do vendedor para o industrializador deve ser enviada ao comprador para que ela seja gravada na nota fiscal de retorno como observação, pois essas notas fiscais não constarão na sua base de dados, ou seja, deve ser informada manualmente na nota fiscal de retorno.

No relacionamento **manual por item**, a transação da movimentação de estoque consignado gerado pela nota de retorno e configurado via tela Transações de Estoques (F001TES) deve ter a Forma Valorização Movimento definida como "M - Movimento". Isso para que o movimento de estoque tenha o valor definido com base no valor do movimento de estoque gerado pela nota de compra do item que está sendo retornado.

No relacionamento **manual ou automático**, se a transação da movimentação de estoque consignado gerado pela nota de retorno e configurado via tela Transações de Estoques (F001TES) estiver com a Forma Valorização Movimento definida como "M - Movimento", o movimento de estoque será gerado com base no valor do item informado na nota fiscal de retorno.

Para qualquer um dos modos, se a forma de valorização do movimento de estoque gerado pela nota de retorno for definida como "F - Fechamento", o valor do movimento de estoque gerado pelo item de retorno será definido com base no **preço médio do item**.

Processar ligação com nota fiscal de cobrança de serviço

Tem a finalidade de no fechamento da nota, possibilitar que o usuário efetue a ligação entre a nota de cobrança de serviço e a de retorno de industrialização com o intuito de identificar os apontamentos de produção em terceiros.

**Indicativo se é inclusa no Programa de Aquisição de Alimentos (PAA)**

Indica se a transação se enquadra no PAA.

**Movimento no Saldo do Produtor**   
Indica se Transação soma ou subtrai do Saldo do produtor rural.

**Código da Operação**   
Código do tipo de operação do agronegócio, cadastrado na tela F113COA.

Emissão em Regime Especial

Indica se o sistema deve exportar, no SPED Fiscal, como nota fiscal emitida por regime especial ou norma específica. Quando "S - Sim", as notas fiscais com esta transação serão exportadas no SPED Fiscal conforme previsto no Guia Prático (Registro C100, exceção 4). Afeta a geração dos Registros C100, C170 e C190.

Desconta o valor do ICMS ST Destacado do valor do estoque

Indica se deve descontar o valor do ICMS ST Destacado do valor do estoque. O valor padrão é "S - Sim". Nas transações em que o desconto não deve ocorrer, preencha o campo como "N - Não".

Observação

Este parâmetro será considerado apenas nos casos em que não houver recuperação de ICMS (Recupera ICMS = “N”).

Quando existir recuperação/crédito de ICMS (Recupera ICMS = “S”), o valor do ICMS-ST destacado não será descontado do valor do estoque, independentemente da configuração deste campo.

**Possíveis cenários:**

* Recupera ICMS = “S”
  + Desconta ICMS-ST do estoque = “SIM”
  + Resultado: parâmetro não é considerado.
* Recupera ICMS = “S”
  + Desconta ICMS-ST do estoque = “NÃO”
  + Resultado: comportamento permanece desconsiderando o parâmetro devido à recuperação de ICMS.
* Recupera ICMS = “N”
  + O parâmetro “Desconta o valor do ICMS-ST destacado do valor do estoque” passa a ser efetivamente considerado no cálculo do estoque.

**Tipo de lançamento para LCDPR**

Este campo permite informar o tipo de lançamento para LCDPR em transações de compras. Há quatro opções disponíveis para seleção, sendo elas:

* 0 - Nenhum
* 1 - Receita da atividade rural
* 2 - Despesas de custeio e investimentos
* 3 - Produtos entregues no ano referente a adiantamentos de recursos financeiros.

**Emitir Contra Nota**

Permite indicar entre "S - Sim" ou "N - Não" para emitir contra nota para as notas fiscais de entrada do tipo 1, 9 ou 11.

Transação de emissão da contra nota

Permite selecionar as transações do módulo "COF" para a emissão de contra nota em operação com ICMS integral diferido. Esse campo só estará disponível se o campo Emitir Contra Nota estiver ativo.

**Observação**

Feita a seleção da Transação de emissão da contra nota, o sistema verificará se existe integração com algum outro módulo. Se existir, o sistema notificará o usuário, e caso o usuário opte pela opção "Não", o ERP retornará o valor anterior do campo.

Tipo Cálculo Devolução CBS/IBS

Define o tipo de cálculo que será obedecido ao efetuar uma devolução. Ao incluir um novo registro, seu valor padrão será "P - Cálculo Proporcional". Este campo também impacta outras notas fiscais de entrada do tipo 2, 3, 4, 5, 7, 8, e 11. Opções de preenchimento:

* "P - Cálculo Proporcional": ao gerar uma nota fiscal de devolução parcial, os valores de CBS e IBS são recalculados proporcionalmente de acordo com a nota fiscal de origem da devolução, considerando a quantidade que está sendo devolvida, em relação à quantidade da nota fiscal de entrada de origem. Esta rotina não aceita parametrização dos identificadores de regras.
* "R - Recálculo de Valores": ao gerar uma nota fiscal de devolução parcial, os valores são recalculados sem considerar a nota fiscal de entrada de origem. Nesta rotina as parametrizações feitas manualmente ou através de identificadores de regras são consideradas.

## Páginas relacionadas

* [GerMsgPed](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#GerMsgPed)
* [Ordem de Compra Agrupada (F420GOC)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f420goc.htm)
* [Ordens de Compra via Solicitação de Compra (F420OSC)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f420osc.htm)
* [F012FXT](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f012fxt.htm)
* [F075PXT](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075pxt.htm)
* [F080SXT](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f080sxt.htm)
* [F012FXF](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f012fxf.htm)
* [F403FPR](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f403fpr.htm)
* [F403LFP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f403lfp.htm)
* [F403FSE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f403fse.htm)
* [F403LFS](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f403lfs.htm)
* [F001TXF](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f001txf.htm)
* [F070EMP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070emp.htm)
* [F080ISV](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f080isv.htm)
* [aqui](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/devolucao_proporcional.htm)
* [Recalcular(M)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f440gne.htm#Recalcular)
* [RecNfcDev](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#RecNfcDev)
* [F051DIS](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f051dis.htm)
* [Parâmetros da Filial para Compras](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070fcp.htm)
* [F095CAD](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f095cad.htm)
* [Redução do ICMS na base de PIS / COFINS](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/manuais_processos/suprimentos/reducao-pis-cofins.htm)
* [F001TVE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f001tve.htm)
* [Processo de Vendas para Entrega Futura](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/processo-vendas-entrega-futura.htm)
* [Siscoserv](https://documentacao.senior.com.br/gestaoempresarialerp/7.0.0/index.htm#compliance/siscoserv/introducao.htm)
* [Admissão Temporária](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/manuais_processos/suprimentos/admissao-temporaria/processo-admissao-temporaria.htm)
* [conta e ordem](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/processo-conta-ordem.htm#2)
* [Nota Fiscal de Retorno – Notas Fiscais Compra – Itens (F440NCI)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f440nci.htm)
* [Transações de Estoques (F001TES)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f001tes.htm)
* [F113COA](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f113coa.htm)
* [Registros C100, C170 e C190](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/sped/fiscal-icms-ipi/bloco-c.htm#C170)
