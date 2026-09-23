# Grupo ZA - Informações do Comércio Exterior

> **Fonte:** Leiautes NF-e e NFC-e — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/leiaute-nf-e-nfc-e.htm  
> **Trilha:** Segmentos > Compliance > Documentos Eletrônicos > NF-e | NFC-e (Nota Fiscal Eletrônica) > Nota Fiscal Eletrônica 4.0  
> **Telas citadas:** —  
> **Identificadores de regras:** —

---
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação | Origem |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 402 | ZA01 | exporta | Grupo Exportação | G | A01 |  | 0-1 |  | Informar apenas na exportação | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 403 | ZA02 | UFSaidaPais | Sigla da UF de Embarque ou de transposição de fronteira | E | ZA01 | C | 1-1 | 2 | Não aceita o valor "EX" | Gera por padrão o valor do campo E140Nfv.UfsEbq. |
| 404 | ZA03 | xLocExporta | Descrição do Local de Embarque ou de transposição de fronteira | E | ZA01 | C | 1-1 | 1 - 60 |  | Gera por padrão o valor do campo E140Nfv.LocEmb. |
| 404a | ZA04 | xLocDespacho | Descrição do local de despacho | E | ZA01 | C | 0-1 | 1 - 60 | Informação do Recinto Alfandegado | Gera por padrão o valor do campo E140Tnf.LocDsp. |
