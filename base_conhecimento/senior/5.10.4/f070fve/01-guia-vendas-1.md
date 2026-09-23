# Guia Vendas 1

> **Fonte:** F070FVE - Parâmetros da Filial para Vendas — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070fve.htm  
> **Trilha:** Ajuda por telas > Cadastros > Filiais > Parâmetros por Gestão  
> **Telas citadas:** E070FIL, E120PED, F020SNF, F070FVE, F120GPC, F120GPD, F161GPC, F420GOC  
> **Identificadores de regras:** VEN-000CRECL01, VEN-120CONDG03, VEN-120LOTPA01, VEN-120PEDSE01

---
Período Inicial/Final 

Data inicial e final do período em aberto para movimentações de saída (emissão
pedidos, pré-faturas, contratos, notas fiscais de saída e faturas).

Filial como Cliente 

Código da filial como cliente.

Filial como Fornecedor 

Código da filial como fornecedor.

Série NF Saída Padrão 

Série padrão para sugestão na emissão da nota fiscal de saída.

Cliente Igual Fornecedor 

Indicativo se os códigos do cliente e fornecedor deverão ser iguais.
Caso esteja definido como S-Sim, o sistema sempre efetuará automaticamente o cadastro correspondente, ou seja, se o
usuário estiver cadastrando um cliente, o sistema efetuará o cadastro de um fornecedor
com mesmo código e dados básicos.

Observação

A alteração do parâmetro de N para S não será permitida quando houver
cliente e/ou fornecedor cadastrado.

CNPJ/CPF Cliente 

Indicativo se a informação do CNPJ/CPF deverá ser obrigatória no sistema. Quando utilizada a proprietária Varejo Senior o campo deve ser igual a S-Sim, pois é obrigatório informar no cadastro CNPJ/CPF do cliente.

CNPJ/CPF Cliente Repetido 

Indicativo se o CNPJ/CPF ou o número de identificação fiscal pode ser repetido, ou seja, se pode haver mais de
um cliente ou fornecedor com o mesmo CNPJ/CPF. O sistema permite alterar este campo para "N - Não" mesmo se existirem cadastros com CNPJ/CPF ou o número de identificação fiscal repetidos na base. Para novos cadastros ou alterando CNPJ/CPF ou o número de identificação de um cadastro existente será realizada a validação impedindo o cadastramento caso for repetido.

Observação:

Quando utilizada integração com o sistema de Varejo Senior, esse campo deve ser configurado como **N - Não** para todas as filiais cadastradas, pois não é permitido repetir CNPJ/CPF para outro cliente ou fornecedor interno. Dessa forma, ao informar um CPF/CNPJ no Retaguarda de qualquer filial, essa pesquisa será efetuada diretamente no ERP e integrada para a loja que efetuou a consulta, não necessitando assim de um novo cadastro.

CNPJ/CPF Repres. Repetido 

Indicativo se o CNPJ/CPF do representante pode ser repetido, ou seja, se pode haver
mais de um representante com o mesmo CNPJ/CPF.

Observação:

Quando utilizada integração com o sistema de Varejo Senior, esse campo deve ser configurado como **N - Não** para todas as filiais cadastradas, pois não é permitido repetir CNPJ/CPF para outro representante interno. Dessa forma, ao informar um CPF/CNPJ no Retaguarda de qualquer filial, essa pesquisa será efetuada diretamente no ERP e integrada para a loja que efetuou a consulta, não necessitando assim de um novo cadastro.

Nº Pedido Automático 

Indicativo se o número do pedido de venda deve ser numerado automaticamente na digitação
de novos pedidos ao sair do campo Pedido nas rotinas
de entrada dos pedidos. Observar que a informação atribuída neste campo terá
influência no campo número inicial pedido previsão.
Quando o parâmetro for informado como S-Sim, o
identificador de regras VEN-120PEDSE01
bloqueará um número de pedido fora de sequência. Quando o parâmetro for definido como N-Não (não gerar a numeração automática), as rotinas que geram pedidos de forma automática não funcionarão (como por exemplo, nas telas F161GPC e F420GOC).

Utiliza Rota

Indicativo se a filial utiliza rota de entrega.

Número Inicial Pedido Previsão 

Este campo tem dependência direta com a informação digitada no campo Nº
pedido Automático, ao qual se for atribuído S (sim), não receberá informação (ficará desabilitado).

Caso no campo Nº pedido Automático for informado N (não), então será informado o
número inicial do pedido de previsão. Observar que a tabela E120PED (pedidos) ficará
ordenada por: pedido normais e previsão.

Observação

Na digitação dos pedidos a numeração dos pedidos normais não poderá ultrapassar os
pedidos de previsão. Aconselha-se informar um número de pedido de previsão maior, para não correr o risco da numeração de
pedidos normais ultrapassar esse número.

Incremento Nº Pedido

Valor do incremento da numeração de pedidos, quando a numeração é automática. Ao
atribuir zero o número será incrementado de um. Caso informado um número maior
que um, será atribuído este incremento ao número do pedido.

Máx.Itens no Pedido 

Número máximo (até 9999) de itens de produto que o pedido irá possuir.

Valor Mínimo Pedido 

Valor mínimo permitido para os pedidos.

Pedido entra Bloqueado 

Indicativo se o pedido fica automaticamente bloqueado na digitação.

Quando o pedido é bloqueado devido a esta configuração da filial, nas telas de Pedido (F120GPD e F120GPC) o sistema apenas apresenta uma mensagem de aviso e permite continuar com o processo de geração do pedido. Portanto, caso seja necessário barrar a entrada do pedido através das telas mencionadas, é necessário utilizar o identificador de regras VEN-120CONDG03. Veja abaixo um exemplo de regra na utilização dessa configuração:

## Regra

**Funcionamento da regra**: foi criado um cursor na tabela de filial (E070Fil) para verificar a informação presente no campo PedBlo (ele indica se o pedido fica automaticamente bloqueado na entrada/digitação). Quando esse campo estiver com valor igual a “S - Sim”, será emitida uma mensagem de erro e o pedido será bloqueado.

**Regra**:

```
DEFINIR ALFA VSORIGEM;

DEFINIR ALFA VCURSOR;

DEFINIR ALFA VSQL;

DEFINIR NUMERO VSCODEMP;

DEFINIR NUMERO VSCODFIL;

DEFINIR ALFA VPEDBLO;

Inicio

Se (VSORIGEM = "PED")

Inicio

SQL_Criar(VCURSOR);

VSQL = "SELECT PEDBLO " +

" FROM E070FIL " +

" WHERE CODEMP = :VSCODEMP " +

" AND CODFIL = :VSCODFIL";

SQL_DefinirComando(VCURSOR, VSQL);

SQL_DEFINIRINTEIRO(VCURSOR, "VSCODEMP", E120PED.CODEMP);

SQL_DEFINIRINTEIRO(VCURSOR, "VSCODFIL", E120PED.CODFIL);

SQL_AbrirCursor(VCURSOR);

Se (SQL_EOF(VCURSOR) = 0)

Inicio

SQL_RETORNARALFA(VCURSOR, "PEDBLO", VPEDBLO);

Fim;

Se (VPEDBLO = "S")

Inicio

Mensagem(Erro, "Pedido bloqueado devido ao Parâmetro da Filial.");

Fim;

SQL_FecharCursor(VCURSOR);

SQL_Destruir(VCURSOR);

Fim;

Fim;
```

Observação

O parâmetro global AnlPedBlo, juntamente com o identificador de regras VEN-000CRECL01, pode ser utilizado para indicar que o sistema deve verificar o crédito do cliente mesmo quando o pedido entrar bloqueado (**Pedido entra Bloqueado** igual a **S** na tela F070FVE). Isso é feito por meio
das variáveis
**VSBLOQUE** e
**VSMOTIVO**.

Dias Limite Entrega Pedido

Quantidade de dias limite para aceitação do pedido.

Dias Antes Aceita Pedido 

Quantidade de dias anterior ao atual aceito para a data de entrega do pedido.

Observação

Ao alterar o campo Previsão: Data/Hora, o sistema valida a data informada em relação à data atual, considerando o parâmetro "Dias Antes Aceita Pedido", configurado na tela "Parâmetros da Filial para Vendas (F070FVE)".

Caso a data de previsão seja inferior ao limite permitido pelo parâmetro, o sistema apresenta a mensagem: "Data de previsão de entrega menor que a data atual".

Quando o parâmetro "Dias Antes Aceita Pedido" estiver configurado com o valor 999, a validação não será realizada e a mensagem não será apresentada, permitindo que o campo Previsão: Data/Hora seja zerado.

Dias Atraso Médio Pedido

Quantidade de dias de atraso médio aceita na entrada do pedido.

## Exemplo

Um cliente está devendo duas parcelas: uma parcela atrasou 30 dias e a outra 60 dias. Somando e fazendo uma média, o atraso se torna de 45 dias. Quando informado no campo Dias Atraso Médio Pedido o valor de 40, automaticamente, neste caso, o pedido será bloqueado. Pois o atraso médio é de 45 dias e o permitido é de 40.

Dia Maior Atraso Pedido 

Quantidade de dias de maior atraso aceita na entrada do pedido. Caso algum título no contas a receber possua um atraso que ultrapasse o valor informado neste campo, o bloqueio será feito.

Dias p/ Aprovação Pedido Cliente Novo 

Quantidade de dias para aprovação de pedidos após o cadastro de um cliente novo.

Quantidade Pagamento Cartório Pedido 

Quantidade máxima de pagamentos em cartório aceita na entrada de pedido.

Quantidade Títulos Atraso Pedido 

Quantidade máxima de títulos em atraso aceita na entrada de pedido.

Dias Atraso Título Pedido 

Quantidade de dias de atraso de títulos aceita para entrada de pedido.

Quantidade Cheques s/ Fundo Pedido 

Quantidade de cheques sem fundo (devolvido) que serão aceitos na entrada de pedido.

Limite Crédito Pedido 

Indicativo se aceita ou não pedido com estouro de limite de crédito.

Transação Pedido Produto

Transação padrão para entrada de pedido de produto.

Transação Pedido Serviço

Transação padrão para entrada de pedido de serviço.

Dias Entre Faturamento

Quantidade de dias permitida entre datas de faturamento.

Definição Nº Título

Indicativo do critério para definição do número de título do contas a receber:

* **N - Pelo Número da Nota Fiscal**: com esta parametrização, o sistema assume o número da nota fiscal mais o sufixo constante nas definições da parcela do cadastro da série - F020SNF
* **S - Sequencial Livre**: o número do título é gerado considerando o número da última duplicata constante também no cadastro da série. Ou seja, segue um sequencial livre não utilizando o número da nota para compor o número do título. Isto é válido também quando os títulos são gerados a partir de pedidos

**% Desconto SUFRAMA**

Percentual de desconto para Suframa.

% ISS Cidade Filial

Percentual do ISS válido para a cidade da filial.

Série N.Fiscal Remessa

Código padrão da série da nota fiscal de remessa de serviço.

Representante Padrão

Código do representante padrão (NF Produtor).

Dias Atraso Médio Fatura

Quantidade máxima de dias de atraso médio aceita para faturamento.

Dias Maior Atraso Fatura

Quantidade máxima de dias de maior atraso aceita para faturamento.

Quantidade Pagamento Cartório Fatura

Quantidade máxima de pagamentos em cartório aceita para faturamento.

Quantidade Títulos Atraso Fatura

Quantidade máxima de títulos em atraso aceita para faturamento.

Dias Atraso Título Fatura

Quantidade de dias de atraso de títulos aceita para faturamento.

Quantidade Cheques s/ Fundo Fatura

Quantidade máxima de cheques s/ fundo aceita para faturamento.

Limite Crédito Fatura

Indicativo se aceita ou não faturamento com estouro de limite de crédito.

Transação Cancelamento C. Receber

Transação padrão de baixa do C. Receber por cancelamento.

Limite % Variação Peso

Valor limite para o percentual de variação do peso informado nas telas de entrada e
saída de vendas.

Inscrição Estadual Cliente Válida

Define como o sistema deve se comportar ao validar IE de clientes conforme as opções:

* "S - Sim": Sempre valida e bloqueia a operação se IE for inválida ou não informada;
* "I - Sim quando informada": Valida apenas se informada e bloqueia se inválida;
* "N - Não": Valida mas apenas avisa, ou seja, permite prosseguir caso desejar mesmo que a IE esteja incorreta.

Aceita Pedido sem Estoque

Indicativo se a filial aceitar gerar pedidos sem estoque suficiente para os itens.
Para produtos controlados por lote com o identificador de regras
VEN-120LOTPA01 cadastrado e ativo, será permitido gerar pedidos sem estoques
independente do parâmetro estar definido como N, pois será utilizado o lote
padrão.

Integra WMW

Indica se esse registro deve ser integrado para o WMW.

Situação WMW

Indica se esse registro está ativo ou inativo para o WMW.

## Páginas relacionadas

* [VEN-120PEDSE01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_120pedse01.htm)
* [F161GPC](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f161gpc.htm)
* [F420GOC](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f420goc.htm)
* [F120GPD](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f120gpd.htm)
* [F120GPC](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f120gpc.htm)
* [VEN-120CONDG03](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_120condg03.htm)
* [AnlPedBlo](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#AnlPedBlo)
* [VEN-000CRECL01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_000crecl01.htm)
* [Percentual de desconto para Suframa](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/deduzir_icms_pis_cofins_.htm)
* [VEN-120LOTPA01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_120lotpa01.htm)
