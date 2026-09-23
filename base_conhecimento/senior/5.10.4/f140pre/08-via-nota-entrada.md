# Via Nota Entrada

> **Fonte:** F140PRE - Preparação da Nota Fiscal de Saída — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f140pre.htm  
> **Trilha:** Ajuda por telas > Mercado > Gestão de Faturamento e Outras Saídas > Notas Fiscais de Saída  
> **Telas citadas:** F027STR  
> **Identificadores de regras:** —

---
Geração de notas fiscais via notas fiscais de entrada. Pode-se informar cliente ligado ou não ao fornecedor.

Ao utilizar esta opção, o percentual, o valor e base do ICMS Simples Nacional serão filtrados do item da nota fiscal de entrada (produto ou serviço). Estes valores serão repassados para a nota fiscal de saída de devolução. A Série do produto na nota fiscal de saída será igual à da nota de origem.

**Sobre o código da situação tributária ICMS de produto:**

* A sugestão da situação tributária é feita com base no documento a partir do qual a nota é criada.
* A situação tributária de ICMS nas devoluções deve ser herdada da nota de entrada quando qualquer uma destas condições forem verdadeiras:
  + A transação do item da nota fiscal de saída estiver configurado o tipo de calculo de devolução diferente de devolução proporcional. Isso porque a rotina de devolução proporcional deve acionar a rotina de sugestão padrão conforme documentação da tela Situações Tributárias (F027STR)
  + A Filial e o Fornecedor forem do regime do Simples Nacional (operação Simples x Simples).
  + A Filial for do regime Normal e a Situação Tributária de ICMS do item da nota fiscal de entrada não for de ST.
* Quando nenhum dos casos acima for verdadeiro apesar de sugerida pode ser sobrescrita conforme documentação da tela Situações Tributárias (F027STR)
* Caso o usuário altere a situação tributária, esta alteração irá prevalecer sobre todas as situações acima citadas.

## Páginas relacionadas

* [F027STR](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f027str.htm#menu_cadastros/F027STR.htm)
