# Exemplos

> **Fonte:** F661PAI - Apuração dos Impostos — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f661pai.htm  
> **Trilha:** Ajuda por telas > Controladoria > Gestão de Tributos > Operações e Cálculos Fiscais > Cálculos  
> **Telas citadas:** F055PPF  
> **Identificadores de regras:** —

---
1. Imposto do tipo 02 - ICMS. Neste é possível ligar um imposto do tipo 03 -
   ICMS Diferencial de Alíquotas. Com isso, ao mostrar os impostos nesta tela, demonstrará somente o imposto do
   tipo 02 - ICMS, porém, a tela referente a apuração deste imposto também
   calculará o imposto do tipo 03 - ICMS Diferencial de Alíquotas.  

   Referente ao período e tipo de período, eles serão demonstrados conforme a parametrização de cada imposto na filial em Configuração de Impostos para a Filial (F055PPF)
2. Para o imposto do tipo 11 - IRRF foi configurado como período Q (Quinzenal). Ao demonstrá-lo e selecioná-lo nesta tela, o campo Período será habilitado para
   informar o período (1ª ou 2ª) e o campo Tipo Período ficará com a descrição
   Quinzenal
3. Serão consideradas somente as configurações (F055PPF) feitas com a maior data em comum, que sejam menores que a data de apuração:

## Produtos - Datas

* 1101 - 01/08/2017
* 1102 - 01/08/2017
* 1103 - 01/09/2017
* 1101 - 01/11/2017

Apuração 01/08/2017: vai considerar os produtos 1101 e 1102  
Apuração 01/12/2017: vai considerar o produto 1101

Quando o imposto estiver com o período "M - Mensal", esses campos estarão
desabilitados, não permitindo alterar nenhum dado.

## Páginas relacionadas

* [F055PPF](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f055ppf.htm)
