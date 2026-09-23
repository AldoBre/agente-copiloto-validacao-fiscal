# Variáveis Disponibilizadas:

> **Fonte:** Identificador de Regra — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/com_000alstr01.htm  
> **Trilha:**   
> **Telas citadas:** —  
> **Identificadores de regras:** —

---
| Nome | Tipo | Observações | Retorna Valor |
| VSORIGEM | ALFA | Origem da chamada da Regra ("CTR" - Contrato,"NFS" - Nota Fiscal Saída,"NFE" - Nota Fiscal Entrada, "PRE" - Pré-Fatura, "PED" - Pedido, “COT” - Cotação) | N |
| VSCODEMP | NÚMERO | Código da Empresa | N |
| VSCODFIL | NÚMERO | Código da Filial | N |
| VSCODFOR | NÚMERO | Código do Fornecedor, só existe se VSOrigem = "NFE" | N |
| VSCODCLI | NÚMERO | Código do Cliente, só existe se VSOrigem = "NFS" | N |
| VSCODSNF | ALFA | Código da Série, só existe se VSOrigem = "NFS" ou "NFE". | N |
| VSNUMERO | NÚMERO | Número da Nota Fiscal só existe se VSOrigem = "NFS" ou "NFE" | N |
| VSCODTNS | ALFA | Código da Transação do Produto | N |
| VSSEQITE | NÚMERO | Sequência do Item de Nota Fiscal só existe se VSOrigem = "NFS" ou "NFE" | N |
| VSCODPRO | ALFA | Código do Produto | N |
| VSCODDER | ALFA | Código da Derivação | N |
| VSCODSER | ALFA | Código do Serviço | N |
| VSCODTST | ALFA | Código de ICMS Substituído | N |
| VSCODTRD | ALFA | Código de Redução de ICMS | N |
| VSPERIPI | NÚMERO | Percentual de IPI do item | N |
| VSPERICM | NÚMERO | Percentual do ICM do item | N |
| VSVENTCF | ALFA | Aplicação da natureza de operação - só existe se VSOrigem = "NFS" | N |
| VSSIGUFS | ALFA | Sigla do estado referente ao endereço. (Fornecedor ou Cliente, depende do VSOrigem) | N |
| VSCODCLF | ALFA | Código interno da classificação fiscal | N |
| VSCPRTCF | ALFA | Aplicação da natureza de operação. Só existe para "CTR" - Contrato e "NFE" - Nota Fiscal Entrada. | N |
| VSNUMANE | NÚMERO | Número da carga/análise | N |
| VSNUMPFA | ALFA | Número da Pré-Fatura | N |
| COMNFILPED | NÚMERO | Filial do pedido | N |
| COMNNUMPED | NÚMERO | Número do pedido | N |
| COMNSEQITEPED | NÚMERO | Sequência do item de pedido | N |
| COMACODDEP | ALFA | Código do depósito | N |
| VSCODLOT | ALFA | Código do lote do item de produto da nota fiscal de venda. | N |
| VSCODAGC | ALFA | Código de agrupamento comercial(compras ou vendas) dos produtos da família | N |
| VSCODAGE | ALFA | Código de agrupamento para estoques dos produtos da família | N |
| VSCODAGF | ALFA | Código de agrupamento para Impostos dos produtos da família | N |
| VSCODAGP | ALFA | Código de agrupamento para produção dos produtos da família | N |
| VSCODAGU | ALFA | Código de agrupamento para custos dos produtos da família | N |
| VSTRIPIS | ALFA | Indicativo se o produto tem tributação de PIS ou não | N |
| VSTRICOF | ALFA | Indicativo se o produto tem tributação de COFINS ou não | N |
| VSTIPNOT | NÚMERO | Tipo da nota fiscal | N |
| VSCODSTR | ALFA | Código da Situação Tributária do Item | S |
| VENAWEBSER | ALFA | Origem da chamada da regra. Preenchido quando executado o web service:   * com.senior.g5.co.mcm.ven.pedidos, sendo a partir da porta SimularPedidos ou GravarPedidos\_13; * com.senior.g5.co.mcm.ven.notafiscal, sendo a partir da porta GravarNotasFiscaisSaida\_13. |  |
| VENACODSTRSEQITE | ALFA | Código da situação tributária de ICMS.   * Caso a regra seja chamada pelo web service com.senior.g5.co.mcm.ven.pedidos, porta SimularPedidos ou porta GravarPedidos\_13. Ou ainda, pelo web service com.senior.g5.co.mcm.ven.notafiscal, porta GravarNotasFiscaisSaida\_13, conterá o valor informado no item da requisição; * Caso contrário, conterá o valor cadastrado no produto/serviço. |  |
| ComNNfc\_FilNfc | NÚMERO | Código da filial da nota fiscal de entrada. |  |
| ComNNfc\_CodFor | NÚMERO | Fornecedor da nota fiscal de entrada |  |
| ComNNfc\_NumNfc | NÚMERO | Número da nota fiscal de entrada. |  |
| ComANfc\_SnfNfc | ALFA | Código da série da nota fiscal de entrada. |  |
| ComNNfc\_SeqIpc | NÚMERO | Sequência do item da nota fiscal de entrada. |  |

## Páginas relacionadas

* [SimularPedidos](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/webservices/com_senior_g5_co_mcm_ven_pedidos.htm#SimularPedidos)
* [GravarPedidos_13](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/webservices/com_senior_g5_co_mcm_ven_pedidos.htm#GravarPedidos13)
* [GravarNotasFiscaisSaida_13](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/webservices/com_senior_g5_co_mcm_ven_notafiscal.htm#GravarNotasFiscaisSaida_12)
* [GravarNotasFiscaisSaida_13](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/webservices/com_senior_g5_co_mcm_ven_notafiscal.htm#GravarNotasFiscaisSaida_13)
