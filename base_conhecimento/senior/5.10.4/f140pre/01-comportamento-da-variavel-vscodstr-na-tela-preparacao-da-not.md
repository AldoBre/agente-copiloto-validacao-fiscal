# Comportamento da variável VSCODSTR na tela Preparação da Nota Fiscal Saída (F140PRE)

> **Fonte:** F140PRE - Preparação da Nota Fiscal de Saída — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f140pre.htm#Comportamento_da_variável_VSCODSTR  
> **Trilha:** Ajuda por telas > Mercado > Gestão de Faturamento e Outras Saídas > Notas Fiscais de Saída  
> **Telas citadas:** F027STR, F070FVE, F140PRE  
> **Identificadores de regras:** VEN-000ALICM01

---
Quando o identificador de regras VEN-000ALICM01 estiver ativo para esta tela, a variável VSCODSTR, responsável pela consulta da situação tributária do ICMS do item da nota fiscal, apresentará o seguinte comportamento:

* Ao clicar em Mostrar, esta variável não apresentará nenhum valor porque não é enviado nenhum para ela nesta fase do processo;
* Ao clicar em Processar, o identificador de regras VEN-000ALICM01 pode ser acionado mais de uma vez, dependendo da configuração pré estabelecida no sistema, como por exemplo, quando o campo Cálculo Manual de Impostos N.F.S. da tela Parâmetros da Filial para Vendas (F070FVE) estiver configurado com o valor **S - Sim**. Porém, a variável VSCODSTR somente apresentará o valor correto na última execução do identificador de regras, quando ocorrer este cenário;
* O valor que é enviado para a variável em questão não é proveniente do pedido. A situação tributária será sugerida novamente, conforme especificado na documentação da tela Situações Tributárias (F027STR) e ela não pode apresentar as informações igual as que estão no pedido. Este comportamento ocorre devido a alteração da parametrização do sistema feita em um momento entre a geração do pedido e a geração da nota fiscal;
* Se a sugestão da situação tributária do pedido for proveniente da transação utilizada no pedido, ela será ignorada pela variável. É recomendável que a transação de venda utilizada para o pedido e para a nota fiscal de saída possuam a mesma configuração, no que for relativo à situação tributária. Esta configuração deverá ser diferente somente em casos especiais que exigem tal comportamento;
* Caso a situação tributária seja alterada manualmente na tela Nota Fiscal Saída (F140PRE), o valor inserido na alteração é o que será enviado para a variável VSCODSTR.

## Páginas relacionadas

* [VEN-000ALICM01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_000alicm01.htm#VEN-000ALICM01)
* [Parâmetros da Filial para Vendas (F070FVE)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070fve.htm)
* [Situações Tributárias (F027STR)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f027str.htm)
