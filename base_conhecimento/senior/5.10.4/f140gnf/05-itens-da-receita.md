# Itens da receita

> **Fonte:** F140GNF - Notas Fiscais de Saída — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f140gnf.htm  
> **Trilha:** Ajuda por telas > Mercado > Gestão de Faturamento e Outras Saídas > Notas Fiscais de Saída  
> **Telas citadas:** F113REM  
> **Identificadores de regras:** —

---
O preenchimentos dos campos desta grade variam de acordo com a origem das informações.

| Nome | Tipo | Condição | Descrição | Estrutura |
| --- | --- | --- | --- | --- |
| CodEmb | Número | Obrigatório | Código da embalagem | Grade Itens da Receita |
| CodEtp | Número | Obrigatório | Código da espécie/cultura | Grade Itens da Receita |
| CodDpp | Número | Obrigatório | Código da praga/problema | Grade Itens da Receita |
| CodDia | Número | Obrigatório | Código do diagnóstico | Grade Itens da Receita |
| CodAtp | Número | Obrigatório | Código do tipo de aplicação | Grade Itens da Receita |
| QtdDos | Número | Obrigatório | Quantidade da dose | Grade Itens da Receita |
| VlrCal | Número | Opcional | Calda | Grade Itens da Receita |
| UniMed | Alfa | Obrigatório | Unidade de Medida | Grade Itens da Receita |
| NumApl | Número | Opcional | Número de aplicações | Grade Itens da Receita |
| VlrAre | Número | Opcional | valor da Area | Grade Itens da Receita |

**Observação**

Quando, no cadastro de produto do item informado na grade de Produtos, o campo **Emite Receituário** for igual a "S - Sim", a grade dos dados dos itens da receita ficará disponível para inserção/edição.

#### Campos

**Valor Calda**

Calculado automaticamente pelo sistema após o usuário digitar o valor da dose.

**Número de Aplicações**

Calculado automaticamente pelo sistema após o usuário digitar o valor da dose.

**Valor da área**

Calculado automaticamente pelo sistema após o usuário digitar o valor da dose.

**Importante**

Só é permitido inserir um item de receita na grade itens da receita, por item de pedido e é possivel inserir somente um registro de dados dos itens da receita para cada item informado no pedido.

Ao clicar em **fechar nota**, caso informados itens que necessitam da emissão do receituário agronômico, o sistema chama a tela F113REM e ao abrir a mesma, os dados dos itens da receita já serão importados para a grid de itens da receita desta tela.

## Páginas relacionadas

* [F113REM](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f113rem.htm)
