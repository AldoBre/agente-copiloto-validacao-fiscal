# Grupo ZX - Informações Suplementares da Nota Fiscal

> **Fonte:** Leiautes NF-e e NFC-e — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/leiaute-nf-e-nfc-e.htm  
> **Trilha:** Segmentos > Compliance > Documentos Eletrônicos > NF-e | NFC-e (Nota Fiscal Eletrônica) > Nota Fiscal Eletrônica 4.0  
> **Telas citadas:** —  
> **Identificadores de regras:** —

---
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação | Origem |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 424 | ZX01 | infNFeSupl | Informações suplementares da Nota Fiscal | G | Raiz | - | 0-1 |  | Informações suplementares da Nota Fiscal, não afetando a assinatura digital. (NT 2015.002) | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 425 | ZX02 | qrCode | Texto com o QR-Code impresso no DANFE NFC-e.  Obs.: URLs, por UF, utilizadas para consulta QR Code acesse: http://nfce.encat.org/desenvolvedor/qrcode/ | E | ZX01 | C | 1-1 | 100-600 | Ver orientações de preenchimento na seção 3.3 do Manual de Orientação do Contribuinte 7.0 | Tag não é gerada pelo ERP, pois trata-se de tag específica para NFC-e que não é emitida pelo sistema. |
| 426 | ZX03 | urlChave | Texto com a URL de consulta por chave de acesso a ser impressa no DANFE NFC-e. Obs.: URLs, por UF, utilizadas para consulta por chave de acesso, acesse: http://nfce.encat.org/consumidor-nfce/consulte-nota-nfce/ | E | ZX01 | C | 1-1 | 21-85 | Informar a URL da "Consulta por chave de acesso da NFC-e". A mesma URL que deve estar informada no DANFE NFC-e para consulta por chave de acesso | Tag não é gerada pelo ERP, pois trata-se de tag específica para NFC-e que não é emitida pelo sistema. |
