# Grupo N02a - Grupo Tributação do ICMS= 02

> **Fonte:** Leiautes NF-e e NFC-e — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/leiaute-nf-e-nfc-e.htm  
> **Trilha:** Segmentos > Compliance > Documentos Eletrônicos > NF-e | NFC-e (Nota Fiscal Eletrônica) > Nota Fiscal Eletrônica 4.0  
> **Telas citadas:** —  
> **Identificadores de regras:** —

---
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação | Origem |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 171.04 | N02a | ICMS02 | Grupo Tributação do ICMS Monofásico | CG | N01 |  | 1-1 |  | Tributação monofásica própria sobre combustíveis | Gerado conforme o padrão do leiaute da SEFAZ |
| 171.05 | N11 | orig | Origem da mercadoria | E | N02a | N | 1-1 | 1 | * 0 - Nacional, exceto as indicadas nos códigos 3, 4, 5 e 8 * 1 - Estrangeira - Importação direta, exceto a indicada no código 6 * 2 - Estrangeira - Adquirida no mercado interno, exceto a indicada no código 7 * 3 - Nacional, mercadoria ou bem com Conteúdo de Importação superior a 40% e inferior ou igual a 70% * 4 - Nacional, cuja produção tenha sido feita em conformidade com os processos produtivos básicos de que tratam as legislações citadas nos Ajustes * 5 - Nacional, mercadoria ou bem com Conteúdo de Importação inferior ou igual a 40% * 6 - Estrangeira - Importação direta, sem similar nacional, constante em lista da CAMEX e gás natural * 7 - Estrangeira - Adquirida no mercado interno, sem similar nacional, constante lista CAMEX e gás natural * 8 - Nacional, mercadoria ou bem   com Conteúdo de Importação superior a 70% |  |
| 171.06 | N12 | CST | Tributação do ICMS | E | N02a | N | 1-1 | 2 | 02= Tributação monofásica própria sobre combustíveis |  |
| 171.07 | N37a | qBCMono | Quantidade tributada | E | N02a | N | 0-1 | 11v0-4 | Informar a BC do ICMS próprio em quantidade conforme a unidade de medida estabelecida na legislação para o produto |  |
| 171.08 | N38 | adRemICMS | Alíquota *ad rem* do imposto | E | N02a | N | 1-1 | 3v2-4 | Alíquota *ad rem* do ICMS estabelecida na legislação para o produto |  |
| 171.09 | N39 | vlICMSMono | Valor do ICMS próprio | E | N02a | N | 1-1 | 13v2 | O valor do ICMS é obtido pela multiplicação da alíquota *ad rem* pela quantidade do produto, conforme a unidade de medida estabelecida na legislação |  |
