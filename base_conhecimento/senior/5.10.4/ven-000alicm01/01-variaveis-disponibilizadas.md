# Variáveis disponibilizadas:

> **Fonte:** Identificador de Regra — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_000alicm01.htm  
> **Trilha:**   
> **Telas citadas:** F070FVE, F140PRE  
> **Identificadores de regras:** —

---
| Nome | Tipo | Observações | Retorna Valor |
| COMNICMAOR | NÚMERO | (DIFAL) Percentual de ICMS partilha do estado de origem | S |
| COMNICMVOR | NÚMERO | (DIFAL) Valor de ICMS partilha do estado de origem | S |
| COMNICMADE | NÚMERO | (DIFAL) Percentual de ICMS partilha do estado de destino | S |
| COMNICMVDE | NÚMERO | (DIFAL) Valor de ICMS partilha do estado de destino | S |
| COMNICMBDE | NÚMERO | (DIFAL) Base de ICMS partilha do estado de destino | S |
| COMNICMAFC | NÚMERO | (DIFAL) Alíquota de fundo de combate à pobreza | S |
| COMNICMVFC | NÚMERO | (DIFAL) Valor do fundo de combate à pobreza | S |
| COMNBASFCP | NÚMERO | Valor base do FCP | S |
| COMNALIFCP | NÚMERO | Alíquota do FCP | S |
| COMNVLRFCP | NÚMERO | Valor do FCP | S |
| COMNICMBFC | NÚMERO | Base de cálculo do FCP na UF de destino (DIFAL) | S |
| VENAORIMER | ALFA | Código de origem fiscal (do produto ou serviço), conforme item do pedido ou da nota fiscal de saída que estiver sendo processada | N |
| VENNPERDIF | NÚMERO | Percentual do diferimento de ICMS | S |
| VENNBASIDF | NÚMERO | Base do ICMS Diferido | S |
| VENNPERIDF | NÚMERO | Alíquota do ICMS Diferido | S |
| VENNVLRIDF | NÚMERO | Valor do ICMS Diferido | S |
| VENARECIDF | ALFA | Define se vai calcular o ICMS Diferido novamente, considerando somente os percentuais de ICMS, ICMS Diferido e Diferimento de ICMS retornados via regra. O valor esperado é igual a "S"; qualquer valor diferente será considerado como "N" | S |
| Para **não recalcular** os valores do ICMS Diferido ao fechar uma nota fiscal, configure o Tipo Cálculo Diferimento como **1 - Diferimento de ICMS por valor** na tela Parâmetros da Filial para Vendas (F070FVE). | | | |
| VENNFILPED | NÚMERO | Filial do Pedido | N |
| VENNNUMPED | NÚMERO | Número do Pedido | N |
| VENNSEQIPD | NÚMERO | Sequência do item de pedido de produtos | N |
| VENNSEQISP | NÚMERO | Sequência do item de pedido de serviços | N |
| VENDDATEMI | DATA | Data de emissão da nota fiscal de saída | N |
| VENNSEQENT | NÚMERO | Sequência do endereço de entrega do cliente | N |
| VENNPERICF | NÚMERO | Percentual de ICMS sobre o frete da nota fiscal de saída | N |
| VENNFILNFC | NÚMERO | Código da filial da nota fiscal de entrada | N |
| VENNFORNFC | NÚMERO | Fornecedor da nota fiscal de entrada | N |
| VENNNUMNFC | NÚMERO | Número da nota fiscal de entrada | N |
| VENASNFNFC | ALFA | Código da série da nota fiscal de entrada | N |
| VENNSEQITC | NÚMERO | Sequência do item de produto na nota fiscal de saída | N |
| VSCODSNF | NÚMERO | Código da Série, só existe se VSOrigem = "NFS" | N |
| VSNUMERO | NÚMERO | Número da Nota Fiscal de Saída ou pedido | N |
| VSSEQITE | NÚMERO | Sequência do Item de Nota Fiscal de Saída ou Pedido | N |
| VSTNSPRO | ALFA | Transação do item | N |
| VSCODCLI | NÚMERO | Código do Cliente | N |
| VSCODPRO | ALFA | Código do Produto | N |
| VSCODDER | ALFA | Código da Derivação | N |
| VSCODFAM | ALFA | Código da Família | N |
| VSCODTRD | ALFA | Código de Redução de ICMS | N |
| VSCODTIC | ALFA | Código de ICMS Especial | N |
| VSVLRIPI | NÚMERO | Valor de IPI | N |
| VSVLRBRU | NÚMERO | Valor Bruto | N |
| VSVLRDSC | NÚMERO | Valor Desconto | N |
| VSVLRDS1 | NÚMERO | Valor Desconto 1 | N |
| VSVLRDS2 | NÚMERO | Valor Desconto 2 | N |
| VSVLRFRE | NÚMERO | Valor do Frete | N |
| VSVLRSEG | NÚMERO | Valor do Seguro | N |
| VSVLREMB | NÚMERO | Valor das Embalagens | N |
| VSVLRENC | NÚMERO | Valor dos Encargos | N |
| VSVLROUT | NÚMERO | Valor Outros | N |
| VSVLRDAR | NÚMERO | Valor de Arredondamento | N |
| VSVLRFRD | NÚMERO | Valor Frete Destacado | N |
| VSVLROUD | NÚMERO | Valor Outras Despesas Destacado | N |
| VSPERICM | NÚMERO | Percentual de ICMS | S |
| VSVLRICM | NÚMERO | Valor de ICMS | S |
| VSVLRBIC | NÚMERO | Valor Base de ICMS | S |
| VSORIGEM | ALFA | Qual a origem da chamada do identificador. Pode ser: PED - Pedido, NFS - Nota fiscal de saída, NFE - Nota fiscal de Entrada, OCP - Ordem de compra ou OCT - Orçamento | N |
| VSQTDITE | NÚMERO | Quantidade do produto/serviço | N |
| VSCODSTR | ALFA | Consulta da situação tributária do ICMS do item da nota fiscal | N |
| VSCODLOT | ALFA | Código do lote do item de produto na nota fiscal de saída. Será preenchida somente quando o item de produto possuir um único lote distribuído | N |
| VSUFSCLI | ALFA | Sigla do estado do cliente | N |
| VSCODDEP | ALFA | Código do depósito | N |
| VSRECDIF | ALFA | Indica se o DIFAL deve ser recalculado no momento do recálculo de valores da Nota Fiscal  **Observação:** deve-se retornar S para que o DIFAL seja recalculado, desde que não tenha sido feita uma alteração manual do DIFAL via regra | N |
| ComNPdiFcp | NÚMERO | Percentual do diferimento de ICMS relativo ao FCP | S |
| ComNVdiFcp | NÚMERO | Valor diferido do ICMS relativo ao FCP | S |
| ComNCodFin | NÚMERO | Código da finalidade de venda | N |

**Observação**

* As variáveis **VSNumero** e **VSSeqIte** sempre serão preenchidas com os campos chave da rotina que chamou o identificador. A origem da execução pode ser *NF Saída*, Pedido, *Orçamento*, *NF Entrada* ou *Ordem*, pois a origem de execução é dada pela variável **VSOrigem**
* Já as variáveis **VenNFilPed**, **VenNNumPed** e **VenNSeqIpd** são preenchidas com as informações do pedido apenas quando a origem de execução do identificador for *NF Saída*
* Com base no exposto, percebe-se que ao gerar um pedido pode-se utilizar as variáveis **VSCodEmp**, **VSCodFil**, **VSNumero** e **VSSeqIte** para ter acesso as chaves do item do pedido
* A variável VSCODSTR apresenta um comportamento específico quando o identificador de regras está ativo na tela Nota Fiscal Saída (F140PRE). Para mais informações, verifique o comportamento da variável VSCODSTR na tela Preparação da Nota Fiscal Saída (F140PRE)

## Páginas relacionadas

* [ICMS Diferido](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/impostos-icms.htm)
* [Parâmetros da Filial para Vendas (F070FVE)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070fve.htm)
* [comportamento da variável VSCODSTR na tela Preparação da Nota Fiscal Saída (F140PRE)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f140pre.htm#Comportamento_da_vari%C3%A1vel_VSCODSTR)
