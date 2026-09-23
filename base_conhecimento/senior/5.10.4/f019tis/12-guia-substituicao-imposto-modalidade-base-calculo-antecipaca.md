# Guia Substituição Imposto / Modalidade Base Cálculo / Antecipação por estado

> **Fonte:** F019TIS - Tipos Substituições Impostos / Modalidade Base Cálculo / Antecipação - Por Estado — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f019tis.htm  
> **Trilha:** Ajuda por telas > Cadastros > Mercado e Suprimentos > Parâmetros Fiscais > Substituições Impostos/Modalidade Base Cálculo/Antecipação  
> **Telas citadas:** F009PPE, F019TIS, F019TST, F070FEF, F070PSE, F075GFP, F075PRO, F440RCI  
> **Identificadores de regras:** —

---
Regime Tributário

Este campo permite os valores:

* "0 - Todos";
* "1 - Simples Nacional";
* "3 - Regime Normal".

Para cada aplicação "A", "E" ou "S" do Estado será permitido informar um regime
tributário, permitindo informar até 2 regimes tributários ("1" ou "3") para cada
aplicação da substituição. Quando o regime tributário for "0 - Todos", será
impedida a utilização dos regimes tributários "1" e "3" para a aplicação do
Estado.

O cálculo das substituições irá considerar o regime tributário de cada
cliente e fornecedor. Se o cliente ou fornecedor for do tipo "1 - Simples
Nacional" ou "2 - Simples Nacional - excesso de sublimite de receita bruta",
serão filtradas as substituições que possuem o regime tributário "0 - Todos"
ou "1 - Simples Nacional", pois não é permitido cadastrar substituições para o estado com o regime
tributário igual a "2 - Simples Nacional - excesso de sublimite de receita
bruta".

Caso o cliente ou fornecedor possuir o regime tributário "0 - Todos" ou "3 - Regime Normal", serão filtradas as substituições que
contenham o regime tributário "0 - Todos" ou "3 - Regime Normal".

Aplic.Substituição

Permitirá os valores:

* "A - Ambas";
* "E - Entrada";
* "S - Saída".

Permitirá que sejam definidas as configurações de ST por entrada e saída dentro
do mesmo estado. O cálculo de substituição para as entradas e saídas passará a respeitar a
aplicação do código de ST.

Para as entradas, somente serão consideradas
substituições com aplicação "A - Ambas" ou "E - Entrada" e para as saídas
somente serão consideradas substituições com aplicação "A - Ambas" ou "S - Saída". Para o cálculo de substituição nas saídas, ainda será considerado o parâmetro
para calcular a ST mesmo quando ela já tenha sido calculada na entrada.

Tipo Desconto ICMS

Define o tipo de desconto que será aplicado sobre o valor do ICMS ST:

1. Não descontar ICMS;
2. Descontar ICMS Normal e Zona Franca;
3. Descontar ICMS Normal (sem FCP) e Zona Franca;
4. Descontar ICMS Normal aplicando redução BC ICMS ST. Ver fórmula.

Se a filial estiver configurada com os campos Código do Regime Tributário igual a "Simples Nacional" (tela Parâmetros da Filial para Tributos (F070FEF), guia Impostos 2) e Substituição Tributária igual a "S - Sim" (tela Parâmetros da Filial para Tributos (F070FEF), guia Impostos 1), o valor de ICMS a ser subtraído do ICMS ST será o calculado com base nos campos % ICMS Saída Contribuinte/% ICMS Saída Não Contribuinte, configurados na tela Parâmetros por Estado (F009PPE).

Observação

O valor "4 - Descontar ICMS Normal aplicando redução BC ICMS ST" somente estará disponível se o critério do cálculo de substituição for igual a "1 - Pela Margem de Lucro" ou "3 - Comparação da base calculada pela Margem e pelo Preço Unitário utilizando maior valor".

% Imposto

Indica a alíquota de ICMS.

% Imposto Não Cont.

Indica a alíquota de ICMS para não contribuintes. O percentual de ICMS deve considerar o percentual do imposto (cliente
contribuinte ou não) configurado no cadastro de modalidade de base de
cálculo.

% Redução

Percentual de redução da base de ICMS.

% Margem/Base

Percentual de margem de lucro para realizar o cálculo do ICMS ST atendendo o regime de estimativa simplificado para do imposto das operações internas. Quando existir margem informada para o respectivo estado, o cálculo do ICMS ST ocorre da seguinte forma:

* Valor total dos produtos - R$ 952,38;
* Valor de IPI - R$ 47,62;
* Valor total da operação - R$ 1.000,00;
* Alíquota interna de ICMS - 17%;
* Valor do ICMS - R$ 161,90 (952,38 \* 17%);
* Margem (MVA) - 38%;
* Valor agregado - R$ 380,00 (1000 \* 38%);
* Carga tributária média - 16%;
* Valor do ICMS ST - R$ 60,80 (380 \* 16%);
* Base de cálculo do ICMS ST - R$ 1.310,00 ([60,80 + 161,90] / 17%).

IPI Base

Indicativo se o IPI será considerado na base de cálculo.

Frete Base

Indicativo se o frete será considerado na base de cálculo.

Seguro Base

Indicativo se o seguro será considerado na base de cálculo.

Embal. Base

Indicativo se a embalagem será considerada na base de cálculo.

Encargo Base

Indicativo se o encargo será considerado na base de cálculo.

Outros Base

Indicativo se outros será considerado na base de cálculo.

Soma Docs

Tem a função de somar o valor do ICMS substituído, FCP retido a substituição tributária, Valor da substituição tributária do Pis e Valor da substituição tributária do Cofins ao valor do item do documento.

Texto NF

Neste campo pode ser digitado um texto para impressão em notas fiscais.

% Ret. ICMS

Este campo define o percentual que será retido no valor do Imposto Substituto.

## Exemplo

Considerando o valor do ICMS ST de R$ 100,00 e este campo configurado com o valor de 50%. O ICMS ST Retido será de R$ 50,00.

Importante

O título de ICMS ST é gerado com base no valor do ICMS ST Retido.

Gera Tit.Ret.NFE e Gera Tit.Ret.NFS

Indicativo se gerará o título de retenção de Imposto Substituto via NFE ou NFS respectivamente. Deve-se informar o valor "S - Sim" e os
parâmetros de "Fornecedor", "Transação", "Tipo de Título" e "Imposto para Vencimento", de
acordo com as configurações feitas para Imposto Substituto na tabela de parâmetros por
estado, em "Tabelas > Comercial > Fiscais > Parâmetros por Estado".

Desc. ZF Base Subst

Indicativo se o valor de desconto de zona franca deve ser subtraído da base
de Imposto Substituto. O procedimento padrão do sistema hoje é descontar, o valor
padrão será igual a "S - Sim".

Ind. MVA

Indicativo se considera a variação das alíquotas de ICMS no cálculo da
margem de lucro (MVA ajustada). Ao utilizar este indicativo como "Sim",
o sistema efetuará o ajuste da Margem de Valor Agregado (MVA) utilizando
a seguinte fórmula:

MVA ajustada = [(1+ MVA ST original) x (1 - ALQ inter) / (1- ALQ
intra)] -1, onde:

* "MVA ST original" é a margem de valor agregado cadastrada no código de
  Imposto Substituído (E019Sub.MarLuc);
* "ALQ inter" é a alíquota interestadual de ICMS aplicável à operação
  (E140Ipv.PerIcm);
* "ALQ intra" é a alíquota interna prevista para as operações
  substituídas na unidade federada de destino (E019Sub.IcmEst).

## Exemplo

MVA Original: 43,83%  
Alíquota Interestadual: 12,00%  
Alíquota Interna: 17,00%  
Valor Bruto do Item na Nota: R$100,00  
Valor ICMS Normal: R$12,00   
Base da ST: R$143,83   
Valor da ST: R$12,45

Ao ativar o indicativo de MVA ajustada:  
MVA Original: 43,83%  
Alíquota Interestadual: 12,00%  
Alíquota Interna: 17,00%  
Valor Bruto do Item na Nota: R$100,00  
Valor ICMS Normal: R$12,00   
Base da ST: R$152,49 (MVA Ajustada: 52,49%)  
Valor da ST: R$13,92

Formação Base

Indicativo se o valor dos descontos devem ser
considerados na formação do cálculo do Imposto Substituição Tributária.  
Quando o campo Formação Base estiver parametrizado como:

* "L - Valor líquido aquisição", o cálculo do ICMS ST utiliza como base padrão o valor líquido da última nota fiscal de entrada para o produto, adquirido pela filial;
* "B - Bruto", o cálculo do ICMS ST utiliza como base padrão o valor bruto;
* "D - Bruto menos descontos", o cálculo do ICMS ST utiliza como base padrão o valor bruto subtraído com os descontos.

A opção "L - Valor líquido aquisição" funciona apenas para o cálculo da base de ICMS ST com os critérios 1 (Pela Margem de Lucro) e 3 (Comparação da Base calculada pela Margem e pelo Preço Unitário utilizando maior valor).

As opções "B - Bruto" ou "D - Bruto menos descontos" devem ser usadas para a formação da base de cálculo de produtos produzidos, visto não haver a compra de produtos.

Cal.ST Saída com ST Entrada

Indicará se as saídas deverão calcular ST mesmo quando já houve o cálculo
na entrada. Esse parâmetro afetará somente as substituições configuradas com aplicação
"A" (Ambas) ou "S" (Saídas).

Mensagem, Mensagem 2, Mensagem 3 e Mensagem 4

Campos para a definição do código de uma mensagem pré-cadastrada no
sistema para impressão em notas fiscais.

ICMS ST despesa acessória Dev.

Indicativo
se o ICMS ST (valor, base e código) possa ser zerado em uma nota fiscal
de saída de devolução e somado ao valor de outras despesas.

Valor ICMS Normal

Indicativo se o valor do ICMS será considerado no valor base do Imposto Substituído.

Vlr. imp. importação

Indicativo se o valor do imposto de importação será considerado no valor base do Imposto Substituído.

Vlr. seg. importação

Indicativo se o valor do seguro de importação será considerado no valor base do Imposto Substituído.

Vlr. fre. importação

Indicativo se o valor do frete de importação será considerado no valor base do Imposto Substituído.

Vlr. desp. importação

Indicativo se o valor de outras despesas de importação será considerado no valor base do Imposto Substituído.

Vlr. PIS Fat.

Indicativo se o valor do PIS Faturamento será considerado no valor base do Imposto Substituído.

Vlr. COFINS Fat.

Indicativo se o valor do COFINS Faturamento será considerado no valor base do Imposto Substituído.

Vlr. PIS Imp.

Indicativo se o valor do PIS Importação será considerado no valor base do Imposto Substituído.

Vlr. COFINS Imp.

Indicativo se o valor do COFINS Importação será considerado no valor base do Imposto Substituído.

ICMS Efe. Cred.

Neste campo é possível configurar qual valor será utilizado como base para o valor do ICMS Efetivamente Creditado na apuração do Imposto ICMS (tipo 2). Ele pode ser preenchido com as seguintes opções:

* Sempre: o valor da base do ICMS que está na nota fiscal será considerado como situação de efetivamente creditado. Esta opção é o comportamento atual e padrão do sistema quando não há preenchimento para o campo;
* Maior: o sistema irá calcular a base do ICMS como se não houvesse a modalidade do ICMS (Cálculo por operação) e comparar esta base de cálculo com a do ICMS que está no documento fiscal. Será considerado como base de cálculo do ICMS Efetivamente Creditado o maior valor nesta comparação. O percentual de ICMS Efetivamente Creditado será o que está na nota fiscal e o valor será recalculado conforme a base de cálculo e o percentual;
* Menor: o sistema irá calcular a base do ICMS como se não houvesse a modalidade do ICMS (Cálculo por operação) e comparar esta base de cálculo com a do ICMS que está no documento fiscal. Será considerado como base de cálculo do ICMS Efetivamente Creditado o menor valor nesta comparação. O percentual do ICMS Efetivamente Creditado será o que está na nota fiscal e o valor será recalculado conforme a base de cálculo e o percentual.

Observação

Para utilizar essa funcionalidade é necessário que o campo Código da Modalidade ICMS, no Cadastro de Produtos (F075PRO), esteja preenchido. Esta funcionalidade não será levada em conta, quando os valores do ICMS que estão na nota fiscal forem alterados manualmente. Neste caso o ICMS efetivamente creditado deve receber os mesmos valores.

## Exemplo 1

|Validades||Situação|

01/08/2011.A – Ativo

05/08/2011.A – Ativo

Nota fiscal emitida em 03/08/2011, buscará definições da validade
"01/08/2011", pois trata-se da maior data de início de validade de
substituição que seja menor que a data de emissão do documento;

Nota fiscal emitida em 06/08/2011, buscará definições da validade
"05/08/2011".

## Exemplo 2

|Validades||Situação|

01/08/2011.  A – Ativo

05/08/2011.  I - inativo

Nota fiscal emitida em 06/08/2011, buscará definições da validade
"01/08/2011", pois a validade 05/08/2011 está inativa.

Exemplo com valores:

Validade: 01/08/2011

Situação: A - Ativo

|UF||% Imposto||% Margem/Base|

SC..17%........35%...........

RS..12%........20%...........

------------------------------

Exemplo NF 1, emitida em 01/08/2011:

UF Cliente : SC

Valor NF : 100,00

ICMS ST : 17%

% Margem/Base : 35%

Base ST : 100,00 + 35% = R$ 135,00

Valor ST : 135,00 \* 17% = R$ 22,95

-----------------------------------------

Exemplo NF 2, emitida em 02/08/2011:

UF Cliente : RS

Valor NF : 104,00

ICMS ST : 12%

% Margem/Base : 20%

Base ST : 104,00 + 20% = R$ 124,80

Valor ST : 124,80 \* 12% = R$ 14,98

Validade: 05/08/2011

Situação: A - Ativo

|UF||% Imposto||% Margem/Base|

SC..10%........30%...........

RS..20%........25%...........

------------------------------

Exemplo NF 3, emitida em 06/08/2011:

UF Cliente : RS

Valor NF : 100,00

ICMS ST : 10%

% Margem/Base : 30%

Base ST : 100,00 + 30% = R$ 130,00

Valor ST : 130,00 \* 10% = R$ 13,00

-----------------------------------------

Exemplo NF 3, emitida em 06/08/2011:

UF Cliente : RS

Valor NF : 104,00

ICMS ST : 20%

% Margem/Base : 25%

Base ST : 104,00 + 25% = R$ 130,00

Valor ST : 130,00 \* 20% = R$ 26,00

 Se neste caso a validade "05/08/2011" estivesse inativo, os
percentuais da validade "01/08/2011" seriam aplicados.

Observações

* O valor do **ICMS ST** 
  é subtraído ou não do valor do movimento de estoque conforme
  parâmetro **Recupera ICMS = S/N**. Não há parâmetro
  específico para ICMS ST;
* O botão **Processar** somente vai gerar os estados na guia caso a coluna "%Imposto" esteja informado algum valor maior que zero.

**Vlr. AFRMM na Base**

Indicativo se o valor AFRMM está na base do Imposto Subtituição.

Busca ICMS ST Ent.

Indicativo se controla a substituição tributária da saída, conforme a entrada do produto de uma nota fiscal de entrada. Caso este campo esteja parametrizado como "S - Herdar base e valor proporcionalmente na venda", o sistema busca os valores do imposto na entrada e coloca na saída no momento da venda.

Caso esteja parametrizado como "M - Recalcular na venda a base de cálculo considerando MVA da entrada", o sistema faz a herança da alíquota de ICMS ST e do percentual de MVA da nota de entrada, utilizando o método PEPS (Primeiro que Entra, Primeiro que Sai) para formar a nova base de cálculo de ICMS ST.

Caso haja mais de um registro de entrada com diferentes percentuais de MVA disponíveis para faturamento, e a quantidade a faturar seja maior que a do primeiro registro disponível, será apresentada uma mensagem bloqueando a operação e sugerindo que as quantidades sejam separadas em um ou mais itens.

Quando este campo está parametrizado como "S - Herdar base e valor proporcionalmente na venda" ou "M - Recalcular na venda a base de cálculo considerando MVA da entrada", o sistema consiste as entradas verificando se existe saldo para atender a quantidade a faturar. Ou seja, o sistema acata um código de ICMS ST proveniente do documento de saída e tenta consumir as quantidades de estoque disponíveis. Caso não tenha o suficiente para atender, o sistema emitirá mensagem de erro.

## Exemplo:

Na tela Manutenção de Controle de Entrada de Produtos (F440RCI), há duas Notas Fiscais de Entrada com Controle:

1. Uma Nota Fiscal de Entrada tem 4 quantidades em estoque disponível do imposto com código ABC;
2. A outra Nota Fiscal de Entrada tem 16 quantidades em estoque disponível do imposto com código DEF.

Caso o usuário do sistema esteja gerando uma saída (pré-fatura ou nota fiscal) com 18 quantidades a faturar, ocorrerá que o sistema não conseguirá utilizar as 16 quantidades de estoque de uma nota fiscal de entrada, e depois consumir 2 quantidades de estoque da outra nota fiscal de entrada. Nesse caso, ocorrerá uma mensagem de erro sobre as quantidades. Essa restrição existe, uma vez que não é permitido o consumo de estoque de impostos com códigos diferentes quando o parâmetro está como "S - Herdar base e valor proporcionalmente na venda" ou "M - Recalcular na venda a base de cálculo considerando MVA da entrada". Em uma analogia simplória, não é permitido misturar impostos laranja com bananas.

Caso este parâmetro esteja marcado como "N - Não Herdar", o sistema consome as entradas até atingir a quantidade a faturar, independente do código do ICMS ST, atendendo toda a quantidade a faturar e sem emitir o erro.

Caso não deseje consistir o saldo do ICMS ST específico da saída, permitindo que o sistema consuma o saldo de outros ICMS ST, pode-se configurar o campo Busca ICMS ST Ent. da tela Tipos Substituições Impostos / Modalidade Base Cálculo / Antecipação - Por Estado (F019TIS) como "N - Não Herdar".

Importante

Vale lembrar que essa é uma decisão de negócio que deve ser validada pela equipe contábil responsável pelo seu processo.

Nota

Não há mais o bloqueio que impedia o processamento, quando não há saldo de entrada suficiente para atender a quantidade faturada. Devido a isso, caso haja um único percentual de MVA de entrada disponível, e o valor a faturar for maior, não será apresentado nenhum bloqueio.

Gera guia FCP ICMS ST

Indica se deve gerar a guia de FCP separadamente da guia do ICMS ST.

* A guia é gerada de acordo com o valor da alíquota parametrizado na tela F070PSE referente aos Parâmetros Fiscais de produtos e serviços por filial e estado.

DIFAL como ICMS ST

Indica se o DIFAL deve ser calculado como ICMS ST para operações de Consumo Próprio ou Imobilizado. Com esse campo como **S** e a aplicação da operação da transação igual a **S-Consumo Próprio** ou **I-Imobilizado**, o sistema calcula o DIFAL como ICMS ST. No caso de uma dessas variáveis estar negativa, o sistema calcula o ICMS ST normalmente.

Tip. Cal. DIFAL

Tipo da base de cálculo do diferencial de alíquota do ICMS.

## Simples

Considerando o seguinte cenário:

Vlr item: 258,40  
% IPI: 25,84 (10% do item)  
Base ICMS: 284,24 IPI considerado na base do ICMS  
% ICMS da ST no estado do cliente: 20% (cadastrado nas telas F019TIS ou F070PSE)  
% ICMS: 2% (cadastrado como Percentual de ICMS Normal ou alíquota interestadual na tela F009PPE)

Teremos o cálculo:   
BASE ST -> 284,24   
VLR ICMS ST -> 284,24 \* (20% - 2%) = 51,16

**Observação**

O campo Tipo Desconto ICMS influencia no Valor do ICMS ST.

## Dupla - Dif. Valor

Considerando o seguinte cenário:

Vlr item: 258,40  
VLR IPI: 25,84 (corresponde a 10% do item)  
Base ICMS: 284,24 (IPI considerado na base do ICMS)  
VLR ICMS: 34,11 (corresponde a 12% em cima do item + IPI)  
% ICMS da ST no estado do cliente: 18% (ambos cadastrados na F070PSE)  
% FCP da ST no estado do cliente: 2% (ambos cadastrados na F070PSE)

Teremos o cálculo:  
BASE ST -> (284,24 - 34,11)/(100% - (18%+2%)) = 312,66  
VLR ICMS ST antes da dedução do ICMS próprio -> 312,66 \* (18%) = 56,28  
VLR ICMS ST -> 56,28 - 34,11 = 22,17

Nota

O parâmetro Ind.MVA modifica a forma de cálculo do Difal como ICMS ST. Para atender a fórmula de cálculo Base Simples e Base Dupla, o parâmetro deve estar sempre como "N - Não", quando não houver Margem de Valor Agregado.

Desc. ICMS Inter. base DIFAL

Indicativo se deve descontar o ICMS da operação interestadual na formação da base de cálculo do DIFAL. Habilitado somente se o campo Tipo Cálculo DIFAL for **1-Dupla Dif. Alíquota**, **3-Dupla Dif. Valor** ou **4-Dupla Dif. Valor por Regime Fornecedor**.

Alíq. Base de Cálculo DIFAL

Indicativo de qual alíquota deve ser aplicada na formação da base de cálculo do DIFAL. Habilitado somente se o campo Tipo Cálculo DIFAL for **1-Dupla Dif. Alíquota**, **3-Dupla Dif. Valor** ou **4-Dupla Dif. Valor por Regime Fornecedor**.

Desc. ICMS Base

Indica se o ICMS é descontado da base de cálculo.

ICMS ST esc. não rel

Indica se o cálculo do ICMS ST deve ser realizado para produtos com produção em escala não relevante. Desta forma, quando o campo Produção em Escala Relevante, das telas de Cadastro de Produto Individual (F075PRO) ou Cadastro de Produto Agrupado (F075GFP), estiver definido como **N - Produzido em Escala Não Relevante**, e esse parâmetro for configurado como **S - Sim**, o ICMS ST será calculado.

Importante

Quando a derivação do produto estiver configurada como **N - Produzido em Escala Não Relevante**, por padrão, não será realizado o cálculo do ICMS ST.

**Red. DIFAL após ICMS**

Este parâmetro pode ser habilitado quando a substituição for **DIFAL como ICMS ST** igual a **S-Sim** e o **Tip. Cal. DIFAL** for **3-Dupla Dif. Valor**, para que a Redução do DIFAL seja aplicada apenas após o cálculo do ICMS por dentro do estado de destino.

**Descontar ICMS da base FCP ST em op. interna** 

Este campo define se a forma de cálculo do valor de base de FCP ST em documentos fiscais de entrada ou documentos fiscais de saída em operações internas (mesmo estado) deve ser calculado, conforme a fórmula:

Valor Base FCP ST = Valor Base FCP - Valor Base ICMS Operação.

O valor padrão do parâmetro será "N - Não" para que seja mantido o cálculo atual e nos estados nos quais o cálculo deve ser efetuado conforme fórmula descrita, o valor deve ser alterado para "S - Sim".

% Carga Trib. Média FCP ST

Este campo permite que se realize o cálculo do FCP pela carga média. Para que seja possível alterá-lo, é necessário que o campo Critério Cálculo Substituição da tela F019TST esteja parametrizado com valor "4 - Pela carga tributária média".

Quando informado o percentual no campo % Carga Trib. Média FCP ST, o cálculo do Valor FCP ST e Base FCP ST em documentos fiscais de entrada e saída serão calculados da seguinte maneira:

* Para Operações interestaduais:  
  Valor FCP ST = Valor Total da Operação \* % Carga Tributária Média para FCP ST  
  Valor Base FCP ST = (Valor FCP ST) / %FCP
* Para Operações internas:  
  Valor FCP ST = Valor Agregado \* % Carga Tributária Média para FCP ST  
  Valor Base FCP ST = (Valor FCP ST + Valor FCP) / %FCP

O percentual de Carga tributária média FCP ST utilizado no cálculo deve ser configurado nesta tela.

Se não existir porcentagem de MVA (campo Ind. MVA) configurada, a operação interna acontecerá da mesma forma como ocorre a operação interestadual.

**Motivo da Desoneração do ICMS-ST**

Permite que seja possível informar o motivo da desoneração do ICMS-ST. Para os motivos "3 - Produtor agropecuário", "9 - Outros" ou "12 - Órgão de fomento e desenvolvimento agropecuário", será calculado o Valor do ICMS-ST desonerado do item com o respectivo código do ICMS substituído (CodTst), substituindo o valor do ICMS-ST no documento.

Desc. PIS Ret.

Indica se o PIS Retido é descontado do valor da base de ICMS ST.

Desc. COFINS Ret.

Indica se o COFINS Retido é descontado do valor da base de ICMS ST.

### Botões

Aplicar

Este botão possui as seguintes funcionalidade de aplicação:

* "Para os Estados": Aplica o(s) valor(es) alterados para todos os estados da validade selecionada que constam nessa guia;

* "Para todas as Validades: Aplicar o(s) valor(es) alterados para todos os estados de todas as validades que constam na guia Validades Substituições Impostos / Modalidade Base Cálculo.

## Páginas relacionadas

* [Parâmetros da Filial para Tributos (F070FEF)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070fef.htm)
* [Parâmetros por Estado (F009PPE)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f009ppe.htm)
* [F075PRO](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075pro.htm)
* [F440RCI](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f440rci.htm)
* [F070PSE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070pse.htm)
* [F075GFP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075gfp.htm)
* [F019TST](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f019tst.htm)
