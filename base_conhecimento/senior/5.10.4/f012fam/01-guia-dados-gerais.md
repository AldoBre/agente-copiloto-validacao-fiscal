# Guia Dados Gerais

> **Fonte:** F012FAM - Cadastro de Famílias — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f012fam.htm  
> **Trilha:** Ajuda por telas > Cadastros > Produtos e Serviços  
> **Telas citadas:** F000ATX, F000IPR, F000PGS, F011CLC, F013AGP, F055TPR, F070EMP, F075GFP, F075PRO, F076MAR, F083ORI, F085COP, F118OCR, F403FPR  
> **Identificadores de regras:** —

---
Esta guia refere-se às definições que compõem os diferentes grupos de famílias de produtos.

Origem Produto

Código da origem de produto que a família pertence.

Tipo Produto

Indicativo de tipo de produto.

* P - Produzido: permite ter estrutura (ficha técnica), gerar ordens de produção, pedidos de venda e movimento de estoque;
* C - Comprado: permite gerar pedidos de venda, ser componente de um produzido, gerar ordens de compra e movimentos de estoque;
* M - Montagem: é um suposto produto, que se agrega ao produto final, possui estrutura, mas não movimenta estoque. Os componentes do produto montagem podem ser comprados ou fabricados, e movimentam o estoque;
* D - Passagem Direta: permite gerar ordens de compra, mas não movimenta estoque, sua entrada na empresa tem destino ligado a um centro de custo;
* S - Serviço: prestação de serviços comprada de terceiros ou vendida para terceiros.

Quantidade Posições Produto

Quantidade de caracteres para a definição da estrutura de codificação do produto, com o limite de 14 caracteres.

Máscara Derivação

Código da máscara utilizada na definição das derivações possíveis para os produtos. No cadastro de famílias de uma origem do tipo serviço produzido, será obrigatório informar uma máscara de derivação, e essa máscara deverá ter apenas um componente.

Unidade Medida (Estoque)

Código da unidade de medida. É herdada pelos produtos.

2ª Unidade Medida

Código da unidade de medida. Esta medida é alternativa para os produtos da família, no caso da produção, esta medida é utilizada na ficha técnica.

3ª Unidade Medida

Código da unidade de medida. Unidade de medida alternativa disponível para outras aplicações, por exemplo nas rotinas que envolvem Balança.
Este campo é utilizado nas rotinas de Agronegócio para a entrada de produto via balança sendo obrigatório a parametrização.

Utiliza Decimais

Indica se o controle da quantidade máxima de casas decimais nas movimentações de estoques dos produtos da família serão controlados pelo cadastro da família ou pelo cadastro de unidade de medida.

* S (Sim): é utilizada a quantidade de decimais definida no campo Quantidade Decimais Estoque.
* N (Não): é utilizada a quantidade de decimais definida no campo Qtd Decimais, na tela Cadastros > Produtos e Serviços> Unidades de Medida.

Observação

Quando o Gestão Empresarial | ERP possui integração com o Varejo Senior, o parâmetro Utiliza Decimais deve ser igual a N, pois a quantidade de decimais é controlada pela Unidade de Medida.

Quantidade Decimais Estoque

Quantidade de dígitos decimais utilizada para os produtos da família. O máximo permitido são cinco dígitos. Seu uso abrange as movimentações de estoque, movimentações no processo produtivo e movimentações na venda do produto. Exemplo: se a família estiver configurada para utilizar casas decimais e a quantidade de casas decimais na família for igual a dois, os produtos dessa família serão movimentados sempre com duas casas decimais ou menos. Caso o usuário informe, em alguma rotina, uma quantidade com três ou mais casas, o ERP não arredondará a quantidade informada. Em vez disso, consistirá o valor informando que o produto não pode ser movimentado com esse número de casas decimais.

Observação

Neste campo é permitida a inclusão de 0 (zero) decimais se o campo Utiliza Decimais estiver parametrizado com S-Sim. Assim, serão considerados 0 (zero) decimais quando na família houver uma unidade de medida que por padrão utiliza decimais.

Tem Características

Permite adicionar informações características relativas ao cadastro do produto, possibilitando posteriormente, selecionar, fazer estatísticas
e emitir relatórios com base em pesquisa usando a característica do produto.

Liga Roteiro ao Produto

Indicativo se o produto utiliza um só roteiro para todas as derivações ou poderá utilizar roteiros diferentes para as suas derivações.

* S - Roteiro único para o produto.
* N - Roteiro para cada derivação do produto.

Observação

Para famílias do tipo serviço, será preenchido sempre com S (sim), ou seja, sempre terá ligação do roteiro ao produto.

Quantidade Múltipla Ordem

Número múltiplo de unidades do produto para o cálculo a ser gerado de ordens de produção ou de compras deste produto.

Quantidade Mínima Ordem

Quantidade mínima de unidades do produto permitido para cada ordem. Ao gerar ordens de produção ou de compras a quantidade nunca será inferior a quantidade informada.

Quantidade Máxima Ordem

Quantidade máxima de unidades do produto permitido para cada ordem. Ao gerar ordens de produção ou de compras para este produto e a quantidade for superior a esta quantidade o sistema gera uma nova ordem.

Quantidade por agrupamento

Quantidade máxima para cada guia de produção.

Baixa na O.P.?

Indicativo se o componente ou a família de produtos deverá aparecer na tela de baixa de componentes da OP para ser baixado. A hierarquia de prioridade é primeiramente o que está definido na Derivação > Produto > Família.

**Quantidade Dia Reposição/Precedentes Paralelismo**

O valor deste campo será sugerido para as derivações novas selecionadas para os produtos nas telas de cadastro de produtos. Quando Comprado, é a quantidade de dias necessário para reposição dos estoques do produto; Quando Produzido, é o Número de Dias de Precedência ao início de produção do Componente.

Observação

Esse campo não deve ser informado quando o produto for acabado.

Agrupamento Estoques

Código de agrupamento de estoque ao qual a família pertence. O código deve estar previamente cadastrado na tabela de agrupamentos, tipo estoques (E).

Agrupamento Produção

Código de agrupamento de Produção ao qual a família pertence. O código deve estar previamente cadastrado na tabela de agrupamentos, tipo produção (P).

Agrupamento Custos

Código de agrupamento de Custos ao qual a família pertence. O código deve estar previamente cadastrado na tabela de agrupamentos, tipo custos (U).

Agrupamento Comercial

Código de agrupamento comercial ao qual a família pertence. O código deve estar previamente cadastrado na tabela de agrupamentos, tipo comercial (C).

Agrupamento Cotas Venda

Código de agrupamento de cotas de venda ao qual a família pertence. O código deve estar previamente cadastrado na tabela de agrupamentos, tipo comercial (T).

Agrupamento Fiscal

Código de agrupamento fiscal ao qual a família pertence. O código deve estar previamente cadastrado na tabela de agrupamentos, tipo fiscal (F).

Gerar EAN13 automático?

Permite gerar os códigos EAN13 manualmente para cada produto em aplicação específica.

* Como montar o código EAN13

Observação

Para habilitar a tela de leitura de múltiplos volumes, o campo precisa estar com o valor N (Não) preenchido.

Tipo Produto para Impostos

No cadastramento será sugerido o tipo de produto para imposto cadastrado na origem, também permite ao usuário informar o tipo dos produtos desta família para impostos. Caso seja alterado o valor do campo Tipo Produto para Impostos na Origem desta família, este campo passa automaticamente a ter este valor.

* 0 - Não Classificado;
* 1 - Mercadorias;
* 2 - Matérias - primas;
* 3 - Produtos intermediários;
* 4 - Materiais de embalagem;
* 5 - Produtos manufaturados;
* 6 - Em Fabricação;
* 7 - Subproduto;
* 8 - Material de Uso e Consumo;
* 9 - Ativo Imobilizado;
* 10 - Serviços;
* 11 - Outros Insumos;
* 99 - Outras.

Classificação Fiscal

Código interno da classificação fiscal para os produtos da família.

Situação Tributária

Código interno da situação tributária para os produtos da família.

Sit Trib. IPI Vendas

Código da situação tributária de IPI nas operações de Vendas.

Sit Trib. PIS Vendas

Código da situação tributária de PIS nas operações de Vendas.

Sit Trib. COFINS Vendas

Código da situação tributária de COFINS nas operações de Vendas.

Recupera IPI

Indica se os produtos da família recuperam IPI.

Recupera COFINS

Indica se as notas fiscais com itens desta família terão recuperação de COFINS.

Tem ICMS

Indica se os produtos da família tributam ICMS.

Código ICMS Especial

Indica se os produtos da família possuem código de ICMS especial.

Código Redução Impostos

Código de redução dos impostos para os produtos da família.

Código ICMS Substituído

Código de substituição tributária de ICMS (ICMS Retido) para os produtos da família.

Recupera ICMS

Indica se os produtos da família fazem a recuperação de ICMS.

Recupera PIS

Indica se os produtos da família fazem a recuperação de PIS.

Código Substituição Tributária COFINS

Código de substituição tributária do COFINS (COFINS Retido).

Código Substituição Tributária PIS

Código de substituição tributária do PIS (PIS Retido).

% IRRF

Percentual do IRRF previsto para venda do produto.

% IRRF Empresa Pública

Percentual do IRRF para empresa pública ou equiparada do produto.

% PIS

Percentual do PIS válido para o produto.

% COFINS

Percentual de COFINS válido para o produto.

% CSLL

Percentual de CSLL válido para o produto.

% Outr. Ret.

Percentual de outras retenções válido para o produto.

Máscara 1 à 7

Define quais os tipos de Máscaras e em qual sequência serão utilizadas na codificação do produto. A soma das quantidades de posições das máscaras indicadas, deverá ser igual ao valor informado no campo Qtde. Posições Produto no início deste cadastro.

Exemplo:

* Quantidade Posições Produto: 7
* Máscara 1: IN-ART- Iniciais do artigo 2 posições
* Máscara 2: L3- Livre de 3 posições
* Máscara 3: TAM- Tamanho do artigo 2 posições
* Produto: PJ123GG (Pijama 123, tam: GG)

Natureza Gasto

Código da natureza de gasto.

Conta Contábil 1, 2, 3 e 4

Códigos contábeis definidos no plano de contas da empresa.

Depósito Padrão

Código do depósito padrão para os produtos da família. Para maiores detalhes, consulte a documentação da tela Sugestão de depósito padrão.

Família KIT

Indica se os produtos produzidos são do tipo KIT (não gera OP). Não é possível preencher o campo com valor S se nos parâmetros da origem
estiver que produto é controlado por lote.

Material Direto

Indica se o material é direto (produto comprado utilizado na fabricação de produtos produzidos).

Produto Misto

Indica se o produto é produzido mas também pode ser comprado.

Emite Guia Tráfego

Indica se é emitida a guia de tráfego para o produto.

Calcula ICMS Importação

Indica se a família calcula ICMS de importação nas notas fiscais de importação e ordens de compra.

Calcula PIS Importação

Indica se a família calcula PIS de importação nas notas fiscais de importação e ordens de compra.

Calcula COFINS Importação

Indica se a família calcula COFINS de importação nas notas fiscais de importação e ordens de compra.

Soma ICMS ao valor líquido importação

Indica se deve ser somado o valor de ICMS no valor líquido das notas fiscais de importação e ordens de compra.

Soma PIS ao valor líquido importação

Indica se deve ser somado o valor de PIS no valor líquido das notas fiscais de importação e ordens de compra.

Soma COFINS ao valor líquido importação

Indica se deve ser somado o valor de COFINS no valor líquido das notas fiscais de importação e ordens de compra.

Código do Plano de Inspeção

Código do plano de inspeção padrão.

Nota Mínima para Fornecimento

Nota mínima necessária para a aprovação de um fornecedor.

Marca da Família

Código da marca. A diferenciação de produtos por marca, permitirá que exista tratamento comercial por marca, como por exemplo condições de pagamento, tabelas de preço, etc. (o que é feito em tela própria para as ligações). As marcas são cadastradas na tela F076MAR.

Código Coleção

Código da coleção da família. O cadastro de coleções é realizado na tela F011CLC.

Controla p/ Série

Indica se a família do produto é controlada por número de série. O controle de série é efetuado na família. O tratamento das máscaras de série são feitos pela origem. Quando for feita uma alteração do campo de controle na origem, todas as famílias também serão alteradas (isto só é possível quando não houverem movimentos de estoque para esta origem). Somente é possível definir que uma família é controlada por série se a origem for controlada, nunca poderá existir uma famíliacontrolada por série quando a origem não for controlada.

Controla Validade

Consiste em todo o sistema se a data de validadede um determinado lote deve ser informada ou não. O ERP só permite esta informação quando estiver processando um movimento de entrada, tanto manual quanto de uma Nota Fiscal de Entrada.

Código Regra

Código da regra para cálculo do dígito verificador do código do produto. Mais detalhes aqui.

Gera O.P.

Indica se o produto gera Ordem de Produção. Somente leva em consideração quando for criado uma família nova.

Permite Gerar Orçamento

Indica se a família de produtos/serviços podem ser orçados.

Preço Custo

Ao informar algum valor nesse campo, o mesmo será sugerido ao inserir uma nova derivação no produto.

Controla valor individual série?

Indica se os produtos da família irão controlar entradas/saídas no estoque por série.

Data Alteração Controle Vlr Ind. Série

Data da alteração do controle do valor individual da série.

Hora Alteração Controle Vlr Ind. Série

Hora da alteração do controle do valor individual da série.

Tipo de Produto para Varejo

Indica o tipo de produto para o Varejo, este campo recebe como sugestão a informação cadastrada na tela
F083ORI. Caso não tenha sido cadastrado na origem do produto o campo fica desabilitado.

Exige montagem?

Indica se o produto exige montagem:

* quando selecionada a opção S (Sim), ao vender o produto no sistema caixa o vendedor poderá informar se o
  produto será ou não montado. Caso seja montado, é gerado uma pendência de montagem.
* quando selecionada a opção N (Não), ao vender o produto no sistema caixa finaliza a venda, sem gerar pendências de montagem.
* quando selecionada a opção O (Obriga), ao vender o produto no sistema caixa, o vendedor é obrigado a informar o montador que efetuará a montagem no produto no cliente e uma pendência de montagem é gerada automaticamente

Usuário Geração

Usuário que cadastrou a família.

Data Geração

Dia, mês e ano que a família foi criada.

Hora Geração

Hora que a família foi criada.

Usuário Última Alteração

Último usuário que realizou alterações do cadastro da família.

Data Última Alteração

Data da última alteração realizada no cadastro da família.

Hora Última Alteração

Última hora em que o cadastro da família foi alterada.

Integrar com Agronegócio

Indica se os produtos da família realizam integração com Agronegócio, no Gestão de Campo. Para o Gestão de Campo são necessárias outras configurações, veja os detalhes na documentação.

Situação

Indica de a família está A (Ativo) ou I (Inativo). Ao colocar a situação da família como inativa, todos os produtos/derivações ficarão inativos, independente de estarem presentes em registros abertos (ordens, pedidos, notas fiscais e etc...).

% PIS importação diferenciado

Percentual do PIS de importação diferenciado.

% COFINS importação diferenciado

Percentual do COFINS de importação diferenciado.

Aplicação

Para o Varejo Senior: Este campo deve ter o mesmo preenchimento que o campo Aplicação da tela de autotextos (F000ATX), assim, ao realizar o cadastro de uma ocorrência com o determinado produto (F118OCR), o autotexto será exibido no campo Detalhes Produto/Serviço da tela de ocorrências.

Cód. Autotexto

Para o Varejo Senior: Este campo deve ter o mesmo preenchimento que o campo Código Autotexto da tela de autotextos (F000ATX), assim, ao realizar o cadastro de uma ocorrência com o determinado produto (F118OCR), o autotexto será exibido no campo Detalhes Produto/Serviço da tela de ocorrências.

Permite incorporação OP 

Indica se as OPs de produtos da família permitem, ou não, a incorporação de produtos.

Observação

Só pode ser alterado para permitir a incorporação quando a origem também permitir. Uma vez preenchido com 'S' (sim), o campo só poderá ser alterado para 'N' (não) nos seguintes casos:

* se não houver nenhum produto desta família permitindo a incorporação;
* se não houver sequência operacional de roteiro que pertença a esta família permitindo a incorporação.

Indicativo Volume

Indica se o produto é controlado no sistema como sendo um volume. Este valor serve como sugestão no cadastramento do produto. Ver ajuda produto volume.

Tabela de presunção IRPJ

Informar o código da tabela de presunção IRPJ, no qual foi feito o cadastro na tela F055TPR.

Tabela de presunção CSLL

Informar o código da tabela de presunção CSLL, no qual foi feito o cadastro na tela F055TPR.

Ficha técnica na geração do SPED Fiscal

Este campo somente estará habilitando quando o tipo de produto da família for Produzido. Ele pode ser preenchido com as opções P - Padrão e R - Real. Essas opções determinam a forma de geração do registro 0210 - Consumo específico padronizado, do SPED Fiscal. Quando este campo não estiver preenchido, o sistema assume como opção a ficha técnica padrão. Quando já existir essa informação no cadastro da origem (F083ORI), ela será herdada para a família se for inclusão.

Ato cooperado

Este campo define se a família do produto caracteriza movimentos de Ato Cooperado. O preenchimento padrão deste campo é Sim.

Para que a operação (nota fiscais de saída ou entrada) seja considerada como Ato Cooperado, é necessário também, que o fornecedor seja um cooperado ativo (F085COP) e que o campo Ato cooperado esteja preenchido com Sim, nas seguintes telas:

* Cadastro de Produtos (F075PRO)
* Origem de Produtos (F083ORI)
* Agrupamento de produtos - produção (F013AGP)
* Ligação entre Fornecedor e Produto (F403FPR)

Este campo pode ser visualizado apenas com a proprietária de Agronegócio (ECCC).

Atenção

Os processos ECCC (Controle do Cooperado) e/ou SRPR (Controle do Produtor), bem como o parâmetro *-e:agro*, não estão mais disponíveis a partir da utilização do sistema no licenciamento por área. Para atendimento das rotinas específicas do Agronegócio, estão disponíveis os parâmetros globais **UtiCtrCoo** e **UtiCtrPrd**, na tela Manutenção dos parâmetros globais do sistema (F000PGS), onde o sistema passa a exigir apenas a existência da liberação das áreas de Mercado e Suprimentos (ou Backoffice, que libera as duas áreas).

* Para informações sobre licenciamento no Gestão Empresarial | ERP, acesse a documentação da tela Definição da Cópia (F000IPR)
* Para informações sobre os parâmetros globais **UtiCtrCoo** e **UtiCtrPrd**, acesse a documentação da tela Manutenção dos parâmetros globais do sistema (F000PGS)

Regime Tributário

Informe o código do regime tributário de apuração da contribuição social. Esta informação é sugerida no cadastro de produto (F075PRO e F075GFP) quando informada a família.

Origem código GTIN

Indica a origem de busca dos códigos GTIN (cEAN e cEANTrib) na geração dos documentos eletrônicos. Ao aplicar uma origem no cadastro da família, será apresentada a mensagem **A Origem do código GTIN, foi alterada. Deseja atualizar todos os produtos ligados a esta família?**. Confirmando, a origem será replicada para todos os produtos pertencentes a ela, mesmo se os produtos tiverem códigos diferentes.

Para mais informações consulte a documentação do GTIN.

Integra WMW

Indica se esse registro deve ser integrado para o WMW.

Situação WMW

Indica se esse registro está ativo ou inativo para o WMW.

Reg. entradas e saídas para controle de impostos.

Serve como sugestão para as futuras derivações cadastradas vinculadas à família.

Serviço Disp. Recebimento Eletrônico

Indica se o serviço está disponível para busca no recebimento eletrônico de NFS. É habilitado quando o campo Tipo Produto for **S-Serviço**.

**Duplica Produtos Outras Empresas**

Indica que os produtos da família podem ser duplicados automaticamente para as empresas do sistema que aceitam a duplicação (campo de mesmo nome na tela F070EMP). Para mais informações, confira a documentação do processo.

**Gerar autom. cód. barras DUN-14**

É uma parametrização utilizada no Cadastro de Produtos (F075PRO) e Cadastro de Produtos Agrupado (F075GFP) para geração automática do DUN-14 e ativação do botão **Un. Despacho**. Ver Geração automática do DUN-14

**Código Cultivar INDEA**

Permite informar um código de até 12 dígitos. Esse código deve ser um valor válido perante ao INDEA (Instituto de Defesa Agropecuária do Estado de Mato Grosso).

**Tipo Produto SisDev**

Permite informar o tipo de produto, de acordo com os valores disponíveis, que são: **2 - Sementes** ou **8 - Mudas**.

Integrar com Gestão Safra

Indica se este registro deve ser integrado com o Gestão Safra. Quando informado o valor "S - Sim" neste campo, o sistema gera pendências de integração para o produto Gestão Safra.

Importante

Quando os registros já tiverem sido integrados e for alterado o valor desse campo para "N - Não", as informações serão inativadas na Senior X ao executar o Processo automático 157 - Integração ERP x Gestão Safra.

Insumo Gestão Safra

Indica se a família do produto deve ser integrada como insumo no Gestão Safra. Quando esse campo estiver definido como:

* "N - Não" e o campo Integrar com Gestão Safra estiver igual a "N - Não", será considerada a família do produto como uma origem de cultura no Gestão Safra;
* "S - Sim" e o campo Integrar com Gestão Safra estiver igual a "S - Sim", será considerada a família do produto como insumo da safra no Gestão Safra.

Nota

Somente serão integradas famílias que estejam com a Situação definida como "A - Ativo".

## Páginas relacionadas

* [centro de custo](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/conceito_centrodecusto.htm)
* [Como montar o código EAN13](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/montagem_ean13.htm)
* [Sugestão de depósito padrão](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/sugestao-deposito-padrao.htm#menu_mercado/Sugestao-deposito-padrao)
* [F076MAR](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f076mar.htm)
* [F011CLC](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f011clc.htm)
* [aqui](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/conceito_digitoverifproduto.htm)
* [F083ORI](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f083ori.htm)
* [F000ATX](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000atx.htm)
* [F118OCR](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_servicos/f118ocr.htm)
* [produto volume](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_manufatura/conceito_produto_com_controle_de_volumes.htm)
* [F055TPR](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f055tpr.htm)
* [Ato Cooperado](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/manuais_processos/agronegocio/processos/ato-cooperado/inicio.htm)
* [F085COP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f085cop.htm)
* [F075PRO](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075pro.htm)
* [F013AGP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f013agp.htm)
* [F403FPR](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f403fpr.htm)
* [Manutenção dos parâmetros globais do sistema (F000PGS)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm)
* [Definição da Cópia (F000IPR)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_ajuda/f000ipr.htm)
* [GTIN](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/manuais_processos/mercado/nf-e/regras-e-sugestoes-valores.htm#gtin)
* [recebimento eletrônico de NFS](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/manuais_processos/recebimento-eletronico/recebimento-eletronico.htm#nfs-e)
* [F070EMP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070emp.htm)
* [confira a documentação do processo](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/manuais_processos/mercado/duplicacao-automatica.htm)
* [F075GFP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075gfp.htm)
* [Geração automática do DUN-14](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_manufatura/dun-14.htm)
* [Processo automático 157 - Integração ERP x Gestão Safra](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/processos-automaticos/157-integracao-erp-gestao-safra.htm)
