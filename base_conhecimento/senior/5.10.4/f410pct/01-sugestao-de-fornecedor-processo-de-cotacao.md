# Sugestão de fornecedor - Processo de Cotação

> **Fonte:** F410PCT - Processo de Cotação — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f410pct.htm  
> **Trilha:** Ajuda por telas > Suprimentos > Gestão de Compras > Cotação de Preço > Processo de Cotação  
> **Telas citadas:** —  
> **Identificadores de regras:** —

---
A sugestão do fornecedor para o processo de cotação é realizada da seguinte forma:

* Quando informado o campo Área Interesse, as opções Sugerir fornecedores ligados ao Produto/Serviço e Apresentar SOMENTE Produtos/Serviços NÃO ligados ao Fornecedor, relacionados com a sugestão de fornecedores, são desabilitadas e o sistema considera o fornecedor parametrizado na área de interesse. Os campos relacionados com a sugestão de fornecedores são habilitados quando a área de interesse informada não for válida;
* Caso ambas as opções em branco, o sistema mostra todas as solicitações. O campo Fornecedores da grade de Produtos/Serviços é exibido em branco. Ou seja, o sistema não faz a sugestão de fornecedor.
* Caso ambas as opções em branco, mas o campo Fornec. a considerar preenchido, o sistema exibe todas as Solicitações e sugere no campo Fornecedores da guia Produtos/Serviços, o preenchimento do campo Fornec. a considerar

## Exemplo

Campo Fornec. a considerar = 1, 2, 3  
Ao Mostrar as solicitações, o campo Fornecedores da guia Produtos/Serviços será preenchido com 1, 2, 3

* A opção Sugerir fornecedores ligados ao Produto/Serviço mostra tanto as solicitações de Produtos/Serviços que possuem ligação com Fornecedor quanto as que não possuem. Para as que possuem ligação, são sugeridos os códigos dos Fornecedores. Para as demais solicitações de Produto/Serviço que não possuem ligação, a coluna Fornecedores ficará vazia.   
  Neste caso, a opção Apresentar SOMENTE Produtos/Serviços NÃO ligados ao Fornecedor é desabilitada.
* Com a opção Apresentar SOMENTE Produtos/Serviços NÃO ligados ao Fornecedor selecionada, a opção Sugerir fornecedores ligados ao Produto/Serviço e o campo Fornec. a considerar são desabilitados. Neste caso, consideram-se as solicitações de compra que contenham apenas produtos/serviços sem ligação com fornecedores;

## Exemplo

| Ligação Produto X Fornecedor | | | | |
| --- | --- | --- | --- | --- |
| Fornecedor 1 | Fornecedor 2 | Fornecedor 3 | Fornecedor 4 | Sem fornecedor |
| Produto A, B e C | Produto A e C | Produto A e B | Sem produto | Produto D |

Cenário 1:

* Sugerir fornecedores ligados a Produto/Serviço: Não
* Apresentar SOMENTE Produtos/Serviços Não ligados
  ao Fornecedor: Não
* Fornec.a Considerar: Nenhum

São exibidas todas as solicitações e a coluna Fornecedor em branco.

| Produto | Fornecedor |
| --- | --- |
| Produto A |  |
| Produto B |  |
| Produto C |  |
| Produto D |  |

Cenário 2:

* Sugerir fornecedores ligados a Produto/Serviço: Não
* Apresentar SOMENTE Produtos/Serviços Não ligados
  ao Fornecedor: Não
* Fornec.a Considerar: 1, 2 e 3

São exibidas todas as solicitações e sugerido os Fornecedores 1, 2, 3.

| Produto | Fornecedor |
| --- | --- |
| Produto A | 1, 2 e 3 |
| Produto B | 1, 2 e 3 |
| Produto C | 1, 2 e 3 |
| Produto D | 1, 2 e 3 |

Cenário 3:

* Sugerir fornecedores ligados a Produto/Serviço: Sim
* Apresentar SOMENTE Produtos/Serviços Não ligados
  ao Fornecedor: Não
* Fornec.a Considerar: 1 e 2

São exibidas todas as solicitações. Para aquelas que possuem produto com ligação ao Fornecedor 1 e 2, o
sistema sugere os fornecedores. Para aquelas que
possuem produtos sem ligação a fornecedor, a coluna Fornecedores fica vazia.

| Produto | Fornecedor |
| --- | --- |
| Produto A | 1 e 2 |
| Produto B | 1 |
| Produto C | 1 e 2 |
| Produto D | Este produto não está ligado a nenhum fornecedor |

Cenário 4:

* Sugerir fornecedores ligados a Produto/Serviço: Sim
* Apresentar SOMENTE Produtos/Serviços Não ligados
  ao Fornecedor: Não
* Fornec.a Considerar: Nenhum

São exibidas todas as solicitações. Para aquelas que
possuem produto com ligação ao Fornecedor, o sistema
sugere os fornecedores. Para aquelas que possuem produtos
sem ligação a fornecedor, a coluna Fornecedores fica vazia.

| Produto | Fornecedor |
| --- | --- |
| Produto A | 1, 2 e 3 |
| Produto B | 1 e 3 |
| Produto C | 1 e 2 |
| Produto D | Este produto não está ligado a nenhum fornecedor |

Cenário 5:

* Sugerir fornecedores ligados a Produto/Serviço: Não
* Apresentar SOMENTE Produtos/Serviços Não ligados
  ao Fornecedor: Sim
* Fornec.a Considerar: Nenhum

São exibidas todas as solicitações que possuem Produto
sem ligação com Fornecedores.

| Produto | Fornecedor |
| --- | --- |
| Produto D | nenhum |
