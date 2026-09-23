# Integração dos Outros Documentos

> **Fonte:** F660IFI - Integração de Outros Documentos — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f660ifi.htm  
> **Trilha:** Ajuda por telas > Controladoria > Gestão de Tributos > Escrituração > Integrações  
> **Telas citadas:** F055PPF, F070FEF, F075PRO, F080SER  
> **Identificadores de regras:** —

---
Esta grade exibe os dados dos títulos financeiros. Ao clicar em Mostrar, os valores de % PIS/COFINS, Valor Base
PIS/COFINS, Valor PIS/COFINS, Sit. Trib. PIS/COFINS e Vlr. Ope. não serão exibidos
na grade, mas sim após informar o produto/serviço e clicar
em Apl. Selecio. ou Apl. Todos. Ao clicar no botão C da grade, será possível definir a ordem em que são
apresentados os dados na tela.

Empresa

Indica qual empresa o título financeiro será integrado ou está integrado.

Filial

Indica qual Filial o título financeiro será integrado ou está integrado.

Doc.

Mostra o número do título financeiro gerado no momento integração, este campo só estará preenchido quando o título
financeiro estiver integrado.

Data Oper.

Indica a data do título financeiro.

Forn.

Indica o fornecedor quando for um título financeiro de entrada.

Cliente

Indica o cliente quando for um título financeiro de saída.

Ent./Saí.

Indica se o documento é um título financeiro de entrada ou saída.

Trans.

Indica a transação do título financeiro.

Produto

Indica o produto informado para o título financeiro.

Derivação

Indica a derivação informada para o título financeiro.

Vlr. Ope.

Mostra o valor do título financeiro. Ao clicar em Mostrar, o sistema listará 0 - Zero quando os Outros Documentos não forem relativos a uma retenção de PIS/COFINS ou nota fiscal de saída. Já para os demais casos o valor de operação será igual a Base de Cofins, que é inicializado de acordo com a parametrização da tela Configuração de Imposto para a Filial (F055PPF), para a transação de baixa do contas a pagar ou contas a receber. Ou seja, caso a parametrização para essa transação indique que deva somar somente a multa, esse campo é preenchido com o total de multa da baixa do título.

Serviço

Indica o serviço informado para o título financeiro.

Descr.

Indica a descrição do tipo do título financeiro.

Cta. Ctb.

Mostra a conta contábil informada no título financeiro.

CC.

Mostra o centro de custo informado no título financeiro.

Sit. Trib. PIS

Indica a situação tributaria do PIS conforme o cadastro do produto ou serviço.

Nat. Rec. PIS

Indica a natureza da receita do PIS.

% PIS

Indica o percentual do PIS conforme a tabela de tributação para o imposto do tipo 41,
43, 47, 19, 20 e agrupamento GAF. Ao clicar em Mostrar, o valor não é exibido na grade,
mas sim após informar o produto/serviço e clicar em **Apl. Selecio.** ou **Apl.
Todos.**

Será feita a seguinte consistência:

* se o Produto/Serviço possuir o Regime Tributário igual a **C -
  Cumulativo** (F075PRO e F080SER),
  o percentual será listado conforme o preenchimento do campo Calcular
  PIS/COFINS Financeiro no cadastro do imposto (F070FEF):
  + se estiver preenchido com 3 (Regime de Caixa), listará os valores
    referente ao imposto 47;
  + se estiver preenchido com um valor diferente de 3 (Regime de Caixa), buscará os valores dos impostos 41 e 43. Se não
    houver valor, trará os valores dos impostos 19 e 20.

Vlr. Base PIS

Mostra a base de cálculo do PIS. Este campo é inicializado de acordo com a parametrização da tela Configuração de Imposto para a Filial (F055PPF), para o imposto do tipo 42,
44, 48, 18, 21, para a transação de baixa do contas a pagar ou contas a receber.  

Caso a parametrização para a transação de baixa do contas a receber indique que deve somar somente a multa, esse campo é preenchido com o total de multa da baixa do título.

Vlr. PIS

Mostra o valor do PIS para o título.

Sit. Trib. COFINS

Indica a situação tributaria do COFINS conforme o cadastro do produto ou serviço.

Nat. Rec. COFINS

Indica a natureza da receita do COFINS.

% COFINS

Indica o percentual do COFINS conforme a tabela de tributação para o imposto do tipo 42,
44, 48, 18, 21  e agrupamento GAF. Ao clicar em Mostrar, o valor não é exibido na grade, mas sim após informar o produto/serviço e clicar em **Apl.
Selecio.** ou **Apl. Todos**.

Será feita a seguinte consistência:

* se o Produto/Serviço possuir o Regime Tributário igual a **C -
  Cumulativo** (F075PRO e F080SER),
  o percentual será listado conforme o campo Calcular
  PIS/COFINS Financeiro no cadastro do imposto (F070FEF):  
  + se estiver preenchido com 3 (Regime de Caixa), listará os valores
    referente ao imposto 48;
  + se estiver preenchido com um valor diferente de 3 (Regime de Caixa), buscará os valores dos impostos 42 e 44. Se não
    houver valor, trará os valores dos impostos 18 e 21.

Base COFINS

Mostra a base de cálculo do COFINS conforme parametrização feita na tela Base Imposto (Liga Filial) na filial matriz
para o imposto do tipo 42, 44, 48, 18, 21.

Vlr. COFINS

Mostra o valor do COFINS para o título.

Base PIS Retido

Mostra base de cálculo do PIS retido conforme título financeiro.

Vlr. PIS Retido

Mostra valor do PIS retido conforme título financeiro.

Base COFINS Retido

Mostra base de cálculo do COFINS retido conforme título financeiro.

Vlr. COFINS Retido

Mostra valor do COFINS retido conforme título financeiro.

Base IRRF

Mostra o valor da base de cálculo do IRRF (Imposto de Renda Retido na Fonte) retido conforme título no financeiro.

Valor IRRF

Mostra o valor do IRRF (Imposto de Renda Retido na Fonte) retido conforme título no financeiro.

Base CSLL Retido

Mostra o valor da base de cálculo da CSLL (Contribuição Social sobre o Lucro Líquido) retida conforme título no financeiro.

Valor CSLL Retido

Mostra o valor da CSLL (Contribuição Social sobre o Lucro Líquido) retida conforme título no financeiro.

Empresa do título a receber

Informa a empresa do título a receber.

Filial do título a receber

Informa a filial do título a receber.

Nº Título a receber

Informa o número do título a receber.

Tipo do título a receber

Informa o código do tipo do título a receber.

Seq.

Informa a sequência de movimento do título a receber.

Empresa do título a pagar

Informa a empresa do título a pagar.

Filial do título a pagar

Informa a empresa do título a pagar.

Nº Título a pagar

Informa o número do título a pagar.

Tipo do título a pagar

Informa o código do tipo de título a pagar.

Fornecedor

Informa o fornecedor do título a pagar.

Seq.

Informa a sequência do movimento do título a pagar.

Empresa da Tesouraria

Informa a empresa da tesouraria.

Conta Interna

Informa o número da conta interna da tesouraria.

Data Mov.

Informa a data do movimento da conta na tesouraria.

Seq.

Informa a sequência na data do movimento da conta interna na tesouraria.

Lct. Multa   
O padrão é "N-Não" e somente será "S-Sim" quando, na tela F055PPF Configuração de Impostos para a Filial em Base Imposto (Liga Filial), for definido para a transação do movimento que devem ser gerados dois outros documentos, sendo um para Multa e outro para Juros. Nesse caso, ao herdar as parametrizações do produto/serviço, o sistema assume como valor e base de cálculo dos impostos o valor da Multa do movimento integrado.

Lct. Juros

O padrão é "N-Não" e somente será "S-Sim" quando, na tela F055PPF Configuração de Impostos para a Filial em Base Imposto (Liga Filial), for definido para a transação do movimento que devem ser gerados dois outros documentos, sendo um para Multa e outro para Juros. Nesse caso, ao herdar as parametrizações do produto/serviço, o sistema assume como valor e base de cálculo dos impostos o valor dos Juros do movimento integrado.

Observação

Ao clicar no botão Marcar, todos os registros da grade são marcados, porém como eles seguem as configurações dos produtos, o sistema apresentará uma mensagem questionando se você quer, de fato, marcar todos ou aplicar a lógica da configuração dos produtos. Clicando com o botão direito do mouse sobre a grade, será possível selecionar de uma só vez todos os itens de multas, juros ou demais registros.

## Páginas relacionadas

* [F075PRO](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075pro.htm)
* [F080SER](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f080ser.htm)
* [F070FEF](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070fef.htm)
* [Configuração de Imposto para a Filial (F055PPF)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f055ppf.htm)
