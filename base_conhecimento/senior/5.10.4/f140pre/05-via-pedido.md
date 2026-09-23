# Via Pedido

> **Fonte:** F140PRE - Preparação da Nota Fiscal de Saída — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f140pre.htm  
> **Trilha:** Ajuda por telas > Mercado > Gestão de Faturamento e Outras Saídas > Notas Fiscais de Saída  
> **Telas citadas:** E085CLI, F027STR  
> **Identificadores de regras:** —

---
Geração de notas fiscais via pedidos.

**Sobre o código da situação tributária ICMS de produto:**

* A sugestão da situação tributária é feita com base no documento a partir do qual a nota foi criada;
* A situação tributária, apesar de sugerida, pode ser sobrescrita conforme documentação da tela Situações Tributárias (F027STR)
* Caso o usuário altere a situação tributária, esta alteração irá prevalecer sobre as situações acima citadas.

Ao utilizar esta opção:

* Os valores dos descontos de antecipação e pontualidade que estão nas parcelas do pedido serão transferidos paras as parcelas da nota fiscal.
* O campo % ICMS Simples Nac. estará zerado no momento em que o pedido for informado, pois pedidos não possuem tratamento para ICMS Simples Nacional.
* Somente na transferência dos itens, caso a filial estiver parametrizada para filtrar as alíquotas no momento do faturamento, o percentual do ICMS herdado do pedido será zerado e o percentual de ICMS Simples Nacional da ultima apuração será utilizado.

Se o campo Faturar Grupo de Empresas estiver marcado, será possível faturar pedidos de outros clientes pertencentes ao mesmo grupo de empresas(E085CLI.CODGRE).

## Páginas relacionadas

* [F027STR](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f027str.htm#menu_cadastros/F027STR.htm)
