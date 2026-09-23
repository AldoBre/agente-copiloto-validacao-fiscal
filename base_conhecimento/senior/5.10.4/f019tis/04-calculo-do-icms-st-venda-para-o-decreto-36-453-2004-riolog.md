# Cálculo do ICMS ST Venda para o Decreto 36.453/2004 - RIOLOG

> **Fonte:** F019TIS - Tipos Substituições Impostos / Modalidade Base Cálculo / Antecipação - Por Estado — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f019tis.htm  
> **Trilha:** Ajuda por telas > Cadastros > Mercado e Suprimentos > Parâmetros Fiscais > Substituições Impostos/Modalidade Base Cálculo/Antecipação  
> **Telas citadas:** F070PSE  
> **Identificadores de regras:** —

---
Esta tela possibilita que o valor de partida para a composição da base de cálculo da ST seja o valor da aquisição mais recente do produto/mercadoria da filial, que corresponde ao valor contábil (valor líquido da nota fiscal), em atendimento ao Decreto 36.453/2004 do Rio de Janeiro (RIOLOG).

Para realização do cálculo, utilizam os seguintes campos:

* A opção **Valor Líquido Aquisição**, do campo **Formação Base** da guia **Substituição Imposto / Modalidade Base Cálculo por estado**, disponível quando o critério de substituição for 1 – Pela Margem de Lucro ou 3 – Comparação da base calculada pela margem e pelo preço unitário utilizando maior valor;
* A opção **3 – Descontar ICMS Normal + Somar Fundo de Combate à Pobreza (FCP)** no campo **Tipo Desconto ICMS**, quando selecionada o sistema deduz o valor do ICMS do cálculo do ICMS ST e soma o valor do FCP (base de cálculo de ICMS multiplicado pelo percentual cadastrado na tela Parâmetos Fiscais (F070PSE)).
* O campo **Percentual mínimo de Imposto Substituição** que indica qual o percentual mínimo que o valor do ICMS ST deve corresponder da base de cálculo. Desta forma, quando o cálculo do ICMS ST for menor que o valor mínimo, o valor do ICMS ST listado na nota fiscal é o valor mínimo.

  ## Exemplo

  % Valor Mínimo ICMS ST = 2%;

  + Base ICMS ST = R$ 1.000,00;
  + Valor ICMS ST calculado pelo sistema = R$ 11,50;
  + Valor mínimo = R$ 20,00.

  Valores apresentados na nota fiscal:

  + Base ICMS ST = R$ 1.000,00;
  + Valor ICMS ST = R$ 20,00.

## Cálculo do ICMS ST

Quando o campo **Formação Base** estiver parametrizado como **Valor Líquido Aquisição**, o cálculo do ICMS ST utiliza como base padrão o valor líquido da última nota fiscal de entrada para o produto, adquirido pela filial;

* Caso a última entrada for por importação, ou seja, tipo 7, utiliza o valor bruto da venda menos os descontos;
* Caso a última entrada for uma nota de entrada tipo 1, utiliza o valor líquido como base de cálculo padrão; e
* Caso a última entrada for uma transferência, considera a última entrada da filial de origem da transferência. Caso ela também for uma transferência, busca na filial de origem a última entrada até encontrar uma nota de entrada tipo 1 ou 7. Se for tipo 7 considera o valor, e se for tipo 1, soma o valor do IPI da nota de origem ao valor líquido da transferência.

Se a opção **Descontar ICMS Normal (sem FCP) e Zona Franca** estiver selecionada no campo **Tipo Desconto ICMS** o cálculo do ICMS ST subtrai o valor do Fundo de Combate a Pobreza do valor de ICMS Normal a ser descontado.

Quando o campo **% Min. ICMS ST** for informado, calcula o valor mínimo usando o percentual informado no campo e verifica o valor do ICMS ST calculado, se o mesmo for menor que o valor mínimo calculado, usa o valor mínimo calculado como ICMS ST.

### Exemplo de cálculo ICMS ST

Produto **A**:

* Preço de venda: R$ 49,90;
* Valor de aquisição da última compra do produto **A**: R$ 38,76;
* Alíquota ICMS: 19% (com FCP);
* Alíquota ICMS: 18% (sem FCP);
* Redução Base de cálculo: 68,42%;
* % MVA: 53,19%
* IPI: 0,00;
* Base de cálculo ICMS: R$ 34,14 (49,90 \* 68,42%);
* Valor ICMS: R$ 6,49 (34,14 \* 19%).

Base de ICMS ST = (Quantidade x valor de aquisição + IPI x MVA x % redução riolog):

* 1 x 38,76 + 0,00 x 1,5319 x 68,42% = 40,63.

Valor ICMS ST = (Base ICMS ST x alíquota interna – Valor ICMS Rio Log (Cálculo do ICMS Sem fundo de combate à pobreza):

* 40,63 x 0,19 – 6,15 (34,14 \* 18%) = 1,57.

## Páginas relacionadas

* [F070PSE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070pse.htm#menu_cadastros/f070pse.htm)
