# ICMS nos movimentos dos estoques

> **Fonte:** Rotinas de ICMS — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/impostos-icms.htm#icms-estoques  
> **Trilha:** Segmentos > Compliance > Configurações para cálculos fiscais > Impostos  
> **Telas citadas:** —  
> **Identificadores de regras:** CPR-440VLRMO01

---
Para que o ICMS não seja considerado no valor do estoque, é necessário que este imposto esteja configurado para não ser recuperado. Caso seja recuperado, os valores do ICMS Substituído Destacado, ICMS Cred. Efetivamente e Valor do FCP não serão somados no valor do estoque.

Caso em uma determinada particularidade o cliente tenha necessidade de recuperar o imposto porém não agregar este valor ao estoque no movimento, é necessário a utilização do identificador CPR-440VLRMO01 para que seja possível desta forma manipular o valor do movimento a ser gravado.

O valor do ICMS Creditado Efetivamente é o valor utilizado no cálculo do movimento de estoque.

## Páginas relacionadas

* [CPR-440VLRMO01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/cpr_440vlrmo01.htm)
