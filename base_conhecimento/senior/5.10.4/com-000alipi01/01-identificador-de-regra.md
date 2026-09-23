# Identificador de Regra

> **Fonte:** Identificador de Regra — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/com_000alipi01.htm  
> **Trilha:**   
> **Telas citadas:** E075PPC, E075PRO, E440IPC, F075PPC, F075PRO  
> **Identificadores de regras:** COM-000ALIPI01

---
## COM-000ALIPI01

**Módulo:** COM - Comercial.

**Finalidade:** alterar o percentual, o valor e a base de IPI ao calculá-lo.

**Características:** é chamado sempre que um item de produto executar o cálculo do valor de IPI. Se o item não calcular o valor de IPI ou caso exista algum parâmetro que faça com que o sistema realize o cálculo, a regra não será chamada.

**Importante**

Para que o sistema execute a regra sem que haja uma alíquota de IPI sugerida previamente, é preciso que no cadastro do Produto (F075PRO) e/ou ligação Cliente X Produto (F075PPC) esteja informada uma tabela de tributação para cálculo do IPI por quantidade/unidade de medida (E075PRO.TPRIPI e/ou E075PPC.TPRIPI).

**Transação:** não se aplica.

**Variáveis Disponibilizadas:**

| Nome | Tipo | Observações | Retorna Valor |
| --- | --- | --- | --- |
| CPRAFREIIM | ALFA | Transação considera o frete na base do II | N |
| CPRASEGIIM | ALFA | Transação considera o seguro na base do II | N |
| CPRAEMBIIM | ALFA | Transação considera a embalagem na base do II | N |
| CPRAENCIIM | ALFA | Transação considera os encargos na base do II | N |
| CPRAOUTIIM | ALFA | Transação considera outras despesas na base do II | N |
| CPRADARIIM | ALFA | Transação considera valor arredondamento na base do II | N |
| CPRAFRDIIM | ALFA | Transação considera o frete destacado na base do II | N |
| CPRAOUDIIM | ALFA | Transação considera outras despesas destacadas na base do II | N |
| CPRAIIMIPI | ALFA | Transação considera valor do II na base do IPI | N |
| CPRAIIMICM | ALFA | Transação considera valor do II na base do ICMS | N |
| CPRACPRFIM | ALFA | Soma valor de frete de importação na base do ICMS | N |
| CPRACPRSIM | ALFA | Soma valor de seguro de importação na base do ICMS | N |
| CPRACPROIM | ALFA | Soma valor de outras despesas de importação na base do ICMS | N |
| CPRACPRAIM | ALFA | Soma valor adicional ao frete para renovação da marinha mercante na base do ICMS | N |
| CPRACPRFII | ALFA | Soma valor do frete de importação na base do IPI | N |
| CPRACPRSII | ALFA | Soma valor de seguro de importação na base do IPI | N |
| CPRACPROII | ALFA | Soma valor de outras despesas de importação na base do IPI | N |
| CPRAFRIIIM | ALFA | Soma valor de frete de importação na base do II | N |
| CPRASGIIIM | ALFA | Soma valor de seguro de importação na base do II | N |
| CPRAOTIIIM | ALFA | Soma valor de outras despesas de importação na base do II | N |
| CPRACPRFIP | ALFA | Soma valor de frete de importação na base do PIS | N |
| CPRACPRSIP | ALFA | Soma valor de seguro de importação na base do PIS | N |
| CPRACPROIP | ALFA | Soma valor de outras despesas de importação na base do PIS | N |
| CPRACPRFIC | ALFA | Soma valor de frete de importação na base do cofins | N |
| CPRACPRSIC | ALFA | Soma valor de seguro de importação na base do cofins | N |
| CPRACPROIC | ALFA | Soma valor de outras despesas de importação na base do cofins | N |
| VSORIGEM | ALFA | Origem da chamada da Regra ("PED" - Pedido,"OCP" - Ordem de Compra,"NFS" - Nota Fiscal Saída,"NFE" - Nota Fiscal Entrada) | N |
| VSCODEMP | NÚMERO | Código da Empresa | N |
| VSCODFIL | NÚMERO | Código da Filial | N |
| VSCODFOR | NÚMERO | Código do Fornecedor, só existe se VSOrigem = "NFE" | N |
| VSCODSNF | ALFA | Código da Série, só existe se VSOrigem = "NFS" ou NFE. | N |
| VSNUMERO | NÚMERO | Número da Nota Fiscal de Entrada, Saída, pedido ou Ordem de Compra | N |
| VSSEQITE | NÚMERO | Sequência do Item de Nota Fiscal de Entrada, Saída, Pedido ou Ordem de Compra | N |
| VSCODPRO | ALFA | Código do Produto | N |
| VSCODDER | ALFA | Código da Derivação | N |
| VSCODFAM | ALFA | Código da Família | N |
| VSQTDITE | NÚMERO | Quantidade do Item (Qtdade.Aberta quando VSOrigem = "PED" ou "OCP", Qtdade.Recebida quando VSOrigem = "NFE" e Qtdade.Faturada quando VSOrigem = "NFS") | N |
| VSPERDS1 | NÚMERO | Percentual de Desconto 1 | N |
| VSPERDS2 | NÚMERO | Percentual de Desconto 2 | N |
| VSPERDSC | NÚMERO | Percentual de Desconto | N |
| VSVLRDS1 | NÚMERO | Valor de Desconto 1 | N |
| VSVLRDS2 | NÚMERO | Valor de Desconto 2 | N |
| VSVLRDSC | NÚMERO | Valor de Desconto | N |
| VSVLRBRU | NÚMERO | Valor Bruto | N |
| VSQTDEST | NÚMERO | Qtde. entrada conforme U.M. de estoque (somente para VSOrigem = "NFE"). Seu valor representa o campo E440IPC.QTDEST. | N |
| VSCODTNS | ALFA | Código da transação | N |
| VSCODCLI | NÚMERO | Código do cliente | N |
| VSVLRFRE | NÚMERO | Valor do frete do item de produto | N |
| VSCODTPR | ALFA | Código da tabela de preço do vendas | N |
| VSCODDEP | ALFA | Código do depósito | N |
| VSNUMPED | NÚMERO | Número do pedido | N |
| VSFILPED | NÚMERO | Filial do pedido | N |
| VSSEQIPD | NÚMERO | Sequência do item de produto do pedido | N |
| VSSEQISP | NÚMERO | Sequência do item de serviço do pedido | N |
| VENNFILNFC | NÚMERO | Código da filial da nota fiscal de entrada | N |
| VENNFORNFC | NÚMERO | Fornecedor da nota fiscal de entrada | N |
| VENNNUMNFC | NÚMERO | Número da nota fiscal de entrada | N |
| VENASNFNFC | ALFA | Código da série da nota fiscal de entrada | N |
| VENNSEQITC | NÚMERO | Sequência do item de produto na nota fiscal de saída | N |
| VSPERIPI | NÚMERO | Percentual de IPI | S |
| VSVLRIPI | NÚMERO | Valor de IPI | S |
| VSVLRBIP | NÚMERO | Valor Base de IPI | S |
| VSCODCLF | ALFA | Código interno da classificação fiscal | S |
| VSALIIPI | NÚMERO | Alíquota de IPI por valor | S |
| VSQTDBIP | NÚMERO | Base de cálculo de IPI por quantidade | S |
| VSVlrOud | NÚMERO | Valor de outras despesas destacado | S |
| VSVlrOut | NÚMERO | Valor do campo "Outros" (VlrOut) do item do documento fiscal. Permite definir via regra o valor a ser lançado no campo "Outros" da nota fiscal de saída e do pedido. | S |

Atenção

Caso o parâmetro global LisVarReg esteja habilitado, a variável ListaVariaveis estará disponível em todos os identificadores de regras do sistema. O conteúdo desta variável lista os campos disponibilizados no identificador de regras em questão.

Não é aconselhada a ativação desse parâmetro global para o uso cotidiano. Esse recurso de listagem dos campos de identificadores auxilia a construção de regras e o Suporte para, por exemplo, depuração ou quando não houver acesso à documentação dos identificadores de regras.

## Páginas relacionadas

* [F075PRO](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075pro.htm)
* [F075PPC](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075ppc.htm)
* [LisVarReg](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#LisVarReg)
