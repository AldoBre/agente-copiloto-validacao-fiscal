# ICMS Diferido

> **Fonte:** Rotinas de ICMS — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/impostos-icms.htm  
> **Trilha:** Segmentos > Compliance > Configurações para cálculos fiscais > Impostos  
> **Telas citadas:** F000INE, F001TCP, F001TVE, F070EMP, F070FVE, F075GFP, F075PCA, F075PPC, F075PRO, F080CSA, F080SER, F085CAD, F085HCL, F095CAD, F095HFO, F120CAC, F120CAI, F120CAP, F120CAR, F120GPB, F120GPD, F135FCA, F135FCP, F140CIP, F140CNF, F140GNF, F140LOT, F140PRE, F403FPR, F403FSE, F403LFP, F403LFS, F410CEA, F410COS, F410PCT, F420GOC, F420OCC, F420OPE, F420OPS, F420VAL, F440CNE, F440GNE, F440GOC, F460CTR, F460PFO  
> **Identificadores de regras:** COM-000ALSTR01

---
É o ICMS recolhido pelo tomador da prestação, ou seja, a responsabilidade pelo pagamento fica atribuída ao adquirente, destinatário ou usuário do serviço que motivar o encerramento do diferimento, na condição de substituto tributário.

O ICMS Diferido pode ser calculado nas rotinas de compras, recebimento, distribuição, vendas e faturamento.

Para que o cálculo do diferimento do ICMS seja realizado, o código da situação tributária utilizado deve terminar em 51 (Diferimento). Quando esse código não for visível em telas, ele deve ser cadastrado previamente nas ligações do Fornecedor X Produto (F403FPR e F403LFP), Fornecedor X Serviço (F403FSE e F403LFS), Produto X Cliente (F075PPC e F075PCA), Cadastro do Produto (F075PRO e F075GFP) ou Cadastro do Serviço (F080SER e F080CSA).

As regras para a busca do código da situação tributária em Suprimentos são:

1. Transação de compras (F001TCP)
2. Cadastro do Produto/Serviço (F075PRO/F080SER)
3. Ligação Produto x Fornecedor (F403FPR)

Em Mercado são:

1. Transação de vendas (F001TVE)
2. Quando o parâmetro global VenProStr estiver ativo: Cadastro do Produto/Serviço (F075PRO/F080SER)
3. Definições do cliente (F085HCL)
4. Ligação Produto x Cliente (F075PPC)

   Observação

   Primeiro é feita a consulta com derivação e, depois, sem derivação.

Se não tiver cadastrado em nenhum dos locais acima, o sistema irá montar o código manualmente conforme configuração do documento que está sendo feito, podendo ainda, ser alterado pelo Identificador de Regras COM-000ALSTR01.

Para o cálculo do valor do ICMS Diferido, primeiramente o percentual que será utilizado deve estar informado. Desta forma, o campo % Diferimento pode ser preenchido nas seguintes telas de cadastros: Definições do Cliente (F085CAD e F085HCL), Produto X Cliente (F075PPC e F075PCA), Produto (F075PRO e F075GFP), Serviço (F080SER e F080CSA), Transação de Venda (F001TVE), Definições do Fornecedor (F095CAD e F095HFO), Fornecedor X Produto (F403FPR e F403LFP), Fornecedor X Serviço (F403FSE e F403LFS) e Transação de Compra (F001TCP).

O cálculo do ICMS diferido pode ser realizado por base ou valor, a forma de cálculo é parametrizada no campo Tipo Cálculo Diferimento da guia Vendas 2, da tela Parâmetros da Filial para Vendas (F070FVE). Quando o cálculo do ICMS diferido for por base (opção 0 – Diferimento de ICMS por base), o valor da base do ICMS normal será o resultado da diferença entre a base de cálculo do ICMS original e o valor da base de cálculo do ICMS diferido.

Importante

Como o tratamento dos valores de diferimento de ICMS total variam de acordo com o estado, deve-se utilizar o campo **Forma de envio do ICMS 51**, na guia Documentos Eletrônicos, tela Parâmetros da Filial para Vendas (F070FVE). Possui duas opções:

* **C - Completa**: nesse caso, na geração do .XML da nota, quando houver percentual de diferimento igual a 100%, serão geradas todas as tags abaixo do CST x51
* **R - Resumida**: nesse caso, na geração do .XML da nota, quando houver percentual de diferimento igual a 100%, serão geradas apenas as tags **Origem** e **CST**

Quando o percentual de diferimento for menor que 100%, o ICMS 51 sempre será enviado de forma completa.

A base de ICMS diferida apresentada no sistema não é apresentada em nenhuma obrigação fiscal ou acessória, somente o valor do ICMS diferido precisa estar com o valor correto. Sendo assim, não é obrigatório o cálculo da base Diferimento.

O parâmetro dinâmico NOTAFISCAL.ICMSDIFERIDO.REMOVERDOPRECOUNITARIO da filial, indica se ao incluir um item em uma nota fiscal, deve ser removido o valor do ICMS diferido do valor unitário do produto. Sendo obrigatório informar uma tabela de preço para a operação ser efetuada. Para a nota fiscal de saída, é possível também efetuar o calculo utilizando um pedido de venda, assim utilizando o preço bruto do item do pedido de venda.

## Gestão de Compras

Nas telas de Contratos (F460CTR e F460PFO) e Cotações de Preços (F410CEA, F410COS e F410PCT), o campo % Diferimento também poderá ser informado, se ainda não estiver cadastrado.

Caso o percentual do diferimento já esteja informado nas telas de cadastros, ele será sugerido na seguinte ordem:

1. Percentual informado nos Parâmetros fiscais de produto e serviços por filial e estado
2. Percentual informado na ligação Fornecedor X Produto ou Fornecedor X Serviço
3. Percentual informado no cadastro do Produto ou Serviço
4. Percentual informado no cadastro do Fornecedor
5. Percentual informado na transação da compra

Importante

* Caso o código da situação tributária não terminar em 51 não será possível informar o percentual de diferimento e ele também não será sugerido
* Para que o percentual de diferimento seja sugerido para os serviços, é necessário que o parâmetro Possui serviços c/ ICMS/IPI (F070EMP) esteja preenchido com S-Sim
* A sugestão do percentual de diferimento informado na ligação Fornecedor X Produto somente será realizada se o parâmetro Usa Produto X Fornecedor, da tela F075PRO, estiver definido como S-Sim

Nas telas de geração de ordens de compra via contrato, cotação ou pedido (F420OCC e F420OPS), o campo % Diferimento também está disponível nas guias de Produtos e Serviços e será preenchido de acordo com o percentual informado/sugerido nesses documentos.

Além do campo % Diferimento, nas guias Produtos e Serviços da tela Ordem de Compra Agrupada (F420GOC), os campos Base ICMS Dif., % ICMS Dif. e Valor ICMS Dif. também estão disponíveis. Apenas será possível alterar o valor do percentual do diferimento, os demais campos somente podem ser consultados.

Observação

* O percentual e o valor do ICMS diferido serão recalculados sempre que houver alteração dos itens e suas quantidades, bem como a alteração do fornecedor
* Se o percentual do diferimento do ICMS estiver informado no contrato, cotação ou pedido, ao gerar a ordem de compra via esses documentos, o percentual do diferimento será mantido
* Na telas Ordem de Compra via Cotação (F420OPS) e Ordem de Compra via Pedido (F420OPE), não é possível buscar o código da situação tributária do documento de origem
* Dessa maneira, ao processas as informações nessas telas para gerar a ordem de compra, a sugestão do código da situação tributária será feita novamente e caso o final não seja mais 51 (Diferimento), o diferimento do ICMS não será calculado, mesmo que no documento de origem exista o cálculo

Na tela de Valores Diversos da Ordem de Compra (F420VAL), acessada via botão Valores da tela F440GOC, os campos Base ICMS Diferimento e Valor ICMS Diferimentoapresentarão a somatória da Base e do Valor do ICMS Diferido de todos os itens da ordem de compra.

## Gestão de Recebimento

Para a geração de notas fiscais de entrada com o cálculo do ICMS diferido, os campos % Diferimento,Base ICMS Dif., % ICMS Dif. e Valor ICMS Dif. estão disponíveis nas grades das guias Produtos e Serviços da tela Nota Fiscal de Entrada Agrupada (F440GNE). O campo % Diferimento somente poderá ser informado quando o código da situação tributária finalizar em 51 (Diferimento). Os demais campos criados serão calculados conforme o percentual informado.

Na tela de Cálculos dos Dados Gerias da Nota Fiscal de Entrada (F440CNE), acessada via botão Cálculosda tela F440GNE, os campos ICMS Diferido - Base e ICMS Diferido - Valor apresentarão a somatória da Base e do Valor do ICMS Diferido de todos os itens da nota fiscal de saída.

Como na ordem de compra, caso o percentual do diferimento já esteja informado nas telas de cadastros, ele será sugerido na seguinte ordem:

1. Percentual informado nos Parâmetros fiscais de produto e serviços por filial e estado
2. Percentual informado na ligação Fornecedor X Produto ou Fornecedor X Serviço
3. Percentual informado no cadastro do Produto ou Serviço
4. Percentual informado no cadastro do Fornecedor
5. Percentual informado na transação da compra

Observação

* Para que o percentual de diferimento seja sugerido para os serviços, é necessário que o parâmetro Possui serviços c/ ICMS/IPI (F070EMP) esteja preenchido com S-Sim
* A sugestão do percentual de diferimento informado na ligação Fornecedor X Produto somente será realizada se o parâmetro Usa Produto X Fornecedor, da tela F075PRO, estiver definido como S-Sim

Ao gerar uma nota fiscal de entrada via uma ordem de compra ou contrato, os valores do diferimento na nota fiscal serão iguais aos valores calculados nesses documentos.

Na geração de notas fiscais de entrada via recebimento de documento eletrônico, as tags pDif e vICMSDif do XML são consideradas e correspondem ao percentual e ao valor do diferimento do ICMS, respectivamente. Esses valores serão salvos em seus respectivos campos das tabelas de itens da nota fiscal via recebimento eletrônico. Nessas tabelas, o valor total do ICMS diferido da nota (soma do valor dos itens) também será armazenado.

Na tela Recebimento de Documento Eletrônico (F000INE), os campos % Diferimento e Valor ICMS Dif. estão disponíveis nas grades dos itens da nota fiscal de entrada, para que esses valores possam ser visualizados e editados. Ao processar o recebimento da nota fiscal de entrada, o valor e o percentual do ICMS diferido serão gravados nesse documento.

Para as notas fiscais de devolução, o percentual do diferimento e o percentual do ICMS diferido dos itens serão os mesmo utilizados para a nota fiscal que está sendo devolvida. A base e o valor do ICMS Diferido serão copiados proporcionalmente à quantidade que está sendo devolvida.

No web service com.senior.g5.co.mcm.cpr.notafiscal@GravarNotasFiscaisEntrada os campos % Diferimento,Base ICMS Dif., % ICMS Dif. e Valor ICMS Dif. são de preenchimento opcional e somente podem ser informados se o código da situação tributária finalizar em 51. Neste caso, ao informar o percentual do diferimento, os demais campos serão são de preenchimento obrigatório.

## Gestão de Vendas

Nas telas de emissão de pedidos (F120GPB e F120GPD), os campos % Diferimentoe % ICMS Dif. foram adicionados estão disponíveis nas grades de Produtos e Serviços. Apenas o campo % Diferimento poderá ser informado, caso o código da situação tributária finalizar em 51. O campo do percentual do ICMS será calculado e preenchido de acordo com o percentual de diferimento.

Caso o percentual do diferimento já esteja informado nas telas de cadastros, ele será sugerido na seguinte ordem:

1. Percentual informado nos Parâmetros fiscais de produto e serviços por filial e estado
2. Percentual informado na ligação entre Produto X Cliente
3. Percentual informado no cadastro do Produto ou Serviço
4. Percentual informado no cadastro do Cliente
5. Percentual informado na transação da venda

Observação

* Para que o percentual de diferimento seja sugerido para os serviços, é necessário que o parâmetro Possui serviços c/ ICMS/IPI (F070EMP) esteja preenchido com S-Sim
* A sugestão do percentual de diferimento informado na ligação Produto X Cliente somente será realizada se o parâmetro Buscar parâmetros fiscais, da tela F075PPC, estiver definido como S-Sim

## Gestão de Distribuição

Na geração de pré-faturas via pedidos, os campos % Diferimentoe % ICMS Dif. serão gerados conforme seus valores do pedido. A pré-fatura será gerada considerando os valores proporcionais ao que está sendo lançado. Os percentuais e alíquotas não consideram a proporcionalidade.

Nas telas de Formação de Cargas (F135FCA e F135FCP) não será possível visualizar os percentuais de diferimento e ICMS diferido. Estes valores somente serão visualizados após a geração da pré-fatura.

## Gestão de Faturamento

Ao gerar a nota fiscal via pedido ou pré-fatura, os valores dos campos % Diferimento,Base ICMS Dif., % ICMS Dif. e Valor ICMS Dif. serão iguais aos informados nos documentos originais.

A quantidade a faturar do pedido pode ser alterada. Nesse caso, deve-se copiar os valores de diferimento proporcional ao que esta sendo faturado (não é válido para percentuais(.

Nas telas Preparação de Nota Fiscal de Saída (F140PRE) e Faturamento de Pedidos Agrupado (F140LOT), apenas os campos % Diferimento e % ICMS Dif. estão disponíveis para digitação e visualização nas grades de Produtos, Serviços e Pedidos, respectivamente.

Na tela Notas Fiscais de Saída (F140GNF), os campos % Diferimento, Base ICMS Dif., % ICMS Dif. e Valor ICMS Dif. estão disponíveis nas grades de Produtos e Serviços.

Apenas o campo % Diferimento poderá ser informado, caso o código da situação tributária finalizar em 51. Os demais campos serão calculados e preenchidos de acordo com o percentual.

Caso o percentual do diferimento já esteja informado nas telas de cadastros, ele será sugerido na seguinte ordem:

1. Percentual informado nos Parâmetros fiscais de produto e serviços por filial e estado
2. Percentual informado na ligação entre Produto X Cliente
3. Percentual informado no cadastro do Produto ou Serviço
4. Percentual informado no cadastro do Cliente
5. Percentual informado na transação da venda

Observação

* Para que o percentual de diferimento seja sugerido para os serviços, é necessário que o parâmetro Possui serviços c/ ICMS/IPI (F070EMP) esteja preenchido com S-Sim
* A sugestão do percentual de diferimento informado na ligação Produto X Cliente somente será realizada se o parâmetro Buscar parâmetros fiscais, da tela F075PPC, estiver definido como S-Sim

### Consulta da Base e do valor do ICMS Diferido

Nas telas F120CAP e F120CAI; F120CAR e F120CAC; F140CIP e F140CNF, acessadas via botão Cálculos do cabeçalho e das guias Produtos e Serviços das telas F120GPD, F120GPB e F140GNF, respectivamente, os campos ICMS Diferido Base e ICMS Diferido Valor apresentarão a somatória da Base e do Valor do ICMS Diferido de todos os itens da nota fiscal de saída.

### Devolução

A devolução da nota fiscal pode ser realizada através da tela Preparação da Nota Fiscal Saída (F140PRE), sendo gerada uma nota de saída de tipo 9 (Devolução). Para a nota fiscal de devolução, o percentual do diferimento e o percentual do ICMS diferido serão copiados da nota fiscal original com o valor integral. Os valores da base de cálculo do ICMS diferido e o valor do ICMS diferido serão calculados de forma proporcional ao que está sendo devolvido.

Observação

Quando um item ou algo na nota fiscal de devolução já gerada for alterado e que possa influenciar no valor do diferimento, o cálculo deve ser refeito com base na situação atual da nota fiscal de devolução.

## Web service e geração de .XML

Para o web service com.senior.g5.co.mcm.ven.notafiscal, versão 2, estão disponíveis nos itens de produto e serviço os campos % Diferimento,Base ICMS Dif., % ICMS Dif. e Valor ICMS Dif.

Observação

Esses campos não podem ser alterados. Em outras versões desse web service, os campos do diferimento do ICMS não estão disponíveis.

Ao gerar o arquivo XML da nota fiscal de saída, as seguintes tags são geradas:

* Tag vBC: Gerada de acordo com a parametrização do cálculo do ICMS: quando for **1 - Diferimento de ICMS por valor** e **0 - Diferimento de ICMS por base** recebem apenas o valor da base de cálculo do ICMS normal
* Tag pICM: Percentual de ICMS da operação
* Tag vICMSOp: Valor ICMS Diferido + Valor ICMS Operação
* Tag pDif: Percentual de diferimento gravado no item da nota fiscal
* Tag vICMSDif: Valor do ICMS diferido do item da nota fiscal
* Tag vICMS: Valor do ICMS da operação

## Após o cálculo do diferimento

Após o cálculo do diferimento, os campos abaixo serão preenchidos nos itens do pedido, ordem de compra, nota fiscal de entrada ou nota fiscal de saída:

* Base Cálculo ICMS Diferido
* % ICMS Diferido
* Valor ICMS Diferido

E, os seguintes campos serão atualizados:

* Base Cálculo ICMS Operação
* % ICMS Operação
* Valor ICMS Operação
* Valor Isento/Outros

### Exemplos de cálculos

Base de cálculo do ICMS Diferido

Fórmula da Base Cálculo ICMS Diferido = Base Cálculo ICMS Operação \* (Percentual de Diferimento / 100).

## Exemplo 1

Diferimento por valor/base

Percentual de Diferimento = 100%

Base Cálculo ICMS Operação = R$ 1000,00

Base Cálculo ICMS Diferido = 1000,00 \* (100 / 100) = 1000,00

## Exemplo 2

**Diferimento por valor/base**

Percentual de Diferimento = 80%

Base Cálculo ICMS Operação = R$ 1000,00

Base Cálculo ICMS Diferido = 1000,00 \* (80 / 100) = 800,00

Percentual de ICMS da operação para o percentual de ICMS diferido

Fórmula: Percentual ICMS Diferido = Percentual do ICMS da Operação.

Cálculo do valor do ICMS diferido

Fórmula do Valor ICMS Diferido = Base Cálculo ICMS Diferido \* (Percentual ICMS Diferido / 100).

## Exemplo 1

Diferimento por valor/base

Percentual de Diferimento = 100 %

Base Cálculo ICMS Operação = R$ 1000,00

Percentual do ICMS da Operação = 12%

Valor do ICMS da Operação = 120,00

Percentual ICMS Diferido = 12%

Base Cálculo ICMS Diferido = 1000,00 \* (100 / 100) = 1000,00

Valor ICMS Diferido = 1000,00 \* (12 / 100) = 120,00

## Exemplo 2

Diferimento por valor/base

Percentual de Diferimento = 80%

Base Cálculo ICMS Operação = R$ 1000,00

Percentual do ICMS da Operação = 12%

Valor do ICMS da Operação = 120,00

Percentual ICMS Diferido = 12%

Base Cálculo ICMS Diferido = 1000,00 \* (80 / 100) = 800,00

Valor ICMS Diferido = 800,00 \* (12 / 100) = 96,00

Cálculo da nova base de cálculo do ICMS de operação

## Exemplo 1

**Diferimento por base**

Percentual de Diferimento = 100 %

Base Cálculo ICMS Operação = R$ 1000,00

Percentual do ICMS da Operação = 12%

Valor do ICMS da Operação = 120,00

Percentual ICMS Diferido = 12%

Base Cálculo ICMS Diferido = 1000,00 \* (100 / 100) = 1000,00

Valor ICMS Diferido = 1000,00 \* (12 / 100) = 120,00

Fórmula da Base de Cálculo ICMS Operação Após Diferimento = Base Cálculo ICMS Operação - Base Cálculo ICMS Diferido.

Base de Cálculo ICMS Operação Após Diferimento = 1000,00 - 1000,00 = 0,00

Base Cálculo ICMS Operação = Base de Cálculo ICMS Operação Após Diferimento.

**Diferimento por valor**

Percentual de Diferimento = 100 %

Base Cálculo ICMS Operação = R$ 1000,00

Percentual do ICMS da Operação = 12%

Valor do ICMS da Operação = 120,00

Percentual ICMS Diferido = 12%

Base Cálculo ICMS Diferido = 1000,00 \* (100 / 100) = 1000,00

Valor ICMS Diferido = 1000,00 \* (12 / 100) = 120,00

Fórmula da Base de Cálculo ICMS Operação Após Diferimento = Base Cálculo ICMS Operação

Base de Cálculo ICMS Operação Após Diferimento = 1000,00

Base Cálculo ICMS Operação = Base de Cálculo ICMS Operação Após Diferimento.

## Exemplo 2

**Diferimento por base**

Percentual de Diferimento = 80%

Base Cálculo ICMS Operação = R$ 1000,00

Percentual do ICMS da Operação = 12%

Valor do ICMS da Operação = 120,00

Percentual ICMS Diferido = 12%

Base Cálculo ICMS Diferido = 1000,00 \* (80 / 100) = 800,00

Valor ICMS Diferido = 800,00 \* (12 / 100) = 96,00

Fórmula da Base de Cálculo ICMS Operação Após Diferimento = Base Cálculo ICMS Operação - Base Cálculo ICMS Diferido.

Base de Cálculo ICMS Operação Após Diferimento = 1000,00 - 800,00 = 200,00

Base Cálculo ICMS Operação = Base de Cálculo ICMS Operação Após Diferimento.

**Diferimento por valor**

Percentual de Diferimento = 80%

Base Cálculo ICMS Operação = R$ 1000,00

Percentual do ICMS da Operação = 12%

Valor do ICMS da Operação = 120,00

Percentual ICMS Diferido = 12%

Base Cálculo ICMS Diferido = 1000,00 \* (80 / 100) = 800,00

Valor ICMS Diferido = 800,00 \* (12 / 100) = 96,00

Fórmula da Base de Cálculo ICMS Operação Após Diferimento = Base Cálculo ICMS Operação

Base de Cálculo ICMS Operação Após Diferimento = 1000,00

Base Cálculo ICMS Operação = Base de Cálculo ICMS Operação Após Diferimento.

Cálculo do novo percentual do ICMS de operação

## Exemplo 1

**Diferimento por base**

Percentual de Diferimento = 100 %

Base Cálculo ICMS Operação = R$ 1000,00

Percentual do ICMS da Operação = 12%

Valor do ICMS da Operação = 120,00

Percentual ICMS Diferido = 12%

Base Cálculo ICMS Diferido = 1000,00 \* (100 / 100) = 1000,00

Valor ICMS Diferido = 1000,00 \* (12 / 100) = 120,00

Base de Cálculo ICMS Operação Após Diferimento = 1000,00 - 1000,00 = 0,00

Base Cálculo ICMS Operação = Base de Cálculo ICMS Operação Após Diferimento

Percentual ICMS Operação Após Diferimento = Se Percentual de Diferimento = 100 %, então 0%, senão Percentual do ICMS da Operação (12%)

**Diferimento por valor**

Percentual de Diferimento = 100 %

Base Cálculo ICMS Operação = R$ 1000,00

Percentual do ICMS da Operação = 12%

Valor do ICMS da Operação = 120,00

Percentual ICMS Diferido = 12%

Base Cálculo ICMS Diferido = 1000,00 \* (100 / 100) = 1000,00

Valor ICMS Diferido = 1000,00 \* (12 / 100) = 120,00

Base de Cálculo ICMS Operação Após Diferimento = 1000,00

Base Cálculo ICMS Operação = Base de Cálculo ICMS Operação Após Diferimento

Percentual ICMS Operação Após Diferimento = Percentual do ICMS da Operação (12%)

## Exemplo 2

**Diferimento por base**

Percentual de Diferimento = 80%

Base Cálculo ICMS Operação = R$ 1000,00

Percentual do ICMS da Operação = 12%

Valor do ICMS da Operação = 120,00

Percentual ICMS Diferido = 12%

Base Cálculo ICMS Diferido = 1000,00 \* (80 / 100) = 800,00

Valor ICMS Diferido = 800,00 \* (12 / 100) = 96,00

Base de Cálculo ICMS Operação Após Diferimento = 1000,00 - 800,00 = 200,00

Base Cálculo ICMS Operação = Base de Cálculo ICMS Operação Após Diferimento

Percentual ICMS Operação Após Diferimento = Se Percentual de Diferimento = 100 %, então 0%, senão Percentual do ICMS da Operação (12%)

**Diferimento por valor**

Percentual de Diferimento = 80%

Base Cálculo ICMS Operação = R$ 1000,00

Percentual do ICMS da Operação = 12%

Valor do ICMS da Operação = 120,00

Percentual ICMS Diferido = 12%

Base Cálculo ICMS Diferido = 1000,00 \* (80 / 100) = 800,00

Valor ICMS Diferido = 800,00 \* (12 / 100) = 96,00

Base de Cálculo ICMS Operação Após Diferimento = 1000,00

Base Cálculo ICMS Operação = Base de Cálculo ICMS Operação Após Diferimento

Percentual ICMS Operação Após Diferimento = Percentual do ICMS da Operação (12%)

Cálculo do novo valor do ICMS de operação

Fórmula do Valor ICMS Operação Após Diferimento = Base de Cálculo ICMS Operação Após Diferimento \* (Percentual ICMS Operação Após Diferimento / 100).

## Exemplo 1

**Diferimento por base**

Percentual de Diferimento = 100 %

Base Cálculo ICMS Operação = R$ 1000,00

Percentual do ICMS da Operação = 12%

Valor do ICMS da Operação = 120,00

Percentual ICMS Diferido = 12%

Base Cálculo ICMS Diferido = 1000,00 \* (100 / 100) = 1000,00

Valor ICMS Diferido = 1000,00 \* (12 / 100) = 120,00

Base de Cálculo ICMS Operação Após Diferimento = 1000,00 - 1000,00 = 0,00

Base Cálculo ICMS Operação = Base de Cálculo ICMS Operação Após Diferimento

Percentual ICMS Operação Após Diferimento = 0%

Percentual ICMS Operação = Percentual ICMS Operação Após Diferimento

Fórmula do Valor ICMS Operação Após Diferimento = Base de Cálculo ICMS Operação Após Diferimento \* (Percentual ICMS Operação Após Diferimento / 100).

Valor ICMS Operação Após Diferimento = 0,00 \* (0 / 100) = 0,00

**Diferimento por valor**

Percentual de Diferimento = 100 %

Base Cálculo ICMS Operação = R$ 1000,00

Percentual do ICMS da Operação = 12%

Valor do ICMS da Operação = 120,00

Percentual ICMS Diferido = 12%

Base Cálculo ICMS Diferido = 1000,00 \* (100 / 100) = 1000,00

Valor ICMS Diferido = 1000,00 \* (12 / 100) = 120,00

Base de Cálculo ICMS Operação Após Diferimento = 1000,00

Base Cálculo ICMS Operação = Base de Cálculo ICMS Operação Após Diferimento

Percentual ICMS Operação Após Diferimento = 12%

Percentual ICMS Operação = Percentual ICMS Operação Após Diferimento

Fórmula do Valor ICMS Operação Após Diferimento = Valor do ICMS da Operação - Valor ICMS Diferido

Valor ICMS Operação Após Diferimento = 120,00 - 120,00 = 0,00

## Exemplo 2

**Diferimento por base**

Percentual de Diferimento = 80%

Base Cálculo ICMS Operação = R$ 1000,00

Percentual do ICMS da Operação = 12%

Valor do ICMS da Operação = 120,00

Percentual ICMS Diferido = 12%

Base Cálculo ICMS Diferido = 1000,00 \* (80 / 100) = 800,00

Valor ICMS Diferido = 800,00 \* (12 / 100) = 96,00

Base de Cálculo ICMS Operação Após Diferimento = 1000,00 - 800,00 = 200,00

Base Cálculo ICMS Operação = Base de Cálculo ICMS Operação Após Diferimento

Percentual ICMS Operação Após Diferimento = 12%

Percentual ICMS Operação = Percentual ICMS Operação Após Diferimento

Fórmula do Valor ICMS Operação Após Diferimento = Base de Cálculo ICMS Operação Após Diferimento \* (Percentual ICMS Operação Após Diferimento / 100).

Valor ICMS Operação Após Diferimento = 200,00 \* (12 / 100) = 24,00

**Diferimento por valor**

Percentual de Diferimento = 80%

Base Cálculo ICMS Operação = R$ 1000,00

Percentual do ICMS da Operação = 12%

Valor do ICMS da Operação = 120,00

Percentual ICMS Diferido = 12%

Base Cálculo ICMS Diferido = 1000,00 \* (80 / 100) = 800,00

Valor ICMS Diferido = 800,00 \* (12 / 100) = 96,00

Base de Cálculo ICMS Operação Após Diferimento = 1000,00

Base Cálculo ICMS Operação = Base de Cálculo ICMS Operação Após Diferimento

Percentual ICMS Operação Após Diferimento = 12%

Percentual ICMS Operação = Percentual ICMS Operação Após Diferimento

Fórmula do Valor ICMS Operação Após Diferimento = Valor do ICMS da Operação - Valor ICMS Diferido

Valor ICMS Operação Após Diferimento = 120,00 - 96,00 = 24,00

Cálculo do novo valor para Isento/Outros

Fórmula do Valor Isento/Outros Após Diferimento = Base de Cálculo ICMS Operação - Base de Cálculo ICMS Operação Após Diferimento + Valor Isento/Outros.

## Exemplo 1

**Diferimento por base**

Percentual de Diferimento = 100 %

Base Cálculo ICMS Operação = R$ 1000,00

Percentual do ICMS da Operação = 12%

Percentual ICMS Diferido = 12%

Base Cálculo ICMS Diferido = 1000,00 \* (100 / 100) = 1000,00

Valor ICMS Diferido = 1000,00 \* (12 / 100) = 120,00

Base de Cálculo ICMS Operação Após Diferimento = 1000,00 - 1000,00 = 0,00

Base Cálculo ICMS Operação = Base de Cálculo ICMS Operação Após Diferimento

Percentual ICMS Operação Após Diferimento = 0%

Percentual ICMS Operação = Percentual ICMS Operação Após Diferimento

Valor ICMS Operação Após Diferimento = 0 \* (0 / 100) = 0,00

Valor ICMS Operação = Valor ICMS Operação Após Diferimento

Valor Isento/Outros Após Diferimento = 1000,00 - 0,00 + 0,00 = 1000,00

**Diferimento por valor**

Percentual de Diferimento = 100 %

Base Cálculo ICMS Operação = R$ 1000,00

Percentual do ICMS da Operação = 12%

Percentual ICMS Diferido = 12%

Base Cálculo ICMS Diferido = 1000,00 \* (100 / 100) = 1000,00

Valor ICMS Diferido = 1000,00 \* (12 / 100) = 120,00

Base de Cálculo ICMS Operação Após Diferimento = 1000,00

Base Cálculo ICMS Operação = Base de Cálculo ICMS Operação Após Diferimento

Percentual ICMS Operação Após Diferimento = 12%

Percentual ICMS Operação = Percentual ICMS Operação Após Diferimento

Valor ICMS Operação Após Diferimento = 120,00 - 120,00 = 0,00

Valor ICMS Operação = Valor ICMS Operação Após Diferimento

Valor Isento/Outros Após Diferimento = 1000,00 - 0,00 + 0,00 = 1000,00

## Exemplo 2

**Diferimento por base**

Percentual de Diferimento = 80%

Valor Isento/Outros = 50,00

Base Cálculo ICMS Operação = R$ 1000,00

Percentual do ICMS da Operação = 12%

Percentual ICMS Diferido = 12%

Base Cálculo ICMS Diferido = 1000,00 \* (80 / 100) = 800,00

Valor ICMS Diferido = 800,00 \* (12 / 100) = 96,00

Base de Cálculo ICMS Operação Após Diferimento = 1000,00 - 800,00 = 200,00

Base Cálculo ICMS Operação = Base de Cálculo ICMS Operação Após Diferimento

Percentual ICMS Operação Após Diferimento = Se 200 = 0, então 0%, senão 12% = 12%

Percentual ICMS Operação = Percentual ICMS Operação Após Diferimento

Valor ICMS Operação Após Diferimento = 200,00 \* (12 / 100) = 24,00

Valor ICMS Operação = Valor ICMS Operação Após Diferimento

Valor Isento/Outros Após Diferimento = 1000,00 - 200,00 + 50,00 = 850,00

Diferimento por valor

Percentual de Diferimento = 80%

Valor Isento/Outros = 50,00

Base Cálculo ICMS Operação = R$ 1000,00

Percentual do ICMS da Operação = 12%

Percentual ICMS Diferido = 12%

Base Cálculo ICMS Diferido = 1000,00 \* (80 / 100) = 800,00

Valor ICMS Diferido = 800,00 \* (12 / 100) = 96,00

Base de Cálculo ICMS Operação Após Diferimento = 1000,00

Base Cálculo ICMS Operação = Base de Cálculo ICMS Operação Após Diferimento

Percentual ICMS Operação Após Diferimento = 12%

Percentual ICMS Operação = Percentual ICMS Operação Após Diferimento

Valor ICMS Operação Após Diferimento = 120,00 - 96,00 = 24,00

Valor ICMS Operação = Valor ICMS Operação Após Diferimento

Valor Isento/Outros Após Diferimento = 1000,00 - 1000,00 + 50,00 = 50,00

Cálculo para as resoluções 13/2019 RJ e Resolução 79/2022 SC

Observação

Para habilitar as resoluções, altere a opção **Cálculo de Desoneração de ICMS** na tela Parâmetros da Filial para Vendas (F070FVE) no caso de notas fiscais de saída e Cadastro de Fornecedores (F095CAD) no caso de notas fiscais de entrada.

## Exemplo 1

Diferimento total

Percentual de Diferimento = 100%

Base Cálculo ICMS Operação = R$ 1000,00

Percentual do ICMS da Operação = 18%

Valor do ICMS da Operação = 180,00

Percentual ICMS Diferido = 18%

Base Cálculo ICMS Diferido = 1000 / (1 - 0,18) = 1000 / 0,82 = 1.219,51

Valor do ICMS da Operação = 1219,51 \* (18 / 100) = 219,51

Valor ICMS Diferido = 219,51 \* 100% = 219,51

Fórmula do Valor ICMS Operação = Valor do produto com ICMS \* (Percentual ICMS / 100)

Fórmula do Valor ICMS Diferido = Valor do ICMS da Operação \* (Percentual ICMS Diferido / 100)

## Exemplo 2

Observação

Para incluir o valor do ICMS no valor unitário do produto (vProd), é necessário informar uma tabela de preço ao incluir um item na nota fiscal.

Diferimento parcial

Percentual de Diferimento = 66,66%

Base Cálculo ICMS Operação = R$ 2000,00

Percentual do ICMS da Operação = 12%

Valor do ICMS da Operação = 240

Percentual ICMS Diferido = 12%

Base Cálculo ICMS Diferido = 2000 / (1 - 0,12) = 2000 / 0,88 = 2272,73

Valor do ICMS da Operação = 2.272,73 \* (12 / 100) = 272,73

Valor ICMS Diferido = 272,73 \* (66,66 / 100) = 181,80

Fórmula do Valor ICMS Operação = Valor do produto com ICMS \* (Percentual ICMS / 100)

Fórmula do Valor ICMS Diferido = Valor do ICMS da Operação \* (Percentual ICMS Diferido / 100)

## Páginas relacionadas

* [F403FPR](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f403fpr.htm)
* [F403LFP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f403lfp.htm)
* [F403FSE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f403fse.htm)
* [F403LFS](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f403lfs.htm)
* [F075PPC](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075ppc.htm)
* [F075PCA](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075pca.htm)
* [F075PRO](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075pro.htm)
* [F075GFP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075gfp.htm)
* [F080SER](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f080ser.htm)
* [F080CSA](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f080csa.htm)
* [F001TCP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f001tcp.htm)
* [F001TVE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f001tve.htm)
* [VenProStr](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#VenProStr)
* [F085HCL](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f085hcl.htm)
* [COM-000ALSTR01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/com_000alstr01.htm)
* [F085CAD](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f085cad.htm)
* [F095CAD](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f095cad.htm)
* [F095HFO](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f095hfo.htm)
* [F001TCP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f001tcp.htm#menu_cadastros/f001tcp.htm)
* [Parâmetros da Filial para Vendas (F070FVE)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070fve.htm)
* [F460CTR](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f460ctr.htm)
* [F460PFO](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f460pfo.htm)
* [F410CEA](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f410cea.htm)
* [F410COS](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f410cos.htm)
* [F410PCT](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f410pct.htm)
* [F070EMP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070emp.htm)
* [F420OCC](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f420occ.htm)
* [F420OPS](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f420ops.htm)
* [F420GOC](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f420goc.htm)
* [F420OPE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f420ope.htm)
* [F420VAL](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f420val.htm)
* [F440GNE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f440gne.htm)
* [F440CNE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f440cne.htm)
* [F000INE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f000ine.htm)
* [F120GPB](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f120gpb.htm)
* [F120GPD](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f120gpd.htm)
* [F135FCA](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f135fca.htm)
* [F135FCP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f135fcp.htm)
* [F140PRE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f140pre.htm)
* [F140LOT](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f140lot.htm)
* [F140GNF](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f140gnf.htm)
* [F120CAP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f120cap.htm)
* [F120CAI](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f120cai.htm)
* [F120CAR](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f120car.htm)
* [F120CAC](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f120cac.htm)
* [F140CIP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f140cip.htm)
* [F140CNF](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f140cnf.htm)
