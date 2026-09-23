# Impostos 2

> **Fonte:** F070FEF - Parâmetros da Filial para Tributos — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070fef.htm  
> **Trilha:** Ajuda por telas > Cadastros > Filiais > Parâmetros por Gestão  
> **Telas citadas:** E070FEF, E140IDE, E661UCR, E900SOP, F001TIT, F049DEC, F049TTR, F051DIS, F055PPF, F055TPR, F070AFI, F070EMP, F070FCA, F445PRC, F660CCI, F660CMO, F660INF, F660INT, F660ISP, F660NCI, F661RST, F661UCR, F669SPC, F690ILA  
> **Identificadores de regras:** —

---
Adicionar Diferencial de Alíquota ao CIAP

Informar se deve ou não adicionar o valor do diferencial de alíquota das notas
fiscais na rotina do CIAP.

Credita CIAP na Apuração do ICMS

Informar se deve ou não creditar o valor do CIAP na apuração do imposto do tipo
02 - ICMS.

Arredondamento CIAP

Tem por finalidade permitir que o usuário selecione o tipo de arredondamento que deve ser utilizado no momento da geração das parcelas do CIAP. Possui duas opções: 1 - Arredonda e 2 - Trunca, sendo a primeira a opção padrão.

Considera NF Entrada de Serviço

Indicativo se considera ou não notas fiscais de entrada de serviços nas
apurações dos impostos dos tipos:  01 - IPI e 02 - ICMS, nos livros
fiscais e arquivos magnéticos.

* Exemplo do
  tratamento das notas fiscais de serviços (Entrada e Saídas) no sistema.

Data Cálculo PIS Financeiro

Data do último cálculo do imposto do tipo 20 - PIS - Não Cumulativo, ou seja,
ao processar a apuração do cálculo é atualizado este campo com a data final da
apuração.

Data Cálculo PIS Patrimônio

Data do último cálculo do imposto do tipo 20 - PIS - Não Cumulativo ou 41 - PIS - Não cumulativo, ou seja, ao processar ou estornar a apuração do cálculo é atualizado este campo com a data final da apuração ou último cálculo efetuado.

Data Cálculo COFINS Financeiro

Data do último cálculo do imposto do tipo 21 - COFINS - Não Cumulativo, ou
seja, ao processar a apuração do cálculo é atualizado este campo com a data
final da apuração.

Data Cálculo COFINS Patrimônio

Data do último cálculo do imposto do tipo 21 - COFINS - Não Cumulativo ou 42 - COFINS - Não cumulativo, ou seja, ao processar ou estornar a apuração do cálculo é atualizado este campo com a data final da apuração ou último cálculo efetuado.

Data de Geração da TARE (DF)

Ao efetuar a geração da TARE (DF), este campo é atualizado com data final de sua
geração.

Hora de Geração da TARE (DF)

Ao efetuar a geração da TARE (DF), este campo é atualizado com hora de sua
geração.

Controla Numeração

Informar neste campo se deseja ou não que o sistema controle a numeração das
notas fiscais de saídas, este parâmetro serve somente para o módulo de impostos.
A numeração é meramente sugestiva, podendo ser alterada.

Informa Itens 

Informar neste campo se deseja ou não que ao digitar notas fiscais no módulo de
Impostos, se possível informar Itens para as notas fiscais de entradas como
para as notas fiscais de saídas.  
Com isso, ao digitar os dados gerais a tela posicionará na página Itens. Caso
não seja informado o item, apresentará mensagem para confirmar a não inserção do
item na nota.

Filial Totalizadora 

Indicativo se a filial é Totalizadora, Consolidadora ou Normal dos cálculos e
apurações dos impostos. Com a opção N (Normal) a filial é independente, podendo apurar somente as
suas próprias movimentações.

## Opções

Com a opção S (Totalizadora) indica para o sistema que a filial é totalizadora de cálculos e apurações de impostos. O sistema permite que se tenha apenas uma filial totalizadora, além de não permitir que a filial totalizadora possua movimento próprio (por exemplo, Notas Fiscais, CIAP etc.).

A rotina de cálculo da filial totalizadora irá totalizar apenas as filiais que possuem cálculo para o período selecionado, caso a mesma não tenha cálculo, ela não será incluída no cálculo da filial totalizadora. O campo Saldo Período Anterior irá totalizar o saldo individual das filiais que estão parametrizadas com a opção N - Normal. Este campo somente poderá ser alterado quando seu valor estiver igual à 0.

Com a opção C - Consolidadora, tem por finalidade totalizar as informações de todas as demais filiais. Para fins de cálculo dos impostos do tipo 1- IPI (Imposto sobre Produto Industrializado), 2 ICMS (Imposto sobre Circulação de Mercadorias e Serviços), 6 - Outros (Base Faturamento), 12-Simples, 30- Super Simples e 98– Contábil, a filial Consolidadora têm o mesmo comportamento da filial totalizadora, ou seja, não permite movimentação alguma na filial Consolidadora, contudo ao calcular os impostos acima, o sistema passa a não mais totalizar os valores dos impostos das filiais, mas sim efetuar a consolidação das bases de cálculo, aplicando a tabela de tributação para a faixa de valores consolidada e calculando o valor do imposto a pagar (ao invés de simplesmente somar os valores a pagar para as demais filiais como é feito na filial totalizadora).

O campo Saldo Período Anterior, faz a busca dos saldo nela mesmo, ou seja, busca o saldo do período anterior na filial parametrizada com a opção C – Consolidadora de apurações. Não é possível alterar o valor do campo quando não encontrar apuração do período anterior, ou seja, é a primeira apuração do imposto no período para esta filial.

Com a opção M (Consolidadora de movimentos) selecionada. poderá ser feita a consolidação de todos os movimentos das filiais que possuírem no campo **Filial Consolidadora**, o código da filial consolidadora de movimentos desta mesma tela. Com isso, serão duplicadas todas as movimentações das outras filiais que apontam para a filial consolidadora de movimentos, e com isso será necessário apurar os impostos apenas da filial consolidadora.

**Exemplo:** fazendeiros que possuem várias fazendas, onde cada fazenda é uma filial para controle individual, porém ante o fisco é um único CNPJ.

Observação

Esse campo não atende o cálculo do imposto 49 - Contribuição Previdenciária sobre Receita Bruta nas opções "S - Totalizadora" e "C - Consolidadora".

Valor Mínimo p/ Retenção do PIS

Informar neste campo o valor mínimo para as retenções do PIS.

Valor Mínimo p/ Retenção do Cofins

Informar neste campo o valor mínimo para as retenções do COFINS.

Valor Mínimo p/ Retenção da CSLL

Informar neste campo o valor mínimo para as retenções da CSLL.

Valor Mínino p/ Retenção de Outras Retenções

Informar neste campo o valor mínimo para as retenções de Outras Retenções.

Controle diário de retenções das contrib. sociais

Indicativo se a retenção das contribuições sociais (PIS, COFINS e CSLL) é cumulativa e diária.

Valor mínimo p/ retenção das contrib. sociais

Valor mínimo para considerar a retenção das contribuições sociais. Este campo é habilitado apenas quando o campo Controle diário de retenções das contrib. sociais estiver parametrizado como S - Sim.

Controle Individual na retenção das contrib. sociais

Indica se o controle de retenção das contribuições sociais (PIS, Cofins e CSLL) será individual (por imposto) ou agrupado. As opções para este campo são S - Sim e N - Não (valor padrão).

Controle diário de retenção IRRF

Indica se a filial controla o cálculo do IRRF diariamente.

Valor mínimo p/ retenção de IRRF

Informar o valor mínimo do IRRF controlado diariamente. Esse campo só fica habilitado quando a opção Controle diário de retenção IRRF estiver com a opção SIM selecionada.

Código Moeda CIAP

Informar o código da moeda ou índice utilizado na rotina do CIAP, para correção
do CIAP.

Base Cálc. Bem p/ Créd. PIS 

Indicativo de como a base de cálculo do bem para crédito do PIS será gerada na
inclusão de bens via NF de Entrada:

* Com a opção C (valor do custo do bem [Vlr. Total da Nota - Impostos recuperáveis]);
* Com a opção A (valor da aquisição do bem):
  + Vlr. Total da Nota - Vlr. IPI: o valor de aquisição para crédito do imposto será dividido pela quantidade de meses. O campo Quantidade Meses Inicial PIS/COFINS/CSLL indica a quantidade de meses inicial que foi calculada em outro sistema ou bem origem

Base Cálc. Bem p/ Créd. COFINS 

Indicativo de como a base de cálculo do bem para crédito da COFINS será gerada
na inclusão de bens via NF de Entrada:

* Com a opção C (valor do custo do bem [Vlr. Total da Nota - Impostos recuperáveis]);
* Com a opção A (valor da aquisição do bem):
  + Vlr. Total da Nota - Vlr. IPI: o valor de aquisição para crédito do imposto será dividido pela quantidade de meses. O campo Quantidade Meses Inicial PIS/COFINS/CSLL indica a quantidade de meses inicial que foi calculada em outro sistema ou bem origem

Base Cálc. Bem p/ Créd. CSLL 

Indicativo de como a base de cálculo do bem para crédito do CSLL será gerada na
inclusão de bens via NF de Entrada:

* Com a opção C (valor do custo do bem [Vlr. Total da Nota - Impostos recuperáveis]);
* Com a opção A (valor da aquisição do bem):
  + A (valor da aquisição do bem [Valor da Nota - IPI])

Somar Diferencial de Alíquota na Apuração do ICMS 

Este campo tem por finalidade indicar se o valor referente ao Diferencial de
Alíquota deve ser considerado juntamente com os débitos na apuração do imposto
do tipo 2 - ICMS ou não.

* Quando estiver com a opção N (Nunca), na apuração do imposto do tipo 02 (ICMS)
  o valor do diferencial de alíquota será gerado no campo Dif. Alíquota Inter.;
* Quando estiver com a opção S (Sempre), na apuração do imposto do tipo
  02 (ICMS) o valor do diferencial de alíquota será gerado no campo Outros
  Débitos;
* Quando estiver com a opção C (ICMS maior que Dif. Alíquota),
  na apuração do imposto do tipo 02 (ICMS) o valor do diferencial de alíquota
  será gerado no campo Outros Débitos quando o valor do saldo credor for maior
  ou igual ao valor do diferencial alíquota, caso o saldo credor for menor que o
  valor do diferencial de alíquota, o valor do diferencial de alíquota será gerado
  no campo Dif. Alíquota Inter;
* Quando estiver com a opção D (ICMS destacado na nota fiscal e ICMS calculado interno) habilitará o parâmetro
  para gerar nos campos de outros créditos ou outros débitos da tela
  F661I18, os valores relativos ao Diferencial de Alíquota, ICMS Destacado e ICMS Interno das notas fiscais de entrada (tributos) e ICMS destacado (compras/vendas) para o estado de São Paulo.

Rateio NF Impostos

Informar umas das opções:  
N  - Nenhum, E -
Entrada, S - Saída, Z - Redução Z, W - Entrada e Saída, X - Entrada e Redução Z, Y - Saída e Redução Z e A - Todos.  
Neste campo deve ser definido se a filial informada possuirá rateios na
gestão de Tributos ou não.

* Para a opção N - Nenhum, a filial não possuirá rateios;
* Para a opção E - Entrada, a filial somente possuirá rateios para as notas
  fiscais de entradas;
* Para a opção S - Saída, a filial somente possuirá rateios para as notas
  fiscais de saídas;
* Para a opção Z - Redução Z, a filial somente possuíra rateios para as reduções Z;
* Para a opção W - Entrada e Saída, a filial possuíra rateios para as notas fiscais de entradas e saídas;
* Para a opção X - Entrada e Redução Z, a filial possuíra rateios para as notas fiscais de entradas e reduções Z;
* Para a opção Y - Saída e Redução Z a filial possuíra rateios para as notas fiscais e reduções Z;
* Para a opção A - Todos, a filial possuirá rateios para as notas fiscais de
  entradas, saídas e reduções Z.

Transação Inversa ao Movimento

Este campo tem por finalidade inverter as transações na nota fiscal. Quando a nota fiscal pertencer a vendas, poderá ser escolhido uma transação de
compra e vice versa.

Credita CIAP Apuração Impostos Outros Base Fat.

Quando informado a opção
S (Sim), neste campo, no imposto do tipo 6 (Outros (Base Faturamento)), na grade estará visível o campo Vlr.CIAP.

Data Inscrição Estadual

Informar a data da Inscrição Estadual, esta data é utilizada para o cálculo do Imposto tipo 30 (Super Simples)
somente será gerado o cálculo caso compreenda esta data.

Código de Regime Tributário

Informar um item da lista:
1 - Simples Nacional;
2 - Simples Nacional - excesso de sublimite de receita bruta;
3 - Regime Normal.

Forma de Tributação Simples Nacional

Informe neste campo se a forma de tributação do Simples Nacional é por regime de competência ou regime de caixa: 1 - Regime de Competência - Entrada; 2 - Regime de Competência - Execução Serviço; 3 - Regime de Caixa.  
Caso não seja feita a apuração do faturamento, este pode ser informado manualmente na tela Informações mensais (F660INF). Nessa tela, utilize a opção Ajuda, conforme indicado na mensagem apresentada pelo sistema: "Na edição ou inserção de um registro com o tipo de imposto Simples Nacional, o sistema irá cadastrar automaticamente um registro na tabela de percentuais do Simples Nacional. O percentual atribuído será buscado na tabela de tributação (tela F049TTR) considerando o campo % ICMS do registro que possuir a mesma empresa, imposto, competência, grupo fiscal e sequência informados nessa tela, F660INF."

Incentivador Cultural

Informar se "S - Sim" ou "N - Não".

Regime Especial de Tributação

1. Microempresa municipal,
2. Estimativa,
3. Sociedade de profissionais,
4. Cooperativa,
5. Microempresário Individual (MEI),
6. Microempresário e Empresa de Pequeno Porte (ME EPP) - Campo Opcional.

Gerar
SPED Contribuições

Este campo indica se os movimentos da
filial serão considerados para a apresentação do SPED Contribuições. Ele possui as seguintes opções e funcionalidades:

* "N - Não": indica que a
  filial não gera o SPED Contribuições;
* "S - Total": indica que a filial gera o SPED
  Contribuições de forma total;
* "C - Não Consolidado": indica que a filial possui
  apenas movimentação patrimonial, gerando
  somente o Bloco F (Demais Documentos e Operações) do
  SPED Contribuições.

## Exemplo

| Código Filial | Matriz | CNPJ | Filial Consolidadora | Gerar SPED Contribuições |
| --- | --- | --- | --- | --- |
| 1 | Sim | 11111111000111 | N - Normal | S - Total |
| 2 | Não | 22222222000122 | N - Normal | C - Não consolidado |
| 3 | Não | 22222222000122 | N - Normal | C - Não consolidado |
| 4 | Não | 22222222000122 | N - Normal | C - Não consolidado |
| 99 | Não | 22222222000122 | M - Consolidadora de Movimentos | S - Total |

Com esta parametrização, as movimentações das filiais 2, 3 e 4 são integradas (consolidadas) para a filial 99. A filial 99 não faz nenhuma apuração patrimonial (sem gerar bens e cálculos), sendo os bens e cálculos patrimoniais feitos nas filiais 2, 3 e 4.

Na geração do SPED Contribuições, ele reconhece os bens e cálculos (depreciação e amortização) das filiais 2, 3 e 4, associando-os à filial 99.

Ver também Funcionalidade do campo Agrupamento de filiais para a geração do SPED Contribuições.

Gerar SPED ECF

Indica se a filial gera informações para o SPED ECF. A apuração do IRPJ/CSLL (53/54/55/56) e geração do SPED ECF são por empresa. Esse parâmetro possui o objetivo de indicar se a filial gera informações para o SPED ECF e apura os impostos 53/54 – IRPJ/CSLL Lucro Presumido (SPED) ou 55/56 – IRPJ/CSLL Lucro Real (SPED).

Regime Especial Rendex

Preencher com o código do regime do Redex  

CIAP de Componentes na Conclusão do Bem Principal  
Quando este campo estiver com S (Sim), o botão Componentes ficará visível na tela
F660NCI onde será possível
consultar os componentes do período.  

Utiliza Crédito Período  
Quando este campo estiver com S (Sim), na apuração dos impostos do tipo
41 e 42 serão utilizados primeiro os créditos da apuração e, se necessário,
os créditos de períodos anteriores.  
Quando o campo estiver preenchido com N (Não), na apuração serão utilizados
primeiro os créditos mais antigos e se necessário o crédito do período de
apuração.

Utiliza Retenção Período

Quando este campo estiver com S (Sim), na apuração dos impostos do tipo
41, 42, 43 e 44 serão utilizados primeiro os créditos da apuração e, se necessário,
os créditos de períodos anteriores. Quando o campo estiver preenchido com N (Não), na apuração serão utilizados
primeiro os créditos mais antigos e se necessário o crédito do período de
apuração.

Observação

Os campos Utiliza Crédito Período e Utiliza Retenção Período estarão habilitados somente quando o campo Filial Matriz (F070FCA) estiver parametrizado como S - Sim ou a filial está definida como Filial Matriz no Agrupamento de Filiais(F070AFI).

Calcular PIS/COFINS/CSLL/IRPJ Financeiro

Indica o tipo de cálculo do imposto PIS/Cofins/CSLL/IRPJ na Gestão de Tributos,
caso seja informado:

1. Regime Competência - Os impostos 20 e 21 serão os responsáveis por calcular
   o PIS/COFINS na Gestão de Tributos.
2. Regime Competência - Os impostos 41 e 42 serão os responsáveis por calcular
   o PIS/COFINS na Gestão de Tributos. Os impostos 53, 54, 55 e 56 serão responsáveis por calcular o IRPJ/CSLL Lucro Presumido e IRPJ/CSLL Lucro Real por regime de competência.
3. Regime Caixa - Os impostos 47 e 48 serão os responsáveis por calcular
   o PIS/COFINS na Gestão de Tributos. Os impostos 53 e 54 serão responsáveis por calcular o IRPJ/CSLL Lucro Presumido por regime de caixa.  
   Caso seja selecionado um tipo diferente do informado na tela, uma
   mensagem de advertência será gerada ao apurar o cálculo dos impostos e os
   valores gravados anteriormente serão preservados.

Filial Controla Diferido

Define se a filial irá controla os valores do imposto
diferido.

CNPJ/CPF da SCP

CNPJ ou CPF da Sociedade em Conta de Participação. A filial será considerada como SCP, na apuração dos impostos de
PIS e COFINS (SPED Contribuições), se este campo estiver
preenchido. Esta filial NÃO deve ter a indicação de gerar SPED
Contribuições.

Considerar Data Autorização NFS-e

Este campo
virá com sugestão de preenchimento igual a N (Não). Se for
preenchido com S (SIM) haverá as seguintes alterações:

* Na integração de notas fiscais, tela F660INT, os campos DatEmi
  e DatSai serão preenchidos com a data de autorização da NFS-e
  (E140IDE.DATAUT).
* Salva a exceção: Se a data de saída (DatSai)
  for maior que a data de autorização (DATAUT) o campo DatSai
  não é alterado.
* Se o campo for preenchido com N (NÃO), o campo DatSai não
  será alterado.

Retenção Data Baixa Título

Se este campo for preenchido igual a "S - Sim" nas telas F661I12 (PIS e COFINS), F661I14 (IRPJ/CSLL Presumido), F661I15 (IRPJ/CSLL Real) e F661I17 (IRPJ/CSLL Imunes e Isentas), serão considerados os valores de retenção dos respectivos impostos proporcionais aos valores baixados do título no período.

No caso das retenções de PIS e COFINS, este parâmetro também está disponível na tela F661UCR, sendo que esta parametrização específica (E661UCR) será mandatória sobre o parametrizado para a filial (E070FEF) e válido exclusivamente para PIS e COFINS, permitindo diferentes regimes entre a apuração de PIS/COFINS e IR/CSLL. Além disso, também permite alternar entre o regime de caixa e competência das retenções de PIS e COFINS.

Esse campo atende clientes que não fazem a retenção das contribuições sociais pelo módulo Financeiro e optam por realizar a retenção diretamente na nota fiscal do Faturamento, onde a rotina de apuração e geração de todas as obrigações acessórias consideram o momento da baixa do título da nota fiscal (independentemente do tipo de baixa), ao invés de considerar a data da emissão da nota fiscal, levando em consideração a possibilidade de pagamentos parcelados. Isso deve ser feito para considerar a retenção na emissão da nota fiscal.

Este campo não tem por objetivo navegar pelos diversos títulos que são gerados ao longo de sua trajetória para identificar quando ocorre a data da entrada do dinheiro na empresa. Se há a necessidade de considerar a retenção pela data da entrada do dinheiro, deve ser utilizada a retenção pelo Financeiro na baixa do título.

O conceito de busca das retenções no caso de títulos substituídos pela sua baixa é aplicado para a apuração dos impostos PIS e Cofins por regime de caixa.

Observação

Para Outros documentos esse parâmetro não possui tratamento. O controle das retenções deve ser feito pela baixa do contas a receber.

Subtrair IPI do valor contábil na composição do índice
do CIAP

Caso este parâmetro esteja preenchido com S (Sim), ao calcular
o índice do CIAP, na tela
F660CCI botão
Calc. Índice, o valor do IPI das notas fiscais
de venda e reduções Z é deduzido do valor contábil.

Limite Utilização Crédito
Rural ICMS (Meses) 

Para o agronegócio. Indica a quantidade de meses anteriores aos do processo
em que podem ser selecionadas as NF de crédito na tela F445PRC.

Dispositivo Fiscal Crédito
Rural ICMS

Para o agronegócio. Permite informar um código de dispositivo fiscal, ele é incluído no item da nota fiscal a fim de justificar o valor da operação de recuperação de crédito efetuado na tela F445PRC, este código será apresentado no arquivo do SPED Fiscal como informativo. Os dispositivos fiscais são cadastrados na tela F051DIS.

Transação Nota Crédito
Rural ICMS 

Para o agronegócio. Permite informar apenas transações de venda com itens de
produto, para gerar a nota fiscal de recuperação do crédito de ICMS, na tela F445PRC.

Série Nota Crédito
Rural ICMS 

Para o agronegócio. Permite informar o código da série a ser utilizado ao gerar a nota fiscal de crédito rural, na tela F445PRC.

Classificação Tributária eSocial

Informe o código da classificação tributária de acordo com o eSocial.

Entidade PAA

Informe se a entidade está inscrita no programa de aquisição de alimentos.

Classificação Tributária Reinf

Informe o código da classificação tributária de acordo com o REINF.

Tipo Sociedade Cooperativa

Nessa campo é informada qual a cooperativa que a filial se
enquadra. Esse campo reflete na geração dos registros M211 e
M611 do SPED Contribuições e possui a seguintes opções:

* 1. (Cooperativa de Produção Agropecuária),
* 2. (Cooperativa de Consumo),
* 3. (Cooperativa de Crédito),
* 4. (Cooperativa de Eletrificação Rural),
* 5. (Cooperativa de Transporte Rodoviário de Cargas),
* 6. (Cooperativa de Médicos) e
* 99. (Outras).

Forma lançamento devolução dif. de alíq. no ICMS

Nesse campo é possível parametrizar como serão utilizadas as devoluções do diferencial de alíquotas na apuração do ICMS/Diferencial de alíquotas.

Manter CIAP na Transferência entre Filiais

Através deste campo é possível parametrizar se na transferência de um bem entre filial, o CIAP será mantido. Opções:

* "S - Sim": o sistema mantém a transferência das parcelas do CIAP, independentemente do estado da filial de destino do bem;
* "N - Paralisar transferências entre estados": o sistema irá paralisar as parcelas do CIAP quando a transferência for realizada entre filiais de estados diferentes;
* "T - Paralisar todas as transferências": o sistema irá paralisar as parcelas do CIAP, independentemente do estado das filiais (localização atual e destino).

Subtrair ICMS ST vlr. cont. na comp. do Índ. CIAP

Caso este parâmetro esteja preenchido com "S - Sim", ao calcular o índice do CIAP, na tela Cálculo do CIAP (F660CCI), botão Calc. Índice, os valores de ICMS ST e FCP retido por ST serão subtraídos do valor contábil das notas fiscais/reduções Z.

Operação Realizada

Se o campo Tipo de Empresa, da tela F070FCA estiver
preenchido com 9 ou 12, este campo fica habilitado. O Bloco I do SPED Contribuições (F669SPC)
será gerado, caso este campo tenha preenchimento, exceto os
registros I200, I300 e I399 que são gerados apenas via cadastro
de declarações (F049DEC), no modelo DACT002.  

Os blocos A, C e D do SPED Contribuições, assim como o registro
F100, são gerados caso este seja igual a 00. No cálculo dos impostos 41, 42, 43 e 44 (F661I12)
se a filial possuir este campo preenchido as alíquotas básicas
de PIS e COFINS cumulativos serão 0,65% e 4%, respectivamente.

Tabela de presunção IRPJ

Informar o código da tabela de presunção IRPJ, no qual foi feito o cadastro na tela F055TPR.

Tabela de presunção CSLL

Informar o código da tabela de presunção CSLL, no qual foi feito o cadastro na tela F055TPR.

Lucro de Exploração

Informar na filial matriz se a empresa usufrui benefícios fiscais calculados com base no lucro da exploração na apuração dos impostos 55 – IRPJ Lucro Real (SPED) e 56 – CSLL Lucro Real (SPED).

FINOR/FINAN/FUNRE

Informar na filial matriz se empresa possui incentivos em favor do Fundo de Investimento do Nordeste (FINOR), Fundo de Investimento da Amazônia (FINAM) e Fundo de Recuperação Econômica do Estado do Espírito Santo na apuração dos impostos 55 – IRPJ Lucro Real (SPED) e 56 – CSLL Lucro Real (SPED).

Modalidade Cálculo CIAP

Nesse campo é definida a forma de cálculo do valor do CIAP para cada parcela, conforme opções abaixo:

* M - Parcelas do Período: é somado o valor das parcelas do período e aplicado o índice. Esse valor de CIAP resultante é distribuído proporcionalmente ao valor da parcela;
* P - Por Parcelas: o índice é aplicado diretamente ao valor da parcela para obter o valor do CIAP.

Período Apuração Estoque e Produção SPED Fiscal

Este parâmetro indica o período que será utilizado para a apuração do estoque e produção na geração do bloco K do SPED Fiscal, podendo ser preenchido com as opções Decendial, Quinzenal ou Mensal. Por padrão, a opção Mensal será sugerida.

Lançar ICMS Simples no ICMS

Indicativo do local em que o crédito do ICMS de compra de fornecedor do simples nacional será lançando. Quando este campo estiver parametrizado com S – Sim o crédito será lançado nos campos relativos ao ICMS, e quando parametrizado com N – Não será lançado em campo específico, neste caso o crédito continua sendo lançando no valor do ICMS do Simples Nacional, no campo de valor de ajustes do item da nota fiscal, para que possa ser justificado nos registros C197 - Outras Obrigações Tributárias, Ajustes e Informações provenientes de Documento Fiscal e E111 - Ajuste/Benefício/Incentivo da Apuração do ICMS do SPED Fiscal.

**Atividade Rural**

Indicativo de Atividade Rural. Possui os valores **S-Sim** e **N-Não**. Na geração da ECF, quando a versão do leiaute for maior ou igual a 5 e esse campo estiver como **N-Não** ou vazio, os registros L300, P150, M300 e M350 não considerarão as linhas de atividade rural.

**Tipo Pessoa Jurídica Imunes ou Isentas**

Permite na apuração dos impostos IRPJ/CSLL Lucro Real, IRPJ/CSLL Lucro Presumido, IRPJ/CSLL Lucro Arbitrado e IRPJ/CSLL Imunes ou Isentas realizar o cadastro/execução de regras de validações. Este campo deverá ser preenchido pela empresas que possuem esse regime tributário, sendo que a informação registrada será apresentada no registro **0010 - Parâmetros de Tributação** do SPED ECF. A codificação que deve ser informada neste campo está disponível no guia prático do SPED ECF.

Tipo Crédito ST Nota

Indica o tipo de crédito de substituição tributária utilizado no cálculo do imposto do ICMS. Possui as opões **T - Total da Nota Fiscal de Entrada** e **S - Proporcional Nota Fiscal de Saída**.

* **T - Total da Nota Fiscal de Entrada:** com esta opção selecionada, todas as aquisições com cálculo de ICMS ST são consideradas como outros créditos de ICMS;
* **S - Proporcional Nota Fiscal de Saída:** com esta opção selecionada, quando ocorrer uma venda interestadual de um produto adquirido com ICMS ST, e na venda possuir ICMS ou ICMS ST (operação tributável), é gerado um item com o valor do ICMS ST das entradas do produto, como outros créditos na apuração do ICMS, correspondente a proporcionalidade da quantidade vendida no período. Este valor de outros créditos é exibido com a mensagem Ressarcimento relativo Substituição Tributária.

Para o funcionamento desta opção, o campo Registra entrada e saída dos produtos deve estar parametrizado como **S – Sim** na tela Cadastro de Empresas (F070EMP).

Filial Consolidadora

Este campo irá identificar a filial que irá consolidar as notas fiscais e o saldo de estoque da filial selecionada. Este campo é uma alternativa à rotina de consolidação de notas fiscais entre filiais, porém com o mesmo objetivo, ou seja, possibilitar a apuração dos impostos e geração dos arquivos fiscais a partir de uma filial consolidadora. Se aplica a:

* Notas fiscais - na tela F660INT, ao selecionar uma filial válida, automaticamente será lançada a nota fiscal para a filial consolidadora, garantindo inclusive, que a informação seja replicada e atualizada em todos os cadastros do sistema que o utilizem.
* Saldos de estoque - na tela F660CMO o campo Tipos Lançamentos permitirá selecionar apenas lançamentos do tipo Inventário Fiscal. E será sugerido como filial disponível para o campo Filiais a Consolidar Movimento, somente as filiais que possuem como filial consolidadora de movimentos a filial logada.

Forma Compensação/Restituição

Indica se a empresa irá controlar os impostos dos tipos 17, 41, 42, 43, 44, 47, 48, 53, 54, 55, 56, 57, 58, 59, 60, 61 que foram pagos a maior ou indevidamente, através da tela de Controle de Restituição/Compensação. Esse campo é habilitado somente para filiais matriz (campo Filial Matriz da tela Cadastro de Filiais - F070FCA) ou a filial está definida como Filial Matriz no Agrupamento de Filiais(F070AFI).   
Estão disponíveis as opções:

* **T - Automática impostos mesmos tipo**: Só serão considerados os saldos para o mesmo tipo do imposto apurado, para compensar o imposto a pagar.
* **A - Automático para qualquer tipo de imposto**: Todos os tipos de imposto serão considerados para compensar o imposto a pagar.
* **M - Manual**: A tela F661RST será exibida durante a apuração, para que seja realizada a compensação manualmente, conforme necessidade.
* **N - Nenhum**: não possui o controle

Considerar RPA na Apuração do ISS

Forma de utilização do valor de ICMS dos RPAs na apuração do ICMS.

Considerar RPA na Apuração do ICMS

Forma de utilização do valor de ICMS dos RPAs na apuração do ICMS, possui as seguintes opções:

* **E - Apuração Específica**: os valores de ICMS retido nos recibos de pagamentos autônomos são lançados na coluna de **Por Entradas** da apuração do imposto de tipo 26 - ICMS Responsabilidade Tributária/Frete;
* **O - Outros Débitos**: os valores de ICMS retido nos recibos de pagamentos autônomos são lançados em uma linha de outros débitos na apuração do imposto do tipo 2 - ICMS.

Lançar Valor Acumulado

Indica a forma que o valor acumulado de IPI é lançado na apuração do imposto. Possui as seguintes opções:

* O - Outros Débitos: o valor acumulado é gerado no campo de outros débitos;
* G - Guia de Recolhimento: o valor acumulado é somado ao valor líquido do título do financeiro e no valor da Guia de Recolhimento.

Desc. Devoluções de venda índice CIAP

Indica se as devoluções de venda que foram consideradas na composição do cálculo Índice do CIAP devem ser descontadas. Quando estiver parametrizado como **Sim**, o valor das devoluções de vendas dos documentos que compõe o índice do CIAP são descontados (saídas tributadas e Valor total das saídas).

## Exemplo

01:

* Venda tributada: 100.000,00;
* Venda Não tributada: 50.000,00;
* Devolução de venda tributada: 5.000,00;
* Percentual índice CIAP: 95.000,00/145.000,00 = 0,6552.

02:

* Venda tributada: 100.000,00;
* Venda Não tributada: 50.000,00;
* Devolução de venda NÃO tributada: 5.000,00;
* Percentual índice CIAP: 100.000,00/145.000,00 = 0,6897.

Nas operações de devoluções de venda (NF de entrada) é considerado também as parametrizações para considerar ou não os valores de Outras, IPI e ICMS ST, conforme indicação da parametrização na filial.

E quando estiver parametrizado como **Não**, o cálculo do CIAP e geração do SPED Fiscal não sofrem alteração, permanecendo o comportamento padrão.

## Exemplo

01:

* Venda tributada: 100.000,00;
* Venda Não Tributadas: 50.000,00;
* Devolução de venda tributada: 5.000,00;
* Percentual índice CIAP: 100.000,00/150.000,00 = 0,6667.

02:

* Venda tributada: 100.000,00;
* Venda Não Tributada: 50.000,00;
* Devolução de venda NÃO tributada: 5.000,00;
* Percentual índice CIAP: 100.000,00/150.000,00 = 0,6667.

Valor limite do faturamento do Simples Nacional

Indica o valor da receita considerada para o sublimite de tributação do ISS. Quando o faturamento dos últimos 12 meses ultrapassar o sublimite o sistema não apresenta o valor da retenção do ISS no cálculo do imposto simples nacional.

Tipo nota fiscal produtor tem valor

Indica qual documento fiscal do produtor rural deve ser escriturado com valor e a opção padrão é **Ambos**. Quando informado **C - Contranota**, o sistema gravará os valores dos dados gerais e itens quando estiver processando uma nota fiscal de emissão própria (contranota). Se informado **N - Nota fiscal**, serão gravados os valores dos dados gerais e itens quando estiver processando uma nota fiscal cujo modelo seja **04 - NF Produtor Rural**.

Essa parametrização influencia na integração de notas fiscais de produtor de acordo com a opção selecionada. Para mais informações, consulte a documentação de integração de notas fiscais.

FCP Próprio incluso ao ICMS

Indica se o FCP Próprio deve ser somado ao ICMS durante o processo de integração de notas fiscais.

FCP ST incluso ao ICMS ST

Indica se o FCP ST deve ser somado ao ICMS ST durante o processo de integração de notas fiscais.

Cont. Isento CP

Indica se o contribuinte possui isenção de contribuição previdenciária de acordo com a lei nº 13.606/2018. Caso possua isenção de contribuição (Sim), na integração dos registros da EFD-Reinf (F690ILA), o campo Indicativo de Comercialização (indCom) será gerado como 7.

Cons. data ex. serv. prestado como data de emissão

Indica se a data de execução do serviço prestado deve ser considerada como data de emissão. Possui as opções S-Sim e N-Não.

Cons. Transf. Créd. Data Saída da NF

Indica se a transferência de crédito/débito de ICMS deve ser considerada conforme data de saída da nota fiscal. Possui as opções S-Sim e N-Não, sendo N-Não a opção padrão.

**Forma de Retenção de IRRF Nota Entrada**

Permite definir a forma de retenção de IRRF nas notas de entrada. Na EFD-Reinf é possível reconhecer (integrar) o IR por regime de caixa, mesmo que a empresa tenha feito a retenção por competência. Assim, havendo IR na nota fiscal, quando esse campo for igual a "3 - Regime Caixa", o IR será integrado na data do pagamento e não da nota.

**Cons. Produtos Distintos**

Permite a integração das ordens de produção de processos internos e externos sem a movimentação de estoque na nota de remessa/retorno. Para mais informações, confira a documentação.

**Cons. Serviços Terc. Bloco K**

* Na tela F660ISP, no processo de rateio quando o componente/insumo é utilizado por mais de um produto produzido, se o parâmetro estiver como "S - Sim", será gerado um apontamento de produção em terceiros com o serviço da nota fiscal de retorno para industrialização. Os componentes dessa operação serão os produtos enviados na nota fiscal de remessa;
* Ainda na mesma tela, na apuração dos movimentos de estoque e produção, se o parâmetro estiver como "S - Sim", serão gerados os serviços ligados à OP (E900SOP) como componente da produção.

Para mais informações, confira a documentação.

Competência de Início do Faturamento da Filial

Indica quando efetivamente ocorreu o primeiro faturamento da filial. Este parâmetro é necessário para reativar as parcelas do CIAP que foram paralisadas anteriormente por ter ocorrido transferências entre filiais. Para reativar, o campo Manter CIAP na Transferência entre Filiais deve estar diferente de "S - Sim".

Ind. Nota Fiscal Prod. Rural Fixar Integração R-2055

Indicativo se devem ser integradas para o registro "R-2055 - Aquisição de produtor rural" do REINF, as notas fiscais de entrada de produtor rural a fixar (depósito).

Quantidade de parcelas para parcelamento do Imposto Importação na apuração do ICMS

Informe a quantidade de parcelas para parcelamento do imposto de importação na apuração do ICMS, lançado como "Outros Débitos" através da mensagem "Débito Parcelado de ICMS Importação - Art. 74".

Quantidade de parcelas para parcelamento do ICMS Diferido das operações internas na apuração do ICMS

Informe a quantidade de parcelas para parcelamento do ICMS Diferido das operações internas a ser lançado na apuração do ICMS como "Outros Débitos".

Considerar estorno por devolução de bem na apuração do PIS e Cofins

Indica se os créditos de PIS e COFINS devem ser estornados na devolução de um bem do ativo imobilizado na apuração dos impostos 41 e 42. Veja o impacto na apuração dos impostos.

Código Filial Sócio Ostensiva

Ver Configuração da filial de Sociedade em Conta de Participação (SCP).

% Participação Filial Sócio Ostensiva

Ver Configuração da filial de Sociedade em Conta de Participação (SCP).

Código de imposto ST para integrar guia paga pelo remetente

* Utilizado para indicar o código do imposto tipo "34 - ICMS - Substituto por estado", este recurso integra, na Gestão de Tributos, a guia de recolhimento paga pelo remetente da mercadoria, para fins de apresentação deste documento no registro C112 do SPED Fiscal. Esse procedimento gerará a guia apenas na Gestão de Tributos, sem criar título no Contas a Pagar.
* A guia será gerada automaticamente sempre que uma nota fiscal de entrada for gravada na Gestão de Tributos, seja por meio da rotina de integração de notas fiscais, digitação manual ou integração via web services. Será gerada uma guia para as notas cujo valor de ("Valor ICMS ST Não Recuperado" + "Valor ICMS Substituído" - "ICMS ST Resp. Solidário") seja maior que zero. Este valor será utilizado como **Valor Principal** e também como **Valor Recolhido** da guia. O vencimento será determinado conforme os parâmetros do imposto na tela Configuração de Impostos para a Filial (F055PPF): Periodicidade (grade Impostos), Início Contagem, Dias Vcto. e Vcto. não útil (grade ICMS ST por Estado, para o estado da filial).

Programa de Incentivo ao Algodão

Neste campo, é possível selecionar o programa de incentivo ao algodão na qual a filial está cadastrada. As opções homologadas são:

* 1 - Nenhum (Valor padrão);
* 2 - Proalba - Programa de Incentivo à Cultura do Algodão da Bahia.

Caso seja selecionado um benefício, serão disponibilizadas outras parametrizações para a realização dos cálculos:

* Impostos: Programas de incentivo ao algodão na Bahia.

Calcula FAF

Indica se deverá ser calculado o fator de ajuste de fruição.

Consid. CST de Pis /Cofins 04 e 05 receita tributada na matriz de crédito

Indicativo sobre se as CST de PIS/COFINS 04 e 05 devem ou não ser consideradas na composição das receitas tributadas para fins de apuração da matriz de crédito do PIS/COFINS.

Local para lançamento do crédito de ICMS monofásico destacado

* I - ICMS do item da Nota Fiscal de Entrada: Quando parametrizado dessa forma, o sistema gerará o valor do "ICMS monofásico destacado" no campo do ICMS próprio ao integrar uma nota fiscal de entrada, desde que o CST do ICMS seja 61 e a operação recupere ICMS (Transação, Fornecedor e Produto configurados para "Recuperar ICMS" = "S-Sim").
* N - Não lançar: Neste caso, os valores do ICMS monofásico serão lançados em seus respectivos campos específicos. Havendo possibilidade de crédito, pode-se realizar o ajuste por dispositivo fiscal.

Lançar ICMS ST Solidário como ICMS ST Não recuperado

Indicativo se o sistema deverá, no processo de Integração de Notas Fiscais (F660INT), lançar ou não na coluna ICMS ST não recuperado das notas fiscais de entrada o valor do ICMS ST Solidário, cuja operação não seja de recuperação do ICMS (transação, fornecedor ou produto que não recuperam ICMS).

**Uti. Rateio Consumo Crédito**

Quando o parâmetro **Uti. Rateio Consumo Crédito** estiver ativo "S - Sim", na apuração do PIS e COFINS não cumulativos, o consumo de créditos ocorrerá de forma proporcional entre os tipos de crédito existentes no período. O rateio ocorrerá quando o saldo de créditos de um determinado período de apuração for superior ao valor dos débitos a serem compensados.

Exemplo - Apuração de 01/2025:  
Débito Pis Não Cumulativo 01/2025: 100.000,00  
Créditos apurados em 01/2025: 40.000,00  
Saldo de créditos períodos anteriores: 110.000.00, sendo parte de nov/24 e parte dez/24  
Saldo credor para período futuro: 20.000,00

* Consumo de créditos rateado conforme abaixo:

Crédito total apurado em 11/2024 (5.000,00) é menor que o valor a ser compensado (100.000,00), sendo integralmente creditado conforme detalhado abaixo:

| Tipo Crédito | Período Apuração Crédito | Valor Crédito | Consumo Crédito | Saldo para mês seguinte |
| --- | --- | --- | --- | --- |
| 101 | 11/2024 | 3.000,00 | 3.000,00 | 0,00 |
| 301 | 11/2024 | 2.000,00 | 2.000,00 | 0,00 |

Crédito total apurado em 12/2024 (105.000,00) é maior que o valor a ser compensado (95.000,00 considerando abatimento dos créditos de 11/2024). Nesse caso, aplicará a proporção:

| Tipo Crédito | Período Apuração Crédito | Valor Crédito | Consumo Crédito | Saldo para mês seguinte | Proporcionalidade |
| --- | --- | --- | --- | --- | --- |
| 101 | 12/2024 | 85.000,00 | 75.904,76 | 8.095,24 | 85.000,00 dividido pelo total crédito período (105.000,00) = 80,95% do valor a compensar (95.000,00) será consumido deste crédito |
| 301 | 12/2024 | 20.000,00 | 18.095,24 | 1.904,76 | 20.000,00 dividido pelo total crédito período (105.000,00) = 19,05% do valor a compensar (95.000,00) será consumido deste crédito |

Crédito apurado no mês da apuração não foi utilizado e será acumulado para meses posteriores:

| Tipo Crédito | Período Apuração Crédito | Valor Crédito | Consumo Crédito | Consumo Crédito |
| --- | --- | --- | --- | --- |
| 101 | 01/2025 | 40.000,00 | 0,00 | 40.000,00 |

Ind. Tipo Data Integr. Reinf:

Define a data a ser considerada para integrar os registros do bloco 4 da EFD-Reinf via tela EFD-Reinf - Integração (F690ILA), nos casos em que não houver parametrização para a geração dos títulos de impostos retidos (F001TIT - Fato Gerador IR)) na transação da nota fiscal.

Apurar DIFAL e FCP para endereço do cliente PJ:   
Quando parametrizado com "S - Sim", permite gerar o registro 0150 do SPED Fiscal com o endereço do destinatário da nota fiscal, em vez do endereço de entrega. Dessa forma, em operações interestaduais com incidência de Diferencial de Alíquota (DIFAL) e Fundo de Combate à Pobreza (FCP) devidos à UF de destino, o sistema se comportará da seguinte maneira:

* Para operações com Pessoa Jurídica:
  + O débito de DIFAL/FCP, ou o crédito (em situações de devolução), será lançado na apuração do estado do cliente
  + Por meio dos campos Outros Crédito e Outros Débitos. A transferência desses valores para o(s) estado(s) do endereço de entrega será registrada nesses mesmos campos.
  + No estado do endereço de entrega, os valores recebidos em transferência também serão automaticamente lançados nos campos Outros Crédito e Outros Débitos.
  + No SPED Fiscal, o registro 0150 será gerado considerando o endereço cadastrado do cliente, em vez do endereço de entrega.
* Para operações com Pessoa Física:
  + O débito de DIFAL/FCP, ou o crédito (em situações de devolução), será lançado na apuração diretamente no estado do endereço de entrega.
  + No SPED Fiscal, o registro 0150 será gerado considerando a sequência do endereço de entrega.

Essa distinção entre clientes pessoa física (PF) ou pessoa jurídica (PJ) decorre do Manual de Orientação do SPED, o qual prevê que podem ser informados múltiplos cadastros de um mesmo participante quando se trata de pessoa física.

“Para o caso de participante pessoa física com mais de um endereço, podem ser fornecidos mais de um registro, com o mesmo NOME e CPF. Neste caso, deve ser utilizado um COD\_PART distinto para cada registro, alterando os demais dados.”

Importante

O Guia Prático da EFD – versão 3.2.1 trouxe esclarecimentos sobre o tema. Para o cenário do DIFAL da EC 87/2015, devem ser mantidos os dados do adquirente ou tomador, alterando-se apenas o código do município para aquele correspondente ao local de entrada física da mercadoria. Diante dessa orientação, este parâmetro deve permanecer configurado como “N - Não”.

## Páginas relacionadas

* [Exemplo do 
tratamento das notas fiscais de serviços (Entrada e Saídas) no sistema.](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/exemplo_tratamento_de_servicos_nos_livros.htm)
* [crédito do imposto](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/patrimonio/calculo-credito.htm)
* [F661I18](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f661i18.htm)
* [F660INF](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f660inf.htm)
* [F049TTR](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f049ttr.htm)
* [Bloco F](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/sped/contribuicoes-pis-cofins/bloco-f.htm)
* [Funcionalidade do campo Agrupamento de filiais para a geração do SPED Contribuições.](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/sped/contribuicoes-pis-cofins/agrupamento-filial.htm)
* [F660NCI](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f660nci.htm)
* [F661UCR](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f661ucr.htm)
* [F660CCI](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f660cci.htm)
* [F445PRC](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f445prc.htm)
* [F051DIS](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f051dis.htm)
* [F669SPC](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f669spc.htm)
* [F049DEC](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f049dec.htm)
* [F661I12](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f661i12.htm)
* [F055TPR](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f055tpr.htm)
* [SPED ECF](http://sped.rfb.gov.br/pasta/show/1644)
* [Cadastro de Empresas (F070EMP)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070emp.htm)
* [F660INT](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f660int.htm)
* [F660CMO](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f660cmo.htm)
* [confira a documentação](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/processo-bloco-k.htm#retorno-bloco-k)
* [F660ISP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f660isp.htm)
* [confira a documentação](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f660isp-remessa-retorno.htm)
* [Veja o impacto na apuração dos impostos](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f661i12.htm#considerar-estorno)
* [Configuração da filial de Sociedade em Conta de Participação (SCP)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/sped/parametrizacoes-fiscal-contribuicoes-sef.htm#scp)
* [C112](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/sped/fiscal-icms-ipi/bloco-c.htm#C112)
* [Configuração de Impostos para a Filial (F055PPF)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f055ppf.htm)
* [Impostos: Programas de incentivo ao algodão na Bahia](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/manuais_processos/agronegocio/processos/impostos/algodao_bahia.htm)
* [EFD-Reinf - Integração (F690ILA)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f690ila.htm)
* [F001TIT](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f001tit.htm)
