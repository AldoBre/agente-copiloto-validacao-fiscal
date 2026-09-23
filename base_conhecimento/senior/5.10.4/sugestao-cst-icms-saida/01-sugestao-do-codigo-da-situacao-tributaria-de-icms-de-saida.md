# Sugestão do Código da Situação Tributária de ICMS de Saída

> **Fonte:** Sugestão do Código da Situação Tributária de ICMS de Saída — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/sugestaocst-icms-saida.htm  
> **Trilha:** Ajuda por telas > Mercado  
> **Telas citadas:** E001TNS, E075PPC, E075PRO, E080SER, E085HCL, F001TVE, F075PPC, F075PRO, F080SER, F085HCL  
> **Identificadores de regras:** —

---
Ajuda por telas > Mercado > Sugestão do Código da Situação Tributária de ICMS de Saída

A sugestão do código da situação tributária de ICMS em rotinas de saída segue a ordem definida abaixo. Assim que o sistema encontrar um código adequado, ele não verifica as próximas opções. Vale destacar que a ordem de busca da parametrização pode variar conforme a versão definida no parâmetro global SugCstIcm.

## Parametrização

### Quando SugCstIcm está com valor "1":

1. F001TVE - Cadastros / Transações / Parâmetros por Gestão / Vendas  
   Guia: ICMS  
   Campo: Situação Tributária (E001TNS.ComStr)
2. F075PPC - Cadastros / Clientes e Fornecedores / Clientes / Ligações / Cliente X Produto / Individual   
    Campo: Situação Tributária (E075PPC.CodStr)  

   O preferencial de retorno para as relações da ligação ocorre na seguinte ordem:

   1. UF da Filial e Transação informados

   2. UF da Filial informada e Transação não informada

   3. UF da Filial não informada e Transação informada

   4. UF da Filial e Transação não informadas

     
   Primeiro é feita a consulta dos itens acima utilizando a derivação. Caso não forem encontrados registros, a consulta é realizada sem derivação.
3. F085HCL - Cadastros / Clientes e Fornecedores / Clientes / Definições/Histórico   
   Campo: Situação Tributária (E085HCL.CodStr)
4. Caso for GoUp ou o parâmetro global VenProStr estiver ativo, busca do cadastro de produto ou serviço:

   1. F075PRO - Cadastros / Produtos e Serviços / Produtos / Individual

      Guia: D. Gerais   
      Campo: Situação Tributária (E075PRO.CodStr)
   2. F080SER - Cadastros / Produtos e Serviços / Serviços / Individual   
      Guia: Cadastro  
      Campo: Situação Tributária (E080SER.CodStr)
5. Se não tiver cadastrado em nenhum dos locais acima, o sistema executará a rotina de geração do código.

### Quando SugCstIcm está com valor "2":

1. F075PPC - Cadastros / Clientes e Fornecedores / Clientes / Ligações / Cliente X Produto / Individual
   Campo: Situação Tributária (E075PPC.CodStr)   

   O preferencial de retorno para as relações da ligação ocorre na seguinte ordem:

   1. UF da Filial e Transação informados

   2. UF da Filial informada e Transação não informada

   3. UF da Filial não informada e Transação informada

   4. UF da Filial e Transação não informadas   

   Primeiro é feita a consulta dos itens acima utilizando a derivação. Caso não forem encontrados registros, a consulta é realizada sem derivação.
2. F085HCL - Cadastros / Clientes e Fornecedores / Clientes / Definições/Histórico

   Campo: Situação Tributária (E085HCL.CodStr)   
   Busca do cadastro de produto e depois de serviço:
3. Caso for GoUp ou o parâmetro global VenProStr estiver ativo:
   1. F075PRO - Cadastros / Produtos e Serviços / Produtos / Individual

      Guia: D. Gerais

      Campo: Situação Tributária (E075PRO.CodStr)
   2. F080SER - Cadastros / Produtos e Serviços / Serviços / Individual

      Guia: Cadastro

      Campo: Situação Tributária (E080SER.CodStr)
4. F001TVE - Cadastros / Transações / Parâmetros por Gestão / Vendas

   Guia: ICMS

   Campo: Situação Tributária (E001TNS.ComStr)
5. Se não tiver cadastrado em nenhum dos locais acima, o sistema executará a rotina de geração do código.

## Páginas relacionadas

* [Ajuda por telas](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/ajuda-telas.htm)
* [Mercado](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/menu_mercado.htm)
