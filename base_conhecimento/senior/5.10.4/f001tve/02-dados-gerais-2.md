# Dados Gerais 2

> **Fonte:** F001TVE - Transações de Vendas — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f001tve.htm  
> **Trilha:** Ajuda por telas > Cadastros > Transações > Parâmetros por Gestão  
> **Telas citadas:** E140LNP, E140NFV, F001TVE, F051DIS, F070EMP, F070FVE, F080ISV, F113COA, F115CAR, F115NPF, F140PRE, F149GNA, F149GNC, F210EMA  
> **Identificadores de regras:** GER-000RTCMP01, VEN-120EXTCR01, VEN-120PCTIT01, VEN-120PTITM01

---
Gerar NF Entrada ao Fechar Pedido

Indicativo de geração de nota fiscal de entrada ao fechar o pedido.

Nota Herda Rateio Origem

Indicativo se a nota fiscal deve herdar o rateio definido no processo que lhe deu origem origem.

Operação Venda

Tipo da operação de venda, C - Cobrança, R - Remessa ou N - Normal.

* ao utilizar o indicativo C (cobrança), na geração de notas de cobrança via
  pedido, a nota gerada será gravada no respectivo  
  pedido desde que o processo seja efetuado pela tela de preparação de notas
  fiscais (F140PRE) com a opção não atualizar pedido marcada.
* ao utilizar o indicativo R (remessa), na geração de notas fiscais utilizando
  as telas de expedição via carga (F115CAR),  expedição via carga (F115NPF),
  faturamento individual (F149GNC), faturamento agrupado (F149GNA), será efetuado
  um tratamento para alterar o tipo da nota para 4 (remessa outros) e será gerado
  um relacionamento com a nota de cobrança (tabela E140LNP).
* nesses casos a transação também deve ser parametrizada para não somar
  financeiro, evitando a geração de mais uma cobrança.

Canc. ou Reabilita Pedido com Títulos Movimentados

Indicativo se será permitido cancelar ou reabilitar pedidos com títulos
movimentados.  
Os seguintes Identificadores de Regra atuam na Rotina quando o Parâmetro Canc. ou Reabilita Pedido com Títulos Movimentados estiver ativo: VEN-120PTITM01, VEN-120EXTCR01 e VEN-120PCTIT01. Para saber mais, acesse a documentação respectiva de cada identificador de regra.

Tributa CIDE

Indicativo se a transação tributa CIDE.

Natureza da Operação do serviço

Natureza de operação do serviço.

Número do Processo de Suspensão

Indica o número do Processo de Suspensão da exigibilidade de ISS (por decisão judicial ou por processo administrativo).

Observação

Para que essa informação seja enviada ao eDocs, é utilizada uma transação de venda específica que tenha o campo Nat. Operação Serviço parametrizado com 5 - Exigibilidade suspensa por decisão judicial ou 6 - Exigibilidade suspensa por procedimento administrativo. A partir disso, o que for informado no campo NumPsu (se preenchido) será enviado na tag InfSenior > Transacao na geração do XML.

NF Exige Nota Entrada

Indicativo se a nota
fiscal de saída gerada deve exigir uma nota fiscal de entrada. Quando este
parâmetro estiver definido como S-sim, o sistema não permite gerar uma nota
fiscal sem que o usuário informe um número de nota fiscal de entrada válido. Caso o usuário
tente processar uma nota fiscal de saída de saída sem informar a nota fiscal de
entrada será exibida uma mensagem: Transação de produto (nnn) exige Nota Entrada ou
Transação de serviço (nnn) exige Nota Entrada e abortado o processo.

Ret. Automático Comp. Industrialização

Indicativo se os componentes de industrialização são inseridos na mesma nota
fiscal de saída.

Obrigar Cód.Produto/Serviço

Este campo tem a finalidade de obrigar ou não o preenchimento do código
do produto/serviço ao incluir uma nota fiscal de venda. A consistência
ocorre no fechamento da nota fiscal.

Obrigar ligação família/produto/serviço X transação

Indicativo se a transação obriga a ligação de família e/ou produto e/ou serviço com a transação.

Pedido aceita lote vencido

Indica se em pedidos com itens de produtos controlados por lote será
possível informar lotes vencidos. Na geração de pedidos, quando este parâmetro estiver definido como Sim, será possível informar um lote vencido para o produto na grade da tela, como também na distribuição de lotes.

Intermediação de Serviços

Apenas para o Varejo Senior: Este campo indica se a transação é referente a intermediação de serviços, ele está ligado aos campos Realiza Intermediação de Serviços, da tela
F070EMP e à tela
F080ISV.

Indicativo presencial   
Indicador de presença do comprador no estabelecimento comercial no momento da operação.  
As opções de preenchimento são: 0 - Não se aplica; 1 - Operação presencial; 2 - Operação não presencial, pela Internet; 3 - Operação não presencial, Teleatendimento; 4 - NFC-e em operação com entrega a domicílio; 5 - Operação presencial, fora do estabelecimento e 9 - Operação não presencial, outros.

Observação

A opção **5 - Operação presencial, fora do estabelecimento** está disponível a partir da versão 4.0 da Nota Fiscal Eletrônica. Ao utilizar esta opção é necessário que exista uma nota fiscal referenciada.

A sugestão automática para as operações de pedido e notas fiscais de saída seguirá o critério abaixo:

1. Utilizar o indicativo presencial informado nas definições do cliente;
2. Se não encontrar nas definições do cliente, irá buscar da transação de produto ou serviço (F001TVE);
3. Se não encontrar nas definições do cliente e nas transações, será
   utilizado o indicativo presencial da filial (F070FVE);
4. Se não encontrar valor na sugestão automática, o indicativo deve ser informado manualmente.

Tipo Cálculo Devolução

Define o tipo de cálculo que será obedecido ao efetuar uma devolução. Ao incluir um novo registro, seu valor padrão será D - Devolução Proporcional. Possui as seguintes opções:

* D - Devolução Proporcional

  Ao gerar uma nota fiscal de devolução parcial, seus os valores (frete, seguro, acréscimo financeiro, base ICMS, base IPI, etc) são recalculados proporcionalmente de acordo com a nota fiscal de origem da devolução, considerando a quantidade que está sendo devolvida, em relação à quantidade da nota fiscal de entrada de origem. Esta rotina não aceita parametrização dos identificadores de regras.

Importante

Ao utilizar a opção “P - Cálculo Proporcionalˮ , o sistema herdará os campos da Nota Fiscal de Origem para Notas do Tipo “2 - NF de Devolução“ e “5 - NF de Retornoˮ. Caso não seja necessária a herança de algum campo, pode ser considerado o uso dos Identificadores de Regras GER-000RTCMP01 ou GER-000CPYCMP1.

* R- Recálculo de Valores

  Ao gerar uma devolução, os valores são recalculados sem considerar a nota fiscal de entrada de origem. Nesta rotina as parametrizações feitas manualmente ou através de identificadores de regras são consideradas.

Importante

Se o preenchimento do campo for P - Cálculo Proporcional, a transação de entrada utilizada na compra deverá estar parametrizada conforme o leiaute pré-definido da composição do valor líquido. Veja detalhes do preenchimento dos campos aqui.

Código do Dispositivo Fiscal

Código do dispositivo cadastrado na tela F051DIS.

Zerar Valor Contábil/Mercadoria

Indica se o valor Contábil/Mercadoria das notas fiscais de simples faturamento serão zerados na integração para tributos. Esta parametrização atende o inciso I do § 3º do artigo 129 do RICMS, dispõe que a nota de simples faturamento deve ser escriturada com data e número, sem valor contábil e sem valor de ICMS para o estado de São Paulo.

Exporta Siscoserv

Indica se a informação será exportada para o Siscoserv. Quando o contrato ou pedido for do tipo Siscoserv esse documento será integrado para o módulo Siscoserv e não será integrado para gestão de tributos.

Integra WMW

Indica se esse registro deve ser integrado para o WMW.

Calcula Funrural

Indicativo de cálculo de funrural.

Obrigar Cód.Produto/Serviço

Esse campo tem a finalidade de obrigar ou não o preenchimento do código
do produto/serviço ao incluir uma nota fiscal de venda. A consistência
ocorre no fechamento da nota fiscal.

Movimento no Saldo do Produtor   
Indica se Transação soma ou subtrai do Saldo do produtor rural.

Código Operação   
Código do tipo de operação do agronegócio, cadastrado na tela F113COA.

Emissão em Regime Especial

Indica se o sistema deve exportar, no SPED Fiscal, como nota fiscal emitida por regime especial ou norma específica. Quando "S - Sim", as notas fiscais com esta transação serão exportadas no SPED Fiscal conforme previsto no Guia Prático (Registro C100, exceção 4). Afeta a geração dos Registros C100, C170 e C190.

Nota fiscal devolução de valor

Indica se a transação da nota fiscal de saída trata-se de uma devolução apenas de valor.

Observação

* Não é feita uma validação referente ao valor devolvido para mais de uma nota de devolução na mesma compra;
* A transação de estoque vinculada à transação de venda marcada para devolução por valor deve ter a Forma Valorização Movimento como "M - pelo Movimento".

Utiliza Sigilo Fiscal NF-e Ref.

Indicativo se a nota fiscal de saída gerará o XML utilizando tag <refNFeSig> referente ao sigilo de notas fiscais referenciadas.  
As opções de preenchimento são: "S - Sim" para gerar o XML com a tag <refNFeSig>, e "N - Não" para gerar o XML com a tag <refNFe>. Sendo a opção "N - Não", o valor padrão.

**Tipo de lançamento para LCDPR**

Este campo permite informar o tipo de lançamento para LCDPR em transações de vendas. Há quatro opções disponíveis para seleção, sendo elas:

* 0 - Nenhum
* 1 - Receita da atividade rural
* 2 - Despesas de custeio e investimentos
* 3 - Produtos entregues no ano referente a adiantamentos de recursos financeiros.

Part. Est. Mín. Automatizado

Indica se a transação de venda participa da análise de estoque mínimo automatizado.

**Importante**

Para saber mais sobre a Análise de Estoque Mínimo Automatizado acesse a documentação da tela de Cadastro de Estoque Mínimo Automatizado (F210EMA).

Soma para Total da Nota

Indicativo que tem a finalidade de somar o valor líquido do item de produto no valor líquido total da nota (campos: E140NFV.VlrLpr --> total líquido dos itens de produto da nota fiscal de saída e E140NFV.VlrLiq --> total líquido da nota fiscal de saída). Este campo pode ser definido com "N - Não" em transações normalmente de bonificação que não impactam no valor total da nota fiscal gerada e é considerada apenas para cálculo de itens de produto. Define também o valor da tag <indTot> do item de produto na geração do XML da nota emitida conforme o seguinte:

* Soma para Total da Nota = "N - Não": tag <indTot> = "0";
* Soma para Total da Nota = "S - Sim" ou " ": tag <indTot> = "1".

Estorno de Crédito da CBS/IBS

Indica se a transação é utilizada para estorno de crédito da CBS/IBS.

Operação de Doação

Indica se a transação é uma operação de doação. Este parâmetro indica a geração da tag <indDoacao> nos documentos eletrônicos.

## Páginas relacionadas

* [VEN-120PTITM01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_120ptitm01.htm)
* [VEN-120EXTCR01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_120extcr01.htm)
* [VEN-120PCTIT01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_120pctit01.htm)
* [F070EMP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070emp.htm)
* [F080ISV](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f080isv.htm)
* [F070FVE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070fve.htm)
* [GER-000RTCMP01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ger_000rtcmp01.htm)
* [GER-000CPYCMP1](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ger_000cpycmp1.htm)
* [aqui](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/devolucao_proporcional.htm)
* [F051DIS](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f051dis.htm)
* [F113COA](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f113coa.htm)
* [Registros C100, C170 e C190](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/sped/fiscal-icms-ipi/bloco-c.htm#C170)
* [F210EMA](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f210ema.htm)
