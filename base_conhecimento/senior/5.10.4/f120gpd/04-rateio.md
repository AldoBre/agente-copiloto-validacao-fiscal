# Rateio

> **Fonte:** F120GPD - Entrada de Pedidos Agrupado — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f120gpd.htm  
> **Trilha:** Ajuda por telas > Mercado > Gestão de Vendas > Pedidos  
> **Telas citadas:** —  
> **Identificadores de regras:** —

---
Rateio

Consulta dos rateios.

Cód. Análise Custos

Exibe o código da análise valorizada de custos ligada ao pedido informado. Será visualizado apenas quando for configurado no
campo **C**, disponível no lado esquerdo da grade.

Reserva

Define se haverá reserva do item ao fechar o pedido. A reserva é feita no depósito padrão ou, se definido em identificador, no depósito
informado.

**Observação**

Ao utilizar alguma ordenação em qualquer uma das grades dessas guias, o sistema não considera a ordenação numérica para campos do tipo String e sim a de caracteres num geral, onde as palavras que começam com o número 1 independente de qual número o segue, ficará sempre anterior ao 2. Por exemplo: a coluna **SeqPcl** no banco, referente ao **Seq.Ped Cli** na tela.

## Itens da receita

O preenchimentos dos campos desta guia varia de acordo com a origem das informações.

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

Quando no cadastro de produto do item informado na grid de produtos, o campo **Emite Receituário** estiver igual a "S - Sim", a grade dos dados dos itens da receita ficará disponível para inserção/edição.

#### Campos

**Valor Calda**

Calculado automaticamente pelo sistema após o usuário digitar o valor da dose.

**Número de Aplicações**

Calculado automaticamente pelo sistema após o usuário digitar o valor da dose.

**Valor da área**

Calculado automaticamente pelo sistema após o usuário digitar o valor da dose.

**Importante**

Só é permitido inserir um item de receita na grade itens da receita, por item de pedido e é possivel inserir somente um registro de dados dos itens da receita para cada item informado no pedido.
