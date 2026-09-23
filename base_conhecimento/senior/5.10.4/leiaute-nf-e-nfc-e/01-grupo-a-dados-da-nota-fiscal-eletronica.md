# Grupo A - Dados da nota fiscal eletrônica

> **Fonte:** Leiautes NF-e e NFC-e — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/leiaute-nf-e-nfc-e.htm  
> **Trilha:** Segmentos > Compliance > Documentos Eletrônicos > NF-e | NFC-e (Nota Fiscal Eletrônica) > Nota Fiscal Eletrônica 4.0  
> **Telas citadas:** E140NFV, F070FVE  
> **Identificadores de regras:** VEN-140NEDGE01

---
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação | Origem |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | A01 | infNFe | Informações da NF-e | G | Raiz | - | 1-1 |  | Grupo que contém as informações da NF-e | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 2 | A02 | versao | Versão do leiaute | A | A01 | C | 1-1 | 1 - 4 | Versão do leiaute (4.00) | * Campo  Integração NF-e da tela F070FVE, guia Documentos Eletrônicos 3; * Pode ser manipulada essa tag através da variável VSIntTipImp do identificador VEN-140NEDGE01. |
| 3 | A03 | Id | Identificador da TAG a ser assinada | ID | A01 | C | 1-1 | 47 | Informar a Chave de Acesso precedida do literal ‘NFe’, | Campo Chave do documento eletrônico (ChvNel) da tabela Vendas - Notas Fiscais de Saída - Dados Gerais (E140NFV) acrescido da palavra "NFe".   A chave é composta por:  * cUF - Código da UF do emitente do Documento Fiscal; * AAMM - Ano e Mês de emissão da NF-e; * CNPJ - CNPJ do emitente; * mod - Modelo do Documento Fiscal; * serie - Série do Documento Fiscal; * nNF - Número do Documento Fiscal; * cNF - Código Numérico que compõe a Chave de Acesso; * cDV - Dígito Verificador da Chave de Acesso. |
| 4 | A04 | pk\_nItem | Regra para que a numeração do item de detalhe da NF-e seja única | RC | - | - | 1-1 |  | Regra de validação do item de detalhe da NF-e, campo de controle do Schema XML, o contribuinte não deve se preocupar com o preenchimento deste campo. |  |

## Páginas relacionadas

* [VEN-140NEDGE01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_140nedge01.htm)
