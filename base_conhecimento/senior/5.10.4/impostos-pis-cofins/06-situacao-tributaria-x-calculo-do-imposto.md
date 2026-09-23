# Situação tributária x cálculo do imposto

> **Fonte:** PIS/COFINS — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/impostos_pis_cofins.htm  
> **Trilha:** Segmentos > Compliance > Configurações para cálculos fiscais > Impostos  
> **Telas citadas:** F001TCP, F049TTR, F075PRO, F095CAD  
> **Identificadores de regras:** —

---
Nas notas fiscais de entrada/saída, a situação tributária influencia no cálculo do PIS/COFINS. Quando o CST for **06 - Operação tributável com alíquota zero** nas notas fiscais de saída, o valor do imposto e alíquota serão zerados e apenas a base será calculada.

Nas notas fiscais de entrada, quando o CST for **73 - Operação de aquisição a alíquota zero**, o valor da base de cálculo será calculado normalmente, porém a alíquota e o valor do imposto serão zerados.  

Para isso, é necessário parametrizar o PIS/COFINS nas seguintes telas:

* Individual (F075PRO);
* Fatura (F001TCP);
* Cadastro (F095CAD);
* Tabelas de tributação (F049TTR).
