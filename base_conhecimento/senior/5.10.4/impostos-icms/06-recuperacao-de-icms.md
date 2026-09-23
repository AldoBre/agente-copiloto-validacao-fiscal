# Recuperação de ICMS

> **Fonte:** Rotinas de ICMS — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/impostos-icms.htm#recuperacao  
> **Trilha:** Segmentos > Compliance > Configurações para cálculos fiscais > Impostos  
> **Telas citadas:** F001TCP, F075PRO, F095CAD, F403FPR  
> **Identificadores de regras:** CPR-000ECICM01

---
Durante a apuração do ICMS em Tributos, o sistema busca do campo “ICMS Creditado Efetivamente – Base/Valor/Percentual” da nota fiscal os valores a recuperar de ICMS.

![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/images/impostos_icms010.png)

Por padrão, os campos de ICMS/IPI Creditado Efetivamente não ficam habilitados, exceto nas notas fiscais de devolução para o campo de IPI Creditado Efetivamente e para qualquer tipo de nota quando o fornecedor for optante do simples.

Para que este campo no item da nota fiscal seja preenchido, é necessário que os cadastros envolvidos no item da nota estejam parametrizado para recuperar ICMS. O valor deste campo pode ser manipulado via identificador “CPR-000ECICM01”.

Onde configurar para recuperar ICMS:

Cadastros > Transações > Parâmetros por Gestão > Compras > Ordem Compra > NF Entrada > Fatura (F001TCP)

Cadastros > Produtos e Serviços > Produtos > Individual (F075PRO)

Cadastros > Clientes e Fornecedores > Fornecedores > Cadastro (F095CAD)

Cadastros > Clientes e Fornecedores > Fornecedores > Ligações > Fornecedor X Produtos > Individual (F403FPR)

## Páginas relacionadas

* [Fatura](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f001tcp.htm)
* [Individual](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075pro.htm)
* [Cadastro](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f095cad.htm)
* [Individual](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f403fpr.htm)
