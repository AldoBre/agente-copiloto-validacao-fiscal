# Pauta fiscal

> **Fonte:** Rotinas de ICMS — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/impostos-icms.htm#pauta-fiscal  
> **Trilha:** Segmentos > Compliance > Configurações para cálculos fiscais > Impostos  
> **Telas citadas:** F001TCP, F001TVE, F019TIS, F075PPC, F075PRO, F403FPR  
> **Identificadores de regras:** —

---
O ICMS por pauta é calculado a partir da estrutura de ICMS ST. Ou seja, para calculá-lo é necessário parametrizar uma tabela de ICMS ST.

Pauta fiscal na prática é um preço mínimo que deve ser utilizado para cálculo do ICMS.

Se o produto X é vendido por R$ 350,00, mas seu preço de pauta é R$ 430,00, então o valor base de ICMS será calculado sobre R$ 430,00. Se vender 10 unidades deste produto, o valor base de ICMS será R$ 4.300,00 e não R$ 3.500,00.

Via parametrização do código de ICMS ST, é possível parametrizar para que seja considerado como base de cálculo sempre o maior valor entre o preço sugerido pela tabela de preços e o preço aplicado no item da nota.

Cadastro da tabela de ICMS ST.

O critério de cálculo deve ser 2 – Pelo Preço Unitário Base. Neste critério de cálculo, é necessário informar uma tabela de preço que será utilizada para definir a pauta para cálculo do ICMS na geração do item na nota.

Cadastros > Mercado e Suprimentos > Parâmetros Fiscais > Substituições Impostos > Modalidade Base Cálculo (F019TIS)

O campo Aplicação da tabela de preço deve ser igual a “2 – Outros ST” para ser vinculado à tabela de pauta fiscal.

Este código de ICMS ST deve ser informado no campo “Código Modalidade ICMS” constante na transação e no produto.

Cadastros > Transações > Parâmetros por Gestão > Compras > Ordem Compra > NF Entrada > Fatura (F001TCP)

Cadastros > Transações > Parâmetros por Gestão > Vendas (F001TVE)

Cadastros > Produtos e Serviços > Produtos > Individual (F075PRO)

Cadastros > Clientes e Fornecedores > Fornecedores > Ligações > Fornecedor X Produtos > Individual (F403FPR)

Cadastros > Clientes e Fornecedores > Clientes > Ligações > Cliente X Produto > Individual (F075PPC)

Na tabela de preço, definir o preço base de ICMS.

Neste caso, o preço do item é R$ 350,00 enquanto que o preço base de ICMS é R$ 430,00.

![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/images/impostos_icms028.png)

## Páginas relacionadas

* [Modalidade Base Cálculo](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f019tis.htm)
* [Fatura](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f001tcp.htm)
* [Vendas](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f001tve.htm)
* [Individual](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075pro.htm)
* [Individual](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f403fpr.htm)
* [Individual](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075ppc.htm)
