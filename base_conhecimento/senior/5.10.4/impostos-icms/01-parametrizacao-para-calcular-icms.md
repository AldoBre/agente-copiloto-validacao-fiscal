# Parametrização para calcular ICMS

> **Fonte:** Rotinas de ICMS — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/impostos-icms.htm#parametrizacao  
> **Trilha:** Segmentos > Compliance > Configurações para cálculos fiscais > Impostos  
> **Telas citadas:** F001TCP, F001TVE, F075PRO, F085CAD, F095CAD, F403FPR  
> **Identificadores de regras:** —

---
* Definir se o fornecedor e o cliente tributam ICMS:
  1. Cadastros > Clientes e Fornecedores > Fornecedores > Cadastro (F095CAD)
  2. Cadastros > Clientes e Fornecedores > Clientes > Cadastro (F085CAD)
* Definir o produto para tributar ICMS:
  1. Se houver ligação produto x fornecedor e o produto estiver definido para obter os parâmetros fiscais desta ligação, então deve ser parametrizada a tela “F403FPR”
  2. Cadastros > Produtos e Serviços > Produtos > Individual (F075PRO)
  3. Cadastros > Clientes e Fornecedores > Fornecedores > Ligações > Fornecedor X Produtos > Individual (F403FPR)
* Definir a transação para calcular ICMS. Informando "N - Não" no campo Isenta ICMS:
  1. Cadastros > Transações > Parâmetros por Gestão > Compras > Ordem Compra > NF Entrada > Fatura (F001TCP)
  2. Cadastros > Transações > Parâmetros por Gestão > Vendas (F001TVE)

## Páginas relacionadas

* [Cadastro](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f095cad.htm)
* [Cadastro](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f085cad.htm)
* [Individual](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075pro.htm)
* [Individual](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f403fpr.htm)
* [Fatura](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f001tcp.htm)
* [Vendas](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f001tve.htm)
