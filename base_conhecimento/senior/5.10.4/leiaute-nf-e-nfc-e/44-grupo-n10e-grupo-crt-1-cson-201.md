# Grupo N10e - Grupo CRT=1 (CSON 201)

> **Fonte:** Leiautes NF-e e NFC-e — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/leiaute-nf-e-nfc-e.htm  
> **Trilha:** Segmentos > Compliance > Documentos Eletrônicos > NF-e | NFC-e (Nota Fiscal Eletrônica) > Nota Fiscal Eletrônica 4.0  
> **Telas citadas:** —  
> **Identificadores de regras:** VEN-140NEITE01

---
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação | Origem |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 245.27 | N10e | ICMSSN201 | Grupo CRT=1 - Simples Nacional e CSON=201 | CG | N01 |  | 1-1 |  | Tributação ICMS pelo Simples Nacional, CSON=201 (v2.0) | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 245.28 | N11 | orig | Origem da mercadoria | E | N10e | N | 1-1 | 1 | 0 - Nacional, exceto as indicadas nos códigos 3, 4, 5 e 8; 1 - Estrangeira - Importação direta, exceto a indicada no código 6; 2 - Estrangeira - Adquirida no mercado interno, exceto a indicada no código 7; 3 - Nacional, mercadoria ou bem com Conteúdo de Importação superior a 40% e inferior a 70%; 4 - Nacional, cuja produção tenha sido feita em conformidade com os processos produtivos básicos de que tratam as legislações citadas nos Ajustes; 5 - Nacional, mercadoria ou bem com Conteúdo de Importação inferior ou igual a 40%; 6 - Estrangeira - Importação direta, sem similar nacional, constante em lista da CAMEX e gás natural; 7 - Estrangeira - Adquirida no mercado interno, sem similar nacional, constante lista CAMEX e gás natural; 8 - Nacional, mercadoria ou bem com Conteúdo de Importação superior a 70%. | Gera por padrão o valor do campo E140Ipv.OriMer. Pode ser alterado utilizando o identificador de regras VEN-140NEITE01 através da variável VSIntImpOri. |
| 245.29 | N12a | CSOSN | Código de Situação da Operação - Simples Nacional | E | N10e | N | 1-1 | 3 | 201=Tributada pelo Simples Nacional com permissão de crédito e com cobrança do ICMS por Substituição Tributária (v2.0) | Gera a informação que consta no campo E140Ipv.CodStr |
| 245.30 | N18 | modBCST | Modalidade de determinação da BC do ICMS ST | E | N10e | N | 1-1 | 1 | 0=Preço tabelado ou máximo sugerido; 1=Lista Negativa (valor); 2=Lista Positiva (valor); 3=Lista Neutra (valor); 4=Margem Valor Agregado (%); 5=Pauta (valor) |  |
| 245.31 | N19 | pMVAST | Percentual da margem de valor Adicionado do ICMS ST | E | N10e | N | 0-1 | 3v2-4 | (v2.0) |  |
| 245.32 | N20 | pRedBCST | Percentual da Redução de BC do ICMS ST | E | N10e | N | 0-1 | 3v2-4 | (v2.0) |  |
| 245.33 | N21 | vBCST | Valor da BC do ICMS ST | E | N10e | N | 1-1 | 13v2 | (v2.0) |  |
| 245.34 | N22 | pICMSST | Alíquota do imposto do ICMS ST | E | N10e | N | 1-1 | 3v2-4 | Alíquota do ICMS ST sem o FCP. Quando for o caso, informar a alíquota do FCP no campo pFCP (Atualizado NT2016.002) |  |
| 245.35 | N23 | vICMSST | Valor do ICMS ST | E | N10e | N | 1-1 | 13v2 | Valor do ICMS ST retido (v2.0) |  |
| 245.35.0 | N23.1 | -x- | Sequência XML | G | N10e |  | 0-1 |  | Grupo opcional (Incluído na NT 2016.002) |  |
| 245.35w | N23a | vBCFCPST | Valor da Base de Cálculo do FCP | E | N23.1 | N | 1-1 | 13v2 | Informar o valor da Base de Cálculo do FCP |  |
| 245.35x | N23b | pFCPST | Percentual do FCP retido por Substituição Tributária | E | N23.1 | N | 1-1 | 3v2-4 | Percentual relativo ao Fundo de Combate à Pobreza (FCP) retido por substituição tributária |  |
| 245.35y | N23d | vFCPST | Valor do FCP retido por Substituição Tributária | E | N23.1 | N | 1-1 | 13v2 | Valor do ICMS relativo ao Fundo de Combate à Pobreza (FCP) retido por substituição tributária |  |
| 245.36 | N29 | pCredSN | Alíquota aplicável de cálculo do crédito (SIMPLES NACIONAL) | E | N10e | N | 1-1 | 3v2-4 | (v2.0) (Atualizado NT2016.002) |  |
| 245.37 | N30 | vCredICMSSN | Valor crédito do ICMS que pode ser aproveitado nos termos do art. 23 da LC 123 (SIMPLES NACIONAL) | E | N10e | N | 1-1 | 13v2 | (v2.0) (Atualizado NT2016.002) |  |

## Páginas relacionadas

* [VEN-140NEITE01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_140neite01.htm)
