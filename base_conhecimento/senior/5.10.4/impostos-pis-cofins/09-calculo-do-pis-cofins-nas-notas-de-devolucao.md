# Cálculo do PIS/COFINS nas notas de devolução

> **Fonte:** PIS/COFINS — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/impostos_pis_cofins.htm  
> **Trilha:** Segmentos > Compliance > Configurações para cálculos fiscais > Impostos  
> **Telas citadas:** —  
> **Identificadores de regras:** COM-000ALPIS01

---
Nas notas de devolução, o PIS/COFINS é calculado automaticamente quando na nota de origem houve cálculo do imposto. Esses impostos são atribuídos em campos específicos de estorno de PIS/COFINS – Estorno Devolução. Não é necessário parametrizar o sistema para calcular estes impostos nessas notas, caso contrário o cálculo será duplicado.

Para calcular o PIS / COFINS a Recuperar em notas fiscais de devolução, é verificado o campo Recupera Pis (RecPis) do cadastro de fornecedor e o campo Recupera Pis (RecPis) do cadastro de produto. É preciso que contenha valor "S" nos dois cadastros. Após isso, também é verificado se um item de nota de entrada está ligado a um item da nota de saída de devolução. Caso sim, o estorno só será calculado se o item da entrada também calculou (VLRPIS).

Outra opção para o cliente é utilizar o identificador de regras COM-000ALPIS01, alterando os valores nas variáveis VSVLRBPI e VSVLRPIS.

**Tela de cálculo de itens na nota de entrada:**

![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/images/imposto_pis_cofins010_thumb_0_48.png)

**Tela de cálculo de itens na nota de saída:**

![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/images/imposto_pis_cofins011_thumb_0_48.png)

## Páginas relacionadas

* [COM-000ALPIS01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/com_000alpis01.htm)
