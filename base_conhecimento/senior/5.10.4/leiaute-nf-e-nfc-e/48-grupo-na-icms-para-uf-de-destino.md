# Grupo NA - ICMS para UF de destino

> **Fonte:** Leiautes NF-e e NFC-e — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/leiaute-nf-e-nfc-e.htm  
> **Trilha:** Segmentos > Compliance > Documentos Eletrônicos > NF-e | NFC-e (Nota Fiscal Eletrônica) > Nota Fiscal Eletrônica 4.0  
> **Telas citadas:** —  
> **Identificadores de regras:** —

---
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação | Origem |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 245a.01 | NA01 | ICMSUFDest | Informação do ICMS Interestadual | G | M01 |  | 0-1 |  | Grupo a ser informado nas vendas interestaduais para consumidor final, não contribuinte do ICMS. Observação: Este grupo não deve ser utilizado nas operações com veículos automotores novos efetuadas por meio de faturamento direto para o consumidor (Convênio ICMS 51/00), as quais possuem grupo de campos próprio (ICMSPart) (Grupo criado na NT 2015/003) | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 245a.03 | NA03 | vBCUFDest | Valor da BC do ICMS na UF de destino | E | NA01 | N | 1-1 | 13v2 | Valor da Base de Cálculo do ICMS na UF de destino | Gera por padrão o valor do campo E140Ipv.IcmBde. |
| 245a.04 | NA04 | vBCFCPUFDest | Valor da BC FCP na UF de destino | E | NA01 |  | 1-1 | 13v2 | Valor da Base de Cálculo do FCP na UF de destino. (Incluído na NT2016/002) | Gera por padrão o valor do campo E140Pvd.IcmBfc. |
| 245a.05 | NA05 | pFCPUFDest | Percentual do ICMS relativo ao Fundo de Combate à Pobreza (FCP) na UF de destino | E | NA01 | N | 0-1 | 3v2-4 | Percentual adicional inserido na alíquota interna da UF de destino, relativo ao Fundo de Combate à Pobreza (FCP) naquela UF. Nota: Percentual máximo de 2%, conforme a legislação. | Gera por padrão o valor do campo E140Ipv.IcmAfc. |
| 245a.07 | NA07 | pICMSUFDest | Alíquota interna da UF de destino | E | NA01 | N | 1-1 | 3v2-4 | Alíquota adotada nas operações internas na UF de destino para o produto/mercadoria. A alíquota do Fundo de Combate à Pobreza, se existente para o produto/mercadoria, deve ser informada no campo próprio (pFCPUFDest) não devendo ser somada à essa alíquota interna. | Gera por padrão o valor do campo E140Ipv.IcmAde. |
| 245a.09 | NA09 | pICMSInter | Alíquota interestadual das UF envolvidas | E | NA01 | N | 1-1 | 2v2 | Alíquota interestadual das UF envolvidas:  * 4% alíquota interestadual para produtos importados; * 7% para os Estados de origem do Sul e Sudeste (exceto ES), destinado para os Estados do Norte, Nordeste, Centro-Oeste e Espírito Santo; * 12% para os demais casos. | Gera o valor conforme o ICMS Interestadual definido pela SEFAZ. |
| 245a.11 | NA11 | pICMSInterPart | Percentual provisório de partilha do ICMS Interestadual | E | NA01 | N | 1-1 | 3v2-4 | Percentual de ICMS Interestadual para a UF de destino:  * 40% em 2016; * 60% em 2017; * 80% em 2018; * 100% a partir de 2019. | Gera por padrão o valor do campo E140Nfv.DatEmi. |
| 245a.13 | NA13 | vFCPUFDest | Valor do ICMS relativo ao Fundo de Combate à Pobreza (FCP) da UF de destino | E | NA01 | N | 0-1 | 13v2 | Valor do ICMS relativo ao Fundo de Combate à Pobreza (FCP) da UF de destino. (Atualizado na NT2016/002) | Gera por padrão o valor do campo E140Ipv.IcmVfc. |
| 245a.15 | NA15 | vICMSUFDest | Valor do ICMS Interestadual para a UF de destino | E | NA01 | N | 1-1 | 13v2 | Valor do ICMS Interestadual para a UF de destino, já considerando o valor do ICMS relativo ao Fundo de Combate à Pobreza naquela UF | Gera por padrão o valor do campo E140Ipv.IcmVde. |
| 245a.17 | NA17 | vICMSUFRemet | Valor do ICMS Interestadual para a UF do remetente | E | NA01 | N | 1-1 | 13v2 | Valor do ICMS Interestadual para a UF do remetente. Nota: A partir de 2019, este valor será zero | Gera por padrão o valor do campo E140Ipv.IcmVde. |
