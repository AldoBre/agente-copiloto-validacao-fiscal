# Cálculo da Base de Substituição 
de ICMS | Critério 2

> **Fonte:** F019TIS - Tipos Substituições Impostos / Modalidade Base Cálculo / Antecipação - Por Estado — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f019tis.htm  
> **Trilha:** Ajuda por telas > Cadastros > Mercado e Suprimentos > Parâmetros Fiscais > Substituições Impostos/Modalidade Base Cálculo/Antecipação  
> **Telas citadas:** —  
> **Identificadores de regras:** —

---
Cálculo da Base de Substituição de ICMS quando o
critério de cálculo é "2 - Pelo Preço Unitário Base", utilizando uma tabela de preço para buscar o preço
da substituição.

1. Definição da Base de Cálculo da Substituição (há três possibilidades):

* Sempre considerar o preço da tabela de preço de
  substituição.
* Se o preço informado no pedido ou na nota fiscal de saída for menor que o
  preço da tabela de preço de substituição, considerar o preço informado no pedido
  ou nota. Se o preço informado na nota de saída ou no pedido for maior que o
  preço da tabela de preço de substituição, considerar o preço da tabela.  

  Este é o padrão do sistema. Ou seja, sempre irá considerar o menor preço entre o
  informado na nota fiscal de saída ou pedido e o preço da tabela de preço da
  substituição;
* Se o preço informado no pedido ou na nota fiscal de saída for menor que o
  preço da tabela de preço de substituição, considerar o preço informado na tabela
  de preço de substituição. Se o preço informando na nota fiscal de saída ou no
  pedido for maior que o preço da tabela de preço de substituição, considerar o
  preço do pedido ou nota fiscal de saída;  

  Ou seja, sempre irá considerar o maior
  preço entre o informado na nota fiscal de saída ou pedido e o preço da tabela de
  preço da substituição.

**Nota**

O sistema soma o valor do IPI na Base de Cálculo do ICMS próprio e do DIFAL quando o campo IPI Base estiver parametrizado como "S - Sim";

2. Descontar o ICMS Normal da operação (há duas
   possibilidades):

* Não aplicar nenhum desconto sobre o valor de substituição calculado. Este
  será o padrão do sistema.
* Descontar do valor de substituição o valor do ICMS normal e o Desconto da Zona
  Franca.

Ambos os parâmetros serão aplicados quando o critério de cálculo da tabela de
substituição de ICMS for utilizado como "2 - Pelo Preço Unitário Base". Quando o
critério de substituição de imposto for "1 - Pela Margem de Lucro", apenas o
parâmetro Descontar o ICMS Normal da Operação estará disponível.

Esse último
parâmetro foi adicionado para o critério 1 também, sendo que o imposto calculado
com base nesse critério sempre era deduzido o ICMS Normal e o Desconto da Zona
Franca.
