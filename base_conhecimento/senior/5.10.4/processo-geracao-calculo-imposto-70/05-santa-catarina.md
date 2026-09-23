# Santa Catarina

> **Fonte:** Cálculo do imposto 70 - ICMS ST Complementar — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/processo-geracao-calculo-imposto-70.htm  
> **Trilha:** Ajuda por telas > Controladoria > Gestão de Tributos > Operações e Cálculos Fiscais > Cálculos > Apuração > F661IA5  
> **Telas citadas:** E661RES, F669DRI  
> **Identificadores de regras:** —

---
## DIME

Conforme publicação da Portaria SEF 7/2019, a DIME foi alterada em decorrência da nova apuração do imposto:

* no quadro 11 do registro 32, foi incluído o campo **115 - Ressarcimento do ICMS substituição tributária acobertado por NF-e**. Nele é gerado os totais de créditos deduzidos os totais de débitos ((E661RES.TOTCRE - E661RES.TOTDEB) na apuração do imposto de tipo 70 - ICMS ST Complementar;
* no registro 46, a origem 3 gera seu valor no item 070 do quadro 09.

Para mais informações, consulte o leiaute de geração da DIME.

## DRCST

O Demonstrativo para Apuração Mensal do Ressarcimento, da Restituição e Complementação do ICMS Substituição Tributária (DRCST) é um arquivo eletrônico, instituído pela portaria SEF 378/2018, referente as vendas de notas fiscais e cupons fiscais, cujo principal intuito é determinar o valor do ICMS e ICMS ST a ser ressarcido em determinado período.

O arquivo é gerado na tela DRCST (F669DRI), onde são listadas as notas fiscais de entrada que dão direito ao ressarcimento do ICMS ST, sendo que a parcela efetiva do ressarcimento é determinada pela nota fiscal ou cupom fiscal de venda.

* Tela Demonstrativo para Apuração Mensal do Ressarcimento, da Restituição e Complementação do ICMS Substituição Tributária.

O processo de ressarcimento do ICMS ST para o estado de SC deve seguir as orientações previstas no inciso I do art. 25º, anexo 3 do RICMS/SC:

1. efetuar nova retenção em favor de outro Estado ou do Distrito Federal na qual a mercadoria esteja sujeita ao regime de substituição tributária;
2. realizar operação com destino a contribuinte localizado em unidade da Federação na qual a mercadoria não esteja sujeita ao regime de substituição tributária;
3. realizar operação com destino a consumidor final não contribuinte do imposto localizado em outra unidade da Federação sujeito ao recolhimento do imposto correspondente à diferença entre a alíquota interna e a interestadual; e
4. promover saídas internas destinadas a empresa optante pelo Simples Nacional, em operações beneficiadas pela redução de 70% (setenta por cento) da MVA, desde que o imposto retido tenha sido calculado mediante utilização de percentual integral da MVA (geração dos movimentos de saída para o módulo de origem **Tributos** para os clientes do Simples Nacional do estado de Santa Catarina e que não sejam consumidor final).

**Observação**

**MVA = Margem de Valor Agregado**, também chamada de IVA (Índice de Valor Agregado) em alguns estados, como SP. Se trata da porcentagem determinada pelas Secretarias da Fazenda dos Governos Estaduais para os produtos (ou grupo de produtos), visando calcular o ICMS que deve ser pago por substituição. Conhecida também como Lucro Substituído, a MVA é aplicada com a finalidade de permitir um maior equilíbrio entre os preços das aquisições internas e interestaduais.

## Páginas relacionadas

* [leiaute de geração da DIME](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f669dme.htm)
* [Demonstrativo para Apuração Mensal do Ressarcimento, da Restituição e Complementação do ICMS Substituição Tributária](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f669dri.htm#menu_controladoria/f669dri.htm)
