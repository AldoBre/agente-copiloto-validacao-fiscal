# Cálculo do PIS/COFINS por quantidade

> **Fonte:** PIS/COFINS — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/impostos_pis_cofins.htm  
> **Trilha:** Segmentos > Compliance > Configurações para cálculos fiscais > Impostos  
> **Telas citadas:** F022CLF, F075PRO, F081TPA  
> **Identificadores de regras:** —

---
Cadastrar uma tabela de preço com a Aplicação 3, 4 ou 5.

* Cadastros > Mercado e Suprimentos > Tabelas de Preço > Cadastro (F081TPA)

Na guia Itens Produto, informe o Valor do imposto por cada unidade constante no documento fiscal.

No cadastro do produto, informar o Código Tabela Preço PIS e Código Tabela Preço COFINS.

Campos da tela de cálculo do item da nota de entrada.

![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/images/imposto_pis_cofins015_thumb_0_48.png)

Para o cálculo do PIS/COFINS por quantidade nos documentos fiscais de saída, ainda é necessário atribuir no item da nota a situação tributária 03 (Operação tributável com alíquota por unidade de medida de produto).

Tributação por Valor Mínimo por Unidade de Medida 

Esse campo, presente nas telas de Cadastro de Produtos (F075PRO) e na Classificações Fiscais(F022CLF), indica se o valor de imposto calculado por percentual deve ser comparado com o valor parametrizado para o item na tabela de tributação por quantidade cadastrada.

Quando o campo estiver configurado como "S - Sim":  
a) Se o valor do imposto calculado for inferior ao valor definido na tabela de tributação, será adotado esse valor da tabela de tributação. Isso significa que a tributação será feita por quantidade, e não mais por percentual.

b) Nessa configuração, o sistema só calculará PIS/COFINS faturamento por quantidade caso a CST (Código de Situação Tributária) seja 04 ou 06.

Quando o campo estiver configurado como "N - Não":  
a) O sistema não compara com o valor calculado: sempre será utilizado o valor fixo cadastrado na tabela de tributação, ou seja, a tributação será feita por quantidade também.

b) No entanto, o sistema só calculará PIS/COFINS faturamento por quantidade se a CST for 03 - Operação tributável com alíquota por unidade de medida do produto, ou se o tipo da nota for "2 - Devolução" e a CST for 49 - Outras Operações de Saída.

## Páginas relacionadas

* [Cadastro (F081TPA)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f081tpa.htm)
* [F075PRO](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075pro.htm)
* [F022CLF](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f022clf.htm)
