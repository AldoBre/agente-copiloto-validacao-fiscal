# Identificador de Regra

> **Fonte:** Identificador de Regra — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/com_000alsub02.htm  
> **Trilha:**   
> **Telas citadas:** F120GPC, F120GPD  
> **Identificadores de regras:** COM-000ALSUB02

---
## COM-000ALSUB02

**Módulo:** COM - Comercial.

**Finalidade:** Alterar o código de substituição dos impostos PIS, COFINS e ICMS.

**Características:** Durante o cálculo de um item, este identificador poderá ser acionado três vezes, sendo uma para cada substituição (PIS, COFINS, ICMS), mesmo que o item não possua um código de substituição do referido imposto. Nesse caso, a regra deverá considerar obrigatoriamente a variável "ComATipSub", para tratar exatamente o tipo de substituição desejado (PIS, COFINS ou ICMS). Isso possibilita que não seja fixado um código de substituição e apenas via regra seja atribuído um código específico para efetivar o cálculo apenas naquela determinada operação de venda.  

**Transação:** Não se aplica.

**Importante**

A execução deste identificador de regras na tela F120GPD só acontece na saída da linha do item de produto, quando já existe quantidade e preço. Na tela F120GPC e no web service com.senior.g5.co.mcm.ven.pedidos, a execução deste identificador ocorre ao atribuir a quantidade ao item de pedido.

**Variáveis Disponibilizadas:**

| Nome | Tipo | Observações | Retorna Valor |
| --- | --- | --- | --- |
| ComNNumOct | NÚMERO | Número do orçamento | N |
| ComNVerOct | NÚMERO | Versão do orçamento | N |
| ComAOrigem | ALFA | Origem da chamada da Regra ("PED" - Pedido,"OCP" - Ordem de Compra,"NFS" - Nota Fiscal Saída,"NFE" - Nota Fiscal Entrada, "OCT" - Orçamento). | N |
| ComATipSub | ALFA | Indica o tipo da substiuição ("ICMS","PIS" ou "COFINS"). | N |
| ComNCodEmp | NÚMERO | Código da empresa. | N |
| ComNCodFil | NÚMERO | Código da filial. | N |
| ComACodSnf | ALFA | Vazio quando a origem for pedido ou ordem de compra, e com valor quando a origem for nota fiscal de saída ou entrada. | N |
| ComNNumero | NÚMERO | Número do pedido, ordem de compra, nota fiscal de saída ou entrada de acordo com a origem da chamada. | N |
| ComNSeqIte | NÚMERO | Sequência do item que estiver sendo calculado. | N |
| ComNIcmNor | NÚMERO | Valor de ICMS normal. | N |
| ComNVlrIpi | NÚMERO | Valor de IPI. | N |
| ComNBasIni | NÚMERO | Valor base inicial. | N |
| ComNQtde | NÚMERO | Quantidade. | N |
| ComNPreUni | NÚMERO | Preço unitário. | N |
| ComASigUfs | ALFA | Estado. | N |
| ComACodPro | ALFA | Código do produto. | N |
| ComACodDer | ALFA | Código da derivação. | N |
| ComNCliFor | NÚMERO | Código do cliente ou código do fornecedor dependendo da origem. | N |
| ComACliCon | ALFA | Indicativo se o cliente é contribuinte ou não. Terá valor somente quando a nota fiscal de entrada for do tipo 2, 3, 4 ou 5. | N |
| ComACodTns | ALFA | Transação do item. | N |
| ComNVlrFre | NÚMERO | Valor de frete do item. | N |
| ComNVlrSeg | NÚMERO | Valor de seguros do item. | N |
| ComNVlrEmb | NÚMERO | Valor de embalagens do item. | N |
| ComNVlrEnc | NÚMERO | Valor de encargos do item. | N |
| ComNVlrOut | NÚMERO | Valor de outras despesas do item. | N |
| ComNVlrFrd | NÚMERO | Valor de frete destacado do item. | N |
| ComNVlrOud | NÚMERO | Valor de outras despesas destacado do item. | N |
| ComNVlrDar | NÚMERO | Valor de arredondamento do item. | N |
| ComNVlrDzf | NÚMERO | Valor de desconto na zona franca. | N |
| ComNVlrRis | NÚMERO | Valor de retenção de ICMS substituto. | N |
| ComNBsiAtu | NÚMERO | Base de cálculo gerada pela margem. | N |
| ComNVlrIcs | NÚMERO | Valor de substituíção. | N |
| ComNPerIcs | NÚMERO | Percentual de substituíção. | N |
| ComNPerIcm | NÚMERO | Percentual de normal. | N |
| ComNFilPed | NÚMERO | Filial do pedido vinculado ao item da nota. | N |
| ComNNumPed | NÚMERO | Número do pedido vinculado ao item da nota. | N |
| ComNSeqIpd | NÚMERO | Sequência do item de produto vinculado ao item da nota. | N |
| ComNSeqIsp | NÚMERO | Sequência do item de serviço vinculado ao item da nota. | N |
| ComNVlrBru | NÚMERO | Valor bruto do item da nota fiscal. | N |
| ComNVlrDsc | NÚMERO | Valor de desconto do item da nota fiscal. | N |
| ComNVlrDs1 | NÚMERO | Valor do desconto 1. | N |
| ComNVlrDs2 | NÚMERO | Valor do desconto 2. | N |
| ComNVlrDs3 | NÚMERO | Valor do desconto 3. | N |
| ComNVlrDs4 | NÚMERO | Valor do desconto 4. | N |
| ComNVlrDs5 | NÚMERO | Valor do desconto 5. | N |
| ComNFilNfc | NÚMERO | Código da filial da nota fiscal de entrada. | N |
| ComNForNfc | NÚMERO | Código do fornecedor da nota fiscal de entrada. | N |
| ComNNumNfc | NÚMERO | Número da nota fiscal de entrada. | N |
| ComASnfNfc | ALFA | Série da nota fiscal de entrada. | N |
| ComNSeqItc | NÚMERO | Sequencia do item da nota fiscal de entrada (serviço ou produto). | N |
| ComAUfsFil | ALFA | Sigla do estado da filial. | N |
| ComACodFam | ALFA | Código da família do produto. | N |
| ComACodClf | ALFA | Código da classificação fiscal. | N |
| ComACodAge | ALFA | Código de agrupamento para estoques. | N |
| ComACodTstTns | ALFA | Código da situação tributária da transação. | N |
| ComACodTstPro | ALFA | Código da situação tributária do produto. | N |
| ComACodSub | ALFA | Código da substituição. | S |
| ComACodSer | ALFA | Código do serviço | N |

Atenção

Caso o parâmetro global LisVarReg esteja habilitado, a variável ListaVariaveis estará disponível em todos os identificadores de regras do sistema. O conteúdo desta variável lista os campos disponibilizados no identificador de regras em questão.

Não é aconselhada a ativação desse parâmetro global para o uso cotidiano. Esse recurso de listagem dos campos de identificadores auxilia a construção de regras e o Suporte para, por exemplo, depuração ou quando não houver acesso à documentação dos identificadores de regras.

## Páginas relacionadas

* [F120GPD](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f120gpd.htm)
* [F120GPC](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f120gpc.htm)
* [com.senior.g5.co.mcm.ven.pedidos](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/webservices/com_senior_g5_co_mcm_ven_pedidos.htm)
* [LisVarReg](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#LisVarReg)
