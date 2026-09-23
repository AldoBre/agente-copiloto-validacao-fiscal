# Grupo BB -  Grupo de Compras Governamentais

> **Fonte:** Leiautes NF-e e NFC-e — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/leiaute-nf-e-nfc-e.htm  
> **Trilha:** Segmentos > Compliance > Documentos Eletrônicos > NF-e | NFC-e (Nota Fiscal Eletrônica) > Nota Fiscal Eletrônica 4.0  
> **Telas citadas:** E085CLI, E140IPR, E140ISR, E140NFR, E140TNF  
> **Identificadores de regras:** —

---
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação | Origem |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 29f | B31 | gCompraGov | Grupo de Compra Governamental | G | B01 | - | 0-1 | - | Grupo compras governamentais | Dados das tabelas E140IPR para produtos e E140ISR para serviços |
| 29f.1 | B32 | tpEnteGov | Tipo de ente governamental | E | B31 | - | 1-1 | 1 | Cadastro do cliente | E085CLI.TipEnt |
| 29f.2 | B33 | pRedutor | Percentual de redução de alíquota em compra governamental | E | B31 | N | 1-1 | 3v2-4 | Conforme o art. 472/370 da LC 214/2025. | E140IPR.PerRgc ou E140ISR.PerRgc |
| 29f.3 | B34 | tpOperGov | Tipo de operação com o ente governamental | E | B31 | N | 1-1 | 1 | E140TNF.TpoGov | 1= Quando a nota fiscal não possuir documento referenciado emitido para um ente governamental. 2= Quando a nota fiscal possuir documento fiscal referenciado emitido para um ente governamental, identificado por E085CLI.TipEnt com valor 1, 2, 3 ou 4. |
| 29.z5 | BB05 | refDFeAnt | Chave de acesso do documento fiscal anterior | E | BB01 | C | 0-99 | 44 | - | E140NFR.CHVDOE |
