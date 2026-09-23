# Sugestão da situação tributária

> **Fonte:** PIS/COFINS — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/impostos_pis_cofins.htm  
> **Trilha:** Segmentos > Compliance > Configurações para cálculos fiscais > Impostos  
> **Telas citadas:** —  
> **Identificadores de regras:** COM-000ALSTR03, COM-000ALSTR04, CPR-440GERCS01

---
A sugestão da situação tributária do PIS e COFINS no item da nota fiscal acontece conforme a seguinte ordem:

* 1º Assume a situação tributária constante no cadastro da transação;
* 2º Assume a situação tributária constante no cadastro do produto/serviço.

A situação tributária do PIS e COFINS ainda pode ser atribuída ao item da nota fiscal a partir de uma regra ligada aos identificadores COM-000ALSTR03 e COM-000ALSTR04, respectivamente.

Questão: Na geração de notas fiscais de entrada dos tipos 3, 6, 7 e 10, que por sua vez geram notas fiscais de saída, o sistema atribui nas notas de saída o mesmo CST das notas de entrada. Como fazer para que o sistema faça a sugestão das CST's nas notas de saída a partir da codificação do módulo de Mercado?

Nesse caso, utilize o identificador de regras CPR-440GERCS01. Com ele ativo, o sistema fará a sugestão dos CSTs nas notas de saída conforme condições do módulo de Mercado e fará com que os identificadores de sugestão do CST sejam executados para os itens das notas de saída.

## Páginas relacionadas

* [COM-000ALSTR03](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/com_000alstr03.htm)
* [COM-000ALSTR04](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/com_000alstr04.htm)
* [CPR-440GERCS01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/cpr_440gercs01.htm)
