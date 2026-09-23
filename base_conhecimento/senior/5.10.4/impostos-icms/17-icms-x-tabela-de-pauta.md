# ICMS x Tabela de Pauta

> **Fonte:** Rotinas de ICMS — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/impostos-icms.htm#tabela-pauta  
> **Trilha:** Segmentos > Compliance > Configurações para cálculos fiscais > Impostos  
> **Telas citadas:** —  
> **Identificadores de regras:** VEN-000ALICM01, VEN-140NEITE01

---
Para calcular o ICMS dos produtos no estado do Mato Grosso há uma tabela de pauta. Como cadastrá-la?

## Exemplo

1.6 GADO BOVINO

Produtos Unidade Valor Ato Normativo

010290190020 - Bovino, Macho, 0 a 12 meses CB 730,00 150/2013

010290190021 - Bovino, Femea, 0 a 12 meses CB 580,00 150/2013

010290190022 - Bovino, Macho, 13 a 24 meses CB 1.100,00 150/2013

010290190023 - Bovino, Femea, 13 a 24 meses CB 870,00 150/2013

010290190024 - Bovino, Macho, 25 a 36 meses CB 1.314,00 150/2013

010290190025 - Bovino, Femea, 25 a 36 meses CB 986,00 150/2013

010290190027 - Bovino, Femea, acima de 36 meses CB 1.000,00 150/2013

010290190028 - Bovino, Macho, acima de 36 meses CB 1.420,00 150/2013

A sugestão atual é atender mediante o uso de identificadores de regra, sendo o VEN-000ALICM01 para alterar os valores de ICMS durante o cálculo do item da nota fiscal e o VEN-140NEITE01 para alterar o campo modBC na geração do XML da NF-e.

## Páginas relacionadas

* [VEN-000ALICM01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_000alicm01.htm)
* [VEN-140NEITE01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_140neite01.htm)
