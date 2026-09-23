# Cadastro da alíquota para os impostos

> **Fonte:** PIS/COFINS — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/impostos_pis_cofins.htm  
> **Trilha:** Segmentos > Compliance > Configurações para cálculos fiscais > Impostos  
> **Telas citadas:** F001TCP, F001TVE, F049TTR, F055PPF, F075PRO, F080SER, F085CAD, F095CAD, F403FPR  
> **Identificadores de regras:** —

---
A alíquota para o PIS/COFINS pode ser definida na tabela de tributação ou a partir do cadastro da classificação fiscal. A alíquota da classificação fiscal tem prioridade em relação a alíquota do cadastro do produto.

* Cadastros > Controladoria > Tributos > Tabelas de tributação (F049TTR)

Ainda, é possível atribuir uma alíquota no cadastro do fornecedor que será priorizada em relação a tabela de tributação e a classificação fiscal, para os documentos de compra.

![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/images/imposto_pis_cofins003_thumb_0_48.png)

Para os documentos de compra existem campos na ligação produto x fornecedor serão considerados sobre os demais cadastros caso o produto esteja parametrizado nesta ligação.

![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/images/suprimentos/impostos_pis_cofins_thumb_0_48.png)

Fazer a ligação imposto x filial.

* Cadastros > Controladoria > Tributos > Base imposto (Liga Filial) (F055PPF)

![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/images/imposto_pis_cofins004_thumb_0_48.png)

Configurar a transação para calcular PIS/COFINS, no campo Tributa PIS Faturamento:

* Cadastros > Transações > Parâmetros por Gestão > Vendas (F001TVE)
* Cadastros > Transações > Parâmetros por Gestão > Compras > Ordem Compra > NF Entrada > Fatura (F001TCP)

Configurar o cliente, nos campos Tributa PIS e Tributa COFINS.

* Cadastros > Clientes e Fornecedores > Clientes > Cadastro (F085CAD)

Configurar o fornecedor, nos campos Recupera PIS e Recupera Cofins.

* Cadastros > Clientes e Fornecedores > Fornecedores > Cadastro (F095CAD)

Configurar o cadastro do produto para calcular PIS/COFINS. Se houver ligação produto x fornecedor, este cadastro deve ser verificado.

* Cadastros > Produtos e Serviços > Produtos > Individual (F075PRO)
* Cadastros > Produtos e Serviços > Serviços > Individual (F080SER)
* Cadastros > Clientes e Fornecedores > Fornecedores > Ligações > Fornecedor X Produtos > Individual (F403FPR)

![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/images/suprimentos/impostos_pis_cofins_01_thumb_0_48.png)

## Páginas relacionadas

* [Tabelas de tributação](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f049ttr.htm)
* [Base imposto (Liga Filial)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f055ppf.htm)
* [Vendas](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f001tve.htm)
* [Fatura](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f001tcp.htm)
* [Cadastro](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f085cad.htm)
* [Cadastro](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f095cad.htm)
* [Individual](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075pro.htm)
* [Individual](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f080ser.htm)
* [Individual](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f403fpr.htm)
