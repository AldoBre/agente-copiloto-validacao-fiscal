# Grupo N03a - Grupo Tributação do ICMS= 15

> **Fonte:** Leiautes NF-e e NFC-e — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/leiaute-nf-e-nfc-e.htm  
> **Trilha:** Segmentos > Compliance > Documentos Eletrônicos > NF-e | NFC-e (Nota Fiscal Eletrônica) > Nota Fiscal Eletrônica 4.0  
> **Telas citadas:** —  
> **Identificadores de regras:** —

---
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação | Origem |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 184.13 | N03a | ICMS15 | Grupo Tributação do ICMS monofásico | CG | N01 |  | 1-1 |  | Tributação monofásica própria e com responsabilidade pela retenção sobre combustíveis | Gerado conforme o padrão do leiaute da SEFAZ |
| 184.14 | N11 | orig | Origem da mercadoria | E | N03a | N | 1-1 | 1 | * 0 - Nacional, exceto as indicadas nos códigos 3, 4, 5 e 8 * 1 - Estrangeira - Importação direta, exceto a indicada no código 6 * 2 - Estrangeira - Adquirida no mercado interno, exceto a indicada no código 7 * 3 - Nacional, mercadoria ou bem com Conteúdo de Importação superior a 40% e inferior ou igual a 70% * 4 - Nacional, cuja produção tenha sido feita em conformidade com os processos produtivos básicos de que tratam as legislações citadas nos Ajustes * 5 - Nacional, mercadoria ou bem com Conteúdo de Importação inferior ou igual a 40% * 6 - Estrangeira - Importação direta, sem similar nacional, constante em lista da CAMEX e gás natural * 7 - Estrangeira - Adquirida no mercado interno, sem similar nacional, constante lista CAMEX e gás natural * 8 - Nacional, mercadoria ou bem   com Conteúdo de Importação superior a 70% |  |
| 184.15 | N12 | CST | Tributação do ICMS | E | N03a | N | 1-1 | 2 | 15= Tributação monofásica própria e com responsabilidade pela retenção sobre combustíveis |  |
| 184.16 | N37a | qBCMono | Quantidade tributada | E | N03a | N | 0-1 | 11v0-4 | Informar a BC do ICMS próprio em quantidade conforme a unidade de medida estabelecida na legislação para o produto |  |
| 184.17 | N38 | adRemICMS | Alíquota *ad rem* do imposto | E | N03a | N | 1-1 | 3v2-4 | Alíquota *ad rem* do ICMS estabelecida na legislação para o produto |  |
| 184.18 | N39 | vICMSMono | Valor do ICMS próprio | E | N03a | N | 1-1 | 13v2 | O valor do ICMS é obtido pela multiplicação da alíquota *ad rem* pela quantidade do produto, conforme a unidade de medida estabelecida na legislação |  |
| 184.19 | N39a | qBCMonoRetem | Quantidade tributada sujeita a retenção | E | N03a | N | 0-1 | 11v0-4 | Informar a BC do ICMS sujeito a retenção em quantidade conforme a unidade de medida estabelecida na legislação para o produto |  |
| 184.20 | N40 | adRemICMSRetem | Alíquota *ad rem* do imposto com retenção | E | N03a | N | 1-1 | 3v2-4 | Alíquota *ad rem* do ICMS sobre o biocombustível a ser adicionado para a composição da mistura vendida a consumidor final estabelecida na legislação para o produto |  |
| 184.21 | N41 | vICMSMonoRetem | Valor do ICMS com retenção | E | N03a | N | 1-1 | 13v2 | O valor do ICMS é obtido pela multiplicação da alíquota *ad rem* pela quantidade do produto conforme a unidade de medida estabelecida em legislação |  |
| 184.22 | N46 | -x- | Sequência XML | G | N03a |  | 0-1 |  | Grupo opcional |  |
| 184.23 | N47 | pRedAdRem | Percentual de redução do valor da alíquota *ad rem* do ICMS | E | N46 | N | 1-1 | 3v2 | Informar o percentual de redução do valor da alíquota *ad rem* do ICMS |  |
| 184.24 | N48 | motRedAdRem | Motivo da redução do *ad rem* | E | N46 | N | 1-1 | 1 | O campo será preenchido quando o campo anterior estiver preenchido. Informe o motivo da redução: 1= Transporte coletivo de passageiros e 9=Outros |  |
