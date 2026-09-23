# F095HFO - Definições/Histórico de Fornecedor

> **Fonte:** F095HFO - Definições/Histórico de Fornecedor — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f095hfo.htm  
> **Trilha:** Ajuda por telas > Cadastros > Clientes e Fornecedores > Fornecedores  
> **Telas citadas:** F000PGS, F001TCP, F045CXA, F070ECT, F095HDU, F095HFO, F097MON  
> **Identificadores de regras:** CPR-440VLRMO02

---
Ajuda por telas > Cadastros > Clientes e Fornecedores > Fornecedores > Definições/Histórico

Essa tela permite o cadastro das definições por empresa/filial dos fornecedores.

Fornecedor

 Código e nome do fornecedor.

Empresa

 Código da empresa.

Filial

 Código da filial.

É Indústria

 Indica se o fornecedor é indústria ou equiparado a industria para IPI presumido.

Grupo Contas Pagar

 Código do grupo do contas a pagar.

% Desconto 1

 Percentual de Desconto 1.

% Desconto 2

 Percentual de Desconto 2.

% Desconto 3

 Percentual de Desconto 3.

% Desconto 4

 Percentual de Desconto 4.

% Desconto 5

 Percentual de Desconto 5.

Tipo de Rateio Valor Conhecimento de Frete

Tipo de rateio do valor do conhecimento de frete para efetuar o movimento de estoque (acerto).

**Importante**

Há uma particularidade em relação às movimentações de estoque em uma nota fiscal de frete ligada a uma nota fiscal de industrialização, onde o sistema não verifica o campo **Tipo de Rateio Valor Conhecimento de Frete** no fornecedor. Isso ocorre com notas fiscais do tipo **4 - Industrialização**, que podem não gerar um movimento para cada item, sendo necessário aplicar o cálculo com base no valor, desconsiderando o referido campo.

**Obs.:** o identificar de regras CPR-440VLRMO02 pode ser utilizado para customizar o cálculo padrão do sistema.

Percentual/Tipo Rateio de Frete

 Percentual e tipo de rateio de frete para os itens de produto.

Percentual/Tipo Rateio de Seguro

 Percentual e tipo de rateio de seguro para os itens de produto.

Percentual/Tipo Rateio de Embalagens

 Percentual e tipo de rateio de embalagens para os itens de produto.

Percentual/Tipo Rateio de Encargos

 Percentual e tipo de rateio de encargos para os itens de produto e
serviço.

Percentual/Tipo Rateio de Outras Despesas

 Percentual e tipo de rateio de outras despesas para os itens de produto
e serviço.

Tipo Rateio Valor de Arredondamento

 Tipo de rateio do valor de arredondamento para os itens de produto e
serviço.

Tipo de Rateio Valor de Frete de
Importação

 Tipo de rateio do valor de frete de Importação para os itens de
produtos.

Tipo de Rateio de Seguros de Importação

 Tipo de rateio do valor de seguro de Importação para os itens de
produtos.

Tipo de Rateio Valor de Outras Desp. de
Importação

 Tipo de rateio de valor de outras despesas de Importação para os itens
de produto e serviço.

% Funrural/INSS

 Percentual do Funrural ou INSS para Produto, considerado nas ordens de compra e notas fiscais de entrada. Veja mais detalhes na documentação de processo do Funrural.

Observações

* O % Funrural já considera o valor do Gilrat em sua porcentagem;
* O % Funrural não pode ser inferior ao % GILRAT.

% GILRAT

Percentual de Gilrat que compõe a alíquota de Funrural.

% SENAR/SENAT

Percentual do imposto SENAT/SENAR para notas fiscais de entrada. Veja mais detalhes na documentação de processos do Senar.

% INSS

 Percentual do INSS para o serviço.  
 Para fazer a retenção é necessário que seja informado na Transação de Entrada, o campo
Desconta INSS/Funrural NF com o valor S.

% INSS Empresa

 Percentual do INSS Empresa.

% ISS

 Percentual do ISS.

% IRRF

 Percentual do IRRF.

Prazo Entrega

 Quantidade de das de prazo de entrega do fornecedor.

Tabela Preço Padrão

 código da tabela de preço padrão.

Condição de Pagamento Padrão

 código da condição de pagamento padrão.

Transportadora Padrão

 código da transportadora padrão.

Frete CIF ou FOB

 Indicativo de frete para o fornecedor é CIF ou FOB.

Portador padrão

 código do portador padrão.

Carteira padrão

 código da carteira padrão.

Código Forma Pagamento

Quando um título de imposto para o financeiro é gerado ao ser emitida uma nota fiscal de vendas, o conteúdo deste campo será gravado como forma de pagamento no título do imposto.

Fornecedor Montador?

 Indica se o fornecedor é montador de produtos.

% Mora M?/Tolerância

 Percentual de juros de mora e quantidade de dias de tolerância para o contas a pagar.

Tipo Juros

 Indicativo de tipo de juros para o contas a pagar.

% Multa/tolerância

 Percentual de multa e quantidade de dias de tolerância para o contas a pagar.

Calcula Desc. Antecipação

 Indica se calcula desconto por antecipação de pagamento.  
 Quanto mais antecipadamente for efetuado o pagamento de um título, maior
será o desconto concedido/recebido. Ex.: Percentual = 0,05 % /dia. Caso o
título seja quitado com um dia de antecedência, será concedido/recebido um desconto de 0,05%.
Caso seja quitado três dias antes do vencimento, ser?concedido/recebido um desconto de 0,15 %.

% Desconto títulos/tolerância

 Percentual de desconto e quantidade de dias de tolerância para os
títulos gerados.

Banco/Agência/Nº Conta

 código do banco e agência e número da conta corrente.

Critério Dia Vencimento

 Critério para escolha do dia do vencimento.

Quantidade Dias Vencimento

 Quantidade de dias para cálculo de vencimento.

Quantidade Mínima Dias Entrada e
Vencimento

Quantidade mínima de dias entre a data de entrada do título e o
vencimento deste. Campo visível apenas pelo Varejo Senior.

Favorecido

 Número do CNPJ ou CPF do favorecido.

Conta Contábil - 1

 Número da conta contábil reduzida 1.

Conta Contábil - 2

 Número da conta contábil reduzida 2.

Conta Contábil - 3

 Número da conta contábil reduzida 3.

Conta Contábil - 4

Número da conta contábil reduzida 4.

Conta Auxiliar Cliente

Informa-se uma conta auxiliar cliente.  
Verificar parâmetro DesCtaAux da tela F000PGS.  
Verificar o campo Gerar Conta Auxiliar Cliente da tela F070ECT.  
Verificar os campos Tipo Relacionamento, Incrementar pelo Relacionamento e Critério na tela F045CXA, sendo que este último deve estar como 2.

Conta Auxiliar Adto. Cliente

Informa-se uma conta auxiliar adiantamento cliente.  
Verificar parâmetro DesCtaAux da tela F000PGS.  
Verificar o campo Gerar Conta Auxiliar Cliente da tela F070ECT.  
Verificar os campos Tipo Relacionamento, Incrementar pelo Relacionamento e Critério na tela F045CXA, sendo que este último deve estar como 2.

Conta Auxiliar - 1

 Conta contábil 1 de composição auxiliar do fornecedor.

Conta Auxiliar - 2

 Conta contábil 2 de composição auxiliar do fornecedor. Há a função de programador GerarContaAuxiliarCliFor
que pode ser utilizada para a cria?o da conta auxiliar, ao gerá-la será adicionado o texto Adiantamento ao final da sua descrição.

Depósito para Armazenagem (WMS)

Código do depósito padrão para armazenagem no sistema de WMS.

Espécie Documento

Espécie de documento para fins fiscais. Deve ser informado o modelo oficial do documento conforme 'Tabela de Modelos de Documentos Fiscais' Convênios ICMS 57/95, 96/97e 31/99.

Origem da Mercadoria

Sequência padrão do endereço de origem da mercadoria.

Tipo Pag. Montagem

 Indica a forma em que pendência de montagem será apurada (tela F097MON) e gerada no contas a pagar.

* OC - Ordem de Compra de Serviço;
* CP - Título a Pagar;

Tipo Pag. Frete

 Indica a forma em que o frete será apurado e gerado no contas a pagar.

* OC - Ordem de Compra de Serviço;
* CP - Título a Pagar;

**Usuário de Geração**   
 Usuário que cadastrou as definições do fornecedor para a empresa/filial.

Data de Geração

Data em que as definições do fornecedor foram criadas para a empresa/filial.

Hora de Geração

Hora em que as definições do fornecedor foram criadas para a empresa/filial.

Usuário de Alteração

Último usuário que alterou as definições do fornecedor para a
empresa/filial.

Data de Alteração

Última data em que as definições do fornecedor para a empresa/filial
foram alteradas.

Hora de Geração

Última hora em que as definições do fornecedor para a empresa/filial foram alteradas.

Considera Qtd. Dev. Item NFE

 Define se as as quantidades devolvidas de um item de produto da nota
fiscal de entrada devem ser consideradas no cálculo de valorização de
notas fiscais de entrada do tipo 8 - Conhecimento de frete. Este
parâmetro será inicializado com a opção N - Não, de modo a não
considerar a quantidade devolvida na valorização, mantendo o padrão
atual do sistema.

Considera Qtd. Dev. Val. NFE   
Considera as quantidades devolvidas no cálculo de valorização nas notas fiscais de entrada do tipo “8 – NF Frete/Serviços Agregados”.

% Diferimento   
Percentual que será utilizado para o cálculo do valor do ICMS Diferido em cotações, contratos, ordens de compras, pedidos, pré-faturas e notas fiscais de entrada e saída.

Transação de recebimento para produto

Possibilita listar as transações em que a Operação de Compra for do tipo **R - Recebimento**, na guia Dados Gerais da tela Transações de Compras (F001TCP), e a transação de produto for do módulo **COF - Compras - NF Entrada Produtos**.

Transação de pagamento para produto

Possibilita listar as transações em que a Operação de Compra for do tipo **P - Pagamento**, na guia Dados Gerais da tela Transações de Compras (F001TCP), e a transação de produto for do módulo **COF - Compras - NF Entrada Produtos**.

Transação de recebimento para serviço

Possibilita listar as transações em que a Operação de Compra for do tipo **R - Recebimento**, na guia Dados Gerais da tela Transações de Compras (F001TCP), e a transação de serviço for do módulo **COS - Compras - NF Entrada Serviços**.

Transação de pagamento para serviço

Possibilita listar as transações em que a Operação de Compra for do tipo **P - Pagamento**, na guia Dados Gerais da tela Transações de Compras (F001TCP), e a transação de serviço for do módulo **COS - Compras - NF Entrada Serviços**.

**Percentual do Diferimento de ICMS relativo ao FCP**

Percentual do diferimento de ICMS relativo ao FCP sugerido para o cálculo do valor do diferimento de ICMS relativo ao FCP nos processos de compras e recebimento. Este campo não tem preenchimento obrigatório.

Emitir Contra Nota

Permite indicar entre "**S** - Sim" ou "**N** - Não" para emitir contra nota para as notas fiscais de entrada do tipo 1, 9 ou 11.

**Calcula Fundeinfra**

Permite indicar entre "**S** - Sim" ou "**N** - Não" para a execução do cálculo do Fundeinfra.

## Botões

Duplicar

Exibe a tela F095HDU para duplicação de definição de fornecedores.

Rateio

Exibe a tela de definição de rateio.

## Identificadores de regras

| Módulo | Código |
| --- | --- |
| GER | 000REMIF01 |

|  |  |
| --- | --- |
|  | Veja também: |

* Criação automática de contas auxiliares

## Páginas relacionadas

* [Ajuda por telas](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/ajuda-telas.htm)
* [CPR-440VLRMO02](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/cpr_440vlrmo02.htm)
* [Funrural](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/manuais_processos/agronegocio/processos/impostos/funrural.htm)
* [Senar](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/manuais_processos/agronegocio/processos/impostos/senar.htm)
* [Critério Dia Vencimento](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_financas/pf_parametros_criteriodiavencimento.htm)
* [F000PGS](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm)
* [F070ECT](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070ect.htm)
* [F045CXA](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f045cxa.htm)
* [GerarContaAuxiliarCliFor](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/regra_funcoes/gerarcontaauxiliarclifor.htm)
* [F097MON](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f097mon.htm)
* [F095HDU](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f095hdu.htm)
* [GER](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ger_095cadfo03.htm)
* [000REMIF01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ger_000remif01.htm)
* [Criação automática de contas auxiliares](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f045pca_contaautomatica.htm)
