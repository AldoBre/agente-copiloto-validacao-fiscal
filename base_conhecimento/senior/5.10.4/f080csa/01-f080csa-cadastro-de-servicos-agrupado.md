# F080CSA - Cadastro de Serviços agrupado

> **Fonte:** F080CSA - Cadastro de Serviços agrupado — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f080csa.htm  
> **Trilha:** Ajuda por telas > Cadastros > Produtos e Serviços > Serviços  
> **Telas citadas:** E012FAM, E070EMP, E080SER, E083ORI, F012FAM, F022CLF, F070EMP, F070FEF, F080CSA, F103CAT, F118PSI, F700CMC, F710CRP  
> **Identificadores de regras:** GER-080SERVI01

---
Ajuda por telas > Cadastros > Produtos e Serviços > Serviços > Agrupado

## 

Esta tela permite o cadastro dos serviços prestados pela empresa de forma
agrupada. Semelhante a estruturação de um produto, o serviço necessita de uma origem e
uma família previamente cadastradas.

* Duplicação automática de produto/serviço para outras empresas

**Importante**

Ao indicar um serviço como sendo um componente do Modelo
de uma família de produtos, somente será possível cadastrá-lo se o nível de origem
deste serviço for igual ou inferior ao nível de origem da família de produtos deste
modelo.

**Observação**

Quando o campo Contabilidade da tela de Cadastros de Empresas (F070EMP) for "S - Sim", é obrigatório informar os seguintes campos:

* Conta Receita Padrão;
* Conta Despesa Padrão.

Deve ser preenchido também ao menos um destes itens:

* Conta de Despesa;
* Conta de Receita;
* Custo Direto;
* Custo Indireto.

## Guia Serviços

Permite o cadastro dos dados principais do serviço.

**Natureza de Rendimentos**

Tem por finalidade a classificação dos serviços para a EFD-Reinf.

Serviço Disp. Recebimento Eletrônico

Indica se o serviço está disponível para busca no recebimento eletrônico de NFS. Se não for preenchido, o sistema buscará a informação no cadastro da família (F012FAM).

## Campos

Origem  
Código da origem do serviço que deseja cadastrar ou consultar.

Família  
Código da família do serviço que deseja cadastrar ou consultar.

Serviço  
Código do serviço que deseja cadastrar ou consultar.

Descrição p/ NF  
Descrição do serviço para impressão na nota fiscal.

Comissionado 

Para o Varejo Senior: se este campos estiver preenchido ele será
gerado como sugestão para o campo Comissão da tela
F118PSI.

Código da filial vinculada ao serviço

Para empresas que utilizam Varejo = Sim, o campo é preenchido automaticamente com a filial na qual o serviço está sendo cadastrado, não permitindo alteração manual.

Caso o usuário possua abrangência diferente da filial informada no cadastro do serviço, o sistema não permite a utilização do serviço em outras filiais.

Qtd. Padrão 

Sugere o valor a contratar para o referido serviço em todas as rotinas
em que ele estiver envolvido.

Preço
Compra 

Preço unitário do serviço para compras.

Preço Venda 

Preço unitário do serviço para vendas.

% Desconto 

Percentual de desconto previsto para venda do serviço.

% ISS 

Percentual do ISS.

% INSS 

Percentual do INSS.

% IRRF 

Percentual do IRRF.

% IRRF Empresa Pública

Percentual do IRRF para empresa pública ou equiparada do produto.

% Comissão 

Percentual de comissão.

Natureza de Gasto 

Código da natureza de gasto.

Conta Contábil-1 

Conta contábil 1.

% SENAR/SENAT

Exibe o percentual do imposto SENAR/SENAT do produto.

Conta Contábil-2 

Conta contábil 2.

Conta Contábil-3 

Conta contábil 3.

Conta Contábil-4 

Conta contábil 4.

Situação  
Situação do serviço (ativo ou inativo).

Nota Mínima para Fornecimento 

Nota mínima necessária para a aprovação de um fornecedor.

Observação do Serviço 

Observação do serviço.

Centro Custo  
Código do centro de custo.

Classificação Fiscal 

Código da classificação fiscal para os serviços com IPI.

Origem fiscal da mercadoria 

Permite informar a origem fiscal da mercadoria:

1. Nacional;
2. Estrangeiro - Importação Direta;
3. Estrangeiro - Adquirida no mercado interno.
   Este campo somente ficará visível para serviços produzidos (E012FAM.IndSpr = 'S').

Qtde Mínima

Quantidade mínima de unidades permitido por ordem de
serviço/compra. Este campo somente ficará editável para serviços produzidos (E012FAM.IndSpr = 'S').

Qtde Múltipla

Quantidade múltipla para cálculo da geração de ordem de serviço/compra. Este campo somente ficará editável para serviços produzidos (E012FAM.IndSpr = 'S').

Qtde Máxima

Quantidade máxima de unidades permitido para uma ordem de serviço/compra. Ao gerar ordens de serviço ou de compras e a quantidade for superior a esta quantidade, o sistema gera uma nova ordem conforme valores de quantidade mínima e múltipla informados. Este campo somente ficará editável para serviços produzidos (E012FAM.IndSpr = 'S').

Observação

As tabelas de preço de PIS/COFINS e IPI informadas no
cadastro do produto/serviço permitem que o Gestão Empresarial | ERP calcule estes impostos
utilizando base de cálculo por quantidade e alíquota em valor.A tabela informada
deve pertencer a uma aplicação de cálculo por quantidade (3, 4 ou 5) e deve
conter a respectiva alíquota em valor para o produto/serviço. Esta tabela será
verificada no cálculo de notas fiscais de entrada, ordens de compra, notas
fiscais de saída e pedidos.

Código Tabela Preço IPI

Seleção de tabelas de preços com aplicações 3 (Cálculo por Quantidade
(Vendas)), 4 (Cálculo por Quantidade (Compras)) e 5 (Cálculo por Quantidade
(Ambas)).

Código Tabela Preço COFINS

Seleção de tabelas de preços com aplicações 3 (Cálculo por Quantidade
(Vendas)), 4 (Cálculo por Quantidade (Compras)) e 5 (Cálculo por Quantidade
(Ambas)).

Código Tabela Preço PIS

Seleção de tabelas de preços com aplicações 3 (Cálculo por Quantidade
(Vendas)), 4 (Cálculo por Quantidade (Compras)) e 5 (Cálculo por Quantidade
(Ambas)).

Cod. do grupo de tensão

Indicativo a qual grupo de tensão está enquadrado.

Tipo de ligação 

Indicativo sobre o tipo de ligação elétrica.

Classe Fornec. água

Indicativo da classe de fornecimento de água.

Classe Cons. Energia/Gás

Indicativo da classe de consumo de energia elétrica ou gás.

% Out. Ret.

Percentual de outras retenções.

% PIS

Percentual de PIS.

% Cofins

Percentual de Cofins.

% CSLL

Percentual de CSLL.

Recupera COFINS

Indicativo se o serviço recupera COFINS.

Código Tributação NFS-e

Código de tributação do serviço para nota fiscal de serviço eletrônica.

Código Fiscal Municipal

Inserir o código fiscal municipal, este campo não tem preenchimento obrigatório.

Código Fiscal Estadual

Inserir o código fiscal estadual, este campo não tem preenchimento obrigatório.

Código Fiscal Federal

Inserir o código fiscal federal, este campo não tem preenchimento obrigatório.

Tributa COFINS

Indicativo se o serviço tributa COFINS.

Tributa PIS

Indicativo se o serviço tributa PIS.

Observação (vale para PIS e COFINS)

1. Ao iniciar o cadastro de um serviço, por padrão, este campo sempre irá assumir o valor **S**;
2. Ao informar a família no campo correspondente, o sistema verifica a classificação fiscal que consta no cadastro da família e então sugere para o campo **Tributa COFINS/PIS** do serviço, os mesmos valores da classificação fiscal;
3. Ao passar pelo campo da classificação fiscal no cadastro do serviço e alterar a classificação (diferente do que está na família), irá sobrepor o campo **Tributa COFINS/PIS**, conforme o que está no cadastro dessa nova classificação fiscal;
4. Atualmente não temos uma forma de manipular o valor a ser sugerido nesses campos no cadastro do serviço, apenas poderá ser consistido o valor do campo através do identificador GER-080SERVI01

Recupera PIS

Indicativo se o serviço recupera PIS.

Recupera ICMS

Indicativo se o serviço recupera ICMS.

Código ICMS Substituído

Código de ICMS substituído.

Código Redução ICMS

Código de redução do ICMS.

Código ICMS Especial

Código do ICMS especial.

Tributa ICMS

Indicativo se o serviço tributa ICMS.

Recupera IPI

Indicativo se o serviço recupera IPI.

% IPI

Percentual de IPI.

Situação Tributária

Código da situação tributária do serviço com tributação de ICMS e IPI.

Regime Tributário

Este campo tem as seguintes opções:

* C (Regime cumulativo)
* U (Regime não cumulativo)
* N (Nenhum).

Estas opção influencia nos tipos de impostos: 41 (PIS Não Cumulativo (SPED)),
43 (PIS Cumulativo (SPED)), 42 (COFINS Não Cumulativo (SPED)),
43&#39; (PIS Cumulativo (SPED)) e 44 (COFINS Cumulativo (SPED)) e na apuração do faturamento na gestão de tributos.

Na inclusão de novos serviços será sugerido o regime tributário
conforme segue:

* se a forma de tributação da filial (Cadastros > Filiais > Parâmetros
  por Gestão > Tributos (F070FEF)) for Real Estimativa, Real Balanço
  Suspensão e Real, então o regime tributário sugerido para o produto e
  serviço (Cadastros > Produtos e Serviços > Produtos e Serviços, telas
  Individual e Agrupado) será U(Não cumulativo).
* se a forma de tributação da filial (Cadastros > Filiais > Parâmetros
  por Gestão > Tributos (F070FEF)) for Presumido, então o regime
  tributário sugerido para o produto e serviço (Cadastros > Produtos e
  Serviços > Produtos e Serviços, telas Individual e Agrupado) será
  C(Cumulativo).
* para outra forma de tributação informada na filial será sugerido como
  regime tributário do produto e serviço N(nenhum).

U.M. 

É a unidade de medida do serviço. Este campo somente é visível quando a origem permitir alterar a unidade a unidade de
medida de produto/serviço (E083ORI.UsaAux = 'S') ou quando a empresa não tiver a área de Manufatura
instalada (E070EMP.PrdEmp = 'N').

% CIDE Tecnologia

Permite informar o percentual de imposto CIDE tecnologia. Este valor é gravado
na tabela E080SER.PerCit.

Categoria Manutenção 

Permite informar o código da categoria de Manutenção realizadas por este serviço, cadastrados na tela F103CAT.  
Este campo somente permanece visível/editável quando na origem possuir
serviços de manutenção (E083ORI.IndSmt = 'S').

Base Cálculo Crédito 

Permite definir a natureza da base de cálculo do crédito de maneira
customizada para os itens de serviço.

Classificação Convênio ICMS

Código da classificação do convênio ICMS 115/2013. O valor informado neste campo é gerado no campo 14 - Código de classificação do item do registro **I - Itens** do relatório Convênio ICMS 115/2003 (CIAE052).

Código Fiscal, Descrição Fiscal

Campos abrangentes para a informação do código e a descrição fiscal do
item. Se não for permitido duplicar o código fiscal, ao sair do campo Código
Fiscal, será verificado se existe este código nos cadastro de produto e serviço, pois não pode haver duplicidade de códigos, sendo apresentada a
mensagem Código fiscal já existe, favor informe outro código.  

Se for
possível duplicar o código fiscal e alterar o código e a descrição
fiscal, ao sair do campo Código Fiscal: para o produto apenas será
possível duplicar o código se a Família, a Unidade de Medida e o
Indicativo do tipo de produto para impostos forem iguais e, para o
serviço somente será possível duplicar o código se a Família, a Unidade
de Medida e o Tipo de Serviço no contexto fiscal forem iguais. Caso os
registros sejam iguais, o campo Descrição Fiscal será sugerido com a
descrição existente na base de dados.  

Ao alterar o conteúdo deste campo
será apresentada a mensagem Deseja alterar descrição para todos os
itens?, que se respondida com Sim, fará com que todos registros que
possuem o mesmo Item Fiscal sejam alterados com a mesma Descrição
Fiscal. Caso contrário, não será permitida a alteração.

Tipo de utilização 

Tipo de utilização do convênio. O valor informado neste campo é gerado no campo 4 - Fase ou tipo de Utilização do registro **I - Itens** quando for uma nota fiscal do tipo 21 ou 22. E caso seja uma nota fiscal do tipo "06 – Energia Elétrica" gera informação do campo Tipo de ligação.

Mod. ICMS

Ao inserir um novo serviço que tenha a família parametrizada com a
modalidade na tela F012FAM, será sugerida a
modalidade da família neste campo.

% Diferimento   
Percentual que será utilizado para o cálculo do valor do ICMS Diferido em cotações, contratos, ordens de compras, pedidos, pré-faturas e notas fiscais de entrada e saída.

Esp. subst. trib.

Código especificador da situação tributária. No cadastro de um produto novo, será sugerido o CEST informado na tela Classificações Fiscais (F022CLF). Ele tem como objetivo estabelecer a sistemática de uniformização e identificação das mercadorias e bens passíveis de sujeição aos regimes de substituição tributária e de antecipação de recolhimento do ICMS.

Tipo de rendimento

Informe qual o tipo de rendimento que deve ser utilizado na geração da DIRF, sendo exibido no registro **VRPDE** (Valores de rendimentos pagos a residentes ou domiciliados no exterior) do arquivo. São apresentadas para seleção as opções de acordo com o anexo II do leiaute da DIRF, disponibilizado pela Receita Federal.

Forma de tributação

Informe qual a forma de tributação que deve ser utilizada na geração da DIRF, sendo exibida no registro **VRPDE** (Valores de rendimentos pagos a residentes ou domiciliados no exterior) do arquivo. São apresentadas para seleção as opções de acordo com o anexo II do leiaute da DIRF, disponibilizado pela Receita Federal.

**Tipo serviço para impostos**

Utilizado na geração do campo 07 do registro 0200 do Bloco K. Para mais informações, confira a documentação.

**Taxa Fixa IR**

Conforme decreto nº 9.580 de 22 de novembro de 2018, artigos 732 e 733, nos pagamentos à PF de prêmios em dinheiro e prêmios em bens e serviços, o imposto de renda é aplicado com alíquota fixa. Já em pagamentos de aluguel, honorários de sucumbências, patrocínios, lucros cessantes e afins, a retenção do IRRF é aplicada sobre a tabela progressiva.

Quando o parâmetro for **S** e houver um percentual de IR informado para o serviço, o cálculo dos itens de serviços das notas de entrada desconsidera o cálculo de IR com RPA (caso ele esteja parametrizado para a série da nota ou fornecedor) e calcula o IR do serviço usando a taxa informada nele, sem fazer as deduções feitas pelo RPA no valor base de IR. O cálculo do RPA desconsidera os serviços com taxa fixa no momento de construir a base de IR do RPA usando as notas anteriores e os serviços anteriores (anteriores ao serviço calculado).

**Per. do Dif. de ICMS FCP**

Percentual do diferimento de ICMS relativo ao FCP sugerido para o cálculo do valor do diferimento de ICMS relativo ao FCP nos processos de vendas, faturamento, compras e recebimento. Este campo não tem preenchimento obrigatório.

Considera % efetivo do ISS do Simples Nacional nas notas fiscais

Indica se o sistema deve considerar a alíquota efetiva do ISS, identificada a partir do cálculo do imposto do Simples Nacional, ou a alíquota do ISS informada na tabela de tributação do Simples Nacional. Isto sempre que forem emitidas notas fiscais de venda de serviço.

Código de Tributação Nacional

Utilizado apenas para o envio de NFS-e para emissores do Ambiente Nacional. Esse campo deve ser preenchido com o código de tributação nacional (6 dígitos), conforme Anexo B disponibilizado pelo projeto da NFS-e Nacional.

Código do Item NFCom

Campo para preenchimento da classificação do item para NFCom, conforme as opções disponíveis no Portal da Nota Fiscal Fatura de Serviço de Comunicação Eletrônica - SVRS

## Botões

Apenas o serviço informado

Ao marcar é possível visualizar apenas
o serviço informado no campo Serviço.

Ver Máscara de Serviço

Ao marcar irá habilitar o campo Componentes da Máscara. Ao
navegar na grade Serviços, este novo campo exibirá os componentes utilizados
para montar o código do serviço posicionado.

Dados Gerais  
Exibe a tela de cadastramento individual referente ao registro posicionado na
grade.

Monta Código

Auxilia a montagem do código do serviço conforme a máscara definida.

Roteiro 

Abre a tela F710CRP.

Modelo 

Abre a tela F700CMC.

Monta Desc.  
Abre a tela para montar a descrição e a descrição complementar do serviço.

Aposentadoria Especial

Informe a quantidade de anos de contribuições.

## Páginas relacionadas

* [Ajuda por telas](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/ajuda-telas.htm)
* [Duplicação automática de produto/serviço para outras empresas](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/manuais_processos/mercado/duplicacao-automatica.htm)
* [Modelo](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_manufatura/conceito_modelo.htm)
* [F070EMP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070emp.htm)
* [recebimento eletrônico de NFS](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/manuais_processos/recebimento-eletronico/recebimento-eletronico.htm#nfs-e)
* [F012FAM](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f012fam.htm)
* [F118PSI](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_servicos/f118psi.htm)
* [GER-080SERVI01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ger_080servi01.htm)
* [F103CAT](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f103cat.htm)
* [CIAE052](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/relatorios/arquivos-eletronicos-estaduais/ciae052.htm)
* [F022CLF](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f022clf.htm)
* [geração da DIRF](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_financas/relatorios/financeiros/fpcp072.htm)
* [confira a documentação](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f660isp-remessa-retorno.htm#retorno-bloco-k)
* [código de tributação nacional](https://www.gov.br/nfse/pt-br/mei-e-demais-empresas/codigos-de-tributacao-nacional-nbs)
* [Portal da Nota Fiscal Fatura de Serviço de Comunicação Eletrônica - SVRS](https://dfe-portal.svrs.rs.gov.br/NFCOM/tabelacclass)
* [F710CRP.](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_manufatura/f710crp.htm)
* [F700CMC](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_manufatura/f700cmc.htm)
