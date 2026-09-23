# Exemplo:

> **Fonte:** Identificador de Regra — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_140mntvl01.htm  
> **Trilha:**   
> **Telas citadas:** —  
> **Identificadores de regras:** —

---
Cenário que a rotina será acionada e eliminará o cálculo do imposto personalizado:

O cálculo padrão do imposto do sistema utilizando "Base \* Alíquota" equivale a um imposto de R$ 0,003254, mas se via regra for alterado o cálculo do valor do imposto para ficar como R$ 0,01, quando não utilizado o identificador de regras para determinar que não será efetuado arredondamento do imposto no fechamento do documento, o valor de imposto definido na regra poderá ser perdido na execução da rotina de arredondamento.
