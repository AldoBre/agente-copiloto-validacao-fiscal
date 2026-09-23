# Grupo N08a - Grupo Tributação do ICMS= 61

> **Fonte:** Leiautes NF-e e NFC-e — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/leiaute-nf-e-nfc-e.htm  
> **Trilha:** Segmentos > Compliance > Documentos Eletrônicos > NF-e | NFC-e (Nota Fiscal Eletrônica) > Nota Fiscal Eletrônica 4.0  
> **Telas citadas:** —  
> **Identificadores de regras:** —

---
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação | Origem |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 171.04 | N08a | ICMS61 | Grupo Tributação do ICMS Monofásico | CG | N01 |  | 1-1 |  | Tributação monofásica sobre combustíveis cobrada anteriormente | Gerado conforme o padrão do leiaute da SEFAZ |
| 171.05 | N11 | orig | Origem da mercadoria | E | N08a | N | 1-1 | 1 | Lista * 0 - Nacional, exceto as indicadas nos códigos 3, 4, 5 e 8 * 1 - Estrangeira - Importação direta, exceto a indicada no código 6 * 2 - Estrangeira - Adquirida no mercado interno, exceto a indicada no código 7 * 3 - Nacional, mercadoria ou bem com Conteúdo de Importação superior a 40% e inferior ou igual a 70% * 4 - Nacional, cuja produção tenha sido feita em conformidade com os processos produtivos básicos de que tratam as legislações citadas nos Ajustes * 5 - Nacional, mercadoria ou bem com Conteúdo de Importação inferior ou igual a 40% * 6 - Estrangeira - Importação direta, sem similar nacional, constante em lista da CAMEX e gás natural * 7 - Estrangeira - Adquirida no mercado interno, sem similar nacional, constante lista CAMEX e gás natural * 8 - Nacional, mercadoria ou bem   com Conteúdo de Importação superior a 70% |  |
| 171.06 | N12 | CST | Tributação do ICMS | E | N08a | N | 1-1 | 2 | 61= Tributação monofásica sobre combustíveis cobrada anteriormente |  |
| 171.07 | N43a | qBCMonoRet | Quantidade tributada retida anteriormente | E | N08a | N | 0-1 | 11v0-4 | Informe a BC do ICMS em quantidade conforme a unidade de medida estabelecida na legislação |  |
| 171.08 | N44 | adRemICMSRet | Alíquota *ad rem* do imposto retido anteriormente | E | N08a | N | 1-1 | 3v2-4 | Alíquota *ad rem* do ICMS estabelecida em legislação para o produto |  |
| 171.09 | N45 | vICMSMonoRet | Valor do ICMS retido anteriormente | E | N08a | N | 1-1 | 13v2 | O valor do ICMS é obtido pela multiplicação da alíquota *ad rem* pela quantidade do produto, conforme a unidade de medida estabelecida em legislação |  |
