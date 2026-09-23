# Grupo BC - Grupo de notas de antecipação de pagamento

> **Fonte:** Leiautes NF-e e NFC-e — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/leiaute-nf-e-nfc-e.htm  
> **Trilha:** Segmentos > Compliance > Documentos Eletrônicos > NF-e | NFC-e (Nota Fiscal Eletrônica) > Nota Fiscal Eletrônica 4.0  
> **Telas citadas:** E140NFR  
> **Identificadores de regras:** —

---
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação | Origem |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 29.y1 | BB01 | gPagAntecipado | Grupo de notas de antecipação de pagamento | G | B01 |  | 0-1 |  | Informado para abater as parcelas de antecipação de pagamento, conforme Art. 10. § 4º |  |
| 29.y2 | BB02 | refNFe | Chave de acesso da NF-e de antecipação de pagamento | E | BB01 | C | 1-99 | 44 | Referência uma NF-e (modelo 55) emitida anteriormente, referente a pagamento antecipado | E140NFR.CHVDOE |
