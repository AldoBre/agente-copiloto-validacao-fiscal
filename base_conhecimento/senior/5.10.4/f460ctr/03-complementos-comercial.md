# Complementos Comercial

> **Fonte:** F460CTR - Contrato de Compra (Comercial/Financeiro/Eventos) — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f460ctr.htm  
> **Trilha:** Ajuda por telas > Suprimentos > Gestão de Compras > Contratos  
> **Telas citadas:** E001TNS, E024MSG, E028CPG, E073TRA, E460CCP, E460CCS, E460IMO, F461GNC  
> **Identificadores de regras:** —

---
Para contratos dos tipos:

* 1 - Comercial Normal
* 2 - Comercial Adicional
* 5 - Comercial Sócios
* 9 - Comercial de Abastecimento\*

Qtde. Parcelas

Quantidade de parcelas do contrato. \*Não possui aplicação no tipo de contrato 9 - Comercial de Abastecimento.

Observação

Esse campo impacta no valor total do contrato, pois multiplica o valor dos itens de produto/serviço de competência igual a 00/0000, pela quantidade de parcelas.

Meses Intervalo

Quantidade de meses de intervalo entre as parcelas. Se o faturamento for mensal, preencha com 1; se for bimestral, 2 e assim por diante. \*Não possui aplicação no tipo de contrato 9 - Comercial de Abastecimento.

A data de geração dos títulos considera esse campo para determinar a quantidade de meses que vai haver de intervalo entre um título e outro.

Parc. Processadas

Quantidade de parcelas processadas.

Periodicidade de Reajuste

Periodicidade de reajuste do contrato, em meses. Controla a aplicação dos reajustes aplicados ao contrato.

Início Reajuste

Data inicial para reajuste do contrato. Após o processamento do reajuste, os novos valores ficarão gravados nos itens dos contratos e serão aplicados para qualquer competência que venha a ser recebida, mesmo que seja anterior ao período de reajuste.

Ult. Reajuste

Data do último reajuste aplicado ao contrato.

Início Processamento

Data do início do processamento. \*Não possui aplicação no tipo de contrato 9 - Comercial de Abastecimento.

Dia Base Processamento

Dia base do mês para processamento das competências do contrato. Ao processar o contrato nas telas do sistema, este campo é utilizado como filtro entre a data de processamento do documento e as competências do contrato. \*Não possui aplicação no tipo de contrato 9 - Comercial de Abastecimento.

Observação

Competência em contrato trata-se das parcelas, pois elas serão geradas com base nas competências, porém o campo Dia Base Processamento não influência no dia do vencimento da parcela. Essa informação está cadastrada na condição de pagamento informada no contrato.

Para contratos financeiros que geram parcelas, o Dia Base Processamento não é utilizado, assim não influenciando nas parcelas. Isso ocorre porque há campos específicos para essa finalidade na tabela Compras - Contratos - Itens das Formas de Pagamento (E460IMO).

Vigência do contrato

Datas inicial e final de vigência do contrato.

Dias de aviso de cancelamento

Especifica em numero de dias, o período de solicitação de cancelamento do contrato em relação à data final de vigência. Campo apenas informativo não tratado pelo sistema.

Condição Pagto

Condição de pagamento. Registros gravados na tabela E028CPG e cadastros em Tabelas > Comercial > Condições de Pagamento > Cadastro. A sugestão padrão é efetuada a partir das definições/ histórico do fornecedor.

Utiliza Juros/Multa no Contrato

Indicativo se o contrato usará juros e multa.

Juros/Tolerância/Tipo

Percentual, dias de tolerância e tipo de juros. A sugestão padrão é efetuada a partir das definições/ histórico do fornecedor.

Multa/Tolerância

Percentual e dias de tolerância de multa. A sugestão padrão é efetuada a partir das definições/ histórico do fornecedor.

Transportadora

Código da transportadora. Registros gravados na tabela E073TRA e cadastrados a partir de Cadastros > Transportadoras > Cadastro. A sugestão padrão é efetuada a partir das definições/ histórico do fornecedor.

Transação Produtos

Código da transação a ser sugerida para os itens de produto. Registros gravados na tabela E001TNS e cadastrados a partir de Tabelas > Transações > Cadastro > Compras > Ordem Compra/NF Entrada/Faturas . A sugestão padrão é efetuada a partir das Tabelas > Comercial > Fiscais > Parâmetros por Estado.

Transação Serviços

Código da transação a ser sugerida para os itens de serviço. Registros gravados na tabela E001TNS e cadastrados a partir de Tabelas > Transações > Cadastro > Compras > Ordem Compra/NF Entrada/Faturas . A sugestão padrão é efetuada a partir das Tabelas > Comercial > Fiscais > Parâmetros por Estado.

Mensagem 1

Código da 1ª mensagem para a nota fiscal. Registros gravados na tabela E024MSG e cadastrados a partir de Tabelas > Comercial > Fiscais > Mensagens NF . A sugestão padrão é efetuada a partir das Tabelas > Transações > Cadastro > Compras > Ordem Compra/NF Entrada/Faturas.

Mensagem 2

Código da 2ª mensagem para a nota fiscal. Registros gravados na tabela E024MSG e cadastrados a partir de Tabelas > Comercial > Fiscais > Mensagens NF . A sugestão padrão é efetuada a partir das Tabelas > Transações > Cadastro > Compras > Ordem Compra/NF Entrada/Faturas.

Mensagem 3

Código da 3ª mensagem para a nota fiscal. Registros gravados na tabela E024MSG e cadastrados a partir de Tabelas > Comercial > Fiscais > Mensagens NF . A sugestão padrão é efetuada a partir das Tabelas > Transações > Cadastro > Compras > Ordem Compra/NF Entrada/Faturas.

Mensagem 4

Código da 4ª mensagem para a nota fiscal. Registros gravados na tabela E024MSG e cadastrados a partir de Tabelas > Comercial > Fiscais > Mensagens NF . A sugestão padrão é efetuada a partir das Tabelas > Transações > Cadastro > Compras > Ordem Compra/NF Entrada/Faturas.

Observação

Todos os campos de mensagem não têm aplicação para o tipo de contrato 9.

Último Processamento

Data do último processamento. Este campo refere-se à última competência gerada no lançamento da nota via contrato, a qual é informada no campo Competência da tela Nota Fiscal de Entrada via Contratos de Compra Comerciais (F461GNC).

Observação

A data de competência e a data de emissão da nota fiscal podem ser ou não diferentes. O sistema não valida se as duas datas são ou não diferentes, pois cada cliente poderá gerar a competência que melhor se adequa ao seu processo.

Número da Última Nota Fiscal/Série/Filial

Número da última nota fiscal, série e filial gerada a partir do contrato.

Consiste Quantidade

Na digitação de um novo contrato, o campo ficará habilitado e com valor default igual a N (Não). Este campo ficará habilitado para contratos tipo 9(comercial de abastecimento). Tem o objetivo de indicar se no contrato será efetuado uma consistência ou não da quantidade atribuída ao item, especificamente na geração de ordens de compra, através das rotinas de geração de ordem compra via contrato ou ordem de compra via solicitação.  

Quando o campo for S (sim), o sistema passará a controlar os itens do contrato, quanto já foi utilizado da quantidade para a geração de ordens de compra. Para efetuar este controle, foi implementado também um campo nas grades das GUIAs de Produto e Serviço, denominado Qtd. Util. Ger. OCs, irá indicar a quantidade já utilizada do item do contrato [E460CCP.QtdUti / E460CCS.QtdUti (Quantidade já utilizada para geração de OC no contrato de abastecimento)], lembrando, esSe campo ficará visível apenas para contrato tipo 9 (Comercial de Abastecimento) e fica sempre desabilitado, ou seja, serve apenas para visualizar a quantidade já utilizada na geração de ordem de compras.

  
Importante: esse campo indica a quantidade utilizada e não o saldo do item, o qual corresponde a quantidade do item no contrato - quantidade utilizada. Ao exibir um contrato e o valor do campo Consiste Quantidade for igual a S e existir algum item deste contrato com quantidade já utilizada maior que zero o campo ficará desabilitado, caso contrário ficará habilitado.

## Páginas relacionadas

* [reajustes](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f460rea.htm)
* [Tabelas > Comercial > Condições de Pagamento > Cadastro](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f028gcp.htm)
* [definições/ histórico do fornecedor](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f095hfo.htm#F095HFO_DEcodcpg1)
* [definições/ histórico do fornecedor](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f095hfo.htm#F095HFO_DEpagjmm1)
* [Cadastros > Transportadoras > Cadastro](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f073tra.htm)
* [definições/ histórico do fornecedor](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f095hfo.htm#F095HFO_DEcodtra1)
* [Tabelas > Transações > Cadastro > Compras > Ordem Compra/NF Entrada/Faturas](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f001tcp.htm)
* [Tabelas > Comercial > Fiscais > Parâmetros por Estado](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f009ppe.htm#F009PPE_cprtnp)
* [Tabelas > Comercial > Fiscais > Mensagens NF](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f024msg.htm)
* [Tabelas > Transações > Cadastro > Compras > Ordem Compra/NF Entrada/Faturas](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f001tcp.htm#F001TCP_DEcprms11)
* [F461GNC](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f461gnc.htm)
