# Guias

> **Fonte:** F075GFP - Cadastro de Produtos — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075gfp.htm  
> **Trilha:** Ajuda por telas > Cadastros > Produtos e Serviços > Produtos  
> **Telas citadas:** E075DER, E075PRO, E075VDR, E815NBP, F000HIS, F012FAM, F015MED, F015UMA, F055TPR, F070EPF, F070FEF, F070FVE, F075PRO, F113REM, F120GPD, F135CCA, F135CMC, F445PRC, F460PFO, F621GCP, F621GPP, F621GPV, F660ISP, F665ICA, F700CMC, F813CNP, F900AQP  
> **Identificadores de regras:** CHA-900CLPOP01

---
## Tipo Comprado

Código de produto da ANP

Indicativo do código do combustível da ANP.

Produto Específico

Indicativo do enquadramento de produto específico (meramente informativo para NF-e).

Desc. Prod. ANP

Descrição do produto conforme a ANP (Agência Nacional do Petróleo, Gás Natural e Biocombustíveis), de acordo com o Sistema de Informações de Movimentação de Produtos - SIMP (http://www.anp.gov.br/simp/).

Gerar grupo Repasse ICMS ST na NF-e

Indicativo se o produto deve gerar o grupo ICMSST no arquivo XML da NF-e. Esse parâmetro é habilitado apenas se o campo Código de produto da ANP estiver preenchido. Se o parâmetro estiver configurado como **Sim** e o produto for vendido em operação com CST 60, ao invés de gerar o grupo ICMS60 no arquivo XML da NF-e, é gerado o grupo ICMSST.

% GLP

Percentual do Gás Liquefeito de Petróleo derivado do petróleo no produto GLP.

% Gás Natural Nac.

Percentual de Gás Natural Nacional (GLGNn) para o produto GLP.

% Gás Natural Imp.

Percentual de Gás Natural Importado (GLGNi) para o produto GLP.

Valor Partida

Valor de partida do produto GLP. Deve ser informado o valor por quilograma sem ICMS.

Observações

O produto GLP possui código ANP igual a 210203001.

### Botões

Procurar

Filtra os produtos a serem carregados para a grade, através da máscara do produto e derivação. Para usar este recurso, é obrigatório que a família tenha Máscara de Derivação e no mínimo duas Máscaras de Produto ligadas a ela.

Consistência entre produto e derivação

* ao ligar uma derivação ao produto se ela for adicionada como Ativa o produto
  caso esteja inativo será ativado automaticamente;
* ao desligar/excluir todas as derivações do produto ele será inativado
  automaticamente;
* ao inativar todas as derivações ligadas ao produto o mesmo será inativado
  automaticamente;
* ao ativar uma derivação caso o produto esteja inativo será necessário ativá-lo
  manualmente;
* ao inativar um produto, todas as derivações ficarão inativas;
* ao ativar um produto, todas as derivações ficarão ativas.

## Produtos

Mostra todos os produtos selecionados através dos parâmetros
informados na tela de cadastro. Permite cadastrar novos produtos que ficarão vinculados a
família de produto informada na tela. Pode-se atualizar a descrição do produto, o
complemento da descrição do produto, a unidade de medida 2, a unidade de medida 3 e a
situação do produto.

O campo Descrição herda a descrição do campo Quantidade Caracteres
Descrição Produto, do cadastro da empresa. Esse total é o que define o total de
caracteres na descrição.  
Quando o cursor estiver posicionado na grade Produtos, e a família
possuir máscara de derivação, foi implementado para que o botão Prod X Cli
localizado no rodapé da tela, fique desabilitado. Esse botão somente ficará
habilitado ao posicionar o cursor sobre alguma derivação selecionada na grade
Derivações Possíveis.

Incorp. OP

 Indica se OPs do produto cadastrado permitem ou não a incorporação de
produtos.

Observação

Poderá ser alterado para permitir incorporação, se a família também
permitir. Uma vez permitida, só poderá ser alterado para 'N' (não) se
haver OP pendente (não finalizada ou cancelada), cujo produto final seja
o em questão, contendo alguma sequência operacional permitindo a
incorporação.

**% Lim. Incorp. OP**

Define o percentual limite de incorporação de produtos em OPs.  
 É utilizado na incorporação de produtos na OP, alertando o usuário se
a quantidade incorporada (somada a outras quantidades antes incorporadas
nesta mesma OP) dividida pela quantidade prevista da OP, supera o
percentual  definido. Porém, o alerta é informativo, não impedindo
que o usuário confirme a incorporação.

* Ao ser definido com o valor 0 (zero), indica que não há limite de
  incorporação.
* Poderá ter valor maior que 0 (zero), se o produto estiver configurado
  para permitir incorporação.

Zera estoque saída balança

Apenas com proprietária Agronegócio. Tem a finalidade de
informar se o produto pode ter, ou não, seu estoque zerado no
momento de um faturamento realizado por uma saída via balança, quando possuir
a terceira unidade de medida.

U.M.

Unidade de medida do produto para estoque.

Observação

Para produtos do tipo Comprados e Passagem Direta é possível que a unidade de medida de estoque do produto
seja diferente da família, desde que no cadastro da Origem, o campo Altera Unidade de
Medida de Compra/Direto, estiver definido igual a "S - Sim".

2ª U.M. 1  
Código da 2ª unidade de medida.Usada normalmente no cadastro da ficha técnica.

3ª U.M. 2  
Código da unidade de medida. Unidade de medida alternativa disponível para
outras aplicações, por exemplo nas rotinas que envolvem Balança.   
Este campo é utilizado nas rotinas de Agronegócio para a entrada de produto via
balança sendo obrigatório a parametrização.Para utilizar o produto nos Contratos com Fornecedores (F460PFO), é necessário que a unidade de medida possua no máximo três casas decimais. O cadastro da unidade de medida é feito na tela F015MED ou F015UMA.

Utiliza Decimais Cadastro Unidade Medida

Defina se o produto utiliza a quantidade de casas decimais da unidade de medida (F015MED) para arredondamento de valores no momento da integração de produção e estoque (F660ISP).

Cla. Fis.

Código interno de classificação fiscal do produto. Nesse campo é
possível informar apenas classificações fiscais de níveis analíticos
(com 8 caracteres numéricos XX.XX.XXXX).

**Importante**

O parâmetro global ExiAtuCes pode ser utilizado para definir se a mensagem **Sugerir o especificador substituição tributária conforme a classificação fiscal?** deve ser apresentada ou não. Por padrão, o valor do parâmetro é **P-Perguntar**. Caso queira que a mensagem não seja apresentada, o parâmetro global deve ser alterado para **N-Não**. Nesse caso, o **Especificador substituição tributária** não será atualizado em relação à classificação fiscal informada no cadastro do produto.

Sit. Tri.

Código de situação tributária do produto.

É de 2ª/ 3ª Ql ou Reaprov.

Indicativo se o produto é utilizado para estocar produto de 2ª e 3ª qualidade
ou reaproveitado (refugo).  
É possível gerar ordens de produção, ligar produtos de 2ª e 3ª qualidade ou
reaproveitado a um roteiro ou a um modelo.

Dep. Pad. 

Ao cadastrar um novo produto, neste campo será atribuído o depósito padrão da família. Se não informado o campo Família, será atribuído o depósito padrão da origem. Se o depósito padrão da família e origem não forem preenchidos, este campo ficará em branco, sendo permitido cadastrar novo produto com o campo Depósito Padrão sem preenchimento.

Sit.

Indicativo da situação do produto. Quando na família do
produto, o campo Situação está como I (inativo), todos os produtos/derivações
da família ficarão inativos. Não será permitido inserir novos produtos enquanto
a família estiver com esta situação.

Classe Produto

Indica como o produto será tratado comercialmente ou contabilmente na
empresa, servido para filtro em algumas rotinas do sistema.

1. De Estoque: Produtos que terão controle de estoques.
2. De Passagem Direta: Permite efetuar compras, mas não controla estoque, sua entrada na
   empresa tem destino ligado a um centro de custos. Se a transação utilizada na entrada
   tiver integração com estoques, automaticamente o sistema fará uma saída por
   requisição. Isto é, ficará registrada a entrada e saída do produto, pois o mesmo não
   é mantido em estoques. Este produto não é disponibilizado para vendas.
3. Imobilizado: Para eventuais necessidades de cadastro dos bens da empresa como produto.
4. Outros: Para os produtos que não se encaixam nas demais classes.  
   Uma vez cadastrado implementado para que o atributo Classe do
   Produto não possa ser alterado quando o produto possuir algum movimento de
   estoque, requisição, solicitação de compra ou ordem de compra. Ao alterar a
   classe do produto será exibido uma mensagem nas seguintes situações:  
   * De passagem direta para qualquer outra classe;
   * De qualquer outra classe para passagem direta;
   * De qualquer outra classe para imobilizado (outros).

Gera OP

* S - Produto gera ordens de produção.
* N - Produto não gera ordens de produção.

**Observação**

1. Permite alterar o indicativo de N (Não) para S (Sim), mesmo que exista
   necessidades de produção em aberto com o produto, desde que estas necessidades
   sejam provenientes da explosão de origens de produtos sem rastreamento ou para
   reposição de estoque e com o valor do campo GerOrp igual a N na tabela
   Necessidades Produtos (E815NBP).  
    As necessidades de produção com GerOrp igual a N são canceladas
   automaticamente ao alterar o valor deste campo de N para S, ou seja, não é
   listada na tela F813CNP.
2. Quando o campo Gera OP for definido como
   N(Não), caso este produto for intermediário de um pedido, não será gerado
   necessidades de produção para ele. Somente será possível gerar ordens de
   produção para este, caso for gerado produção para repor estoques.

Peso Bruto

Peso bruto do produto. Ao informar ou alterar algum valor
nesse campo, o mesmo será sugerido na derivação do produto.

Peso Líquido

Peso líquido do produto. Ao informar ou alterar algum valor
nesse campo, o mesmo será sugerido na derivação do produto.

Toler.Peso

Tolerância do peso líquido do produto/derivação. Ao informar
ou alterar algum valor nesse campo, o mesmo será sugerido na derivação do
produto.

Volume

Volume do produto. Ao informar ou alterar algum valor nesse campo, o mesmo será sugerido na derivação do produto.

Se os campos Largura, Comprimento e Altura estiverem preenchidos, o volume é calculado automaticamente, onde o resultado não pode ultrapassar 999.999,99999.

Tipo prod. para impostos

Permite ao usuário informar o tipo dos produtos para impostos. Para este
campo estão disponíveis os seguintes valores:

0. Não Classificado;
1. Mercadorias;
2. Matérias - primas;  
   Produtos intermediários;  
   Materiais de embalagem;  
   Produtos manufaturados;  
   Em Fabricação.

Este campo será inicializado com 0 (Não Classificado) para todos os produtos já
cadastrados via Correct. Os valores correspondem aos valores para este campo
disponível na tela F075PRO.
Ao incluir um novo produto o valor do campo Tipo Produto para Impostos será
inicializado com o mesmo valor definido na família deste produto.
Caso seja alterado o valor do campo Tipo Produto para Impostos na Família ou
na Origem deste produto este campo passa automaticamente a ter este valor.

Lote Base

Este campo somente ficará habilitado se a origem do produto controlar por lote. Ao optar por "S - Sim", no momento de
liberar a OP, se o identificador de regras
CHA-900CLPOP01 estiver cadastrado, ativo e ligado a uma regra e o campo Gerar Lote OP na origem
do produto estiver como "S - Na Liberação OP" irá gerar um lote para o produto da O.P..

% Funrural

Percentual do imposto funrural do produto a ser descontado em notas fiscais de saída. Veja mais detalhes na documentação de processo do Funrural.

**Observação**

* O % Funrural já considera o valor do Gilrat em sua porcentagem;
* O % Funrural não pode ser inferior ao % GILRAT.

% GILRAT

Percentual de Gilrat que compõe a alíquota de Funrural.

Base Recálculo

Este campo ficará habilitado somente se o tipo de produto for produzido ou comprado.

* A opção N - Não, indica que a quantidade prevista do componente será recalculada quando for
  alterada a quantidade prevista da OP na tela F900AQP.
* A opção S - Sim, indica que a quantidade prevista do componente será recalculada quando for alterada a quantidade prevista dos produtos (componentes) da OP.

% SENAR/SENAT

Percentual do imposto SENAR/SENAT do produto a ser descontado em notas fiscais de saída. Veja mais detalhes na documentação de processos do Senar.

Ori. fiscal merc.

Permite informar a origem fiscal da mercadoria.

0. Nacional;
1. Estrangeiro - Importação Direta;
2. Estrangeiro - Adquirida no mercado interno.

Este campo (E75PRO.ORIMER) é preenchido com o primeiro dígito do valor
informado no campo Situação Tributária (E075PRO.CODSTR). Caso este esteja em
branco, é atribuído então o valor padrão igual a zero.

Por exemplo, se no campo Situação Tributária possuir a
informação 120, então é preenchido com o valor 1. Se o primeiro dígito deste
campo for diferente do código da Situação Tributária é emitida uma mensagem
para corrigir as informações dos campos.

Ao criar novos produtos, o valor é
herdado da família (atribuído o valor existente no primeiro dígito do campo
Situação Tributária), caso não exista
valor informado na família, este campo é preenchido com o valor igual a zero.

Base Cálculo Crédito

Permite definir a natureza da base de cálculo do crédito de maneira
customizada para os itens de produto.

Exige montagem?

Indica se o produto exige montagem. Quando selecionada a opção S
(Sim), ao vender o produto no sistema caixa o vendedor poderá informar se o produto será ou não montado. Caso seja montado, é gerado
uma pendência de montagem.

Quando selecionada a opção N (Não), ao
vender o produto no sistema caixa finaliza a venda, sem gerar pendências
de montagem. Quando selecionada a opção O (Obriga), ao vender o
produto no sistema caixa, o vendedor é obrigado a informar o montador
que efetuará a montagem no produto no cliente e uma pendência de montagem é gerada automaticamente.

Exige entrega?

Indica se o produto exige ser entregue.

Tipo de Produto para Varejo

Indica o tipo de produto para o Varejo.

Agr. Garantia Estendida

Código de agrupamento de materiais/produtos para garantia
estendida.

Quantidade volumes do produto

Quantidade de volumes que vai compor o produto.

**Observação**

Estando o produto com este indicativo maior que zero, o
sistema obriga que as derivações deste produto tenham um código de
barras livre (E075DER.CODBA2).  
Quando for informado no produto quantidade de volumes maior que zero,
o sistema irá consistir na derivação que seja informado um código de
barras livre. Caso a derivação não possua código de barras livre
informado, ao gerar os volumes o sistema irá consistir, este código de
barras livre, precisa ter os seus 4 últimos caracteres com valor 0
(zero).

Produto Fora de Linha

Indica se o produto está fora de linha e não pode ser reposto.  
Somente poderá ser alterado quando o produto não utilizar mascara de
derivação.

Produto vendido separadamente

Indica se o produto pode ser vendido separadamente.

Exige NF-e

Indica se o produto exige que seja emitido uma NF-e no momento da venda.

Regime Tributário

Este campo tem as seguintes opções:

* C (Regime cumulativo);
* U (Regime não cumulativo) e;
* N (Nenhum).  
   Esta opção influencia nos tipos de impostos: 41 (PIS Não Cumulativo (SPED)),
  43 (PIS Cumulativo (SPED)), 42 (COFINS Não Cumulativo (SPED)),
  43&#39; (PIS Cumulativo (SPED)) e 44 (COFINS Cumulativo (SPED)) e na apuração do faturamento na gestão de tributos.

Na inclusão de novos produtos será sugerido o regime tributário
conforme segue:

* Se a forma de tributação da filial (Cadastros > Filiais > Parâmetros
  por Gestão > Tributos (F070FEF)) for Real Estimativa, Real Balanço
  Suspensão e Real, então o regime tributário sugerido para o produto e
  serviço (Cadastros > Produtos e Serviços > Produtos e Serviços, telas
  Individual e Agrupado) será U(Não cumulativo).
* Se a forma de tributação da filial (Cadastros > Filiais > Parâmetros
  por Gestão > Tributos (F070FEF)) for Presumido, então o regime
  tributário sugerido para o produto e serviço (Cadastros > Produtos e
  Serviços > Produtos e Serviços, telas Individual e Agrupado) será
  C(Cumulativo).
* Para outra forma de tributação informada na filial será sugerido como
  regime tributário do produto e serviço N(nenhum).

Ind. Vol.

Indica se o produto é controlado no sistema como sendo um volume. Ver ajuda
produto volume.

Contr. Créd. ICMS

Exibido apenas com proprietária agronegócio.
Este campo controla o crédito de ICMS para essa modalidade na tela F445PRC.

Qtd. Meses Créd. 

Exibido apenas com proprietária agronegócio.
Indica a quantidade de parcelas de credito rural e é habilitado se o campo
Controla Crédito ICMS estiver parametrizado com Sim.

Tipo Crédito ICMS

Este campo é habilitado se o campo Controla Crédito ICMS for preenchido com Sim. Seu preenchimento define que tipo de a que tipo de crédito de ICMS o produto pertence, no processo de Crédito do Produtor Rural.

**Observação**

Sempre que este campo estiver preenchido igual a "S - Sim", o campo Qtd.
Meses Créd deve ter o valor igual a 1 (um).

Mod. ICMS

Ao inserir um novo produto que tenha a família parametrizada com a
modalidade na tela F012FAM, será sugerida a
modalidade da família neste campo.

% Diferimento   
Percentual que será utilizado para o cálculo do valor do ICMS Diferido em cotações, contratos, ordens de compras, pedidos, pré-faturas e notas fiscais de entrada e saída.

Tabela de presunção IRPJ

Informar o código da tabela de presunção IRPJ, no qual foi feito o cadastro na tela F055TPR.

Tabela de presunção CSLL

Informar o código da tabela de presunção CSLL, no qual foi feito o cadastro na tela F055TPR.

Contr. Vlr Ind. Série

Define se a valorização dos estoques será controlada por série. Para mais informações consulte a documentação
Fechamento dos Estoques - Detalhes.

Emite receita agronômica

Se estiver preenchido com SIM, possibilita a geração e impressão de receita agronômica na tela F113REM.  
Este campo pode ser visualizado apenas com a Proprietária do Receituário Agronômico.

Identificação do parceiro

Este campo corresponde ao código de Bula do Agrotóxico, presente na tabela de agrotóxicos do sistema Winfit. Ao encontrar o respectivo código na tabela do sistema parceiro, e informando o valor a esse campo, isso possibilitará a integração das informações do Winfit de geração de bula, sendo elas: a própria bula, as classes do agrotóxico, os tipos de aplicação. Este campo pode ser visualizado apenas com a Proprietária do Receituário Agronômico.

% IRRF Empresa Pública

Percentual do IRRF para empresa pública ou equiparada do produto.

**Voltagem do Produto**

Indicativo da voltagem do produto.

**Cor do produto**

Indicativo da cor do produto

**Derivação do produto**

Indicativo da derivação do produto. Na inserção de uma nova derivação, este campo deve ser sugerido com o valor contido no campo **Voltagem do Produto**.

Ficha CAT 83/09

Informe neste campo para qual ficha da CAT 83/09 o produto será integrado (F665ICA), conforme parametrizações do seu código de lançamento. As opções disponíveis são:

* Ficha 1A: Controle de materiais;
* Ficha 1C: Controle de energia elétrica;
* Ficha 3A: Controle de produtos acabados;
* Ficha 3B: Controle de mercadorias de revenda.

Observação

Este campo não é de preenchimento obrigatório.

Ficha SPED Fiscal

Este campo somente estará habilitando quando o produto for do tipo Produzido. Ele pode ser preenchido com as opções P - Padrão e R - Real, que determinam a forma de geração do registro 0210 - Consumo específico padronizado, do SPED Fiscal. Quando este campo não estiver preenchido, o sistema assume como opção a ficha técnica padrão. Quando já existir essa informação no cadastro da família (F012FAM), ela será herdada para o produto se for uma inclusão.

Apres. Prod. Agrup.

Defina neste campo se as ordens de produção devem ser apresentadas de forma agrupada na apuração do bloco K, realizada na tela Produção e Estoque (F660ISP).

Suj. Int. ZFM

Identifica se está sujeito ao processo de internação na Zona Franca de Manaus.

Tipo Produto DCI

Identifica o tipo de produto para a Declaração de Controle de Internação.

ICMS Antecipação

Exibe o código do ICMS Antecipação utilizado.

Descrição (ICMS Antecipação)

Exibe a descrição do ICMS Antecipação utilizado.

Classificação Convênio ICMS

Código da classificação do convênio ICMS 115/2013. O valor informado neste campo é gerado no campo 14 - Código de classificação do item do registro **I - Itens** do relatório Convênio ICMS 115/2003 (CIAE052).

Tipo de utilização 

Tipo de utilização do convênio. O valor informado neste campo é gerado no campo 4 - Fase ou tipo de Utilização do registro **I - Itens** quando for uma nota fiscal do tipo 21 ou 22. E caso seja uma nota fiscal do tipo 06 – Energia Elétrica gera informação do campo Tipo de ligação.

Código de enquadramento

Código do enquadramento legal do IPI.

Origem do código GTIN

Indica a origem de busca dos códigos GTIN (cEAN e cEANTrib) na geração dos documentos eletrônicos. Para mais informações, consulte a documentação do GTIN.

Tipo do GTIN

Indica qual o formato do GTIN que será usado na sua apresentação nos documentos fiscais:

1. GTIN8;
2. GTIN12;
3. GTIN13;
4. GTIN14.

Ex.: Tipo de GTIN = GTIN8. O GTIN será apresentado com o tamanho 8 nos documentos fiscais. Caso seu tamanho seja menor que 8, ele será preenchido com zeros à esquerda.

**Motivo Desoneração do ICMS**

Aceita os seguintes valores:

* 0 - Nenhum;
* 1 - Taxi;
* 6 - Utilitários e Motocicletas da Amazônia Ocidental e Áreas de Livre Comércio (Resolução 714/88 e 790/94 - CONTRAN e suas alterações);
* 9 - Outros;
* 90 - Solicitado pelo fisco.

Calcula FAF   
Indica o Fator de ajuste de Fruição (FAF) no cadastro do produto.

Tributação por Vlr. Min. Unidade Medida

Indica se o valor de imposto calculado por percentual deve ser comparado com o valor parametrizado para o item na tabela de tributação por quantidade cadastrada. Quando o campo estiver parametrizado como **S - Sim**, caso o valor calculado seja inferior ao cadastrado na tabela de tributação, será utilizado o valor cadastrado, ou seja, passará a tributar por quantidade, e não mais por percentual.

Produto Consignado

Indica se o produto cadastrado é consignado ou não.

Tipo de produção

Serve para indicar o tipo de produção e possui as opções C-Produção Conjunta e T-Produção Tradicional.

**Tipo de Resíduo Produzido**

Tem por finalidade o preenchimento do campo 19 do registro 1391 do SPED Fiscal.

**Art. 119 do RICMS/2017**

Está relacionado à geração da ADRC-ST. Identifica se uma NCM tem relação com o art. 119 do RICMS/2017 do estado do Paraná. Sempre que o conteúdo do campo for alterado na Classificação Fiscal, todos os produtos que possuem a mesma Classificação Fiscal serão alterados.

**Per. do Dif. de ICMS FCP**

Percentual do diferimento de ICMS relativo ao FCP sugerido para o cálculo do valor do diferimento de ICMS relativo ao FCP nos processos de vendas, faturamento, compras e recebimento. Este campo não tem preenchimento obrigatório.

Unidade de Medida para Etiqueta   
Campo destinado ao preenchimento da unidade de medida para impressão de etiquetas no Gestão de Supermercados.

Fator de Conversão para Etiqueta   
Campo destinado ao preenchimento do fator de conversão para impressão de etiquetas no Gestão de Supermercados.

Observação

Os campos Unidade de Medida para Etiqueta e Fator de Conversão para Etiqueta só ficarão visíveis nesta tela, quando o usuário possuir Proprietária de Gestão de Supermercados.

Considerar no I-Simp

Indique se o produto deve ou não ser exportado no I-Simp.

Dispensa coleta (I-Simp)

Indica se o produto é dispensado de coleta.

Data Alteração para Palmtop

Indica a data da alteração para Palmtop

Hora Alteração para Palmtop

Indica a hora da alteração para Palmtop

## Derivações Possíveis

Mostra todas as derivações possíveis para o produto. Elas
são sugeridas a partir da máscara de derivações informada na família do produto
a qual ele pertence.  
As derivações desejadas para o produto devem ser marcadas,
e a alteração de qualquer informação referente a elas, deve ser feita pelos botões
no rodapé da tela.  As alterações realizadas em um desses campos serão gravadas
automaticamente e caso ela ocorra em uma derivação ainda não cadastrada, será marcada como
ativa e cadastrada.

Data Validade

Este campo é utilizado para inserir um prazo máximo de validade para a derivação do produto. O formato de preenchimento é DD/MM/AAAA.

O sistema utiliza a data de validade informada nesse campo nas seguintes rotinas:

* Na tela de pedidos (F120GPD), quando existe uma data de validade na derivação do produto, ela será validada ao inserir o item no pedido. A validação realizada pelo sistema é feita com base na data de entrada do item, ou seja, a data de validade informada na derivação do produto precisa ser maior do que a data de entrada do item. Caso não seja, o sistema retornará a mensagem: “Data entrega maior que validade do produto/derivação.
* No módulo de custos, a data da validade é utilizada como filtro através do botão Seleção (telas F621GCP, F621GPP e F621GPV). O usuário define a data de validade para a qual ele deseja validação e o sistema compara com o que foi preenchido no campo Data Validade da derivação do produto. Tendo a data de validade informada no filtro, o sistema lista na tela produtos cuja data de validade for maior ou igual à data informada na seleção.
* Na tela de Modelo (Composição do Produto/Serviço) (F700CMC), o sistema também valida a data de validade na inclusão do componente. Neste caso, a data de validade do componente tem que ser maior ou igual à data previamente cadastrada no sistema.

Número Registro ANVISA

Informe o número de registro dos medicamentos e matérias-primas farmacêuticas.

Produção em Escala Relevante

Informe se o produto é produzido em escala relevante ou não.

Os produtos produzidos em escala não relevante cuja NCM esteja relacionada no Anexo XXVII do Convênio 52/2017 devem ser preenchidas com o valor **N - Produzido em Escala Não Relevante**. Para mais informações, consulte a documentação do Indicador de Escala Relevante.

Especificador substituição tributária

Informe o Código especificador da substituição tributária (CEST) da derivação.

**Cor do produto**

Código da cor do produto.

**Descrição da Cor**

Indicativo da descrição da cor do produto.

### Campos

**Sel.**

Ao marcar uma derivação, ela será cadastrada para o produto que estiver
selecionado e a situação da derivação será A (Ativa). Ao desmarcar uma derivação, ela será excluída, mantendo-se na grade como derivação
possível de cadastrar.

Preço Reposição

O preço de reposição será automaticamente
atualizado com o valor de 0,01 quando for criada uma nova derivação.

Conferir Qtde nas Cargas

Quando o campo estiver com valor igual a "S- Sim", as cargas somente serão fechadas após conferência, utilizando as telas F135CCA ou F135CMC. Quando o campo estiver com valor igual a "N- Não", o sistema possibilitará fechar as cargas no momento de sua geração.

Esse campo só ficará habilitado para edição quando o campo Conferir Carga Antes do Fechamento estiver parametrizado com valor igual a "S - Sim" na tela F070FVE.

Situação

Situação da derivação do
produto, podendo ser A (Ativa) ou I (Inativa). Se a derivação ainda não está
cadastrada para o produto, ou seja, uma derivação possível, a situação será
sugerida como A (Ativa).

Qtde Múltipla

Quantidade múltipla para cálculo da geração de ordem de produção/compra.
Esse processo somente acontecerá para geração de OP's via pedido.

Observação

Este campo somente ficará habilitado para produtos
produzidos e com origens que geram OP por produto/derivação (ver no cadastro de Origens, o campo O.P.gera por Produto/Derivação
que deverá estar
definido como S (Sim)).

Qtde. Mínima

Quantidade mínima de unidades do produto permitido por ordem de produção/compra. Esse processo somente acontecerá para geração de OPs via pedido.

* Na geração das ordens de produção o sistema sempre obedecerá a quantidade mínima do produto definida neste campo, ou seja, mesmo que um pedido ou geração manual de OP tenha necessidade menor que o valor definido neste campo, o sistema irá gerar a quantidade aqui informada.
* Quando o campo **Produto 2ª, 3ª Qualidade ou Reaproveitado** for diferente de N (Normal), esse campo não ficará habilitado.
* Para origens que geram OP por produto/derivação, é possível estabelecer quantidade mínima, múltipla e máxima na derivação do produto. Ao gerar uma OP, o sistema busca esta informação primeiro na tabela de derivações, caso não encontre nada, busca na tabela de produtos.

Observação

Somente ficará habilitado para produtos
produzidos e com origens que geram OP por produto/derivação (ver no cadastros de
Origens o campo O.P.gera por Produto/Derivação que deverá definido estar
como S (Sim)).

Qtde. Máxima

Quantidade máxima de unidades da derivação do produto para uma ordem de
produção/compra.
Esse processo somente acontecerá para geração de OP's via pedido.

Observação

Este campo somente ficará habilitado para produtos
produzidos e com origens que geram OP por produto/derivação (ver no cadastro de Origens, o campo O.P. gera por Produto/Derivação,
que deverá estar
definido como S (Sim)).

Código Tabela Preço Pis

Seleção de tabelas de preços com aplicações “3”(Cálculo por Quantidade
(Vendas)), “4”(Cálculo por Quantidade (Compras)) e “5”(Cálculo por Quantidade
(Ambas)).

Código Tabela Preço Cofins

Seleção de tabelas de preços com aplicações “3”(Cálculo por Quantidade
(Vendas)), “4”(Cálculo por Quantidade (Compras)) e “5”(Cálculo por Quantidade
(Ambas)).

Código Tabela Preço IPI

Seleção de tabelas de preços com aplicações “3”(Cálculo por Quantidade
(Vendas)), “4”(Cálculo por Quantidade (Compras)) e “5”(Cálculo por Quantidade
(Ambas)).

Observação

As tabelas de preço de PIS/COFINS e IPI
informadas no cadastro do produto/serviço permitem que o Gestão Empresarial | ERP calcule estes
impostos utilizando base de cálculo por quantidade e alíquota em valor.A tabela
informada deve pertencer a uma aplicação de cálculo por quantidade (3, 4 ou 5) e
deve conter a respectiva alíquota em valor para o produto/serviço. Esta tabela
será verificada no cálculo de notas fiscais de entrada, ordens de compra, notas
fiscais de saída e pedidos.

CST PIS Venda

Código da situação tributária de PIS Venda.
Se for informado um valor no campo Sit. Trib. COFINS Vendas no cadastro de na família, este valor será sugerido neste campo automaticamente.

CST COFINS Venda

Código da situação tributária de COFINS Venda.
Se for informado um valor no campo Sit. Trib. COFINS Vendas no cadastro de na família, este valor será sugerido neste campo automaticamente.

CST IPI Venda

Código da situação tributária de IPI Venda.
Se for informado um valor no campo Sit. Trib. COFINS Vendas no cadastro de na família, este valor será sugerido neste campo automaticamente.

Classe Cons. Energia/Gás

Indicativo da classe de consumo de energia elétrica ou gás.

Classe Fornec. água

Indicativo da classe de fornecimento de água.

Tipo de ligação

Indicativo sobre o tipo de ligação elétrica.

Cod. do grupo de tensão

Indicativo a qual grupo de tensão está enquadrado.

Densidade

Permite informar valores para ser considerado na densidade do produto, sem necessariamente
informar peso líquido.

% CIDE Tecnologia

Permite informar o percentual de imposto  CIDE tecnologia. Este valor é gravado na tabela E075DER.PerCit.

Volume

Volume da derivação. Esse campo recebe o valor do volume do produto como sugestão. Se for alterado o valor dos campos Largura, Comprimento e Altura (inserção ou alteração do cadastro), o volume é calculado automaticamente, onde o resultado não pode ultrapassar 999.999,99999.

Ind. Vol.

Indica se o produto é controlado no sistema como sendo um volume. Confira a documentação sobre produto volume.

Código fiscal federal

Código fiscal federal

Código fiscal estadual

Código fiscal estadual

Código fiscal municipal

Código fiscal municipal

Descr. Fis

Descrição fiscal do item gravada na base de dados da tabela (E075VDR) ao alterar alguma informação na derivação do produto. Essa informação ficará gravada na guia Derivações da tela Históricos Cadastrais (F000HIS).

Observação

Este campo somente estará disponível para edição caso campo Alterar Código/Descrição da tela Parâmetros Fiscais (F070EPF) esteja parametrizado igual a " S - Sim".

Mot. Isenção Anvisa

Motivo de isenção do registro Anvisa. Essa informação é gerada no campo **xMotivoIsencao** do Grupo K no arquivo XML de NF-e/NFC-e.

## Páginas relacionadas

* [Contratos com Fornecedores](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/manuais_processos/agronegocio/processos/contrato/contratos.htm)
* [F460PFO](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f460pfo.htm)
* [F015MED](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f015med.htm)
* [F015UMA](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f015uma.htm)
* [F660ISP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f660isp.htm)
* [ExiAtuCes](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#ExiAtuCes)
* [F813CNP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_manufatura/f813cnp.htm)
* [liberar a OP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f083ori.htm#gerar_lote_op)
* [CHA-900CLPOP01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/cha_900clpop01.htm)
* [Funrural](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/manuais_processos/agronegocio/processos/impostos/funrural.htm)
* [F900AQP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_manufatura/f900aqp.htm)
* [Senar](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/manuais_processos/agronegocio/processos/impostos/senar.htm)
* [produto volume](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_manufatura/conceito_produto_com_controle_de_volumes.htm)
* [F445PRC](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f445prc.htm)
* [Crédito do Produtor Rural](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/manuais_processos/agronegocio/processos/credito_icms/icms_produtor.htm)
* [F012FAM](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f012fam.htm)
* [F055TPR](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f055tpr.htm)
* [Fechamento dos Estoques - Detalhes](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f215fes_fechamento_detalhes.htm#Pre%C3%A7o)
* [F113REM](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f113rem.htm)
* [F665ICA](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f665ica.htm)
* [ICMS Antecipação](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/impostos-icms.htm#icms-antecipacao)
* [CIAE052](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/relatorios/arquivos-eletronicos-estaduais/ciae052.htm)
* [GTIN](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/manuais_processos/mercado/nf-e/regras-e-sugestoes-valores.htm#gtin)
* [F120GPD](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f120gpd.htm)
* [F621GCP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_custos/f621gcp.htm)
* [F621GPP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_custos/f621gpp.htm)
* [F621GPV](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_custos/f621gpv.htm)
* [F700CMC](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_manufatura/f700cmc.htm)
* [Indicador de Escala Relevante](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/manuais_processos/mercado/nf-e/regras-e-sugestoes-valores.htm#indicador_de_escala_relevante)
* [F135CCA](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f135cca.htm)
* [F135CMC](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f135cmc.htm)
* [F070FVE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070fve.htm)
