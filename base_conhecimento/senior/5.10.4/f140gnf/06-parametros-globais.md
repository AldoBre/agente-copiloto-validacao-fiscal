# Parâmetros globais

> **Fonte:** F140GNF - Notas Fiscais de Saída — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f140gnf.htm  
> **Trilha:** Ajuda por telas > Mercado > Gestão de Faturamento e Outras Saídas > Notas Fiscais de Saída  
> **Telas citadas:** E000GRI, F140GNF  
> **Identificadores de regras:** —

---
| Nome | Descrição |
| AjuCotTit | Ao gerar um título no fechamento de uma nota de saída na tela Notas Fiscais de Saída (F140GNF) com uma moeda diferente da moeda da empresa, o sistema pode gerar um valor de moeda arredondado que não bate com o valor original da nota.  Este parâmetro global ajusta a cotação na hora de gerar um título pelo faturamento, abrangendo até dez casas decimais no campo Cotação Moeda Emissão da tela |
| ArrDebCre | Indicativo se não deve corrigir perda de precisão decimal para o valor bruto em notas de Débito e Crédito. O valor pode ser igual a "Vazio" (sempre corrigir), "5 - Não corrigir Nota de Crédito" e/ou "6 - Não corrigir Nota de Débito". |
| AtuCodBnf | Parâmetro global criado para auxiliar na sugestão dos benefícios fiscais. |
| AtuUltNum | Indicativo se deve utilizar a nova forma de atualizar o último número da Série. |
| DesIcmBpc | Indica quais bases de PIS/COFINS receberão o desconto de ICMS |
| ExiMsgTns | Quando este parâmetro global estiver com o valor S-Sim, será indicado ao Gestão Empresarial | ERP para apresentar a mensagem de sugestão ao alterar uma transação do item. Quando o parâmetro estiver com o valor N-Não, o ERP não apresentará a mensagem referente à transação.  Quando o parâmetro estiver com o valor R-Regra, a rotina de sugestão de transação será chamada, porém a pergunta de sugestão não será exibida |
| GerPenGri | Indicativo se deve gerar a pendência na tabela Busca eDocs - Guia de Recolhimento de Impostos (E000GRI) na emissão da nota no modo síncrono |
| GerTagTra | Indicativo se deve gerar a tag <Transporta> quando a modalidade do frete for 3 ou 4. |
| LogNfsTit | Indica se deve gerar logs de títulos do contas a receber nas notas fiscais de saída |
| OriCstNfs | Indica se o sistema deve preencher a origem da mercadoria da nota fiscal de saída com o primeiro dígito da situação tributária de ICMS. Esse parâmetro deve ser usado em empresas do regime normal |
| SugCstTra | Indicativo se a Situação Tributária de ICMS deve ser sugerida ao gerar notas fiscais de entrada de transferência via nota fiscal de saída. |
| TemLimCad | Estipula o tempo que as informações do cadastro de clientes, fornecedores, impostos, classificação fiscal e substituições de ICMS por estados ficam na memória, dessa forma diminuindo as buscas no banco de dados. Por padrão, o tempo é 02:30, porém é possível configurá-lo conforme a necessidade da empresa |
| UtiBenIcm | Indicativo se o item de nota fiscal de saída pode utilizar mais de um benefício fiscal de ICMS (redução de ICMS e FCI) |
| UtiGnvUnn | Indica se deve usar a função **ObterProximoId** para gerar os nossos números dos títulos de contas a receber. |
| UsaEntOri | Indicativo se o sistema irá utilizar o endereço de entrega e origem da mercadoria nos documentos fiscais e obrigações acessórias.  Ao utilizá-lo, se o CEP informado nos dados gerais não existir e o **Tipo de Mercado** do cliente for **E - Externo (Exterior)**, as tags de endereço do destinatário (enderDest) serão preenchidas com os seguintes valores padrões: cMun = 9999999, xMun = EXTERIOR e UF = EX |

## Páginas relacionadas

* [AjuCotTit](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#AjuCotTit)
* [ArrDebCre](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#ArrDebCre)
* [AtuCodBnf](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#AtuCodBnf)
* [AtuUltNum](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#AtuUltNum)
* [DesIcmBpc](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#DesIcmBpc)
* [ExiMsgTns](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#ExiMsgTns)
* [GerPenGri](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#GerPenGri)
* [GerTagTra](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#GerTagTra)
* [LogNfsTit](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#LogNfsTit)
* [OriCstNfs](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#OriCstNfs)
* [SugCstTra](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#SugCstTra)
* [TemLimCad](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#TemLimCad)
* [UtiBenIcm](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#UtiBenIcm)
* [UtiGnvUnn](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#UtiGnvUnn)
* [UsaEntOri](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#UsaEntOri)
