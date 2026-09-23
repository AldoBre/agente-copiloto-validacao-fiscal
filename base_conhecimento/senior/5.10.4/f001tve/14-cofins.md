# COFINS

> **Fonte:** F001TVE - Transações de Vendas — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f001tve.htm  
> **Trilha:** Ajuda por telas > Cadastros > Transações > Parâmetros por Gestão  
> **Telas citadas:** E019RET, E140PVD, F019TIR, F140GNF, F140PRE, F660NFV  
> **Identificadores de regras:** —

---
Sit. Trib. COFINS  
Código de situação tributária de COFINS.

Tributa COFINS Faturamento

Indicativo se tributa COFINS faturamento.

Valor Mínimo Cofins Retido

Valor mínimo do COFINS Retido considerado na Nota Fiscal de Saída. Caso este campo esteja informado e o cliente referente à nota fiscal estiver configurado para utilizar valor mínimo de retenção, o sistema irá verificar este valor para efetuar a retenção ou não do imposto por documento.  

Ou seja, caso o valor retido do imposto calculado na nota seja menor que o valor definido neste campo, no fechamento da nota fiscal o imposto será zerado e não haverá acúmulo na tabela de Controle de Retenção de Impostos (E019RET) para considerar nas próximas notas.

Outras Destacadas Base COFINS

Indicativo se o valor de outras despesas destacadas será considerado na base de
COFINS.

Arredondamento Base COFINS

Indicativo se o valor de encargos será considerado na base de COFINS.

Subtrai IPI Pres. Base COFINS

Indica se o valor do IPI Presumido será subtraído da base cálculo do COFINS a recuperar das notas fiscais de entrada (tipos 1 - NF Entrada, 7 - NF Geração Manual, 8 - NF Frete/Serviços Agregados e 11 - Transferência entre Empresas/Filiais) e saída (tipo 2 - Devolução).

ICMS desonerado base COFINS

Indicativo de como a transações considera o ICMS desonerado na base do COFINS. Possui as seguintes opções:

* - (Subtrair): indica que o valor do ICMS desonerado é subtraído da base de cálculo do imposto;
* + (Adicionar): indica que o valor do ICMS desonerado é somado na base do imposto;
* N (Nenhum): indica que o sistema não altera a base do imposto relacionado, ou seja, não adiciona nem subtrai o ICMS desonerado do imposto.

ICMS Subst. Base COFINS

Indicativo se o valor de ICMS substituto será considerado na base de
COFINS.

Embalagem Base COFINS

Indicativo se o valor de embalagem será considerado na base de
COFINS.

Seguro Base COFINS  
Indicativo se o valor de seguro será considerado na base de
COFINS.

Frete Base COFINS  
Indicativo se o valor de frete será considerado na base de
COFINS.

IPI Base COFINS  
Indicativo se o valor de IPI será considerado na base de
COFINS.

COFINS como despesa acessória em devoluções

Indica se o valor de COFINS deve ser considerados na devolução de uma nota fiscal de entrada.  

Este parâmetro é considerado ao realizar a devolução de uma nota fiscal de entrada na tela Preparação da Nota Fiscal de Saída (F140PRE). Ou seja, quando este campo estiver parametrizado com Sim, o valor de COFINS não é calculado e somado ao valor líquido da nota fiscal.

Desconta ICMS da base da COFINS

Indica se o ICMS deve ser descontado no cálculo da COFINS. Essa definição éaplicada somente aos cálculos de PIS e COFINS de Faturamento/Recuperar. Por nãohaver uma legislação clara sobre o tema, o cliente pode definir se deseja ou não descontar os valores do DIFAL da base de cálculo (juntamente com o valor do ICMS danota fiscal), conforme as seguintes opções:

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

Nesse parâmetro, quando lê-se"antes redução" ou "após redução" isto refere-se à redução que será/foi aplicada na base do COFINS. Essa redução é referente ao cadastro de Reduções e Acréscimos de bases de Cálculos de Impostos - Por Estado (F019TIR) do tipo de imposto reduzido "42 - COFINS Não Cumulativo".

Desconta ISS da base da COFINS

Indica se o ISS deve ser descontado no cálculo da COFINS. Essa definição é aplicadasomente aos cálculos de PIS e COFINS de Faturamento e Recuperar.

**Observação**

Nas opções de desconto antes da redução, o sistema primeiro desconta os impostos da opção selecionada na base do COFINS e depois desconta outras reduções/acréscimos de impostos.  
Nas opções de desconto após a redução, o sistema primeiro desconta outras reduções/acréscimos de impostos, conforme abaixo:

1. Dependendo da configuração do campo ICMS Desonerado Base COFINS, presente na transação, o sistema efetua o desconto ou acréscimo do ICMS Desonerado na base do COFINS. Essa situação ocorre apenas para o COFINS Faturamento;
2. Caso houver um código de redução de imposto com tipo de imposto “COFINS Não Cumulativo (SPED)”, o sistema descontará da base do COFINS, o percentual da Entrada ou Saída para Contribuinte. Ocorre apenas para o COFINS Faturamento/A Recuperar.

O COFINS Retido não possui diferença nos cálculos quando configurado com antes ou após redução.  
Além disso, destacamos que o parâmetro global DesIcmBpc indica quais bases de COFINS receberão o desconto de ICMS.

Des. Val do ICMS do item ligado na base do COFINS

Desconta o valor do ICMS do item ligado (através dos campos E140PVD.SnfNfr, E140PVD.NumNfr e E140PVD.SeqIpr). Essa ligação é feita somente através das telas F140GNF (Botão Dados Comp.) e F140PRE (Ligação é feita de forma automática se a nota for criada via Nota Saída). Para que o valor seja descontado é necessário que a configuração Desconta ICMS da base do COFINS  esteja diferente de "N - Não descontar".

Natureza Receita COFINS

Informa a natureza da receita do COFINS de acordo com o CST informado para a transação. O código é exigido na escrituração fiscal do SPED Contribuições e deve ser utilizado de acordo com os códigos existentes nas tabelas da Receita Federal. Para mais informações, consulte a ajuda da tela Notas Fiscais de Saída (F660NFV), guia Itens.

## Páginas relacionadas

* [F140PRE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f140pre.htm)
* [F140GNF](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f140gnf.htm)
* [F660NFV](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f660nfv.htm)
