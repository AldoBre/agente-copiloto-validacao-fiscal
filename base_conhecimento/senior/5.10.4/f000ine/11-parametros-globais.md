# Parâmetros globais

> **Fonte:** F000INE - Via Recebimento de Documento Eletrônico — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f000ine.htm  
> **Trilha:** Ajuda por telas > Suprimentos > Gestão de Recebimento > Notas Fiscais de Entrada  
> **Telas citadas:** E070CPR, E440NFC, F000INE, F070FCP, F073TRA, F090REP  
> **Identificadores de regras:** CPR-000ALICM01, CPR-440BURAT01

---
| Nome | Descrição |
| AltFreCpr | Define se deve alterar o Tipo de Frete para X-Sem Frete quando o valor de frete for 0 (zero) |
| CalIcmDif | Indicativo se deve recalcular os valores do ICMS Diferido ao modificar os percentuais de ICMS ou ICMS Diferido via identificador CPR-000ALICM01. Este recálculo existe para manter os valores corretos. |
| CanCnhNfs | Indicativo se a chave de notas fiscais de serviço devem ser validadas quando o campo E070CPR.CONCHV estiver com valor "S". |
| CodEdcNfs | Código do Modelo/Espécie de Documento Fiscal para Recebimento Eletrônico de NFS-e |
| ConComDfs | Indicativo para controlar a compatibilidade dos DF-es com eDocs. |
| ConIcmCte | Indicativo se a rotina de Recebimento Eletrônico, ao processar um CTe ou CTe-OS, vai ignorar a consistência dos valores de ICMS recebidos X valores de ICMS calculados |
| ConVlrFin | Indica se a mensagem de consistência deve ser apresentada ao processar a tela F000INE quando os valores recebidos da importação do .XML forem diferentes dos valores calculados pelo sistema, ainda que o valor financeiro da nota seja igual |
| DefNumNfs | Indicativo se deve considerar apenas os 9 dígitos significativos do número da nota fiscal de serviço quando o XML possuir mais de 9 dígitos no recebimento eletrônico. |
| EqiVinOcp | Indicativo se deve ser apresentada a mensagem "Item da ordem de compra já foi vinculado à outro item da nota fiscal." durante o processamento dos itens de produto do recebimento eletrônico, quando a filial utiliza produtos equivalentes. |
| GerLogRec | Indicativo se deve gerar arquivo de log ao processar as inconsistências do recebimento eletrônico |
| GerMsgPed | Indica se o sistema deve ou não mostrar uma mensagem de geração de pedido no fechamento de uma nota fiscal de entrada na tela Via Recebimento de Documento Eletrônico |
| HabNotSai | Indicativo para habilitar o botão Nota Saída (1), para notas tipos 1 e 5 |
| HerObsPar | Indicativo se realiza a herança da observação das parcelas da ordem de compra para as parcelas das notas fiscais de entrada, tela agrupada |
| HerRatCve | Indicativo se durante a herança do rateio através do identificador de regra CPR-440BURAT01, o sistema busque apenas itens da nota de origem em que a transação esteja parametrizada para considerar para valorização de estoques. |
| LigNotOri | Indicativo se o sistema permite ligar notas fiscais de origem que contenham apenas itens de serviços em notas fiscais de entrada do tipo 8. |
| LotIneWms | Indicativo para que se faça sugestão do lote padrão da origem do produto ao processar uma nota fiscal quando processado na tela F000INE, sempre que o produto não possuir lote. |
| ObrTraIne | Indicativo se deve ser obrigatório cadastrar a transportadora informada no XML da nota fiscal durante o processamento do recebimento eletrônico. |
| OpcGerNfc | Indicativo da opção padrão para geração das parcelas das notas fiscais de entrada |
| RepForCli | Indicativo para chamar o Cadastro do Representante (F090REP) através de outras telas. O código do representante deve ser igual ao do fornecedor ou cliente quando a filial estiver configurada para ter códigos iguais para cliente e fornecedor. |
| SugCdPIne | Indicativo se o sistema deve sugerir a condição de pagamento na nota fiscal conforme está na ordem de compra. |
| SugTnsRec | Indicativo se deve sugerir as transações de produto e serviço no processamento da nota fiscal de entrada no recebimento eletrônico |
| TnsRegPar | Indica se o sistema deve regerar as parcelas após alteração das transações de produto ou serviço dos dados gerais da nota fiscal de entrada no recebimento eletrônico |
| TraCliFor | Indica se o sistema deverá atualizar as ligações transportadora/fornecedor e transportadora/cliente ao incluir ou alterar o registro da transportadora |
| TraForCli | Indicativo se chamar o cadastro da transportadora (F073TRA) através de outras telas, o código deve ser igual ao do fornecedor ou cliente quando a filial estiver configurada para ter códigos iguais para cliente e fornecedor. |
| UtiIcmXml | Indicativo se o sistema deve utilizar o valor, valor base e percentual do ICMS obtido do XML no cálculo da nota através desta tela. |
| ValNumDfs | Indicativo se deve validar número da nota do XML com o campo E440NFC.NumDfs. |
| ValPagRec | Indicativo se deve validar notas de Recebimento/Pagamento apenas pelo tipo de operação de compra da transação. |
| ValRecCcl | Indicativo para validação do campo CClass durante o recebimento eletrônico de documentos fiscais com dados de CBS/IBS no XML. |
| VlrMarDif | Define o arredondamento dos valores da Nota Fiscal, para considerar o valor informado no campo **Valor Máx. Arredondamento** da F070FCP como limite de diferença aceito entre o arquivo XML e a nota fiscal de entrada gerada, quando a opção Fechar nota após processar estiver desmarcado |

## Páginas relacionadas

* [AltFreCpr](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#AltFreCpr)
* [CalIcmDif](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#CalIcmDif)
* [CPR-000ALICM01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/cpr_000alicm01.htm)
* [CanCnhNfs](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#CanCnhNfs)
* [CodEdcNfs](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#CodEdcNfs)
* [ConComDfs](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#ConComDfs)
* [ConIcmCte](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#ConIcmCte)
* [ConVlrFin](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#ConVlrFin)
* [DefNumNfs](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#DefNumNfs)
* [EqiVinOcp](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#EqiVinOcp)
* [GerLogRec](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#GerLogRec)
* [GerMsgPed](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#GerMsgPed)
* [HabNotSai](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#HabNotSai)
* [HerObsPar](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#HerObsPar)
* [HerRatCve](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#HerRatCve)
* [LigNotOri](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#LotIneWms)
* [ObrTraIne](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#ObrTraIne)
* [OpcGerNfc](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#OpcGerNfc)
* [RepForCli](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#RepForCli)
* [F090REP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f090rep.htm)
* [SugCdPIne](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#SugCdPIne)
* [SugTnsRec](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#SugTnsRec)
* [TnsRegPar](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#TnsRegPar)
* [TraCliFor](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#TraCliFor)
* [TraForCli](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#TraForCli)
* [F073TRA](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f073tra.htm)
* [UtiIcmXml](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#UtiIcmXml)
* [ValNumDfs](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#ValNumDfs)
* [ValPagRec](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#ValPagRec)
* [ValRecCcl](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#ValRecCcl)
* [VlrMarDif](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#VlrMarDif)
