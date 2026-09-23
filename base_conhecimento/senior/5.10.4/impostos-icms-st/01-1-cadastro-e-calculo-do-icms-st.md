# 1. Cadastro e cálculo do ICMS ST

> **Fonte:** ICMS ST — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/impostos-icms-st.htm#Cadastro  
> **Trilha:** Ajuda por telas > Controladoria > Gestão de Tributos > Operações e Cálculos Fiscais > Cálculos > Apuração > F661IA5  
> **Telas citadas:** E019SUB, E019TST, E075DER, E081ITP, E140NFV, E660NFC, E660NFV, F001TCP, F001TIT, F001TVE, F009PPE, F019TIE, F019TIS, F051GUI, F051IMP, F055PPF, F070FEF, F070PSE, F075CEP, F075PCA, F075PPC, F075PPF, F075PRO, F085CAD, F095CAD, F403FPR, F661PAI  
> **Identificadores de regras:** COM-000ALSUB01, COM-000ALSUB02, CPR-440GERTI01, VEN-000ALISD01, VEN-000PRUIS01

---
## 1.1. Cadastrar um código de ICMS ST

* Cadastros > Mercado e Suprimentos > Parâmetros Fiscais > Substituições Impostos > Modalidade Base Cálculo (F019TIS)

![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/images/imposto_icms_st001_thumb_0_48.png)

## 1.2. Informar o código do ICMS ST em algum dos seguintes cadastros

* Cadastros > Transações > Parâmetros por Gestão > Compras > Ordem Compra > NF Entrada > Fatura (F001TCP)
* Cadastros > Transações > Parâmetros por Gestão > Vendas (F001TVE)
* Cadastros > Produtos e Serviços > Produtos > Individual (F075PRO)
* Cadastros > Clientes e Fornecedores > Fornecedores > Ligações > Fornecedor X Produtos > Individual (F403FPR)
* Cadastros > Clientes e Fornecedores > Clientes > Ligações > Cliente X Produto > Individual (F075PPC)

O código de ICMS ST constante na transação é atribuído no item da nota e, a partir da configuração deste código de ICMS ST, o sistema faz o cálculo do imposto.

![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/images/imposto_icms_st003_thumb_0_48.png)

Para que o cálculo seja efetuado, é necessário que a unidade fiscal do cadastro do cliente conste na tabela de ICMS ST.

![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/images/imposto_icms_st004_thumb_0_48.png)

Para que o cálculo seja efetuado em Notas Fiscais de Entrada, é necessário que a unidade fiscal do cadastro do fornecedor conste na tabela de ICMS ST.

Para que o cálculo seja efetuado, é necessário que a data de emissão da nota seja igual ou maior que a validade inicial da tabela de ICMS ST.

Se a tabela de ICMS ST estiver parametrizada para descontar o valor do ICMS Normal e o valor do ICMS Normal for maior que o valor do ICMS ST, o ICMS ST ficará zerado.

Quando precisar configurar um código de ICMS ST onde o valor do ICMS normal seja descontado, é este o parâmetro que deverá ser alterado.

![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/images/imposto_icms_st006_thumb_0_48.png)

Se o ICMS ST não estiver sendo calculado nas notas de saída e pedidos, é necessário verificar se a tabela de ICMS ST está parametrizada para calcular o imposto na saída quando já calculado na entrada.

![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/images/imposto_icms_st007_thumb_0_48.png)

Caso necessário, o ICMS ST pode ser alterado via identificador de regras COM-000ALSUB01. Este identificador de regras é executado somente quando o sistema estiver devidamente configurado para calcular o ICMS ST.

Se o ICMS ST não estiver sendo calculado nas notas de saída e pedidos, é necessário verificar se a tabela de ICMS ST está parametrizada para calcular o imposto para produtos com produção em escala não relevante. Isso pode ser feito na tela Tipos Substituições Impostos / Modalidade Base Cálculo / Antecipação - Por Estado (F019TIS) por meio do campo ICMS ST esc. não rel.

## 1.3. Código do ICMS ST

Por padrão, o campo de ICMS ST nos itens dos documentos do ERP Senior não fica habilitado quando não sugerido automaticamente um código de ICMS ST. Então, para deixá-lo habilitado possibilitando ao usuário atribuir um código específico, a sugestão é cadastrar um código de ICMS ST com todos os percentuais zerados e vinculá-lo num dos cadastros que permitem informar este código. Logo, este código sempre será atribuído ao item do pedido, ordem e notas e o campo ficará habilitado.

O sistema também não permite limpar o campo de ICMS ST. Para zerá-lo, a sugestão é também ter um código com todos os percentuais zerados para utilizá-lo quando se fizer necessário zerar o imposto.

Caso as possibilidades de vínculo de ICMS ST no ERP não sejam suficientes para as necessidade do cliente, pode-se então utilizar o identificador de regras “COM-000ALSUB02” para alterar o código de ICMS ST conforme necessidades especificas. Este identificador de regras é executado somente quando o sistema estiver devidamente configurado para calcular o ICMS ST.

## 1.4. Geração de títulos – ICMS ST Retenção – Guia de Recolhimento

Esta parametrização serve para gerar título com o valor do ICMS retido constante na nota.

No cadastro do ICMS ST deve ser informado um percentual de redução no campo % Ret. ICMS e se o código de redução gera título com S nos campo Gera Tit. Ret. N.F.E. e Gera Tit. Ret. N.F.S.

* Cadastros > Mercado e Suprimentos > Parâmetros Fiscais > Substituições Impostos > Modalidade Base Cálculo (F019TIS)  
  Para operações de compra, deve-se utilizar o estado do fornecedor da nota.

A consulta do código de ICMS ST nesta tela deve ser feita aplicando o código da filial onde o documento esteja sendo incluído. Muitas vezes consulta-se a tela F019TIS (Cadastro do ICMS ST) deixando o campo referente a filial vazio, porém se há um código de ICMS ST definido com o código da filial, este sobrepõe aquele que está sem código de filial definido.

* Cadastrar a guia de recolhimento.
* Cadastros > Controladoria > Tributos > Guias de recolhimento (F051GUI).
* Cadastrar um imposto do tipo 34.
* Cadastros > Controladoria > Tributos > Cadastro (F051IMP).

Ligação do código do imposto à filial. Devem ser preenchidos os campos destacados para geração do título e também da guia de recolhimento.

![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/images/imposto_icms_st011_thumb_0_48.png)

Nas definições por estado, defina o fornecedor, tipo de título, transação e imposto para vencimento do título. Para operações de compra, deve-se utilizar o estado da filial recebedora da nota.

* Cadastro (F009PPE):

![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/images/imposto_icms_st012_thumb_0_48.png)

Com esses parâmetros, o título de ICMS ST é gerado com o valor retido:

![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/images/imposto_icms_st013_thumb_0_48.png)

Também é gerada a guia de recolhimento correspondente ao título:

![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/images/imposto_icms_st014_thumb_0_48.png)

Caso queira gerar o título com o valor do ICMS ST e não com o valor retido, faça s eguinte parametrização:

Utilize um imposto do tipo 98 - Livre. Ele exige um tratamento via regra para que o valor do imposto seja gerado.

* Cadastro (F051IMP) - cadastre um imposto do tipo 98 - Livre;
* Base imposto (Liga Filial) (F055PPF) - faça a ligação do imposto na filial;
* Configuração para geração de títulos de impostos (F001TIT) - cadastrar o imposto do tipo 98. Na última coluna da grade deve ser informada uma regra.

Edite uma regra para que o valor da substituição tributária (E140NFV.VlrSic) seja atribuído à variável **VSVLRIMP**. Para verificar as variáveis para criação da regra, consulte a documentação do identificador de regras CPR-440GERTI01.

## 1.5. Geração da guia de recolhimento exclusiva para o Fundo de Combate à Pobreza

Quando a coluna Gera guia FCP ICMS ST, da grade da tela Tipos Substituição Imposto/Modalidade Base Cálculo - Por Estado (F019TIS), estiver parametrizada como **S – Sim**, é gerada uma guia para o Fundo de Combate à Pobreza (FCP) separada da guia de recolhimento da substituição tributária, quando o recolhimento é realizado através da nota fiscal, de acordo com o valor da alíquota parametrizado na tela Parâmetros Fiscais de produtos e serviços por filial e estado (F070PSE).

## 1.6. Valor do ICMS ST na 1º parcela

A condição de pagamento pode ser configurada para receber apenas o valor do ICMS Substituído na primeira parcela, com um vencimento também configurável. Para isso, basta informar na condição de pagamento S para o campo ICMS Substituído na 1ª parcela e que o Tipo Parcelas é 3-Parcelas Diferentes.

Dessa forma, é possível informar nos itens das parcelas da condição de pagamento que a primeira parcela terá percentual de rateio igual a 0 (zero) com o número de dias de intervalo desejado (10, por exemplo).

E que as demais parcelas receberão 100% de rateio. Assim, a primeira parcela não receberá nenhum valor além do ICMS Substituído e terá um vencimento de acordo com os dias de intervalo parametrizado.

Já as demais parcelas terão o restante do valor financeiro da nota fiscal, também com vencimento dentro do intervalo configurado na condição de pagamento.

Se desejar colocar o valor do ICMS ST na 1º parcela somado a parte do valor financeiro da nota, basta não confirmar a 1º parcela com rateio igual a 0.

## 1.7. Cálculo MVA

* F019TIS.

## 1.8. Exceções de cálculo

Para exceções de cálculo, onde o cálculo é feito somente para determinados tipos de clientes ou fornecedor ou em condições específicas, há as seguintes alternativas:

* Cadastros > Clientes e Fornecedores > Fornecedores > Ligações > Fornecedor X Produtos > Individual (F403FPR)
* Cadastros > Clientes e Fornecedores > Clientes > Ligações > Cliente X Produto > Agrupado (F075PCA), efetuar seleção por Estado, e vincular os códigos cadastrados acima, conforme o estado do cliente;

Utilizar o identificador de regras COM-000ALSUB01, ligando a uma regra para alterar o cálculo, conforme o estado;

Utilizar o identificador de regras COM-000ALSUB02, ligando a uma regra para alterar o código de Substituição Tributária do ICMS, conforme o estado.

## 1.9. ICMS ST Responsável Solidário

**Parametrizações necessárias para apuração do cálculo do imposto:**

Cadastrar o imposto em F051IMP com o tipo 31
- ICMS Substituto Retenção.  
Cadastrar na filial o código do imposto em
F055PPF.  
Para esse imposto não é preciso cadastrar uma tabela de tributação.  
No menu
F661PAI
informar o código da filial e o período desejado, clicar no botão MOSTRAR e selecionar o código do imposto e CALCULAR. Irá abrir a tela de apuração do cálculo do
ICMS Substituto Retido, serão demonstrados os valores e para gravar a apuração clicar no botão PROCESSAR.

Não é permitido informar exceções de base de cálculo
para o imposto do tipo 25 - Outras Retenções.

Na apuração do cálculo do Imposto ICMS Substituto Retido são demonstrados os valores do imposto
ICMS Substituto Retenção que foram creditados e os valores que foram debitados, conforme
abaixo:

* Valores Creditados:

### No campo 1 - Imposto Pelas Entradas

Para este campo será buscado o Valor de Retenção (E660NFC.VLRRIS)
das notas fiscais entrada que não são de devolução (E660NFC.TIPNFE
<> 2 e 3)

* Valores Debitados:

### No campo 1 - Imposto Pelas Saídas

Para este campo será buscado o Valor de Retenção (E660NFV.VLRRIS) das notas fiscais de saída que não são de devolução (E660NFV.TIPNFS <> 2).

Movimentos de Redução Z cancelados não serão considerados.  
As notas fiscais de entradas e saídas para serem consideradas na apuração precisam
estar integradas no módulo de Impostos.  
Os valores referentes a Outros Créditos e Outros Débitos poderão serem
preenchidos
manualmente.  
O cálculo do ICMS Substituto Retido será composto pela somatória do campo 1 - Imposto
Pelas Entradas e todos os valores dos campos da coluna N. F. Saída.  
Os demais campos da coluna N. F. Entrada irão deduzir no valor a recolher.
O valor a recolher será gerado no campo Imposto a Recolher.  
Para gravar a apuração do cálculo é preciso clicar no botão PROCESSAR a apuração do cálculo é gravada, com isso, ao
sair da tela e acessá-la novamente no mesmo período, os valores da última apuração
são demonstrados.  
Caso desejar apurar novamente, apresentará a mensagem:

Ao clicar no botão Não a apuração não é concluída, permitindo o
usuário informar novos valores na apuração.  
Ao clicar no botão Sim as informações serão gravadas na apuração, onde
apresentará a mensagem:

O processo de apuração poderá ser feito quantas vezes forem necessárias.

### Quando a Filial for Totalizadora

Será gerado neste campo a somatória do campo VLRRIS (Valor de ICMS Substituto Retenção) das notas de saída.

Descrição atribuída no campo: Saídas - Retenção ICMS Substituto.

## 1.10. ICMS ST no preço unitário do produto

Existe alguma forma de somar o valor do ICMS ST no preço unitário dos itens da NF?

Não existe uma forma de somar o valor do ICMS ST no preço unitário dos itens, o que existe é o parâmetro Soma Líq da tela F019TIS que permite definir se o valor do ICMS ST será somado no campos 'Valor Produtos / Líquidos Outros' e 'Valor Líquido / Financeiro'.

## 1.11. ICMS ST destacado

Se na nota de entrada houve cálculo de ICMS ST e a tabela de ICMS ST estiver parametrizada para não calcular imposto na saída quando já houve cálculo para o produto na entrada, nesse caso o ICMS ST destacado é calculado

Para gerar o valor de ICMS substituído destacado, o sistema verifica a base do ICMS substituído destacado e multiplica pelo percentual do ICMS substituído da última entrada por compra. Porém, quando o identificador de regras VEN-000ALISD01 estiver ativo, o valor do ICMS Substituído tem como base o item de produto que está sendo calculado, isso por meio do campo **Valor unitário de ICMS Substituído na última entrada (E075DER.VLRUIS)**, que depois é multiplicado pela quantidade do produto na nota fiscal. Este é o valor que originalmente será enviado para a regra. É possível manipular o valor do ICMS ST destacado pelo identificador VEN-000PRUIS01.

Quando os campos destacados na figura estiverem preenchidos, significa que o produto já calculou ICMS ST na entrada.

* Cadastros > Produtos e Serviços > Ligações > Produto X Fabricante > Individual (F075PPF)

![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/images/imposto_icms_st017_thumb_0_48.png)

Verificar se a tabela de ICMS ST está configurada para calcular imposto na saída quando já houve cálculo na entrada. O campo Calc. ST saída com St Entrada deve ser igual a **N-Não**.

* Cadastros > Mercado e Suprimentos > Parâmetros Fiscais > Substituições Impostos > Modalidade Base Cálculo (F019TIS)

ICMS ST destacado calculado na nota.

![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/images/imposto_icms_st019_thumb_0_48.png)

O valor do ICMS ST destacado é calculado multiplicando o valor unitário do ICMS ST encontrado nos parâmetros fiscais do produto pela quantidade no item da nota.

**Observação**

Na geração de notas fiscais de saída, os valores de **ICMS ST Destacado** serão gerados apenas quando o **Código da situação tributária** terminar em 60 ou for igual a 500.

## 1.12. Redução da Base de Cálculo e Alíquota Diferenciada

O ERP conta com a parametrização da alíquota diferenciada e redução da base de cálculo de duas formas:

1. Quando é operação direta do contribuinte, tanto na entrada como na saída, na parametrização são utilizadas as estruturas de alíquota por estado, ICMS especial e a parametrização de redução de base de cálculo.
2. Quando é operação de substituição tributária, toda a parametrização ocorre nas configurações de ST. O documento de compra, por exemplo, deve possuir na configuração da substituição tributária as parametrizações correspondentes à possível venda no estado da filial, aplicando a alíquota interna prevista ou especial e a redução da base de cálculo. Na tela de substituição tributária, ocorre também a parametrização para uma operação de venda (substituto) com a configuração dos parâmetros conforme o estado de destino, aplicando a alíquota interna ou especial e a redução da base de cálculo descrita na legislação do estado destino.

Diante dessas possibilidades de parametrização do ERP, abaixo estão descritos os cenários de compra com ou sem redução de base de cálculo nas diversas combinações. A aplicação da redução da base de cálculo sobre a valor da nota fiscal de venda a consumidor final deve ser aplicado na composição da base de cálculo, e não sobre a alíquota, tornando-a efetiva.

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Estado de origem **sem** redução e estado de destino **com** redução | | Estado de origem **com** redução e estado de destino **sem** redução | | Estado de origem **com** redução e estado de destino **com** redução | | Estado de origem **sem** redução e estado de destino **sem** redução | |
| Vlr. Merc. Compra | R$1.000,00 | Vlr. Merc. Compra | R$ 1.000,00 | Vlr. Merc. Compra | R$ 1.000,00 | Vlr. Merc. Compra | R$ 1.000,00 |
| % Red BC | 0% | % Red BC | **50%** | % Red BC | **50%** | % Red BC | **0%** |
| BC ICMS | R$ 1.000,00 | BC ICMS | R$ 500,00 | BC ICMS | R$ 500,00 | BC ICMS | R$ 1.000,00 |
| % | 12% | % | 12% | % | 12% | % | 12% |
| Vlr ICMS | R$ 120,00 | Vlr ICMS | R$ 60,00 | Vlr ICMS | R$ 60,00 | Vlr ICMS | R$ 120,00 |
| - | - | - | - | - | - | - | - |
| % MVA | 70% | % MVA | 70% | % MVA | 70% | % MVA | 70% |
| % Red BC ST (interno) | **40%** | % Red BC ST (interno) | 0% | % Red BC ST (interno) | **40%** | % Red BC ST (interno) | **0%** |
| BC ST s/ red | R$ 1.700,00 | BC ST s/ red | R$ 1.700,00 | BC ST s/ red | R$ 1.700,00 | BC ST s/ red | R$ 1.700,00 |
| BC ST | R$ 1.020,00 | BC ST | R$ 1.700,00 | BC ST | R$ 1.020,00 | BC ST | R$ 1.700,00 |
| % ST (alíquota interna) | 18% | % ST (alíquota interna) | 18% | % ST (alíquota interna) | 18% | % ST (alíquota interna) | 18% |
| Vlr ST | R$ 63,60 | Vlr ST | R$ 246,00 | Vlr ST | R$ 123,60 | Vlr ST | R$ 186,00 |
| - | - | - | - | - | - | - | - |
| Venda cons. Final | R$ 2.000,00 | Venda cons. Final | R$ 2.000,00 | Venda cons. Final | R$ 2.000,00 | Venda cons. Final | R$ 2.000,00 |
| BC para complementação | R$ 1.200,00 | BC para complementação | R$ 2.000,00 | BC para complementação | R$ 1.200,00 | BC para complementação | R$ 2.000,00 |
| Apuração ERP | | Apuração ERP | | Apuração ERP | | Apuração ERP | |
| C | D | C | D | C | D | C | D |
| R$ 183,60 | R$ 216,00 | R$ 306,00 | R$ 360,00 | R$ 183,60 | R$ 216,00 | R$ 306,00 | R$ 360,00 |
|  | R$ 32,40 |  | R$ 54,00 |  | R$ 32,40 |  | R$ 54,00 |
| Apuração Lei | | Apuração Lei | | Apuração Lei | | Apuração Lei | |
| BC | R$ 180,00 | BC | R$ 300,00 | BC | R$ 180,00 | BC | R$ 300,00 |
| Valor | R$ 32,40 | Valor | R$ 54,00 | Valor | R$ 32,40 | Valor | R$ 54,00 |

Conforme art. 25-A, inciso II, nota 02 do decreto Nº 54.308/2018, será considerado, quando houver, o benefício da redução de base de cálculo. Assim, quando realizada uma venda a consumidor final de R$ 2.000,00 e o produto for beneficiado pela redução de base de cálculo (configuração de redução de base de cálculo para o estado da filial) de 40%, por exemplo, a base de cálculo efetiva a ser considerada no cálculo do imposto 70 deve ser de R$ 1.200,00. A alíquota considerada, nesse caso, é apenas a alíquota de ICMS especial ou a alíquota interna padrão, sem apresentar a alíquota efetiva aplicando a redução de base de cálculo.

* Controle de Entrada de Produtos (F075CEP) - Redução da Base de Cálculo

## 1.13. Cálculo do Imposto ICMS Diferencial de Alíquota EC 87/15

ICMS Diferencial de Alíquota EC 87/15 - Imposto sobre Circulação de Mercadorias e Serviços cobrado nas operações interestaduais com consumidor final.

* Cadastrar o imposto na tela Cadastro de Imposto (F051IMP), com o tipo 63 - Dif. Alíq. do ICMS interestadual com consumidor final;

> Quando for cadastrado um imposto do tipo 63 - Dif. Alíq. do ICMS interestadual com consumidor final o recolhimento dos impostos do DIFAL e Fundo de Combate a Pobreza (FCP) serão realizados de forma conjunta, na mesma guia de recolhimento. Para que o FCP seja gerado em uma guia de recolhimento específica, deve ser cadastrado o imposto do tipo 64 - FCP - Fundo de Combate a Pobreza e ligado a transação de venda. Assim, o recolhimento é gerado de forma separada.

* Cadastrar na filial o código do imposto na tela Configuração de Impostos para a Fiial (F055PPF) e cadastrar na guia Estado os estados que serão calculados para este imposto.   
  Para esse imposto não é possível cadastrar uma Tabela de Tributação;
* Na tela Apuração de Impostos (F661PAI), informar o código da filial e o período desejado, clicar no botão Mostrar e selecionar o código do imposto e clicar no botão Calcular. Irá abrir a tela de apuração do cálculo do ICMS Diferencial de Alíquota EC 87/15, serão demonstrados os valores e para gravar a apuração clicar no botão Processar ou no botão Todos.   
  Neste cálculo temos os botões de navegação na tela, para poder mudar conforme o estado do cálculo do imposto.

Na apuração do cálculo do Imposto ICMS Diferencial de Alíquota EC 87/15 por Estado são demonstrados os valores do imposto ICMS Diferencial de Alíquota e Fundo de Combate à pobreza que foram creditados através das notas fiscais de entradas devolução e os valores que foram debitados através das notas fiscais de saídas.

As notas fiscais de entradas e saídas para serem consideradas na apuração precisam estar integradas no módulo de Tributos.

Na guia Origens, são demonstrados todas as Naturezas de Operações com os seus movimentos de entradas e saídas que foram considerados na apuração.

Os valores referentes a Outros Créditos, Outros Débitos, poderão ser alterados manualmente.

Os campos Deduções 1 e Deduções 2 podem ser preenchidos manualmente, lembrando que todos esses campos influenciaram no resultado da apuração.

O cálculo do ICMS Diferencial de Alíquota EC 87/15 é baseado no total dos Créditos menos o total dos Débitos, sendo que, quando esse cálculo gera um resultado credor o valor é gerado no campo Saldo Credor se não houver filial Totalizadora. Quando houver filial Totalizadora este valor será gerado nesta filial, apresentará o seguinte LOG: IMPOSTO XX ESTADO XX: Saldo credor do imposto do período anterior, no valor de R$ XX,XX será considerado juntamente no cálculo da filial totalizadora XX.

Quando isso ocorre, para o próximo período apurado, o valor desse campo passa a ser gerado no campo Saldo Período Anterior.

Quando o resultado é devedor o valor é gerado no campo Imposto a Recolher. Quando o cálculo não atinge o valor mínimo para geração de título e guia, não será considerado o valor acumulado no cálculo do mês seguinte.

Ao clicar no botão Processar a apuração do cálculo é gravada e será gerado um LOG Informativo. Também pode-se clicar no botão Todos a apuração será gerada para todos os estados ligados ao imposto, gerando um LOG informativo.

Ao sair da tela e acessá-la novamente no mesmo período, os valores da última apuração são demonstrados.

Caso desejar apurar novamente, será apresentada uma mensagem informando que o imposto já foi apurado parao período, além de questionar se deve sobrepor, conforme opções:

* **Sim:** as informações serão gravadas na apuração, onde apresentará o seguinte LOG: IMPOSTO: XX ESTADO XX : Gravação da apuração concluída com sucesso!   
  O processo de apuração poderá ser feito quantas vezes forem necessárias;
* **Não:** a apuração não é concluída, permitindo o usuário informar novos valores na apuração.

## 1.14. ICMS ST recolhido pelo fornecedor com margem de lucro menor que a determinado pela legislação vigente

O art. 15 do anexo XV do RICMS/MG coloca a seguinte situação

O estabelecimento destinatário de mercadoria submetida ao regime de substituição tributária relacionada na Parte 2 deste Anexo, inclusive o varejista, é responsável pelo imposto devido a este Estado a título de substituição tributária, quando o alienante ou o remetente, sujeito passivo por substituição, não efetuar a retenção ou efetuar retenção a menor do imposto.

Com isso, quando o fornecedor fizer o recolhimento do ICMS ST considerando uma margem de lucro menor que a determinada pela legislação vigente, o comprador deverá destacar o ICMS ST faltante como recolhido solidariamente na nota fiscal, sendo que os valores serão carregados para o Controle de Entrada de Produtos. O valor do ICMS ST do Controle será totalizado com o valor do ICMS ST normal mais o ICMS ST solidário (VlrIcs + VlrRis) existentes na nota fiscal de compra.

Demais estados possuem a mesma orientação, por exemplo SC no art. 17 § 4º do anexo 3 do RICMS/SC.

Assim, uma nota fiscal de compra cuja operação deve ter ICMS ST pode se enquadrar nas seguintes situações:

1. O fornecedor calcula integralmente o valor do ICMS ST e já soma esse valor à nota fiscal. Nesse caso, o sistema atende com o preenchimento dos campos de ICMS substituído;
2. O fornecedor não calcula o valor do ICMS ST e o comprador solidariamente aplica o cálculo e faz o recolhimento em favor do estado. Nesse caso, o sistema atende com o preenchimento dos campos do ICMS substituto por responsabilidade solidária;
3. O fornecedor calcula o valor do ICMS ST e já soma o valor ao da nota fiscal, porém ele é inferior ao valor total que deveria ser recolhido para o estado do comprador. Dessa forma, o comprador deve calcular o valor do ICMS ST solidariamente e complementar o valor faltante. Nesse caso, a nota fiscal de compra terá valor no campo ICMS substituído e ICMS substituto por responsabilidade solidária, sendo que a soma dos 2 campos irá compor o valor total do ICMS ST na entrada.

### Exemplo

Compra interestadual de um produto com ICMS ST no valor de R$ 1.000,00.  
% ICMS = 12%  
Valor do ICMS = 1.000 x 12% = 120,00

MVA utilizada pelo fornecedor = 50%  
Base ICMS ST = 1.000 + 50% = 1.500,00  
% ICMS ST = 18%  
Valor ICMS ST = 1.500 \* 18% = 270 - 120 = 150,00

MVA correta = 60%  
Base ICMS ST = 1.000 + 60% = 1.600,00  
% ICMS ST = 18%  
Valor ICMS ST = 1.600 \* 18% = 288 - 120 = 168,00

Na entrada da nota fiscal, deve-se calcular o ICMS ST retido para complementar o valor do ICMS ST e chegar no valor de 168,00.

**Cálculo do ICMS ST retido (solidário)**:  
MVA = 60%  
Base ICMS ST = 1.000 + 60% = 1.600,00  
% ICMS ST = 18%  
Valor ICMS ST retido (Solidário)= 1.600 \* 18% = 288 - 120 - 150 = 18,00

## 1.15. Presunção por preço de pauta

Durante a inicialização/carga da nota fiscal de entrada para o Controle de Entrada e Saída de um item que não possui valor de ICMS ST no documento fiscal, esse valor pode ser presumido conforme parametrização do produto. Caso ele possua uma parametrização de substituição tributária pelo preço de pauta, o cálculo do ICMS ST presumido considerará o valor de pauta. A fórmula de cálculo para esse cenário se diferencia pela forma de composição da base, que parte de um valor de pauta unitário publicado pelo governo e multiplicado pela quantidade da entrada.

A definição da base de cálculo será da seguinte forma:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| E019TST.CALSUB | Critério | E019SUB.DEFBCS | Descrição | Base |
| 1 | Pela margem de lucro | - | - | E440Ipc.VlrBru ou E660Inc.VlrMrc |
| 2 | Pelo preço unitário base | 1 | Considerar preço da tabela de preço | E081ITP.PREBAS |
| 2 | Pelo preço unitário base | 2 | Considerar o menor preço | E440Ipc.VlrBru\E660Inc.VlrMrc ou E081ITP.PREBAS o que for menor |
| 2 | Pelo preço unitário base | 3 | Considerar o maior preço | E440Ipc.VlrBru\E660Inc.VlrMrc ou E081ITP.PREBAS o que for maior |

Ou seja, durante o cálculo da presunção dos movimentos de entrada, quando para o estado da filial a tabela de substituição possuir o critério para cálculo de substituição **(E019TST.CALSUB)** igual a **1 - Pela Margem de Lucro**, será aplicado o cálculo do MVA normalmente. Caso seja igual a **2 - Pelo Preço Unitário Base**, será considerada como base de cálculo do Controle o valor definido na tabela de preço, multiplicado pela quantidade da nota fiscal.

Após isso, será analisado o parâmetro **Definição da Base de Cálculo Substituição (E019SUB.DEFBCS)** para compor a base de cálculo do Controle. Caso a opção seja igual a:

1. **Considerar o valor da tabela de preço:** base de cálculo recebe o valor da tabela de preço (E081ITP.PREBAS), multiplicado pela quantidade da nota fiscal;
2. **Comparar a quantidade da nota fiscal e o valor da tabela de preço:** base de cálculo recebe o **menor** preço, multiplicado pela quantidade da nota fiscal.
3. **Comparar a quantidade da nota fiscal e o valor da tabela de preço:** base de cálculo recebe o **maior** preço, multiplicado pela quantidade da nota fiscal.

## 1.16. ICMS ST nas Notas Fiscais de Entrada

O cálculo da substituição tributária é feito com base no cadastro do código de substituição tributária na tela F019TIS pela UF do fornecedor.

**Observação**

Quando houver retenção de ICMS ST (vide tópico 1.4. Geração de títulos – ICMS ST Retenção – Guia de Recolhimento) o sistema gerará o título para a UF da filial de entrada da nota.

## 1.17. ICMS ST nas Notas Fiscais de Entrada - Fornecedor Simples Nacional

Parametrizações:

* Cadastro de Fornecedores (F095CAD):
  + Código do Regime Tributário (Simples Nacional);
  + % ICMS.
* Cadastro de Clientes (F085CAD):
  + Na guia Cadastro, o campo Cliente Contribuinte ICMS deve ser preenchido com "S - Sim".

  **Observação**

  É necessário que o fornecedor esteja vinculado nos cadastros de clientes e fornecedores, respectivamente nos campos Cliente como Fornecedor (F085CAD) e o Fornecedor como Cliente (F095CAD).
* Cadastro de Produtos (F075PRO):
  + Código ICMS Especial;
  + Código ICMS Substituído.
* Parâmetros da Filial para Tributos (F070FEF):
  + Na guia Impostos 2, o Código do Regime Tributário deve ser preenchido com "3 - Regime Normal".
* Transações de Compras (F001TCP):
  + Na guia ICMS:
    - Recupera ICMS deve ser preenchido com "S - Sim";
    - Calcula Diferença Alíquota deve ser preenchido com "S - Sim".
* Tipos Substituições Impostos / Modalidade Base Cálculo / Antecipação - Por Estado (F019TIS):
  + Cadastrar o imposto substituição (para o estado do fornecedor simples nacional);
  + Aplicação Subst. deve ser preenchido com "A - Ambos" ou "E - Entrada";
  + Tipo Desconto ICMS deve ser preenchico com "4 - Descontar ICMS Normal" aplicando redução BC ICMS ST);
  + Regime Tributário deve ser preenchido com "1 - Simples Nacional".
* ICMS Especial - Por Estado (F019TIE):
  + Cadastrar o imposto especial para a filial e estado (fornecedor).
* Parâmetros por Estado (F009PPE):
  + Cadastrar os parâmetros para Filial e Estado (fornecedor);
  + Cadastrar todas as alíquotas (% ICMS);
  + Cadastrar Transação NF Produtos Adquiridos (transação de compra).
* Na Nota (Itens):
  + Sugestão do Código ICMS Especial, como já faz com o Código ICMS Substituído;
  + Cálculo de ICMS Substituições: (Quando atender as validações e as parametrizações acima usar o cálculo): ICMS Subst = (Base ICMS Substituições \* % ICMS (Parâmetros por Estado)) - (Base ICMS Simples Nacional \* % ICMS (e019icm (ICMS Especial) ))

**Importante**

Para que a memória de cálculo ICMS Subst = (Base ICMS Substituições \* % ICMS (Parâmetros por Estado)) - (Base ICMS Simples Nacional \* % ICMS (e019icm (ICMS Especial) )) seja realizada, é imprescindível que seja realizado o cálculo do ICMS Simples Nacional no item da nota fiscal.

## Páginas relacionadas

* [Modalidade Base Cálculo](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f019tis.htm)
* [Fatura](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f001tcp.htm)
* [Vendas](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f001tve.htm)
* [Individual](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075pro.htm)
* [Individual](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f403fpr.htm)
* [COM-000ALSUB01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/com_000alsub01.htm)
* [COM-000ALSUB02](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/com_000alsub02.htm)
* [Guias de recolhimento](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f051gui.htm)
* [Cadastro](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f051imp.htm)
* [Cadastro (F009PPE):](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f009ppe.htm)
* [Base imposto (Liga Filial) (F055PPF)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f055ppf.htm)
* [Configuração para geração de títulos de impostos (F001TIT)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f001tit.htm)
* [CPR-440GERTI01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/cpr_440gerti01.htm)
* [Parâmetros Fiscais de produtos e serviços por filial e estado (F070PSE)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070pse.htm)
* [Agrupado](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075pca.htm)
* [F661PAI](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f661pai.htm)
* [Individual](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075ppf.htm)
* [Controle de Entrada de Produtos (F075CEP) - Redução da Base de Cálculo](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075cep.htm#reducao-base)
* [F095CAD](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f095cad.htm)
* [F085CAD](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f085cad.htm)
* [F070FEF](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070fef.htm)
* [F019TIE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f019tie.htm)
