# Grupo ZF - Informações de Produtos da Agricultura, Pecuária e Produção Florestal

> **Fonte:** Leiautes NF-e e NFC-e — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/leiaute-nf-e-nfc-e.htm  
> **Trilha:** Segmentos > Compliance > Documentos Eletrônicos > NF-e | NFC-e (Nota Fiscal Eletrônica) > Nota Fiscal Eletrônica 4.0  
> **Telas citadas:** E140DEF, E140TNF  
> **Identificadores de regras:** —

---
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação | Origem |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 423k | ZF01 | agropecuario | Informações de produtos da agricultura, pecuária e produção Florestal | G | A01 |  | 0-1 |  |  | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 423k.1 | ZF02 | defensivo | Defensivos Agrícolas | CG | ZF01 |  | 1-20 |  |  | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 423k.2 | ZF03 | nReceituario | Número da receita ou receituário do agrotóxico / defensivo agrícola. | E | ZF02 | C | 1-1 | 1-30 | Informar o número da receita ou receituário de aplicação do defensivo | Gera a informação que consta no campo E140DEF.NumRec. |
| 423k.2a | ZF03a | CPFRespTec | CPF do Responsável Técnico pela emissão do receituário. | E | ZF02 | N | 1-1 | 11 | Informar o CPF do Responsável Técnico legalmente habilitado para emissão do receituário agrícola, conforme exigências federais e estaduais, como engenheiro agrônomo, engenheiro florestal ou técnico agrícola. | Gera a informação que consta no campo E140DEF.CpfTec. |
| 423k.3 | ZF04 | guiaTransito | Guia de Trânsito | CG | ZF01 |  | 1-1 |  |  | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 423k.4 | ZF05 | tpGuia | Tipo da Guia | E | ZF04 | N | 1-1 | 1 | 1 - GTA - Guia de Trânsito Animal; 2 - TTA - Termo de Trânsito Animal; 3 - DTA - Documento de Transferência Animal; 4 - ATV - Autorização de Trânsito Vegetal; 5 - PTV - Permissão de Trânsito Vegetal; 6 - GTV - Guia de Trânsito Vegetal; 7 - Guia Florestal (DOF; Sisflora - PA e MT ou SIAM - MG). | Gera a informação que consta no campo E140TNF.TipGua. |
| 423k.5 | ZF06 | UFGuia | UF de emissão | E | ZF04 | C | 0-1 | 2 | UF de emissão da guia | Gera a informação que consta no campo E140TNF.UfGuia. |
| 423k.6 | ZF07 | serieGuia | Série da Guia | E | ZF04 | C | 0-1 | 1-9 | Informar sempre que houver a série da guia | Gera a informação que consta no campo E140TNF.SerGui. |
| 423k.7 | ZF08 | nGuia | Número da Guia | E | ZF04 | N | 1-1 | 1-9 | Número da Guia | Gera a informação que consta no campo E140TNF.NumGui. |
