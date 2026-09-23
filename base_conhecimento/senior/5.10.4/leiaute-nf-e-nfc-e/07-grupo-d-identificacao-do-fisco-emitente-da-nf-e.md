# Grupo D - Identificação do Fisco Emitente da NF-e

> **Fonte:** Leiautes NF-e e NFC-e — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/leiaute-nf-e-nfc-e.htm  
> **Trilha:** Segmentos > Compliance > Documentos Eletrônicos > NF-e | NFC-e (Nota Fiscal Eletrônica) > Nota Fiscal Eletrônica 4.0  
> **Telas citadas:** —  
> **Identificadores de regras:** —

---
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação | Origem |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 50 | D01 | avulsa |  | G | A01 |  | 0-1 |  | Informações do fisco emitente (uso exclusivo do fisco) | Esse grupo não é gerado pelo ERP. Trata-se de um grupo de informações geradas e de uso exclusivo do fisco. |
| 51 | D02 | CNPJ | CNPJ do órgão emitente | E | D01 | C | 1-1 | 14 | Informar os zeros não significativos. |  |
| 52 | D03 | xOrgao | Órgão emitente | E | D01 | C | 1-1 | 1-60 |  |  |
| 53 | D04 | matr | Matrícula do agente do Fisco | E | D01 | C | 1-1 | 1-60 |  |  |
| 54 | D05 | xAgente | Nome do agente do Fisco | E | D01 | C | 1-1 | 1-60 |  |  |
| 55 | D06 | fone | Telefone | E | D01 | N | 0 -1 | 6-14 | Preencher com Código DDD + número do telefone (v2.0) (NT 2011/004) |  |
| 56 | D07 | UF | Sigla da UF | E | D01 | C | 1-1 | 2 |  |  |
| 57 | D08 | nDAR | Número do Documento de Arrecadação da Receita | E | D01 | C | 0-1 | 1 - 60 | (NT 2011/004) |  |
| 58 | D09 | dEmi | Data de emissão do Documento de Arrecadação | E | D01 | D | 0-1 |  |  |  |
| 59 | D10 | vDAR | Valor Total constante no Documento de arrecadação de Receita | E | D01 | N | 0-1 | 1-13v2 | (NT 2011/004) |  |
| 60 | D11 | repEmi | Repartição Fiscal emitente | E | D01 | C | 1-1 | 1-60 |  |  |
| 61 | D12 | dPag | Data de Pagamento do Documento de Arrecadação | E | D01 | D | 0-1 |  |  |  |
