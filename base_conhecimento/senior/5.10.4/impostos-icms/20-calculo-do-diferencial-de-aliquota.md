# Cálculo do diferencial de alíquota

> **Fonte:** Rotinas de ICMS — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/impostos-icms.htm#calculo-diferencial  
> **Trilha:** Segmentos > Compliance > Configurações para cálculos fiscais > Impostos  
> **Telas citadas:** E009PPE, F001TCP, F009PPE, F019TIS, F070FCA, F070FCP, F070PSE, F095CAD  
> **Identificadores de regras:** CPR-440ALDFA01, CPR-440ALDFA02

---
## Parametrização para cálculo do diferencial

Indicar se a filial para calcula o diferencial, no campo Diferença Alíquota com S.

Cadastros > Filiais > Cadastro (F070FCA)

Indicar se a transação calcula diferencial, na aba ICMS, preencher o campo Calcula Diferença Alíquota com S.

Cadastros > Transações > Parâmetros por Gestão > Compras > Ordem Compra > NF Entrada > Fatura (F001TCP)

Nas definições da filial para o Compras definir para quais operações o diferencial deve ser calculado. Na aba Compras 2, preencher o campo Calcular diferencial de alíquota com S.

Cadastros > Filiais > Parâmetros por Gestão > Compras e Recebimento (F070FCP)

Na transação há o campo Aplicação Operação. O cálculo do diferencial é influenciado por este campo dependendo de como estiver parametrizado o campo acima.

Cadastros > Transações > Parâmetros por Gestão > Compras > Ordem Compra > NF Entrada > Fatura (F001TCP)

O estado (UF) do fornecedor deverá ser diferente do estado (UF) da Filial ativa.

Cadastros > Clientes e Fornecedores > Fornecedores > Cadastro (F095CAD)

Cadastros > Filiais > Cadastro (F070FCA)

![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/images/impostos_icms021.png)

A alíquota de ICMS do estado do fornecedor deve ser menor que a alíquota interna – alíquota do estado da filial.

Cadastros > Mercado e Suprimentos > Parâmetros Fiscais > Parâmetros por Estado > Cadastro (F009PPE)

Com esta configuração, o sistema calcula o diferencial de alíquota, sendo a diferença do cálculo do ICMS feito na nota com o cálculo que seria feito com a alíquota interna.

![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/images/impostos_icms023.png)

O diferencial de alíquota pode ser alterado via identificadores “CPR-440ALDFA01” e “CPR-440ALDFA02”

## Diferencial de alíquota x ICMS especial

Quando há tabela de ICMS Especial no item da nota, o que o sistema faz para realizar o cálculo do diferencial de alíquota é, primeiramente, verificar todas as alíquotas da tabela de ICMS Especial, se não encontrar alíquota para as unidades fiscais envolvidas na nota, busca da tabela E009PPE(Parâmetros por estado).

## Diferencial de alíquota nas notas de saída

Para calcular o diferencial de alíquota nas notas de saída, deve-se utilizar um código de ICMS ST(ICMS Substituição Tributária) e apenas atribuir o percentual equivalente ao diferencial de alíquota no campo % Imposto da tela F019TIS(Tela da cadastro de ICMS ST).

Cadastros > Mercado e Suprimentos > Parâmetros Fiscais > Substituições impostos (F019TIS)

## Convênio ICMS 52/91

Nos processos de compras (Ordem de Compra) e recebimento (Nota fiscal de Entrada), quando o estado de destino (UF filial) de uma operação de aquisição de “Ativo Imobilizado” estiver enquadrado no Convênio ICMS 52/91 e a nota fiscal for emitida com uma redução de base de cálculo, conforme a carga efetiva a ser gerada no final da operação, na entrada destes produtos de acordo com o convênio, o diferencial de alíquota deve ser calculado a partir da alíquota interna também baseado na carga efetiva.

Caso o tipo da base de cálculo do diferencial de alíquota do ICMS para compra de ativo imobilizado seja definido como "9 - Dupla c/ Alíq. interna por dentro", a base de cálculo do diferencial de alíquota nesta operação deve aplicar o cálculo por dentro a partir da alíquota da carga efetiva através da fórmula:

**Fórmula:**

```
Base Cálculo DIFA = Valor da Operação / (1 - AliqEfetiva)  
Diferencial Alíquota = Aliq Efetiva - (Aliq. ICMS Operação - (Aliq. Redução ICMS))  
Valor do DIFA = Base cálculo * Diferencial de alíquota
```

**Exemplo:**

```
Valor Base ICMS Sem Redução = 1000,00  
Aliq. Efetiva UF Filial = 8,80 %  
% ICMS Operação = 7%  
% Redução ICMS = 26,57

Base Calculo DIFA = 1000,00 / (1 - 8,80%) = 1096,49  
Diferencial Alíquota = 8,80 - (7 - 26,57%) = 3,66  
Valor do DIFA = 1096,49 * 3,66% = 40,13
```

Caso o tipo da base de cálculo do diferencial de alíquota do ICMS para compra de ativo imobilizado seja definido como "2 - Simples", a base de cálculo do diferencial de alíquota trata-se do valor da operação:

**Fórmula:**

```
Base Cálculo DIFA = Valor da Operação  
Diferencial Alíquota = Aliq Efetiva - (Aliq. ICMS Operação - (Aliq. Redução ICMS))  
Valor do DIFA = Base cálculo * Diferencial de alíquota
```

**Exemplo:**

```
Valor Base ICMS Sem Redução = 1000,00  
Aliq. Efetiva UF Filial = 8,80 %  
% ICMS Operação = 7%  
% Redução ICMS = 26,57

Base Calculo DIFA = 1000,00  
Diferencial Alíquota = 8,80 - (7 - 26,57%) = 3,66  
Valor do DIFA = 1000,00 * 3,66% = 36,60
```

A parametrização da alíquota efetiva para o estado destino deve ser informada nas grades de produto e/ou serviço dos parâmetros de entrada, no campo %Efet. ICMS UF destino da tela de Parâmetros Fiscais de produtos e serviços por filial e estado (F070PSE). Esta parametrização indicará que o cálculo do diferencial de alíquota para o estado será efetuado conforme o convênio ICMS 52/91.

## Convênio ICMS 236/2021

Nos processos de compra (Ordem de Compra) e recebimento (Nota fiscal de Entrada), quando o estado destino (UF filial) de uma operação de aquisição de Ativo Imobilizado ou Uso e Consumo estiver enquadrado no Convênio ICMS 236/2021, o cálculo do diferencial de alíquota terá base dupla com ICMS interno por dentro.

Para que o cálculo seja feito na entrada dos produtos, o campo **Tipo cálculo DIFA** da tela Parâmetros da Filial para Compras (F070FCP) deve ser preenchido com o valor "10 - Dupla c/ desconto do ICMS e alíq. interna por dentro c/ aplicação da diferença de alíq."

**Fórmula:**

```
Base Cálculo DIFA = Valor Base do ICMS - Valor do ICMS;
Base Cálculo DIFA = Valor Base do DIFA / (1 - (Percentual de ICMS interna no estado de destino / 100));
Valor do DIFA = (Valor Base do DIFA * Percentual de ICMS interna no estado de destino) / 100;
Valor do DIFA = Valor do DIFA - Valor do ICMS;
```

## Páginas relacionadas

* [Cadastro](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070fca.htm)
* [Fatura](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f001tcp.htm)
* [Compras e Recebimento](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070fcp.htm)
* [Cadastro](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f095cad.htm)
* [Cadastro](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f009ppe.htm)
* [CPR-440ALDFA01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/cpr_440aldfa01.htm)
* [CPR-440ALDFA02](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/cpr_440aldfa02.htm)
* [Substituições impostos](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f019tis.htm)
* [F070PSE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070pse.htm)
