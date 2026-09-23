# Identificador de Regra

> **Fonte:** Identificador de Regra — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/cpr_000ecipi01.htm  
> **Trilha:**   
> **Telas citadas:** —  
> **Identificadores de regras:** CPR-000ECIPI01

---
## CPR-000ECIPI01

**Módulo:** CPR - Compras.

**Finalidade:** alterar o percentual, o valor e a base de IPI creditado efetivamente ao calculá-lo.

**Características:** na ordem de compra não há o Efetivamente Creditado, então não justifica a execução nesse caso.

**Tela:** NFE.

**Transação:** não se aplica.

**Variáveis disponibilizadas:**

| Nome | Tipo | Observações | Retorna Valor |
| --- | --- | --- | --- |
| CPRNQECIPI | NÚMERO | Quantidade da Base de IPI Creditado Efetivamente | S |
| CPRNAECIPI | NÚMERO | Alíquota por Valor de IPI Creditado Efetivamente | S |
| CPRAORIGEM | ALFA | Origem da chamada da Regra (OC - Ordem de Compra, NFE - Nota Fiscal Entrada) | N |
| CPRNCODEMP | NÚMERO | Código da Empresa | N |
| CPRNCODFIL | NÚMERO | Código da Filial | N |
| CPRNCODFOR | NÚMERO | Código do Fornecedor, só existe se CprAOrigem = NFE | N |
| CPRACODSNF | ALFA | Código da Série, só existe se CprAOrigem = NFE | N |
| CPRNNUMERO | NÚMERO | Número da Nota Fiscal de Entrada ou Ordem de Compra | N |
| CPRNSEQITE | NÚMERO | Sequência do Item de Nota Fiscal de Entrada ou Ordem de Compra | N |
| CPRACODPRO | ALFA | Código do Produto | N |
| CPRACODDER | ALFA | Código da Derivação | N |
| CPRACODFAM | ALFA | Código da Família | N |
| CPRACHVNEL | ALFA | Chave Nota Fiscal Eletrônica | N |
| CPRNQTDITE | NÚMERO | Quantidade do Item (Qtdade.Aberta quando CprAOrigem = OC, Qtdade.Recebida quando CprAOrigem = NFE) | N |
| CPRNPERIPI | NÚMERO | Percentual IPI | N |
| CPRNVLRIPI | NÚMERO | Valor de IPI | N |
| CPRNVLRBIP | NÚMERO | Valor Base de IPI | N |
| CPRNPERDSC | NÚMERO | Percentual de Desconto | N |
| CPRNPERDS1 | NÚMERO | Percentual de Desconto 1 | N |
| CPRNPERDS2 | NÚMERO | Percentual de Desconto 2 | N |
| CPRNVLRDSC | NÚMERO | Valor de Desconto | N |
| CPRNVLRDS1 | NÚMERO | Valor de Desconto 1 | N |
| CPRNVLRDS2 | NÚMERO | Valor de Desconto 2 | N |
| CPRNVLRBRU | NÚMERO | Valor Bruto | N |
| CPRNQTDEST | NÚMERO | Qtde. entrada conforme U.M. de estoque (somente para CprAOrigem = NFE) | N |
| CPRACODTNS | ALFA | Código da transação | N |
| CPRNCODCLI | NÚMERO | Código do Cliente | N |
| CPRNVLRFRE | NÚMERO | Valor do frete do item de produto | N |
| CPRACODDEP | ALFA | Código do depósito | N |
| CPRNNUMPED | NÚMERO | Número do pedido | N |
| CPRNFILPED | NÚMERO | Filial do Pedido | N |
| CPRNSEQIPD | NÚMERO | Sequência do item de produto do pedido | N |
| CPRNSEQISP | NÚMERO | Sequência do item de serviço do pedido | N |
| CPRNALIIPI | NÚMERO | Alíquota de IPI por valor | N |
| CPRACODCLF | ALFA | Código interno da classificação fiscal | S |
| CPRNQTDBIP | NÚMERO | Base de cálculo de IPI por quantidade | S |
| CPRNPECIPI | NÚMERO | Percentual IPI creditado efetivamente | S |
| CPRNVECIPI | NÚMERO | Valor de IPI creditado efetivamente | S |
| CPRNBECIPI | NÚMERO | Valor Base de IPI creditado efetivamente | S |

Atenção

Caso o parâmetro global LisVarReg esteja habilitado, a variável ListaVariaveis estará disponível em todos os identificadores de regras do sistema. O conteúdo desta variável lista os campos disponibilizados no identificador de regras em questão.

Não é aconselhada a ativação desse parâmetro global para o uso cotidiano. Esse recurso de listagem dos campos de identificadores auxilia a construção de regras e o Suporte para, por exemplo, depuração ou quando não houver acesso à documentação dos identificadores de regras.

## Páginas relacionadas

* [LisVarReg](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#LisVarReg)
