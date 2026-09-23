# Exemplo

> **Fonte:** F661I12 - Resumo de Apuração do Imposto — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f661i12.htm  
> **Trilha:** Ajuda por telas > Controladoria > Gestão de Tributos > Operações e Cálculos Fiscais > Cálculos > Apuração  
> **Telas citadas:** F661UCR  
> **Identificadores de regras:** —

---
Quando o parâmetro Sequenciamento dos créditos antigos baseado no período e tipo de crédito estiver selecionado, o sistema irá se comportar conforme abaixo:

Sequenciamento por período dos créditos (F661UCR)

![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/images/f661ucr_thumb_0_48.png)

Consulta dos créditos utilizados na apuração (F661I12)

![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/images/f661cre_thumb_0_48.png)

Baseado nas parametrizações realizadas na tela F661UCR, o sistema montará a seguinte lógica de utilização dos créditos:

1º - Mais antigo (01/2018..06/2018)

* 101

2º - Mês do cálculo (07/2018)

* 101

3º - Mais antigo (01/2018..06/2018)

* 105
* 102
* 103
* 104

4º - Mês do cálculo (07/2018)

* 102
* 103
* 104
* 105

## Páginas relacionadas

* [F661UCR](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f661ucr.htm)
