# Grupo Y - Dados da Cobrança

> **Fonte:** Leiautes NF-e e NFC-e — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/leiaute-nf-e-nfc-e.htm  
> **Trilha:** Segmentos > Compliance > Documentos Eletrônicos > NF-e | NFC-e (Nota Fiscal Eletrônica) > Nota Fiscal Eletrônica 4.0  
> **Telas citadas:** —  
> **Identificadores de regras:** —

---
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação | Origem |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 389 | Y01 | cobr | Grupo Cobrança | G | A01 |  | 0-1 |  |  | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 390 | Y02 | fat | Grupo Fatura | G | Y01 |  | 0-1 |  |  | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 391 | Y03 | nFat | Número da Fatura | E | Y02 | C | 0-1 | 1 - 60 |  | Gera o valor, conforme consta no campo E140Rci.NumNfv. |
| 392 | Y04 | vOrig | Valor Original da Fatura | E | Y02 | N | 0-1 | 13v2 |  | Gera o valor, conforme consta no campo E440Par.VctPar. |
| 393 | Y05 | vDesc | Valor do desconto | E | Y02 | N | 0-1 | 13v2 |  | Tag gerada caso o parâmetro global **UtiNot160** esteja igual a como "S" e é inserido o valor "0.00" como padrão. |
| 394 | Y06 | vLiq | Valor Líquido da Fatura | E | Y02 | N | 0-1 | 13v2 |  | Gera o valor, conforme consta no campo E440Par.VlrTro. |
| 395 | Y07 | dup | Grupo Parcelas | G | Y01 |  | 0-120 |  | (NT 2011/004) (Grupo atualizado na NT2016.002)  A tag não será gerada para pagamentos à vista para NF-e, fazendo o controle pelo vencimento e pelo número de parcelas da NF-e se possuir mais de uma parcela, ou, quando houver uma única parcela com data de vencimento maior que a emissão da nota. | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 396 | Y08 | nDup | Número da Parcela | E | Y07 | C | 0 - 1 | 1 - 60 | Obrigatória informação do número de parcelas com 3 algarismos, sequenciais e consecutivos. Ex.: "001", "002", "003" [...].  Observação: este padrão de preenchimento será obrigatório somente a partir de 03/09/2018 | Gera o valor, conforme consta no campo E440Nfr.CodPar. |
| 397 | Y09 | dVenc | Data de vencimento | E | Y07 | D | 0-1 |  | Formato: "AAA-MM-DD". Obrigatória a informação da data de vencimento na ordem crescente das datas. Ex.: "2018-06-01", "2018-07-01", "2018-08-01", etc. | Gera o valor, conforme consta no campo E140Par.VctPar. |
| 398 | Y10 | vDup | Valor da Parcela | E | Y07 | N | 1-1 | 13v2 | (NT 2012/003) | Gera o valor, conforme consta no campo E140Par.VlrPar. |
