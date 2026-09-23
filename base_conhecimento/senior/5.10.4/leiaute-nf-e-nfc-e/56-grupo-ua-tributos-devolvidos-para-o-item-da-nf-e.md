# Grupo UA - Tributos Devolvidos (para o item da NF-e)

> **Fonte:** Leiautes NF-e e NFC-e — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/leiaute-nf-e-nfc-e.htm  
> **Trilha:** Segmentos > Compliance > Documentos Eletrônicos > NF-e | NFC-e (Nota Fiscal Eletrônica) > Nota Fiscal Eletrônica 4.0  
> **Telas citadas:** —  
> **Identificadores de regras:** —

---
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação | Origem |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 324p | UA01 | impostoDevol | Informação do Imposto devolvido | G | H01 |  | 0-1 |  | Observação: o motivo da devolução deverá ser informado pela empresa no campo de Informações Adicionais do Produto (tag:infAdProd) | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 324q | UA02 | pDevol | Percentual da mercadoria devolvida | E | UA01 | N | 1-1 | 3v2 | Observação: o valor máximo deste percentual é 100%, no caso de devolução total da mercadoria | Gera o valor, conforme consta no campo E140Ipv.QtdFat. |
| 324r | UA03 | IPI | Informação do IPI devolvido | G | UA01 |  | 1-1 |  |  | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 324s | UA04 | vIPIDevol | Valor do IPI devolvido | E | UA03 | N | 1-1 | 13v2 |  | Gera o valor, conforme consta no campo E140Ipv.VlrIdv. |
