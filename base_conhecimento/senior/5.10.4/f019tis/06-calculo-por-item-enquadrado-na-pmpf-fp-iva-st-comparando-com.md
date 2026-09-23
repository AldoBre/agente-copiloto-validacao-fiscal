# Cálculo por item enquadrado na PMPF/FP/IVA ST comparando com PMC | Critério 6

> **Fonte:** F019TIS - Tipos Substituições Impostos / Modalidade Base Cálculo / Antecipação - Por Estado — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f019tis.htm  
> **Trilha:** Ajuda por telas > Cadastros > Mercado e Suprimentos > Parâmetros Fiscais > Substituições Impostos/Modalidade Base Cálculo/Antecipação  
> **Telas citadas:** —  
> **Identificadores de regras:** —

---
Para este novo modelo de cálculo do ICMS ST (critério), é necessário configurar duas tabelas de preço: a primeira para representar o Preço Médio Ponderado a Consumidor Final (PMPF) ou a Farmácia Popular (FP) e a segunda para um produto da Preço Máximo a Consumidor (PMC). É requerido percentual de trava que também tem variação conforme a categoria do medicamento. A trava ajustada deve ser aplicada em operações interestaduais, já nas operações internas que possuem ICMS ST esta deve utilizar o percentual de trava previsto na legislação.

O campo Definição Base Cálculo Substituição não é considerado para o calculo desse critério. Sempre será assumido o menor valor conforme explicado abaixo.

O cálculo funciona em duas etapas da seguinte forma:

1. Será calculado primeiro qual a base a ser comparada com o PMC:
   * Se o valor do PMPF após aplicada a % Trava (PMPF \* % Trava) for MAIOR que o Preço Produto, então a base para comparação fica sendo igual ao PMPF;
   * Se o percentual da trava da PMPF estiver zerada, será utilizado o conceito da Farmácia Popular (FP). Se o valor do FP for MAIOR OU IGUAL que o Preço Produto, então a base para comparação fica sendo igual ao FP;
   * Se o valor do PMPF após aplicada a % Trava (PMPF \* % Trava) for MENOR que o Preço Produto, então o sistema aplica o IVA na base para comparação.
2. Após a execução do item 1, temos a base a ser comparada com o PMC onde se a base calculada for MENOR em relação o PMC, então a base calculada será utilizada. Caso contrário, será utilizado o PMC. Nesse ponto, o menor sempre prevalece.

**Importante**

* Se houver desconto aplicado ao Preço Produto, esse não será aplicado nas tabelas PMPF e PMC.
* Ao executar um dos cálculos do critério 6, o valor da base de cálculo e o valor do ICMS ST serão adicionados nas observações dos itens da nota fiscal da seguinte forma:
  + Método de cálculo ICMS ST: PMPF/FP/PMC/IVA; BC R$ 999,99; ICMS ST R$ 99,99.

Exemplo do cálculo para base:

## Operação: Compra interestadual MG para SP

**Documento fiscal (PMPF <= PMC)**

Preço Produto = 10,99  
Quantidade = 80,00  
% ICMS = 12%  
% ICMS ST = 18%  
PMPF = R$ 17,75  
PMC = R$ 19,81  
% Trava = 90,00%  
% Trava ajustada = % trava \* ((1 - % ICMS ST) / (1 - % ICMS)) = 0,80 \* ((1 - 0,18) / (1 - 0,12)) = 83,8636%  
PMPF com Trava = PMPF \* % Trava ajustada = 17,75 \* 0,838636 = 14,89  

Base ICMS ST = PMPF \* Quantidade = 1420,00

**Documento fiscal (PMPF > PMC)**

Preço Produto = 51,39  
Quantidade = 15,00  
% ICMS = 12%  
% ICMS ST = 18%  
PMPF = R$ 87,01  
PMC = R$ 61,19  
% Trava = 90,00%  
% Trava ajustada = % trava \* ((% ICMS ST) / (% ICMS)) = 0,80 \* ((1 - 0,18) / (1 - 0,12)) = 83,8636%  
PMPF com Trava = PMPF \* % Trava ajustada = 87,01 \* 0,838636 = 72,97  

Base ICMS ST = PMC \* Quantidade = 917,85

**Documento fiscal (IVA ST <= PMC)**

Preço Produto = 12,99  
Quantidade = 80,00  
Valor total do produto = Preço Produto \* Quantidade = 12,99 \* 80,00 = 1039,20  
% ICMS = 12%  
% ICMS ST = 18%  
PMPF = R$ 15,20  
PMC = R$ 19,81  
% Trava = 90,00%  
% Trava ajustada = % trava \* ((1 - % ICMS ST) / (1 - % ICMS)) = 0,80 \* ((1 - 0,18) / (1 - 0,12)) = 83,8636%  
% IVA ST = 36,02%  
% IVA ST ajustada = ((% IVA ST) \* (% ICMS) / (% ICMS ST)) - 1 = ((1 + % 0,3206) \* (1 - % 0,12) / (1 - % 0,18)) = 45,97%  
PMPF com Trava = PMPF \* % Trava ajustada = 87,01 \* 0,838636 = 72,97  
Base IVA ST = Valor total do produto + (Valor total do produto \* % IVA ST ajustada) = 1039,20 + (1039,20 \* 0,4597) = 1516,95  

Base ICMS ST = Base IVA ST = 1516,95

**Documento fiscal (IVA ST > PMC)**

Preço Produto = 12,99  
Quantidade = 80,00  
Valor total do produto = Preço Produto \* Quantidade = 12,99 \* 80,00 = 1039,20  
% ICMS = 12%  
% ICMS ST = 18%  
PMPF = R$ 15,20  
PMC = R$ 18,41  
% Trava = 90,00%  
% Trava ajustada = % trava \* ((1 - % ICMS ST) / (1 - % ICMS)) = 0,80 \* ((1 - 0,18) / (1 - 0,12)) = 83,8636%  
% IVA ST = 36,02%  
% IVA ST ajustada = ((% IVA ST) \* (% ICMS) / (% ICMS ST)) - 1 = ((1 + % 0,3206) \* (1 - % 0,12) / (1 - % 0,18)) = 45,97%  
PMPF com Trava = PMPF \* % Trava ajustada = 87,01 \* 0,838636 = 72,97  
Base IVA ST = Valor total do produto + (Valor total do produto \* % IVA ST ajustada) = 1039,20 + (1039,20 \* 0,4597) = 1516,95  

Base ICMS ST = PMC \* Quantidade = 1472,80

## Operação: Compra interna SP para SP

**Documento fiscal (PMPF <= PMC)**

Preço Produto = 10,99  
Quantidade = 80,00  
% ICMS = 12%  
% ICMS ST = 18%  
PMPF = R$ 17,75  
PMC = R$ 19,81  
% Trava = 90,00%  
PMPF com Trava = PMPF \* % Trava = 17,75 \* 0,90 = 15,98  

Base ICMS ST = PMPF \* Quantidade = 1420,00

**Documento fiscal (PMPF > PMC)**

Preço Produto = 51,39  
Quantidade = 15,00  
% ICMS = 12%  
% ICMS ST = 18%  
PMPF = R$ 87,01  
PMC = R$ 61,19  
% Trava = 90,00%  
PMPF com Trava = PMPF \* % Trava = 87,01 \* 0,90 = 78,31  

Base ICMS ST = PMC \* Quantidade = 917,85

**Documento fiscal (IVA ST <= PMC)**

Preço Produto = 12,99  
Quantidade = 80,00  
Valor total do produto = Preço Produto \* Quantidade = 12,99 \* 80,00 = 1039,20  
% ICMS = 12%  
% ICMS ST = 18%  
PMPF = R$ 14,30  
PMC = R$ 19,81  
% Trava = 90,00%  
% IVA ST = 36,02%  
PMPF com Trava = PMPF \* % Trava = 14,30 \* 0,90 = 12,87  
Base IVA ST = Valor total do produto + (Valor total do produto \* % IVA ST) = 1039,20 + (1039,20 \* 0,3602) = 1413,52  

Base ICMS ST = Base IVA ST = 1516,95

**Documento fiscal (IVA ST > PMC)**

Preço Produto = 12,99  
Quantidade = 80,00  
Valor total do produto = Preço Produto \* Quantidade = 12,99 \* 80,00 = 1039,20  
% ICMS = 12%  
% ICMS ST = 18%  
PMPF = R$ 14,30  
PMC = R$ 18,41  
% Trava = 90,00%  
% IVA ST = 36,02%  
PMPF com Trava = PMPF \* % Trava = 14,30 \* 0,90 = 12,87  
Base IVA ST = Valor total do produto + (Valor total do produto \* % IVA ST) = 1039,20 + (1039,20 \* 0,3602) = 1413,52  

Base ICMS ST = PMC \* Quantidade = 1472,80
