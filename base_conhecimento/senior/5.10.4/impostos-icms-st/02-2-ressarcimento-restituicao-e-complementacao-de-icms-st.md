# 2. Ressarcimento, Restituição e Complementação de ICMS ST

> **Fonte:** ICMS ST — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/impostos-icms-st.htm  
> **Trilha:** Ajuda por telas > Controladoria > Gestão de Tributos > Operações e Cálculos Fiscais > Cálculos > Apuração > F661IA5  
> **Telas citadas:** E012CLF, E019SUB, E022CLF, E070VEN, E075BAR, E075DER, E075PRO, E440IPC, E660INC, E660INV, E660RSC, E660RSV, F009PPE, F019TIS, F070EMP, F070PSE, F075APF, F075CEP, F075GFP, F075PFI, F075PRO, F085CAD, F140GNF, F140PRE, F440GNE, F660CRS, F660GDG  
> **Identificadores de regras:** —

---
A legislação dos estados para a restituição ou complementação do ICMS ST abrangem os contribuintes varejistas e não varejistas, visando apurar a diferença do resultado da aplicação da alíquota interna no estado sobre o valor efetivo da venda aos consumidores finais pelo valor ICMS ST pago nas compras de produtos sujeitos a substituição tributária.

![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/images/restituicao-e-complemento-icms-st/icms-st-processo-completo_thumb_0_48.png)

## 2.1. Ressarcimento de ICMS ST

O contribuinte poderá solicitar o ressarcimento do valor pago quando ocorrer uma bitributação do imposto. Isso acontecerá quando:

* o substituto recolher uma nova retenção sobre a mesma operação;
* realizar retenção para qual a mercadoria não esteja sujeita ao regime de ST;
* efetuar operações para consumidor final não contribuinte do imposto localizado em outra unidade da federação sujeito ao DIFAL e entre outras situações.

O arquivo do SPED Fiscal possui o registro C176 para o ressarcimento do ICMS ST, utilizando-se de um leiaute padrão para que outros estados possam utilizar desta informação para que os seus contribuintes realizem os seus respectivos pedidos de restituição deste valor.

## 2.2. Restituição de ICMST ST

Alguns estados possibilitam que seus contribuintes que são substituídos tributariamente, sejam também o substituto tributário nas vendas interestaduais. Ou seja, o fornecedor já calcula o valor do ICMS ST a ser cobrando do contribuinte, e o contribuinte, na sua venda, também deve apurar e recolher o ICMS ST do seu cliente, ou realiza a venda tributada de ICMS normal. Com isso, ocorre uma bitributação onde o contribuinte paga o ICMS ST na entrada e tem uma tributação na venda. Assim, esse contribuinte tem o direito da restituição do valor do ICMS ST pago na entrada, correspondente a esta venda tributada, rastreada pelo controle do PEPS.

Este pedido de restituição do ICMS ST é aplicado para o estado de Minas Gerais, por meio da entrega dos registros 88STES e 88TIT junto ao arquivo do Sintegra para este estado.

O estado de São Paulo possui a Portaria CAT 42/2018 com o seu arquivo correspondente para realizar o envio destas informações do pedido de restituição do ICMS ST.

Outro desafio para o pedido de restituição do ICMS ST são as constantes alterações nas legislações estaduais incluindo ou removendo produtos para o controle do regime tributário de substituição tributária. Quando um produto que já está em operação pelas empresas entram neste controle, o contribuinte deve realizar uma contagem do produto na data da entrada nesse controle, e baseado no valor do custo de aquisição, deve aplicar o cálculo do MVA estabelecido para este produto com a alíquota interna do estado, para que o contribuinte realize o recolhimento do ICMS ST, via guia de recolhimento, sobre os produtos que estão em estoque e que entraram nesse controle. Caso um destes produtos saiam do controle do regime tributário de substituição tributária, esse mesmo cálculo deve ser realizado, porém o valor será utilizado como crédito na sua apuração do ICMS.

Para esse cenário de inclusão do produto no regime tributário de substituição tributária, o ERP possui a apuração do imposto tipo 99, onde o imposto é parametrizado com os produtos e a configuração de substituição tributária correspondentes. Feita a apuração, o título a pagar e a guia de recolhimento serão gerados para que o contribuinte faça o seu recolhimento. Como o contribuinte realizou o recolhimento do ICMS ST via apuração, para que ele possa ter o direito da restituição do ICMS ST nas futuras vendas tributadas, ele precisa acessar a tela Manutenção de Controle de Entrada de Produtos para realizar a carga das notas fiscais desses produtos, como já indicado anteriormente.

Além disso, como estas notas fiscais de compra não possuem valor de ICMS ST, na tela Manutenção de Controle de Entrada de Produtos deve-se utilizar a opção Alterar Entradas para que seja imputado o código de substituição tributária a esses itens de notas fiscais, conforme o código que foi utilizado na apuração do imposto 99.

Com isso, o valor do ICMS ST apurado e recolhido pelo imposto 99 será atribuído a cada um dos documentos de entrada de forma proporcional ao número de aquisição de cada um desses itens.

## 2.3. Complementação de ICMS ST

Alguns estados brasileiros estão exigindo aos seus contribuintes que efetuam vendas a consumidor final no seu próprio estado, para que realizem uma apuração confrontando o valor da operação de venda para esses consumidores finais versus o valor efetivo cobrado como ICMS ST na sua respectiva compra. Essa apuração ocorre por meio do imposto 70 - ICMS ST complementar, que define se o contribuinte possui valor de ICMS ST a complementar para o seu estado, ou valor do ICMS ST a restituir nessas operações de venda ao consumidor final.

## 2.4. Parametrizações necessárias

Para calcular o imposto a ser recolhido/complementado do ICMS ST, é necessário que a empresa esteja configurada para calcular o ICMS ST e, depois, ativar o registro das entradas e saídas para controle do imposto, dando a carga inicial na rotina de Controle de Entrada e Saída.

### 2.4.1. Controle de Entrada e Saída

![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/images/restituicao-e-complemento-icms-st/icms-st-controle-de-entrada-e-saida_thumb_0_48.png)

1. Configure a empresa para calcular ICMS;
2. No cadastro de empresa, configure o campo Registra entrada e saída dos produtos igual a Sim;
3. No cadastro de parâmetros fiscais ou família, configure o campo Registra entradas e saídas para controle de impostos igual a Sim;
4. Realize o processo de Controle de Entrada de Produtos, que tem por objetivo inserir automaticamente nas estruturas de controle de entrada de produtos os cupons e notas fiscais de compra/entrada/venda indicados para serem controlados;
   1. se o período a ser processado não estiver completo, é necessário inicializar o Controle de Entrada e Saída pelo saldo do inventário fiscal.
   2. para utilizar a opção, o sistema deverá estar habilitado para controlar entrada de produtos (F070EMP.RegEsp);
   3. produtos que possuem direito ao ressarcimento do ICMS ST deverão estar previamente parametrizados em Parâmetros Fiscais.

Observação

Serão gravados os movimentos de Entrada e Saída de estoque quando não relativos a documentação fiscal conforme filtros abaixo:

* Entrada ou Saída (ESTEOS = E ou S);
* Não relacionado a nota fiscal (NUMNFC e NUMNFV = 0);
* Quantidade maior que ZERO (QTDMOV > 0);
* Tipo de Estoque Movimentado da Transação igual a **NO-Normal**.

Movimentos gerados a partir do estoque e que foram integrados para este campo não possuem ICMS e ICMS ST, exceto quando houver parametrização desses impostos em Manutenção de Controle de Entrada de Produtos.

#### Controlar produtos com ICMS ST entre filiais em estados diferentes

Quando uma empresa possui duas ou mais filiais em estados diferentes e comercializa produtos com ICMS ST em um estado, enquanto em outro o produto não é controlado pelo ICMS ST, este último não pode ser considerado no Controle de Entrada e Saída; o primeiro, sim.

**Exemplo:** no estado de SC, o produto A não tem ICMS ST. No estado do RS, sim; ou seja, deve passar pelos processos de ressarcimento, restituição e complementação. Como o processo parte do produto registrado nas estruturas de Entrada e Saída, se o produto para determinada filial não estiver no Controle, ele não será apresentado na declaração para o estado. Diante disso, é necessário parametrizar a nível de filial se o produto deve ou não entrar no Controle:

Ao tratar uma nota/cupom fiscal, o sistema analisa o conteúdo do campo **Reg. entradas e saídas para controle de impostos** das telas F075PFI/F075APF, juntamente com as parametrizações das telas F075PRO/F075GFP:

* **Quando não há ligação do produto com a filial**: o sistema gera um registro no Controle de Entrada e Saída de produtos apenas se na derivação for informado **S-Sim** para o campo **Reg. entradas e saídas para controle de impostos**;
* **Quando há ligação do produto com a filial:** o sistema gera um registro no Controle de Entrada e Saída de produtos apenas se na derivação e na ligação for informado **S-Sim** para o campo **Reg. entradas e saídas para controle de impostos**;
* Caso contrário, o sistema não gera um registro no Controle de Entrada e Saída de produtos.

## Cálculo do ICMS para o Controle de Entrada e Saída

Para a gestão do Controle de Entrada e Saída, é necessário preencher os valores de base e imposto referentes ao ICMS. Ao gerar a carga na estrutura de Entrada e Saída, a base de cálculo do ICMS deve ser a soma dos valores de isentos e outros de ICMS. Caso não aconteça a identificação e composição da base de cálculo do ICMS a partir de isentos e outros, esse valor deve ser apurado a partir da base de cálculo do ICMS ST retido anteriormente ou do ICMS ST responsável solidário e a configuração de MVA previsto no código de substituição tributária, indicada no item da nota fiscal ou no cadastro do produto. Se for utilizado o MVA, a fórmula a ser aplicada será:

* BC ICMS = (BC ICMS ST / (% MVA / 100)) / ((1 / (%MVA / 100)) + 1)

Se existir o percentual no item da nota fiscal, ele deve ser considerado. Caso não, deve aplicar a busca da sugestão do percentual de ICMS baseado em todos os parâmetros já existentes no ERP (ICMS especial e parâmetros por estado).

O valor do ICMS será o resultado da aplicação da base de cálculo pela alíquota de ICMS encontrada anteriormente.

Esse cálculo do ICMS para o controle de Entrada pode ser aplicado sempre que a nota fiscal de entrada possuir ICMS ST retido anteriormente ou ICMS ST responsável solidário (e não possuir valores de ICMS na nota fiscal de compra).

## Estado do RS

É possível efetuar o cálculo do ICMS ST efetivo sobre as vendas internas ao consumidor final, não importando se a compra relacionada possui ou não valor de crédito:

* quando o parâmetro global CalEfeSol estiver definido como **S-Sim**, o sistema calculará o imposto efetivo nas saídas, mesmo que a entrada relacionada não possua crédito de ICMS ST (F075CEP e F140GNF/F140PRE);
* o sistema realizará a presunção para o movimento de entrada cuja data seja inferior ou igual a data informada no parâmetro global PerLimSol (F075CEP e F440GNE).

Após isso, é necessário executar a tela F660GDG para todas as filiais e períodos e calcular o imposto 70. A inicialização dos campos do Controle ocorrerá da seguinte forma:

* **E660RSC.PerIcs**: conforme parâmetro da tela F070PSE, F019TIS ou F009PPE, mesmo não havendo crédito na entrada;
* **E660RSV.VlrTot, E660RSV.VlrBsc, E660RSV.VlrIsc, E660RSV.UniMed** e **E660RSV.CodStr**: serão preenchidos mesmo que a entrada relacionada com a saída não possua ICMS ST.

Não serão gravados no Controle as notas fiscais de entrada e inventário que cumprirem os requisitos abaixo:

1. Data de Entrada maior que a data do parâmetro global PerLimSol;
2. Estado da filial for Rio Grande do Sul;
3. Campos **ICMS ST Retido**, **ICMS ST Retido Anteriormente/Destacado** e **ICMS ST Retido Solidariamente** iguais a 0 (zero).

Importante

A F660GDG deve ser utilizada apenas para ajustar os registros de Controle de Entrada integrados anteriormente pela F075CEP.

### 2.4.2. Notas de compra

Uma vez implementado o Controle de Entrada e Saída, pode-se iniciar o lançamento das notas fiscais de entrada contendo produtos com ICMS ST:

![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/images/restituicao-e-complemento-icms-st/icms-st-compra_thumb_0_48.png)

## Compras com tributação de ICMS ST

1. Lance a nota de entrada contendo produtos que tributem ICMS ST. Consulte a documentação para configurar o cálculo do ICMS ST nas notas de compra e venda.
2. O valor do ICMS ST pode:
   * ter seu valor calculado nos campos de valor do ICMS ST que estão somando ao valor da nota fiscal e que foram recolhidos pelo fornecedor;
   * ter seu valor retido anteriormente para operações que utilizem o código CST x60 (contribuinte geral) ou CSOSN 500 (contribuinte Simples Nacional). Este valor deve estar destacado no XML do documento;
   * ser calculado com valor presumido, caso o imposto não tenha sido retido e a operação utilize o codigo CST x60 (contribuinte geral) ou CSOSN 500 (contribuinte Simples Nacional).

   #### Cálculo do valor presumido

   O cálculo da presunção é realizado com base no código da substituição informado no produto da nota fiscal de entrada (E440IPC.CodTst) ou no parâmetro global por filial **CodTstPre** - Código do ICMS Substituído para cálculo da presunção do ICMS ST no Controle de Entrada e Saída.  
   A forma utilizada no cálculo é:

   *Crédito presumido = Valor da operação + MVA de operação interna X alíquota interna*  
   *Crédito presumido = E440IPC.VlrBru + E019SUB.MarLuc x E019SUB.IcmEst*

   Quando a nota fiscal emitida com o CST 60 é integrada para o módulo de **Suprimentos**, e não teve o valor da base de cálculo do ST retido anteriormente unitário - valor do ICMS ST destacado para o ERP, devido a não obrigatoriedade, é calculada a presunção deste valor conforme a fórmula: *Valor da operação + MVA de operação interna x alíquota interna = Crédito presumido*. A regra é válida para os créditos de notas fiscais de compra e para os movimentos de estoque.

   Importante

   No Controle de Entrada de produtos, ao realizar o cálculo presumido do ICMS ST em uma situação de entrada com CST 060/500 onde não há o cálculo de ICMS próprio, o valor do ICMS Substituto no XML da NF-e fica zerado.

   Para o cálculo do ICMS ST Presumido, onde já seja realizado o desconto do ICMS Próprio do contribuinte substituto, o campo Tipo Desconto de ICMS, da tela Tipos Substituições Impostos / Modalidade Base Cálculo / Antecipação - Por Estado, deve estar parametrizado para descontar ICMS Normal (tipos 2 ou 3).
3. Armazene as notas de compra na fila de consumo. A nota pode ser consultada na tela de Manutenção de Controle de Entrada de Produtos.

### 2.4.3. Notas de venda/Cupons fiscais

![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/images/restituicao-e-complemento-icms-st/icms-st-venda_thumb_0_48.png)

#### Geração do arquivo .XML

A IN 48/2018 estabeleceu regras na geração do arquivo .XML para o preenchimento das tags nas operações com CST 60 ou CSOSN 500.

O Gestão Empresarial | ERP gera as tags referente ao ICMS ST da entrada de acordo com a operação para **Consumidor final** ou **Normal**, definido no campo Consumidor Final, guia Definições do Cadastro de Cliente (F085CAD).

* Operações não destinadas a consumidor final (Cliente normal): os valores do ICMS ST da entrada são gerados nas tags vBCSTRet, pST e vICMSSTRet;
* Operações destinadas a consumidor final (Cliente consumidor final): os valores do ICMS ST da entrada são gerados nas tags pRedBCEfet, vBCEfet, pICMSEfet e vICMSEfet.

Quando na entrada de itens com Substituição Tributária que não tiveram o ICMS ST Retido OU ICMS ST Destacado informado, o ERP realiza o cálculo presumido do ICMS ST. Esse cálculo consiste em uma presunção do ICMS ST retido anteriormente nas entradas em que não seja informado os respectivos valores.

O cálculo irá ocorrer quando:

* A base e valor ICMS ST estiverem zerados: não caracteriza entrada com ICMS ST Retido;
* A base e valor ICMS ST Destacado estiverem zerado: não caracteriza entrada com ICMS ST Retido anteriormente;
* Código da Situação Tributária CST de ICMS do produto (E440IPC.CodStr):
  + Para empresas regime tributário Normal: 60 - ICMS cobrado anteriormente por substituição tributária;
  + Empresas regime tributário Simples Nacional: 500 - ICMS cobrado anteriormente por substituição tributária (substituído) ou por antecipação.

## Geração do grupo <ICMS60>

Para geração do grupo <ICMS60> nas notas com as tags referentes ao ICMS Efetivo no XML são necessárias as seguintes condições:

1. No cadastro da filial, guia Documentos Eletrônicos, o parâmetro Gerar informações do ICMS Efetivo na NF-e deve estar informado igual a S - Sim;
2. O ERP irá gerar as tags de saída referente ao ICMS ST da entrada de acordo com a operação para Consumidor final ou Normal, definido no campo Consumidor Final, guia Definições do Cadastro de Cliente da tela de cadastro de clientes.
   * Operações não destinadas a consumidor final (Cliente normal): os valores do ICMS ST da entrada são gerados nas tags vBCSTRet, pST e vICMSSTRet;
   * Operações destinadas a consumidor final (Cliente consumidor final): os valores do ICMS ST da entrada são gerados nas tags pRedBCEfet, vBCEfet, pICMSEfet e vICMSEfet.
3. No cadastro do código de ICMS ST, o parâmetro Calc. ST Saída com ST Entrada deve estar informado igual a N - Não;
   * Este código de ST deve estar informado em um dos cadastros (Transação, Produto, Ligação Cliente X Produto...).
   * A Situação tributária informada no item deve ser X60.
   * O produto constante na NF-e deve ter valor de ICMS ST na entrada.
   * A operação deve ter ICMS ST.

   Obs.: A nota fiscal de saída não pode ter valor de ICMS ST, pois ele foi retido anteriormente e a operação de venda não é tributada.

Com isso, as tags referentes ao ICMS Efetivo são geradas no XML conforme exemplo abaixo:

![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/images/mercado/tag-grupo-icms.png)

#### Utilizar a mesma base de cálculo do ICMS ST da nota de entrada na nota de saída

Para que, ao gerar uma nota fiscal de saída de um produto controlado pelo PEPS, o valor base de cálculo de ICMS ST deste item seja o mesmo valor recebido na nota de entrada, é necessário configurar a substituição tributária para calcular a substituição na saída com a substituição da entrada. Esta configuração deve ser feita na tela Tipos Substituições Impostos / Modalidade Base Cálculo / Antecipação - Por Estado, configurando o campo Calc. ST Saída com ST Entrada com o valor **S–Sim**.

![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/images/processo-controle-entrada-saída-produtos/imagem-f019tis_thumb_0_48.png)

Desta forma, ao gerar uma nota de saída de um produto que foi adquirido com substituição tributária de ICMS, ou seja, na nota fiscal de entrada deste produto há valor de ICMS ST, o cálculo do ICMS ST na nota de saída será realizado com base no cálculo da nota de entrada. Por exemplo, se a nota de entrada possui quantidade 1.000,00 e valor base de ICMS ST de 10.000,00, e a nota de saída é gerada com quantidade 500,00, o valor base de ICMS ST da nota de saída será 5.000,00, sendo proporcional a quantidade de venda. Este cenário é aplicado às empresas atacadistas e distribuidoras no estado do Espírito Santo (ES).

#### Destaque de ICMS ST em vendas por comércios

Para que, ao gerar uma nota fiscal de saída de um produto controlado pelo PEPS, e nesta nota de saída tenha que ser destacado o valor de ICMS ST cobrado anteriormente (quando a CST da nota é igual a “X60”), seja utilizado o valor de ICMS ST da nota de entrada do respectivo produto, é necessário configurar a substituição tributária para buscar o ICMS ST da entrada. Esta configuração deve ser feita na tela Tipos Substituições Impostos / Modalidade Base Cálculo / Antecipação - Por Estado, configurando o campo Busca ICMS ST Ent. com o valor **S–Herdar base e valor proporcionalmente na venda** ou **M–Recalcular na venda a base de cálculo considerando MVA da entrada**.

![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/images/processo-controle-entrada-saída-produtos/imagem-f019tis-2_thumb_0_48.png)

Desta forma, ao gerar uma nota de saída de um produto que foi adquirido com substituição tributária de ICMS, ou seja, na nota fiscal de entrada deste produto há valor de ICMS ST, e esta nota de saída deve destacar o valor de ICMS ST cobrado anteriormente, serão buscados os valores de ICMS ST da respectiva nota de entrada do produto. Por exemplo, se estiver configurado para herdar a base de cálculo e o valor proporcionalmente na venda, se a nota de entrada possui quantidade 500,00 e valor de ICMS ST de 1.000,00, e a nota de saída é gerada com quantidade 250,00, o valor de ICMS ST da nota de saída será 500,00, sendo proporcional a quantidade de venda.

## Para vendas com tributação de ICMS ST

1. Nesse caso, a venda não é tributada pelo ICMS, pois ele já foi recolhido anteriormente. O CST na venda será novamente o X60.
2. O sistema irá localizar a nota fiscal de compra mais antiga do produto vendido com saldo de estoque, e fará a ligação com esta nota de venda;
3. Ao gerar o XML da NF-e, o sistema:
   1. Caso não exista ICMS ST retido anteriormente, ele verifica se existe ou não tributação do imposto na operação de venda;
   2. Caso exista ICMS ST retido anteriormente, é gerado o valor do imposto apresentado na nota fiscal de compra, proporcional a quantidade de venda.

## 2.5. Inicialização das médias e cálculo do imposto 70 - ICMS ST Complementar

**Importante**

  
As parametrizações abaixo são obrigatórias **somente** para filiais de estados cuja Tabela 5.7 já é tratada pelo ERP e que entregam informações de ressarcimento, restituição e complementação de ICMS ST no SPED Fiscal.

Antes de calcular o imposto 70 é necessário configurar a atualização da média móvel ponderada. Para isso, confira a documentação sobre Adequação aos leiautes 14 e 15 do SPED Fiscal, tópico Inicialização das médias. Após isso, confira o funcionamento da Apuração do imposto 70 (essa última sendo obrigatória, no momento, apenas para o estado do RS).

## 2.6. Ressarcimento - Simples Nacional

Os pontos de recálculo do ICMS ST no cenário do Simples Nacional são:

* F075CEP - Geração dos registros de tributos;
* F660CRS - Lançamento manual de uma saída (nota e cupom);
* Integração online: ao lançar a nota em **Mercado** (módulo) é gerado automaticamente um movimento em **Tributos**.

Para sugerir a base e valor do ICMS, ICMS ST e FCP, é necessário que o parâmetro **Direito ao ressarcimento de ICMS ST** da tela de Transações de Vendas esteja igual a **S-Sim**.

### Santa Catarina

O valor a ressarcir não é o valor correspondente a 100% da entrada. Será o resultado da multiplicação dos fatores previstos no § 5º do art. 127 RICMS/SC:

1. base de cálculo utilizada para apuração do imposto devido por substituição, excluída desta a parcela correspondente à MVA utilizada para o cálculo do imposto retido;
2. coeficiente correspondente a 70% (setenta por cento) do percentual de MVA original aplicável à operação;
3. coeficiente determinado pela equação: (1 - ALQ inter) / (1 - ALQ intra), em que:
   1. ALQ inter é o coeficiente correspondente à alíquota interestadual aplicável à operação; e
   2. ALQ intra é o coeficiente correspondente:
      * à alíquota interna aplicável sobre a operação substituída; ou
      * na hipótese de a operação substituída ser contemplada com redução de base de cálculo, ao percentual de carga tributária efetiva; e
4. coeficiente correspondente à alíquota interna incidente sobre a mercadoria.

**Exemplo:**

MVA Original 40%  
ALQ interestadual = 12%  
ALQ interna = 17%

MVA Ajustada = [(1+ MVA ST original) x (1 - ALQ inter) ÷ (1- ALQ intra)] -1  
MVA Ajustada = [(1+ 0,40) x (1 - 0,12) ÷ (1- 0,17)] - 1 = 0,4843

* Na compra, a nota fiscal está registrada com os seguintes valores:  

  Valor Mercadoria = R$ 1.000,00  
  BC ICMS = R$ 1.000,00  
  % ICMS = 12%  
  Vlr ICMS = R$ 120,00  

  MVA = 40%  
  MVA Ajustada = 48,43%  
  BC ICMS ST = R$ 1.484,30  
  % ICMS ST = 17%  
  Vlr ICMS ST = 252,33 - 120,00 = R$ 132,33
* Quando a partir dessa compra for realizada uma venda para um **contribuinte do estado de SC do Simples Nacional**, o valor a ressarcir deve ser:  

  **Item I:**  
  BC ICMS ST a ressarcir = 1.484,30 / (1 + 0,4843) = R$ 1000,00  

  **Item II:**  
  MVA = 40% \* 70% = 28%  

  **Item III:**  
  Coeficiente = (1 - ALQ inter)/ (1 - ALQ intra)  
  Coeficiente = (1 - 0,12)/ (1 - 0,17)  
  Coeficiente = 1,060240963855422  

  **Item IV:**  
  % ICMS interno = 17%  

  Valor a ressarcir = 1000 \* 28% \* 1,060240963855422 \* 17% = **R$ 50,47**.

Quando o **CodRtr** (Código do Regime Tributário) for igual a **1** ou **2** e **SigUfs** (Sigla da Unidade da Federação) for igual a **SC**, será gravado o valor de **R$ 50,47** em vez do valor da NF de entrada.no ICMS ST a ressarcir.

### Paraná

**Exemplo do cálculo de ressarcimento do Simples Nacional para o Paraná:**

E660RSV.VlrIcs = ((((E660RSC.VlrBsi / E660RSC.QtdEnt) / (1 + (E660RSC.PerMva / 100))) \* ((E660RSC.PerMva / 100) / (Se E660RSC.PerIcs = 18 então 0,70 senão 0,50)) \* (E660RSC.PerIcs / 100))) \* E660RSV.QtdFat

Na compra, a nota fiscal está registrada com os seguintes valores:

* Valor base do ICMS substituído = R$ 1.000,00
* Quantidade de entrada do produto = 10
* % MVA ENTRADA = 40%
* % ICMS Interno = 18%
* % Fator ICMS Interno = 70% quando % ICMS Interno for 18% senão será 50%
* Quantidade vendida: 5

Quando a partir dessa compra for realizada uma venda para um contribuinte do estado do PR do Simples Nacional, o valor a ressarcir deve ser:

* **Item I:**
  + Coeficiente = (Valor base do ICMS substituído / Quantidade de entrada do produto) / (1 + (MVA / 100))
  + Coeficiente = (1.000,00 / 10) / (1 + (40 / 100))
  + Coeficiente = 71,428571...
* **Item II:**
  + Coeficiente = (MVA /100) / (% Fator ICMS Interno)
  + Coeficiente = (40 /100) / (0,70)
  + Coeficiente = 0,571428...
* **Item III:** 
  + Coeficiente = (% Fator ICMS Interno / 100)
  + Coeficiente = (18 / 100)
  + Coeficiente = 0,18
* **Valor a ressarcir** = (Item I \* Item II \* Item III) \* Quantidade vendida
  + **Valor a ressarcir** = (71,428571 \* 0,571428 \* 0,18) \* 5 = R$ 36,73.

Quando o **CodRtr** (Código do Regime Tributário) for igual a **1** ou **2** e **SigUfs** (Sigla da Unidade da Federação) for igual a **PR**, será gravado o valor de **R$ 36.73** em vez do valor da NF de entrada.no ICMS ST a ressarcir.

## 2.7. Robô - ICMS ST

Visando auxiliar no processo de ressarcimento, restituição e complementação do ICMS ST, pode-se utilizar a aplicação **Robo.exe**, que apresentará os dados para ajuste de lançamentos, resolução de críticas, informações faltantes etc.

A aplicação está disponível no diretório de instalação do ERP (a partir das versões 5.8.11.63 e 5.8.10.150). O arquivo com as validações fica disponível no diretório **...\modelos\robodiagnosticos**. Abaixo, seguem as regras validadas pelo robô:

![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/images/icms/robo-icms-st_thumb_0_48.png)

Também estão disponíveis as seguintes listagens que impactam na geração da ADRC-ST (PR):

* Código da CEST das tabelas E75PRO, E075DER e E022CLF
* Origem do GTIN das tabelas E075PRO e E070VEN
* Código do GTIN das tabelas E075DER e E075BAR
* Produto enquadrado no art 119 do RICMS do PR das tabelas E075PRO e E012CLF
* Situação tributária do ICMS das tabelas E660INC, E660INV e E660RSV.

Importante

Diferentemente do ERP, no Gestão de Lojas o ICMS ST gera as informações baseadas na última nota fiscal de entrada. Para que as informações sejam buscadas corretamente, a NF de entrada do produto com ST deve estar integrada no Retaguarda. Confira mais informações sobre os cenários do Gestão de Lojas na documentação sobre Parametrizações para NF-e 4.0.

## Páginas relacionadas

* [PEPS](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/processo-controle-entrada-saida-produto.htm)
* [Portaria CAT 42/2018](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f669gpc.htm#cat-42-2018)
* [Manutenção de Controle de Entrada de Produtos](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f440rci.htm)
* [70 - ICMS ST complementar](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/processo-geracao-calculo-imposto-70.htm)
* [calcular ICMS](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/impostos-icms.htm)
* [empresa](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070emp.htm#menu_cadastros/f070emp.htm)
* [parâmetros fiscais](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075pff.htm)
* [família](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f012fam.htm#menu_cadastros/f012fam.htm)
* [Controle de Entrada de Produtos](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075cep.htm)
* [CalEfeSol](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#CalEfeSol)
* [PerLimSol](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#PerLimSol)
* [Tipos Substituições Impostos / Modalidade Base Cálculo / Antecipação - Por Estado](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f019tis.htm)
* [cadastro da filial](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070fve.htm)
* [cadastro de clientes](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f085cad.htm)
* [Tabela 5.7](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/sped/fiscal-icms-ipi/adequacoes-leiautes.htm#tabela)
* [Adequação aos leiautes 14 e 15 do SPED Fiscal](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/sped/fiscal-icms-ipi/adequacoes-leiautes.htm)
* [Inicialização das médias](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/sped/fiscal-icms-ipi/adequacoes-leiautes.htm#medias)
* [Apuração do imposto 70](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/sped/fiscal-icms-ipi/adequacoes-leiautes.htm#imposto-70)
* [ADRC-ST (PR)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f669drr.htm)
* [Parametrizações para NF-e 4.0](https://documentacao.senior.com.br/gestaodelojas/6.2.20#ajuda-por-processos/retaguarda/notas-fiscais/nfe-4-0/parametrizacoes.htm)
