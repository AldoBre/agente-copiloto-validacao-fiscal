# Redução da base de cálculo de ICMS x valor do frete

> **Fonte:** Rotinas de ICMS — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/impostos-icms.htm#reducao-frete  
> **Trilha:** Segmentos > Compliance > Configurações para cálculos fiscais > Impostos  
> **Telas citadas:** —  
> **Identificadores de regras:** CPR-000REDUC01, VEN-000REDUC01

---
Temos uma nota fiscal onde tem redução de base de ICMS e o valor de frete não está sendo considerado na base, por exemplo:

Valor Produtos: R$ 30.914,00

Valor Frete: R$ 4.800,00

Redução base ICMS: 41,67

Base de cálculo do ICMS: R$ 22.832,14 --> Esta base deveria ser R$ 20.831.98

Isto ocorre porque o sistema não considera o frete na redução da base de ICMS. Para que o valor do frete seja também considerado na redução da base, deve-se ativar o identificador de regras CPR-000REDUC01(Compras) e/ou VEN-000REDUC01(Vendas). Se o usuário estiver utilizando o GO UP, os parâmetros globais CPR-000REDUC01 e VEN-000REDUC01 devem ser utilizados para essa função.

## Páginas relacionadas

* [CPR-000REDUC01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/cpr_000reduc01.htm)
* [VEN-000REDUC01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_000reduc01.htm)
