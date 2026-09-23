# PIS

> **Fonte:** F001TVE - Transações de Vendas — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f001tve.htm  
> **Trilha:** Ajuda por telas > Cadastros > Transações > Parâmetros por Gestão  
> **Telas citadas:** E019RET, E140PVD, F019TIR, F140GNF, F140PRE, F660NFV  
> **Identificadores de regras:** —

---
Tributa PIS Faturamento

 Indicativo se tributa PIS faturamento.

Valor Mínimo PIS Retido

Valor mínimo do PIS Retido considerado na Nota Fiscal de Saída. Caso este campo esteja informado e o cliente referente à nota fiscal estiver configurado para utilizar valor mínimo de retenção, o sistema irá verificar este valor para efetuar a retenção ou não do imposto por documento.  

Caso o valor retido do imposto calculado na nota seja menor que o valor definido neste campo, no fechamento da nota fiscal o imposto será zerado e não haverá acúmulo na tabela de Controle de Retenção de Impostos (E019RET) para considerar nas próximas notas.

Sit. Trib. PIS  
 Código da situação tributário de PIS.

Encargos Base PIS

 Indicativo se o valor de encargos será considerado na base de PIS.

Outras Despesas Base PIS

 Indicativo se o valor de outras despesas será considerado na base de PIS.

Arredondamento Base PIS

Indicativo se o valor de Arredondamento será considerado na base de PIS.

Outras Destacadas Base PIS  
 Indicativo se o valor de Outras Despesas Destacadas será considerado na base de PIS.

IPI Base PIS

 Indicativo se o valor de IPI será considerado na base de PIS.

Frete Base PIS

 Indicativo se o valor de frete será considerado na base de PIS.

Seguro Base PIS

Indicativo se o valor de seguro será considerado na base de PIS.

Embalagem Base PIS

 Indicativo se o valor de embalagem será considerado na base de PIS.

ICMS Subst. Base PIS

 Indicativo se o valor de ICMS substituto será considerado na base de PIS.

Subtrai IPI Pres. Base PIS

 Indica se o valor do IPI Presumido será subtraído da base cálculo do PIS a recuperar das notas fiscais de entrada (tipos 1 - NF Entrada, 7 - NF Geração Manual, 8 - NF Frete/Serviços Agregados e 11 - Transferência entre Empresas/Filiais) e saída (tipo 2 - Devolução).

ICMS desonerado base PIS

 Indicativo de como a transações considera o ICMS desonerado na base do PIS. Possui as seguintes opções:

* - (Subtrair): indica que o valor do ICMS desonerado é subtraído da base de cálculo do imposto;
* + (Adicionar): indica que o valor do ICMS desonerado é somado na base do imposto;
* N (Nenhum): indica que o sistema não altera a base do imposto relacionado, ou seja, não adiciona nem subtrai o ICMS desonerado do imposto.

PIS como despesa acessória em devoluções

Indica se o valor de PIS deve ser considerados na devolução de uma nota fiscal de entrada.  

Este parâmetro é considerado ao realizar a devolução de uma nota fiscal de entrada na tela Preparação da Nota Fiscal de Saída (F140PRE). Ou seja, quando este campo estiver parametrizado com Sim, o valor de PIS não é calculado e somado ao valor líquido da nota fiscal.

Desconta ICMS da base do PIS

Indica se o ICMS deve ser descontado no cálculo do PIS. Por não haver uma legislação clara sobre o tema, o cliente pode definir se deseja ou não descontar os valores do DIFAL da base de cálculo (juntamente com o valor do ICMS da nota fiscal), conforme as seguintes opções:

* U - Descontar ICMS Normal antes redução;
* S - Descontar ICMS Normal + DIFAL antes redução;
* T - Descontar ICMS Normal após redução;
* R - Descontar ICMS Normal + DIFAL após redução;
* O - Descontar ICMS+ FCP Normal antes redução;
* P - Descontar ICMS + FCP Normal + DIFAL + FCP DIFAL antes redução;
* Q - Descontar ICMS + FCP Normal após redução;
* V - Descontar ICMS + FCP Normal + DIFAL + FCP DIFAL após redução;
* N - Não descontar;

**Observação**

* Nas opções de desconto antes da redução, o sistema primeiro desconta os impostos da opção selecionada na base do PIS e depois desconta outras reduções/acréscimos de impostos.  
   Nas opções de desconto após a redução, o sistema primeiro desconta outras reduções/acréscimos de impostos, conforme abaixo:

1. Dependendo da configuração do campo ICMS Desonerado Base Pis, presente na transação, o sistema efetua o desconto ou acréscimo do ICMS Desonerado na base do PIS. Essa situação ocorre apenas para o Pis Faturamento;
2. Caso houver um código de redução de imposto com tipo de imposto "PIS Não Cumulativo (SPED)", o sistema descontará da base do PIS o percentual da Entrada ou Saída para Contribuinte. Isso ocorre apenas para o PIS Faturamento/A Recuperar;

O PIS Retido não possui diferença nos cálculos quando configurado antes ou após redução.
Além disso, destacamos que o parâmetro global DesIcmBpc indica quais bases de PIS/COFINS receberão o desconto de ICMS.

* Nesse parâmetro, quando lê-se "antes redução" ou "após redução" isto refere-se à redução que será/foi aplicada na base do PIS. Essa redução é referente ao cadastro de Reduções e Acréscimos de bases de Cálculos de Impostos - Por Estado (F019TIR) do tipo de imposto reduzido "41 - PIS Não Cumulativo".

Desconta ISS da base do PIS

Indica se o ISS deve ser descontado no cálculo de PIS. Essa definição é aplicada somente aos cálculos de PIS e COFINS de Faturamento e Recuperar.

Des. Val do ICMS do item ligado na base do PIS

Desconta o valor do ICMS do item ligado (através dos campos E140PVD.SnfNfr, E140PVD.NumNfr e E140PVD.SeqIpr). Essa ligação é feita somente através das telas F140GNF (Botão Dados Comp.) e F140PRE (Ligação é feita de forma automática se a nota for criada via Nota Saída). Para que o valor seja descontado é necessário que a configuração Desconta ICMS da base do PIS esteja diferente de "N - Não descontar".

Natureza Receita PIS

Informa a natureza da receita do PIS de acordo com o CST informado para a transação. O código é exigido na escrituração fiscal do SPED Contribuições e deve ser utilizado de acordo com os códigos existentes nas tabelas da Receita Federal. Para mais informações, consulte a ajuda da tela Notas Fiscais de Saída (F660NFV), guia Itens.

## Páginas relacionadas

* [F140PRE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f140pre.htm)
* [DesIcmBpc](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#DesIcmBpc)
* [F019TIR](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f019tir.htm)
* [F140GNF](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f140gnf.htm)
* [F660NFV](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f660nfv.htm)
