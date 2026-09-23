# Grupo N07 - Grupo Tributação do ICMS= 51

> **Fonte:** Leiautes NF-e e NFC-e — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/leiaute-nf-e-nfc-e.htm  
> **Trilha:** Segmentos > Compliance > Documentos Eletrônicos > NF-e | NFC-e (Nota Fiscal Eletrônica) > Nota Fiscal Eletrônica 4.0  
> **Telas citadas:** F051DIS, F070FVE  
> **Identificadores de regras:** VEN-140NEITE01

---
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação | Origem |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 205 | N07 | ICMS51 | Grupo Tributação do ICMS = 51 | CG | N01 |  | 1-1 |  | Tributação com Diferimento (a exigência do preenchimento das informações do ICMS diferido fica a critério de cada UF) | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 206 | N11 | orig | Origem da mercadoria | E | N07 | N | 1-1 | 1 | 0 - Nacional, exceto as indicadas nos códigos 3, 4, 5 e 8; 1 - Estrangeira - Importação direta, exceto a indicada no código 6; 2 - Estrangeira - Adquirida no mercado interno, exceto a indicada no código 7; 3 - Nacional, mercadoria ou bem com Conteúdo de Importação superior a 40% e inferior ou igual a 70%; 4 - Nacional, cuja produção tenha sido feita em conformidade com os processos produtivos básicos de que tratam as legislações citadas nos Ajustes; 5 - Nacional, mercadoria ou bem com Conteúdo de Importação inferior ou igual a 40%; 6 - Estrangeira - Importação direta, sem similar nacional, constante na lista da CAMEX e gás natural; 7 - Estrangeira - Adquirida no mercado interno, sem similar nacional, constante na lista CAMEX e gás natural; 8 - Nacional, mercadoria ou bem com Conteúdo de Importação superior a 70% | Gera por padrão o valor do campo E140Ipv.OriMer. Pode ser alterado utilizando o identificador de regras VEN-140NEITE01 através da variável VSIntImpOri. |
| 207 | N12 | CST | Tributação do ICMS = 51 | E | N07 | N | 1-1 | 2 | 51=Diferimento | Gera por padrão o valor do campo E140Ipv.OriMer + E140Ipv.CodStr. Pode ser alterado utilizando o identificador de regra VEN-140NEITE01 através da variável VSIntImpCst. |
| 208 | N13 | modBC | Modalidade de determinação da BC do ICMS | E | N07 | N | 0-1 | 1 | 0=Margem Valor Agregado (%); 1=Pauta (valor); 2=Preço Tabelado Máx. (valor); 3=Valor da operação | Verifica o valor do campo E140Ipv.CodBic para buscar o valor do campo E019Tst.CalSub e gerar na tag. Pode ser alterado utilizando o identificador de regra VEN-140NEITE01 através da variável VSIntImpMbc. |
| 209 | N14 | pRedBC | Percentual da Redução de BC | E | N07 | N | 0-1 | 3v2-4 |  | Gera a informação que consta no campo E019Red.RedEnt. Pode ser alterado utilizando o identificador de regra VEN-140NEITE01 variável VSIntImpRbc. |
| 209.01 | N14.1 | cBenefRBC | Código do benefício fiscal para redução de base de cálculo com diferimento | E | N07 | C | 0-1 | 10 | Incluído na NT2019.001 | A tag é gerada conforme o campo Ben. Fiscal Red. Base da tela F051DIS. |
| 210 | N15 | vBC | Valor da BC do ICMS | E | N07 | N | 0-1 | 13v2 |  | Se na tela F070FVE, guia Vendas 2, o campo Tipo Cálculo Diferimento for igual a 1, gera o valor que consta no campo E140Ipv.VlrBic. Se o campo estiver com o valor igual a 2, gera o valor da soma dos campos E140Ipv.VlrBic + E140Ipv.BasIdf. |
| 211 | N16 | pICMS | Alíquota do Imposto | E | N07 | N | 0-1 | 3v2-4 | Alíquota do ICMS sem o FCP. Quando for o caso, informar a alíquota do FCP no campo pFCP (Atualizado NT2016.002) | Se o campo E140Ipv.PerDif for igual a 100%, então gera o valor do campo E140Ipv.PerIdf. Caso contrário, gera o valor do campo PerIcm. |
| 211.01 | N16a | vICMSOp | Valor do ICMS da Operação | E | N07 | N | 0-1 | 13v2 | Valor como se não tivesse o diferimento | Gera a informação que consta no campo E140Ipv.VlrIdf. |
| 211.02 | N16b | pDif | Percentual do diferimento | E | N07 | N | 0-1 | 3v2-4 | No caso de diferimento total, informar o percentual de diferimento "100" | Gera a informação que consta no campo E140Pvd.AliImf. |
| 211.03 | N16c | vICMSDif | Valor do ICMS diferido | E | N07 | N | 0-1 | 13v2 |  | Gera a informação que consta no campo E140Ipv.VlrIdf. |
| 212 | N17 | vICMS | Valor do ICMS | E | N07 | N | 0-1 | 13v2 | Informar o valor realmente devido | Gera a informação que consta no campo E140Ipv.VlrIcm. |
| 212.0 | N17.1 | -x- | Sequência XML | G | N07 |  | 0-1 |  | Grupo opcional (Incluído na NT2016.002) | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 212.w | N17a | vBCFCP | Valor da Base de Cálculo do FCP | E | N17.1 | N | 1-1 | 13v2 | Informar o valor da Base de Cálculo do FCP | Gera a informação que consta no campo E140Pvd.BasFcp. |
| 212.x | N17b | pFCP | Percentual do ICMS relativo ao Fundo de Combate à Pobreza (FCP) | E | N17.1 | N | 1-1 | 3v2-4 | Percentual relativo ao Fundo de Combate à Pobreza (FCP) | Gera a informação que consta no campo E140Pvd.AliFcp. |
| 212.y | N17c | vFCP | Valor do ICMS relativo ao Fundo de Combate à Pobreza (FCP) | E | N17.1 | N | 1-1 | 13v2 | Valor do ICMS relativo ao Fundo de Combate à Pobreza (FCP) | Gera a informação que consta no campo E140Pvd.VlrFcp. |

## Páginas relacionadas

* [VEN-140NEITE01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_140neite01.htm)
* [F051DIS](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f051dis.htm)
* [F070FVE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070fve.htm)
