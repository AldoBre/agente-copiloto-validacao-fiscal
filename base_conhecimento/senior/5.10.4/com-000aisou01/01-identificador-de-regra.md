# Identificador de Regra

> **Fonte:** Identificador de Regra — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/com_000aisou01.htm  
> **Trilha:**   
> **Telas citadas:** —  
> **Identificadores de regras:** COM-000AISOU01

---
## COM-000AISOU01

**Módulo:** COM - Comercial.

**Finalidade:** Alterar os valores de Isentas e Outras de ICMS e IPI no cálculo dos itens das Notas Fiscais de Entrada e Saída.

**Características:** Na descrição das variáveis disponibilizadas existe uma informação entre parênteses, que tem o seguinte significado:

* (N.Fiscal de Entrada) - Variável terá valor quando se tratar de uma Entrada;
* (N.Fiscal de Saída) - Variável terá valor quando se tratar de uma Saída;
* (N.Fiscal de Entrada e Saída) - Variável terá valor tanto na Entrada como na Saída.

**Tela:** Notas Fiscais de Entrada e Saída.

**Transação:** Não se aplica.

**Variáveis Disponibilizadas:**

| Nome | Tipo | Observações | Retorna Valor |
| --- | --- | --- | --- |
| ComAOriMer | ALFA | Código de origem fiscal (do produto ou serviço), conforme item da nota fiscal (de entrada ou saída) que estiver sendo processada. | N |
| ComNAECIPI | NÚMERO | Alíquota por Valor de IPI Creditado Efetivamente |  |
| ComNBecIcm | NÚMERO | Base de ICMS efetivamente creditado | N |
| ComNBecIpi | NÚMERO | Base de IPI efetivamente creditado | N |
| ComNPecIcm | NÚMERO | Percentual de ICMS efetivamente creditado | N |
| ComNPecIpi | NÚMERO | Percentual de IPI efetivamente creditado | N |
| ComNQECIPI | NÚMERO | Quantidade da Base de IPI Creditado Efetivamente |  |
| ComNVecIcm | NÚMERO | Valor de ICMS efetivamente creditado | N |
| ComNVecIpi | NÚMERO | Valor de IPI efetivamente creditado | N |
| VSCliFor | NÚMERO | Código do Fornecedor (N.Fiscal Entrada) ou Cliente (N.Fiscal Saída) | N |
| VSCodEmp | NÚMERO | Código da Empresa (N.Fiscal de Entrada e Saída) | N |
| VSCodFil | NÚMERO | Código da Filial (N.Fiscal de Entrada e Saída) | N |
| VSCodPro | ALFA | Código do Produto (N.Fiscal de Entrada e Saída) | N |
| VSCodSer | ALFA | Código do Serviço (N.Fiscal de Entrada e Saída) | N |
| VSCodSnf | ALFA | Código de Série da Nota Fiscal (N.Fiscal de Entrada e Saída) | N |
| VSCodStr | ALFA | Código Interno da Situação Tributária (N.Fiscal de Entrada e Saída) | N |
| VSCodTrd | ALFA | Código do tipo de ICMS reduzido (N.Fiscal de Entrada) | N |
| VSCprEnt | ALFA | Forma de escrituração para não tributadas (N.Fiscal de Entrada) | N |
| VSCprIbi | ALFA | Transação considera o IPI na base de ICMS (N.Fiscal de Entrada) | N |
| VSCprRic | ALFA | Indicativo se a transação recupera o ICMS (N.Fiscal de Entrada) | N |
| VSCprRip | ALFA | Indicativo se a transação recupera o IPI (N.Fiscal de Entrada) | N |
| VSCprTcf | ALFA | Aplicação da natureza de operação (N.Fiscal de Entrada) | N |
| VSNopPro | ALFA | Natureza de Operação para Produtos (N.Fiscal de Entrada e Saída) | N |
| VSNopSer | ALFA | Natureza de Operação para Servicos (N.Fiscal de Entrada e Saída) | N |
| VSNumNfs | NÚMERO | Número da Nota Fiscal (N.Fiscal de Entrada e Saída) | N |
| VSOrigem | ALFA | Procedência da Regra (NFE - N.Fiscal de Entrada / NFS - N.Fiscal de Saída) | N |
| VSQtdBip | NÚMERO | Valor da base de cálculo de IPI por quantidade | N |
| VSRecIcm | ALFA | Recuperação de ICMS (N.Fiscal de Entrada) | N |
| VSRecIpi | ALFA | Recuperação de IPI (N.Fiscal de Entrada) | N |
| VSSeqIte | NÚMERO | Sequência do item de produto ou serviço da nota fiscal que está sendo inserida/alterada. | N |
| VSTemPro | ALFA | Indicativo se existe Código de Produto (N.Fiscal de Entrada) | N |
| VSTipNfe | NÚMERO | Tipo de Nota Fiscal de Entrada (N.Fiscal de Entrada) | N |
| VSTipNfs | NÚMERO | Tipo da Nota Fiscal de Saída (N.Fiscal de Saída) | N |
| VSTnsPro | ALFA | Transação de Produto (N.Fiscal de Entrada e Saída) | N |
| VSTnsSer | ALFA | Transação de Serviço (N.Fiscal de Entrada e Saída) | N |
| VSTtbIpi | NÚMERO | Indicativo do tipo de tributação de IPI (N.Fiscal de Entrada e Saída) | N |
| VSUfsCic | ALFA | Sigla do estado base para cálculo do ICMS | N |
| VSVenEnt | ALFA | Forma de escrituração para não tributadas (N.Fiscal de Saída) | N |
| VSVenIbi | ALFA | Transação considera valor do IPI na base do ICMS (N.Fiscal de Saída) | N |
| VSVenTcf | ALFA | Aplicação da natureza de operação (N.Fiscal de Saída) | N |
| VSVlrBic | NÚMERO | Valor Base ICMS (N.Fiscal de Entrada e Saída) | N |
| VSVlrBid | NÚMERO | Valor base IPI presumido (N.Fiscal de Entrada) | N |
| VSVlrBip | NÚMERO | Valor Base IPI (N.Fiscal de Entrada e Saída) | N |
| VSVlrIcm | NÚMERO | Valor ICMS (N.Fiscal de Entrada e Saída) | N |
| VSVlrIcs | NÚMERO | Valor do ICMS Substituído (N.Fiscal de Entrada e Saída) | N |
| VSVlrIic | NÚMERO | Valor isento ICMS (N.Fiscal de Entrada e Saída) | S |
| VSVlrIip | NÚMERO | Valor isento IPI (N.Fiscal de Entrada e Saída) | S |
| VSVlrIpd | NÚMERO | Valor do IPI presumido (N.Fiscal de Entrada) | N |
| VSVlrIpi | NÚMERO | Valor IPI (N.Fiscal de Entrada e Saída) | N |
| VSVlrLiq | NÚMERO | Valor Líquido (N.Fiscal de Entrada e Saída) | N |
| VSVlrOic | NÚMERO | Valor outros ICMS (N.Fiscal de Entrada e Saída) | S |
| VSVlrOip | NÚMERO | Valor outros IPI (N.Fiscal de Entrada e Saída) | S |

Atenção

Caso o parâmetro global LisVarReg esteja habilitado, a variável ListaVariaveis estará disponível em todos os identificadores de regras do sistema. O conteúdo desta variável lista os campos disponibilizados no identificador de regras em questão.

Não é aconselhada a ativação desse parâmetro global para o uso cotidiano. Esse recurso de listagem dos campos de identificadores auxilia a construção de regras e o Suporte para, por exemplo, depuração ou quando não houver acesso à documentação dos identificadores de regras.

## Páginas relacionadas

* [LisVarReg](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#LisVarReg)
