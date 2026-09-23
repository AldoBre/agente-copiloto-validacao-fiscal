# Via Nota Saída

> **Fonte:** F140PRE - Preparação da Nota Fiscal de Saída — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f140pre.htm  
> **Trilha:** Ajuda por telas > Mercado > Gestão de Faturamento e Outras Saídas > Notas Fiscais de Saída  
> **Telas citadas:** E085CLI, F027STR, F140PRE  
> **Identificadores de regras:** VEN-000TNSDE01

---
Geração de notas fiscais via notas fiscais de saída, inclusive de cliente diferente do informado no cabeçalho. Ao utilizar esta opção, o percentual, o valor e base do ICMS Simples Nacional serão os mesmos da nota fiscal de saída de origem.

Este recurso trata-se de um facilitador, não é mantida nenhuma ligação entre as notas origem e a gerada. Possibilitado informar notas fiscais de clientes diferentes do cliente informado no cabeçalho, inclusive pertencentes a outro grupo de empresas (E085CLI.CODGRE).

No entanto, a geração de notas fiscais geradas pelo processo da gestão de distribuição e formação de cargas, via nota de saída na tela Preparação da Nota Fiscal de Saída (F140PRE), não será permitida. Esse processo, que envolve a formação de cargas gerando posteriormente notas fiscais do tipo "10", possui um filtro, não sendo permitida a geração por meio deste. Se houver a necessidade de copiar a nota fiscal, então esta deve ser gerada novamente pelo mesmo processo de formação de cargas.

**Sobre o código da situação tributária ICMS de produto:**

* A sugestão da situação tributária é feita com base no documento a partir do qual a nota é criada;
* Se a transação do item de produto for a mesma do item de produto da nota de origem então herda as situações tributárias;
* Quando as transações forem diferentes, a situação tributária, apesar de sugerida pode ser sobrescrita conforme documentação da tela Situações Tributárias (F027STR);
* Caso o usuário altere a situação tributária, esta alteração irá prevalecer sobre todas as situações acima citadas.

Observação

O identificador de regras VEN-000TNSDE01 não será executado, pois é realizada uma cópia idêntica da nota fiscal a ser copiada, sendo assim, não irá sugerir uma transação diferente. A sugestão da transação somente ocorrerá quanto a nota fiscal que estiver copiando for um cupom fiscal, pois neste caso trata-se de operações diferentes.

## Páginas relacionadas

* [F027STR](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f027str.htm#menu_cadastros/F027STR.htm)
