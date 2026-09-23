# Grupo N07a - Grupo Tributação do ICMS= 53

> **Fonte:** Leiautes NF-e e NFC-e — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/leiaute-nf-e-nfc-e.htm  
> **Trilha:** Segmentos > Compliance > Documentos Eletrônicos > NF-e | NFC-e (Nota Fiscal Eletrônica) > Nota Fiscal Eletrônica 4.0  
> **Telas citadas:** F070FCA  
> **Identificadores de regras:** —

---
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação | Origem |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 212.09 | N07a | ICMS53 | Grupo Tributação do ICMS Monofásico | CG | N01 |  | 1-1 |  | Tributação monofásica sobre combustíveis com recolhimento diferido | Gerado conforme o padrão do leiaute da SEFAZ |
| 212.10 | N11 | orig | Origem da mercadoria | E | N07a | N | 1-1 | 1 | Lista * 0 - Nacional, exceto as indicadas nos códigos 3, 4, 5 e 8 * 1 - Estrangeira - Importação direta, exceto a indicada no código 6 * 2 - Estrangeira - Adquirida no mercado interno, exceto a indicada no código 7 * 3 - Nacional, mercadoria ou bem com Conteúdo de Importação superior a 40% e inferior ou igual a 70% * 4 - Nacional, cuja produção tenha sido feita em conformidade com os processos produtivos básicos de que tratam as legislações citadas nos Ajustes * 5 - Nacional, mercadoria ou bem com Conteúdo de Importação inferior ou igual a 40% * 6 - Estrangeira - Importação direta, sem similar nacional, constante em lista da CAMEX e gás natural * 7 - Estrangeira - Adquirida no mercado interno, sem similar nacional, constante lista CAMEX e gás natural * 8 - Nacional, mercadoria ou bem   com Conteúdo de Importação superior a 70% |  |
| 212.11 | N12 | CST | Tributação do ICMS | E | N07a | N | 1-1 | 2 | 53= Tributação monofásica sobre combustíveis com recolhimento diferido |  |
| 212.12 | N37a | qBCMono | Quantidade tributada | E | N07a | N | 0-1 | 11v0-4 | Informar a BC do ICMS próprio em quantidade conforme a unidade de medida estabelecida na legislação para o produto |  |
| 212.13 | N38 | adRemICMS | Alíquota *ad rem* do imposto | E | N07a | N | 0-1 | 3v2-4 | Alíquota *ad rem* do ICMS estabelecida na legislação para o produto |  |
| 212.14 | N41a | vICMSMonoOp | Valor do ICMS da operação | E | N07a | N | 0-1 | 13v2 | O valor do ICMS é obtido pela multiplicação da alíquota *ad rem* pela quantidade do produto, conforme a unidade de medida estabelecida em legislação, como se não houvesse diferimento |  |
| 212.15 | N42 | pDif | Percentual do diferimento | E | N07a | N | 0-1 | 3v2-4 | No caso de diferimento total, informe o percentual de diferimento "100" |  |
| 245.74 | N43 | vICMSMonoDif | Valor do ICMS diferido | E | N07a | N | 0-1 | 13v2 | O valor do ICMS é obtido pela multiplicação da alíquota *ad rem* pela quantidade do produto, conforme a unidade de medida estabelecida, multiplicado pelo percentual de diferimento |  |
| 212.18 | N39 | vICMSMono | Valor do ICMS próprio devido | E | N07a | N | 0-1 | 13v2 | O valor do ICMS próprio devido é o resultado do valor do ICMS da operação menos valor do ICMS diferido | Para emitir esse campo zerado ao utilizar um produto do tipo combustível e havendo diferimento total, ative o parâmetro dinâmico NOTAFISCAL.XML.ICMS.MONOFASICO.DIFERIMENTO.GERAVICMSMONO, acessado a partir da tela Cadastro de Filiais (F070FCA), botão Par. Dinâmicos |

## Páginas relacionadas

* [NOTAFISCAL.XML.ICMS.MONOFASICO.DIFERIMENTO.GERAVICMSMONO](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000ppd.htm)
* [Cadastro de Filiais (F070FCA)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070fca.htm)
