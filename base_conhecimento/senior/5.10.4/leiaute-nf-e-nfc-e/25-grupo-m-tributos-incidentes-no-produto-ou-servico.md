# Grupo M - Tributos incidentes no Produto ou Serviço

> **Fonte:** Leiautes NF-e e NFC-e — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/leiaute-nf-e-nfc-e.htm  
> **Trilha:** Segmentos > Compliance > Documentos Eletrônicos > NF-e | NFC-e (Nota Fiscal Eletrônica) > Nota Fiscal Eletrônica 4.0  
> **Telas citadas:** —  
> **Identificadores de regras:** —

---
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação | Origem |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 163 | M01 | imposto | Tributos incidentes no Produto ou Serviço | G | H01 |  | 1-1 |  | Grupo ISSQN mutuamente exclusivo com os grupos ICMS e II, isto é, se o grupo ISSQN for informado os grupos ICMS e II não serão informados e vice-versa. | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 163a | M02 | vTotTrib | Valor aproximado total de tributos federais, estaduais e municipais | E | M01 | N | 0-1 | 13v2 | (NT 2013/003) | Verifica se o "OriPdf" (Origem detalhamento da carga tributária nos documentos fiscais) é igual a "2".   * Caso seja, é enviado os valores das tabelas E140Dts.IbpFeb, E140Dts.IbpEst, E140Dts.IbpMun * Caso não seja, envia o Valor total dos tributos pela tabela E140Dts.VlrIns, E140Dts.VlrIim, E140VlrCid denominado de VlrTot |
