# Impacto de apuração do imposto

> **Fonte:** F661I12 - Resumo de Apuração do Imposto — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f661i12.htm  
> **Trilha:** Ajuda por telas > Controladoria > Gestão de Tributos > Operações e Cálculos Fiscais > Cálculos > Apuração  
> **Telas citadas:** —  
> **Identificadores de regras:** —

---
Com as transações de operações com álcool parametrizadas, o sistema identifica quanto do total do imposto a pagar é relativo à movimentações com álcool. Após separar as movimentações com álcool das demais, ele gera as guias de recolhimento conforme parametrizado para o Imposto apurado e para o Imposto Regime Especial.

**Exemplo do cálculo PIS, válido também para a COFINS:**

1. Total do PIS originado de Receitas de outras operações: R$ 30.000,00;
2. Total do PIS originado de Receitas de vendas de álcool: R$ 150.000,00;
3. Total de créditos do PIS de outras operações: R$ 12.000,00;
4. Total de créditos presumidos do PIS para operações com álcool: R$ 22.000,00.

**Apuração do PIS:**

1. Total da contribuição: R$ 180.000,00;
2. Total dos créditos: R$ 34.000,00;
3. Total a recolher: R$ 146.000,00.

**Supondo que as transações parametrizadas para as operações com álcool representem os itens 2 e 4 do cenário:**

* Total da contribuição do PIS para o álcool: item 2 - item 4 = 150.000,00 - 22.000,00 = R$ 128.000,00;
* Participação das operações do álcool sobre o total da contribuição (antes dos créditos) = 128.000,00 / (30.000,00 + 150.000,00) = 0,7111.

**Guias:**

* Guia com o código da receita 0906 = 146.000,00 \* 0,7111 = R$ 103.820,60;
* Guia com o código da receita 6912 = 146.000,00 - 103.820,60 = R$ 42,179,40.
