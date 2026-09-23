# Cadastro de empresas (F070EMP)

> **Fonte:** F000PPD -  Configuração de parâmetros dinâmicos — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000ppd.htm#cademp  
> **Trilha:** Ajuda por telas > Cadastros  
> **Telas citadas:** E045PLA, E113ACR, E900COP, F001TPA, F001TRE, F021MOT, F070EMP, F070ONF, F070PDV, F075GFP, F075PRO, F113REM, F135AEA, F135APM, F301ATL, F410QCP, F420OSC, F435CCC, F435MDT, F501ATL, F900RCP  
> **Identificadores de regras:** GER-000BLQPE01, VEN-135EUDLE02

---
#### AGR.FILIAL.PADRAO.INTEGRACOES

Tem como objetivo definir a filial padrão a ser utilizada nas integrações do Agronegócio Senior.

Valor **Padrão**: 0.

#### AGR.FIX.BAIXAADIANTAMENTOCP

Importante

Este parâmetro deve ser cadastrado previamente pela tela Transações de Contas a Pagar (F001TPA).

Indica o código de transação utilizado para fazer a baixa por adiantamento do contas a pagar da fixação.

Padrão: 90560 - Sugestão de Código

Transação: Baixa de Título por Adiantamento no Contas a Pagar da Fixação - Sugestão para a Descrição da Transação

Adiciona ou Subtrai: 0

Tipo de Baixa: CR

#### AGR.FIX.BAIXACANCELAMENTOCP

Importante

Este parâmetro deve ser cadastrado previamente pela tela Transações de Contas a Pagar (F001TPA).

Indica o código de transação utilizado para fazer a baixa por cancelamento do Contas a Pagar utilizado na criação do título da fixação.

Padrão: 90360 - Sugestão de Código

Transação: Baixa de Título por Cancelamento no Contas a Pagar - Sugestão para a Descrição da Transação

Adiciona ou Subtrai: 3

Tipo de Baixa: CA

#### AGR.FIX.BAIXACANCELAMENTOCR

Importante

Este parâmetro deve ser cadastrado previamente pela tela Transações de Contas a Receber (F001TRE).

Indica o código de transação utilizado para fazer a baixa por cancelamento do Contas a Receber (antecipação) do título da fixação.

Padrão: 90360 - Sugestão de Código

Transação: Baixa de Título por Cancelamento no Contas a Receber - Sugestão para a Descrição da Transação

Adiciona ou Subtrai: 4

Tipo de Baixa: CA

#### AGR.HABILITAR.TRANSGENIA.PRODUTOS.SEM.INFORMACAO.ROYALTY

Define se o sistema deve habilitar o campo Variedade da tela F435CCC sem a necessidade de informação de royalty.

Valor Padrão: "N - Não".

#### AGR.IMPOSTOPORPRODUTO.IGNORARDIFVLRIMPORTACAONOTA

Esse parâmetro permite que a importação do XML da nota seja realizada quando houver na nota cálculo de Impostos por Produto Agro.

Valor **Padrão**: S - Ignorar a diferença causada pelos impostos e não mostrar a mensagem de divergência de valores na tela de parâmetros dinâmicos por filial.

#### AGR.INTEGRACAOHUBROYALTIES.HABILITAR

Indica se deve habilitar a integração com o Hub de Royalties.

Valor **Padrão**: "N - Não".

#### AGR.LIMITE.LOTE.INTEGRACOES

Define a quantidade limite de registros que serão enviados dentro de um lote de informações, para as integrações realizadas através do Processo Automático 151 - Integração ERP x Agronegócio Senior - Envio e Processo Automático 157 - Integração ERP x Gestão Safra.

Valor **Padrão**: 50 registros.

Valor **Mínimo**: 25 registros.

Valor **Máximo**: 200 registros.

#### AGR.SITUACAO.CAN.NOTA.PESAGEM

Definir a situação do ticket de pesagem após o cancelamento da nota fiscal gerada por ele.
Esse comportamento ocorre se uma única nota fiscal foi gerada pela pesagem.
Se parametrizado como 1, será perguntado ao usuário se deseja reabilitar a pesagem.

| Valor (Lista) | Descrição |
| --- | --- |
| 1 | Aberto/digitado |
| 2 | Fechado |
| 3 | Cancelado |
| 5 | Ticket fechado e aguardando novo faturamento. |

#### AGR.TRANSGENIA.FAT.AGR.TICKET

Este parâmetro irá definir se a empresa consiste ou não transgenias diferentes no faturamento de ticket de pesagens agrupadas pela tela F435MDT.

Valor **Padrão**: P - Permite.

#### AGRO.SISDEV.HASH

Define o Hash da filial para exportação de registros para o SisDev - Sistema de Defesa Vegetal.   
O número informado para o parâmetro, no formato String de 70 posições, será enviado ao e-mail da revenda que foi informada junto ao Instituto de Defesa e Agropecuária de Mato Grosso (INDEA).

Valor **Padrão**: vazio.

#### ASSISTENCIA.MOTIVOPADRAO.DEVOLUCAO

Define o motivo padrão que a assistência irá utilizar para a devolução. O número informado para o parâmetro, no formato inteiro, deve ser de acordo com o motivo desejado cadastrado em Cadastros > Identificadores e parâmetros > Motivo de situações/observações (F021MOT). Por exemplo: 0, 1, 2, 3, 4.

Valor **Padrão**: vazio.

#### ASSISTENCIA.MOTIVOPADRAO.TROCA

Define o motivo padrão que a assistência irá utilizar para a troca. O número informado para o parâmetro, no formato inteiro, deve ser de acordo com o motivo desejado cadastrado em Cadastros > Identificadores e parâmetros > Motivo de situações/observações (F021MOT). Por exemplo: 1, 2, 3, 4.

Valor **Padrão**: vazio.

#### BLOCOXPAF.HABILITA.DESABILITA

Responsável por habilitar/desabilitar a funcionalidade do Bloco X no Gestão de Lojas. Quando o valor for alterado, será necessário reiniciar o Integrador-Retaguarda.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Desabilitado (valor **Padrão**) |
| 1 | Habilitado |

#### BLOCOXPAF.HABILITA.DESABILITA.ESTOQUE

Responsável por permitir gerar ou não o arquivo de estoque do Bloco X no Gestão de Lojas. Será obrigatório o cadastro do parâmetro somente se desejar desativar o envio do Bloco X estoque.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Desabilitado |
| 1 | Habilitado (valor **Padrão**) |

Observação

O parâmetro BLOCOXPAF.HABILITA.DESABILITA.ESTOQUE somente terá vigência se o parâmetro BLOCOXPAF.HABILITA.DESABILITA estiver habilitado com o valor **1**.

#### CREDENCIAMENTOPAF.PORTA.CONSULTA

Indica a porta do servidor no qual terá o número de credenciamento consultado no sistema.

Valor **Padrão**: 9797.

#### CREDENCIAMENTOPAF.SERVER.CONSULTA

Indica o nome do servidor no qual terá o número de credenciamento consultado no sistema.

Valor **Padrão**: http://licenciamento.senior.com.br

#### EMPRESA.ATENDIMENTOPEDIDOS.SUGERILOTEPADRAO

Ao realizar o atendimento manual de pedidos via tela ou serviço, este parâmetro permite que logo após a execução de todos os identificadores de sugestão de lotes, caso não hajam lotes distribuídos, seja sugerido o lote padrão da origem.

**Rotinas envolvidas**

* Tela Atendimento Manual de Pedidos (Pré-fatura) (F135APM);
* Tela Atendimento Automático de Pedidos (Análise de Embarque) (F135AEA);
* Web service com.senior.g5.co.mcm.ven.manualpedidos, porta AtenderManualPedidos;
* Identificador de Regras: VEN-135EUDLE02.

| Valor (Lista) | Descrição |
| --- | --- |
| N | Não (valor **Padrão**) |
| S | Sim |

#### EMPRESA.COBRANCA.MENSAGEM1

Recurso para envio de mensagens personalizadas no header de lote (cabeçalho do arquivo), que serão consideradas em todos os títulos do lote. Para mais informações, acesse o item "3.2 Parametrizações da Cobrança Escritural" da página Van Bancária.

#### EMPRESA.COBRANCA.MENSAGEM2

Recurso para envio de mensagens personalizadas no header de lote (cabeçalho do arquivo), que serão consideradas em todos os títulos do lote. Para mais informações, acesse o item "3.2 Parametrizações da Cobrança Escritural" da página Van Bancária.

#### EMPRESA.CONTASPAGAR.OUTROSVALORESAPROVACAOMULTINIVEL

Indica se deve ser enviado para a aprovação multi-nível os títulos do contas a pagar que tiveram alterações em juros, multas, descontos e outros valores negociados, além de valor de desconto e valor de juros ao dia. Aplicável na tela Alteração de Títulos por Lote do Contas a Pagar (F501ATL).

| Valor | Descrição |
| --- | --- |
| 0 | Não (valor **Padrão**) |
| 1 | Sim |

#### EMPRESA.COTACAOAGRUPADA.PERMITIRREPOSICIONARCOLUNAS

Permite habilitar e desabilitar a manipulação das propriedades das colunas disponíveis na grade de Cotações, em Quadro Comparativo de Propostas de Cotações (F410QCP).

| Valor | Descrição |
| --- | --- |
| S | Sim |
| N | Não (valor **Padrão**) |

#### EMPRESA.ECD.REGISTROI050.NATUREZACONTADECUSTOCOMODESPESA

Permite gerar a natureza das contas de custo como despesa no registro I050 do SPED ECD. Seu valor padrão é **N-Não**.

O campo **03 - COD\_NAT** do registro é gerado com valor **04 - Contas de Resultado** quando **E045PLA.DefGru** é igual a **D, R ou X**. Com este parâmetro dinâmico ativo, o campo **também** receberá o valor 4 quando **E045PLA.DefGru** for igual a **M, N, V, C, S ou E**, ou seja, se houver uma conta com alguma dessas definições de grupo, ela será exportada no registro I050 com o campo **03 - COD\_NAT** igual a 04 em vez de **09**, como ocorre normalmente.

#### EMPRESA.FINANCEIRO.PREFIXOTITULOSUBSTITUTO

Permite alterar o prefixo do número do título substituto do contas a receber. Será considerado apenas os 3 primeiros caracteres informados para a composição do número do título.

Caso o número de dígitos do número da nota fiscal ocupar 6 dígitos e tamanho do sufixo ocupar 4, o tamanho máximo do parâmetro deverá ser de 2 dígitos, para garantir o range de 99 parcelas.

Valor **Padrão**: SCT.

#### EMPRESA.GESTORSENIOR.EXIBIRTRANSACAOCABECALHO

Indica se deve ser exibida, na mensagem enviada ao Gestor Senior, a transação do cabeçalho do documento.

Valor Padrão: Não.

#### EMPRESA.GESTORSENIOR.EXIBIRVALORBRUTOVALORMOEDA

Indica se deve ser exibido, na mensagem enviada ao Gestor Senior, Valor Bruto e Valor na Moeda para Ordens de Compra.

Valor Padrão: 1.

#### EMPRESA.GESTORSENIOR.FORMAEXIBIRRATEIO

Indica o formato de Exibição dos Rateios dos documentos no aplicativo Gestor Senior. As opções disponíveis são:

1. Agrupar as Contas e Centros de Custo por Documento.
2. Deixar todas abertas as linhas de rateio por Documento e por Item.
3. Agrupar as Contas e Centros de Custo por Documento e/ou por Item.
4. Agrupar por Documento e/ou por Item (3) suprimindo as linhas que sejam iguais ao rateio pré-definido na conta financeira.
5. Não exibir rateios.

Valor Padrão: 1.

Maiores detalhes sobre estas opções estão em Parâmetro dinâmico EMPRESA.GESTORSENIOR.FORMAEXIBIRRATEIO.

#### EMPRESA.GS.CAMPODESCRICAOFISCAL

O objetivo deste parâmetro é enviar as informações do Cadastro de Produto (F075PRO) - de acordo o valor que foi selecionado neste parâmetro - para o campo DESFIS, encontrado no retorno do web service Com.senior.g5.co.int.gs.produtogs, porta Exportar.

## Campos disponíveis para seleção:

Valor **Padrão**: DESFIS (campo que representa a descrição fiscal do item para o Gestão de Supermercados).

| Valor (Numérico) | Descrição |
| --- | --- |
| 0 | Não |
| 1 | Sim (valor **Padrão**) |

Valor: DESNFV (descrição para nota fiscal).

| Valor (Numérico) | Descrição |
| --- | --- |
| 0 | Não (valor **Padrão**) |
| 1 | Sim |

Valor: DESPRO (descrição do produto).

| Valor (Numérico) | Descrição |
| --- | --- |
| 0 | Não (valor **Padrão**) |
| 1 | Sim |

Valor: DESDER (descrição da derivação).

| Valor (Numérico) | Descrição |
| --- | --- |
| 0 | Não (valor **Padrão**) |
| 1 | Sim |

### Exemplo:

1. Caso o valor selecionado seja o **DESNFV**, no retorno do web service, no campo **DESFIS**, será apresentado o valor do campo Descrição da Nota Fiscal, preenchido na tela de Cadastro de Produtos.
2. Caso o valor selecionado seja o **DESPRO**, no retorno do web service, no campo **DESFIS**, será apresentado o valor do campo Descrição do Produto, também preenchido na tela de Cadastro de Produtos.
3. Funcionará desta forma para todos os valores selecionáveis.

#### EMPRESA.INTWMS.FATORCONVERSAODIMENSAOPRODUTO

Indica o fator de conversão das dimensões (altura/largura/comprimento) do produto/derivação. Este fator sempre será multiplicado pela dimensão do produto. Para integração com Gestão de Armazenagem | WMS​ Senior, normalmente o valor é 10 (cm para mm). Para Alcis, o valor é 1.

Valor **Padrão**: 1

#### EMPRESA.INTWMS.FATORCONVERSAOPESOPRODUTO

Indica o fator de conversão de peso para produto. Este fator sempre será multiplicado pelo peso do produto. Para integração com Gestão de Armazenagem | WMS​ Senior, normalmente o valor é 1000 (kg para gr). Para Alcis, o valor é 1.

Valor **Padrão**: 1

#### EMPRESA.INTWMS.INTEGRARDADOSAUTORIZACAOSEFAZWIS

Indica se na integração, enviará os campos Protocolo e Chave eletrônica para o WMS WIS.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não (valor **Padrão**) |
| 1 | Sim |

#### EMPRESA.INTWMS.TRANSFEREESTOQUEPRODUCAOEXTERNA

Este parâmetro indica se, ao retornar da separação do WMS, uma separação oriunda de abastecimento de produção para produção externa, o estoque deve ser transferido para um depósito que não integra com WMS e se a remessa deve ser gerada a partir desse depósito.

Sendo o valor desse parâmetro = S, ao gerar a solicitação de separação na tela F900RCP, é obrigatória a informação de um depósito destino para que ao retornar seja feita a transferências.

**Valor
padrão**: = N

#### EMPRESA.LIMITATAMANHOCADASTRAMENTOIMAGEMEMKB

Controla o tamanho máximo do arquivo de imagem ao cadastrar.

| Valor (Inteiro) | Descrição |
| --- | --- |
| 0 | Não (valor **Padrão**) |
| Maior que 0 | Sim |

Importante

Quando existir a necessidade de controlar o tamanho do arquivo de imagem, deverá ser informado um valor em KB. Por exemplo 1000 KB é igual a 1 MB; ou 2500 KB é igual a 2,5 MB.

#### EMPRESA.OCVIASOLICITACAO.ORDENACAO.PREVISAOENTREGA

Indica o campo de **Prazo de Entrega do Produto** na ordenação utilizada para a geração das Ordens de Compra via Solicitação (F420OSC). Quando for ativado, consideraremos o Prazo de Entrega para ordenação e geração dos itens. Essa ordenação vem depois do Código de Produto e Código da Derivação / Código do Serviço.

Valor **Padrão**: N - Não

#### EMPRESA.PAGAMENTOELETRONICO.QUEBRAO.Código do portador

Define se o segmento **O** terá a quebra definida conforme a seguinte regra: sempre que for encontrado um código de barras onde o segundo caractere for "5", será gerado um novo header.

Os valores são "S - Sim" ou "N - Não". Exemplo:

* Chave: EMPRESA.PAGAMENTOELETRONICO.QUEBRAO.BB01 Valor 'S'.

#### EMPRESA.PERMITEAPLICARPORTADORMULTIPLOS

Indica se na tela F301ATL será permitido utilizar a opção "Aplicar" para o campo Novo Portador.

| Valor (Numérico) | Descrição |
| --- | --- |
| 0 | Não (valor **Padrão**) |
| 1 | Sim |

#### EMPRESA.PGTOELETRONICO.CODIGO.INSTRUCAO.BANCO.237

Ao gerar a remessa de pagamento eletrônico usando a integração com a VAN Bancária por meio do leiaute Remessa - Pgto Eletrônico - LPN (CNAB 240) (SAEX10001), o **código da instrução para movimento** dos segmentos J, O e N é gerado sempre com o valor fixo "00 - Inclusão de registro detalhe liberado".

No entanto, para o banco Bradesco (237) pode haver a necessidade de enviar outro valor nesse campo, conforme uma lista pré-determinada que há no manual de geração do arquivo. Para isso, você pode utilizar este parâmetro dinâmico vinculado ao cadastro da empresa. Seu valor será o código da instrução que precisa ser enviado.

#### EMPRESA.PRODUTO.EDITADESCRICAONF

Quando esse parâmetro for configurado com o valor **S**, permitirá a edição do campo Descrição p/ Nota fiscal para produtos do tipo "M - Montagem" (F075PRO/F075GFP), sendo o mesmo exportado como Descrição do Produto para o Retaguarda.

| Valor (Lista) | Descrição |
| --- | --- |
| N | Não (valor **Padrão**) |
| S | Sim |

#### EMPRESA.NAOCONSISTIRENVIOBOLETOCLIENTESEMEMAIL

Em uma execução via web service não consiste mensagem em tela se o cliente possui e-mail cadastrado, quando o identificador de regras GER-000BLQPE01 estiver ativo.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não (valor **Padrão**) |
| 1 | Sim |

#### EMPRESA.RECEITUARIOAGRONOMICO.APLICACAO.VALORMINIMO

Esse parâmetro dinâmico permite o controle de busca de valores máximos ou mínimos.

| Valor (Lista) | Descrição |
| --- | --- |
| S | Ao informar "S" o sistema seguirá o comportamento normal, ou seja, continuará buscando o valor mínimo. (valor **Padrão**) |
| N | Quando o valor do parâmetro for "N", o sistema buscará o valor máximo. |

#### EMPRESA.RECEITUARIOAGRONOMICO.CONSULTA.DATTRT

Indique como será feita a consulta do sequenciamento do ART, considerando a data de cadastro ou o número inicial da receita na tela Emissão de Receita (F113REM).

| Valor (Lista) | Descrição |
| --- | --- |
| N | Considera o número inicial da receita (E113ACR.RECINI) |
| S | Considera a data de cadastro do TRT (E113ACR.DATTRT) no filtro (valor **Padrão**) |

#### EMPRESA.REPLICARHISTORICOCLIENTEFILIAIS

Indica se na importação de clientes do Gestão Empresarial | ERP para o Retaguarda as informações do histórico do cliente devem ser replicadas para todas as filiais da empresa.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não (valor **Padrão**) |
| 1 | Sim |

#### EMPRESA.SEPARACAOOP.PERMITESEPARACAOOPNAOLIBERADA

Indica se na tela F900RCP pode listar Ordens de Produção não liberadas.

| Valor | Descrição |
| --- | --- |
| N | Não |
| S | Sim (valor **Padrão**) |

Caso o parâmetro esteja igual a **S**, os filtros aplicados são:

E900COP.SITORP IN ('L','A','E')  
Senao =  
E900COP.SITORP IN ('L','A')

#### EMPRESA.VAREJO.LIMITECARACTERESCOMBINACAOFISCAL

Define a quantidade limite de caracteres para a combinação fiscal do Varejo Senior.
Utilizado para validar o tamanho das combinações de código do produto + derivação ou código de barras livre.
Deve ser um valor numérico inteiro maior que 0, limitado ao tamanho máximo possível da combinação dos caracteres de código do produto + derivação ou código de barras livre.

Padrão: 14

#### EMPRESA.WS.CLIENTE.EXPORTARIMAGEM

Este parâmetro indica se o sistema deve exportar ou não a imagem de documentos no web service com.senior.g5.co.int.varejo.cliente, porta Exportar.

| Valor (Lista) | Descrição |
| --- | --- |
| N | Não |
| S | Sim (valor **Padrão**) |

#### EMPRESA.WS.IGNORARINATIVOAOVALIDARDUPLICIDADE

Indica quando um registro está sendo gravado através de web services. A validação de duplicidade irá desconsiderar os registros inativos.

| Valor (Lista) | Descrição |
| --- | --- |
| N | Não (valor **Padrão**) |
| S | Sim |

#### EMPRESA.WS.PRODUTO.EXPORTARIMAGEM

Este parâmetro indica se o sistema deve exportar ou não a imagem do produto no web service com.senior.g5.co.int.varejo.produto, porta Exportar.

| Valor (Lista) | Descrição |
| --- | --- |
| N | Não |
| S | Sim (valor **Padrão**) |

#### ENTIDADE.EXIBECODIGO

Indica se o sistema exibe o código da pessoa (cliente ou fornecedor).

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não (valor **Padrão**) |
| 1 | Sim |

#### ENTIDADE.EXIBEINFORMACOESDETALHADAS

Define se exibe as informações detalhadas da pessoa (cliente ou fornecedor) na consulta de clientes ou fornecedores.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não exibe (valor **Padrão**) |
| 1 | Exibe |

#### ENTIDADE.EXIBEINFORMACOESSPC

Define se devem ser exibidas no PDV as informações do SPC de um cliente quando o sistema exigir a confirmação dos dados (parâmetro dinâmico Entidade.ExigeConfirmacao configurado com o valor **1**).

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não exibe (valor **Padrão**) |
| 1 | Exibe |

#### ENTIDADE.EXIGECONFIRMACAO

Define se deve ser exigida uma confirmação dos dados da pessoa (cliente ou fornecedor) quando a pessoa for identificada através de código ou CPF/CNPJ.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não exige (valor **Padrão**) |
| 1 | Exige |

#### ENTIDADE.IDENTIFICACLIENTENOINICIOVENDA

Indica se o sistema solicita ao operador identificar o cliente/consumidor no início da venda.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não (valor **Padrão**) |
| 1 | Sim |

#### ENTIDADE.IDENTIFICACLIENTEOPERACAONAOFISCAL

Habilita a identificação de cliente/consumidor final nas operações não fiscais.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não (valor **Padrão**) |
| 1 | Sim |

#### ENTIDADE.IDENTIFICACONSUMIDORFINAL

Habilita recurso para identificar consumidor final na venda.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não (valor **Padrão**) |
| 1 | Sim |

#### ENTIDADE.IMPRIMECLIENTECUPOM

Define quais dados do cliente ou consumidor final serão impressos no cupom fiscal ou comprovante de recebimento não fiscal, considerando:

* 0 - Não imprime
* 1 - Imprime

| Código | Descrição | Valor Padrão |
| --- | --- | --- |
| 1 | CPF / CNPJ | 1 |
| 2 | Código | 1 |
| 3 | Nome | 1 |
| 4 | Logradouro | 1 |
| 5 | Número | 1 |
| 6 | Complemento | 1 |
| 7 | Bairro | 0 |
| 8 | Cidade | 1 |
| 9 | UF | 1 |
| 10 | CEP | 0 |
| 11 | Telefone | 0 |

Observação

Os campos serão impressos somente se existirem. Mesmo se habilitado, o complemento será impresso somente de existir complemento no endereço do cliente.

## Exemplo

Configuração:

1,1,1,1,1,1,0,1,1,0,0

* 1: CPF/CNPJ: sempre imprime
* 1: Código: nuca é impresso
* 1: Nome: sempre imprime
* 1: Logradouro: sempre imprime
* 1: Número: sempre imprime
* 1: Complemento: sempre imprime
* 0: Bairro: não imprime
* 1: Cidade: sempre imprime
* 1: Estado: sempre imprime
* 0: CEP: não imprime
* 0: Telefone: não imprime

#### ENTIDADE.INFORMACOESCONSUMIDORFINAL

Define quais informações serão solicitadas ou exigidas para identificação do consumidor final. É necessário o parâmetro dinâmico Entidade.IdentificaConsumidorFinal estar configurado com o valor **1**.

Importante

Após a atualização do PDV, é necessário ajustar esse parâmetro para **PDV PAF**, que passará a funcionar como o **PDV NFC-e**. Caso ele não seja ajustado, a obrigatoriedade será aplicada de forma inadequada.

Opções PDV PAF / PDV NFC-e:

* 0 - Não solicita informação;
* 1 - Solicita informação como opcional
* 2 - Obriga informação.

| Código | Descrição | Valor Padrão |
| --- | --- | --- |
| 1 | Origem | 2 |
| 2 | CPF/CNPJ ou NIF | 2 |
| 3 | Nome | 2 |
| 4 | RG | 1 |
| 5 | Inscrição Estadual | 1 |
| 6 | Inscrição Municipal | 1 |
| 7 | SUFRAMA | 1 |
| 8 | CEP | 2 |
| 9 | País | 2 |
| 10 | Estado | 2 |
| 11 | Cidade | 2 |
| 12 | Logradouro | 2 |
| 13 | Número | 2 |
| 14 | Complemento | 1 |
| 15 | Bairro | 2 |
| 16 | Telefone | 1 |

## Exemplo de configuração

Configuração:

2,2,2,1,1,2,2,2,2,2,2,1,2,1,1,1

* 2: Origem - Obrigatório
* 2: CPF/CNPJ/ou NIF - Obrigatório
* 2: Nome - Obrigatório
* 1: Inscrição Estadual - Opcional
* 1: Inscrição Municipal - Opcional
* 2: CEP - Obrigatório
* 2: Pais - Obrigatório
* 2: Estado - Obrigatório
* 2: Cidade - Obrigatório
* 2: Logradouro - Obrigatório
* 2: Número - Obrigatório
* 1: Complemento - Opcional
* 2: Bairro - Obrigatório
* 1: Telefone - Opcional
* 1: E-mail - Opcional
* 1: Observações - Opcional

#### ENTIDADE.LIMITATAMANHOINFOCLIENTECUPOM

Define se o sistema limita as informações do cliente/consumidor para impressão/registro no cupom fiscal.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não (valor **Padrão**) |
| 1 | Sim |

#### ENTIDADE.TIPOPESQUISA

Tipo de pesquisa do texto na consulta de entidade.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Contendo no texto (valor **Padrão**) |
| 1 | Pelo início do texto |

#### ENTREGA.ATUALIZA.TELA

Altera a forma de atualização da tela de Controle de Entrega. Com o parâmetro com o valor **0**, o comportamento do sistema se mantém da forma atual, onde o sistema, ao efetuar uma ação na tela de Controle de Entrega, refaz a consulta atualizando toda a tela. Com o parâmetro com o valor **1**, o sistema irá manter a tela no estado atual, atualizando apenas as informações da grade.

| Valor | Descrição |
| --- | --- |
| 0 | Desabilitado (valor **Padrão**) |
| 1 | Habilitado |

#### ENTREGA.EXIGETRANSPORTADORA

Impede a entrega de controles de entrega sem transportador que não seja por retirada no balcão.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não (valor **Padrão**) |
| 1 | Sim |

#### ENTREGA.FILIALTRANSPORTEPADRAO

Indica a filial padrão, no valor inteiro, que transportará a entrega (se o valor for igual a **0**, o campo filialtransporte será populado com o mesmo valor do campo filialentrega da tabela entrega).

Valor **Padrão**: 0.

#### ENTREGA.IMPRIMIRRELATORIOENTREGABALCAO

Indica se o relatório deve ou não ser impresso para retiradas no balcão.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não (valor **Padrão**) |
| 1 | Sim |

#### ENTREGA.PERMITEGERARREMESSA

Define se pode ser solicitado ao Gestão Empresarial | ERP a geração da Nota fiscal de Remessa na Entrega quando a filial que fará o transporte da mercadoria for diferente a da filial da entrega.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não permite (valor **Padrão**) |
| 1 | Permite |

#### ENTREGA.RESERVAESTOQUE

Define se a filial reserva estoque ao receber uma entrega.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não reserva (valor **Padrão**) |
| 1 | Reserva |

#### ENTREGA.RESERVAESTOQUE

Define se a filial reserva estoque ao receber uma entrega.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não reserva (valor **Padrão**) |
| 1 | Reserva |

#### ERP.EXP.NOTAENTRADA.SEMMOVESTOQUE

Indica se o sistema exportará notas fiscais de entrada que não movimentam estoque.

| Valor (Inteiro) | Descrição |
| --- | --- |
| 0 | Não exporta |
| 1 | Exporta |

#### ESTOQUE.BLOQUEIOOFFLINE

Define se será bloqueada a venda de produtos quando o PDV estiver off-line do sistema de retaguarda, em vendas feitas diretamente no PDV pelo fato que não ser possível consultar o estoque para produtos que não controlam estoque por série ou lote.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não bloqueia (valor **Padrão**) |
| 1 | Bloqueia |

#### ESTOQUE.BLOQUEIOSERIELOTEOFFLINE

Define se deve ser bloqueado a venda de produtos, vendidos por lote ou série, quando o PDV estiver off-line do sistema de retaguarda, em vendas feitas diretamente no PDV pelo fato que não ser possível consultar o estoque.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não bloqueia |
| 1 | Bloqueia (valor **Padrão**) |

#### ESTOQUE.EXIBESALDOESTOQUE

Define se o sistema exibe a quantidade em estoque do produto na tela de consulta de itens.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não exibe |
| 1 | Exibe (valor **Padrão**) |

#### ESTOQUE.VERIFICASALDONAVENDA

Define se será verificado estoque do produto na venda, quando vendido diretamente no PDV, considerando que:

* se for verificado e o produto não possuir estoque suficiente, a venda dele será bloqueada;
* somente para produtos que não controlam estoque por série ou lote.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não verificar (valor **Padrão**) |
| 1 | Verificar |

#### ESTOQUE.VERIFICASERIELOTENAVENDA

Define se será verificado estoque para produtos vendidos por lote ou série, e se o número de série ou lote é válido, quando vendido diretamente no PDV, considerando que:

* se for verificado e o produto não possuir estoque suficiente ou o número de série ou lote não existir, a venda do mesmo será bloqueada;
* para produtos que controlam estoque por série ou lote.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não verificar (valor **Padrão**) |
| 1 | Verificar |

#### FECHAMENTO.IMPRIMERELATORIOGERENCIAL

Define se deve ser emitido o relatório de fechamento de caixa.

| Valor | Descrição |
| --- | --- |
| 0 | Não imprime |
| 1 | Imprime uma via (valor **Padrão**) |

#### FECHAMENTO.QUANTIDADEVIASRELATORIOGERENCIAL

Define o número de vias, no formato inteiro, do relatório de fechamento de caixa.

Valor **Padrão**: 1

#### FECHAMENTO.SALDONEGATIVO

Define se deve permitir fechar caixa com saldo negativo.

| Valor | Descrição |
| --- | --- |
| 0 | Bloqueia (valor **Padrão**) |
| 1 | Permite gerando um suprimento para zerar o caixa antes |

#### FECHAMENTO.SALDOPOSITIVO

Define qual ação deve ser realizada no fechamento de caixa.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Realiza sangria total (valor **Padrão**) |
| 1 | Mantém saldo de caixa para o próximo movimento (abertura) |
| 2 | Realiza sangria e mantém fundo de troco para o próximo movimento (abertura) |

#### FISCAL.ENDERECOCALCULOIMPOSTO

Parametriza o Retaguarda sobre qual a UF será utilizada para calcular tributos e quais endereços de entrega estarão disponíveis para seleção, considerando que:

* Caso o parâmetro estiver configurado com o valor **0**, na tela do Retaguarda, em que é possível selecionar o endereço de entrega do pedido, só será exibido o endereço do cliente para seleção (endereço que possui sequência igual a **0**), mesmo que existam mais endereços de entrega registrados no cadastro do cliente, estes endereços não ficarão disponíveis para a seleção;
* Caso o parâmetro estiver configurado com o valor **1**, na tela do Retaguarda, em que é possível selecionar o endereço de entrega do pedido, serão exibidos apenas os endereços cadastrados como endereços de entrega no cadastro do cliente (endereços que possuem sequência maior que 0). O endereço padrão do cadastro do cliente (que possui sequência igual a 0) não será exibido para seleção;
* O parâmetro dinâmico FISCAL.ENDERECOCALCULOIMPOSTO funciona em conjunto com o parâmetro USAENTORI, do Gestão Empresarial | ERP. Para ter o comportamento correto, se no Gestão de Lojas o parâmetro estiver definido com **1**, será necessário que no Gestão Empresarial | ERP ele esteja definido como "S". Se estiver com **0** ou não configurado no Gestão de Lojas, é necessário que no ERP esteja com "N".

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Endereço do cliente (valor **Padrão**) |
| 1 | Endereço de entrega |

#### FISCAL.ENDERECO.CLIENTE.NOTA

Parametriza o Retaguarda para informar o endereço do cliente no bloco Destinatário da NF quando o parâmetro FISCAL.ENDERECOCALCULOIMPOSTO for igual a "1 - Entrega".

Valor Padrão: 0.

| Valor | Descrição |
| --- | --- |
| 0 | Não habilitado |
| 1 | Habilitado |

#### FRETE.HORARIOTRANSPORTE

Horário de início do transporte de mercadorias, no formato:

* Inteiro - Quando o parâmetro dinâmico Frete.TipoHorarioTransporte estiver configurado com o valor **0**: tempo em minutos para início do transporte após a venda;
* Hora - Quando o parâmetro dinâmico Frete.TipoHorarioTransporte estiver configurado com o valor **1**: horário que inicia o transporte das mercadorias; ou **3**: data de entrega informada no DAV . Por exemplo: 18:15;
* Não considerado quando o parâmetro dinâmico Frete.TipoHorarioTransporte estiver configurado com o valor **2**: espaço em branco para preenchimento manual.

Valor **Padrão**: 0.

#### FRETE.PLACAVEICULO

Placa do veículo, no formato texto, para transporte de mercadorias.

#### FRETE.TIPOHORARIOTRANSPORTE

Modo de registro da data e hora do transporte de mercadorias.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Tempo após venda: tempo em minutos para início do transporte após a venda (valor **Padrão**) |
| 1 | Horário fixo: horário que inicia o transporte das mercadorias |
| 2 | Manual: espaço em branco para preenchimento manual |
| 3 | Data de entrega: data de entrega informada no DAV |

#### GARANTIA.DANOSELETRICOS.GRUPOPRODUTO

Indica um grupo de produtos, no formato alfanumérico, que define quais os produtos que estarão sujeitos à cobertura de danos elétricos. É utilizado para a impressão do bilhete de garantia estendida.

#### GARANTIA.DANOSELETRICOS.PERCENTUALRATEIO

Indica o percentual de rateio, no formato inteiro, do valor da garantia estendida para a cobertura de danos elétricos. É utilizado para a impressão do bilhete de garantia estendida.

Valor **Padrão**: 15 (padrão atendido pela seguradora Assurant).

#### GARANTIAESTENDIDA.PERCENTUALIOF

Percentual de IOF, no formato numérico, cobrado na venda de garantia estendida.

Valor **Padrão**: 7,38

#### GARANTIAESTENDIDA.PRAZODEVOLUCAOINTEGRAL

Prazo em dias, no formato numérico, devolução integral do valor pago pela garantia estendida.

Valor **Padrão**: 7.

#### HORARIO.EXECUCAO.PROCESSO.ALTERACAO.PRECOS

Define o horário em que o processo que busca as alterações de preço irá ser executado.

Valor **Padrão**: 00:00 (esse valor será assumido pelo sistema, caso nenhum valor esteja cadastrado).

Importante

Caso o parâmetro seja utilizado com um horário definido, e não pelo padrão (00:00), após o parâmetro ser integrado do Gestão Empresarial | ERP para o Retaguarda, torna-se necessário reiniciar o serviço do IntegradorRetaguarda, pois é o mesmo que possui a *Thread* que executa o processo na loja. Este parâmetro é executado apenas uma vez ao dia. Caso o processo de agendamento já tenha sido executado, qualquer alteração realizada no mesmo dia só será executada no dia seguinte.

## Exemplo

No dia 01/01/2019, foi criado um agendamento para 00:00 do dia 02/01/2019. Durante o dia 01/01/2019, foi alterado o parâmetro para às 06:00, como esse parâmetro já havia sido agendado para 00:00 do dia 02/01/2019, a alteração será válida apenas para o dia 03/01/2019.

Caso haja necessidade de alterar a hora de um processo já agendado, é necessário reiniciar o IntegradorRetaguarda após alterar o parâmetro.

#### IMP.NFCE.MEGASUL.ATUALIZARRESERVAEXCLUSIVA

Indica se a importação de NFC-e atualiza a reserva exclusiva no estoque.

| Valor (Inteiro) | Descrição |
| --- | --- |
| 0 | Não |
| 1 | Sim (valor **Padrão**) |

#### MARGEMCONTRIBUICAO.TIPOCALCULOJUROS

Define qual será a forma de cálculo de juros na margem de contribuição.

| Valor (Inteiro) | Descrição |
| --- | --- |
| 0 | Sem Juros |
| 1 | Tabela Price (valor **Padrão**) |
| 2 | Juros Compostos |
| 3 | Juros Simples |

#### MONTAGEM.GERENCIARPELAMATRIZ

Define para quais tipos de pedido que as montagens serão gerenciadas pela matriz. Para as montagens destes pedidos, através do Gestão Empresarial | ERP será possível reagendar, finalizar, cancelar, entre outros.

| Valor (Inteiro) | Descrição |
| --- | --- |
| 0 | Apenas pedidos de entrega futura pelo CD |
| 1 | Qualquer tipo de pedido |

#### NFCE.PERMITEGERARNFE

Para o PDV NFC-e, caso o parâmetro esteja ativo, o PDV emitirá uma NF-e para pessoas jurídicas (PJ) e NFC-e para pessoas físicas (PF) na finalização de qualquer venda.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Desabilitado |
| 1 | Habilitado (valor **Padrão**) |

Observação

Para que esse parâmetro funcione corretamente, é necessário que o parâmetro **OPERACAONOTAFISCAL.VENDAPDV** esteja configurado.

#### NOTA.FISCAL.MANUAL.CFOP.PDV

A transação informada neste parâmetro, no formato inteiro, será utilizada para processar a Nota Fiscal Manual. Os cupons fiscais continuarão buscando a transação de vendas no cadastro da Filial.

Esta transação informada não deve possuir integração com o financeira.

Valor **Padrão**: 0.

#### NOTAFISCAL.XML.FORMADEPAGAMENTOPADRAO

A função deste parâmetro é definir qual forma de pagamento irá para o XML na geração de NF-e/NFC-e, caso a parcela não possua forma de pagamento definida.

Para o Gestão de Lojas, ao emitir uma NF-e/NFC-e no sistema, utilizando uma forma de pagamento não esperada pela SEFAZ, será enviado no XML a forma "99 - Outros". Desta forma, será feito o envio obrigatório de uma descrição desta forma de pagamento não esperada pela SEFAZ, e o Gestão de Lojas utilizará a descrição da forma de pagamento informada neste parâmetro dinâmico

## Exemplo:

Quando utilizada a forma de pagamento "Acerto" e neste parâmetro dinâmico informado o código "1" (Dinheiro), a SEFAZ não irá esperar a forma de pagamento "Acerto". Neste caso, o Gestão de Lojas enviará no XML da NF-e ou NFC-e a forma de pagamento "99 - Outros" na tag **tPag** com a descrição "Dinheiro" na tag **xPag**.

Valor **Padrão**: 1 - Dinheiro.

#### NOTAFISCAL.XML.HABILITARNT200606

Habilita as alterações implementadas no Gestão de Lojas para atender às exigências da Nota Técnica 2020.006.

| Valor | Descrição |
| --- | --- |
| N | Não |
| S | Sim (valor **Padrão**) |

#### NOTAFISCAL.GERADA.QTDMAXITENS

Define a quantidade máxima, no formato inteiro, de itens que serão incluídos em uma única nota fiscal ao gerar as Notas Fiscais de Entrada e/ou Saída no processo de finalização do Inventário.

Valor **Padrão**: 500, caso o parâmetro não esteja configurado ou contenha valor inválido.

#### NUMERO.CEI

Busca o valor do cadastro específico do INSS, no formato inteiro, e é utilizado por pessoas físicas equiparadas por lei a empresas.

Valor **Padrão**: vazio.

#### OBSBANCARIAS.BBBCCVV

O **Tipo de Cobrança** é requerido na integração com a VAN Bancária ao utilizar a cobrança escritural com o Banco do Brasil. Essa informação é disponibilizada pelo banco na abertura do contrato. Para enviá-la, configure o parâmetro dinâmico OBSBANCARIAS.BBBCCVV na tela F070EMP, botão **Parâmetros Dinâmicos**, onde:

* BBB = Código do banco
* CC = Código interno da carteira
* VV = Código da carteira no banco

Para mais informações, acesse o manual da Nexxera na documentação da VAN Bancária, campo NX31.

#### OPERACAONOTAFISCAL.TRANSFERENCIAENTREGA

Operação de nota fiscal, no formato inteiro, utilizada na emissão de notas fiscais de transferência no processo de entrega em outras filiais.

Valor **Padrão**: 0.

#### OPERACAONOTAFISCAL.VENDAPDV

Identifica qual operação de nota fiscal será utilizada ao fazer vendas do tipo NF-e no PDV, sendo aplicável somente ao PDV NFC-e. Seu funcionamento está condicionado à emissão de NF-e no PDV, rotina essa habilitada pelo parâmetro **NFCE.PERMITEGERARNFE**.

O valor cadastrado para esse parâmetro deve ser o Código da Operação indicado na tela Operações de nota fiscal (F070ONF), onde consta a série da nota de venda. Lembrando que a série da NFC-e **não pode** ser utilizada. Use a série da nota fiscal eletrônica de venda utilizada pelo cliente.

#### ORCAMENTO.DIAS.VALIDADE

Configura uma validade padrão para o orçamento. Permite indicar o valor sugerido para a quantidade de dias que o orçamento será válido.

Valor **Padrão**: 5

#### PAF.GERARREGISTROATO1704REDUCAOZ

Executa a geração dos arquivos Ato Cotepe 17/04 após a redução Z, independentemente do estado (UF).

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não (valor **Padrão**) |
| 1 | Sim |

#### PARCELA.POSTERGADATAVENCIMENTO

Indica se pode postergar, ou não, a data da parcela no pedido.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não permite |
| 1 | Permite (valor **Padrão**) |

#### PDV. ACAOSALDOEMCAIXAATINGIDO

Define a ação que o sistema vai realizar quando o saldo do caixa atingir o limite máximo.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Nenhuma ação (valor **Padrão**) |
| 1 | Exibe aviso para realizar sangria |
| 2 | Exibe aviso e exige que seja realizada sangria |

Importante

Esta ação é dependente das definições do parâmetro dinâmico PDV.LIMITESALDOEMCAIXA, e o mesmo ocorre ao contrário.

#### PDV.ACRESCIMOSUBTOTAL

Habilita acréscimo no subtotal.

| Valor | Descrição |
| --- | --- |
| 0 | Não |
| 1 | Sim (valor **Padrão**) |

#### PDV.AVISOFALTAITENS

Habilita a apresentação de uma mensagem informando sobre a falta de determinados itens (de serviço) na venda: garantia estendida e seguro parcela protegida.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não (valor **Padrão**) |
| 1 | Sim |

#### PDV.AVISOGARANTIAESTENDIDAPENDENTE

Habilita a apresentação de uma mensagem informando que o cliente possui garantia estendida pendente de outras vendas.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não (valor **Padrão**) |
| 1 | Sim |

#### PDV.DIASLOG

Define o tempo de armazenamento do log do sistema, em dias e no formato inteiro, sendo o mínimo 60 dias.

Valor **Padrão**: 60.

#### PDV.DIRETORIOAUTORIZACAOECF

Define o diretório do arquivo de autorização de ECFs, no formato texto.

#### PDV.ESPERAGAVETAFECHAR

Ao abrir gaveta pelo sistema, espera gaveta fechar para continuar o processo.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não (valor **Padrão**) |
| 1 | Sim |

#### PDV.EXIBEINFORMACAOCALCULOFINALIZADOR

Exibe detalhes do finalizador como: saldo restante e troco.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não |
| 1 | Sim (valor **Padrão**) |

#### PDV.EXIGECONFIRMACAOFINALIZADORES

Define se o sistema exige confirmação dos valores recebidos nas operações de venda e recebimento.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não (valor **Padrão**) |
| 1 | Sim |

#### PDV.FINALIZADORDINHEIROPADRAO

Define o finalizador que será utilizado como dinheiro padrão do sistema de PDV. Deve ser informado o código da forma de pagamento dinheiro, no formato inteiro.

#### PDV.FINALIZADORRAPIDOF1

Define o finalizador que será utilizado como finalizador rápido através da tecla de atalho `F1`. Deve ser informado o código da forma de pagamento, no formato inteiro.

#### PDV.FINALIZADORRAPIDOF2

Define o finalizador que será utilizado como finalizador rápido através da tecla de atalho `F2`. Deve ser informado o código da forma de pagamento, no formato inteiro.

#### PDV.FINALIZADORRAPIDOF3

Define o finalizador que será utilizado como finalizador rápido através da tecla de atalho `F3`. Deve ser informado o código da forma de pagamento, no formato inteiro. É necessário o parâmetro dinâmico Venda.SeguroParcelaProtegida estar configurado com o valor **0**.

#### PDV.FINALIZADORRAPIDOF4

Define o finalizador que será utilizado como finalizador rápido através da tecla de atalho `F4`. Deve ser informado o código da forma de pagamento, no formato inteiro. É necessário o parâmetro dinâmico Venda.GarantiaEstendida estar configurado com o valor **0**

#### PDV.FINALIZADORVALORZEROASSUMESALDO

Assume saldo ao confirmar finalizador com valor zero.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não |
| 1 | Sim (valor **Padrão**) |

#### PDV.LIMITESALDOEMCAIXA

Define o valor máximo,no formato moeda, que poderá ter no caixa. Caso seja informado algum valor, o sistema irá informar ao usuário para fazer sangria quando o saldo do caixa atingir este valor.

Valor **Padrão**: 0 (sem limite).

Importante

Esta ação é dependente do parâmetro dinâmico PDV. ACAOSALDOEMCAIXAATINGIDO, e o mesmo ocorre ao contrário e vice-versa.

#### PDV.MINIMOCARACTERESPESQUISA

Define o número mínimo de caracteres, no formato inteiro, para pesquisar.

Valor **Padrão**: 3.

#### PDV.NUMEROPRODUTOSPROMPT

Define a quantidade de produtos listados em consulta, no formato inteiro.

Valor **Padrão**: 50.

#### PDV.TECLARENTERVISOR

Define se exige `Enter` após escolher uma opção em uma lista no visor.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não (valor **Padrão**) |
| 1 | Sim |

#### PDV.TIPOCALCULODESCONTOACRESCIMOFINALIZADOR

Indica qual o tipo de cálculo que será utilizado para atribuir desconto e/ou acréscimo nas formas de pagamento.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Sobre o valor da forma de pagamento (exemplos 1, 2 e 3) (valor **Padrão**) |
| 1 | Sobre a representação financeira do valor. Esta opção quita o recebimento na venda, quando faltar menos que 5 centavos (exemplos 4, 5, 6 e 7) |

## Exemplo

##### Exemplo 1

* Desconto atribuído sobre o valor do finalizador - quitar o saldo
* Percentual de desconto configurado para o finalizador: 10%

|  |  |
| --- | --- |
| Saldo a receber: | 1.000,00 |
| Acréscimo: | 100,00 |
| Dinheiro: | 900,00 |
| Saldo a receber: | 0,00 |

##### Exemplo 2

* Desconto sobre o valor informado para o finalizador, para quitar parte do saldo da operação
* Percentual de desconto configurado para o finalizador: 10%

|  |  |
| --- | --- |
| Saldo a receber: | 1.000,00 |
| Acréscimo: | 700,00 |
| Dinheiro: | 70,00 |
| Saldo a receber: | 230,00 |

##### Exemplo 3

* Desconto sobre o valor informado para o finalizador, para quitar o saldo da operação com troco
* Percentual de desconto configurado para o finalizador: 10%

|  |  |
| --- | --- |
| Saldo a receber: | 1.000,00 |
| Acréscimo: | 100,00 |
| Dinheiro: | 1.000,00 |
| Saldo a receber: | 0,00 |

##### Exemplo 4

* Desconto conforme a representação financeira do valor, considerando quitar o saldo da operação
* Percentual de desconto configurado para o finalizador: 10%

Cálculo:

VALOR\_A\_SUGERIR = VALOR\_SALDO x (1 – (PERCENTUAL\_DESCONTO / 100))  
VALOR\_A\_SUGERIR = 1000,00 x (1 - (10 / 100))  
VALOR\_A\_SUGERIR = 1000,00 x 0,9  
VALOR\_A\_SUGERIR = 900,00

ACRÉSCIMO = 1000,00 - 900,00  
ACRÉSCIMO = 100,00

Valores calculados/exibidos:

|  |  |
| --- | --- |
| Saldo a receber: | 1000,00 |
| Acréscimo: | 100,00 |
| Dinheiro: | 900,00 |
| Saldo a receber: | 0,00 |

##### Exemplo 5

* Desconto conforme a representação financeira do valor, para quitar parte do saldo da operação
* Percentual de desconto configurado para o finalizador: 10%
* Valor da operação: 1000,00
* Valor informado para recebimento parcial: 300,00

Cálculo:

VALOR\_INFORMADO = VALOR\_A\_ABATER x (1 – (PERCENTUAL\_DESCONTO / 100))  
300,00 = VALOR\_A\_ABATER x (1 - (10 / 100))  
300,00 = VALOR\_A\_ABATER x 0,90  
VALOR\_A\_ABATER = 300,00 / 0,90  
VALOR\_A\_ABATER: 333,33

DESCONTO = VALOR\_A\_ABATER – VALOR\_INFORMADO  
DESCONTO = 333,33 - 300,00  
DESCONTO = 33,33

Valores calculados/exibidos:

|  |  |
| --- | --- |
| Saldo a receber: | 1.000,00 |
| Acréscimo: | 300,00 |
| Dinheiro: | 33,33 |
| Saldo a receber: | 666,67 |

##### Exemplo 6

Desconto conforme a representação financeira do valor, considerando quitar o saldo da operação, com troco.

Valores calculados/exibidos:

|  |  |
| --- | --- |
| Saldo a receber: | 1.000,00 |
| Acréscimo: | 100,00 |
| Dinheiro: | 1.000,00 |
| Saldo a receber: | 0,00 |
| Troco: | 100,00 |

##### Exemplo 7

Desconto conforme a representação financeira do valor, quitando o saldo em vários recebimentos.

|  |  |
| --- | --- |
| Saldo a receber: | 1.000,00 |
| Dinheiro | 100,00 |
| Desconto: | 11,11 |

|  |  |
| --- | --- |
| Saldo a receber: | 888,89 |
| Dinheiro | 100,00 |
| Desconto: | 11,11 |

|  |  |
| --- | --- |
| Saldo a receber: | 777,78 |
| Dinheiro | 400,00 |
| Desconto: | 44,44 |

|  |  |
| --- | --- |
| Saldo a receber: | 333,34 |
| Dinheiro | 200,00 |
| Desconto: | 22,22 |

|  |  |
| --- | --- |
| Saldo a receber: | 111,12 |
| Dinheiro | 100,00 |
| Desconto: | 11,12 |

|  |  |
| --- | --- |
| Saldo a receber: | 0,00 |

#### PDV.TIPOLEITURASENHA

Define o modo de leitura da senha de acesso do usuário ao sistema.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Usuário e senha em campos específicos (valor **Padrão**) |
| 1 | Usuário e senha no mesmo campo, com as informações separadas por **+** |

#### PDV.VALORFUNDOTROCO

Define o valor de fundo de troco.

| Valor (Moeda) | Descrição |
| --- | --- |
| 0 | Permite informar qualquer valor de fundo de troco, inclusive 0. Desconsidera fundo de troco (valor **Padrão**) |
| 1 | Exige que seja informado um fundo de troco maior do que 0 |
| 2 | Exige que seja informado um fundo de troco maior ou igual à sugestão de fundo de troco (PDV.ValorFundoTroco) |

#### PDV.VALORMAXIMODIGITADO

Indica o valor máximo, no formato inteiro, a ser digitado no visor para números.

Valor **Padrão**: 999999.

#### PEDIDO.APROVEITAMENTOCREDITO.EXIGIRTITULO

Exige que informe os títulos ao informar uma forma de pagamento do tipo Aproveitamento de Crédito.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não |
| 1 | Sim (valor **Padrão**) |

#### PEDIDO.CONSULTA.LOTE.REDE

Sugere oportunidade de venda na tela de pedido.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não sugere inclusão de garantia estendida ou seguro furto e roubo ao adicionar o item no pedido de venda |
| 1 | Sugere inclusão de garantia estendida ou seguro furto e roubo (valor **Padrão**) |

#### PEDIDO.CONSULTA.SERIE.REDE.AUTOMATICAMENTE

Define se ao abrir a tela de consulta de série no pedido já deve consultar na rede automaticamente.

| Valor | Descrição |
| --- | --- |
| 0 | Não (valor **Padrão**) |
| 1 | Sim |

#### PEDIDO.CONSULTAESTOQUETODOSDEPOSITOS.SOMARQTDORDEMDISPONIVEL

Indica se a quantidade em ordem de compra, soma ou não na quantidade disponível para o depósito.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não |
| 1 | Sim |

#### PEDIDO.FINALIZAR.TEMRECEBIMENTO

Configura se deve exigir, na finalização de um pedido, o registro de recebimento (financeiro) para o pedido.

| Valor (Lista) | Descrição |
| --- | --- |
| N | Não |
| S | Sim (valor **Padrão**) |

#### PEDIDO.HABILITAFRETEGRATIS

Habilita ou desabilita o possibilidade de conceder frete grátis no pedido.

| Valor (Lista) | Descrição |
| --- | --- |
| N | Impede o Frete grátis |
| S | Aceita o frete grátis, ou seja, o botão Frete Grátis fica visível no Retaguarda (valor **Padrão**) |

#### PEDIDO.LAYOUT

Define qual será a exibição da tela de pedidos conforme segmento/necessidade da empresa.

| Valor (Lista) | Descrição |
| --- | --- |
| 1 | Padrão (valor **Padrão**) |
| 2 | Simplificado |
| 3 | Calçadista |
| 4 | Construção |

Observação

Com o valor **4** configurado são apresentadas na grade de Itens do Pedido, as colunas Lote/Série e removida a coluna Serviço Vinc. Além disso, o botão Oportunidades Vendas também será removido da tela. Com esta configuração, o campo Indicado Por será apresentado no cabeçalho do pedido, e permitirá selecionar um cliente que indicou a Loja para a realização da venda. A informação do cliente indicador de negócio será integrada ao Gestão Empresarial | ERP, quando o pedido for integrado.

#### PEDIDO.LIMPARTIPOENTREGA

Limpa o tipo de entrega após inserir um item no pedido ou consulta de preço do Retaguarda, para que seja necessário informar a entrega a cada novo item incluído ou consultado.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Mantém o tipo de entrega informado pelo usuário (valor **Padrão**) |
| 1 | Limpa o tipo de entrega informado sempre que um item é incluído |

#### PEDIDO.MONTAGEMFRETE.INFORMACOESADICIONAIS

Configura a obrigatoriedade de preenchimento de informação do campo Informações Adicionais, tanto para frete quanto para montagem.

| Valor (Lista) | Descrição |
| --- | --- |
| S | Sim |
| N | Não (valor **Padrão**) |

#### PEDIDO.PERMITE.APELIDO.CLIENTE

Informa uma identificação extra do nome do cliente no pedido. Ao habilitar esse parâmetro (**S**) será apresentado o campo Ident. Cliente no pedido. Quando esse campo é informado, e quando o nome do cliente do pedido for igual a CONSUMIDOR FINAL, na tela de importação de pedidos no PDV será exibido o conteúdo do campo Ident. Cliente informado no pedido.

| Valor | Descrição |
| --- | --- |
| N | Não (valor **Padrão**) |
| S | Sim |

#### PEDIDO.PERMITE.DESCONTO.JUROS

Permite informar um desconto sobre o valor de juros do pedido, gerado através da seleção de uma condição de pagamento que tenha juros.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não (valor **Padrão**) |
| 1 | Sim |

#### PEDIDO.SINALIZARBLOQUEIO

Habilita a mensagem de sinalização de bloqueio no pedido.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não apresentar mensagem (valor **Padrão**) |
| 1 | Apresentar mensagem |

#### PEDIDO.SUGERE.OPORTUNIDADE.VENDA

Sugere oportunidade de venda na tela de pedido.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não sugere inclusão de garantia estendida ou seguro furto e roubo ao adicionar o item no pedido de venda |
| 1 | Sugere inclusão de garantia estendida ou seguro furto e roubo (valor **Padrão**) |

#### PEDIDO.VENDEDOR.PREENCHIMENTOAUTOMATICO

Configura se o sistema deve preencher, na geração de um pedido de venda, a informação do vendedor (usuário) logado para o pedido.

| Valor (Lista) | Descrição |
| --- | --- |
| S | Sim (valor **Padrão**) |
| N | Não |

#### PEDIDOPREVENDA.FINALIZAR.RETORNO

Configura o retorno de tela após finalização do pedido ou pré venda. O parâmetro deve indicar se retorna para a tela de consulta de pedido ou pré venda (respectivamente) ou não.

| Valor (Lista) | Descrição |
| --- | --- |
| S | Sim (valor **Padrão**) |
| N | Não |

#### PERMITE.ALTERAR.VALIDADE.ORCAMENTO

Por padrão, não é possível gerar pedido para um orçamento vencido, porém através desse parâmetro é permitido alterar a validade do orçamento manualmente. Essa alteração é configurada para usuários específicos conforme parametrizado no perfil.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não (valor **Padrão**) |
| 1 | Sim |

#### PROTECAOCREDITO.TIPO

Indica o tipo de proteção de crédito. Utilizado para cheques.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não executa verificação (valor **Padrão**) |
| 1 | Verifica pelo Serasa, através do SiTef (condicionada ao uso do SiTef) |

#### PROTECAOCREDITO.TODOSCHEQUES

Indica se a proteção de crédito será realizada para todos os cheques. É necessário o parâmetro dinâmico ProtecaoCredito.Tipo estar configurado com o valor **1**.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Consulta somente o primeiro cheque da operação |
| 1 | Consulta todos os cheques da operação (valor **Padrão**) |

#### PROTECAOCREDITO.VALORMINIMOCONSULTA

Indica o valor mínimo, no formato inteiro, para efetuar a verificação de crédito do cheque.

Valor **Padrão**: 0.

#### RECARGA.MOTIVOLANCAMENTO

Define o motivo, no formato inteiro, a ser considerado nos movimentos de tesouraria gerados a partir da venda de recarga de celular. O motivo é utilizado para obter a natureza de gasto do lançamento.
Por exemplo: 0, 1, 2, 3, 4.

O número informado para o parâmetro deve ser de acordo com o motivo desejado cadastrado em Cadastros > Identificadores e parâmetros > Motivo de situações/observações (F021MOT).

Valor **Padrão**: 0.

#### RECEBIMENTO.BLOQUEARPRORROGACAO

Indica se é possível prorrogar o vencimento de determinada parcela, quando trata-se de condição onde a parcela é sem juros ou com taxa de juros igual a zero.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Indica que permite prorrogar vencimento da parcela sem juros ou com taxa de Juros igual a zero (valor **Padrão**) |
| 1 | Indica que não permite prorrogar vencimento de parcelas sem juros. Dessa forma, não é possível prorrogar a data de vencimento sem recalcular juros |

#### REDUCAOZ.VERIFICAPEDIDOSPENDENTES

Define se será verificado a existência de pedidos pendentes para faturamento antes da emissão da redução Z.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não verifica (valor **Padrão**) |
| 1 | Verifica e avisa |
| 2 | Verifica e bloqueia |

#### RETAGUARDA.CONTROLAESTOQUE

Define se a filial Retaguarda deve permitir estoque negativo, independentemente do parâmetro na ligação produto x depósito.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não (valor **Padrão**) |
| 1 | Sim |

#### RMI.IPSERVIDOR

IP do servidor RMI, no formato texto.

#### RMI.PortaServidor

Porta para conexão RMI, no formato inteiro. Define a porta de comunicação com o servidor do Retaguarda.

#### RMI.TIPOREPLICACAO

Indica a forma como a replicação das operações irá ocorrer para o Retaguarda.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Via serviço (valor **Padrão**) |
| 1 | Via sistema de PDV |

#### SANGRIA.IMPRIMERELATORIOGERENCIAL

Habilita função para imprimir relatório de sangria.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não (valor **Padrão**) |
| 1 | Sim |

#### SANGRIA.INFORMAPORTADORCHEQUE

Indica se o usuário deve informar o portador para fazer sangria de cheques.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não |
| 1 | Sim (valor **Padrão**) |

#### SANGRIA.MOTIVOLANCAMENTOAUTOMATICO

Código do motivo, no formato inteiro, que será utilizado nos lançamentos automáticos de sangria. Por exemplo: Sangria para fechamento de caixa.

Valor **Padrão**: 0

Observação

Configuração obrigatória quando utilizado motivo na tesouraria (sangria e suprimento).

#### SANGRIA.MOTIVOPADRAOCHEQUE

Indica se as sangrias de cheques terão um motivo padrão que será selecionado automaticamente. Deve ser informado o código do motivo de sangria, no formato inteiro, no ERP. Caso o código seja inválido, esta configuração será ignorada.

#### SANGRIA.QUANTIDADEVIASRELATORIOGERENCIAL

Define número de vias, no formato inteiro, do relatório de sangria. É necessário o parâmetro dinâmico Sangria.ImprimeRelatorioGerencial estar configurado com o valor **1**.

Valor **Padrão**: 1

#### SANGRIA.RETIRADAFUNDOTROCO

Define o comportamento do sistema de PDV nas operações de retirada de valor do caixa em que o valor do fundo de troco estiver ou resultar em um valor menor do que definido no valor para fundo de troco (parâmetro dinâmico PDV.ValorFundoTroco).

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não exige confirmação e realiza a retirada |
| 1 | Exige confirmação para realizar a retirada (valor **Padrão**) |

#### SANGRIA.TRANSFERENCIAAUTOMATICABANCO

Identifica se a filial realiza sangria no PDV, enviando os valores em dinheiro direto para uma conta banco.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não, o valor da sangria é encaminhando para o caixa geral da Loja e posteriormente, via Retaguarda, para o banco (valor **Padrão**) |
| 1 | Sim, ocorre o envio da sangria diretamente para o banco |

#### SANGRIA.VERIFICASALDO

Define se deve permitir manter o caixa com saldo negativo.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não permite saldo negativo (valor **Padrão**) |
| 1 | Permite saldo de caixa negativo |
| 2 | Gera um suprimento de sobra de caixa antes de fazer a sangria, deixando o saldo zerado |
| 3 | Permite, porém exige uma confirmação do operador de caixa |

#### SAT.VERSAO

Informa a versão do equipamento SAT utilizado pelo PDV.

| Valor (Texto) | Descrição |
| --- | --- |
| 0.07 | Versão do equipamento SAT |
| 0.08 | Versão do equipamento SAT (valor **Padrão**) |

#### SEGUROFURTOROUBO.PRAZODEVOLUCAOINTEGRAL

Prazo em dias, no formato numérico, devolução integral do valor pago pelo seguro furto e roubo.

Valor **Padrão**: 7

#### SEGUROFURTOROUBO.REPRESENTANTE.CNPJ

CNPJ da filial, no formato texto, que aparece no Relatório de Seguro Furto e Roubo.

Valor **Padrão**: CNPJ da filial que vende o seguro

#### SEGUROFURTOROUBO.REPRESENTANTE.NOME

Nome da filial que aparece no Relatório de Seguro Furto e Roubo.

Valor **Padrão**: nome da filial que vende o seguro.

#### SEGUROPARCELA.PERCENTUALIOF

Percentual de IOF, no formato numérico, cobrado na venda de seguro parcela protegida.

Valor **Padrão**: 7,38.

#### SEGUROPARCELA.PRAZODEVOLUCAOINTEGRAL

Prazo em dias, no formato numérico, de devolução integral do valor pago pelo seguro parcela protegida.

Valor **Padrão**: 7

#### SUPRIMENTO.IMPRIMERELATORIOGERENCIA

Habilita função para imprimir relatório de suprimento.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não (valor **Padrão**) |
| 1 | Sim |

#### SUPRIMENTO.MOTIVOLANCAMENTOAUTOMATICO

Define o código do motivo, no formato inteiro, que será utilizado nos lançamentos automáticos de suprimento. Por exemplo, suprimento para cobrir falta de caixa.

Valor **Padrão**: 0.

Importante

Configuração obrigatória quando utilizado motivo na tesouraria (sangria e suprimento).

#### SUPRIMENTO.QUANTIDADEVIASRELATORIOGERENCIAL

Define número de vias, no formato inteiro, do relatório de suprimento. É necessário o parâmetro dinâmico Suprimento.ImprimeRelatorioGerencial estar configurado com o valor **1**.

#### TEF.DUPLICARECIBORECARGACELULAR

Indica se duplica o texto do recibo de recarga de celular. Usado principalmente para recargas de celular no VsPague, que está enviando apenas uma via.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não (valor **Padrão**) |
| 1 | Sim |

#### TEF.FALHARECEBEPOS

Direciona para POS em caso de falha no TEF.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não (valor **Padrão**) |
| 1 | Sim |

#### TEF.FILIAL

Número da filial dentro do servidor TEF Auttar. Deve ser configurado com o mesmo número da filial informada no servidor Auttar.

#### TEF.FINALIZADORCARTAOCREDITO

Indica a forma de pagamento, no formato inteiro, **Cartão de Crédito** para o sistema de TEF - SiTef.

#### TEF.FINALIZADORCARTAODEBITO

Indica a forma de pagamento, no formato inteiro, **Cartão de Débito** para o sistema de TEF - SiTef. Informe o código da forma de pagamento.

#### TEF.FINALIZADORCHEQUE

Indica a forma de pagamento, no formato inteiro, **Cheque** para o sistema de TEF - SiTef. Informe o código da forma de pagamento.

#### TEF.FINALIZADORDINHEIRO

Indica forma de pagamento, no formato inteiro, **Dinheiro** para o sistema de TEF - SiTef. Informe o código da forma de pagamento.

#### TEF.FORCACONFIRMACAOTEF

Confirma a transação assim que ela for autorizada, independentemente se o comprovante de pagamento foi impresso ou não. Quando o parâmetro estiver configurado com o valor **0** ou vazio, caso ocorra algum problema com a emissão do comprovante não fiscal, a transação será cancelada mesmo se ela já estiver autorizada.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não (valor **Padrão**) |
| 1 | Sim |

#### TEF.HABILITACORRESPONDENTEBANCARIO

Habilita função de correspondente bancário.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não (valor **Padrão**) |
| 1 | Sim |

#### TEF.HABILITARECARGACELULAR

Habilita função de recarga de celular.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não (valor **Padrão**) |
| 1 | Sim |

#### TEF.IPSERVIDOR

**TEF SITEF ou Auttar:** define o IP do Servidor TEF.

**TEF V$Pague:** permite definir o IP onde o client V$Pague estará em execução, caso opte por um client remoto (usado em ambiente cloud).

Default = Localhost.

#### TEF.PORTASERVIDOR

Define a porta onde o client V$Pague estará em execução (usado em ambiente cloud). Para o TEF Auttar, é a porta de acesso ao Servidor, por exemplo: 1996.

Default = 60906.

#### TEF.LIMITEPAGAMENTOSCARTAO

Define a quantidade, no formato texto, de formas de pagamento do tipo TEF que um cupom fiscal poderá ter.

| Valor | Descrição |
| --- | --- |
| 0 | Sem limite |
| 2 | Limitação máxima em duas formas de pagamento (valor **Padrão**) |

#### TEF.MENSAGEMPINPAD

Mensagem exibida no pinpad.

Observação

Não utilizado para Auttar. A configuração deve ser realizada diretamente no CTFClient.

#### TEF.NUMEROLOJA

Define o número, no formato texto, da loja para o TEF.

#### TEF.PORTASERIALPINPAD

Define a porta de comunicação com o PINPAD.

O parâmetro está disponível para ser utilizado para definir o mesmo valor para toda a filial e, consequentemente, para todos os PDVs cadastrados. Também é possível adicioná-lo em PDVs específicos através do cadastro do PDV (F070PDV). Para cadastrar, utilize o botão Par. Dinâmicos. O parâmetro do tipo PDV sempre será prioritário quando existir. Se não existir uma parametrização, será utilizado o de Filial. E se não tiver nenhum, o valor ficará vazio.

Observação

Não utilizado para Auttar. A configuração deve ser realizada diretamente no CTFClient.

#### TEF.RESTRICAOADMINISTRATIVA

Define as restrições, no formato texto, para as funções administrativas no sistema de TEF - SiTef.

#### TEF.RESTRICAOCONSULTACHEQUE

Define as restrições, no formato texto, para a função de consulta cheque no sistema de TEF - SiTef.

Valor **Padrão**: vazio.

#### TEF.RESTRICAOCORRESPONDENTEBANCARIO

Define restrições, no formato texto, para a função de correspondente bancário no sistema de TEF - SiTef.

#### TEF.RESTRICAORECARGACELULAR

Define restrições, no formato texto, para a função de recarga de celular no sistema de TEF - SiTef.

#### TEF.RESTRICAORECEBIMENTO

Define as restrições, no formato texto, para transação de cartão em recebimento de título, no sistema de TEF - SiTef e Auttar. Os códigos a serem ocultos devem ser separados com ponto e vírgula.

## Códigos TEF Auttar

Todas as transações ficam habilitadas de forma padrão. Se alguma não será utilizada, pode ser oculta utilizando este parâmetro, incluindo o código da operação que não será utilizada conforme a tabela:

| Código | Descrição | Explicação |
| --- | --- | --- |
| 101 | Débito | Pagamento convencional com débito. |
| 103 | Débito Pré-Datado | O produto pré-datado permite ao portador do cartão de débito realizar compras e pré-datar o pagamento em até 90 dias. O débito na conta do portador e o crédito ao estabelecimento comercial são efetuados no dia acordado entre as partes. |
| 104 | Débito Parcelado | O serviço de parcelamento no cartão de débito é relativamente novo no mercado. Ele se trata de uma linha de crédito, mas disponibilizada na função de débito que permite o parcelamento das compras em todos os estabelecimentos que possuem uma máquina ou terminal compatível com o uso de crediário. |
| 105 | Débito Parcelado com Parcela À Vista | Mesmo conceito do código 104 mas com a parcela à vista. |
| 106 | Débito Voucher | Vouchers são cartões-benefícios, disponibilizados pelos empregadores aos funcionários para compra de produtos específicos. |
| 108 | Débito CDC com Parcela À Vista | O Crédito Direto ao Consumidor (CDC) é a obtenção de crédito sem burocracia, ou seja, o valor é disponibilizado de forma imediata por bancos ou instituições financeiras em dinheiro ou crédito, sem complicações. Neste caso, com parcela à vista. |
| 109 | Débito CDC sem Parcela À Vista | Mesmo conceito do código 108 mas sem a parcela à vista. |
| 112 | Crédito | Pagamento convencional com crédito. |
| 113 | Crédito Parcelado sem Juros | Pagamento com crédito e parcelado pelo estabelecimento. |
| 114 | Crédito Parcelado com Juros | Pagamento com crédito e parcelado pela administradora. |
| 120 | Crédito Digitado | Pagamento com crédito e cartão digitado. |
| 121 | Crédito Digitado Parcelado sem Juros | Pagamento com crédito, cartão digitado e parcelado pelo estabelecimento (a loja arca com os juros aplicados). |
| 122 | Crédito Digitado Parcelado com Juros | Pagamento com crédito, cartão digitado e parcelado pela administradora (o cliente arca com os juros aplicados). |
| 142 | Crédito Private Label | Cartão private label ou cartão de crédito de loja é um tipo de cartão de crédito emitido por um varejista e usualmente válido apenas para a realização de compra nos estabelecimentos de propriedade deste varejista. |
| 143 | Crédito Private Label Digitado | Mesmo conceito do código 142 mas utilizando o cartão digitado. |

Nota

Códigos retirados do manual de integração Auttar.

#### TEF.RESTRICAOVENDA

Define restrições, no formato texto, para transação de cartão em vendas, no sistema de TEF - SiTef e Auttar. Os códigos a serem ocultos devem ser separados com ponto e vírgula.

## Exemplo

TEF.RESTRICAOVENDA = 120;121;122;143.

## Códigos TEF Auttar

Todas as transações ficam habilitadas de forma padrão. Se alguma não será utilizada, pode ser oculta utilizando este parâmetro, incluindo o código da operação que não será utilizada conforme a tabela:

| Código | Descrição | Explicação |
| --- | --- | --- |
| 101 | Débito | Pagamento convencional com débito. |
| 103 | Débito Pré-Datado | O produto pré-datado permite ao portador do cartão de débito realizar compras e pré-datar o pagamento em até 90 dias. O débito na conta do portador e o crédito ao estabelecimento comercial são efetuados no dia acordado entre as partes. |
| 104 | Débito Parcelado | O serviço de parcelamento no cartão de débito é relativamente novo no mercado. Ele se trata de uma linha de crédito, mas disponibilizada na função de débito que permite o parcelamento das compras em todos os estabelecimentos que possuem uma máquina ou terminal compatível com o uso de crediário. |
| 105 | Débito Parcelado com Parcela À Vista | Mesmo conceito do código 104 mas com a parcela à vista. |
| 106 | Débito Voucher | Vouchers são cartões-benefícios, disponibilizados pelos empregadores aos funcionários para compra de produtos específicos. |
| 108 | Débito CDC com Parcela À Vista | O Crédito Direto ao Consumidor (CDC) é a obtenção de crédito sem burocracia, ou seja, o valor é disponibilizado de forma imediata por bancos ou instituições financeiras em dinheiro ou crédito, sem complicações. Neste caso, com parcela à vista. |
| 109 | Débito CDC sem Parcela À Vista | Mesmo conceito do código 108 mas sem a parcela à vista. |
| 112 | Crédito | Pagamento convencional com crédito. |
| 113 | Crédito Parcelado sem Juros | Pagamento com crédito e parcelado pelo estabelecimento. |
| 114 | Crédito Parcelado com Juros | Pagamento com crédito e parcelado pela administradora. |
| 120 | Crédito Digitado | Pagamento com crédito e cartão digitado. |
| 121 | Crédito Digitado Parcelado sem Juros | Pagamento com crédito, cartão digitado e parcelado pelo estabelecimento (a loja arca com os juros aplicados). |
| 122 | Crédito Digitado Parcelado com Juros | Pagamento com crédito, cartão digitado e parcelado pela administradora (o cliente arca com os juros aplicados). |
| 142 | Crédito Private Label | Cartão private label ou cartão de crédito de loja é um tipo de cartão de crédito emitido por um varejista e usualmente válido apenas para a realização de compra nos estabelecimentos de propriedade deste varejista. |
| 143 | Crédito Private Label Digitado | Mesmo conceito do código 142 mas utilizando o cartão digitado. |

Nota

Códigos retirados do manual de integração Auttar.

#### TEF.SENHASUPERVISOR

Define senha,no formato texto, de supervisor para operações de cancelamento no TEF - SiTef.

#### TEF.TIPO

Define qual o integrador de TEF utilizado.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Nenhum (valor **Padrão**) |
| 1 | SiTef |
| 2 | V$Pague |
| 3 | Auttar |

Importante

Para integrar a solução Gestão de Lojas com o sistema V$Pague é necessário:

* No campo Filial informar a filial em que será utilizado o V$Pague e clicar em Mostrar;
* Inserir (ou alterar caso já exista o parâmetro) um novo parâmetro preenchendo da seguinte forma: após informar os campos e clicar em Processar aguarde a integração com o Retaguarda. Logo após integrar o parâmetro, acesse Cadastros > Filiais, clique em Visualizar e verificar na guia Definições > PDV se o parâmetro criado no ERP encontra-se nesta tela.

## Páginas relacionadas

* [F435CCC](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f435ccc.htm)
* [F435MDT](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f435mdt.htm)
* [F135APM](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f135apm.htm)
* [F135AEA](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f135aea.htm)
* [AtenderManualPedidos](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/webservices/com_senior_g5_co_mcm_ven_manualpedidos.htm#AtenderManualPedidos_2)
* [VEN-135EUDLE02](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_135eudle02.htm)
* [Van Bancária](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/van-bancaria/van-bancaria-integracao.htm)
* [F410QCP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f410qcp.htm#f410qcp.htm)
* [registro I050](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/sped/contabil-ecd/bloco-i.htm#I050)
* [Parâmetro dinâmico EMPRESA.GESTORSENIOR.FORMAEXIBIRRATEIO](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/parametro_dinamico_empresa.gestorsenior.formaexibirrateio.htm)
* [F075PRO](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075pro.htm)
* [F900RCP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_manufatura/f900rcp.htm)
* [VAN Bancária](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/van-bancaria/vans.htm)
* [com.senior.g5.co.int.varejo.cliente](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/webservices/com_senior_g5_co_int_varejo_cliente.htm)
* [com.senior.g5.co.int.varejo.produto](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/webservices/com_senior_g5_co_int_varejo_produto.htm)
* [F070EMP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070emp.htm)
* [Operações de nota fiscal (F070ONF)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070onf.htm)
* [F070PDV](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070pdv.htm)
