# F120GPB - Entrada de Pedidos Simplificada

> **Fonte:** F120GPB - Entrada de Pedidos Simplificada — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f120gpb.htm  
> **Trilha:** Ajuda por telas > Mercado > Gestão de Vendas > Pedidos  
> **Telas citadas:** E210DLS, E210EST, F000AVA, F000CRT, F019TIS, F028GCP, F070FVE, F075CPD, F081CTV, F081TCA, F085HCL, F099UVE, F120GPB, F120GPD, F120GPS, F121CAR, F211CPR  
> **Identificadores de regras:** GER-120PEDAP01, VEN-120SUSPE01

---
Ajuda por telas > Mercado > Gestão de Vendas > Pedidos > Simplificada

Esta tela permite a geração de pedidos de venda de forma
simplificada.

## Processos

É possível inserir um produto do tipo Passagem Direta no pedido. Se
a classe do produto for 2 - De Passagem Direta, serão efetuadas as
consistências realizadas para o produto do tipo de passagem direta. Como
produtos de passagem direta não possuem estoque, não será exigida a
informação do depósito, porém, o campo Depósito poderá ser preenchido
com finalidade informativa.

Não serão realizadas consistências
relacionadas ao depósito, como por exemplo saldos disponíveis e
ligações do produto. Para o produto de passagem direta não será permitida a reserva de
estoque, pois este produto não possui estoque.

Nesta tela não é possível digitar pedidos de orçamento (pedidos cuja transação seja do módulo de orçamentos - VEO), apenas pedidos normais (cuja transação seja do módulo normal - VEP).

Ao gerar pedidos com parcelas especiais e condição de pagamento
parametrizada para considerar juros desde a venda (tela
F028GCP),
a data de vencimento será a de geração, e a data de vencimento
original, calculada a partir da condição de pagamento, será a data provável
de pagamento do
título.

Caso a
transação utilizada possua integração com o financeiro, esse processo
será aplicado também nos títulos gerados no contas a receber.

* As parcelas, na geração de um pedido, podem seguir as definições cadastradas na condição de pagamento (F028GCP), com os dias fixos determinados através dos campos Dia/Mês Fixo ou Dia Fixo.

As condições de pagamento utilizadas devem estar vinculadas à tabela de preço (Tabelas de Preço x Condição de Pagamento) através da tela F081TCA.

* Ao utilizar o identificador de regras VEN-120SUSPE01
  no fechamento de pedidos, as seguintes regras sejam consideradas:   
  1. Atribuir a situação 3 - Suspenso para o pedido quando o identificador de regras estiver ativo e não possuir regra vinculada
  2. Atribuir a situação definida na variável VenNSitPed para o pedido quando o identificador de regras possuir uma regra vinculada
  3. Executar a rotina padrão do sistema para atualizar a situação do pedido quando o identificador de regras estiver vinculado a uma regra, e ela não retornar nenhum valor para a variável VenNSitPed
  4. Executar a rotina padrão do sistema para atualizar a situação do pedido quando o identificador de regra não estiver ativo

Para o cálculo do ICMS Diferido, conheça o processo.

Quando houver integração com a Megasul, a filial do pedido está credenciada na versão **02.03** do PAF-ECF e o pedido é do tipo **ECF**, não será possível gravar um pedido sem pelo menos um item de produto ou serviço ou realizar a exclusão de pedidos e seus itens. O item é gravado no pedido no momento em que é confirmada a inclusão ou alteração do item do pedido.

**Reforma Tributária – Consulta de Impostos**

Esta tela permite o acesso à Consulta de Impostos da Reforma Tributária (F000CRT), o qual pode ser feito das seguintes formas:

* Por meio do botão CBS e IBS, disponível nos botões de Cálculo para telas de Pedido, Ordem de Compra, Cotação e Nota Fiscal;
* Ou diretamente pelo botão CBS e IBS para as telas de consulta.

Para conferir todas as rotinas impactadas pela Reforma Tributária, acesse esta documentação.

---

## Campos

Tem Avalistas

Indica se o pedido possui avalistas, ou não. Este campo terá
seu valor sugerido de acordo com a parametrização da filial de vendas (F070FVE). Caso a filial controlar avalistas em pedidos, este campo será
sugerido com S - Sim e, se a filial não controlar avalistas em pedidos, o campo será preenchido com N - Não. Quando a filial não
controlar avalistas em nenhuma entidade, este campo permanecerá desabilitado.

Indicativo Presencial e Data Prest. Serviço

Indicam de que forma o pedido foi realizado e a data. Estes campos só
podem ser alterados enquanto o pedido estiver com a situação igual a 9
- Não Fechado. Se o pedido for fechado com o campo Indicativo Presencial em branco, o
fechamento do pedido irá fazer a sugestão de um valor para o campo
seguindo o critério:

* Utilizar o indicativo presencial informado nas definições do cliente
* Se não encontrar no cadastro do cliente, irá buscar da transação da
  transação de produto, se o pedido não possuir uma transação de produto,
  então será buscada da transação de serviço
* Se não encontrar no cadastro do cliente e nas transações, será
  utilizado o indicativo presencial informado nas definições da filial
  para as operações de vendas, tela F070FVE

Rota/Seq./Sub Rota

Código/sequência da rota/sub rota para entrega do pedido.

Importante

Quando os botões estão visíveis (opção Exibir Botões Gerais (K) marcada), entre os botões e os campos de Dados Gerais existe um recurso que permite redimensionar a área para melhor visualizar os campos. Caso os botões não estejam visíveis, esse recurso fica entre os campos de Dados Gerais e as guias Produtos e Parcelas.

**Indicador de Intermediador/Marketplace**

 Campo para atendimento à NT 2020.006.

* Operação sem intermediador (em site ou plataforma própria)
* Operação em site ou plataforma de terceiros (intermediadores/marketplace)

**Código do Intermediador**

 Campo para atendimento à NT 2020.006.

**CNPJ do Intermediador**

 Campo para atendimento à NT 2020.006. CNPJ do Intermediador da Transação
(agenciador, plataforma de delivery, marketplace e
similar) de serviços e de negócios.

**Cadastro no Intermediador**

Campo para atendimento à NT 2020.006. Nome do usuário ou identificação do perfil do vendedor no
site do intermediador (agenciador, plataforma de
delivery, marketplace e similar) de serviços e de
negócios.

## Botões

Avalistas

Exibe a tela F000AVA, onde é possível informar os
avalistas do pedido.

Sel. Campos

Exibe a tela F120GPS.

---

## Guia Produtos

### Campos

Nº Lote do cliente

Número do lote do cliente informado no pedido, essa informação pode ser inserida, alterada ou removida da grade, mesmo que os dados foram originários de uma integração, como web service.

**Nº Remessa do cliente**

Número de remessa do cliente informado no pedido, essa informação pode ser inserida, alterada ou removida da grade, mesmo que os dados foram originários de uma integração, como web service.

**Nº Pedido do cliente**

Número do pedido cliente informado no pedido, essa informação pode ser inserida, alterada ou removida da grade, mesmo que os dados foram originários de uma integração como, web service.

**Per. do Dif. de ICMS FCP**

Percentual do diferimento de ICMS relativo ao FCP sugerido a partir das parametrizações do ERP

**Mot. deson ICMS-ST**

 Motivo da desoneração do ICMS-ST na grade de produtos para calcular o valor do ICMS-ST desonerado. Sugerido a partir das parametrizações definidas na tela F019TIS.

**Sit. Trib. ICMS**

Situação tributária do ICMS do item do pedido. Essa informação não pode ser inserida, alterada ou removida da grade, sendo somente um informativo da sugestão dada pelo sistema.

Importante

Acesse a documentação para verificar quais telas do sistema geram os diferentes tipos de pedidos.

Res?

Reservar quantidade de estoque

**Observação**

Quando o item é controlado por série e foi optado por reservar estoque, caso seja utilizada uma série que não possua saldo na E210DLS,a reserva não será gravada nessa tabela. Isso ocorre porque a série adota o conceito de um para um, ou seja, a cada movimento de entrada é gerado um novo registro na E210DLS. Assim, se a série não tiver saldo, ao realizar a entrada será criado um novo registro, impossibilitando que, no fechamento do pedido com reserva de estoque, seja vinculada uma quantidade a uma série sem saldo.

Já na E210EST, a reserva ocorrerá normalmente, garantindo que a quantidade do produto esteja corretamente reservada.

### Botões

Cálculos e Valores

Exibe a tela F121CAR com os cálculos dos itens dos produtos do pedido.

Produto

Exibe a tela F075CPD para
consulta do produto selecionado.

Tabela de Preço

Exibe a tela F081CTV para
consulta da tabela de preço do produto selecionado.

Estoque

Exibe a tela F211CPR para consulta do estoque do produto selecionado.

Comp. Calc.

Exibe a tela de consulta da margem de contribuição.

## Guia Parcelas

### Campos

% Desc. Antecipação

Percentual do desconto de antecipação.

% Desc. Pontualidade

Percentual do desconto de pontualidade, sendo exclusivo do Agronegócio.

Observação

Os
percentuais dos descontos serão preenchidos no momento da geração das
parcelas. A regra para a busca dos percentuais dos descontos é:

* F081TCA
* F028GCP (guia Itens)
* F028GCP
* F085HCL

O identificador de regras GER-120PEDAP01, porém,
fica à frente da sequência descrita acima. Caso tenha uma regra cadastrada, no
momento de geração das parcelas serão sugeridos os percentuais dos
descontos de antecipação e pontualidade informados na regra. Esses
percentuais também poderão ser informados manualmente, desde
que isso esteja parametrizado na tela F099UVE.

Operadora

Nome da operadora financeira. O campo será habilitado somente quando o tipo de pagamento atrelado à forma de pagamento for igual a "2, 3, 4, 6, 7, 8, 12, 14, 15, 16, 17, 18, 19, 20, 22, 23, 24, 25, 27, 28, 29, 30 ou 31".

Autorização da Transação (TEF) 

Número de autorização da transação da operação cartão de crédito e/ou débito

Bandeira

Nome da bandeira do cartão de crédito e/ou débito.

Forma Pagto

Herda a informação da Forma de Pagto do cabeçalho do pedido.

Quando a tela for acessada a partir do menu Varejo, esse campo terá um comportamento diferente quanto à forma de pagamento e uso de parcelas especiais. Ao alterar a forma de pagamento no cabeçalho, ela **não será replicada para as parcelas**, que permanecem com o valor anterior e devem ser alteradas manualmente.

Isso não se aplica caso haja, em sua proprietária, a integração com o Varejo (Gestão de Lojas). Esse comportamento também não se aplica à tela F120GPD.

Observação

Marcando a caixa de seleção Reservar Estoque faz com que, ao ser criado um novo pedido, ele já venha com o campo Res? preenchido como "S-Sim".

---

## Identificadores de regras

| Módulo | Código |
| GER | 120PEDAP01 |
| VEN | 120ALFLT01 |
| VEN | 120CTRCB01 |
| VEN | 120EXCOB01 |
| VEN | 120EXCLU01 |
| VEN | 120GERNE01 |
| VEN | 000CONIT01 |
| VEN | 120CAPED01 |

## Páginas relacionadas

* [Ajuda por telas](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/ajuda-telas.htm)
* [Mercado](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/menu_mercado.htm)
* [Gestão de Vendas](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/menu_mercado_gestao_vendas.htm)
* [Pedidos](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/fluxos/fluxograma_vendas_pedidos.htm)
* [F028GCP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f028gcp.htm)
* [F081TCA](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f081tca.htm)
* [VEN-120SUSPE01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_120suspe01.htm)
* [processo](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/impostos-icms.htm)
* [F000CRT](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000crt.htm)
* [documentação](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/reforma-tributaria/rotinas-impactadas.htm)
* [NT 2020.006](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/notas-tecnicas-nfe-nfce.htm#2020.006)
* [F000AVA](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f000ava.htm)
* [F120GPS](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f120gps.htm)
* [documentação](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/processo_pedidos.htm)
* [F075CPD](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075cpd.htm)
* [F081CTV](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f081ctv.htm)
* [F211CPR](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f211cpr.htm)
* [F085HCL](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f085hcl.htm)
* [GER-120PEDAP01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ger_120pedap01.htm)
* [F099UVE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f099uve.htm)
* [F120GPD](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f120gpd.htm)
* [120ALFLT01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_120alflt01.htm)
* [120CTRCB01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_120ctrcb01.htm)
* [120EXCOB01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_120excob01.htm)
* [120EXCLU01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_120exclu01.htm)
* [120GERNE01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_120gerne01.htm)
* [000CONIT01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_000conit01.htm)
* [120CAPED01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_120caped01.htm)
