# Detalhamento por Código de Arrecadação - IPI

> **Fonte:** F055PPF - Configuração de Impostos para a Filial — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f055ppf.htm  
> **Trilha:** Ajuda por telas > Cadastros > Controladoria > Tributos  
> **Telas citadas:** —  
> **Identificadores de regras:** —

---
Quando houver detalhamento de operação da transação, produto ou serviço informado, a apuração do imposto 1 - IPI gera um o título a pagar e/ou guia de recolhimento para cada detalhamento cadastrado.

O sistema totaliza por código de arrecadação os valores das notas fiscais conforme transações/produto/serviço parametrizados na respectiva tela.

Exemplo:

* Código de Arrecadação: 1449;
* Transações: 1101, 1102, 5101, 5102 entre outras.

O total por código de arrecadação é obtido através da operação: **Notas fiscais de saída - notas fiscais de entrada**. Caso possuir mais notas fiscais de entrada que notas fiscais de saída o sistema mantem **0 como imposto a pagar**.

Para mais informações sobre a geração do cálculo do imposto IPI, consulte a documentação da apuração.

## Páginas relacionadas

* [documentação da apuração](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/processo_geracao_calculo_ipi.htm)
