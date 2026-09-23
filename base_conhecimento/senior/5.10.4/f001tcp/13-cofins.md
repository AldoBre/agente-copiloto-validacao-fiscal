# COFINS

> **Fonte:** F001TCP - Transações de Compras — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f001tcp.htm  
> **Trilha:** Ajuda por telas > Cadastros > Transações > Parâmetros por Gestão > Compras  
> **Telas citadas:** E440PCD, F000INE, F019TIR, F440GNE  
> **Identificadores de regras:** —

---
Recupera Cofins

Indicativo se a transação recupera Cofins.

Sit.Trib.Cofins

Código de situação tributária de COFINS.

Calcula Cofins Importação

Indicativo se a transação Calcula COFINS importação a recuperar em nota fiscal de entrada.

Arredondamento Base Cofins

Indicativo se o valor do Arredondamento deve ser considerado na base de Cofins.

Outras Despesas Base Cofins

Indicativo se o valor de Outras Despesas deve ser considerado na base de Cofins.

Encargos Base Cofins

Indicativo se o valor dos Encargos deve ser considerado na base de Cofins.

Subtrai IPI Pres. Base Cofins

Indica se o valor do IPI Presumido será subtraído da base cálculo do COFINS a recuperar das notas fiscais de entrada (tipos 1 - NF Entrada, 7 - NF Geração Manual, 8 - NF Frete/Serviços Agregados e 11 - Transferência entre Empresas/Filiais) e saída (tipo 2 - Devolução).

ICMS desonerado base COFINS

Indicativo de como a transações considera o ICMS desonerado na base do COFINS. Possui as seguintes opções:

* - (Subtrair): indica que o valor do ICMS desonerado é subtraído da base de cálculo do imposto;
* + (Adicionar): indica que o valor do ICMS desonerado é somado na base do imposto;
* N (Nenhum): indica que o sistema não altera a base do imposto relacionado, ou seja, não adiciona nem subtrai o ICMS desonerado do imposto.

ICMS Subst. base de Cofins a recuperar

Indicativo se deve ser considerado o ICMS Substituído na base de Cofins a recuperar.

Embalagem Base Cofins

Indicativo se a valor da Embalagem deve ser considerado na base de Cofins.

Seguro Base Cofins

Indicativo se o valor Seguro deve ser considerado na base de Cofins.

Frete Base Cofins

Indicativo se o valor Frete deve ser considerado na base de Cofins.

IPI Base Cofins

Indicativo se o valor do IPI deve ser considerado na base de Cofins.

Frete Destacado Base Cofins

Indicativo se o valor do Frete Destacado deve ser considerado na base de Cofins.

Outras Destacadas Base Cofins

Indicativo se o valor de Outras Despesas Destacadas deve ser considerado na base de
Cofins.

Frete Importação Base COFINS

Indicativo se o valor do Frete de Importação deve ser considerado na base de COFINS.

Seguro Importação Base COFINS

Indicativo se o valor de Seguro de Importação deve ser considerado na base de COFINS.

Outras Despesas Importação Base COFINS

Indicativo se o valor de Outras Despesas de Importação deve ser considerado na base de COFINS.

Desconta ICMS da base da COFINS

Indica se o ICMS deve ser descontado no cálculo da COFINS. Essa definição é aplicada somente aos cálculos de PIS e COFINS de Faturamento/Recuperar. Por não haver uma legislação clara sobre o tema, o cliente pode definir se deseja ou não descontar os valores do DIFAL da base de cálculo (juntamente com o valor do ICMS da nota fiscal), conforme as seguintes opções:

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

Veja mais detalhes na documentação do processo. Essa definição é aplicada somente aos cálculos de PIS e COFINS de Faturamento/Recuperar.

Nesse parâmetro, quando lê-se"antes redução" ou "após redução" isto refere-se à redução que será/foi aplicada na base do COFINS. Essa redução é referente ao cadastro de Reduções e Acréscimos de bases de Cálculos de Impostos - Por Estado (F019TIR) do tipo de imposto reduzido "42 - COFINS Não Cumulativo".

Importante

O valor do DIFAL, presente nas opções S - Descontar ICMS Normal + DIFAL antes redução e R - Descontar ICMS Normal + DIFAL após redução, é referente aos campos IcmVor (ICMS Partilha UF Remetente) ou IcmVde (ICMS Partilha UF Destinatário). O campo VlrDfa (Diferencial de Alíquota), por sua vez, não faz parte do cálculo.

% Diário da Adm. Temp. do AFRMM

Neste campo é definido o percentual diário que será utilizado do valor da base original para formar a base de cálculo do imposto, visando atender o processo de Admissão Temporária para produtos importados.

Des. Val do ICMS do item ligado na base do COFINS

Desconta o valor do ICMS do item ligado (através dos campos E440PCD.SnfNfr, E440PCD.ForNfr, E440PCD.NumNfr e E440PCD.SeqIpr). Essa ligação é feita manualmente somente através das telas F440GNE e F000INE nos itens de produtos. Para que o valor seja descontado é necessário que a configuração Desconta ICMS da base do COFINS esteja diferente de "N - Não descontar".

## Páginas relacionadas

* [processo](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/manuais_processos/suprimentos/reducao-pis-cofins.htm)
* [Admissão Temporária](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/manuais_processos/suprimentos/admissao-temporaria/processo-admissao-temporaria.htm)
* [F440GNE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f440gne.htm)
* [F000INE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f000ine.htm)
