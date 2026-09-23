# Exemplo

> **Fonte:** Gross Up - Retenção de IRRF/PIS/COFINS/ISS- Fornecedor Exterior — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/regime-calculo-irrf-pis-cofins-iss-fe.htm#exemplo-calculo  
> **Trilha:** Segmentos > Compliance > Configurações para cálculos fiscais > Retenção  
> **Telas citadas:** F049TTR, F070EPF  
> **Identificadores de regras:** —

---
Abaixo segue um exemplo de cálculo a ser feito pelo sistema quando o fornecedor da Nota Fiscal de Entrada possuir moeda estrangeira (nesse caso Dólar). Como determinar o valor da base de cálculo para essa situação quando a cotação da moeda na baixa do título é menor que a cotação do segundo dia útil anterior?

Cenário

Lançamento de uma Nota Fiscal de Entrada, com valor de US$ 1.868,27 (cotação do dólar no dia da emissão: R$ 5,5709), totalizando R$ 10.407,95. Como o regime utilizado para o cálculo das retenções (IRRF/PIS/COFINS/ISS) está definido para Caixa (conforme parametrizado na tela F070EPF), esses títulos de retenção serão gerados no momento da baixa do Contas a Pagar.

Na data da baixa do título do fornecedor, em virtude de variação cambial, a cotação do dólar estava em R$ 5,5426.

Dois dias úteis anteriores a data da baixa, a cotação do dólar era de R$ 5,5537.

Nesse exemplo, o IRRF irá ser calculado convertendo o valor do título em dólares utilizando a maior cotação, ou seja, a cotação do 2º dia útil anterior a data da baixa do título, logo R$ 5,5537.

Assim, o valor em reais passa a ser de R$ 10.375,81 (1.868,27 × 5,5537).

Cálculo IRRF:

O IRRF é calculado aplicando-se a metodologia Gross-Up sobre o valor do título na data da baixa.

## Fórmula aplicada:

Valor na Baixa / (1 - Alíquota IRRF) × Alíquota IRRF

## Cálculo detalhado:

* Valor do título na baixa: R$ 10.375,81
* Alíquota do IRRF: 15% (0,15)
* Aplicando a fórmula: 10.375,81 / (1 - 0,15) × 0,15 = 10.375,81 / 0,85 × 0,15
* Base de cálculo: 10.375,81 / 0,85 = **12.206,84**
* Valor de IRRF retido: 12.206,84 x 0,15 = **R$ 1.831,03**

**Cálculo de PIS**

O PIS é calculado aplicando-se a metodologia Gross-Up sobre o valor já ajustado pelo IRRF, considerando também a soma das alíquotas de PIS e COFINS.

## Fórmula aplicada:

(Valor na Baixa / (1 - Alíquota IRRF)) / (1 - (Alíquota PIS + Alíquota COFINS)) × Alíquota PIS

## Cálculo detalhado:

* Valor do título na baixa: R$ 10.375,81
* Alíquota do IRRF: 15% (0,15)
* Alíquota do PIS: 1,65% (0,0165)
* Alíquota do COFINS: 7,6% (0,076)
* Soma PIS + COFINS: 0,0925
* Aplicando a fórmula: (10.375,81 / 0,85) / (1 - 0,0925) × 0,0165
* Base de cálculo: 12.206,84 / 0,9075 = **13.451,06**
* Valor de PIS retido: 13.451,06 x 0,0165 = **R$ 221,94**

**Cálculo de COFINS**

O COFINS segue a mesma metodologia do PIS, mudando apenas a alíquota final aplicada.

## Fórmula aplicada:

(Valor na Baixa / (1 - Alíquota IRRF)) / (1 - (Alíquota PIS + Alíquota COFINS)) × Alíquota COFINS

## Cálculo detalhado:

* Valor do título na baixa: R$ 10.375,81
* Alíquota do IRRF: 15% (0,15)
* Alíquota do PIS: 1,65% (0,0165)
* Alíquota do COFINS: 7,6% (0,076)
* Soma PIS + COFINS: 0,0925
* Aplicando a fórmula: (10.375,81 / 0,85) / (1 - 0,0925) × 0,076
* Base de cálculo: 12.206,84 / 0,9075 = **13.451,06**
* Valor de COFINS retido: 13.451,06 x 0,076 = **R$ 1.022,28**

**Importante**

O valor **0,0925** utilizado nos cálculos de PIS e COFINS representa o somatório das alíquotas destes dois impostos (COFINS 0,076 + PIS 0,0165), sendo necessário para aplicação correta da metodologia Gross-Up considerando ambos os tributos simultaneamente.

É necessário ter configurado corretamente os percentuais de PIS e COFINS na tela F049TTR.

## Páginas relacionadas

* [F070EPF](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070epf.htm)
* [F049TTR](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f049ttr.htm)
