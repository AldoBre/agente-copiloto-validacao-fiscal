# PIS

> **Fonte:** F001TCP - Transações de Compras — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f001tcp.htm  
> **Trilha:** Ajuda por telas > Cadastros > Transações > Parâmetros por Gestão > Compras  
> **Telas citadas:** E440PCD, F000INE, F019TIR, F440GNE  
> **Identificadores de regras:** —

---
Recupera PIS

Indicativo se a transação recupera o PIS.

Sit.Trib.PIS

Código de situação tributária de PIS.

Calcula PIS Importação

Indicativo se a transação Calcula PIS importação a recuperar em nota fiscal de entrada.

Encargos Base PIS

Indicativo se o valor dos Encargos deve ser considerado na base de PIS.

Outras Despesas Base PIS

Indicativo se o valor de Outras Despesas deve ser considerado na base de PIS.

Arredondamento Base PIS

Indicativo se o valor do Arredondamento deve ser considerado na base de PIS.

IPI Base PIS

Indicativo se o valor do IPI deve ser considerado na base de PIS.

Frete Base PIS

Indicativo se o valor do Frete deve ser considerado na base de PIS.

Seguro Base PIS

Indicativo se o valor do Seguro deve ser considerado na base de PIS.

Embalagem Base PIS

Indicativo se o valor da Embalagem deve ser considerado na base de PIS.

ICMS Subst. base de PIS a recuperar

Indicativo se considera o ICMS Substituto na base de PIS a recuperar.

Subtrai IPI Pres. Base PIS

Indica se o valor do IPI Presumido será subtraído da base cálculo do PIS a recuperar das notas fiscais de entrada (tipos 1 - NF Entrada, 7 - NF Geração Manual, 8 - NF Frete/Serviços Agregados e 11 - Transferência entre Empresas/Filiais) e saída (tipo 2 - Devolução).

ICMS desonerado base PIS

Indicativo de como a transações considera o ICMS desonerado na base do PIS. Possui as seguintes opções:

Outras Destacada Base PIS

Indicativo se o valor do Outras Despesas Destacadas deve ser considerado na base de
PIS.

Frete Destacado Base PIS

Indicativo se o valor do Frete Destacado deve ser considerado na base de PIS.

Frete Importação Base PIS

Indicativo se o valor do Frete de Importação deve ser considerado na base de PIS.

Seguro Importação Base PIS

Indicativo se o valor de Seguro de Importação deve ser considerado na base de PIS.

Outras Despesas Importação Base PIS

Indicativo se o valor de Outras Despesas de Importação deve ser considerado na base de PIS.

Desconta ICMS da base do PIS

Indica se o ICMS deve ser descontado no cálculo de PIS. Por não haver uma legislação clara sobre o tema, o cliente pode definir se deseja ou não descontar os valores do DIFAL da base de cálculo (juntamente com o valor do ICMS da nota fiscal), conforme as seguintes opções:

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

Nesse parâmetro, quando lê-se"antes redução" ou "após redução" isto refere-se à redução que será/foi aplicada na base do PIS. Essa redução é referente ao cadastro de Reduções e Acréscimos de bases de Cálculos de Impostos - Por Estado (F019TIR) do tipo de imposto reduzido "41 - PIS Não Cumulativo".

Importante

O valor do DIFAL, presente nas opções S - Descontar ICMS Normal + DIFAL antes redução e R - Descontar ICMS Normal + DIFAL após redução, é referente aos campos IcmVor (ICMS Partilha UF Remetente) ou IcmVde (ICMS Partilha UF Destinatário). O campo VlrDfa (Diferencial de Alíquota), por sua vez, não faz parte do cálculo.

Des. Val do ICMS do item ligado na base do PIS

Desconta o valor do ICMS do item ligado (através dos campos E440PCD.SnfNfr, E440PCD.ForNfr, E440PCD.NumNfr e E440PCD.SeqIpr). Essa ligação é feita manualmente somente através das telas F440GNE e F000INE nos itens de produtos. Para que o valor seja descontado é necessário que a configuração Desconta ICMS da base do PIS esteja diferente de "N - Não descontar".

## Páginas relacionadas

* [processo](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/manuais_processos/suprimentos/reducao-pis-cofins.htm)
* [F440GNE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f440gne.htm)
* [F000INE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f000ine.htm)
