# Dados Gerais

> **Fonte:** F001TCP - Transações de Compras — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f001tcp.htm  
> **Trilha:** Ajuda por telas > Cadastros > Transações > Parâmetros por Gestão > Compras  
> **Telas citadas:** E001TCP, E001TNS, F027STR, F440VAL  
> **Identificadores de regras:** VEN-000BUDEP02

---
Detalhes Transação

Detalhamento da transação.

Aceita Manual

Indica se a transação aceita ou não lançamentos manuais.

Forma Contabilização

Código da forma de contabilização.

Forma Rateio

Define-se a forma de rateio da transação.

* "0 - Sem Rateio": o rateio não será gerado nos processos nos quais a transação, com
  esta forma de rateio, for utilizada;
* "1 - Pré-definido c/ Confirmação": apresenta o rateio pré-definido em algum
  objeto de busca de rateio determinado no campo Critério
  Rateio, devendo o usuário confirmar o rateio apresentado;
* "2 - Pré-definido s/ Confirmação": o rateio é gerado automaticamente, conforme o Critério
  Rateio definido, não havendo a intervenção do usuário;
* "3 - Rateio Manual": o rateio será definido manualmente pelo usuário nos processos
  que utilizam alguma transação com esta forma de rateio.

Atualiza Projetos

Indica se o movimento da transação atualiza o controle de projetos.

Natureza Gasto

Código da Natureza Gasto.

Código Regra

Código de regra associada a transação. A funcionalidade deste campo foi substituída pelos identificadores de regra, que
são mais versáteis em sua aplicação.

Conta Contábil - 1,2, 3 e 4

Contas contábeis reduzida 1 a 4.

Item Negativo

Indica se o item de serviço da nota fiscal deverá ser considerado como um
desconto e diminuir os valores do total da nota.

Natureza Operação - CFOP 

Código da natureza de operação correspondente (CFOP).

Nova Natureza Operação - CFOP

Código da nova natureza de operação (CFOP) correspondente a transação (utilizada
devido transição conforme ajuste SINIEF 7/2002).

Considera apenas impostos Mov. Estoque 

Indica se deverão considerados apenas os valores de impostos na valorização movimento de estoque.

Soma Seguro no frete

Indicativo se deve somar o seguro no frete. Quando este parâmetro está definido como "S - Sim", o valor inserido no campo Soma seguro no frete, na tela Nota Fiscal de Entrada - Valores Diversos (F440VAL), será somado ao valor líquido da nota fiscal. Por outro lado, quando o parâmetro está definido como "N - Não", o valor do seguro não será incluído no cálculo do valor líquido.

Atualiza Históricos Última OC

Indica se a transação atualiza históricos das últimas compras.

Atualiza Históricos Entrada NF

Indica se a transação atualiza históricos das entradas de notas fiscais.

Aplicação Operação 

Aplicação da Natureza de Operação.

| Código | Descrição | ICMS | IPI |
| --- | --- | --- | --- |
| N | Industrialização/Comercialização | Sim | Sim |
| S | Consumo Próprio | Sim | Sim |
| I | Imobilizado | Sim | Sim |
| R | Remessas |  |  |
| O | Retornos |  |  |
| T | Transferências | Sim | Sim |
| D | Devoluções | Sim | Sim |
| B | Substituição Tributária | Sim | Sim |
| E | Energia Elétrica | Sim |  |
| C | Comunicação | Sim |  |
| F | Transporte | Sim |  |
| G | Integração | Sim | Sim |
| V | Serviços | Sim | Sim |
| X | Outros | Sim | Sim |

NFE Devolução

Indica se a transação é de nota fiscal de devolução. Este campo influencia no filtro das transações disponíveis para geração de notas fiscais.

NFE Exige Ordem Compra

Indica se a transação exige que a nota fiscal seja emitida baseada em ordem de
compra. Os parâmetros "Exige Ordem de Compra" (E001TNS.CPRAOC) e "Exige
Contrato" (E001TCP.CPRCTR) podem ser definidos como "S" simultaneamente, porém na nota
fiscal somente um dos documentos envolvidos (ordem de compra ou contrato), poderá
ser informado.

No caso do contrato, deverá ser informado qualquer contrato nos
dados gerais da nota, permitindo alterá-lo na grade. As consistências serão feitas para as
transações dos itens da nota.

Depósito Padrão

Código do depósito padrão sugerido nas ordens de compra, notas
fiscais e contratos se o identificador de regras VEN-000BUDEP02 estiver ativo

Mensagem 1,2,3,4

Mensagens padrões a serem impressas na nota fiscal de saída, pré-definidas em
Cadastros > Mercado e Suprimentos > Parâmetros Fiscais > Mensagens
NF. As mensagens fiscais presentes no cadastro do cliente terão prioridade no preenchimento das mensagens da nota fiscal.

Serão preenchidas todas as mensagens do cliente na nota, obedecendo a sequência definida no cadastro (Ex: mensagem informada no campo Mensagem - 2 no cadastro do cliente, será listada no campo Mensagem - 2 na nota fiscal). Após isso, ocorrerá o mesmo para as mensagens da transação.

Caso haja uma sobreposição de campos (Ex: cliente com uma mensagem no campo Mensagem - 4 e a transação com uma mensagem no campo Mensagem - 4, a mensagem do cliente será listada no campo Mensagem - 4, e a mensagem da transação será atribuída ao primeiro campo de mensagem disponível na nota fiscal.

Forma Não Tributadas

Forma de escrituração fiscal dos lançamentos
não tributados.

* "I - Isentas ICMS / Isentas IPI"
* "O - Outras ICMS / Outras IPI"
* "A - Isentas ICMS / Outras IPI"
* "B - Outras ICMS / Isentas IPI"
* "N - Nenhuma
* "S - Padrão Senior"

## Comportamento:

1. Quando na Gestão de Mercado ou de Suprimentos não houver o lançamento do ICMS, e não for
   feito o crédito do imposto: na escrituração dos livros fiscais será lançado o Valor contábil (deduzido o IPI,
   quando houver) em **ISENTAS**.
2. Quando na Gestão de Mercado ou de Suprimentos o lançamento do ICMS, e não for feito o
   crédito do imposto: na escrituração dos livros fiscais será lançado o Valor contábil (deduzido o IPI,
   quando houver) em **OUTRAS**.
3. Quando na Gestão de Mercado ou de Suprimentos não houver o lançamento do IPI, e não for
   feito o crédito do imposto: na escrituração dos livros fiscais será lançado o Valor contábil em **ISENTAS**.
4. Quando na Gestão de Mercado ou de Suprimentos houver o lançamento do IPI, e não for feito o crédito
   do imposto: na escrituração dos livros fiscais será lançado Valor contábil (deduzido o IPI,
   quando houver) em **OUTRAS**.
5. Quando na Gestão de Mercado ou de Suprimentos houver o lançamento do crédito do IPI de 50%, e for
   feito o crédito do imposto: na escrituração dos livros fiscais lançar o Valor dos 50% não tributados em **ISENTAS**
6. Quando "CprRic - Não Recupera ICMS": se não possuir ICMS, soma o "VlrLiq - Valor Líquido" como "Outros ICMS" desde que a aplicação da transação for "R", "O", "T" e "X", senão lança para isentos.

**Exceções**: para os itens 1 e 3 , o sistema atribuirá a condição de
**OUTRAS**, quando o parâmetro Aplicação da Operação (Transação) estiver
definido como "R - Remessas", "O - Retornos", "T - Transferências" ou "X - Outros".

Observação

Esta informação é buscada primeiramente no cadastro da situação tributária a partir da tela F027STR. Caso não haja parametrização, o sistema verifica a informação do campo **Forma Não Tributadas** acima.

Considera Valorização dos Estoques

Indicativo se o item da nota fiscal deve ser considerado ao ser efetuada a
valorização dos estoques pelo conhecimento de frete (nota tipo 8).

Situação 

Indicativo da situação da transação. Quando houver notas fiscais de entrada e saída que estejam com situação "2" ou "3" com seus títulos
pagos/baixados e contabilizados e estejam integradas para a gestão de tributos, poderá inativar as transações de vendas
e/ou de compras utilizadas nas notas fiscais.

Indicativo exportação Palmtop

Indica se o registro foi alterado para exportar para o Pamtop.

Data alteração Palmtop

Data da última alteração para o Palmtop.

Hora alteração Palmtop

Hora da última alteração para o Palmtop.

Usuário geração

Usuário responsável pela geração do registro.

Data geração

Data da geração do registro.

Hora geração

Hora da geração do registro.

Mov. Contr. Ent. Prod.

Indica se a transação movimenta os itens no Controle de Entrada de Produtos. Se o produto controlar entradas e saídas e a transação possuir esse parâmetro como **S-Sim**, o registro irá para o Controle, independentemente da origem (módulo **Comercial** ou **Tributos**).

* Processo para Controle de Entrada e Saída de Produtos (PEPS/FIFO).

**Código do ajuste da contribuição previdenciária sobre a receita bruta - REINF**

Permite que as informações da apuração do imposto 49 sejam enviadas para o registro R-2060 da EFD-Reinf. As transações que possuírem esse campo informado gerarão os ajustes para cada Classificação Fiscal.

Transação permite Geração de Manifesto

Indica se a transação permite a geração de "Manifestação de destinatário" na geração de Nota fiscal de entrada agrupada.

## Páginas relacionadas

* [F440VAL](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f440val.htm)
* [VEN-000BUDEP02](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_000budep02.htm)
* [Mensagens
NF](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f024msg.htm)
* [F027STR](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f027str.htm)
* [Processo para Controle de Entrada e Saída de Produtos (PEPS/FIFO)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/processo-controle-entrada-saida-produto.htm)
