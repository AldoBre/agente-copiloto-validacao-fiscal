# Sugestão do Código da Situação Tributária de ICMS de Entrada

> **Fonte:** Sugestão do Código da Situação Tributária de ICMS de Entrada — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/sugestaocst-icms-entrada.htm  
> **Trilha:** Ajuda por telas > Suprimentos  
> **Telas citadas:** E001TNS, E075PRO, E080SER, E403FPR, F001TVE, F075PRO, F080SER, F403FPR  
> **Identificadores de regras:** —

---
Ajuda por telas > Suprimentos > Sugestão do Código da Situação Tributária de ICMS de Entrada

A sugestão do código da situação tributária de ICMS em rotinas de entrada segue a ordem definida abaixo. Assim que o sistema encontrar um código adequado, ele não verifica as próximas opções. Vale destacar que a ordem de busca da parametrização pode variar conforme a versão definida no parâmetro global SugCstIcm.

## Parametrização

### Quando SugCstIcm está com valor "1":

1. F001TVE - Cadastros / Transações / Parâmetros por Gestão / Vendas  
   Guia: ICMS  
   Campo: Situação Tributária (E001TNS.ComStr)
2. F403FPR - Cadastros / Clientes e Fornecedores / Fornecedores / Ligações / Fornecedor X Produtos / Individual  
   Campo: Situação Tributária (E403FPR.CodStr)
3. Busca do cadastro de produto e depois de serviço:

   1. F075PRO - Cadastros / Produtos e Serviços / Produtos / Individual

      Guia: D. Gerais   
      Campo: Situação Tributária (E075PRO.CodStr)
   2. F080SER - Cadastros / Produtos e Serviços / Serviços / Individual   
      Guia: Cadastro  
      Campo: Situação Tributária (E080SER.CodStr)
4. Se não tiver cadastrado em nenhum dos locais acima, o sistema irá executar a rotina de geração do código.

### Quando SugCstIcm está com valor "2":

1. F403FPR - Cadastros / Clientes e Fornecedores / Fornecedores / Ligações / Fornecedor X Produtos / Individual  
    Campo: Situação Tributária (E403FPR.CodStr)
2. Busca do cadastro de produto e depois de serviço:
   1. F075PRO - Cadastros / Produtos e Serviços / Produtos / Individual

      Guia: D. Gerais

      Campo: Situação Tributária (E075PRO.CodStr)
   2. F080SER - Cadastros / Produtos e Serviços / Serviços / Individual

      Guia: Cadastro

      Campo: Situação Tributária (E080SER.CodStr)
3. F001TVE - Cadastros / Transações / Parâmetros por Gestão / Vendas

   Guia: ICMS

   Campo: Situação Tributária (E001TNS.ComStr)
4. Se não tiver cadastrado em nenhum dos locais acima, o sistema irá executar a rotina de geração do código.

## Páginas relacionadas

* [Ajuda por telas](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/ajuda-telas.htm)
* [Suprimentos](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/menu_suprimentos.htm)
