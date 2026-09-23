# Identificador de Regra

> **Fonte:** Identificador de Regra — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/com_000alstr02.htm  
> **Trilha:**   
> **Telas citadas:** —  
> **Identificadores de regras:** COM-000ALSTR02

---
## COM-000ALSTR02

**Módulo:** COM - Comercial.

**Finalidade:** Alterar a sugestão do código da situação tributária de IPI do item.

**Características:** Executado na sugestão do código da situação tributária, em notas fiscais de compra e venda, para produtos e serviços.  
---  
5.8.1.13  
- Adicionado as váriaveis de agrupamento "VSCodAgc", "VSCodAge", "VSCodAgf", "VSCodAgp" e "VSCodAgu".  
- Adicionada as váriaveis "VSTriPis" e "VSTriCof" para indicar se tributa PIS e COFINS.  
- Adicionada a váriavel "VSTipNot" que corresponde ao tipo da nota.

**Tela:** Geral

**Transação:** Pode estar ligado a uma transação.

**Variáveis Disponibilizadas:**

| Nome | Tipo | Observações | Retorna Valor |
| --- | --- | --- | --- |
| VSORIGEM | ALFA | Origem da chamada da Regra ("CTR" - Contrato,"NFS" - Nota Fiscal Saída,"NFE" - Nota Fiscal Entrada) | N |
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
| ComNFilPed | NÚMERO | Filial do pedido | N |
| ComNNumPed | NÚMERO | Número do pedido | N |
| ComNSeqItePed | NÚMERO | Sequência do item de pedido | N |
| ComACodDep | ALFA | Código do depósito | N |
| VSCODAGC | ALFA | Código de agrupamento comercial(compras ou vendas) dos produtos da família | N |
| VSCODAGE | ALFA | Código de agrupamento para produção dos produtos da família | N |
| VSCODAGF | ALFA | Código de agrupamento para Impostos dos produtos da família | N |
| VSCODAGP | ALFA | Código de agrupamento para produção dos produtos da família | N |
| VSCODAGU | ALFA | Código de agrupamento para custos dos produtos da família | N |
| VSTRIPIS | ALFA | Indicativo se o produto tem tributação de PIS ou não | N |
| VSTRICOF | ALFA | Indicativo se o produto tem tributação de COFINS ou não | N |
| VSTIPNOT | NÚMERO | Tipo da nota fiscal | N |
| VSCODSTR | ALFA | Código da Situação Tributária do Item | S |

Atenção

Caso o parâmetro global LisVarReg esteja habilitado, a variável ListaVariaveis estará disponível em todos os identificadores de regras do sistema. O conteúdo desta variável lista os campos disponibilizados no identificador de regras em questão.

Não é aconselhada a ativação desse parâmetro global para o uso cotidiano. Esse recurso de listagem dos campos de identificadores auxilia a construção de regras e o Suporte para, por exemplo, depuração ou quando não houver acesso à documentação dos identificadores de regras.

## Páginas relacionadas

* [LisVarReg](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#LisVarReg)
