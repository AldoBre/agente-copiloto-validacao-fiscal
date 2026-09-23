# Grupo VC - Referenciamento de item de outro Documento Fiscal Eletrônico - DF-e - Novo grupo para atender a Reforma Tributária!

> **Fonte:** Leiautes NF-e e NFC-e — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/leiaute-nf-e-nfc-e.htm  
> **Trilha:** Segmentos > Compliance > Documentos Eletrônicos > NF-e | NFC-e (Nota Fiscal Eletrônica) > Nota Fiscal Eletrônica 4.0  
> **Telas citadas:** E140IDE, E140ISV, E140PVD, F140NCI  
> **Identificadores de regras:** —

---
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação | Origem |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 325i | VC01 | DFeReferenciado | Documento Fiscal Eletrônico Referenciado | G | H01 |  | 0-1 |  | Grupo para referenciamento de itens de outro DF-e. | Gera notas vinculadas ao produto utilizando os campos E140PVD.CODEMP, E140PVD.CODFIL, E140PVD.SNFNFR, E140PVD.NUMNFR e para serviços utilizando o campo E140ISV.CODEMP, E140ISV.CODFIL, E140ISV.SNFNFR, E140ISV.NUMNFR  Estes campos são informados no sistema pela tela F140NCI. |
| 325j | VC02 | chaveAcesso | Chave de acesso do DF-e referenciado | E | VC01 | N | 1-1 | 44 | Chave de acesso do DF-e referenciado. | Gera por padrão o valor do campo E140IDE.CHVNEL vinculado aos campos E140PVD.CODEMP, E140PVD.CODFIL, E140PVD.SNFNFR, E140PVD.NUMNFR para produtos e E140ISV.CODEMP, E140ISV.CODFIL, E140ISV.SNFNFR, E140ISV.NUMNFR para serviços  Estes campos são informados no sistema pela tela F140NCI. |
| 325k | VC03 | nItem | Número do item do documento referenciado. | E | VC01 | N | 0-1 | 3 | Corresponde ao atributo “nItem” do elemento “det” do documento original. | Gera por padrão o valor do campo E140PVD.SEQIPR para produtos e E140ISV.SEQISR para serviços  Estes campos são informados no sistema pela tela F140NCI. |
