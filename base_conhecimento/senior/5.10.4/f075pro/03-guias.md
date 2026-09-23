# Guias

> **Fonte:** F075PRO - Cadastro de Produtos — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075pro.htm  
> **Trilha:** Ajuda por telas > Cadastros > Produtos e Serviços > Produtos  
> **Telas citadas:** E075DER, E075PRO, E210DLS, E815NBP, F000IPR, F000PGS, F012FAM, F013AGP, F015MED, F015UMA, F019ANP, F019TST, F022CLF, F051DIS, F055NRE, F055TPR, F070EMP, F070EPF, F070FVE, F075BAR, F075FCI, F075FPI, F075PRO, F075SFC, F081GTP, F081TPA, F083ORI, F085COP, F113REM, F114CCS, F115CST, F120DPV, F120GPD, F120LPV, F135CCA, F135CMC, F403FPR, F445PRC, F460PFO, F621ACP, F621GCP, F621GPP, F621GPV, F627TSP, F632ACC, F632ACP, F634ACC, F660GDG, F660ISP, F660MIA, F660NFV, F665ICA, F665PAT, F700CMC, F813CNP, F813GNE, F900AQP  
> **Identificadores de regras:** CHA-900CLPOP01, GER-075CACDF01

---
## Guia Dados Gerais

Descrição

Descrição usual do produto.

Família  
Código da família do produto.

Observação

Alguns campos do cadastro do produto são herdados da família como sugestão, sendo que alguns destes podem ser modificados.

Complemento

Descrição complementar do produto.

Descrição p/ Nota Fiscal

Descrição do produto para impressão na nota fiscal.
O conteúdo desde campo é utilizado apenas para impressão de
Notas Fiscais em formulário contínuo. Para a geração de NF-e,
por padrão, é utilizado o campo 
Descrição para gerar da descrição do produto no arquivo XML.

Unidade Medida (Estoque)

Unidade de medida do produto para estoque.

Observação

Para produtos do tipo Comprados e Passagem Direta é possível que a unidade de medida de estoque do produto seja diferente da família,
desde que no cadastro da Origem, o campo Altera Unidade de Medida de Compra/Direto, estiver definido como S (sim).

2ª Unidade Medida

Código da 2ª unidade de medida. Utilizada para componentes na ficha técnica para produtos produzidos.

3ª Unidade Medida  
Código da unidade de medida. Unidade de medida alternativa disponível para outras aplicações, por exemplo nas rotinas que envolvem Balança. Este campo é utilizado nas rotinas de Agronegócio para a entrada e algumas saídas de produto via balança (por exemplo, a tela F115CST), sendo obrigatório a parametrização.
Para utilizar o produto nos Contratos com Fornecedores (F460PFO), é necessário que a unidade de medida possua no máximo três casas decimais. O cadastro da unidade de medida é feito na tela F015MED ou F015UMA.

Utiliza Decimais Cadastro Unidade Medida

Defina se o produto utiliza a quantidade de casas decimais da unidade de medida (F015MED) para arredondamento de valores no momento da integração de produção e estoque (F660ISP).

Unidade Medida (Cálculo de preço)

Campo apenas para indicação visual da unidade de medida base utilizada para o cálculo de preço do produto. Esse valor é herdado do cadastro de produto e exibido no campo UM Calc. Preço das telas F081GTP e F081TPA, sem possibilidade de edição e sem impacto funcional — tratando-se apenas de um campo informativo, sem validações ou regras de negócio associadas.

Observação

Nas telas F081GTP e F081TPA esse campo fica disponível apenas quando o produto Varejo consta na proprietária.

Tipo Produto

Indicativo de tipo de produto.

Classe Produto

Classe do produto. Indica como o produto será tratado comercialmente ou contabilmente na empresa, servindo para filtro em algumas rotinas do sistema:

1. de Estoque: produtos que terão controle de estoques
2. de Passagem Direta: permite efetuar compras, mas não controla estoque, sua entrada na empresa tem destino ligado a um centro de custos.
   Se a transação utilizada na entrada tiver integração com estoques, automaticamente o sistema fará uma saída por requisição. Isto é, ficará registrada
   a entrada e saída do produto, pois este não é mantido em estoques. Este produto não é disponibilizado para vendas
3. imobilizado: para eventuais necessidades de cadastro dos bens da empresa como produto
4. outros para os produtos que não se encaixam nas demais classes.Uma vez cadastrado implementado para que o atributo Classe do Produto não possa ser alterado quando o produto possuir algum movimento de estoque,
   requisição, solicitação de compra ou ordem de compra. Ao alterar a classe do produto será exibido uma mensagem nas seguintes situações:
   * De passagem direta para qualquer outra classe
   * De qualquer outra classe para passagem direta
   * De qualquer outra classe para imobilizado
   * Outros

Origem Produto

Código da origem do produto.Alguns campos da origem são sugeridos para o produto, sendo que alguns destes poderão podem ser alterados.

Máscara Derivação

Máscara da derivação padrão do produto.

Observação

A máscara da derivação do produto está relacionada com a família e é sugerida a partir de Cadastros > Produtos > Famílias não sendo
possível definir uma máscara de derivação no produto diferente da máscara definida na família.

Modelo

Código do modelo para o produto fabricado ou de montagem. Este código é preenchido ao executar a ligação modelo x produto, no módulo engenharia de produto. Não permite alteração.

Liga Roteiro ao Produto

Indicativo se o roteiro informado é utilizado por todas as derivações do produto. Se o roteiro for único para o produto todas as derivações utilizarão o roteiro informado no campo Roteiro do cadastro do produto, que só fica habilitado
nesta opção. Roteiro para cada derivação do produto, neste caso, o roteiro será informado no cadastro da derivação.

Roteiro  
Código do roteiro de produção para produto fabricado. Este campo só é informado se o indicativo Lig. Rot. ao Produto possuir valor S (sim). Não permite alteração.

Qtde Múltipla

Quantidade múltipla para cálculo da geração de ordem de produção/compra. Quando o campo Produto 2ª, 3ª Qualidade ou Reaproveitado for diferente de N (Normal), esse campo não ficará habilitado.

Observação

Quando a empresa fizer uso da gestão de contabilidade, conforme
indicação no cadastro da empresa (F070EMP),
será consistido o preenchimento das contas contábeis e
financeiras conforme segue:

* Será obrigatório informar a conta de receita quando produto tiver indicação que pode ser vendido, não for do tipo Montagem e não for da classe Imobilizado
* Será obrigatório informar a conta de despesa quando produto tiver indicação que pode ser comprado ou requisitado, não for do tipo Montagem e não for da classe Imobilizado
* Será obrigatório informar a conta de estoque/imobilizado quando produto tiver indicação que pode ser comprado ou requisitado, não for do tipo Montagem e não for da classe Imobilizado
* Será obrigatório informar a conta de custo direto quando o produto tiver indicação que pode ser comprado ou requisitado, não for do tipo Montagem e não for da classe Imobilizado
* Será obrigatório informar a conta de custo indireto quando produto tiver indicação que pode ser comprado ou requisitado e não for da classe Imobilizado

Qtde. Mínima

Quantidade mínima de unidades do produto permitido por ordem de produção/compra.  
Na geração das ordens de produção o sistema sempre obedecerá a quantidade mínima do produto definida neste campo, ou seja, mesmo que um pedido ou geração manual de OP tenha necessidade menor que o valor definido neste campo, o sistema irá gerar a quantidade aqui informada.  
Quando o campo Produto 2ª, 3ª Qualidade ou Reaproveitado for diferente de N (Normal), esse campo não ficará habilitado.

Qtde. Máxima

Quantidade máxima para uma ordem de produção ou item da ordem de compra. Ao gerar ordens de produção ou de compras para este produto e a quantidade for superior a essa quantidade, o sistema gera uma nova ordem de produção ou um novo item na ordem de compra. Quando o campo Produto 2ª, 3ª Qualidade ou Reaproveitado for diferente de "N - Normal", esse campo não ficará habilitado.

Observação

Esse processo somente acontecerá para geração de O.Ps via pedido.

Quantidade Múltipla de Vendas

Quantidade múltipla para vendas.

> Observação
>
> * Quando o campo Produto 2ª, 3ª Qualidade ou Reaproveitado for diferente de N (Normal), esse campo não ficará habilitado
> * Este processo somente acontecerá para geração de OPs via pedido

Qtde Guias

Quantidade máxima de guias para a ordem de produção.

Considerar como Montagem

Indicativo se deverá considerar o produto produzido como montagem na busca da estrutura.

Baixa na OP?

Se for componente de algum produto, indica se baixa na O.P. No cadastramento do produto, este campo assume o valor que consta no campo Baixa na OP? do cadastro da família do produto.

Tipo produto para impostos

Permite ao usuário informar o tipo dos produtos para impostos. Para este campo estão disponíveis os seguintes valores:

* 0 - Não Classificado
* 1 - Mercadorias
* 2 - Matérias - primas
* 3 - Produtos intermediários
* 4 - Materiais de embalagem
* 5 - Produtos manufaturados
* 6 - Em Fabricação
* 7 - Subproduto
* 8 - Material de Uso e Consumo
* 9 - Ativo Imobilizado
* 10 - Serviços
* 11 - Outros Insumos
* 99 - Outras

Observação

Quando um produto possui o tipo de produto para impostos diferente, dependendo da filial onde é produzido, a tela Parâmetros por Filial (F075FPI) deve ser utilizada.

Agrup. Estoques  
Código do agrupamento de materiais/produtos para estoques.

Agrup. Produção  
Código de agrupamento de materiais/produtos para produção.

Agrup. Custos

Código do agrupamento de materiais/produtos para custos.

Agrup. Comercial

Código do agrupamento de materiais/produtos para compras ou vendas.

Agrup. Preço

Código de agrupamento de materiais/produtos para preços.

Agrup. Fiscal

Código de agrupamento de materiais/produtos para fiscal.

Classificação Fiscal  
Código interno de classificação fiscal do produto.
Neste campo é possível apenas informar classificações fiscais de
níveis analíticos (com 8 caracteres numéricos XX.XX.XXXX).

Observação

Quando o parâmetro global ExiAtuFis estiver definido como **P - Perguntar** ou **S - Sim** e o campo Indica ligação produto no fornecedor for **S - Sim**, será alterada a Classificação Fiscal na ligação Produto x Fornecedor e a % IPI será atualizado conforme percentual da classificação.

**Importante**

O parâmetro global ExiAtuCes pode ser utilizado para definir se a mensagem **Sugerir o especificador substituição tributária conforme a classificação fiscal?** deve ser apresentada ou não. Por padrão, o valor do parâmetro é **P-Perguntar**. Caso queira que a mensagem não seja apresentada, o parâmetro global deve ser alterado para **N-Não**. Nesse caso, o **Especificador substituição tributária** não será atualizado em relação à classificação fiscal informada no cadastro do produto.

Origem fiscal da mercadoria

Permite informar a origem fiscal da mercadoria. Ao criar novos produtos, o valor é herdado da família (atribuído o valor existente no primeiro dígito do campo Situação Tributária), caso não exista valor informado na família, este campo é preenchido com o valor igual a zero.

Situação Tributária

Código de situação tributária do produto.

% IPI

Percentual de IPI é aplicar no produto.

Observação

Esse percentual será sugerido na entrada de um pedido ou na emissão de nota fiscal de venda. Para notas de compras será sugerido o IPI da classificação fiscal ou então da ligação produto x fornecedor.

Recupera IPI 

Indicativo se o produto recupera IPI.

Tem ICMS 

Indicativo se o produto tem ou não ICMS.

Código ICMS Especial 

Código do ICMS especial.

Código Redução Impostos 

Código da redução de impostos.

Código ICMS Substituído 

Código do ICMS substituído.

Código Substituição COFINS  
Código da substituição tributária do COFINS.

Código Substituição PIS 

Código da substituição tributária do PIS.

Recupera ICMS 

Indicativo se o produto recupera ICMS.

Recupera PIS 

Indicativo se o produto recupera PIS.

Recupera COFINS 

Indicativo se o produto recupera COFINS.

% IRRF Empresa Pública

Percentual do IRRF para empresa pública ou equiparada do produto.

Código fiscal federal 

Código fiscal federal.

Código fiscal estadual 

Código fiscal estadual.

Código fiscal municipal 

Código fiscal municipal.

Tributa PIS

Indicativo se o produto tributa PIS.

Tributa COFINS

Indicativo se o produto tributa COFINS.

Código Tabela Tributação PIS  
Seleção de tabelas de preços com aplicações 3 (Cálculo por Quantidade (Vendas)), 4 (Cálculo por Quantidade (Compras)) e 5 (Cálculo por Quantidade (Ambas)).

Código Tabela Tributação PIS Importação

Código da tabela de preço para o cálculo do PIS importação por unidade de medida.

Código Tabela Tributação COFINS 

Seleção de tabelas de preços com aplicações 3 (Cálculo por Quantidade (Vendas)), 4 (Cálculo por Quantidade (Compras)) e
5 (Cálculo por Quantidade (Ambas)).

Código Tabela Tributação COFINS Importação

Código da tabela de preço para o cálculo do COFINS importação por unidade de medida.

Código Tabela Tributação IPI 

Seleção de tabelas de preços com aplicações 3 (Cálculo por Quantidade (Vendas)), 4 (Cálculo por Quantidade (Compras)) e 5 (Cálculo por Quantidade (Ambas)).

Código Tabela tributação ICMS Monofásico

Código da tabela de tributação do ICMS Monofásico.

**Observação**

As tabelas de preço de PIS/COFINS e IPI informadas no cadastro do produto/serviço permitem que o
Gestão Empresarial | ERP
calcule estes
impostos utilizando base de cálculo por quantidade e alíquota em valor.

A tabela informada deve pertencer a uma aplicação de cálculo por quantidade (3, 4 ou 5)
e deve conter a respectiva alíquota em valor para o produto/serviço. Essa tabela será verificada no cálculo de notas fiscais de entrada, ordens de compra, notas
fiscais de saída e pedidos.

Sit. Trib. PIS Vendas 

Código da situação tributária de PIS Vendas. Se for informado um valor no campo Sit. Trib. PIS Vendas no cadastro de na família, este valor será
sugerido neste campo automaticamente.

Sit. Trib. COFINS Vendas 

Código da situação tributária de COFINS Vendas. Se for informado um valor no campo Sit. Trib. COFINS Vendas no cadastro de na família, este valor será
sugerido neste campo automaticamente.

Sit. Trib. IPI Vendas 

Código da situação tributária de IPI Vendas. Se for informado um valor no campo Sit. Trib. IPI Vendas no cadastro de na família, este valor será
sugerido neste campo automaticamente.

Código de enquadramento

Código do enquadramento legal do IPI.

Prod. 2ª , 3ª Qualidade ou Reaproveitado 

Indicativo se o produto é utilizado para estocar produto de 2ª e 3ª qualidade ou reaproveitado (refugo). É possível gerar ordens de produção, ligar produtos de 2ª , 3ª qualidade ou reaproveitado a um roteiro ou a um modelo.

Produto 2ª Qualidade 

Código do produto associado para entrada no estoque quando o produto for classificado como 2ª qualidade. Quando este campo não for informado, a entrada no
estoque assumirá o produto como 1ª qualidade. Para o controle e movimentação deste produto, o parâmetro O.P. controla Qualidade (2a., 3a.)? no cadastro de Origem deverá estar definido como S.

Derivação 2ª Qualidade 

Código da derivação do produto para completar a definição da 2ª qualidade, quando assim for classificado. Quando este campo não for informado, a entrada
no estoque assumirá o produto como 1ª qualidade.

Produto 3ª Qualidade 

Código do produto para completar a definição da 3ª qualidade, quando assim for classificado. Quando este campo não for informado, a entrada no estoque
assumirá o produto como 1ª qualidade. Para o controle e movimentação deste produto, o parâmetro O.P. controla Qualidade (2a., 3a.)? no cadastro de Origem deverá estar definido como S.

Derivação 3ª Qualidade 

Código da do produto para completar a definição da 3ª qualidade, quando assim for classificado. Quando este campo não for informado, a entrada no estoque
assumirá o produto como 1ª qualidade.

Produto Reaproveitado 

Código do Produto Reaproveitado associado ao
produto titular para dar entrada no estoque de
Sucatas/Rebarbas/Refugos da Produção. Serão efetuadas
entradas no estoque somente quando este campo for
informado. Para o controle e movimentação deste produto, o parâmetro O.P. controla Refugos? no cadastro de Origem deverá estar definido como S. Código da derivação do Produto Reaproveitado, quando assim for classificado.

Derivação Reaproveitado 

Código da derivação do Produto Reaproveitado, quando assim for classificado. Quando este campo não for informado, a entrada no estoque assumirá a derivação do produto de 1ª qualidade desde que a derivação esteja cadastrada para o produto reaproveitado.

Depósito Padrão

Ao cadastrar um novo produto, neste campo será atribuído o depósito padrão da família. Se não informado o campo Família, será atribuído o depósito padrão da origem. Se o depósito padrão da família e origem não forem preenchidos, este campo ficará em branco, sendo permitido cadastrar novo produto com o campo Depósito Padrão sem preenchimento.
Para maiores detalhes, consulte a documentação da tela Sugestão de depósito padrão.

Código Royalty 

Código do royalty para o produto. Este código autoriza o direito de uso de uma marca para comercialização do seu produto.

Produto Kit 

Indicativo se o produto produzido é um Kit com vários produtos agregados para venda.

Material direto 

Indica se o material é direto (produto comprado que é utilizado para fabricação de produtos produzidos).

Produto Misto 

Indicativo se o produto é produzido, mas também pode ser comprado. Neste campo, não será permitido alterar o parâmetro S (sim) para
N (não), se já existir uma nota fiscal de saída ou de entrada para o produto.

Pode Ser Requisitado 

Indicativo se o produto pode ser requisitado (movimento de estoque).

Pode Ser Vendido 

Indicativo se o produto pode ser vendido/faturado.

Pode Ser Comprado 

Indica se o produto pode ser comprado.

Usa Produto X Fornecedor 

Indicativo se ligação produto X fornecedor é utilizada para obter parâmetros fiscais.   
É indicado que os produtos que serão ligados ao fornecedor através da tela F403FPR, tenham este campo definido igual a "S - Sim" em bases que utilizam o processo de geração do grupo fiscal de entrada para integração.

Exige Certificado Classificação 

Indicativo se o produto exige certificado de classificação.  
Usado para o controle de sementes agrícolas.

Emite Guia Tráfego 

Indicativo se é emitida guia de tráfego para o produto.

Soma ICMS/PIS/COFINS ao valor líquido importação 

Indicativo se deve ser somado o valor do ICMS, PIS e COFINS a recuperar no valor líquido das notas fiscais de importação e ordens de compra.

Calcula Desconto Suframa 

Indicativo deve ser calculado o desconto Suframa para o produto nas entradas.

Processo Suframa CBS Zero

 Número do processo na Suframa para CBS zero

% SENAR/SENAT

Percentual do imposto SENAR/SENAT do produto a ser descontado em notas fiscais de saída.Veja mais detalhes na documentação de processos do Senar.

% Funrural

Percentual do imposto funrural do produto a ser descontado em notas fiscais de saída. Veja mais detalhes na documentação de processo do Funrural.

Observações

* O % Funrural já considera o valor do Gilrat em sua porcentagem
* O % Funrural não pode ser inferior ao % GILRAT

% GILRAT

Percentual de Gilrat que compõe a alíquota de Funrural.

Nota Mínima para Fornecimento 

Nota mínima necessária para aprovação de um fornecedor.

Marca do Produto 

Código da marca/etiqueta do produto.

Controle Validade 

Indicativo da forma de controle da data de validade nos estoques.

Situação 

Indicativo de situação do produto. Quando na família do produto, o campo Situação está como I (inativo), todos os produtos/derivações da família.

Gera OP

* S - Produto gera ordens de produção;
* N - Produto não gera ordens de produção.

Observação

Permite alterar o indicativo de N (Não) para S (Sim), mesmo que exista necessidades de produção em aberto com o produto, desde que estas
necessidades sejam provenientes da explosão de origens de produtos sem rastreamento ou para reposição de estoque e com o valor do campo GerOrp igual
a N na tabela Necessidades Produtos (E815NBP). As necessidades de produção com GerOrp igual a N são canceladas automaticamente ao alterar o valor deste campo de N para S, ou seja, não é listada na tela F813CNP;Quando o campo

Gera OP for definido como N (Não), caso este produto for intermediário de um pedido, não será gerado necessidades de produção para ele.
Somente será possível gerar ordens de produção para este, caso for gerado produção para repor estoques.

Filial de Produção 

Utilizada para orientar a geração da ordem de produção na filial indicada.

Na geração de pedido de venda, a filial de produção do produto é gravada no item do pedido, para depois ser usada na geração da ordem de produção do produto. Com isto, no item do pedido já fica registrado que o produto deve ser produzido em outra filial.

Na geração da ordem de produção, o filtro pela filial de produção, é ativado apenas para geração Agrupada. Com ele, é possível selecionar os itens de pedidos vinculados a respectiva filial de produção e assim gerar a O.P. somente para estes itens.

Além disto, a filial de produção quando informada é utilizada:

* 1. Na tela de **Tabelas de Seleção de Produtos para Custos (F627TSP)**: ao processar a seleção de produtos para Custos na tela F627TSP, serão carregados apenas os produtos que têm a Filial Produção correspondente quando informada na tela de seleção.
* 2. Na **geração de pedido previsão para plano produção**: ao gerar o pedido previsão pela tela F120LPV/F120DPV, no item de pedido é gravado com a filial de produção quando informada no cadastro do produto.
* 3. No **processo automático 91 - Calcular FCI (F075FCI)**: na tela de Seleção (F075SFC), se o filtro Filial produção do produto estiver assinalada, serão listados apenas os produtos em que a filial de produção definida no cadastro do produto seja igual a filial de cálculo da FCI.
* 4. Na **geração do cálculo FCI Acabado**: caso o cálculo do FCI seja por filial, no produto que é do tipo produzido e que a filial de produção é diferente da filial do cálculo FCI, ele será processado como comprado.

Identificação Produto

Identificação rápida do produto. Campo informativo da tela, sem qualquer consistência em outras rotinas do sistema.

Tipo de Aferição 

Indicativo do tipo de aferição (conversão de peso do produto)

* P - Afere por produto: será gravado o peso líquido na tabela E075PRO;
* L - Afere por lote: será gravado o peso líquido na tabela de lotes E210DLS.

Quantidade a ser Aferida 

Indicativo da quantidade do produto a ser pesada para aferição (amostra). Este valor servirá como base para o cálculo do peso médio das peças na conversão realizada através da aferição.

Peso Bruto 

Peso bruto do produto. Ao informar ou alterar algum valor nesse campo, o mesmo será sugerido na derivação do produto.

Peso Líquido 

Peso líquido do produto. Ao informar ou alterar algum valor nesse campo, o mesmo será sugerido na derivação do produto.

Toler. Peso 

Tolerância do peso líquido do produto/derivação. Ao informar ou alterar algum valor nesse campo, o mesmo será sugerido na derivação do produto.

Volume 

Volume do produto. Ao informar ou alterar algum valor nesse campo, o mesmo será sugerido na derivação do produto.

Lote Base 

Este campo somente ficará habilitado se a origem do produto controlar por lote. Ao optar por "S - Sim", no momento de
liberar a OP, se o identificador de regras
CHA-900CLPOP01 estiver cadastrado, ativo e ligado a uma regra e o campo Gerar Lote OP na origem
do produto estiver como "S - Na Liberação OP" irá gerar um lote para o produto da O.P..

Base  Recálculo 

Este campo ficará habilitado somente se o tipo de produto for produzido ou comprado.

* A opção N - Não, indica que a quantidade prevista do componente será recalculada quando for
  alterada a quantidade prevista da OP na tela F900AQP
* A opção S - Sim, indica que a quantidade prevista do componente será recalculada quando for alterada a quantidade prevista dos produtos (componentes) da OP

Enquadramento de Produto Específico

Indicativo do enquadramento de produto específico (meramente informativo para NF-e).

Controla valor individual da Série? 

Define se a valorização dos estoques será controlada por série, a opção deste campo somente poderá ser alterado caso as séries do produto não possuam estoque. Para mais informações consulte a documentação
Fechamento dos Estoques - Detalhes.

Classe Cons. Energia/Gás 

Indicativo da classe de consumo de energia elétrica ou gás.

Classe Fornec. Água 

Indicativo da classe de fornecimento de água.

Tipo de ligação 

Indicativo sobre o tipo de ligação elétrica.

Cod. do grupo de tensão 

Indicativo a qual grupo de tensão está enquadrado.

Regime Tributário 

Este campo tem as seguintes opções:

* C - Regime cumulativo
* U - Regime não cumulativo
* N - Nenhum

Estas opções influenciam nos tipos de impostos:

* 41 - PIS Não Cumulativo (SPED)
* 42 - COFINS Não Cumulativo (SPED)
* 43 - PIS Cumulativo (SPED)
* 44 - COFINS Cumulativo (SPED)
* Além da apuração do faturamento na Gestão de Tributos

Exige Montagem?

Define se o produto cadastrado exige serviço de montagem. Campo exclusivo de Varejo. Essa informação é integrada com o Cadastro de Produtos no Retaguarda. Valores possíveis: Não, Sim e Obrigatório. Quando obrigatório, significa que o cliente não poderá levar o produto sem que a montagem seja de responsabilidade da loja.

Exige Entrega?

Define se o produto cadastrado exige serviço de entrega. Campo exclusivo de Varejo. Essa informação é integrada com o Cadastro de Produtos no Retaguarda. Valores possíveis: Não, Sim e Obrigatório. Quando obrigatório, significa que o cliente não poderá levar o produto sem que a entrega seja de responsabilidade da loja.

Agr. Garantia Estendida

Código do agrupamento de garantia estendida. Indica a qual agrupamento de garantia o produto pertence. Essa informação é alimentada no cadastro de produtos e é utilizada para relacionar com a tabela de preços para identificar quais os valores de garantia estendida poderão ser oferecidos para esse produtos.

Usuário Geração 

Usuário que cadastrou a derivação.

Data Geração 

Data em que a derivação foi cadastrada.

Hora Geração 

Data em que a derivação foi cadastrada.

Usuário Alteração 

Usuário que realizou a última alteração na derivação.

Data Alteração 

Data de última alteração na derivação.

Hora Alteração 

Hora de última alteração na derivação.

Base Cálculo Crédito 

Permite definir a natureza da base de cálculo do crédito de maneira customizada para os itens de produto.

Permite Incorporação OP 

Indica se OPs do produto cadastrado permitem ou não a incorporação de
produtos.

**Observação**

Poderá ser alterado para permitir incorporação, se a família também
permitir. Uma vez permitida, só poderá ser alterado para N (não) se
não possuir OP pendente (não finalizada ou cancelada), cujo produto
final seja o em questão, contendo alguma sequência operacional
permitindo a incorporação.

Prazo Recuperação Gar. (em dias) 

Define o prazo de dias que será possível vender uma garantia separada, em outra venda, para um produto de uma venda anterior.

Percentual Limite Incorporação OP 

Define o percentual limite de incorporação de produtos em OPs.

* É utilizado na incorporação de produtos na OP, alertando o usuário se
  a quantidade incorporada (somada a outras quantidades antes incorporadas
  nesta mesma OP) dividida pela quantidade prevista da OP, supera o
  percentual  definido. Porém, o alerta é informativo, não impedindo
  que o usuário confirme a incorporação
* Ao ser definido com o valor 0 (zero), indica que não há limite de
  incorporação
* Poderá ter valor maior que 0 (zero), se o produto estiver configurado
  para permitir incorporação

Motivo desoneração ICMS 

Aceita os valores 0, 1, 6, 9 listados no cadastro de
motivo.

Código Modalidade ICMS 

Código da modalidade para definição da base de cálculo do ICMS. A pesquisa deste campo busca os códigos de substituição/modalidade de ICMS.

* Quando informado um código, a formação da base de cálculo do ICMS normal respeitará o critério de cálculo informado na tela F019TST
* Quando o produto não possuir código de modalidade de determinação da base de cálculo de ICMS, a modalidade informada na NF-e será **3 - Valor da Operação**. Esta é considerada a padrão do sistema
* Quando for informado um código de modalidade com critério **1 - Pela Margem de Lucro**, a modalidade informada na NF-e será **0 - Margem Valor Agregado (%)**
* Quando for informado um código de modalidade com critério **2 - Pelo Preço Unitário Base**, a modalidade informada na NF-e será **1 - Pauta (Valor)**
* Os códigos de modalidade não atendem a opção **2 - Preço Tabelado Máx. (valor)** prevista no manual da NF-e

Indicativo Volume

Indica se o produto é controlado no sistema como sendo um volume. Este valor serve como sugestão no cadastramento da derivação do produto.
Ver ajuda 
produto volume.

Controla Credito ICMS

Define se o produto pode ter o crédito de ICMS reaproveitado na tela F445PRC.

Quantidade meses crédito

 Define em quantas parcelas será pago o crédito de ICMS, ao gerar uma nota fiscal de crédito de ICMS.

Tipo Crédito ICMS

Este campo é habilitado se o campo Controla Crédito ICMS for preenchido com Sim. Seu preenchimento define que tipo de a que tipo de crédito de ICMS o produto pertence, no processo de Crédito do Produtor Rural. Se estiver preenchido com Sim, poderá ser utilizado nas notas fiscais de Crédito, Se estiver preenchido com Não, poderá ser utilizado na notas fiscais de Produção.

% Diferimento

Percentual que será utilizado para o cálculo do valor do ICMS Diferido em cotações, contratos, ordens de compras, pedidos, pré-faturas e notas fiscais de entrada e saída.

Ficha técnica na geração do SPED Fiscal

Este campo somente estará habilitando quando o produto for do tipo Produzido. Ele pode ser preenchido com as opções P - Padrão e R - Real, que determinam a forma de geração do registro 0210 - Consumo específico padronizado, do SPED Fiscal.

Quando este campo não estiver preenchido, o sistema assume como opção a ficha técnica padrão. Quando já existir essa informação no cadastro da família (F012FAM), ela será herdada para o produto se for uma inclusão.

Apresentar produção agrupada bloco K

Defina neste campo se as ordens de produção devem ser apresentadas de forma agrupada na apuração do bloco K, realizada na tela Produção e Estoque (F660ISP).

Tabela de presunção IRPJ

Informar o código da tabela de presunção IRPJ, no qual foi feito o cadastro na tela F055TPR.

Tabela de presunção CSLL

Informar o código da tabela de presunção CSLL, no qual foi feito o cadastro na tela F055TPR.

Emite receita agronômica

Se estiver preenchido com SIM, possibilita a geração e impressão de receita agronômica na tela F113REM. Veja o Manual de processos do Receituário Agronômico.  
Este campo pode ser visualizado apenas com a Proprietária do Receituário Agronômico.

Código de identificação do parceiro

Este campo corresponde ao código de Bula do Agrotóxico, presente na tabela de agrotóxicos do sistema Winfit. Ao encontrar o respectivo código na tabela do sistema parceiro, e informando o valor a esse campo, isso possibilitará a integração das informações do Winfit de geração de bula, sendo elas: a própria bula, as classes do agrotóxico, os tipos de aplicação.
Este campo pode ser visualizado apenas com a Proprietária do Receituário Agronômico.

Especificador situação tributária

Código especificador da situação tributária. No cadastro de um produto novo, será sugerido o CEST informado na tela Classificações Fiscais (F022CLF). Ele tem como objetivo estabelecer a sistemática de uniformização e identificação das mercadorias e bens passíveis de sujeição aos regimes de substituição tributária e de antecipação de recolhimento do ICMS.

**Código princípio ativo**   
Utilizado para o vínculo do princípio ativo ao produto em questão.

* Só poderá ser informado um **Código do Princípio Ativo** para os produtos cujo **Tipo Produto** seja igual a **C - Comprado**
* Não será permitido alterar o **Tipo do Produto** para valores diferentes de **C - Comprado** em registros que já estão com este código informado

Ficha CAT 83/09

Informe neste campo para qual ficha da CAT 83/09 o produto será integrado (F665ICA), conforme parametrizações do seu código de lançamento. As opções disponíveis são:

* Ficha 1A: Controle de materiais
* Ficha 1B: Controle de terceirização
* Ficha 1C: Controle de energia elétrica
* Ficha 1D: Controle de telecomunicações
* Ficha 3A: Controle de produtos acabados
* Ficha 3B: Controle de mercadorias de revenda
* Ficha 5B: Controle de perdas e sobras (reaproveitamento)

**Observação**

Este campo não é de preenchimento obrigatório.

Produto Sob Encomenda

Permite informar se o produto é Sob Encomenda, com as opções de Sim e Não.
Este estará visível caso haja proprietária do Varejo Senior.
Quando integrado com o sistema de
Gestão de Lojas
, será exibido nas telas de Consultas e Cadastros de Produtos.

Código do Dispositivo Fiscal

Código do dispositivo cadastrado na tela F051DIS.

**Cor do produto**

Indicativo da cor do produto

**Voltagem do Produto**

Indicativo da voltagem do produto.

**Derivação do produto**

Indicativo da derivação do produto. Na inserção de uma nova derivação, este campo deve ser sugerido com o valor contido no campo **Voltagem do Produto**.

Ato cooperado

Este campo define se o produto caracteriza movimentos de Ato Cooperado. O preenchimento padrão deste campo é Sim.

Para que a operação (nota fiscais de saída ou entrada) seja considerada como Ato Cooperado, é necessário também, que o fornecedor seja um cooperado ativo (F085COP) e que o campo Ato cooperado esteja preenchido com Sim, nas seguintes telas:

* Cadastro de Famílias (F012FAM)
* Origem de produtos (F083ORI)
* Agrupamento de produtos - produção (F013AGP)
* Ligação entre Fornecedor e Produto (F403FPR)

Este campo pode ser visualizado apenas com a proprietária de Agronegócio (ECCC).

Atenção

Os processos ECCC (Controle do Cooperado) e/ou SRPR (Controle do Produtor), bem como o parâmetro *-e:agro*, não estão mais disponíveis a partir da utilização do sistema no licenciamento por área. Para atendimento das rotinas específicas do Agronegócio, estão disponíveis os parâmetros globais **UtiCtrCoo** e **UtiCtrPrd**, na tela Manutenção dos parâmetros globais do sistema (F000PGS), onde o sistema passa a exigir apenas a existência da liberação das áreas de Mercado e Suprimentos (ou Backoffice, que libera as duas áreas).

* Para informações sobre licenciamento no Gestão Empresarial | ERP, acesse a documentação da tela Definição da Cópia (F000IPR)
* Para informações sobre os parâmetros globais **UtiCtrCoo** e **UtiCtrPrd**, acesse a documentação da tela Manutenção dos parâmetros globais do sistema (F000PGS)

Sujeito internação na ZFM

Identifica se está sujeito ao processo de internação na Zona Franca de Manaus.

Tipo Produto DCI

Identifica o tipo de produto para a Declaração de Controle de Internação.

Identificador Multiplicadores

Informe o código da tabela de multiplicadores para associação aos produtos adquiridos pelo contribuinte, conforme cadastrado na tela Tabela de Multiplicadores para ICMS na Entrada Nacional do Amazonas (F660MIA).

**Calcula Cofins Importação**

Indicativo se o produto Calcula COFINS importação a recuperar em nota fiscal de entrada e ordens de compra.

**Calcula PIS Importação**

Indicativo se o produto Calcula PIS importação a recuperar em nota fiscal de entrada e ordens de compra.

Possui Admissão temporária de tributos

Este campo define se o produto permite o cálculo diferenciado dos impostos contemplados pela Admissão temporária.

* Caso o produto tenha suspensão total, os impostos IPI, PIS, COFINS, Importação e CIDE não são calculados na nota fiscal, mesmo se todos os demais parâmetros do ERP estiverem parametrizados para calcular
* Caso o produto possua suspensão parcial, defina os percentuais e o tempo de permanência. Veja como ocorre o cálculo no manual de processos de Admissão temporária

Código ICMS Antecipação

Esse campo permite informar o código do ICMS Antecipação.

Código de produto da ANP

Indicativo do código do combustível da ANP.
Utilizando o dados cadastrados pela tela Produtos ANP (F019ANP).

Tipo de Combustível

Informe o tipo de combustível. Exemplo: 1 - Biodiesel B100.

Produto Misturado

Informe o código do produto misturado.

Índice de Mistura

Informe o índice de mistura do produto.

Gerar grupo Repasse ICMS ST na NF-e

Indicativo se o produto deve gerar o grupo ICMS ST no arquivo .XML da NF-e. Esse parâmetro é habilitado apenas se o campo Código de produto da ANP estiver preenchido. Se o parâmetro estiver configurado como **Sim** e o produto for vendido em operação com CST 60, ao invés de gerar o grupo ICMS60 no arquivo XML da NF-e, é gerado o grupo ICMSST.

% Gás Natural Nacional

Percentual de Gás Natural Nacional (GLGNn) para o produto GLP.

% GLP derivado do petróleo

Percentual do Gás Liquefeito de Petróleo derivado do petróleo no produto GLP.

% Gás Natural Importado

Percentual de Gás Natural Importado (GLGNi) para o produto GLP.

Valor de partida

Valor de partida do produto GLP. Deve ser informado o valor por quilograma sem ICMS.

Observação

O produto GLP possui código ANP igual a 210203001.

Classificação Convênio ICMS

Código da classificação do convênio ICMS 115/2013. O valor informado neste campo é gerado no campo 14 - Código de classificação do item do registro **I - Itens** do relatório Convênio ICMS 115/2003 (CIAE052).

Tipo de utilização

Tipo de utilização do convênio. O valor informado neste campo é gerado no campo 4 - Fase ou tipo de Utilização do registro **I - Itens** quando for uma nota fiscal do tipo 21 ou 22. E caso seja uma nota fiscal do tipo 06 – Energia Elétrica gera informação do campo Tipo de ligação.

Origem do código GTIN

Indica a origem de busca dos códigos GTIN (cEAN e cEANTrib) na geração dos documentos eletrônicos. Para mais informações, consulte a documentação do GTIN.

Tipo do GTIN

Indica qual o formato do GTIN que será usado na sua apresentação nos documentos fiscais:

1. GTIN8
2. GTIN12
3. GTIN13
4. GTIN14

Ex.: Tipo de GTIN = GTIN8. O GTIN será apresentado com o tamanho 8 nos documentos fiscais. Caso seu tamanho seja menor que 8, ele será preenchido com zeros à esquerda.

Tributação por Vlr. Min. Unidade Medida

Indica se o valor de imposto calculado por percentual deve ser comparado com o valor parametrizado para o item na tabela de tributação por quantidade cadastrada. Quando o campo estiver parametrizado como **S - Sim**, caso o valor calculado seja inferior ao cadastrado na tabela de tributação, será utilizado o valor cadastrado, ou seja, passará a tributar por quantidade, e não mais por percentual.

Produto Consignado

Indica se o produto cadastrado é consignado ou não.

Tipo de produção

Serve para indicar o tipo de produção e possui as opções C-Produção Conjunta e T-Produção Tradicional.

### Descrição da Produção Conjunta

A produção conjunta é a produção de mais de 1 produto resultante do consumo de 1 ou mais componentes, onde não é possível apontar o consumo dos insumos diretos para os produtos resultantes. Por não ser possível precisar quais insumos e suas respectivas quantidades para a composição de um determinado produto, esse tipo de produção não requer a apresentação da sua ficha técnica (Registro 0210).

Esse tipo de produção é apresentado nos registros K290, K291 e K292, no caso de produção conjunta interna, ou nos registros K300, K301 e K302, no caso de produção conjunta em terceiros.

O sistema irá identificar a produção conjunta por meio da engenharia com componentes de entrada dos tipos 5 ou 6. A rotina da tela F660GDG deverá ser feita para que o campo seja alimentado com o tipo C. Caso tenha algum produto que não seja desse tipo, deverá ser incluída a necessidade por meio da tela F075PRO.

### Descrição da Produção Tradicional

A produção tradicional se enquadra no caso de produtos que são produzidos com base na composição de 1 ou mais componentes. Ex.: produtos originados a partir de montagens, fórmulas, receitas etc., além de se ter a noção exata do que será produzido.

Esse tipo de produção exige que os componentes voltados para a criação do produto estejam indicados previamente na sua ficha técnica (Registro 0210). Ele é apresentado nos registros K230 e K235, no caso de produção interna, ou nos registros K250 e K255, no caso de produção em terceiros.

**Natureza Rendimentos**

Classificação da natureza de rendimento do produto. Irá buscar as informações na tela Natureza de Rendimentos (F055NRE).

**Tipo de Resíduo Produzido**

Tem por finalidade o preenchimento do campo 19 do registro 1391 do SPED Fiscal.

**Art. 119 do RICMS/2017**

Está relacionado à geração da ADRC-ST. Identifica se uma NCM tem relação com o art. 119 do RICMS/2017 do estado do Paraná. Sempre que o conteúdo do campo for alterado na Classificação Fiscal, todos os produtos que possuem a mesma Classificação Fiscal serão alterados.

Cla. Categoria

Indica a classificação da categoria a qual o produto está vinculado.

**Percentual do Diferimento de ICMS relativo ao FCP**

Percentual do diferimento de ICMS relativo ao FCP sugerido para o cálculo do valor do diferimento de ICMS relativo ao FCP nos processos de vendas, faturamento, compras e recebimento. Este campo não tem preenchimento obrigatório.

Unidade de Medida para Etiqueta   
Campo destinado ao preenchimento da unidade de medida para impressão de etiquetas no
Gestão de Supermercados
.

Fator de Conversão para Etiqueta   
Campo destinado ao preenchimento do fator de conversão para impressão de etiquetas no
Gestão de Supermercados
.

Observação

Os campos Unidade de Medida para Etiqueta e Fator de Conversão para Etiqueta só ficarão visíveis nesta tela, quando o usuário possuir Proprietária de
Gestão de Supermercados
.

O campo Cla. Categoria só ficará visível nesta tela quando o usuário possuir as proprietárias:

* Gestão Empresarial com o Gestão de Supermercados;
* Integração Padrão com Varejo;
* Gestão de Lojas Senior com eDocs;
* Integração Megasul;
* Integração com web services e Ações SID.

Considerar no I-Simp

Indique se o produto deve ou não ser exportado no I-Simp.

Dispensa coleta (I-Simp)

Indica se o produto é dispensado de coleta.

Calcula FAF

Indica através das opções "S-Sim" ou "N-Não" o cálculo do FAF (Fator de ajuste de fruição) para o produto. Por padrão, este campo estará parametrizado como "N-Não".

Natureza Receita PIS  
 Informa a natureza da receita do PIS de acordo com a Sit. Trib. PIS Vendas informada para o produto. O código é exigido na escrituração fiscal do SPED Contribuições e deve ser utilizado de acordo com os códigos existentes nas tabelas da Receita Federal. Para mais informações, consulte a ajuda da tela Notas Fiscais de Saída (F660NFV), guia Itens.

Natureza Receita COFINS

 Informa a natureza da receita do COFINS de acordo com a Sit. Trib. COFINS Vendas informada para o produto. O código é exigido na escrituração fiscal do SPED Contribuições e deve ser utilizado de acordo com os códigos existentes nas tabelas da Receita Federal. Maiores informações, consulte ajuda da tela Notas Fiscais de Saída (F660NFV), guia Itens.

## Guia Derivações

Derivações  
Esta atividade trata as características dos produtos por Derivações. Ver Regra para Consumo de Componentes.

Descrição  
Descrição da derivação no componente da máscara.

Conferir Qtde nas Cargas

Quando o campo estiver com valor igual a "S- Sim", as cargas somente serão fechadas após conferência, utilizando as telas F135CCA ou F135CMC. Quando o campo estiver com valor igual a "N- Não", o sistema possibilitará fechar as cargas no momento de sua geração.

Esse campo só ficará habilitado para edição quando o campo Conferir Carga Antes do Fechamento estiver parametrizado com valor igual a "S - Sim" na tela F070FVE.

Descrição Complementar 

Descrição da derivação do produto.

Data Validade

Este campo é utilizado para inserir um prazo máximo de validade para a derivação do produto. O formato de preenchimento é DD/MM/AAAA. O sistema utiliza a data de validade informada nesse campo nas seguintes rotinas:

* Na tela de pedidos (F120GPD), quando existe uma data de validade na derivação do produto, ela será validada ao inserir o item no pedido. A validação realizada pelo sistema é feita com base na data de entrada do item, ou seja, a data de validade informada na derivação do produto precisa ser maior do que a data de entrada do item. Caso não seja, o sistema retornará a mensagem: “Data entrega maior que validade do produto/derivação
* No módulo de custos, a data da validade é utilizada como filtro através do botão Seleção (telas F621GCP, F621GPP e F621GPV). O usuário define a data de validade para a qual ele deseja validação e o sistema compara com o que foi preenchido no campo Data Validade da derivação do produto. Tendo a data de validade informada no filtro, o sistema lista na tela produtos cuja data de validade for maior ou igual à data informada na seleção
* Na tela de Modelo (Composição do Produto/Serviço) (F700CMC), o sistema também valida a data de validade na inclusão do componente. Neste caso, a data de validade do componente tem que ser maior ou igual à data previamente cadastrada no sistema

Código Barras EAN13 

Código de barras EAN formado de 13 caracteres numéricos.

**Cor do produto**

Indicativo da cor do produto.

Código de Barras Livre 

Código de barras livre, utilizado para a composição do código de barras para a leitura de múltiplos volumes. O campo deve ser preenchido com até 26 caracteres, pois é formado por trinta caracteres. Porém, os quatro últimos dígitos ficam reservados para o controle de volumes a serem lidos.

**Observação**

Quando o
Gestão Empresarial | ERP
está integrado com o
WMS WIS
, todo novo produto cadastrado precisa possuir um código de barras (no campo Código Barras EAN13
 ou Código de Barras Livre , ou ainda na tela F075BAR - Código de Barras). Do contrário, a seguinte mensagem é exibida ao salvar: Existem registros incoerentes para integração com WMS. Deseja visualizar o arquivo de Log?.

Dias Rep./Prec. Paral.

O valor deste campo será sugerido pela família.  
Quando o produto for comprado, este campo indicará a quantidade de dias necessários para reposição dos estoques do produto.  
Quando o produto for produzido, indicará o Número de Dias de Precedência ao início de produção do Componente (Consulte a documentação sobre o conceito de Número de dias de precedência para saber mais sobre esse processo).

Observação

Este campo não deverá ser informado quando o produto for acabado.

Código Fiscal e Descrição Fiscal  
Estes campos são atualizados e montados pelo sistema de acordo com a parametrização existente no cadastro de parâmetros fiscais (F070EPF).

**Observação**

O código ou a descrição fiscal permite alteração desde que no cadastro de parâmetros fiscais, o campo Alterar Código/Descrição Fiscal esteja como Sim.

Caso o usuário alterar alguma informação no cadastro do produto, o sistema já atualiza o código/descrição fiscal de acordo com a parametrização de montagem existente no cadastro de parâmetros fiscais.

Para o sistema não sobrepor o código/descrição fiscal, necessário ativar o identificador de regra GER-075CACDF01, assim o usuário pode confirmar se atualiza o código/descrição fiscal da derivação com o código/descrição montado pelo sistema.

Se optar por Não, permanecerá o código e a descrição fiscal que consta na derivação.

Consumo de energia elétrica em Kwh

Este campo é de preenchimento opcional e nele deve ser informado o consumo em Kwh (Quilowatt-hora), conforme laudo técnico. O Kwh informado no cadastro do produto é utilizado no cálculo de rateio do consumo de energia elétrica por produto, quando a natureza de gastos de energia elétrica não estiver informada na tela Parâmetros CAT 83/09 (F665PAT).

Número registro ANVISA

Informe o número de registro dos medicamentos e matérias-primas farmacêuticas.

Produção em Escala Relevante

Informe se o produto é produzido em escala relevante ou não. Os produtos produzidos em escala não relevante cuja NCM esteja relacionada no Anexo XXVII do Convênio 52/2017 devem ser preenchidas com o valor **N - Produzido em Escala Não Relevante**. Para mais informações, consulte a documentação do Indicador de Escala Relevante.

GTIN Unid. Trib.

Informe o código de barras do produto que representa a menor unidade tributável, e que será utilizado como código GTIN tributável na geração dos documentos eletrônicos. Para mais informações consulte a documentação do GTIN.

Especificador substituição tributária

Informe o Código especificador da substituição tributária (CEST) da derivação.

**Código do Princípio Ativo**

Permite informar o código do princípio ativo.

No momento da inclusão de um novo registro ao passar o foco pelos campos citados o sistema irá realizar a sugestão de valores com base no cadastro de famílias (F012FAM).

**Código Cultivar INDEA**

Esse campo será sugerido, caso tenha sido preenchido na tela de Cadastro de Famílias (F012FAM). Também será possível informar um código de até 12 dígitos.   

Esse código deve ser um valor válido perante ao INDEA (Instituto de Defesa Agropecuária do Estado de Mato Grosso).

**Tipo Produto SisDev**

Esse campo será sugerido, caso tenha sido preenchido na tela de Cadastro de Famílias (F012FAM). Também será possível informar o tipo de produto, de acordo com os valores disponíveis, que são: **1 - Agrotóxicos**, **2 - Sementes** ou **8 - Mudas**.

**Categoria da Semente**

Campo de ligação com o Cadastro de Categoria de Semente (F114CCS).

## Validação durante o cadastro de Produto

Ocorre depois que o
Gestão Empresarial | ERP
estiver integrado com o Gestão de Armazenagem | WMS. Do contrário, o ERP exibe um alerta, pois a falta do código de barras geraria inconsistências no WMS.

Tipo Conversão Unidade Medida 2 

Tipo de conversão da 1ª unidade de medida de estoque para a 2ª unidade de medida do produto/derivação.

Valor Conversão Unidade Medida 2 

Valor de conversão da 1ª unidade de medida de estoque para a 2ª unidade de medida do produto/
derivação.Quando informada é utilizada na ficha técnica do produto (modelo).

Tipo Conversão Unidade Medida 3 

Tipo de conversão da 1ª unidade de medida de estoque para a 3ª unidade de medida do produto/derivação.

Valor Conversão Unidade Medida 3 

Valor de conversão da 1ª unidade de medida de estoque para a 3ª unidade de medida do produto/derivação.

Valor/Data/Hora Preço Custo 

Valor do preço de custo. O campo Preço Custo ficará desabilitado quando existe o módulo Custos instalado na empresa. Este parâmetro está definido no
Cadastros de Empresas, campo Custos.

Origem do Preço de Custo

Indica a origem da formação do preço de custo do produto/derivação. As opções disponíveis são:

* D – Digitado
* F – Formação de preço: definido através da tela Custos > Gestão de Preço para Indústria > Formação de Preços > Custo Padrão > Atualiza Custo no cadastro de Produtos (F621ACP)
* C – Contabilidade de custos
  : definido através da tela Custos > Gestão de Contabilidade de Custos > Custo Integrado > Ajuste dos Custos dos Produtos > Atualiza Custo Ajustado do Produto (F632ACC)
* E – Contabilidade de custos
   – Critérios alternativos de avaliação de estoques: definido através da tela Custos > Gestão de Contabilidade de Custos > Custo não Integrado > Atualização do Custo no cadastro de Produtos (F632ACP)
* R – Produção a custo real
  : definido através da tela Custos > Gestão de Contabilidade de Custos > Análises de Desempenho > Custo da Produção > Atualiza Custo Real no cad. de Produtos (F634ACC)
* A – Sobre o preço de venda

Valor/Data Preço Médio 

Preço médio orientativo (o preço médio real é calculado pelo fechamento. Data base do preço médio.

Valor/Data Preço última Entrada 

Preço da última entrada. Data base do preço da última entrada.

Valor/Data Preço Reposição 

Preço de reposição.Data base do preço de reposição.

Dias Cálculo Validade Lote 

Quantidade de dias para o cálculo da validade do lote de fabricação.

Custos Salários e Ordenados

Custos gastos com salários e ordenados para a fabricação de uma unidade do produto.

Custos Encargos Sociais e Trabalhistas

Custos gastos com encargos sociais e trabalhistas para fabricação de uma unidade do produto.

Número Registro DCR-e

Número do registro DCR-e.

Peso Bruto 

Peso bruto do produto.

Peso Líquido 

Peso líquido do produto.

Volume 

Volume do produto. Em centímetros cúbicos.

% Perda 

Percentual de perda do produto (estocagem, defeituosos, imperfeitos). Ao informar algum valor nesse campo, o total mencionado será adicionado ao total de
peças geradas no pedido, em forma de percentual.

### Exemplo

Se esse campo tiver o valor 10 e gerar um pedido com 100 unidades, na tela de explosão de necessidades (F813GNE), o campo % Perda será preenchido com
o mesmo valor mencionado na tela de cadastro de produto (conforme o exemplo: 10), e o campo Qtde Perda receberá 10, ou seja, 100 unidades \* 10% (100\*0,10 = 10). Assim a explosão do pedido de 100 unidades será feita na realidade com 110 unidades, devido a perda mencionada.

Quantidade Perda Fixa 

Quantidade de perda fixa do produto que será considerado para a explosão de necessidades e geração de OPs.

Observação

O total mencionado neste campo será adicionado ao total de peças geradas no pedido.

### Exemplo

Se este campo estiver com o valor 10 e gerar um pedido com 100 unidades, a O.P. será gerada com um total de 110 unidades.

Quantidade Padrão Inspeção Qualidade 

Quantidade padrão para inspecionar pela qualidade quando da movimentação de OPs.

Quantidade Ciclo Inspeção Qualidade 

Quantidade cíclica (de quando em quando) para inspecionar pela qualidade quando da movimentação de OPs.

Roteiro  
Código do roteiro (quando a derivação do produto tem processo de fabricação específico).

Curva ABC 

Curva ABC (informar A, B ou C) através da classificação da curva de quantidades em estoque.

Código Regra 

Código da regra usado para cálculo do consumo do modelo (Eng. Ind.).

Embalagem 

Código da embalagem padrão do produto/derivação.

Quantidade por Embalagem 

Quantidade padrão do produto por embalagem.

Baixa na OP?

Indicativo de baixa na OP. No cadastramento da derivação, este campo assume o valor que consta no campo Baixa na OP? da guia Dados Gerais do cadastro do produto.

Aprova Defeito 

Indicativo se o produto pode ou não ser aprovado com defeitos ou não-conformidades.

Código do Plano de Inspeção

Código do plano de inspeções que serão efetuadas no produto.

Serviço Movimentado pelo Produto 

Código do serviço ligado ao produto para geração de nota fiscal de serviços que necessitam de movimentação de estoques. Ao fechar uma nota fiscal de entrada será gerado o movimento de estoques considerando os valores e quantidades do item de serviço. No item de produto da nota
fiscal de entrada será gravado o número da seq. do item de serviço gerado pelo Produto.

Não será possível alterar informações desse produto, nem excluí-lo,
devendo qualquer alteração ser feita na pasta Serviços, inclusive a exclusão. Ao fechar a nota fiscal de entrada, o movimento de estoque será gerado
considerando os valores e quantidades do item de Serviço. O produto terá seus valores zerados, ficando a nota fiscal de entrada com os valores
referentes ao Serviço.

Controle Validade 

Consiste em todo o
Gestão Empresarial | ERP
se a data de validade de um determinado lote deve ser informada ou não. O ERP só permite esta informação, quando
estiver sendo processado um movimento de entrada, tanto manual quanto de uma Nota Fiscal de Entrada.

* L - Livre: o usuário ficará livre para informar ou não a data de validade;
* O - Obriga: o usuário ficará obrigado a informar a data de validade
* D - Desativa: o campo ficará desativado na tela

Qtde Múltipla  
Quantidade múltipla para cálculo da geração de ordem de produção/compra.

> Observação
>
> * Este campo somente ficará habilitado para produtos produzidos e com origens que geram OP por produto/derivação
>   (ver em Cadastros > Produtos > Origens, o campo O.P.gera por Produto/Derivação deverá estar como S (Sim)
> * Esse processo somente acontecerá para geração de OPs via pedido

Qtde. Mínima

Quantidade mínima de unidades do produto permitido por ordem de produção/compra.

* Na geração das ordens de produção o sistema sempre obedecerá a quantidade mínima do produto definida neste campo, ou seja, mesmo que um pedido ou geração manual de OP tenha necessidade menor que o valor definido neste campo, o sistema irá gerar a quantidade aqui informada
* Quando o campo **Produto 2ª, 3ª Qualidade ou Reaproveitado** for diferente de N (Normal), esse campo não ficará habilitado
* Para origens que geram OP por produto/derivação, é possível estabelecer quantidade mínima, múltipla e máxima na derivação do produto. Ao gerar uma OP, o sistema busca esta informação primeiro na tabela de derivações, caso não encontre nada, busca na tabela de produtos

Observação

* Este campo somente ficará habilitado para produtos produzidos e com origens que geram OP por produto/derivação
  (ver em Cadastros > Produtos > Origens, o campo O.P.gera por Produto/Derivação deverá estar como S (Sim)
* Este processo somente acontecerá para geração de OPs via pedido

Qtde. Máxima 

Quantidade máxima de unidades da derivação do produto para uma ordem de produção/compra.

Observação

* Este campo somente ficará habilitado para produtos produzidos e com origens que geram OP por produto/derivação
  (ver em Cadastros > Produtos > Origens, o campo O.P. gera por Produto/Derivação deverá estar como S (Sim)
* Este processo somente acontecerá para geração de OPs via pedido

Situação 

Situação da derivação do produto (A Ativo ou I Inativo).

Densidade  
Permite informar valores para ser considerado na densidade do produto, sem necessariamente informar peso líquido.

Usuário Geração

Usuário que cadastrou o produto.

Data Geração 

Data em que o produto foi cadastrado.

Hora Geração 

Data em que o produto foi cadastrado.

Usuário Alteração 

Usuário que realizou ultima alteração no produto.

Data Alteração 

Data de última alteração no produto.

Hora Alteração 

Hora de última alteração no produto.

% CIDE Tecnologia 

Permite informar o percentual de imposto CIDE tecnologia. Este valor é gravado na tabela E075DER.PerCit.

Código Fiscal 

Permite informar o código fiscal. Este campo somente estará disponível para edição, casa seja parametrizado como S (Sim) o campo
Alterar Código/Descrição da tela F070EPF.

Descrição Fiscal 

Permite informar a descrição fiscal. Este campo somente estará disponível para edição, casa seja parametrizado como S (Sim) o
campo Alterar Código/Descrição da tela F070EPF.

Indicativo Volume 

Indica se o produto é controlado no sistema como sendo
um volume.
Ver  produto volume.

Mot. Isenção Anvisa

Motivo de isenção do registro Anvisa. Essa informação é gerada no campo **xMotivoIsencao** do Grupo K no arquivo XML de NF-e/NFC-e.

Bem móvel usado

Somente para fornecimentos de bem móvel usado adquirido de pessoa física que não seja contribuinte ou que seja inscrita como MEI.

## Guia Caract. Produto/Derivação

Descrição Livre 

Somente poderá ser alterada a descrição se a característica não tiver componentes.

Observação

Este campo somente é gravado na ligação da característica com produto/derivação, quando essa característica não possui componente. Isso porque, quando o componente não possui uma máscara de derivação, o sistema permite que no momento de realizar a ligação da característica ao produto/derivação o usuário possa informar uma descrição livre que ficará registrada na ligação.

No caso da característica com componentes, a descrição livre inserida na característica é da característica, não da ligação dela com o produto/derivação, por este motivo não é enviada para a ligação do produto/derivação com a característica.

## Guia Históricos

Históricos  
Refere-se aos textos informativos e ou detalhes técnicos relativos a fatos e observações de necessidade a fazer histórico que podem ser por derivação e
sequência de produto. Este histórico é livre.

## Guia Inf. Complementares

Emitir Contra Nota   
Permite indicar entre "S-Sim" ou "N-Não" para emitir contra nota para as notas fiscais de entrada do tipo 1, 9 ou 11.

**Considera Siga**

Permite indicar entre "S-Sim" ou "N-Não" para indicar se há necessidade de geração do arquivo para o Siga. Esse campo é útil para sinalizar produtos que não emitem receituário agronômico, mas devem ser incluídos no arquivo para o Siga, de movimentação de estoque.

Int. Hub Royalties

Permite indicar se há integração do produto com o Hub de Royalties. As duas opções disponíveis são:

* **Sim**: Para indicar que há integração ativa. Portanto, só serão integrados a entrega de Royalties com o Hub de Royalties se o campo estiver informado com esta opção.
* **Não**: Para indicar que o produto não possui integração com o Hub de Royalties.

Código item cClass

Campo para preenchimento da classificação do item para NFCom e NF3-e, conforme as opções disponíveis no Portal da Nota Fiscal Fatura de Serviço de Comunicação Eletrônica - SVRS.

Calcula FUST

Indica se o produto calcula o FUST para itens da NFCom.

Percentual FUST

Percentual do FUST para aplicar nos itens da NFCom.

Calcula FUNTTEL

Indica se o produto calcula o FUNTTEL para itens da NFCom.

Percentual FUNTTEL

Percentual do FUNTTEL para aplicar nos itens da NFCom.

Aplicação da CBS/IBS

Indicador do tipo de aplicação utilizado no CBS/IBS para determinar o cClassTrib utilizado no motor de cálculo.

## Páginas relacionadas

* [F115CST](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f115cst.htm)
* [Contratos com Fornecedores](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/manuais_processos/agronegocio/processos/contrato/contratos.htm)
* [F460PFO](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f460pfo.htm)
* [F015MED](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f015med.htm)
* [F015UMA](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f015uma.htm)
* [F660ISP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f660isp.htm)
* [F070EMP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070emp.htm)
* [F075FPI](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075fpi.htm)
* [ExiAtuCes](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#ExiAtuCes)
* [ICMS Monofásico](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/icms-monofasico.htm)
* [Sugestão de depósito padrão](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/sugestao-deposito-padrao.htm#menu_mercado/Sugestao-deposito-padrao)
* [royalty](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/manuais_processos/agronegocio/processos/royalties.htm)
* [F403FPR](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f403fpr.htm)
* [Senar](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/manuais_processos/agronegocio/processos/impostos/senar.htm)
* [Funrural](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/manuais_processos/agronegocio/processos/impostos/funrural.htm)
* [F813CNP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_manufatura/f813cnp.htm)
* [liberar a OP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f083ori.htm#gerar_lote_op)
* [CHA-900CLPOP01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/cha_900clpop01.htm)
* [F900AQP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_manufatura/f900aqp.htm)
* [Fechamento dos Estoques - Detalhes](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f215fes_fechamento_detalhes.htm#Pre%C3%A7o)
* [F019TST](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f019tst.htm)
* [produto volume](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_manufatura/conceito_produto_com_controle_de_volumes.htm)
* [F445PRC](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f445prc.htm)
* [nota fiscal de crédito de ICMS](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/manuais_processos/agronegocio/processos/credito_icms/icms_produtor.htm)
* [F012FAM](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f012fam.htm)
* [F055TPR](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f055tpr.htm)
* [F113REM](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f113rem.htm)
* [Manual de processos do Receituário Agronômico](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/manuais_processos/receituario_agronomico/inicio.htm)
* [F022CLF](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f022clf.htm)
* [F665ICA](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f665ica.htm)
* [F051DIS](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f051dis.htm)
* [Ato Cooperado](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/manuais_processos/agronegocio/processos/ato-cooperado/inicio.htm)
* [F085COP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f085cop.htm)
* [F083ORI](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f083ori.htm)
* [F013AGP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f013agp.htm)
* [Manutenção dos parâmetros globais do sistema (F000PGS)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm)
* [Definição da Cópia (F000IPR)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_ajuda/f000ipr.htm)
* [Tabela de Multiplicadores para ICMS na Entrada Nacional do Amazonas (F660MIA)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f660mia.htm)
* [percentuais](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/manuais_processos/suprimentos/admissao-temporaria/processo-admissao-temporaria.htm#percentual)
* [tempo de permanência](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/manuais_processos/suprimentos/admissao-temporaria/processo-admissao-temporaria.htm#data)
* [Admissão temporária](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/manuais_processos/suprimentos/admissao-temporaria/processo-admissao-temporaria.htm)
* [ICMS Antecipação](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/impostos-icms.htm#icms-antecipacao)
* [F019ANP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f019anp.htm)
* [CIAE052](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/relatorios/arquivos-eletronicos-estaduais/ciae052.htm)
* [GTIN](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/manuais_processos/mercado/nf-e/regras-e-sugestoes-valores.htm#gtin)
* [F660GDG](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f660gdg.htm)
* [Natureza de Rendimentos (F055NRE)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f055nre.htm)
* [Regra para Consumo de Componentes](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_manufatura/conceito_regra_consumo.htm)
* [F135CCA](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f135cca.htm)
* [F135CMC](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f135cmc.htm)
* [F070FVE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070fve.htm)
* [derivação](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/conceito_mascara_devericao.htm)
* [F120GPD](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f120gpd.htm)
* [F621GCP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_custos/f621gcp.htm)
* [F621GPP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_custos/f621gpp.htm)
* [F621GPV](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_custos/f621gpv.htm)
* [F700CMC](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_manufatura/f700cmc.htm)
* [F075BAR - Código de Barras](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075bar.htm)
* [Número de dias de precedência](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_manufatura/conceito_dias_precedencias.htm)
* [F665PAT](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f665pat.htm)
* [Indicador de Escala Relevante](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/manuais_processos/mercado/nf-e/regras-e-sugestoes-valores.htm#indicador_de_escala_relevante)
* [modelo](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_manufatura/conceito_modelo.htm)
* [F621ACP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_custos/f621acp.htm)
* [F632ACC](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_custos/f632acc.htm)
* [F632ACP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_custos/f632acp.htm)
* [F634ACC](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_custos/f634acc.htm)
* [F813GNE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_manufatura/f813gne.htm)
* [F070EPF](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070epf.htm)
* [Portal da Nota Fiscal Fatura de Serviço de Comunicação Eletrônica - SVRS](https://dfe-portal.svrs.rs.gov.br/NFCOM/tabelacclass)
