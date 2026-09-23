# Grupo H - Detalhamento de Produtos e Serviços da NF-e

> **Fonte:** Leiautes NF-e e NFC-e — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/leiaute-nf-e-nfc-e.htm  
> **Trilha:** Segmentos > Compliance > Documentos Eletrônicos > NF-e | NFC-e (Nota Fiscal Eletrônica) > Nota Fiscal Eletrônica 4.0  
> **Telas citadas:** —  
> **Identificadores de regras:** —

---
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação | Origem |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 98 | H01 | det | Detalhamento de Produtos e Serviços | G | A01 |  | 1-990 |  | Múltiplas ocorrências (máximo = 990) | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 99 | H02 | nItem | Número do item | A | H01 | N | 1-1 | 1-3 | Número do item (1-990) | Gera por padrão o item gravado na E140Ipv.SeqIpv. |
