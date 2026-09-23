# ICMS

> **Fonte:** F001TCP - Transações de Compras — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f001tcp.htm  
> **Trilha:** Ajuda por telas > Cadastros > Transações > Parâmetros por Gestão > Compras  
> **Telas citadas:** F119OCT  
> **Identificadores de regras:** —

---
Isenta ICMS

 Indicativo de cálculo na tributação de ICMS para produtos e serviços.

Recupera ICMS

 Indicativo se a transação recupera o ICMS.

Considera ICMS no preço/valor

 Indicativo se o ICMS deve ser somado ou diminuído do preço unitário ou do valor
líquido do item. Para somar ou subtrair o ICMS no preço unitário, obrigatoriamente o item deve ter uma tabela de preço com seu preço base devidamente configurado.

* Quando estiver definido como"1 - Soma no Preço Unitário":
  + Conceito nas Notas Fiscais, Pedidos e Pré-faturas: O cálculo da soma de ICMS no preço unitário é realizado com o preço base da tabela de preço dividido pelo percentual de ICMS.

    ## Exemplo

    - Preço Base do Item = 200;
    - Percentual de ICMS = 12;
    - Preço unitário do item = (200) / ((100 - 12) / 100) = 227,27.
* Quando estiver definido como"2 - Soma no Valor Líquido":
  + Conceito nas Notas Fiscais, Pedidos e Pré-faturas: O cálculo da subtração de ICMS no preço unitário é realizado com o preço base da tabela de preço multiplicado pelo percentual de ICMS.
  + Conceito no Orçamento: O sistema calcula os impostos, somando o valor de ICMS e valor do FCP, no total líquido do orçamento.

    ## Exemplo

    - Valor de ICMS = 1,0;
    - Valor de FCP = 0,67;
    - Total de Impostos = 1,67;
    - Valor Bruto = 100;
    - Total Líquido = 100 + 1,67 = 101,67;
    - Segue imagem abaixo do exemplo na tela F119OCT:

    ![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/images/cadastros/f001tve-exemplo-soma-valor-liquido_thumb_0_48.png)
* Quando estiver definido como"3 - Subtrai do Preço Unitário":
  + Conceito nas Notas Fiscais, Pedidos e Pré-faturas: O cálculo da soma de ICMS no preço unitário é realizado com o preço base da tabela de preço multiplicado pelo percentual de ICMS.

    ## Exemplo

    - Preço Base do Item = 200;
    - Percentual de ICMS = 12;
    - Preço unitário do item = (200) x ((100 - 12) / 100) = 176,0.
* Quando estiver definido como"4 - Subtrai do Valor Líquido":
  + Conceito nas Notas Fiscais, Pedidos e Pré-faturas: O sistema subtrai o valor de ICMS no valor líquido.
  + Conceito no Orçamento: O sistema calcula os impostos, subtraindo o valor de ICMS e valor do FCP, no total líquido do orçamento.

    ## Exemplo

    - Valor de ICMS = 1,0;
    - Valor de FCP = 0,67;
    - Total de Impostos = 1,67;
    - Valor Bruto = 100;
    - Total Líquido = 100 - 1,67 = 98,33;
    - Segue imagem abaixo do exemplo na tela F119OCT:

    ![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/images/cadastros/f001tve-exemplo-subtrai-valor-liquido_thumb_0_48.png)

Calcula Diferença Alíquota

 Indicativo se a transação calcula diferença de alíquota. Para o Regime Simples nacional não é observado se tributa ou não o ICMS, uma vez que o sistema sempre busca uma base do ICMS. Neste caso, para não calcular um diferencial apenas em determinadas operações é necessário utilizar uma transação específica, definindo o campo Calcula Diferença Alíquota igual a "N - Não".

Código ICMS Especial

 Código do ICMS especial.

Código ICMS Substituído

 Código do ICMS Substituído padrão.

Código Redução Imposto

Código de redução do ICMS.

Situação Tributária

 Código da situação tributária.

IPI Base ICMS

 Indicativo se o valor do IPI deve ser considerado na base de ICMS.

Frete Base ICMS

 Indicativo se o valor do Frete deve ser considerado na base de ICMS.

Seguro Base ICMS

 Indicativo se o valor do Seguro deve ser considerado na base de ICMS.

Embalagem Base ICMS

 Indicativo se o valor da Embalagem deve ser considerado na base de ICMS.

Encargos Base ICMS

 Indicativo se o valor de Encargos Financeiros deve ser considerado na base de ICMS.

Outras Despesas Base ICMS

 Indicativo se o valor de Outras Despesas deve ser considerado na base de ICMS.

Arredondamento Base ICMS

 Indicativo se o valor do Arredondamento deve ser considerado na base de ICMS.

Frete Destacadas Base ICMS

 Indicativo se o valor do Frete Destacado deve ser considerado na base de ICMS.

Outras Destacadas Base ICMS

 Indicativo se o valor do Outras Despesas Destacadas deve ser considerado na base de ICMS.
