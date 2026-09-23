# Cálculo da Base de Substituição de ICMS | Critérios 1 e 3

> **Fonte:** F019TIS - Tipos Substituições Impostos / Modalidade Base Cálculo / Antecipação - Por Estado — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f019tis.htm  
> **Trilha:** Ajuda por telas > Cadastros > Mercado e Suprimentos > Parâmetros Fiscais > Substituições Impostos/Modalidade Base Cálculo/Antecipação  
> **Telas citadas:** —  
> **Identificadores de regras:** —

---
Para realização do cálculo, utiliza os seguintes campos: a opção Valor Líquido Aquisição, do campo Formação Base da guia Substituição Imposto / Modalidade Base Cálculo por estado, disponível quando o critério de substituição for 1 – Pela Margem de Lucro ou 3 – Comparação da base calculada pela margem e pelo preço unitário utilizando maior valor.

Quando o campo Formação Base estiver parametrizado como Valor Líquido Aquisição, o cálculo do ICMS ST utiliza como base padrão o valor líquido da última nota fiscal de entrada para o produto, adquirido pela filial.

Quando o critério de substituição de imposto for 1 (Pela Margem de Lucro), o parâmetro Descontar o ICMS Normal da Operação ficará disponível.

Quando o critério de substituição de imposto for 1 (Pela Margem de Lucro) e o campo Formação Base estiver parametrizado como "T - Tabela de Preço", o cálculo do ICMS ST utiliza como base padrão o valor informado na tabela de preço, respeitando a opção do campo Definição da Base de cálculo ("1 - Considerar preço da tabela de preço" / "2 - Considerar o menor preço"/ "3 - Considerar o maior preço").

## Exemplo:

Cálculo utilizando a opção 3 - Considerar o maior preço:

* Quantidade: 10
* Valor Unitário: R$ 10,00
* Preço Pauta: R$ 11,85
* MVA: 79%

O cálculo da Base do ICMS ST:

* (Quantidade \* Preço Pauta) \* (1 + MVA)
* ((10 \* 11,85) \* (1 + 0,79)) = R$ 212,12

Descontar o ICMS Normal da Operação

Há três possibilidades:

1. Não aplicar nenhum desconto sobre o valor de substituição calculado. Este é o padrão do sistema;
2. Descontar o valor do ICMS normal e o Desconto da Zona Franca do valor de substituição;
3. Descontar o valor do ICMS normal do valor de substituição, aplicando a redução da Base ICMS ST:
   1. Base ICMS ST = Base ICMS + %MVA - %  
      Redução Base ICMS ST
      Valor ICMS ST = ((Base ICMS ST \* %ICMS ST) - ((Base ICMS - %Redução Base ICMS ST) \* %ICMS))
