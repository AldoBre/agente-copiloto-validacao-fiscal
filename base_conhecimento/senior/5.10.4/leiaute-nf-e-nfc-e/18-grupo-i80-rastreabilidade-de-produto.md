# Grupo I80 - Rastreabilidade de produto

> **Fonte:** Leiautes NF-e e NFC-e — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/leiaute-nf-e-nfc-e.htm  
> **Trilha:** Segmentos > Compliance > Documentos Eletrônicos > NF-e | NFC-e (Nota Fiscal Eletrônica) > Nota Fiscal Eletrônica 4.0  
> **Telas citadas:** E140DLS, E210DLS  
> **Identificadores de regras:** VEN-140LTRAS01, VEN-140NERAS01

---
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação | Origem |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 128.70 | I80 | rastro | Detalhamento de produto sujeito a rastreabilidade | G | I01 |  | 0-500 |  | Informar apenas quando se tratar de produto a ser rastreado posteriormente. (Grupo criado na NT/2016/002) | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 128.71 | I81 | nLote | Número do Lote do produto | E | I80 | C | 1-1 | 1 - 20 |  | Gera por padrão o valor do campo E140DLS.CodLot. Se necessária a alteração dessa informação, verificar a documentação do Identificador de Regras VEN-140LTRAS01. |
| 128.72 | I82 | qLote | Quantidade de produto no Lote | E | I80 | N | 1-1 | 8v3 |  | Gera por padrão o valor do campo E140DLS.QtdEst. Se necessária a alteração dessa informação, verificar a documentação do Identificador de Regras VEN-140LTRAS01. |
| 128.73 | I83 | dFab | Data de fabricação / Produção | E | I80 | D | 1-1 |  | Formato: "AAAA-MM-DD" | Gera por padrão o valor do campo E210DLS.DatFab. Se necessária a alteração dessa informação ,verificar a documentação do Identificador de Regras VEN-140LTRAS01. |
| 128.74 | I84 | dVal | Data de validade | E | I80 | D | 1-1 |  | Formato: "AAAA-MM-DD". Informar o último dia do mês caso a validade não especifique o dia. | Gera por padrão o valor do campo E210DLS.DatVlt. Se necessária a alteração dessa informação, verificar a documentação do Identificador de Regras VEN-140LTRAS01. |
| 128.75 | I85 | cAgreg | Código de Agregação | E | I80 | N | 0-1 | 1 - 20 |  | Tag gerada via identificador de regra VEN-140NERAS01 através da variável VenACodAgr. |

## Páginas relacionadas

* [VEN-140LTRAS01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_140ltras01.htm)
* [VEN-140NERAS01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_140neras01.htm)
