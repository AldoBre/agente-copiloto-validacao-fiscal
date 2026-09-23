# Compras 2

> **Fonte:** F070FCP - Parâmetros da Filial para Compras — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070fcp.htm  
> **Trilha:** Ajuda por telas > Cadastros > Filiais > Parâmetros por Gestão  
> **Telas citadas:** E009PPE, E075PRO, E095HFO, E099USU, E405SOL, E410COT, E410CPE, E410LCO, E420OCP, E440CDV, E440HAR, E440NFV, E460CTR, F000DLA, F000DLS, F000INE, F001TCP, F008CEP, F009PPE, F070FCA, F070FCP, F070FVE, F070PSE, F099UCP, F115COE, F115TRF, F207RRP, F211ADA, F301BAA, F403FPR, F410CEA, F410COS, F420APR, F420GOC, F425FOA, F426CEQ, F435CCC, F435CCT, F435COS, F435CST, F435MDT, F439FIX, F440CNF, F440GNE, F440NOR, F440VAL, F460CXO, F460PFO, F460REA, F461GNC  
> **Identificadores de regras:** CPR-435TNSFO01, CPR-435TNSFO02, CPR-440SGLOT01

---
Limite % Variação Peso

Valor limite para o percentual de variação de peso informado nas telas de controle de
entradas e saídas (F435CCC, F435CST, F460PFO e F435COS).

Utiliza Fracionamento NF Entrada

Indicativo se a rotina de fracionamento de produtos do módulo de estoques deverá ser
chamada no fechamento das notas fiscais de entrada.

Valor máximo NF s/ doc. de origem (Contrato/OC)

A consistência de valor máximo sem documentos de origem (Contrato/OC) exibirá a seguinte mensagem no fechamento da nota fiscal de entrada:  
**Não é permitido fechar Notas Fiscais com valor financeiro acima de ???,??. É necessário que seja via documento de origem (Contrato/OC)**.  
Isso ocorrerá nas seguintes condições:

* Existir valor no parâmetro da filial compras MnfSoc - Valor máximo permitido para notas fiscais sem documento de origem (Contrato/OC);
* A verificação de valor máximo sem documento de origem (Contrato/OC) só poderá ser feita se a Aplicação da Operação, que está na transação dos dados gerais, for diferente de R, O, T, D, B, E, C, F, G, X, A. Se nos dados gerais existir transação de produto, usa-se a de produto, caso contrário, usa-se a de serviço.
* Se a nota fiscal de entrada possuir algum item sem documento de origem (Contrato/OC), a verificação será feita.
* A validação é feita pelo valor financeiro, caso não exista, utiliza-se o valor líquido da nota.

Transação Padrão Saída NFe Acerto

Transação padrão do movimento de saída do estoque gerado a partir de uma nota
fiscal de entrada de acerto tipo 9 ou 10.

Excluir Título Previsto OC

Indicativo se deve ser excluído o título de previsão gerado pela ordem de compra,
durante o fechamento de uma nota fiscal de entrada via ordem de compra.  
Este parâmetro será verificado e caso estiver igual a:

* "S - Sim": os títulos de previsão gerados via ordem de compra serão excluídos
* "N - Não": os títulos de previsão gerados via ordem de compra não serão excluídos
* "P - Perguntar": o usuário será questionado se deseja excluir os títulos de
  previsão.

Tipo Busca Número OC

Indicativo de como deverá ser a numeração da ordem de compra, conforme a
lista:

* N - incrementar a partir do último número;
* A - buscar número livre somente nos processos automáticos;
* M - buscar número livre somente nos processos manuais;
* T - buscar número livre em todos os processos.

Valor Máximo de Retenção de INSS

Valor máximo de retenção de INSS para pessoa física. Veja detalhes em Parametrizações do RPA/NF municipal.

Transação OC via Análise Reposição

Transação padrão para a ordem de compra via análise de reposição.

Enviar OC Anexo

Indicativo se a ordem de compra deve ser enviada com anexo.

* "N- Não";
* "S - Sim": formato Html;
* "P- Sim": formato Pdf;
* "X - Sim": formato Planilha de dados.

Enviar Figuras com HTML

Indicativo se devem ser enviadas as figuras do HTML em anexo ao *e-mail* nos processo de
compras. O envio de anexo no corpo do *e-mail* só poderá ser utilizado quando o serviço de
*e-mail*
utilizado é o SMTP, não funcionando quando o serviço utilizado for MAPI.

Dias Antes Aceita OC

Quantidade em dias, anterior ao atual aceito para data de emissão da ordem de compra.

Tipo Retenção

Indicativo de como será efetuado o cálculo das retenções de impostos
(Cofins/PIS/CSLL). Define também a relação com o imposto Outras Retenções:

* "D - Desconsidera": retenções de CSLL /
  COFINS / PIS / Outras Retenções;
* "C - Considera Outras Retenções": como imposto próprio;
* "S - Substitui CSLL / COFINS / PIS": em Outras Retenções;
* "O - Outras Retenções": serão desconsideradas.

Controle Valor Mín. Retenções

Indicativo de onde é feito o controle do valor mínimo de retenção das contribuições sociais (Contas a Pagar ou Compras).

Tipo de Rateio Valor Conhecimento de Frete

Tipo de rateio do valor do conhecimento de frete para efetuar movimento de
estoque (acerto).
O tratamento para todos abaixo é idêntico. Todos devem ser informados obrigatoriamente, lembrando que foram inicializados
com: **V - Valor Líquido**. E podem assumir os valores: **V - Valor Líquido** (valor total do item, já com descontos, acréscimos e impostos) / **B - Valor Bruto** (quantidade x a quantidade unitária do produto, sem considerar descontos) / **P - Peso** / **Q -
Quantidade**.  

A única exceção é que no caso dos campos RVLDAR (rateio do valor de
arredondamento), RVLOUT (rateio do valor de outros) e RVLENC (rateio do valor de
encargos) serão aceitos apenas valor e quantidade pois eles são tratados
para produtos e serviços e não faz sentido ratear os serviços por peso.

**Importante**

Os parâmetros da filial servem somente como sugestão para as
definições do fornecedor, ou seja, no processo de compras vale o que está nas
definições do fornecedor.

Tipo de Rateio Valor de Frete

Tipo de rateio do valor de frete para itens de produto.

Tipo de Rateio Valor de Seguro

Tipo de rateio do valor de seguro para itens de produto.

Tipo de Rateio Valor de Embalagens

Tipo de rateio do valor de embalagens para itens de produto.

Tipo de Rateio Valor de Encargos

Tipo de rateio do valor de encargos para itens de produto.

Tipo de Rateio Valor de Outros

Tipo de rateio do valor de outras despesas para itens de produto.

Tipo de Rateio Valor de Arredondamento

Tipo de rateio do valor de arredondamento para itens de produto.

Credita Desconto Suframa

Indicativo se credita o desconto Suframa nas notas fiscais de entrada.

Transação Sol. Compra - Manual

Transação padrão para as solicitações de compra manuais.

Transação Sol. Compra - Produção

Transação padrão para as solicitações de compra via produção.

Transação Sol. Compra - Automática

Transação padrão para as solicitações de compra via processos automáticos.

Controla Descontos 1, 2, 3, 4 e 5

Indicativo se o controle dos descontos 1, 2, 3, 4 e 5 nas ordens de compra e notas
fiscais de entrada é feito por item ou pro dados gerais.

Considera Parâmetros das Origens NF Frete

Indicativo se deve ser considerada a parametrização dos itens das notas fiscais de origem no fechamento das notas fiscais de frete para crédito de IPI, ICMS, PIS e
COFINS.

Caso a nota fiscal de frete possua uma nota de origem relacionada, ao realizar a valorização de estoque, se existir valor de diferencial de alíquota, esse valor será somado ao valor do movimento de estoque, respeitando a definição desse parâmetro, conforme abaixo:

* "0 - Nunca Considerar": o valor do diferencial de alíquota da nota de frete nunca será considerado no valor do movimento de estoque;
* "1 - Sempre Considerar": o valor do diferencial de alíquota da nota de frete sempre será considerado no valor do movimento de estoque;
* "2 - Perguntar": será realizada uma pergunta ao usuário se deseja considerar o valor do diferencial de alíquota da nota de frete no valor do movimento.

Com o parâmetro definido igual a "1 - Sempre considerar" ou "2 - Perguntar" e na pergunta indicar igual a "S - Sim", as situações tributárias da nota de origem que possui ICMS, PIS e COFINS a recuperar são herdadas para a nota de frete. Se a nota de origem possuir itens com situações tributárias diferentes e que indicam recuperação de ICMS, PIS e COFINS, serão herdadas as situações do primeiro item encontrado.

Importante

A opção "2 - Perguntar" está disponível apenas para telas em que há interação com usuários. Caso seja utilizada para web service, o valor de diferencial de alíquota nunca será considerado no valor do movimento de estoque.

Consistir Data de Entrada NFE

Indicativo se a data de entrada deve ser consistida na digitação ou no fechamento das
notas fiscais. Se o parâmetro for definido igual a "F - Fechamento", o efetivo fechamento da nota fiscal só
poderá ser efetuado quando a data de entrada da referida nota fiscal for igual ou menor
que a data do sistema.

Realizar retorno das OPs ao fechar nota de entrada

Indicativo se deve realizar retorno das O.Ps ao fechar a nota fiscal de entrada de
retorno (tipo 4).

Gera itens por lote

Indicativo se dever gerar os itens controlados por lotes distribuídos na nota fiscal,
de acordo com a quantidade de lotes informada na transferência de itens de produto da
ordem de compra para a nota fiscal de entrada.  

Esta funcionalidade está presente apenas no momento da transferência. Não se
aplica a lotes com máscara de auto-incremento. A transferência sempre herdará os lotes
da ordem de compra (independente do tipo de máscara do lote). Só fará sentido
distribuir os itens na nota fiscal quando houver mais de um lote.

Transação OC para Venda entre Filiais

Transação padrão para geração de ordem de compra (venda entre filiais).

Transação OC para Transferência entre Filiais

Transação padrão para geração de ordem de compra (transferência entre filiais).

**Aceita Dev./Ret. Grupo Empresas**

Indicativo se poderá ou não informar-se notas fiscais de saída de clientes com
código diferente do cliente ligado ao fornecedor, pertencentes porém ao mesmo grupo de
empresas.

**Exige Reaprovação Contrato**

Com o parâmetro ativo igual a "S - Sim", o sistema ao processar o reajuste de contrato,
verifica se o contrato encontra-se aprovado e atualiza o mesmo para que o
reajuste seja analisado novamente pelo processo de aprovação.

Observações

1. Contratos com situação do controle de aprovação Em Análise (E460CTR.SITAPR
   = ANA) ou Aprovados (E460CTR.SITAPR = APR) podem ser alterados pela
   rotina de reajuste de contratos;
2. Contratos na situação do controle de aprovação igual a Em Preparação
   (E460CTR.SITAPR = PRE) não podem ser visualizados na tela F460REA;
3. Quando um contrato já aprovado for reajustado e o indicativo APRRCT
   estiver igual a "S - Sim", a aprovação existente será excluída, e um novo controle de
   aprovação será gerado com situação inicial Em Análise ou Aprovado, caso não
   existam níveis de aprovação compatíveis.

Desc. Antecipação Histórico Fornecedor

O objetivo deste é levar em consideração os campos % Desconto Títulos
(E095HFO.PERDSC), Calcula Desc.Antecipação (E095HFO.ANTDSC) e Tolerância
Desc. Antecipação (E095HFO.TOLDSC) na geração de títulos para o contas a pagar,
no fechamento da nota fiscal de entrada caso este indicativo esteja igual a "S - Sim".
O padrão no sistema é herdar estas informações da condição de pagamento, se
existirem.
O campo foi inicializado com valor "N - Não".  
Sempre que for informado o Percentual de Desconto da parcela da
nota fiscal de entrada, será ignorada a busca nas definições do fornecedor, independente da configuração do novo parâmetro, conforme ocorre nos
processos de vendas.

Consistir chave eletrônica da nota fiscal

Quando marcado igual a "S - Sim", verifica a chave tanto da nota fiscal eletrônica como do conhecimento de transporte eletrônico.

Estado de inicialização da Ordem de Compra

Servirá para informar ao sistema em que estado as ordens de compra manuais (individual e agrupada) deverão ser criadas,
podendo assumir os valores: "PRE - Preparação" ou "ANA - Análise". Também é utilizado pelo Gestor Senior no processo de Ordem de Compra.

Cancelamento de ordem de compra

Permitir que o usuário possa escolher entre três opções no cancelamento de uma
ordem de compra. O valor padrão é a opção 1 - Cancelar Cotação e Solicitação. Opções possíveis:

* **Cancelar Cotação e Solicitação**:
  caso o usuário selecione esta opção, as rotinas continuarão realizando as
  operações que eram feitas até o momento, ou seja, a ordem de compra ficará
  com situação cancelada (E420OCP.SitOcp =  5). A Cotação vai para
  finalizada (E410COT.SITCOT = 4) e não pode ser usada novamente porque fica a
  ligação na tabela E410LCO (ligação com a ordem de compra). A Solicitação
  permanece em situação Cotação (E405SOL.SITSOL = 1 ), não podendo ser
  reutilizada.
* **Liberar Cotação e Solicitação**:
  caso selecione esta opção, as rotinas atualizarão a situação da ordem de compra deixando em situação cancelada (E420OCP.SitOcp = 5) e serão executadas as seguintes operações:
  + As ligações com a ordem de compra serão excluídas (E410LCO - Ligação com a ordem de compra) e será verificada a procedência da ordem de compra (E420OCP.PRCOCP).   
    Sendo igual a **3 - Via Cotação**, serão executadas as seguintes operações:
    - A cotação vinculada à ordem de compra terá os seguintes campos atualizados (E410COT - Cotações - Preços dos Produtos e Serviços):
      * Situação da cotação (SITCOT) = 3 - aprovada;
      * Número ordem compra (NUMOCP) = 0;
      * Filial ordem compra (FILOCP) = 0;
      * Hora geração ordem de compra (HOROCP) = 0;
      * Usuário geração ordem de compra (USUOCP) = 0;
      * Data geração ordem de compra (DATOCP) = 0.
    - A solicitação vinculada a cotação terá o campo quantidade aprovada ordem compra (E405SOL.QTDAPR) = 0
  + Sendo a procedência igual a **9 - Via Solicitação de Compra**, serão executadas as seguintes operações:
    - Serão excluídas as parcelas vinculadas a cotação (E410CPE - Cotações parcela de entregas)
    - Serão excluídas as cotações (neste caso são cotações automáticas geradas para controle interno)
    - Serão liberadas as solicitações que estão vinculadas a itens da ordem de compra com situações em: "1 - Aberto Total", "5 - Cancelado" e "9 - Não fechado" para que sejam cotadas novamente. Caso houver a necessidade de não liberar os itens da ordem de compra com situação "5 - Cancelado", o parâmetro global LibIteCan dever ser parametrizado para "N - Não".
    - Os seguintes campos da tabela E405SOL - Solicitações de Compra (Dados Gerais) sofrerão atualizações:
      * número da cotação (NUMCOT) = 0;
      * quantidade aprovada (QTDAPR) = 0;
      * situação solicitação (SITSOL) = 3 - finalizada;
      * tipo integração (TIPINT) = 4 - aprovado.
* **Perguntar**: caso o usuário selecione esta opção, as rotinas irão questioná-lo como deve
  proceder no momento que for realizar o cancelamento da ordem de compra.
  + Esta opção não é considerada quando o cancelamento da ordem de compra acontece no Gestor Senior. Mo momento da integração, não há interação com o usuário e, com isso, apenas as opções "1 - Cancelar Cotação e Solicitação" e "2 - Liberar Cotação e Solicitação" são válidas.

Os tipos "2 - Liberar Cotação e Solicitação" e "3 - Perguntar" somente
funcionarão ao proceder o cancelamento pelos dados gerais da ordem de compra.

Estado de inicialização da Cotação de Preço 

Informa ao sistema em que estado as cotações de preço manuais
(individual e agrupada) deverão ser criadas, podendo assumir os valores: "
PRE - Preparação" ou "ANA - Análise".

Considera prev. entrega no agrup da OC via Solic

Padrão de configuração é igual a "N - Não". O
objetivo é informar se dentre os campos considerados para agrupamento de
itens iguais será adicionada a Previsão de Entrega.

Compensação de títulos na Devolução

O objetivo é indicar se a transação permite a compensação de títulos nas notas
fiscais de devolução (tipos 2 e 3).  
Se definido igual a "S - Sim", será exibida, ao final do processo, a mensagem Foram
gerados títulos no contas à receber referentes a esta nota fiscal. Deseja chamar
a tela de baixa por créditos?[Sim,Não]. Em caso afirmativo, será exibida a tela
de baixa por créditos do Financeiro F301BAA apenas com os títulos da nota.
Este campo por padrão receberá "N - Não". Além do parâmetro deverão ser atendidas
a condições:

* O valor financeiro da nota fiscal deverá ser maior do que 0 (zero)e na
  pasta parcelas da nota fiscal de entrada deverá haver os títulos na
  Guia;
* A transação utilizada precisa estar integrada com uma transação do contas
  a receber e o campo Soma para Financeiro deverá estar definido igual a "S - Sim".

Aceita somente dia útil entrega OC

Objetivo é informar se dentre os campos considerados para agrupamento de itens
iguais será adicionada a Previsão de Entrega.
Padrão de configuração é "N - Não".
Nas rotinas de geração automática de ordem de compra, foram criadas
consistências para que a data a ser sugerida passe pela seguinte validação:
se o parâmetro estiver definido igual a "S - Sim", não aceitará sábados, domingos e
feriados (conforme cadastro no CEP do fornecedor), sempre postergando a
data de forma a encontrar um dia da semana útil.

Depósito para entrada por transferência

Deverá ser informado qualquer depósito desde que esteja ativo e cadastrado no sistema.
Será utilizado no procedimento para a geração de notas fiscais de entrada por
transferência a partir de notas fiscais de saída

Estado inicial da nota fiscal por transferência

Estado inicial da nota fiscal de transferência (ESTNFT), no qual poderá ser informado apenas “1 - Digitada” ou “2 - Fechada”. Esse parâmetro é utilizado no procedimento de geração de notas fiscais de entrada por transferência a partir de notas fiscais de saída.  
Para parametrizar o estado inicial da nota fiscal por transações, utilize o campo Estado inicial da nota fiscal por transferência na guia Outros da tela Transações de Compras (F001TCP).

Consiste Contrato Abastecimento

Indicativo se deve ser feita a consistência do contrato de abastecimento na
geração das compras (cotação e ordem de compras). Opções disponíveis:

* "C - Cotação": a consistência ocorrerá
  apenas nas telas de cotação;
* "O - Ordem de compra": ocorrerá
  apenas nas telas de ordens de compra;
* "A - Ambos": ocorrerá tanto para
  cotação, quanto para ordem de compra;
* "N - Não consiste": nenhuma
  consistência será feita.

Este parâmetro tem o objetivo de bloquear compras via cotação manual e ordem de
compra manual, ou seja não permitir a geração destas.
O bloqueio da geração irá ocorrer sempre que houver um contrato de abastecimento
com saldo de item, ou seja, caso o usuário esteja tentando utilizar um produto
ou serviço que esteja em um contrato tipo 9 (comercial de abastecimento) da
empresa/filial ativa, se neste item do contrato existir saldo de quantidade, se
o contrato estiver ativo, se consistir quantidade (consiste quantidade = S) e
estiver dentro do período de vigência, irá ocorrer o bloqueio, que ocorrerá da
seguinte forma:

* Tela F410CEA e F410COS: A consistência ocorre ao tentar cotar o
  produto/serviço utilizando-se dos botões Cotar e Cotar Agr. após o item
  estar selecionado;
* Tela F420GOC:
  A consistência ocorre ao tentar inserir o produto/serviço na ordem de compra,
  ocorre na saída do campo derivação para os produtos e na saída do campo serviço
  para os serviços.

Mensagem do bloqueio: Não é possível utilizar este produto/derivação (ou
serviço) pois o mesmo está inserido em item de contrato de abastecimento,
onde o qual) ainda possui saldo de quantidade para geração de ordens de compra
(quantidade utilizada para geração de ordens de compra menor que a quantidade do item do
contrato)!

Observação

Quando não for informado o código do produto ou serviço e sim um
complemento para os mesmos no contrato e/ou na solicitação, os mesmos não serão
considerados nesta consistência, somente se existir o código do produto ou do
serviço.

Validar existência da contagem

Indica se deve ser avisado que a contagem já existe ou não ao informar o número da contagem na tela
F440CN. Caso a opção seja "N - Não", sempre que informar uma
contagem irá incluir na contagem existente os procedimentos informados. Este
parâmetro será inicializado com a opção "P - Perguntar".

Trat. defeitos/excedente conferência

Indica se permite tratamento de defeito/excedente na rotina de conferência da
contagem F440CNF (veja mais detalhes no ajuda desta tela para os campos
abaixo).
Os campos abaixo estão diretamente ligados ao campo trat. defeitos/excedentes
conferência e ficarão habilitados para receber informação se informada a
opção "S - Sim", caso contrário serão limpos e desabilitados:

* Depósito transferência defeito contagem (DepDef);
* Transação defeito contagem (TnsDef);
* Depósito excedente acerto contagem(DepAct);
* Transação acerto contagem (TnsAct).

**Substitui data prev ent dos itens da OC**

O objetivo é substituir a data de previsão de entrega de todos os itens da
ordem de compra (produto e serviço) no momento que for efetuada a última
aprovação pendente no controle de aprovação multinível:

* Se o parâmetro estiver igual a "N - Não", a previsão de entrega dos itens de uma
  ordem de compra se dá pelo resultado do cálculo (data de emissão + prazo de
  entrega do fornecedor), como já era realizado anteriormente e não há recálculo da data prevista para entrega. Neste caso, o sistema assume a data calculada inicialmente;
* Se estiver igual a "S - Sim", no momento da última aprovação para o
  documento em questão, o sistema irá alterar a data de previsão de entrega de
  todos os itens da ordem de compra utilizando a seguinte lógica: (data atual +
  prazo de entrega do fornecedor).

Observação

Esta alteração implica em queda de desempenho nas rotinas citadas no
momento em que a última aprovação pendente é efetuada e o parâmetro estiver igual a "
S - Sim".

Utiliza Preço Normal

Indicativo se utiliza preço normal em tabelas de preços de compras.

Fechar Ordens Ana. Rep. Dep. Filial

Indicará se as ordens de compras geradas a partir da tela F211ADA (botão
Análise) serão fechadas ao final do processo:

* Estando definido igual a "N - Não", ao final do processamento
  será exibida a mensagem: "Deseja abrir a tela de fechamento agrupado de ordens de
  compra?";
* Caso definido igual a "S - Sim", a tela F425FOA será aberta com as
  ordens de compra carregadas.

Moeda para OC recebimento Mat. Prima

Informar a moeda que será utilizada para definir o preço de balcão utilizado
na rotina de controle de entrada/saída via balança. 

Percentual da Moeda OC

Informar o % que será utilizado compor o preço de balcão (preço unitário)
aplicado na entrada do caminhão na rotina de entrada/saída via balança. Este campo tem preenchimento obrigatório sempre que for informada uma
moeda no campo acima.

Condição Pagamento Fixação

Condição de pagamento padrão a ser aplicado na rotina de fixação de preços (F439FIX).

Transação Fixação

Código da transação a ser aplicada no título gerado para o contas
a pagar na fixação no controle de entrada/saída via balança.

Tipo Título Fixação

Código do tipo do título a ser gerado no titulo da fixação para o controle
de entrada/saída balança.

Transação Royalty

Código da transação a ser aplicada no título gerado para o contas a pagar na
fixação no controle de entrada/saída via balança.

Tipo titulo Royalty

Código do tipo do título a ser gerado no titulo da fixação para o controle
de entrada/saída balança.

Utiliza dados bancários fornec. nos títulos da OC

Indicativo de gravação dos dados bancários (banco, agência e conta) na
geração dos títulos de previsão da ordem de compra. Será seguida a seguinte
ordem:

* Primeiramente serão utilizados os dados informados nas parcelas do documento
  (no caso da ordem de compra não existe, apenas na nota fiscal de entrada);
* Senão, caso exista algum favorecido ligado nas definições do fornecedor serão
  sugeridos os dados do favorecido;
* Por último, serão sugeridos os dados informados nas definições do fornecedor.

**Observação**

A forma de pagamento somente será gerada no título da ordem de compra, se este campo estiver informado igual a "S - Sim".

Gera débitos de comissão na ent de NF devolução

Ao fechar uma Nota Fiscal de Devolução com esse parâmetro definido como “S – Sim”, o sistema gerará o débito (estorno) de comissão. O valor do débito será calculado proporcionalmente ao valor total devolvido na nota.

Importante

Ao gerar uma nota de devolução antes da baixa do título ou quando o título já possui alguma baixa parcial, pode ocorrer a existência de um débito de estorno de comissão antes mesmo da geração de um crédito, ou ainda um débito superior ao crédito existente. Esse comportamento é esperado, pois, na modalidade de comissão por recebimento, os valores de créditos e débitos se equilibram somente após a baixa total do título.

Em resumo, se o campo Gera débitos de comissão na ent. de NF devolução estiver configurado como S - Sim, o sistema sempre gerará o movimento de estorno de comissão, independentemente da situação ou dos valores do título.

Valor util. atualiz. saldo de contratos nas NFEs

Indicativo do valor que deve ser utilizado para atualizações de saldos de
contratos financeiros com saldo (contratos tipo 10).

N.F. Origem dig. nos conhecimentos de transporte

Indicativo se será aceita a ligação de notas fiscais de entrada na situação "1 - Digitada" em notas de tipo "8 - NF Frete/Serviços Agregados. Se estiver igual a "N - Não", ao processar uma nota de frete na tela F000INE será verificado se a nota fiscal de origem está fechada e caso não estiver, o processamento será bloqueado.

Fecha conhecimento transp. no fec. N.F. Origem

Indica se o conhecimento de transporte deverá ser fechado automaticamente quando
uma nota fiscal de origem ligada estiver sendo fechada.

Transação Desc. Classificação Entrada

Informar uma transação de entrada de estoque na condição de permitir a movimentação de estoque, da quantidade descontada da
classificação que não gera sub-produto informada na guia Classificação, da tela F435CCC. Para
que esta movimentação possa ser realizada, deve-se utilizar o parâmetro global  IndMovDsc com a
informação igual a "S - Sim".

Agrupar distrib. de Coleta item de OC. existente

No parâmetro, apenas os valores "S - Sim" e "N - Não" poderão ser atribuídos. O
padrão será "N - Não" e quando estiver igual a "S - Sim", ao invés da rotina F426CEQ gerar novos
itens de ordem de compra no processamento conforme padrão, as distribuições
serão agrupadas em um único item de ou das ordem de compra já existente, quando
se tratar de um mesmo produto/derivação, sendo que este agrupamento irá ocorrer
para os três tipos de ordens de compra possíveis de serem geradas (rota,
produtor e transportador).

Gerar Log Tab. Preço Compras

Indicativo se ao alterar informações nos itens de produto das tabelas de
preços de compras, o sistema deve ou não gerar *LOGs* das alterações
efetuadas.

Tipo Busca Número Cotações

Indicativo do tipo de busca da numeração de processo de cotações. Poderá
receber:

* "N - Normal - Incrementar a partir do último número";
* "T - Buscar
  número livre em todos os processos".

**Nota**

O campo Tipo Busca Número Cotações  não é levado em consideração quando existe integração com o COTEI.

Herdar as observações das OC para a NFE

Indicativo se o sistema deve herdar as observações das ordens de compra
para a nota fiscal de entrada.

Permite Inativar Contrato financ. com títulos

Indicativo se permite inativar um contrato financeiro que possui títulos gerados.

* "N - Não": Permite inativar contrato tipo "3 - Financeiro" e "4 - Financeiro
  adicional". A situação no contrato estará desabilitada;
* "S - Sim": Será permitido inativar um contrato do tipo "3 - Financeiro" e "4 - Financeiro
  adicional". Ao inativar um contrato do tipo financeiro será
  questionado se o mesmo deverá baixar os títulos efetivos ou não.

Observação

Para alterar o situação de um contrato de compra é necessário que o usuário
utilize o parâmetro (E099USU.CPRACC - Indicativo se o usuário pode alterar a
situação do contrato de compra deve estar igual a "S - Sim").

Exibe pergunta na exclusão de tit. efetivos na OC

Indicativo se o sistema deve ou não fazer o questionamento se o usuário
deseja reabilitar ou cancelar a ordem de compra excluindo os títulos efetivos da
mesma.

Tratar divergência a menor

Indicativo de tratamento de divergências a menor nas conferências de
contagem. Quando igual a "S - Sim", automaticamente
desmarca e desabilita a coluna Devolver na tela de conferência e ajusta o item
da nota fiscal de entrada para a quantidade efetivamente recebida.

Tratar divergência a maior

Indicativo de tratamento de divergências a maior nas conferências de
contagem. Quando igual a "S - Sim", automaticamente desmarca e desabilita a coluna Receber e
Ent. Exc. na tela de conferência. A opção Devolver já encontra-se
desabilitada quando a divergência é a maior. Não haverá ajuste da nota fiscal
original digitada. Não haverá movimento de estoque da entrada de excedente. Será
apenas gravado um registro de divergência (E440CDV) informando sobre o
fechamento da nota de origem e da não geração da nota de acerto tampouco do
movimento de estoque de excedente.

Estado de inicialização da nota fiscal de entrada

Indica se a nota fiscal será gerada com a situação do controle de aprovação
(E440NFV.SITAPR) como "PRE - Em preparação" ou "ANA - Em análise". A situação
PRE indica que uma nota fiscal de entrada encontra-se digitada, porém ainda
pretende-se continuar a digitação e quando finalizado este processo será
necessário clicar no botão Liberar, o que alterará a situação de aprovação
para ANA. Neste momento o referido botão será alterado para Aprovar e a nota
fiscal está apta à aprovação.

Considerar red.base no cálculo do ICMS import.

Indicativo se deverá considerar a redução na base de cálculo de ICMS na
notas fiscais de importação.

**Manter ICMS OC na NF**

Indica se o ICMS do item da NF será mantido com o mesmo valor da Ordem de Compra. Tendo neste campo a informação "N - Não", o ICMS do item da NF
terá o mesmo valor das tabelas E009PPE ou E009PPE.

Fornecedor Curso

Indica o fornecedor padrão para a compra de cursos online.

Calcular diferencial de alíquota

Define o cálculo do diferencial de alíquota utilizado em notas fiscais de
entrada. Possui as opções:

* "N - Não": o cálculo do diferencial de alíquota não será
  efetuado;
* "S - Operações de imobilizado, uso e
  consumo e frete": o cálculo será realizado como atualmente, somente para
  operações de ativo imobilizado, uso e consumo e frete;
* "T - Todas as operações": a filial irá calcular o diferencial de
  alíquota para qualquer aplicação da transação, desde que a transação esteja
  configurada para calcular o diferencial de alíquota.

% Limite Mín. para Calcular Diferencial Alíquota

Percentual de limite mínimo da diferença entre a alíquota interna e a alíquota interestadual para calcular o valor do diferencial de alíquota. Ao informar um valor para esse campo, não será calculado o diferencial de alíquota (alíquota interna - alíquota interestadual) quando esta diferença for igual ou inferior ao valor percentual informado. O campo ficará habilitado, caso o campo Calcular diferencial de alíquota esteja com o valor igual a "T - Todas as operações".

For. do Simples nacional calc. dif. alíquota

Define se o cálculo do diferencial de alíquota será efetuado para fornecedores
do Simples Nacional.
Será inicializado com a opção "N - Não".
Caso este parâmetro estiver definido igual a "S - Sim" e o fornecedor for do Simples Nacional e não possuir base e valor de ICMS, será calculado um valor de ICMS com alíquota básica para a entrada interestadual (esta alíquota será a que estiver cadastrada no
parâmetro do estado do fornecedor na tela F009PPE), tendo como base este valor no momento do cálculo do diferencial de alíquota. Esta situação será aplicada para a nota fiscal de entrada que possuir base e valor de ICMS, utilizando estes valores como base para o cálculo do diferencial de alíquota para fornecedores do Simples Nacional, considerando o parâmetro Calcular diferencial de alíquota.

Valor Máx. Arredondamento

Define qual o valor máximo de arredondamento da nota fiscal de entrada
efetuada através do web service. Ao alterar o valor desse campo, é
gravado o histórico de alteração na tabela de Compras - Notas Fiscais de Entrada - Histórico de arredondamento (E440HAR).

Forma de Rateio para AFRMM

Este campo define como será realizado o rateio do Valor do AFRMM (Adicional ao Frete para Renovação da Marinha Mercante) nas Ordens de Compra e Notas Fiscais de Entrada, sendo que

* "1 - Valor Líquido";
* "2 - Valor Bruto";
* "3 - Peso";
* "4 - Quantidade".

Trans. NFS Dev. Balança

Seu preenchimento será levado ao campo **Trans. NFS Dev**.
(disponível apenas sem a proprietária do Agronegócio), na tela
F115COE. Caso não informada
segue o comportamento antigo.

Pré-entrada na pesagem (disponível apenas com a
proprietária do Agronegócio)  
 Permite realizar uma pré-entrada na tela F435CCC, antes da
pesagem inicial do caminhão. Na tela, ocorrerá os seguinte:

Primeiro o operador realiza o cadastramento dos dados iniciais (campos do cabeçalho);  
Depois, essa informação é processada e podem ser efetuadas outras entradas;  
Quando necessário, a entrada pode ser reaberta para receber as demais informações (peso inicial, classificação, etc).

Caso este campo seja preenchido com Não, não há o processamento dos dados iniciais, ou seja, a entrada é efetuada com o peso inicial do veículo.

Pós-Saída na pesagem   
Disponível apenas com a
proprietária do Agronegócio. Caso seja preenchido igual a "N - Não", será possível gerar o Ticket ao finalizar a entrada, dessa forma, o recebimento permanece com a situação
5 - Aguardando Fechamento (pós-saída) e sua manutenção deve feita através da tela F435MDT.  
Para/ao preencher o campo igual a "S - Sim":

* Sempre será gerada a Nota Fiscal na tela F435CCC e será possível deixar o documento em situação de pós-saída antes de emitir a nota fiscal;
* O Processo de pesagem poderá ser fechado na tela
  F435CCC, apenas se o
  usuário estiver autorizado na tela F099UCP, no
  campo Permite liberar pós-saída.
* O campo Doc. Emitir Rec. na tela F099UCP deve estar preenchido com Escolhe entre Ticket ou Nota para que a pós saída seja configurada.

Permite múltiplas entradas na Pesagem   
Disponível apenas com a
proprietária do Agronegócio. É habilitado para preenchimento se o campo Pós-saída na Pesagem estiver igual a "S - Sim", ou seja, na geração de Ticket não é possível realizar múltiplas entradas.  
Se for preenchido igual a "S - Sim", permite várias entradas informando a mesma placa, na tela F435CCC.

Observação

Ao informar uma placa que já existe no sistema, será apresentada a mensagem "Existem informações de pós- saída para este veículo. Deseja selecionar a informação?."

* Se a opção "S - Sim" for selecionada será aberta a tela de pesquisa para o usuário selecionar a placa já cadastrada no sistema;
* Se a opção "N - Não" for selecionada o processo ocorrerá como uma entrada normal, mesmo que a pesagem anterior com a mesma placa não esteja finalizada, na tela F435CCC.

Agrupar Itens Fixação

Disponível apenas com a
proprietária do Agronegócio. Se estiver preenchido igual a "S - Sim", na tela F439FIX, será exibida a Guia Itens Agrupados. Essa guia efetua a simulação de agrupamento de ordens de compra para questões de arredondamentos de preço. Se o campo estiver preenchido igual a "N - Não", a guia para agrupamento de itens não é exibida. Além disso, se o campo estiver preenchido igual a "S - Sim", será habilitada a guia de Notas Fiscais de empresas agrupadas e será possível que pessoas jurídicas efetuem a Fixação de Preços, desde que exista pelo menos uma nota de negociação entre empresas e notas fiscais

Informar NF Produtor Fixação

Disponível apenas com a
proprietária do Agronegócio. Se estiver preenchido igual a "S - Sim", na tela F439FIX, serão exibidos os campos abaixo para preenchimento:

* N°. NF Produtor;
* Série NF Produtor;
* Data Ent. NF Produtor.

Obrigar Informar NF Produtor   
Disponível apenas com a
proprietária do Agronegócio. Definição se nas telas F115COE, F115TRF, F435CCC, F435MDT e F439FIX será consistido se foi informado os dados da Nota Fiscal do Produtor. Este possui as seguintes opções:

* "N - Não Obrigar": não impacta no processamento das telas. Esta opção quando selecionada, permite a entrada de cargas de produtores rurais sem a necessidade de notas fiscais;
* "O - Obrigar": obriga que seja informado os dados da Nota Fiscal do Produtor (Chave NFP-e ou Nº da Nota, Série e Data) nas telas descritas;

* C - Obrigar e consistir série: além de obrigar que seja informado os dados da Nota Fiscal do Produtor, consiste se a Série de Produtor informada é válida (segue as regras de validação da SEFAZ).

**Observação**

Na tela de Compras - Controle de Entradas e Saídas - Fixação (F439FIX), os campos para informar a nota de produtor são habilitados apenas se o parâmetro **Informar NF Produtor Fixação** estiver parametrizado igual a "S - Sim". Portanto, deve ser observado conflito de parametrização.

Observação obrigatória ao cancelar OC

Indicativo se é obrigatório informar uma observação ao cancelar a ordem de compra, através do botão Canc. OC da tela F420APR.

Herdar anexos (Req./Sol./Cot./O.C)

Indica se os anexos são herdados no processo de compra (Requisição, Solicitação, Cotação e Ordem de Compra).

Incluir anexos p/ Ordem de Compra

Indica se o anexo é incluído no e-mail enviado ao Fornecedor pela Ordem de Compra.

Incluir anexos p/ Cotação

Indica se o anexo é incluído no e-mail enviado ao Fornecedor pela Cotação.

Tipo Cálculo DIFA

Permite a escolha do tipo de cálculo DIFA para os tipos "Dupla" (Dif Alíquota, Dif. Valor, Dif. Valor por Regime Fornecedor, Dupla c/ aplicação da diferença de alíq. c/ redução de base de cálculo  e C/ desconto do ICMS e alíq. interna por dentro c/ aplicação da diferença de alíq.) ou "Simples".

Caso o tipo "Dupla" seja selecionado, o cálculo do DIFA será diferente ao calcular itens de serviço e produto das ordens de compra e notas fiscais de entrada. Este cálculo é feito conforme a configuração do campo Calcular diferencial de alíquota e o diferencial é o resultado da diferença entre a alíquota interestadual (destacada na nota fiscal de entrada) e a alíquota interna no estado do cliente/comprador.

## Exemplo:

Compra de detergente de SP para o uso na limpeza do escritório em SC:

* Valor da nota: R$ 1.000,00
* Alíquota da nota: 12%
* Alíquota interna SC: 17%
* Diferencial: 5%

Utilizando a opção "2 - Simples", a base do DIFA será a mesma do ICMS Normal, com isso, teríamos R$ 50,00 de DIFA.

Se a mesma operação for feita entre, por exemplo, os estados de SP e RS e o parâmetro estiver com a opção "1 - Dupla Dif. Alíquota", o cálculo é diferente, pois a base do DIFA não é a mesma. Para chegar à base, o cálculo é o seguinte:

* Base DIFA = Base do ICMS - ICMS da Nota / ((100 - Alíquota Interna)/100);
* Base DIFA = 1000,00 - 120,00 / ((100 - 17)/100);
* Base DIFA = 880,00 / 0,83;
* Base DIFA = 1060,24.

Se o parâmetro estiver com a opção "3 - Dupla Dif. Valor":

* Base DIFA = Base do ICMS - ICMS da Nota / ((100 - Alíquota Interna)/100);
* Base DIFA = 1000,00 - 120,00 / ((100 - 17)/100);
* Base DIFA = 880,00 / 0,83;
* Valor do DIFA: 1060,24 \* 17% - 120 = R$ 60,25.

O valor do Diferencial de Alíquota será resultante da aplicação da diferença entre as alíquotas sobre essa base nova, ou seja, 1060,24 \* 5% = 53,01.

### Aquisição de fornecedor do Simples Nacional

No caso de uma aquisição de fornecedor do Simples Nacional, configurando o parâmetro com a opção "4 - Dupla Dif. Valor por Regime Fornecedor" e considerando os dados abaixo:

* Base de cálculo do ICMS = R$ 10.752,69;
* % ICMS Simples Nacional = 2,33%;
* Valor ICMS Simples Nacional = R$ 250,54 (10.752,69 \* 2,33%);
* Alíquota interestadual padrão (exemplo compra de SP) = 7%;
* Alíquota Interna BA = 18%.

O cálculo será feito conforme abaixo:

* Valor da operação sem ICMS = Base de cálculo do ICMS \* (1 - % ICMS Simples Nacional);
* Valor da operação sem ICMS = 10.752,69 \* (1 - 2,33%);
* Valor da operação sem ICMS = R$ 10.502,15;

* Base de ICMS Interna BA (ICMS por dentro) = Valor da operação sem ICMS / (1 - Alíquota Interna BA);
* Base de ICMS Interna BA (ICMS por dentro) = 10.502,15 / (1 - 18%);
* Base de ICMS Interna BA (ICMS por dentro) = R$ 12.807,50;

* % Diferencial de alíquota = Alíquota Interna BA - Alíquota interestadual padrão;
* % Diferencial de alíquota = 18% - 7%;
* % Diferencial de alíquota = 11%;

* Base DIFA = Base de ICMS Interna BA \* % Diferencial de alíquota;
* Base DIFA = 12.807,50 \* 11%;
* Base DIFA = R$ 1.408,83.

O valor do Diferencial de Alíquota será resultante da aplicação da diferença entre as alíquotas sobre essa base nova, ou seja, 1.408,83 \* 11% = **154,97**.

### Convênio ICMS 236/2021

Veja também:

ICMS - Convênio ICMS 236/2021.

Quando o estado destino da operação de aquisição de “Ativo Imobilizado” ou "Uso e Consumo" estiver enquadrado no Convênio ICMS 236/2021, configurando o parâmetro com a opção "10 - Dupla c/ desconto do ICMS e alíq. interna por dentro c/ aplicação da diferença de alíq." e considerando os dados abaixo:

* Valor Base do ICMS: R$ 1.000,00;
* Valor do ICMS: R$ 120,00;
* Percentual de ICMS interna no estado de destino: 20%.

O cálculo será feito conforme abaixo:

* Base DIFA = (Valor Base do ICMS - Valor do ICMS) / (1 - (Percentual de ICMS interna no estado de destino / 100));
* Base DIFA = (1000,00 - 120,00) / (1 - (20/100));
* Base DIFA = 880,00 / 0,80;
* Base DIFA = 1100,00;
* Valor do DIFA = ((Valor Base do DIFA \* Percentual de ICMS interna no estado de destino) / 100) - Valor do ICMS;
* Valor do DIFA = ((1100,00 \* 20) / 100) - 120;
* Valor do DIFA = **R$ 100,00**.

Quando o estado destino da operação de aquisição de “Ativo Imobilizado” ou "Uso e Consumo" estiver enquadrado no Convênio ICMS 236/2021, configurando o parâmetro com a opção "12 - Dupla c/ aplicação da diferença de alíq. c/ redução de base de cálculo" e considerando os dados abaixo:

* Valor base do ICMS sem redução = R$ 1.000,00
* % Redução Base Cálculo Operação (Parametrizado no cadastro do produto (F075pro, campo CodTrd)) = 41,42%
* Base de Cálculo operação = 1000 - ( 1000 \* 41,42%) = 585,80
* % ICMS = 7%
* Valor ICMS = 585 \* 7% = 41,01
* Alíquota interna = 20%
* Percentual de Redução de Base de Cálculo = 72%, cadastrado na tela F070PSE.

O cálculo será feito conforme abaixo:

* Base DIFA = (Valor base do ICMS sem redução - Valor do ICMS) / ( 1 - alíquota interna)
* Base DIFA = (1000 - 41) / ( 1 - 0,20) = 1.198,75
* Base DIFA= Base DIFA \* (Percentual de Redução de Base de Cálculo/100)
* Base DIFA = 1.198,75 - (1.198,75 \* 72%) = 335,65
* Valor do DIFA = Base DIFA \* Alíquota interna
* Valor do DIFA = 335,65 \* 20% = 67,13
* Valor do DIFA = Valor do DIFA - Valor ICMS
* Valor do DIFA = 67,13 - 41,00 = **26,13**

Descontar ICMS Interestadual da base DIFA

Indicativo se deve descontar o ICMS da operação interestadual na formação da base de cálculo do DIFA. Habilitado somente se o campo Tipo Cálculo DIFA for **1-Dupla Dif. Alíquota**, **3-Dupla Dif. Valor** ou **4-Dupla Dif. Valor por Regime Fornecedor**.

Alíquota Base de Cálculo DIFA

Indicativo de qual alíquota deve ser aplicada na formação da base de cálculo do DIFA. Habilitado somente se o campo Tipo Cálculo DIFA for **1-Dupla Dif. Alíquota**, **3-Dupla Dif. Valor** ou **4-Dupla Dif. Valor por Regime Fornecedor**.

Quantidade máxima de tolerância (Para o Agronegócio)  
Este campo define a quantidade (Kg) de diferença de peso permitida entre a nota fiscal do fornecedor pessoa jurídica e o peso apurado na pesagem da balança, no momento de realizar o recebimento de produtos. Veja detalhes na documentação de Recebimento de Produtos > Ajustes no estoque no recebimento de produtos.

Percentual de tolerância(Para o Agronegócio)  
Este campo define o percentual de diferença de peso permitido entre a nota fiscal do fornecedor pessoa jurídica e o peso apurado na pesagem da balança, no momento de realizar o recebimento de produtos. Veja detalhes na documentação de Recebimento de Produtos > Ajustes no estoque no recebimento de produtos.

Enviar IE de Produtor Rural

Indica se a inscrição municipal do produtor rural é enviada no arquivo XML das notas fiscais de compra dos tipos "3 - Devolução (NF de Saída)", "7 - NF Geração Manual" e "10 - NF Acerto (NF Saída)".

Exige Lote/Série NFC

Quando esse campo estiver definido igual a "N - Não", faz com que seja possível informar o lote e a série **somente ao fechar a nota**. Com isso, a tela F000DLS não será aberta após cada inclusão de item na NF, mas sim a tela F000DLA, permitindo informar de uma única vez todos os lotes dos itens inseridos na tela F440GNE. Lembrando que o parâmetro funciona apenas quando a quantidade da NF de entrada for igual à quantidade da NF de saída, caso contrário o sistema faz o processo de recálculo, dessa forma abrindo a tela F000DLS.

Como por padrão o sistema exige a informação de lote e série, isso é útil para casos em que o lote/série do produto só é conhecido no fechamento da nota (por exemplo quando uma pessoa faz o recebimento e outra a conferência). Caso o lote/série tenha sido sugerido via identificador de regras (CPR-440SGLOT01), a tela será aberta com os lotes/séries definidos na regra para conferência.

Soma frete e seguro importação vl. unitário itens

Se este campo estiver preenchido igual a "S - Sim", ao processar a tela Nota Fiscal de Entrada - Valores Diversos (F440VAL), acessada através do botão Valores da tela Nota Fiscal de Entrada Agrupada (F440GNE), e calcular os rateios do frete e seguro importação, os valores calculados serão incorporados ao preço unitário dos itens e os valores dos campos **Valor Frete Importação** e **Valor Seguros Importação** ficam zerados (no item e nos dados gerais). Esse campo possui abrangência por filial.

## Exemplo:

Nota fiscal de importação (NF tipo 7) conforme abaixo:

* Item 1 - Preço Unitário: R$ 50,00 - Quantidade Recebida (QtdRec): 10
* Item 2 - Preço Unitário: R$ 100,00 - Quantidade Recebida (QtdRec): 10
* Frete Importação (VlrFei): R$ 15,00
* Seguro Importação (VlrSei): R$ 0,00
* Valor Total: R$ 1500,00

Valor unitário após o rateio:

* Item 1 - Preço Unitário: R$ 50,50 (Esse valor é 50 (preço unitário) + (5 (VlrFei) / 10 (QtdRec)))
* Item 2 - Preço Unitário: R$ 101,00 (Esse valor é 100 (preço unitário) + (10 (VlrFei) / 10 (QtdRec)))
* Frete Importação: 0
* Seguro Importação: 0
* Valor Total: (50,50 X 10 (QtdRec)) + (101,00 X 10 (QtdRec)) = 505,00 + 1010,00 = R$ 1.515,00

Observação

O cálculo do valor unitário após o rateio de Frete Importação (VlrFei) e/ou Seguro Importação (VlrSei) são da mesma fórmula.

Permite reabilitar requisição

Este campo define se será possível reabilitar requisições já atendidas via processo de compra. Além disso, será possível cancelar ou reabilitar a nota fiscal que atendeu a requisição, mesmo que o processo esteja finalizado. Veja detalhes na documentação das telas F207RRP e F440GNE. Seu preenchimento padrão é "N - Não".  

Esse mesmo processo é atendido pelo web service com.senior.g5.co.mcm.cpr.notafiscalentrada, porta ReabilitaCancelaNota, através do parâmetro Reabilitar Requisição.

Valida Vigência Ctr.

Este campo define se o sistema irá validar a vigência de Contratos ao tentar vinculá-los à Ordens de Compra nas telas F435CCC e F460CXO.

* "N - Não": neste caso, é possível vincular uma ordem de compra a um contrato fora da data de vigência;
* "S - Sim": neste caso, ao tentar vincular um contrato fora da data de vigência, será exibida a seguinte mensagem "O Contrato XX não pode ser vinculado pois está fora da vigência".

Emitir contra nota para o Fornecedor Pessoa Física

Por meio deste campo, é possível configurar o sistema para que não gere a contra nota para o Fornecedor Pessoa Física nas seguintes rotinas:

* Compras - Controle de Entradas e Saídas (Expedição via Contrato com Classificação) (F435CCC);
* Compras - Fixação de Preços (F439FIX);
* Transferência entre Produtores (F115TRF).

Por padrão, o campo será inicializado igual a "S - Sim", mantendo o comportamento normal. Caso seja selecionada a opção "N - Não", o sistema irá se comportar como se o Fornecedor fosse uma Pessoa Jurídica, ou seja, emitindo a sua própria nota fiscal de entrada do tipo 1.

Funcionamento Transação para Recebimento de Grãos

Este campo indica qual será o comportamento da transação utilizada na tela (Compras - Controle de Entradas e Saídas (Expedição via Contrato com Classificação) (F435CCC). A rotina funcionará de acordo com as seguintes opções:

* P - Padrão: será mantido o comportamento original do sistema, sem filtros e sem preenchimentos automáticos;
* A - Preenchimento automático: busca como sugestão, a transação a ser utilizada na apresentação dos registros das guias de contratos. Para isso, a rotina obedece a seguinte ordem de busca:
  1. Com o identificador de regras CPR-435TNSFO01 ativo e os parâmetros de regras preenchidos, será atribuída a transação retorno do identificador;
  2. Caso não retorne e o identificador de regras CPR-435TNSFO02 estiver ativo com os parâmetros de regra, será atribuída a transação retorno do identificador;
  3. Caso não retorne, a busca pela transação será avaliada por contrato, desde que possua uma transação vinculada;
  4. Caso não retorne, a busca será feita pelo campo Transação Recebimento Grãos, na ligação fornecedor x produto da tela de Ligações Fornecedor x Produtos Individual (F403FPR).
  5. E por último, caso não retorne a transação, a busca será feita pela configuração da tela Parâmetros da Filial para Compras (F070FCP), campo Transação Recebimento Grãos.

  Observação

  Para que a sugestão ocorra corretamente, a transação deve ser do tipo de recebimento a fixar, a depósito ou compra imediata. Essa configuração é feita no cadastro das transações de compras (F070FCP) no campo Tipo de Recebimento.
* F- Filtrar Contratos: busca todos os contratos relacionados à transação selecionada. Este campo apresentará os contratos que correspondem à Transação de Recebimento de Grãos, definida na tela (Compras - Controle de Entradas e Saídas (Expedição via Contrato com Classificação) (F435CCC).Para habilitar essa funcionalidade, o campo Funcionamento Transação Recebimento de Grãos da tela de Parâmetros da Filial para Compras (F070FCP), deverá ter o valor F - Filtrar contratos.

**Receber Produto Equivalente**   
Seu objetivo é indicar se a Filial irá receber produtos equivalentes. Será utilizado na rotina de Compra por Princípio Ativo. Por padrão, seu valor é "N - Não".

Transação Recebimento Grãos

Este campo indica como sugestão, a transação que será utilizada ao realizar o recebimento de grãos. Este campo deve ser utilizado quando a transação pelos identificadores de regras não estiver definida, ou quando não houver contratos.

**Origem Código Cidade Tributação ISS**

Determina como será o preenchimento do campo **Código Cidade ISS** da tela F440GNE.

* Se estiver definido como **0 - Filial** (padrão), será sugerido o código definido no campo **Código Cidade ISS** do cadastro da filial (F070FCA) logada na tela;
* Se estiver definido como **1 - Fornecedor**, será sugerido o código definido no campo **Código Rais** da tela F008CEP, a partir do CEP do fornecedor da nota fiscal que está sendo gerada.

Afeta a geração do campo **CodRai** nas seguintes rotinas:

* Compras e Recebimento (F070FCP);
* Agrupada (F440GNE);
* Via Contrato Comercial (F461GNC);
* Via Ordem de Compra Simplificada (F440NOR);
* Web service com.senior.g5.co.mcm.cpr.notafiscal.

Gera Título Fixação com Valor Integral

Indica se o valor original do título deve ser gerado com o valor integral da fixação ou com o valor líquido, atuando para títulos selecionados do Contas a Pagar e Receber. No parâmetro, apenas os valores S - Sim e N - Não podem ser atribuídos, sendo que o padrão é N - Não (valor líquido).

## Exemplo:

Parâmetro definido com N - Não: no processo de fixação, o usuário informa as OCs ou a quantidade que será fixada. Nesse mesmo processo, executado na tela Compras - Fixação de Preços (F439FIX), é possível através da guia de Contas a Receber selecionar alguns, todos ou nenhum título que o Produtor esteja devendo para a Empresa. Caso exista a seleção de títulos nessa guia, os valores correspondentes à dívida do Produtor são descontados do valor que ele receberia no final do processo da fixação:

* Valor que será fixado: 10.000,00 R$
* Valor dos títulos selecionados: 2.000,00 R$
* Título gerado no processo de fixação: 8.000,00 R$
* Valor em aberto do título gerado: 8.000,00 R$

Parâmetro definido com S - Sim: quando houver compensação de títulos, o valor do título gerado da fixação será o total da fixação, mantendo o valor em aberto com as compensações. Seguindo o mesmo exemplo anterior:

* Valor que será fixado: 10.000,00 R$
* Valor dos títulos selecionados: 2.000,00 R$
* Título gerado no processo de fixação: 10.000,00 R$
* Valor em aberto do título gerado: 8.000,00 R$

Permite entrada via balança com ticket sem classificação

Indica se deve permitir a entrada via balança, com ticket sem classificação. Por padrão, seu valor é "N - Não".

Permite Desmembramento de Carga PJ

Indica se haverá o desmembramento do ticket quando a pesagem for maior que a quantidade da nota. Por padrão, seu valor é "N - Não", mantendo o comportamento normal do sistema e, quando definido como "S - Sim", será permitido efetuar o desmembramento da quantidade excedente em um novo ticket.  
Esta funcionalidade somente poderá ser utilizada quando o ticket for originário de fornecedor pessoa jurídica.

Pes. deve ser realizada na U.M. estoque produto 

Indicativo se a pesagens rotinas de balança deve ser efetuada na unidade de medida de estoque do produto (E075PRO.UNIMED) em vez da terceira unidade de medida do produto (E075PRO.UNIME3).

**Importante**

Esse parâmetro impacta no cálculo das quantidades de pesagem informadas, onde:

* Ao configurar para "S", somente considera a unidade de medida de estoque, sem fazer conversões;
* Ao configurar para “N”, efetua a conversão das quantidades entre a “Unidade Medida (Estoque)” e “3ª Unidade Medida”, informadas no cadastro do produto.

Para não haver diferenças de comportamento entre as rotinas, é aconselhável que esse parâmetro seja configurado de forma semelhante ao parâmetro de mesmo nome localizado no cadastro de Parâmetros da Filial para Vendas (F070FVE).

Rotinas onde o parâmetro atua: telas F435CCC, F435CCT, F435CST, F435MDT, F435COS e no web service com.senior.g5.co.int.agr.pesagem, porta RegistrarEntradaManual.

Transação de emissão de contra nota ICMS diferimento   
Permite selecionar as transações do módulo "COF" para a emissão de contra nota em operação com ICMS integral diferido.

**Observação**

Feita a seleção da Transação de emissão de contra nota ICMS diferimento, o sistema verificará se existe integração com algum outro módulo. Se existir, o sistema notificará o usuário, e caso o usuário opte pela opção "Não", o ERP retornará o valor anterior do campo.

Valor base de entrada via balança: indica qual será a base utilizada, caso haja uma diferença de peso entre o recebimento e a nota fiscal do fornecedor, que esteja dentro da tolerância definida. O recebimento será gerado, com base ou pela quantidade das Notas Fiscais, ou pela quantidade líquida da pesagem, conforme preenchido neste campo.

Pes. deve ser realizada na U.M estoque do produto

Este parâmetro define se a pesagem, via telas de entrada e via balança, será feita na unidade de medida de estoque do produto ou se será usada a 3ª unidade de medida do cadastro do produto, seguido de conversão para a unidade de medida de estoque.

* Se estiver marcado como "S - Sim", o sistema entende que a pesagem já está sendo feita na unidade de medida de estoque, então não precisa converter. Não haverá conversão da 3ª unidade de medida do cadastro do produto para a unidade de estoque.
* Se estiver marcado como "N - Não", o sistema entende que a pesagem está sendo feita na 3ª unidade de medida do cadastro do produto, e será necessário converter para a unidade de medida de controle de estoque do produto.

NF Saída em contingência para transferência

Indicativo para permitir a seleção de notas fiscais de saída que estejam com situação "16 - Autorizada em contingência" no processo de geração de notas fiscais de entrada do tipo "11 - Transferência entre Empresas/Filiais".

Integra com o Hub de Royalties

Este parâmetro define se há integração vigente com o Hub de Royalties para a filial. Há duas opções disponíveis:

* **S - Sim**: Filial integra com a Bayer. Portanto, gera pendência de integração e, integra com o Hub de Royalties.
* **N - Não**: Filial não integra com a Bayer. Portanto, não gera pendência de integração nem integra com o Hub de Royalties.

Data Inicial Agrocheck

Permite informar a data inicial da integração com o Agrocheck. Esta data é utilizada para montar as cargas iniciais dos Romaneios (Entrada/Saída/Transferência), ou seja irá montar os registros através desta data inicial até a data atual do sistema.

**Bloqueia Transf. Cred. entre Prod.**

Permite definir, quando ativa a Integração com o Hub de Royalties, a validação a ser executada nos casos em que a quantidade de créditos da origem for insuficiente para a transferência entre produtores, na tela F115TRF. Há três opções disponíveis:

* **B - Bloquear**: Será exibida uma mensagem na tela F115TRF informando ao usuário a insuficiência de créditos e a operação será cancelada.
* **P - Perguntar**: Será exibida uma mensagem na tela F115TRF informando ao usuário a insuficiência de créditos e, perguntando se o usuário deseja continuar ou não a operação.
* **S- Sempre Permitir**: O processo de transferência ocorre normalmente.

**Atenção**

* Caso não seja informado, o parâmetro assumirá o comportamento da opção **B - Bloquear**.
* Após o processamento, caso a transferência tenha ocorrido com pendências, uma mensagem será exibida, informando ao usuário que será necessário acessar o ITS da Bayer para regularizar o produtor.

Controlar certificação dos fornecedores

Indica se a filial realiza o controle da certificação dos fornecedores. Quando ativado, o ERP valida a existência e a validade do certificado tanto na geração da ordem de compra (via diferentes telas ou web services) quanto no processamento e fechamento da OC. Essa validação considera que a digitação da ordem de compra pode ocorrer enquanto o certificado ainda está válido, mas o fechamento pode acontecer em uma data posterior ao seu vencimento.

Transação Canc. titulo Royalty  
Permite armazenar a transação de cancelamento de títulos de royalties gerados em compra imediata com Integração com o Hub de Royalties.

**Observação**

Somente se o campo Integra com Hub de Royalties estiver configurado como S, e a empresa estiver parametrizada para integrar com o Hub de Royalties, é que essa validação será ativada.

## Páginas relacionadas

* [F435CCC](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f435ccc.htm)
* [F435CST](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f435cst.htm)
* [F460PFO](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f460pfo.htm)
* [F435COS](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f435cos.htm)
* [Parametrizações do RPA/NF municipal](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/manuais_processos/suprimentos/rpa/parametrizacao.htm#inss)
* [Gestor Senior](https://documentacao.senior.com.br/seniorxplatform/manual-do-usuario/aplicativo-gestor-senior/)
* [LibIteCan](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#LibIteCan)
* [Transações de Compras (F001TCP)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f001tcp.htm#menu_cadastros/f001tcp.htm)
* [F410CEA](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f410cea.htm)
* [F410COS](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f410cos.htm)
* [F420GOC](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f420goc.htm)
* [F425FOA](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f425foa.htm)
* [F115COE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f115coe.htm)
* [F435MDT](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f435mdt.htm)
* [situação de pós-saída](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/manuais_processos/agronegocio/processos/recebimento/recebimento_passos2.htm#pos-saida)
* [F099UCP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f099ucp.htm)
* [F439FIX](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f439fix.htm)
* [F420APR](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f420apr.htm)
* [ICMS - Convênio ICMS 236/2021](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/impostos-icms.htm#236/2021)
* [F070PSE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070pse.htm)
* [Ajustes no estoque  no recebimento de produtos](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/manuais_processos/agronegocio/processos/recebimento/origem-porto.htm#tolerancia)
* [F000DLS](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000dls.htm)
* [F000DLA](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000dla.htm)
* [F440GNE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f440gne.htm)
* [CPR-440SGLOT01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/cpr_440sglot01.htm)
* [F207RRP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f207rrp.htm#reabilitacao)
* [F440GNE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f440gne.htm#reabilitar)
* [Contratos](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/manuais_processos/agronegocio/processos/contrato/contratos.htm)
* [F460CXO](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f460cxo.htm)
* [Transferência entre Produtores (F115TRF)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f115trf.htm)
* [tipo 1](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/manuais_processos/agronegocio/processos/recebimento/recebimento_passos2.htm)
* [CPR-435TNSFO01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/cpr_435tnsfo01.htm)
* [CPR-435TNSFO02](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/cpr_435tnsfo02.htm)
* [Ligações Fornecedor x Produtos Individual (F403FPR)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f403fpr.htm)
* [(F070FCA)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070fca.htm)
* [F008CEP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f008cep.htm)
* [F070FVE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070fve.htm)
* [F435CCT](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f435cct.htm)
* [com.senior.g5.co.int.agr.pesagem](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/webservices/com_senior_g5_co_int_agr_pesagem.htm)
* [Integração com o Hub de Royalties](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/manuais_processos/agronegocio/integracao-hub-royalties/inicio-hub-royalties.htm)
