# Cadastro

> **Fonte:** F080SER - Cadastro de Serviços — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f080ser.htm  
> **Trilha:** Ajuda por telas > Cadastros > Produtos e Serviços > Serviços  
> **Telas citadas:** E080SER, E083ORI, F012FAM, F019TIR, F022CLF, F047NTG, F051DIS, F055TPR, F066OTE, F070FEF, F073TRA, F080CSA, F080SXC, F080TSI, F081GTP, F095CBO, F103CAT, F118PSI, F140GNF, F660NFV, F670EBI, F670EBN  
> **Identificadores de regras:** GER-080SERVI01

---
Descrição  
Descrição do serviço.

Descrição p/ NF 

Descrição do serviço a ser impresso na nota fiscal.

**Observação**

Quando a forma de integração na filial estiver configurada como **Senior**, a descrição do serviço é trazida da tag InfSenior, e não da tag <Discriminacao> via identificador de regras. A tag <Descricao> do grupo InfSenior é gerada com a informação desse campo (**Descrição p/ NF**).

Nesse caso, para que a tag <Descricao> tenha o mesmo valor da tag <Discriminacao>, utilize o identificador de regras GER-000GERSDE4, manipulando a variável **VSIntDesSrv** no momento da emissão do .XML no ERP para que a tag <Descrição> fique com a mesma informação da tag <Discriminacao>.

Complemento  
Complemento, onde pode ser cadastrados mais detalhes do serviço.

Código Tributação p/ DARF

Código de tributação para emissão da DARF.

Família  
Código da família que o serviço pertence. A família é cadastrada na tela F012FAM.

Unidade Medida

Unidade de medida do serviço.

Quantidade Padrão  
Quantidade padrão do serviço, de acordo com a unidade de medida.

Preço Compra 

Preço unitário do serviço para compras.

Preço Venda  
Preço unitário do serviço para vendas.

% Desconto 

Percentual de desconto previsto para venda do serviço.

% INSS 

Percentual do INSS.

% ISS 

Percentual do ISS.

% IRRF 

Percentual do IRRF.

% IRRF Empresa Pública

Percentual do IRRF para empresa pública ou equiparada do produto.

% PIS Retido 

Percentual de PIS.

% COFINS Retido 

Percentual de COFINS.

% CSLL 

Percentual de CSLL.

% Out. Ret. 

Percentual de outras retenções válidas para o serviço.

% Comissão 

Percentual de comissão prevista para a venda do serviço.

Natureza de Gasto 

Código da natureza de gasto, cadastradas na tela F047NTG.

Conta Receita Padrão  
Campo destinado a informação da conta financeira receita e que é utilizado como sugestão para geração do rateio para serviços na solução Gestão Empresarial GO UP.

Conta Despesa Padrão 

Campo destinado a informação da conta financeira despesa e que é utilizado como sugestão para geração do rateio para serviços na solução Gestão Empresarial GO UP.

Conta Contábil-1 

Para que o conteúdo informado nesse campo seja inserido no item da Ordem de Compra gerada a partir da produção, é necessário ativar o parâmetro global ConCtaRed.

Conta Contábil-2 

Conta contábil 2.

Conta Contábil-3 

Conta contábil 3.

Conta Contábil-4 

Conta contábil 4.

Observação do Serviço 

Observação do serviço.

Centro Custo 

Código do centro de custo do serviço.

Classificação Fiscal 

Código da classificação fiscal para os serviços com IPI.

Origem Fiscal da Mercadoria

Permite informar a origem fiscal da mercadoria.

* Nacional
* Estrangeiro - Importação Direta
* Estrangeiro - Adquirida no mercado interno.

Situação Tributária 

Código da situação tributária do serviço com tributação de ICMS e IPI.

% IPI 

Percentual de IPI.

Recupera IPI 

Indicativo se o serviço recupera IPI.

Tributa ICMS 

Indicativo se o serviço tributa ICMS.

Código ICMS Especial

Código do ICMS especial.

Código Redução Impostos 

Código de redução de impostos. Para que o código seja exibido nesta tela é necessário que haja cadastro na tela Reduções e Acréscimos de Base de Cálculo de Impostos - Por Estado (F019TIR).  
Para RPA e Notas fiscais municipais, veja mais em Redução de INSS, para transportistas.

Código ICMS Substituído 

Código de ICMS substituído.

Recupera ICMS 

Indicativo se o serviço recupera ICMS.

Recupera PIS 

Indicativo se o serviço recupera PIS.

Recupera COFINS 

Indicativo se o serviço recupera COFINS.

Tributa PIS 

Indicativo se o serviço tributa PIS.

Tributa COFINS 

Indicativo se o serviço tributa COFINS.

Observação (vale para PIS e COFINS)

1. Ao iniciar o cadastro de um serviço, por padrão, este campo sempre vai assumir o valor **S**
2. Ao informar a família no campo correspondente, o sistema verifica a classificação fiscal que consta no cadastro da família e então sugere para o campo **Tributa COFINS/PIS** do serviço, os mesmos valores da classificação fiscal
3. Ao passar pelo campo da classificação fiscal no cadastro do serviço e alterar a classificação (diferente do que está na família), irá sobrepor o campo **Tributa COFINS/PIS**, conforme o que está no cadastro dessa nova classificação fiscal
4. Atualmente não temos uma forma de manipular o valor a ser sugerido nesses campos no cadastro do serviço, apenas poderá ser consistido o valor do campo por meio do identificador GER-080SERVI01

Código Tributação NFS-e 

Código de tributação do serviço para nota fiscal de serviço eletrônica.

Calcula PIS Importação

Indica se calcula o PIS de importação nas notas fiscais de importação e ordens de compra.

Calcula COFINS Importação

Indica se calcula o COFINS de importação nas notas fiscais de importação e ordens de compra.

Sit. Trib. PIS

Código da situação tributária de PIS.

Natureza Receita PIS

Informa a natureza da receita do PIS de acordo com a Sit. Trib. PIS informada para o serviço. O código é exigido na escrituração fiscal do SPED Contribuições e deve ser utilizado de acordo com os códigos existentes nas tabelas da Receita Federal. Para mais informações, consulte a ajuda da tela Notas Fiscais de Saída (F660NFV), guia Itens.

Sit. Trib. COFINS

Código da situação tributária do COFINS.

Natureza Receita COFINS

Informa a natureza da receita do COFINS de acordo com a Sit. Trib. COFINS informada para o serviço. O código é exigido na escrituração fiscal do SPED Contribuições e deve ser utilizado de acordo com os códigos existentes nas tabelas da Receita Federal. Maiores informações, consulte a ajuda da tela Notas Fiscais de Saída (F660NFV), guia Itens.

Sit. Trib. IPI Compras

Código da situação tributária de IPI nas operações de compra.

Sit. Trib. PIS Compras

Código da situação tributária de PIS nas operações de compra.

Sit. Trib. COFINS Compras

Código da situação tributária de COFINS nas operações de compra.

Sit. Trib. IPI

Código da situação tributária de IPI.

Código Tabela Tributação PIS 

Seleção de tabelas de preços com aplicações 3(Cálculo por Quantidade (Vendas)), 4(Cálculo por Quantidade (Compras)) e 5(Cálculo por Quantidade (Ambas)), por unidade de medida.

Código Tabela Tributação COFINS

Seleção de tabelas de preços com aplicações 3(Cálculo por Quantidade (Vendas)), 4(Cálculo por Quantidade (Compras)) e 5(Cálculo por Quantidade (Ambas)), por unidade de medida.

Código Tabela Tributação IPI 

Seleção de tabelas de preços com aplicações 3(Cálculo por Quantidade (Vendas)), 4(Cálculo por Quantidade (Compras)) e 5(Cálculo por Quantidade (Ambas)), por unidade de medida.

Observação

As tabelas de preço de PIS/COFINS e IPI, informadas no cadastro do produto/serviço, permitem que o Gestão Empresarial | ERP calcule esses impostos utilizando a base de cálculo por quantidade e alíquota em valor. A tabela informada deve pertencer a uma aplicação de cálculo por quantidade (3, 4 ou 5) e conter a respectiva alíquota em valor para o produto/serviço. Essa tabela será verificada no cálculo de notas fiscais de entrada, ordens de compra, notas fiscais de saída e pedidos.

Código Fiscal Federal  
Inserir o código fiscal federal, este campo não tem preenchimento obrigatório.

Código Fiscal Estadual 

Inserir o código fiscal estadual, este campo não tem preenchimento obrigatório.

Código Fiscal Municipal 

Inserir o código fiscal municipal, este campo não tem preenchimento obrigatório.  
Esse campo é utilizado para emissão de NFS-e para Prefeitura de Florianópolis.

Nota Mínima para Fornecimento 

Nota mínima necessária para a aprovação de um fornecedor.

Código do Plano de Inspeção 

Permite informar o código do plano de inspeção de serviços para ser realizado na Qualidade.

Permite Gerar Orçamento

Indica se o serviço pode ser orçado.

Tipo Serviço

 Tipo de serviço no contexto fiscal baseado na LC 116/2003.

Observação

Deve ser informado no campo Tipo Serviço com um tipo previamente cadastrado na tela F080TSI. Os tipos devem respeitar a Tabela de Códigos de item da Lista de Serviços, que pode ser baixado acessando o Portal da Nota Fiscal Eletrônica.

% CIDE Tecnologia 

Permite informar o percentual de imposto CIDE tecnologia. Este valor é gravado na tabela E080SER.PerCit.

Tipo de Serviço para o Comércio

Indica o tipo de serviço para Varejo Senior. Se este campo estiver preenchido com N (Serviço) será possível poder alterar/incluir valor no campo Valor de Serviço nesta tela. Ao ser gerado um de garantia estendida, pela tela F081GTP, este não poderá ser alterado.

Operadora Telefonia

Código da operadora de telefonia (F066OTE). O campo fica habilitado quando a opção selecionada no campo Tipo de Serviço para Comércio for L (Recarga Celular).

Transportadora 

Código da transportadora (F073TRA). O campo fica habilitado quando a opção selecionada no campo Tipo de Serviço para Comércio for F (Frete).

Categoria Manutenção 

Permite informar o código da categoria de Manutenção, cadastrados na tela F103CAT. Este campo somente permanece para edição quando na origem possuir serviços de manutenção (E083ORI.IndSmt = &#39;S&#39;).

Situação 

Situação do serviço (ativo ou inativo).

Usuário Geração  
Usuário que cadastrou o serviço.

Data Geração 

Dia, mês e ano que o serviço foi criado.

Hora Geração 

Hora que o serviço foi criado.

Usuário Última Alteração  
Usuário que alterou o serviço.

Data Última Alteração 

Dia, mês e ano que o serviço foi alterado.

Hora Última Alteração

Hora que o serviço foi alterado.

Este campo somente ficará habilitado para serviços produzidos. Quantidade mínima de unidades permitido por ordem de serviço/compra.

Classe Cons. Energia /Gás  
Classe de consumo de energia elétrica ou gás.

* Comercial
* Consumo Próprio
* Iluminação Pública
* Industrial
* Poder Público
* Residencial
* Rural
* Serviço Público

Classe Fornec. Água

Classe de fornecimento de água.

* 0 - Consumo residencial até R$ 50,00
* 1 - Consumo residencial de R$ 50,01 a R$ 100,00
* 2 - Consumo residencial de R$ 100,01 a R$ 200,00
* 3 - Consumo residencial de R$ 200,01 a R$ 300,00
* 4 - Consumo residencial de R$ 300,01 a R$ 400,00
* 5 - Consumo residencial de R$ 400,01 a R$ 500,00
* 6 - Consumo residencial de R$ 500,01 a R$ 1000,00
* 7 - Consumo residencial acima de R$ 1000,01
* 20 - Consumo comercial/industrial até R$ 50,00
* 21 - Consumo comercial/industrial de R$ 50,01 a R$ 100,00
* 22 - Consumo comercial/industrial de R$ 100,01 a R$ 200,00
* 23 - Consumo comercial/industrial de R$ 200,01 a R$ 300,00
* 24 - Consumo comercial/industrial de R$ 300,01 a R$ 400,00
* 25 - Consumo comercial/industrial de R$ 400,01 a R$ 500,00
* 26 - Consumo comercial/industrial de R$ 500,01 a R$ 1000,00
* 27 - Consumo comercial/industrial acima de R$ 1000,01
* 80 - Consumo de órgão público
* 90 - Outros tipos de consumo até R$ 50,00
* 91 - Outros tipos de consumo de R$ 50,01 a R$ 100,00
* 92 - Outros tipos de consumo de R$ 100,01 a R$ 200,00
* 93 - Outros tipos de consumo de R$ 200,01 a R$ 300,00
* 94 - Outros tipos de consumo de R$ 300,01 a R$ 400,00
* 95 - Outros tipos de consumo de R$ 400,01 a R$ 500,00
* 96 - Outros tipos de consumo de R$ 500,01 a R$ 1000,00
* 97 - Outros tipos de consumo acima de R$ 1000,01

Tipo de ligação

Tipo de ligação elétrica.

* 1 - Monofásico
* 2 - Bifásico
* 1 - Trifásico

Cod. do grupo de tensão

Indicativo a qual grupo de tensão está enquadrado.

1. A1 - Alta Tensão (230kV ou mais)
2. A2 - Alta Tensão (88 a 138kV)
3. A3 - Alta Tensão (69kV)
4. A3a - Alta Tensão (30kV a 44kV)
5. A4 - Alta Tensão (2,3kV a 25kV)
6. AS - Alta Tensão Subterrâneo
7. B1 - Residencial
8. B1 - Residencial Baixa Renda
9. B2 - Rural
10. B2 - Cooperativa de Eletrificação Rural
11. B2 - Serviço Público de Irrigação
12. B3 - Demais Classes
13. B4a - Ilum. Púb. - rede de distribuição
14. B4b - Ilum. Púb. - bulbo de lâmpada

Regime Tributário

Este campo tem as seguintes opções:

* C (Regime cumulativo)
* U (Regime não cumulativo); e
* N (Nenhum)

Estas opção influencia nos tipos de impostos: 41 (PIS Não Cumulativo (SPED)), 43 (PIS Cumulativo (SPED)), 42 (COFINS Não Cumulativo (SPED)), 43&#39; (PIS Cumulativo (SPED)) e 44 (COFINS Cumulativo (SPED)) e na apuração do faturamento na gestão de tributos.

Na inclusão de novos serviços será sugerido o regime tributário conforme segue:

* Se a forma de tributação da filial (Cadastros > Filiais > Parâmetros por Gestão > Tributos (F070FEF)) for Real Estimativa, Real Balanço Suspensão e Real, então o regime tributário sugerido para o produto e serviço (Cadastros > Produtos e Serviços > Produtos e Serviços, telas Individual e Agrupado) será U(Não cumulativo)
* Se a forma de tributação da filial (Cadastros > Filiais > Parâmetros por Gestão > Tributos (F070FEF)) for Presumido, então o regime tributário sugerido para o produto e serviço (Cadastros > Produtos e Serviços > Produtos e Serviços, telas Individual e Agrupado) será C (Cumulativo)
* Para outra forma de tributação informada na filial será sugerido como regime tributário do produto e serviço N (Nenhum)

Qtde Múltipla  
Este campo somente ficará habilitado para serviços produzidos. Quantidade múltipla para cálculo da geração de ordem de serviço/compra.

Qtde. Máxima  
Quantidade máxima de unidades permitido para uma ordem de serviço/compra. Este campo somente ficará habilitado para serviços produzidos. Ao gerar ordens de serviço ou de compras e a quantidade for superior a esta quantidade, o sistema gera uma nova ordem conforme valores de quantidade mínima e múltipla informados.

Base Cálculo Crédito

Permite definir a natureza da base de cálculo do crédito de maneira customizada para os itens de produto.

%PIS importação diferenciado

Percentual de PIS de importação diferenciado.

%Cofins importação diferenciado

Percentual de COFINS de importação diferenciado.

Código Fiscal e Descrição Fiscal

Campos abrangentes para a informação do código e a descrição fiscal do item.

Se não for permitido duplicar o código fiscal, ao sair do campo Código Fiscal, será verificado se existe este código nos cadastro de produto e serviço, pois não pode haver duplicidade de códigos, sendo apresentada a mensagem Código fiscal já existe, favor informe outro código.

Se for possível duplicar o código fiscal e alterar o código e a descrição fiscal, ao sair do campo Código Fiscal: para o produto apenas será possível duplicar o código se a Família, a Unidade de Medida e o Indicativo do tipo de produto para impostos forem iguais e, para o serviço somente será possível duplicar o código se a Família, a Unidade de Medida e o Tipo de Serviço no contexto fiscal forem iguais. Caso os registros sejam iguais, o campo Descrição Fiscal será sugerido com a descrição existente na base de dados.

Ao alterar o conteúdo deste campo será apresentada a mensagem Deseja alterar descrição para todos os itens?, que se respondida com Sim, fará com que todos registros que possuem o mesmo Item Fiscal sejam alterados com a mesma Descrição Fiscal. Caso contrário, não será permitida a alteração.

Filial do Serviço  
Código da filial do serviço.

Código Tabela Preço 

Código da tabela de preço que o serviço foi gerado automaticamente.

Validade Inicial 

Indica a validade inicial do serviço na tabela de preço (F081GTP).

Idade Mínima 

Indica a idade mínima, proveniente da tabela de preço (F081GTP) quando a aplicação for 8 (Parcela Protegida).

Idade Máxima 

Indica a idade máxima, proveniente da tabela de preço (F081GTP) quando a aplicação for 8 (Parcela Protegida).

Código Garantia Estendida 

Código da garantia estendida proveniente da tabela de preço (F081GTP).

Prazo Garantia Estendida 

Prazo da garantia estendida em meses, proveniente do campo Prazo Garantia Est. da guia Garantia Estendida (F081GTP).

Valor Inicial 

Indica o valor inicial do serviço. Exclusivo Varejo. O campo é somente leitura, pois sua informação é proveniente do Valor Inicial das guias Garantia Estendida ou Parcela Protegida da tabela de preço (F081GTP).  
Este campo é utilizado somente quando o tipo de serviço for P – Parcela Protegida ou G - Garantia Estendida.

Valor Final

Indica o valor final do serviço. Exclusivo Varejo. O campo é somente leitura, pois sua informação é proveniente do Valor Final das guias Garantia Estendida ou Parcela Protegida da tabela de preço (F081GTP). Este campo é utilizado somente quando o tipo de serviço for P – Parcela Protegida ou G - Garantia Estendida.

Valor Serviço

Indica o valor do serviço da tabela de preço. O campo é somente leitura, pois sua informação é proveniente do Valor Cobrado das guias Garantia Estendida ou Parcela Protegida da tabela de preço (F081GTP). Este campo é alimentado somente quando o tipo de serviço for P – Parcela Protegida ou G - Garantia Estendida.

Observação

Quando o campo Tipo de Serviço para Comércio for preenchido com qualquer informação diferente de P - Parcela Protegida e G - Garantia Estendida, o campo Valor Serviço ficará editável para que seja definido o valor do serviço

Agrup. Garantia Estendida 

Código do agrupamento da garantia estendida do serviço. O campo é leitura, pois é proveniente do campo Agrupamento da guia Itens Produto da tabela de preço (F081GTP).

Código NBS 

Informe o código NBS do serviço. A sigla NBS refere-se é a Nomenclatura Brasileira de Serviços, relacionadas à várias classes de serviços, intangíveis e outras operações. É importante atentar-se ao preenchimento desse campo, porque a informação incorreta pode acarretar em penalidades.

Essa informação é exportada para a Senior X para atender o Siscoserv.

Imobilizar Serviço 

Se este campo estiver preenchido com Sim, a nota fiscal deste serviço será apresentada na integração com o patrimônio via Tributos (F670EBI) ou Recebimento (F670EBN).

Código Modalidade ICMS 

Ao inserir um novo serviço que tenha a família parametrizada com a modalidade na tela F012FAM, será sugerida a modalidade da família neste campo.

Comissionado 

Para o Varejo Senior: se este campo estiver preenchido, ele será gerado como sugestão para o campo Comissão da tela F118PSI.

Aposentadoria Especial 

Informe a quantidade de anos de contribuições.

Percentual da aposentadoria especial

Com base na quantidade de anos de contribuição da aposentaria especial, informe o percentual que será recolhido do valor da base de INSS para a previdência social como forma de aposentadoria especial.

Código da Atividade

Este campo deve ser preenchido com a subclasse da CNAE ( Classificação Nacional de Atividades Econômicas) encontrada na coluna SUBCLASSE da lista de CNAEs.

Observação

Este campo é utilizado para a emissão de NFS-e para o município de Florianópolis.

% SENAR/SENAT

Percentual do imposto SENAR/SENAT do serviço para notas fiscais de saída.

% Diferimento

Percentual que será utilizado para o cálculo do valor do ICMS Diferido em cotações, contratos, ordens de compras, pedidos, pré-faturas e notas fiscais de entrada e saída.

Tabela de presunção IRPJ

Informar o código da tabela de presunção IRPJ, no qual foi feito o cadastro na tela F055TPR.

Tabela de presunção CSLL

Informar o código da tabela de presunção CSLL, no qual foi feito o cadastro na tela F055TPR.

Situação Tributária ISS

Informar a situação tributária do ISS para a nota fiscal de serviço. Este campo também pode ser parametrizado no cadastro do serviço agrupado (F080CSA) ou na ligação de serviço e CEP (F080SXC). A parametrização definida em uma dessas telas servirá de sugestão para o item de serviço na tela F140GNF. A sugestão é realizada na seguinte ordem:

* 1º : busca da ligação de serviço com o CEP
* 2º : se não houver na ligação de serviço com o CEP, busca do cadastro do serviço
* 3º : se não encontrou sugestão, obriga informar no item de serviço na tela F140GNF

Para mais informações sobre a Nota Fiscal de Prestação de Serviço, acesse a documentação da NFS-e de Florianópolis.

Especificador situação tributária

Código especificador da situação tributária. No cadastro de um produto novo, será sugerido o CEST informado na tela Classificações Fiscais (F022CLF). Ele tem como objetivo estabelecer a sistemática de uniformização e identificação das mercadorias e bens passíveis de sujeição aos regimes de substituição tributária e de antecipação de recolhimento do ICMS.

Código do Dispositivo Fiscal

Código do dispositivo cadastrado na tela F051DIS.

Tipo de rendimento

Informe qual o tipo de rendimento que deve ser utilizado na geração da DIRF, sendo exibido no registro **VRPDE** (Valores de rendimentos pagos a residentes ou domiciliados no exterior) do arquivo. São apresentadas para seleção as opções de acordo com o anexo II do leiaute da DIRF, disponibilizado pela Receita Federal.

Forma de tributação

Informe qual a forma de tributação que deve ser utilizada na geração da DIRF, sendo exibida no registro **VRPDE** (Valores de rendimentos pagos a residentes ou domiciliados no exterior) do arquivo. São apresentadas para seleção as opções de acordo com o anexo II do leiaute da DIRF, disponibilizado pela Receita Federal.

Natureza de Atividade

Indica a natureza da atividade do serviço:

* 1 - Trabalho Urbano;
* 2 - Trabalho Rural.

Número CBO

Número da classificação brasileira de ocupação, conforme cadastrado na tela F095CBO.

Prestação Siscoserv

Indica o modo de prestação do serviço para Siscoserv. Podendo ser:

1. **Transfronteiriço**: quando o serviço prestado do território de um país ao território de outro país, por residente ou domiciliado no Brasil a residente ou domiciliado no exterior. Exemplo: Serviço vendido pela internet
2. **Consumo no Exterior**: quando o serviço é prestado por residente e domiciliado no exterior e consumido no território de outro país por residente ou domiciliado no Brasil. Exemplo: Serviços educacionais presenciais prestados no exterior a residente no Brasil; capacitação no exterior de funcionários de pessoa jurídica domiciliada no Brasil
3. **Presença Comercial no Brasil**: quando o serviço prestado por residente ou domiciliado no Brasil e consumido no território brasileiro por residente ou domiciliado no exterior. Exemplo: Serviço educacional, serviço médico
4. **Movimento Temporário de Pessoas Físicas**: quando o residentes no Brasil deslocam-se por tempo limitado ao exterior com vistas a prestar um serviço a residente ou domiciliado no exterior. Exemplo: Advogado residente no Brasil desloca-se para o exterior a fim de prestar serviço

Classificação Convênio ICMS

Código da classificação do convênio ICMS 115/2013. O valor informado neste campo é gerado no campo 14 - Código de classificação do item do registro **I - Itens** do relatório Convênio ICMS 115/2003 (CIAE052).

Tipo de utilização

Tipo de utilização do convênio. O valor informado neste campo é gerado no campo 4 - Fase ou tipo de Utilização do registro **I - Itens** quando for uma nota fiscal do tipo 21 ou 22. E caso seja uma nota fiscal do tipo "06 – Energia Elétrica" gera informação do campo Tipo de ligação.

% INSS Empresa

Indica o percentual de INSS da empresa.

**Natureza de Rendimentos**

Tem por finalidade a classificação dos serviços para a EFD-Reinf.

**Tipo serviço para impostos**

Utilizado na geração do campo 07 do registro 0200 do Bloco K. Para mais informações, confira a documentação.

Serviço Disp. Recebimento Eletrônico

Indica se o serviço está disponível para busca no recebimento eletrônico de NFS-e. Se não for preenchido, o sistema busca a informação no cadastro da família (F012FAM).

**Taxa Fixa para IRRF**

Conforme decreto nº 9.580 de 22 de novembro de 2018, artigos 732 e 733, nos pagamentos à PF de prêmios em dinheiro e prêmios em bens e serviços, o imposto de renda é aplicado com alíquota fixa. Já em pagamentos de aluguel, honorários de sucumbências, patrocínios, lucros cessantes e afins, a retenção do IRRF é aplicada sobre a tabela progressiva.

Quando o parâmetro for **S** e houver um percentual de IR informado para o serviço, o cálculo dos itens de serviços das notas de entrada desconsidera o cálculo de IR com RPA (caso ele esteja parametrizado para a série da nota ou fornecedor) e calcula o IR do serviço usando a taxa informada nele, sem fazer as deduções feitas pelo RPA no valor base de IR. O cálculo do RPA desconsidera os serviços com taxa fixa no momento de construir a base de IR do RPA usando as notas anteriores e os serviços anteriores (anteriores ao serviço calculado).

**Percentual do Diferimento de ICMS relativo ao FCP**

Percentual do diferimento de ICMS relativo ao FCP sugerido para o cálculo do valor do diferimento de ICMS relativo ao FCP nos processos de vendas, faturamento, compras e recebimento. Este campo não tem preenchimento obrigatório.

Categoria Recibo de Pagamento Autônomo   
Definir qual a categoria de recibo de pagamento autônomo com as seguintes opções:

* "701 - Contrib. Indiv. - Autônomo em geral, exceto demais categorias"
* "711 - Contrib. Indiv. - Transportador autônomo"
* "721 - Contrib. Indiv. - Diretor não empregado, com FGTS"
* "722 - Contrib. Indiv. - Diretor não empregado, sem FGTS"
* "723 - Contrib. Indiv. - Empresários, sócios e membro conselho Adm. ou fiscal"
* "731 - Contrib. Indiv. - Cooperado que presta serviço intermédio Cooperativa"
* "734 - Contrib. Indiv. - Transp. Coop. presta serviços intermédio cooperativa"
* "738 - Contrib. Indiv. - Cooperado filiado a Cooperativa de Produção"
* "741 - Contrib. Indiv. - Micro Empreendedor Individual, contratado por PJ"
* "751 - Contrib. Indiv. - Aposent., nomeado magistr. class. temp. J. Trabalho/Eleitoral"
* "761 - Contrib. Indiv. - Associado eleito p/direção cooper.,assoc. ou entid. renum"
* "771 - Contrib. Indiv. - Membro de cons. tutelar, conforme Lei nº 8.069, de 13/07/1990"
* "781 - Ministro de confissão religiosa ou membro de vida consagrada"

Tipo pagamento serviço comunicação

Forma de pagamento do serviço comunicação: "1- Pré-pago" e "2 - Pós-pago". Atende o Leiaute 17 do SPED Fiscal.

Considera % efetivo do ISS do Simples Nacional nas notas fiscais

Indica se o sistema deve considerar a alíquota efetiva do ISS, identificada a partir do cálculo do imposto do Simples Nacional, ou a alíquota do ISS informada na tabela de tributação do Simples Nacional. Isto sempre que forem emitidas notas fiscais de venda de serviço.

Serviço tomado em Unidade Econômica

Indica se o serviço foi tomado em Unidade Econômica ou não (campo 21 do relatório, em Serviços Prestados).

Código de Tributação Nacional

Utilizado apenas para o envio de NFS-e para emissores do Ambiente Nacional. Esse campo deve ser preenchido com o código de tributação nacional (6 dígitos), conforme Anexo B disponibilizado pelo projeto da NFS-e Nacional.

Código item cClass

Campo para preenchimento da classificação do item para NFCom (cClass), conforme as opções disponíveis no Portal da Nota Fiscal Fatura de Serviço de Comunicação Eletrônica - SVRS.

Calcula FUST

Indica se o serviço calcula o FUST para itens da NFCom.

Percentual FUST

Percentual do FUST para aplicar nos itens da NFCom.

Calcula FUNTTEL

Indica se o serviço calcula o FUNTTEL para itens da NFCom.

Percentual FUNTTEL

Percentual do FUNTTEL para aplicar nos itens da NFCom.

Aplicação da CBS/IBS   
Indicador do tipo de aplicação utilizado no CBS/IBS para determinar o cClassTrib utilizado no motor de cálculo.

Operação uso ou consumo pessoal

Indica operação de uso ou consumo pessoal para NFS-e.

Indicador NFS-e Disp. ao MDIC

Indicador se a NFS-e deverá ser disponibilizada ao MDIC. Conta com as opções:

* Não enviar para o MDIC
* Enviar para o MDIC

## Páginas relacionadas

* [GER-000GERSDE4](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ger_000gersde4.htm)
* [F012FAM](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f012fam.htm)
* [F047NTG](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f047ntg.htm)
* [ConCtaRed](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#ConCtaRed)
* [F019TIR](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f019tir.htm)
* [INSS](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/manuais_processos/suprimentos/rpa/parametrizacao.htm#reducao-inss)
* [GER-080SERVI01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ger_080servi01.htm)
* [F660NFV](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f660nfv.htm)
* [Prefeitura de Florianópolis](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/integracao_nfse_florianopolis.htm)
* [F080TSI](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f080tsi.htm)
* [Portal da Nota Fiscal Eletrônica](http://www.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=/NJarYc9nus=)
* [F081GTP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f081gtp.htm)
* [F066OTE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f066ote.htm)
* [F073TRA](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f073tra.htm)
* [F103CAT](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f103cat.htm)
* [Siscoserv](https://documentacao.senior.com.br/gestaoempresarialerp/7.0.0/index.htm#compliance/siscoserv/introducao.htm)
* [F670EBI](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f670ebi.htm)
* [F670EBN](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f670ebn.htm)
* [F118PSI](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_servicos/f118psi.htm)
* [F055TPR](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f055tpr.htm)
* [F080CSA](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f080csa.htm)
* [F080SXC](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f080sxc.htm)
* [F140GNF](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f140gnf.htm)
* [F022CLF](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f022clf.htm)
* [F051DIS](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f051dis.htm)
* [geração da DIRF](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_financas/relatorios/financeiros/fpcp072.htm)
* [F095CBO](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f095cbo.htm)
* [CIAE052](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/relatorios/arquivos-eletronicos-estaduais/ciae052.htm)
* [confira a documentação](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f660isp-remessa-retorno.htm#retorno-bloco-k)
* [recebimento eletrônico de NFS-e](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/manuais_processos/recebimento-eletronico/recebimento-eletronico.htm#nfs-e)
* [Leiaute 17](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/sped/fiscal-icms-ipi/adequacoes-leiautes.htm#17)
* [relatório](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/relatorios/arquivos-eletronicos-municipais/ciam048.htm)
* [código de tributação nacional](https://www.gov.br/nfse/pt-br/mei-e-demais-empresas/codigos-de-tributacao-nacional-nbs)
* [Portal da Nota Fiscal Fatura de Serviço de Comunicação Eletrônica - SVRS](https://dfe-portal.svrs.rs.gov.br/NFCOM/tabelacclass)
