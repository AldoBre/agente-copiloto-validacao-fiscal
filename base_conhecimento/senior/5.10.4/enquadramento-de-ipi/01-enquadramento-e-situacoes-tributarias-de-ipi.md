# Enquadramento e Situações Tributárias de IPI

> **Fonte:** Enquadramento e Situações Tributárias de IPI — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/enquadramento-de-ipi.htm  
> **Trilha:** Segmentos > Compliance > Configurações para cálculos fiscais > Impostos > IPI  
> **Telas citadas:** F001TVE, F022CLF, F027EQI, F075GFP, F075PCA, F075PRO, F075PXT, F403LFP  
> **Identificadores de regras:** COM-000ALENQ01, COM-000ALSTR02

---
Segmentos > Compliance > Configurações para cálculos fiscais  > Impostos  > IPI > Enquadramento de IPI

|  |  |
| --- | --- |
|  | Veja também: |

* IPI
* Cálculo do IPI

O código de enquadramento de IPI é utilizado para especificar a utilização do código de situação tributária (CST). A partir de 01/01/2016, tornou-se obrigatório a utilização do mesmo. Para mais informações, acesse a nota técnica NT 2015.002.

O enquadramento de IPI é configurado através do campo Código do enquadramento, presente nas telas de Cadastros de Produto, Classificações Fiscais, Transações de Venda, Transações de Compra, Notas Fiscais de Entrada, Notas Fiscais de Saída, Ligação Produto x Cliente, Ligação Produto x Fornecedor e Ligação Produto x Transação. Para cadastrar o Código do Enquadramento de IPI, utilize a tela Enquadramento de IPI (F027EQI).

## Sugestão para o código de Enquadramento de IPI

O código de enquadramento de IPI dos produtos é sugerido na seguinte ordem:

1. Ligação Produto x Cliente (F075PCA) / Ligação Produto x Fornecedor (F403LFP)
2. Ligação Produto x Transação (F075PXT)
3. Produto (F075PRO e F075GFP)
4. Transação (F001TVE)
5. Classificação Fiscal (F022CLF)

A sugestão para os itens de serviço ou sem produto informado segue a ordem abaixo:

1. Transação
2. Classificação Fiscal

Importante

Após a sugestão do sistema é possível alterar o código de enquadramento executando o identificador de regras COM-000ALENQ01.

## Sugestão para o código de Situação Tributária de IPI

A sugestão do código de situação tributária de IPI (CST) depende da definição de um código de enquadramento de IPI.

O código de Situação tributária de IPI é sugerido na seguinte ordem:

1. Situação tributária vinculada ao código de enquadramento legal do IPI do item
2. Situação tributária de IPI informada no cadastro da transação do item
3. Situação tributária de IPI do enquadramento vinculado à transação
4. Situação tributária de IPI informada no cadastro do produto
5. Situação tributária de IPI do enquadramento vinculado ao produto
6. Situação tributária de IPI do enquadramento vinculado à classificação fiscal
7. Situação tributária de IPI conforme tabela de IPI informada na classificação fiscal
   * Nessa situação, a sugestão considera se a nota é de entrada ou saída e a definição do campo Tributação de IPI da tela Classificações Fiscais (F022CLF). Desta forma, o código da situação tributária de IPI será uma das opções abaixo

| Indicativo do tipo de tributação de IPI | Nota de Entrada | Nota de Saída |
| --- | --- | --- |
| 0 - Normal | 00 | 50 |
| 1 - Tributada com Alíquota zero | 01 | 51 |
| 2 - Isenta | 02 | 52 |
| 3 - Não Tributada | 03 | 53 |
| 4 - Imune | 04 | 54 |
| 5 - Com Suspensão | 05 | 55 |
| 9 - Outros | 49 | 99 |

Importante

Após a sugestão do sistema é possível alterar o código de situação tributária de IPI executando o identificador de regras COM-000ALSTR02.

## Validações CST X Código Enquadramento de IPI

* Se o CST de IPI for de Isenção ("02" ou "52"), o Código de Enquadramento deve ser de "301" a "399"
* Se o CST de IPI for de Imunidade ("04" ou "54"), o Código de Enquadramento deve ser de "001" a "099"
* Se o CST de IPI for de Suspensão ("05" ou "55"), o Código de Enquadramento deve ser de "101" a "199"
* Para os demais, deve-se informar "999" (tributação normal e outros) ou os códigos de "601" a "608" (redução)

Como o código de enquadramento "999" é indicado para todas as situações que não se encaixam entre isenção, suspensão e imunidade, a informação da situação tributária para este enquadramento deve permanecer em branco (campos Sit. Trib. IPI para NF Entrada e Sit. Trib. IPI para NF Saída) na tela Enquadramento do IPI (F027EQI), para que seja sugerido automaticamente para essas situações.

**Observação**

Lembrando que, para não ocorrer a mensagem de enquadramento incompatível na sugestão padrão 999 para situações tributárias de IPI que são de isenção, suspensão ou imune, obrigatoriamente deve haver CST e o enquadramento informado em um destes cadastros: na transação, ligação produto X cliente, produto ou classificação fiscal. Se não for informado o enquadramento gerará a mensagem "Enquadramento 999 sugerido por padrão pelo sistema não é compatível com a Situação Tributária de IPI XX sugerida do cadastro da transação" ao digitar a nota.

Para utilizar o código de enquadramento "999", o CST IPI do item não poderá estar vinculado com nenhum código de enquadramento de IPI. Do contrário, será apresentada a mensagem: "Enquadramento não é compatível com a Situação tributária de IPI selecionada", impedindo a utilização do código "999".

## Páginas relacionadas

* [IPI](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/impostos_ipi.htm)
* [Cálculo do IPI](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/processo_geracao_calculo_ipi.htm)
* [NT 2015.002](http://www.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=tW+YMyk/50s=)
* [F027EQI](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f027eqi.htm)
* [F075PCA](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075pca.htm#enquadramento_legal_do_ipi)
* [F403LFP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f403lfp.htm#enquadramento_legal_do_ipi)
* [F075PXT](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075pxt.htm#enquadramento_legal_do_ipi)
* [F075PRO](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075pro.htm#enquadramento-de-ipi)
* [F075GFP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075gfp.htm#enquadramento-de-ipi)
* [F001TVE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f001tve.htm#enquadramento-legal-ipi)
* [F022CLF](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f022clf.htm#enquadramento-legal-ipi)
* [F022CLF](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f022clf.htm)
