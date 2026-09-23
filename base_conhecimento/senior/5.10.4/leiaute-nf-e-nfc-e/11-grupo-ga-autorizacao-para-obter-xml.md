# Grupo GA - Autorização para obter XML

> **Fonte:** Leiautes NF-e e NFC-e — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/leiaute-nf-e-nfc-e.htm  
> **Trilha:** Segmentos > Compliance > Documentos Eletrônicos > NF-e | NFC-e (Nota Fiscal Eletrônica) > Nota Fiscal Eletrônica 4.0  
> **Telas citadas:** —  
> **Identificadores de regras:** VEN-140NEAUT01

---
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação | Origem |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 97a.1 | GA01 | autXML | Pessoas autorizadas a acessar o XML da NF-e | G | A01 |  | 0-10 |  |  | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 97a.2 | GA02 | CNPJ | CNPJ Autorizado | CE | GA01 | N | 1-1 | 14 | Informar CNPJ ou CPF. Preencher os zeros não significativos. | Gera a tag via identificador de regras VEN-140NEAUT01. |
| 97a.3 | GA03 | CPF | CPF Autorizado | CE | GA01 | N | 1-1 | 11 |  | Gera a tag via identificador VEN-140NEAUT01. |

## Páginas relacionadas

* [VEN-140NEAUT01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_140neaut01.htm)
