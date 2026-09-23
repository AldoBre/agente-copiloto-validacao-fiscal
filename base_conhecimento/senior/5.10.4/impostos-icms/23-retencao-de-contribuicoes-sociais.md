# Retenção de contribuições sociais

> **Fonte:** Rotinas de ICMS — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/impostos-icms.htm#retencao-sociais  
> **Trilha:** Segmentos > Compliance > Configurações para cálculos fiscais > Impostos  
> **Telas citadas:** F019RET, F070FEF  
> **Identificadores de regras:** —

---
Nos casos em que o valor do DARF for igual ou inferior a R$ 10,00 (dez reais), está dispensada a retenção das contribuições sociais (PIS, COFINS e CSLL), exceto na hipótese de Documento de Arrecadação de Receitas Federais - DARF eletrônico efetuado por meio do SIAFI, eliminando a cumulatividade mensal.

Para realizar o controle de retenções por documento e cumulativo, o limite (R$ 10,00) deve ser informado no campo Valor mínimo p/ retenção das contrib. Sociais, que estará disponível para edição quando o parâmetro Controle diário de retenções das contribuições sociais estiver igual a S - Sim. Estes campos estão disponíveis na guia Impostos 2 da tela de Parâmetros da Filial para Tributos (F070FEF).

O controle é exibido de forma diária nas telas de controles de retenção de impostos (F019RET).

Com essa configuração, o limite de retenção é verificado através da soma dos valores das contribuições sociais retidas das notas fiscais de entrada ou saída dentro do respectivo dia, que devem resultar em valor superior ao limite informado no parâmetro da filial.

## Páginas relacionadas

* [F070FEF](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070fef.htm)
* [F019RET](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f019ret.htm)
