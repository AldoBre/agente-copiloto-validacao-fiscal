# ICMS

> **Fonte:** F001TVE - Transações de Vendas — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f001tve.htm  
> **Trilha:** Ajuda por telas > Cadastros > Transações > Parâmetros por Gestão  
> **Telas citadas:** F119OCT  
> **Identificadores de regras:** —

---
Isenta ICMS

Indicativo se transação é isenta de ICMS. Quando este campo for igual a S-Sim o campo Situação Tributária obrigatoriamente deverá ser preenchido como Nacional-Isenta ou não tributada para que a integração com o Retaguarda funcione corretamente.

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

Considera no Índice CIAP

Indicativo se a transação é considerada para o índice de crédito do CIAP.

Código ICMS Especial

Código de ICMS especial padrão para a transação.

Código ICMS Substituído

Código de substituição tributária de ICMS padrão para a transação.

Código Redução Imposto

Código de redução de ICMS padrão para a transação.

Situação Tributária

Código da Situação tributária para a transação. Verificar informação no campo Isenta ICMS.

IPI Base ICMS

Indicativo se o valor do IPI será considerado na base de ICMS.

Frete Base ICMS

Indicativo se o valor do frete será considerado na base de ICMS.

Seguro Base ICMS

Indicativo se o valor do seguro será considerado na base de ICMS.

Embalagem Base ICMS

Indicativo se o valor da embalagem será considerado na base de ICMS.

Encargos Base ICMS

Indicativo se o valor de encargos será considerado na base de ICMS.

Outras Base ICMS

Indicativo se o valor de outras despesas será considerado na base de ICMS.

Arredondamento Base ICMS

Indicativo se o valor de arredondamento será considerado na base de ICMS.

Frete Destacado Base ICMS

Indicativo se o valor do frete destacado será considerado na base de ICMS.

Outras Destacadas Base ICMS

Indicativo se o valor de outras despesas destacadas será considerado na base de ICMS.
