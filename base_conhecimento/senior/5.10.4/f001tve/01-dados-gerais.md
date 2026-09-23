# Dados Gerais

> **Fonte:** F001TVE - Transações de Vendas — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f001tve.htm  
> **Trilha:** Ajuda por telas > Cadastros > Transações > Parâmetros por Gestão  
> **Telas citadas:** F027STR, F075INF, F140VAL  
> **Identificadores de regras:** —

---
Detalhes Transação

Descrição detalhada da transação.

Aceita Manual

Este campo tem influência direta no filtro das transações nas telas de entrada e baixa de títulos. Quando este campo estiver como **Sim**, a transação poderá ser utilizada em processos que tenham interação com o usuário. Caso este campo esteja preenchido com **Não**, em muitos dos processos de entrada e baixa de títulos a transação não poderá ser utilizada.

Ao ser digitada uma transação com este campo igual a **Não**, durante a inclusão de um título, será apresentada a mensagem **Registro não existe. Selecione outro**.

Forma Contabilização

Código da forma de contabilização, pré-definidas em Cadastros > Controladoria >
Contabilidade > Formas Contabilização
> Cadastro.

Forma Rateio

Forma de rateio nos lançamentos de origem.

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

Indicativo se a transação atualiza o módulo de projetos.

Código Regra

Código de regra associada a transação.

> Observação
>
> A funcionalidade deste campo foi substituída pelos identificadores de regra.

Conta Contábil - 1, 2, 3 e 4

Contas contábeis reduzidas 1, 2, 3 e 4.

Item Negativo

É o indicativo se o item de serviço da nota fiscal deverá ser considerado como um desconto e diminuir os valores do total da nota fiscal. A informação de item negativo é permitido somente para transações de compra e venda de serviços. Quando configurado todos os valores da nota fiscal serão considerados, incluindo os impostos. A nota fiscal não permitirá que o seu valor total seja negativo, podendo ser exibida a mensagem em alguma circunstância: **Esta operação não é possível, valor da nota fiscal ficará negativo. Verifique os itens de serviço cuja transação é de desconto (parâmetro item negativo)**.

Importante

A utilização da parametrização de Item negativo não pode ser utilizada em conjunto com rateios por item na nota fiscal.

Nova Natureza Operação - CFOP

Código da nova natureza de operação fiscal (CFOP) - 4 dígitos.

Notas

* Para transações relacionadas à NFCom, quando não deve haver cálculo de ICMS e deve ser gerada a tag indSemCST, o campo deve conter o valor “0000”.
* Para integrações com o sistema WMW, os registros serão exportados somente quando o parâmetro Integra WMW estiver definido como "S - Sim" e este campo estiver preenchido. Caso contrário, o registro não será exportado.

Natureza Operação - CFOP

Código da natureza de operação fiscal (CFOP). Habilitado somente quando o campo Módulo da transação for igual à Vendas - NF Saída Serviços.

Considera apenas impostos Mov.Estoque

Indicativo se devem ser considerados apenas os impostos para o movimento de estoques.

Soma seguro no frete

Indicativo se deve somar o seguro no frete. Quando este parâmetro está definido como "S - Sim", o valor inserido no campo Soma seguro no frete, na tela F140VAL, será somado ao valor líquido da nota fiscal. Por outro lado, quando o parâmetro está definido como "N - Não", o valor do seguro não será incluído no cálculo do valor líquido.

Atualiza Último Pedido

Indicativo se a transação atualiza histórico do último pedido.

Aplicação Operação

Define a natureza de operação da transação. Para a geração dos impostos no documento fiscal (F075INF) esse campo deve ser preenchido com **S - Consumo Próprio** ou **V - Serviço** se o campo Consumidor Final estiver em branco. Quando for igual **V - Serviços**, o valor levado para apuração do faturamento é carregado na coluna **Produtos**, caso contrário é carregado na coluna **Serviços**.

NF Saída Devolução

Indicativo se a transação é para devoluções.

Considera Faturamento

Indicativo de atualização do histórico do cliente no fechamento da nota fiscal
saída.

NF Exige Pedido

Indicativo se a transação exige que a nota fiscal seja emitida baseada em pedido.

| Código | Descrição | ICMS | IPI |
| --- | --- | --- | --- |
| R | Remessas | Sim | Sim |
| O | Retornos | Sim | Sim |

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

Depósito Padrão

Código do depósito padrão sugerido nos pedidos, notas
fiscais e contratos. Para maiores detalhes, consulte a documentação da tela Sugestão de depósito padrão.

Embalagem Padrão

Código do tipo de embalagem padrão sugerido nas movimentações.

Mensagem - 1, 2,3 e 4

Permitem parametrizar um padrão de mensagens fiscais para a nota fiscal de saída, conforme a regra de sugestão.

Libera Guia Tráfego Automático

Indicativo se a guia de tráfego deve ser liberada automaticamente na geração da
pré-fatura.

Tipo de Venda

Indicativo do tipo de venda, normal, troca ou bonificação.

Situação

Indicativo da situação da transação.
Quando houver notas fiscais de entrada e saída que estejam com situação 2 ou 3 com seus títulos baixados e
contabilizados e estejam integradas para a gestão de tributos, pode-se inativar as transações de vendas ou de compras
utilizadas nas notas fiscais.

Indicativo exportação Palmtop

Indicativo se o registro foi alterado para exportar para o Pamtop.

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

## Páginas relacionadas

* [Formas Contabilização](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f048fct.htm)
* [F140VAL](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f140val.htm)
* [F075INF](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075inf.htm)
* [F027STR](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f027str.htm)
* [Sugestão de depósito padrão](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/sugestao-deposito-padrao.htm#menu_mercado/Sugestao-deposito-padrao)
* [regra de sugestão](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/manuais_processos/mercado/nf-e/regras-e-sugestoes-valores.htm#mensagens-fiscais)
* [Processo para Controle de Entrada e Saída de Produtos (PEPS/FIFO).](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/processo-controle-entrada-saida-produto.htm)
