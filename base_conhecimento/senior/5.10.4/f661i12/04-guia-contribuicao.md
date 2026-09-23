# Guia Contribuição

> **Fonte:** F661I12 - Resumo de Apuração do Imposto — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f661i12.htm  
> **Trilha:** Ajuda por telas > Controladoria > Gestão de Tributos > Operações e Cálculos Fiscais > Cálculos > Apuração  
> **Telas citadas:** F055PPF, F070FEF, F661ARC  
> **Identificadores de regras:** —

---
### Cumulativo

Descrição (Contr. Soc)

Esse campo é gerado de acordo com o código (Lista 4.3.5 SPED PIS/PASEP/COFINS) de contribuição
cadastrada na tela F055PPF para os impostos do tipo "43 - PIS/PASEP Cumulativo (SPED)", "44 - COFINS Cumulativo (SPED)", "47 - PIS Regime Caixa" e "48 - COFINS Regime Caixa".

Cálculo da Contribuição Cumulativa apurada a Alíquota Básica

* Quando se tratar de uma nota fiscal/cupom fiscal/outros documentos, o regime de tributação do produto/serviço vinculado deverá ser Cumulativo. Já no caso de vendas de imóveis, o sistema assume como sendo especificamente do regime cumulativo;
* Também no item da nota fiscal/Cupom Fiscal/Outros documentos/Venda de Imóvel, a alíquota por percentual do imposto PIS/PASEP/COFINS deve ser 0,65%, 3% ou 4% e a Situação Tributário de PIS/COFINS do lançamento deve ser diferente de "02 - Alíquotas diferenciadas";
* O cálculo agrupa todos os valores do imposto nessa condição para o respectivo código de contribuição.

Observação

No cálculo dos impostos 41, 42, 43 e 44, caso a
filial possua o campo Operação Realizada, da tela
F070FEF,
preenchido, as alíquotas básicas de PIS/PASEP e COFINS cumulativos
serão 0,65% e 4%, respectivamente.

Cálculo da
Contribuição Cumulativa apurada a Alíquotas Diferenciadas

* Quando se tratar de uma nota fiscal/cupom fiscal/outros documentos, o regime de tributação do produto/serviço vinculado deverá ser Cumulativo. Já no caso de vendas de imóveis, o sistema assume como sendo especificamente do regime cumulativo;
* Também no item da nota fiscal/Cupom Fiscal/Outros documentos/Venda de Imóvel, a alíquota por percentual do imposto PIS/PASEP/COFINS deve ser diferente 0,65%, 3% ou 4% e a Situação Tributário de PIS/COFINS do lançamento deve ser igual "02 - Alíquotas diferenciadas";
* O cálculo agrupa todos os valores do imposto nessa condição para o respectivo código de contribuição.

Cálculo da Contribuição
Cumulativa apurada a alíquota por unidade de medida de produto

É verificado o cadastro do Produto/Serviço/Classificação Fiscal regime de tributação igual a cumulativo, no item
da nota fiscal/Cupom Fiscal/Outros documentos devem estar preenchidos os campos: Quantidade da base do PIS/PASEP por
faturamento, Alíquota por valor do PIS/PASEP Faturamento, Quantidade da base do COFINS por faturamento e Alíquota por
valor do COFINS Faturamento.

O
cálculo agrupa a apuração por alíquota, quando existe mais de uma alíquota o cálculo é quebrado em linhas, gerando
uma linha para cada alíquota diferente conforme o respectivo código de contribuição.

Cálculo da Contribuição
Apurada por Substituição Tributária

É verificado o cadastro do Produto/Serviço/Classificação Fiscal com regime de tributação igual a cumulativo. No item da nota fiscal, cupom fiscal ou outros documentos, devem estar preenchidos os campos: Situação Tributária do PIS/COFINS igual a "05 - Operação tributável por substituição tributária", Valor da base de substituição do PIS/PASEP e Valor da base de substituição do COFINS. Por fim, no cadastro do cliente, o campo Benefício Fiscal deve ser diferente de Zona Franca de Manaus e Zona Franca.

O
cálculo agrupa a apuração por alíquota, quando existe mais de uma alíquota o cálculo é quebrado em linhas, gerando
uma linha para cada alíquota diferente conforme o respectivo código de contribuição.

**Cálculo da Contribuição
Apurada por Substituição Tributária – Vendas à Zona Franca de Manaus**

 É verificado o cadastro do Produto/Serviço/Classificação Fiscal com regime de tributação igual a cumulativo. No item da nota fiscal, cupom fiscal ou outros documentos, devem estar preenchidos os campos: Situação Tributária do PIS/COFINS igual a "05 - Operação tributável por substituição tributária", Valor da base de substituição do PIS/PASEP e Valor da base de substituição do COFINS. Por fim, no cadastro do cliente, o campo Benefício Fiscal deve ser igual à Zona Franca de Manaus e Zona Franca.

O
cálculo agrupa a apuração por alíquota, quando existe mais de uma alíquota o cálculo é quebrado em linhas, gerando
uma linha para cada alíquota diferente conforme o respectivo código de contribuição.

Vlr. Cont.

Soma o total do imposto que consta no campo Vlr. Cont. da
guia Detalhamento, para o respectivo
código de contribuição.

Contribuição apurada de SCP -Incidência cumulativa É verificado no cadastro da filial (F070FEF), guia Impostos 2, se o campo CPF filial SCP está preenchido e se o campo gera SPED Contribuições está com N (Não). Na tela F055PPF, o código da contribuição 72 (Contribuição Apurada de SCP - incidência cumulativa) deve estar cadastrada para os tipos de imposto 43 e 44. No cálculo, a linha referente às contribuições 72 lista apenas os documentos fiscais relativos às filiais SCP.

O tratamento é válido para notas fiscais de venda, reduções Z e outros documentos de saída, os demais não foram alterados (Alíquota Básica, Diferenciada, Unidade de Medida e outras).

### Guia Detalhamento

Alíq. Imp.

É a alíquota que consta no item da nota fiscal/Cupom Fiscal/Outros documentos para o respectivo código de
contribuição.

Rec. Bru.

Resultado da multiplicação do preço unitário pela quantidade do produto agrupado para o respectivo código de
contribuição e alíquota.

Vlr. Bas. Cál.

Base de cálculo de PIS/COFINS que consta item da nota fiscal/Cupom Fiscal/Outros documentos agrupado
para o respectivo código de contribuição e alíquota.

Tot. Contr. Soc.

Resultado da multiplicação do campo Vlr. Bas. Cálc. com campo Alíq. Imp. agrupado para o respectivo
código de contribuição e alíquota.

Ajust. Acr.

Informar valores de Acréscimo ao imposto. Para buscar valores nesse campo deve ser informado um Dispositivo
Fiscal ou uma Forma de Busca de dados na guia Ajustes.

Ajust. Red.

Informar valores de Redução ao imposto. A busca desses valores ocorre através da
guia Ajustes onde
existe a opção de informar um Dispositivo Fiscal ou uma Forma de Busca de dados. Quando a devolução é gerada a partir de um título, este campo exibe o valor dos títulos de devolução.

Observação

* O campo Ajust. Red. buscará os valores referentes à devolução de venda do regime de tributação cumulativo;
* As
  notas fiscais de entrada do tipo 02 e 03 serão levadas em consideração, é verificado no cadastro do Produto/Serviço/Classificação
  Fiscal o regime de tributação igual a cumulativo;
* Os valores do imposto referente à devolução serão buscados dos campos: Valor Base PIS faturamento, Quantidade da
  Base PIS Faturamento, Alíquota PIS Faturamento, Percentual do PIS Faturamento, Valor do PIS Faturamento, Valor Base
  COFINS faturamento, Quantidade da Base COFINS Faturamento, Alíquota COFINS Faturamento, Percentual do COFINS
  Faturamento, Valor do COFINS Faturamento;
  + Para que o sistema busque informações nesses campos, é necessário ter cadastrado um dispositivo fiscal específico para devolução. A aplicação do
    dispositivo deverá ser 02, não estar associado a documento, ter mensagem de devolução e informar o respectivo código de
    ajuste para SPED PIS/COFINS.

Vlr. Dif.

O sistema irá buscar o valor da contribuição a diferir no período, referente às receitas ainda
não recebidas decorrentes da celebração de contratos com pessoa jurídica de direito público, empresa pública,
sociedade de economia mista ou suas subsidiárias, relativos à construção por empreitada ou a fornecimento a preço
predeterminado de bens ou serviços (parágrafo único e no caput do art. 7º da Lei nº 9.718, de 1998).

Vlr. Dif. Ant.

O sistema irá buscar o valor da contribuição diferida em períodos anteriores,
adicionada a este período de escrituração, referente às receitas diferidas recebidas no mês da escrituração.

Vlr. Cont.

É a busca do valor total da contribuição do período da escrituração para o respectivo código de contribuição
e alíquota, devendo ser igual à Tot. Contr. Soc. mais Ajust. Acr. menos Ajust. Red. menos Vlr. Dif. mais Vlr. Dif. Ant..

#### Não Acumulativo

Descrição (Contr. Soc)

Esse campo é gerado de acordo com o código (Lista 4.3.5 SPED PIS/COFINS) de contribuição
cadastrada na tela F055PPF para os impostos do Tipo 41 (PIS Não-Cumulativo (SPED)) e
42 (COFINS
Não-Cumulativo (SPED)).

Cálculo da Contribuição Não-Cumulativa apurada a Alíquota Básica

É verificado o cadastro do Produto/Serviço/Classificação Fiscal regime de tributação igual a não-cumulativo, no item da nota fiscal/Cupom Fiscal/Outros documentos a alíquota por percentual do imposto PIS/COFINS deve ser 1,65% ou 7,6% e a Situação Tributário de PIS/COFINS do lançamento deve ser diferente de "02 - Alíquotas diferenciadas".

O cálculo agrupa todos os valores do imposto nessa condição para o respectivo código de contribuição.

Cálculo da Contribuição Não-Cumulativa apurada a Alíquotas Diferenciadas

É verificado o cadastro do Produto/Serviço/Classificação Fiscal regime de tributação igual a cumulativo, no item da nota fiscal/Cupom Fiscal/Outros documentos a alíquota do imposto deve ser diferente de 1,65%, 7,6% ou a Situação Tributário de PIS/COFINS do lançamento deve ser igual a "02 - Alíquotas diferenciadas".

O
cálculo agrupa a apuração dos valores por alíquota, quando existe mais de uma alíquota o cálculo é quebrado em
linhas, gerando uma linha para cada alíquota diferente conforme o respectivo código de contribuição.

Cálculo da
Contribuição Não-Cumulativa apurada a alíquota por unidade de medida de produto

É verificado o cadastro do Produto/Serviço/Classificação Fiscal regime de tributação igual a não-cumulativo, no
item da nota fiscal/Cupom Fiscal/Outros documentos devem estar preenchidos os campos: Quantidade da base do PIS por
faturamento, Alíquota por valor do PIS Faturamento, Quantidade da base do COFINS por faturamento e Alíquota por
valor do COFINS Faturamento.

O cálculo agrupa a apuração por alíquota, quando existe mais de uma alíquota o cálculo é quebrado em linhas, gerando
uma linha para cada alíquota diferente conforme o respectivo código de contribuição.

Cálculo da Contribuição
Apurada por Substituição Tributária

É verificado o cadastro do Produto/Serviço/Classificação Fiscal com regime de tributação igual a cumulativo. No item da nota fiscal, cupom fiscal ou outros documentos, devem estar preenchidos os campos: Situação Tributária do PIS/COFINS igual a "05 - Operação tributável por substituição tributária", Valor da base de substituição do PIS/PASEP e Valor da base de substituição do COFINS. Por fim, no cadastro do cliente, o campo Benefício Fiscal deve ser diferente de Zona Franca de Manaus e Zona Franca.

O cálculo agrupa a apuração por alíquota, quando existe mais de uma alíquota o cálculo é quebrado em linhas, gerando
uma linha para cada alíquota diferente conforme o respectivo código de contribuição.

Cálculo da Contribuição
Apurada por Substituição Tributária – Vendas à Zona Franca de Manaus

É verificado o cadastro do Produto/Serviço/Classificação Fiscal com regime de tributação igual a cumulativo. No item da nota fiscal, cupom fiscal ou outros documentos, devem estar preenchidos os campos: Situação Tributária do PIS/COFINS igual a "05 - Operação tributável por substituição tributária", Valor da base de substituição do PIS/PASEP e Valor da base de substituição do COFINS. Por fim, no cadastro do cliente, o campo Benefício Fiscal deve ser igual à Zona Franca de Manaus e Zona Franca.

O
cálculo agrupa a apuração por alíquota, quando existe mais de uma alíquota o cálculo é quebrado em linhas, gerando
uma linha para cada alíquota diferente conforme o respectivo código de contribuição.

Vlr. Cont.

Soma do total do imposto que consta no campo Vlr. Cont. da
guia de Detalhamento para o respectivo código de
contribuição. Contribuição apurada de SCP -Incidência não cumulativa É verificado no cadastro da filial (F070FEF), guia Impostos 2, se o campo CPF filial SCP está preenchido e se o campo gera SPED Contribuições está com N (Não). Na tela F055PPF, o código da contribuição 71 (Contribuição Apurada de SCP - incidência não cumulativa) deve estar cadastrado para os tipos de impostos 41 e 42.

No cálculo, a linha referente às contribuições 71 lista apenas os documentos fiscais relativos às filiais SCP. O Tratamento é válido para notas fiscais de venda, reduções Z e outros documentos de saída, os demais não foram alterados (Alíquota Básica, Diferenciada, Unidade de Medida e outras).

#### Detalhamento

Alíq. Imp.

É a alíquota que consta no item da nota fiscal/Cupom Fiscal/Outros documentos para o respectivo código de
contribuição.

Rec. Bru.

Resultado da multiplicação do preço unitário pela quantidade do produto agrupado para o respectivo código de
contribuição e alíquota.

Vlr. Bas. Cál.

Base de cálculo de PIS/COFINS que consta item da nota fiscal/Cupom Fiscal/Outros documentos agrupado
para o respectivo código de contribuição e alíquota.

Acrésc. da Base

Totalizador dos valores informados na tela acessada pelo botão Ajustes Base.

Reduções da Base

Totalizador dos valores informados na tela acessada pelo botão Ajustes Base.

Base após Ajustes

Totalizador dos valores informados na tela acessada pelo botão Ajustes Base.

Tot. Contr. Soc.

Resultado da multiplicação do campo Vlr. Bas. Cálc. pelo campo Alíq. Imp. Agrupado para o respectivo
código de contribuição e alíquota.

Ajust. Acr.

Informar valores de Acréscimo ao imposto. Para buscar valores nesse campo deve ser informado um Dispositivo
Fiscal ou uma Forma de Busca de dados na guia Ajustes.

Ajust. Red.

Informar valores de Redução ao imposto, a busca desses valores ocorre através da
guia de Ajustes onde
existe a opção de informar um Dispositivo Fiscal ou uma Forma de Busca de dados. As
notas fiscais de entrada do tipo 02 e 03 serão levadas em consideração, é verificado no cadastro do Produto/Serviço/Classificação
Fiscal o regime de tributação igual não cumulativo.

Nas informações complementares da transação deve ser informada, no campo Crédito do detalhamento a base de
cálculo do crédito com o código 12. As operações de Devolução de Vendas, no regime de incidência não cumulativo, correspondem a hipóteses de
crédito, devendo ser escrituradas com os CFOP correspondentes em C170 (no caso de escrituração individualizada dos
créditos por documento fiscal) ou nos registros C191/C195 (no caso de escrituração consolidada dos créditos.

Vlr. Dif.

O sistema irá buscar o valor da contribuição a diferir no período, referente às receitas ainda
não recebidas decorrentes da celebração de contratos com pessoa jurídica de direito público, empresa pública,
sociedade de economia mista ou suas subsidiárias, relativos à construção por empreitada ou a fornecimento a preço
predeterminado de bens ou serviços (parágrafo único e no caput do art. 7º da Lei nº 9.718, de 1998).

Vlr. Dif. Ant.

O sistema irá buscar o valor da contribuição diferida em períodos anteriores,
adicionada a este período de escrituração, referente às receitas diferidas recebidas no mês da escrituração.

Vlr. Cont.

É o valor total da contribuição do período da escrituração para o respectivo código de contribuição e
alíquota, devendo ser igual à Tot. Contr. Soc. mais Ajust. Acr. menos Ajust. Red. menos Vlr. Dif. mais Vlr.
Dif. Ant..

### Botões

**Ajustes**

Os dispositivos e forma de busca de dados tem a função de informar do que se tratam os valores informados na tela de
cálculo. Os dispositivos fiscais que tem no campo Associar a Documento Fiscal que são igual a "S -Sim" e foram a associados nas
notas fiscais com valor de ajuste, este valor será carregado automaticamente ao ser informado para a linha que esta
posicionado.

**Exemplo:** se houver valor para a apuração do Cumulativo na linha Contribuição Cumulativa Apurada a alíquota
básica e estiver posicionado na guia Ajustes os campos de Dispositivos e Formas de Busca de dados serão
referente a esta linha. Ou seja, a guia de Ajustes é válida para cada linha da guia Descrição (Contr. Soc.).

**Ajustes Base**

Ao clicar no botão será aberta a tela Ajustes da base de cálculo das contribuições (F661ARC), que permite ao usuário inserir, alterar ou consultar os acréscimos e reduções da base de cálculo dos impostos PIS/COFINS.

## Páginas relacionadas

* [F055PPF](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f055ppf.htm)
* [F070FEF](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070fef.htm)
* [F661ARC](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f661arc.htm)
