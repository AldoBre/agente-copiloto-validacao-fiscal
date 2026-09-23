# Cálculo do IPI

> **Fonte:** Cálculo do IPI — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/processo_geracao_calculo_ipi.htm  
> **Trilha:** Segmentos > Compliance > Configurações para cálculos fiscais > Impostos > IPI  
> **Telas citadas:** F051IMP, F055PPF, F070FEF, F661ORI, F661PAI  
> **Identificadores de regras:** —

---
Segmentos > Compliance > Configurações para cálculos fiscais  > Impostos  > IPI > Cálculo do IPI

|  |  |
| --- | --- |
|  | Veja também: |

* IPI
* Enquadramento e Situações Tributárias de IPI

## Carta e declaração de suspensão de IPI para fornecedores

Empresas do ramo de produção de produtos autopropulsados ou de componentes para produtos autopropulsados devem apresentar declaração de suspensão de IPI à Secretaria da Receita Federal e ao vendedor indicando que o seu produto pode ser comercializado com suspensão de IPI conforme art. 29 da Lei 10.637/2002 e art. 7º da IN RFB 948/2009.

* CIOD033 - Carta de suspensão de IPI a ser encaminhada aos fornecedores
* CIOD034 - Declaração de suspensão de IPI a ser encaminhada à Receita

## Parametrizações necessárias para apuração do cálculo do imposto

* Cadastrar o imposto na tela F051IMP, tipo 01 -
  IPI
* Cadastrar, na filial, o código do imposto (F055PPF)
* Para esse imposto não é possível cadastrar uma Tabela de Tributação
* Na tela F661PAI
  informe o código da filial e o período desejado, clique no botão Mostrar e selecione o código do imposto. Depois, clique em Calcular. Será aberta a tela de apuração do cálculo do
  IPI com os respectivos valores. Para gravar a apuração, clique em Processar

Na apuração do cálculo do Imposto IPI são demonstrados os valores do imposto IPI
que foram creditados através das notas fiscais de entradas e os valores que foram
debitados através das notas fiscais de saídas.  
As notas fiscais de entradas e saídas para serem consideradas na apuração precisam estar integradas.

No botão Origem é acessada a tela F661ORI, onde são
demonstrados todos os movimentos de entradas e saídas que foram considerados na
apuração. Os valores referentes a Saída Exportação, Ressarcimento Crédito, Outros Créditos, Outros Débitos,
Estorno de Débitos e Estorno Créditos poderão ser alterados
manualmente. O valor acumulado do IPI é gerado no campo Outros Débitos quando o campo Lançar Valor Acumul., da grade Impostos da tela Base imposto Liga Filial (Configuração de Impostos para a Filial) (F055PPF), estiver parametrizado com **O - Outros Débitos**.

Os campos Deduções 1 e Deduções 2 podem ser preenchidos
manualmente, lembrando que esses campos influenciam no resultado da apuração. O cálculo do IPI é baseado no total dos Créditos menos o total dos Débitos, sendo
que, quando esse cálculo gera um resultado credor o valor é gerado no campo Saldo
Credor. Quando isso ocorre, para o próximo período apurado o valor desse campo passa a ser
gerado no campo Saldo Período Anterior. Quando o resultado é devedor o valor é gerado no campo Imposto a Recolher.

Ao clicar no botão Processar a apuração do cálculo é gravada, com isso, ao
sair da tela e acessá-la novamente no mesmo período, os valores da última apuração
são demonstrados. Caso desejar apurar novamente, apresentará a mensagem: Imposto já apurado para este período. Sobrepor? Clicando em Não a apuração não é concluída, permitindo ao
usuário informar novos valores na apuração. Ao clicar no botão Sim as informações serão gravadas na apuração, onde
apresentará a mensagem: Atualização da apuração concluída com sucesso.

O processo de apuração poderá ser feito quantas vezes forem necessárias.

## Quando a Filial não for Totalizadora

As notas fiscais de entrada serão filtradas pelo módulo da transação COF ou COS, a Natureza de Operação da nota fiscal deve iniciar com 1, 2 ou 3. Quando no cadastro da filial em F070FEF o campo Considera NF Entrada de Serviço estiver com a opção S -
Sim as notas fiscais de entradas de serviços que possuírem transações de aplicação de operação igual a V - Serviços
e a espécie do documento for diferente de 01 serão consideradas na apuração. Caso contrário,
não serão consideradas.

As notas fiscais de saídas serão filtradas pelo módulo
VEF ou VES. As notas fiscais de saídas de serviços serão consideradas, quando aplicação
de operação da transação for igual a V - Serviços e a espécie do documento for
diferente de 01. Caso contrário, a rotina considerará essas notas
como **não serviço**.

## Quando a Filial for Totalizadora

Serão somadas todas as apurações da empresa para o mesmo
imposto, considerando em todos os campos a descrição Totalização das
Filiais. Com isso, será necessário efetuar as apurações do imposto para cada filial da empresa.

No campo Saldo Período Anterior será valor dos
Créditos do Contas Corrente de Imposto referente a última apuração do imposto.

## Quando for Nota Fiscal de Saída de Devolução

Quando a CFOP começar com **5** ou **6** e a aplicação da natureza de operação da transação for igual a **D-Devoluções** ou **A-Devoluções com Substituição Tributária**, a tela terá o seguinte comportamento:

Na coluna **Saída Nacional** será preenchido o valor do IPI quando:

* a nota fiscal de entrada possuir valor de IPI Creditado e a nota fiscal de saída de devolução possuir valor do IPI (Valor de IPI + Valor do IPI Presumido) e não possuir IPI Devolvido;
* a nota fiscal de entrada não possuir valor de IPI Creditado e a nota fiscal de saída de devolução possuir valor do IPI (Valor de IPI + Valor do IPI Presumido) e não possuir IPI Devolvido.

Na coluna **Estorno Créditos** será preenchido o valor do IPI Devolvido quando a nota fiscal de entrada possuir valor de IPI Creditado e a nota fiscal de saída de devolução não possuir valor do IPI (Valor de IPI + Valor do IPI Presumido) e possuir IPI Devolvido.

Na coluna **Estorno Débitos** será preenchido o valor do IPI quando a nota fiscal de entrada não possuir valor de IPI Creditado e a nota fiscal de saída de devolução possuir valor do IPI (Valor de IPI + Valor do IPI Presumido) e não possuir IPI Devolvido.

Na coluna **Outros Débitos** será preenchido o valor do IPI Presumido quando a nota fiscal de saída de devolução possuir IPI Presumido.

## Geração de títulos/guias de recolhimento por Detalhamento por Código de Arrecadação

Quando o IPI possuir detalhamento de operação da transação na guia **Detalhamento por Código de Arrecadação** da tela Configuração de Impostos para a Filial (F055PPF), a apuração do imposto **1 - IPI**gera um o título a pagar e/ou guia de recolhimento para cada detalhamento cadastrado. As informações são geradas de acordo com os filtros sobre os documentos fiscais de entrada e saída. Agrupando o valor de IPI, somando em caso de documento de saída (transação de venda) e subtraindo em caso de documento de entrada (transação de compra).

Quando o valor da apuração for positivo é gerada a guia e título correspondente. As configurações são agrupadas pela guia de recolhimento, ou seja, se possuir mais de uma transação configurada com o mesmo código de guia de recolhimento, elas são agrupadas para a geração. Este mesmo agrupamento é válido para os parâmetros da geração do título (fornecedor, transação e tipo de título), considerando ainda neste caso a separação pela guia de recolhimento.

No valor total das guias de recolhimento geradas a partir do detalhamento é subtraído o valor total a recolher indicado na apuração do imposto IPI e esta diferença positiva é gerada na guia de recolhimento e título a pagar para o IPI padrão (normal).

As notas fiscais com transações não parametrizadas na tela F055PPF terão seus valores somados para o código de arrecadação do próprio cadastro do imposto, ou seja:

* caso a transação 5353 não esteja parametrizada em F055PPF o sistema deverá totalizar o respectivo valor da nota fiscal para o código de arrecadação do vínculo do imposto a filial;
* caso o usuário opte por não cadastrar nenhum código de arrecadação na guia **Detalhamento por Código de Arrecadação** o valor das notas fiscais identificadas no período da apuração deverão ser somados para o código de arrecadação do imposto ligado a filial.

## Páginas relacionadas

* [IPI](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/impostos_ipi.htm)
* [Enquadramento e Situações Tributárias de IPI](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/enquadramento-de-ipi.htm)
* [CIOD033 - Carta de suspensão de IPI a ser encaminhada aos fornecedores](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/relatorios/declaracoes/ciod033.htm)
* [F051IMP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f051imp.htm)
* [F055PPF](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f055ppf.htm)
* [F661PAI](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f661pai.htm)
* [F070FEF](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070fef.htm)
