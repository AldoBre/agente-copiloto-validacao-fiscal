# Cadastro de filiais (F070FCA)

> **Fonte:** F000PPD -  Configuração de parâmetros dinâmicos — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000ppd.htm#cadfil  
> **Trilha:** Ajuda por telas > Cadastros  
> **Telas citadas:** E660RRZ, E660RSC, E660RSV, F000AGE, F000GOW, F000PPD, F001TES, F021MOT, F039POR, F070FCA, F070VAR, F075CEP, F113REM, F135FCP, F185CFG, F460APR  
> **Identificadores de regras:** GER-140EUDLE01, GER-210EUDLE01, VEN-140CFILE01, VEN-140EUDLE02

---
#### ABERTURA.EXIGEFUNDOTROCO

Define se deve ser exigido que o operador informe o valor para fundo de troco.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não exige (valor **Padrão**) |
| 1 | Exige fundo de troco maior que zero |
| 2 | Exige fundo de troco maior ou igual ao definido como fundo de troco |
| 3 | Mantém o fundo de troco sugerido, sem possibilitar alterações do usuário |

#### AGR.DENTRO.ESTADO.NF.ACERTO.FIXACAO.TNSPRO

Transação (dentro do Estado) para geração de nota fiscal de entrada tipo 10, para fixação de pessoa física, quando não foram calculados os valores referentes ao Funrural Senar e GilRat.

#### AGR.FORA.ESTADO.NF.ACERTO.FIXACAO.TNSPRO

Transação (fora do Estado) para geração de nota fiscal de entrada tipo 10, para fixação de pessoa física, quando não foram calculados os valores referentes ao Funrural Senar e GilRat.

#### AGR.PESAGEM.TOLERANCIA.PESO.OP.CAN

Informar o peso máximo de tolerância para a operação de cancelamento (Carga/Descarga não realizada). Essa tolerância poderá ser para mais ou para menos.

Valor **Padrão**: 40

#### AGR.PESAGEM.VALIDAR.TNSCTR.X.TNSNOTA

A função desse parâmetro, é após a pesagem, definir se o usuário pode ou não alterar a participação do contrato e se a transação da nota deve respeitar a transação do contrato.

| Valor (Lista) | Descrição |
| --- | --- |
| N | Não consistir. (valor **Padrão**) |
| S | Consistir. |

#### AGR.PRAZOAPAGARFOTOSBALANCA

Este parâmetro indica com quanto tempo as fotos de pesagem da balança "antigas" devem ser excluídas. Exemplo: se for configurado como 15 dias, as fotos que têm mais de 15 dias serão apagadas.

Para ativar esta funcionalidade, é necessário que a rotina de processo automático 146 - Limpar fotos antigas da Balança esteja configurada.

**Valor Padrão:** 20

#### AGRO.NFS.GERA.TAG.RECEITUARIO.AGRONOMICO.NFS

O objetivo desse parâmetro é definir se as tags referentes ao receituário agronômico serão geradas no envio da NFS para a SEFAZ.

| Valor (Lista) | Descrição |
| --- | --- |
| N | Não gerar tags (Valor Padrão) |
| S | Gerar tags |

#### AGRO.RECEITA.SUGESTAODOSE.MAXIMO

O objetivo desse parâmetro é definir a sugestão de dose que o sistema irá trazer como padrão na tela Emissão da receita agronômica (F113REM).

| Valor (Lista) | Descrição |
| --- | --- |
| N | Define a sugestão da dose como Valor Mínimo |
| S | Define a sugestão da dose como Valor Máximo |

#### AGRO.TAXAS.ARREDONDAMENTO

Define a tolerância para realizar o arredondamento dos valores das taxas. Caso o resultado do cálculo seja diferente do valor total informado a ser fixado, transferido e/ou devolvido, e esta diferença esteja dentro da tolerância informada neste parâmetro, o montante será arredondado para o valor informado. Destaca-se, ainda, que ao ativar este parâmetro, é possível alterar o valor padrão de tolerância informado.

Exemplo: O valor a fixar é 6.000,00 porém, após todos os cálculos, o resultado obtido foi 5.999,99999. Neste caso, se estiver na tolerância informada, o valor será transformado em 6.000,00.

Valor **Padrão**: 0,00002

#### AGR.VENDA.CODIGOIMPOSTOAGROCALCULOCDO

Indica qual o código do imposto Agro de cálculo da Taxa de Cooperação e Defesa da Orizicultura (CDO) para vendas.

#### APROVCREDITO.TIPO

Define quais as formas de utilizar o aproveitamento de crédito no PDV e no Retaguarda.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Ambos (valor **Padrão**) |
| 1 | Por cliente |
| 2 | Por documento |

#### APROVEITAMENTO.EXIBELISTADOCUMENTOS

Define se deve ou não apresentar a lista de documentos para aproveitamento de crédito quando encontrar mais de um registro para o mesmo número na filial.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não (valor **Padrão**) |
| 1 | Sim |

#### ARR\_RFT\_NFS

Define o método de arredondamento aplicado pelo motor de cálculo de IBS e CBS da Reforma Tributária para todos os Documentos de Saída emitidos pela filial, independentemente da série.
Quando configurado, sobrescreve o valor do parâmetro global TipArrRef para NF.
Para configurar o método por série específica de NF, utilize o parâmetro ARR\_RFT\_NFS\_{série} (por exemplo: ARR\_RFT\_NFS\_A para a série A), que tem precedência sobre este parâmetro.

| Valor (Lista) | Descrição |
| --- | --- |
| A | Arredondamento normal (Padrão) |
| B | Arredondamento conforme ABNT NBR 5891 |
| T | Truncamento do valor calculado |

#### ARR\_RFT\_NFS\_{série}

Define o método de arredondamento aplicado pelo motor de cálculo de IBS e CBS da Reforma Tributária para NF de uma série específica. O trecho {série} deve ser substituído pela série da nota fiscal de serviço (por exemplo: ARR\_RFT\_NFS\_A para a série A; ARR\_RFT\_NFS\_B para a série B). Este parâmetro tem precedência sobre o parâmetro ARR\_RFT\_NFS e sobre o parâmetro global TipArrRef.

|
|  |
| Valor (Lista) | Descrição |
| A | Arredondamento normal (Padrão) |
| B | Arredondamento conforme ABNT NBR 5891 |
| T | Truncamento do valor calculado |

#### ASSISTENCIA.DEVOLUCAO.COMPENSAR.FINANCEIRO

Identifica se no processo de devolução, na tela de assistência técnica, o sistema vai compensar os títulos da venda de origem automaticamente. Caso o parâmetro esteja marcado como **0**, o sistema irá identificar, no momento da devolução, se a nota de entrada é proveniente de uma assistência. Caso seja, o sistema não irá entrar na rotina que efetua o endosso dos títulos.

| Valor | Descrição |
| --- | --- |
| 0 | Não |
| 1 | Sim (valor **Padrão**) |

#### ASSISTENCIA.DIAS.VENCIMENTO

Define a quantidade de dias que o registro será pintado de vermelho na tela de assistência técnica no Retaguarda. O número informado para o parâmetro, no formato inteiro.

Valor **Padrão**: 25

#### ASSISTENCIA.HABILITAR.BOTAO.TROCA

Indica se o botão **Trocar Item (F3)** fica habilitado na assistência técnica.

| Valor | Descrição |
| --- | --- |
| 0 | Desabilita |
| 1 | Habilita (valor **Padrão**) |

#### ASSISTENCIA.MOTIVOPADRAO.TRANSFERENCIA

Define o motivo padrão que a assistência irá utilizar para a transferência. O número informado para o parâmetro, no formato inteiro, deve ser de acordo com o motivo desejado cadastrado em Cadastros > Identificadores e parâmetros > Motivo de situações/observações (F021MOT). Por exemplo: 1, 2, 3, 4.

Valor **Padrão**: vazio.

#### ATUALIZACAO.ATUALIZADORES.DIR

Nome do diretório compartilhado, no formato texto, no qual localizam-se os atualizadores. Recomenda-se fortemente utilizar o padrão SeniorAtualizadoresVarejo, pois neste caso, não é necessário informar este parâmetro.

Valor **Padrão**: SeniorAtualizadoresVarejo.

#### ATUALIZACAO.ATUALIZADORES.DOMINIO

Complementa o parâmetro ATUALIZACAO.ATUALIZADORES.LOGIN especificando o domínio (workgroup), no formato texto, ao qual o usuário pertence. Caso o usuário não seja de domínio e sim um usuário local do computador destino, informar o nome de rede do computador onde localizam-se os atualizadores.

Valor **Padrão**: vazio.

#### ATUALIZACAO.ATUALIZADORES.HOST

Nome de rede ou IP do computador, no formato texto, onde localiza-se o diretório compartilhado com os atualizadores do Gestão de Lojas. Este computador pode ter sistema operacional Windows ou Linux (Ubuntu) e precisa estar acessível por todas as estações (PDVs e Retaguarda) de todas as lojas. Caso não informado, cada estação vai procurar os atualizadores no servidor do Retaguarda.

Valor **Padrão**: vazio

#### ATUALIZACAO.ATUALIZADORES.LOGIN

Nome do usuário a ser utilizado, no formato texto, para acessar o diretório compartilhado em busca dos atualizadores. Este parâmetro é necessário apenas quando o usuário das estações (PDV e Retaguarda) não possuir permissão de acesso nativa ao diretório compartilhado. E utilizado somente quando ATUALIZACAO.ATUALIZADORES.USARSMB estiver com o valor **1**.

Ao informar este parâmetro, deve-se informar também ATUALIZACAO.ATUALIZADORES.SENHA e ATUALIZACAO.ATUALIZADORES.DOMINIO.

Valor **Padrão**: vazio.

#### ATUALIZACAO.ATUALIZADORES.SENHA

Complementa o parâmetro dinâmico ATUALIZACAO.ATUALIZADORES.LOGIN, especificando a senha deste usuário, no formato texto, para acesso ao diretório compartilhado.

Para segurança, obrigatoriamente, a senha deve ser informada neste parâmetro já codificada em formato Base64. Para codificar a senha, podem ser utilizados os seguintes utilitários Base64 Decode and Encode ou Base64 Encode. Utilize charset UTF-8.

Valor **Padrão**: vazio.

#### ATUALIZACAO.ATUALIZADORES.USARSMB

Determina se deve ser utilizada a biblioteca SMB (Samba) ao acessar o diretório compartilhado para busca dos atualizadores. Esta biblioteca é necessária quando o servidor dos arquivos é Windows e as estações são Linux. Neste caso, será necessário também informar os parâmetros

* ATUALIZACAO.ATUALIZADORES.LOGIN
* ATUALIZACAO.ATUALIZADORES.SENHA
* ATUALIZACAO.ATUALIZADORES.DOMINIO

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não utiliza a biblioteca Samba(valor **Padrão**) |
| 1 | Utiliza a biblioteca Samba |

#### BALANCAETIQUETA.DESCONSIDERAZEROESQUERDA

Indica se na pesquisa pelo código do produto, o sistema deve considerar ou não os zeros à esquerda.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não (valor **Padrão**) |
| 1 | Sim |

#### BALANCAETIQUETA.DIGITOIDENTIFICACAO

Define o dígito identificador que determina se o código é de uma etiqueta de balança. Se estiver vazio, não identifica etiquetas de balança. O dígito 9 já é utilizado para variação de código de barras.

| Valor (Numérico) | Descrição |
| --- | --- |
| 0 - 8 | Caso seja informado de 0 a 8, o sistema irá determinar se o código é de uma etiqueta de balança |
| (vazio) | Manter campo **Valor** vazio (valor **Padrão**) |

#### BALANCAETIQUETA.TAMANHOCODIGO

Define a quantidade de dígitos do código identificador do produto.

O TAMANHOVALOR + TAMANHOCODIGO devem compor até 11 dígitos, pois o código de balança possui 13 dígitos, onde o primeiro é identificador e o último é verificador.

| Valor (Numérico) | Descrição |
| --- | --- |
| 1 - 9 | Caso seja informado de 1 a 9, o sistema irá definir a quantidade de dígitos do código identificador do produto |
| 5 | Quantidade de dígitos do código identificador do produto (valor **Padrão**) |

#### BALANCAETIQUETA.TAMANHOVALOR

Define a quantidade de dígitos do valor após o código identificador do produto. Esse valor pode ser tanto a quantidade quanto o preço total do produto.

O TAMANHOVALOR + TAMANHOCODIGO devem compor até 11 dígitos, pois o código de balança possui 13 dígitos, onde o primeiro é identificador e o último é verificador.

| Valor (Numérico) | Descrição |
| --- | --- |
| 1 - 9 | Caso seja informado de 1 a 9, o sistema irá definir a quantidade de dígitos do código identificador do produto |
| 6 | Quantidade de dígitos do código identificador do produto (valor **Padrão**) |

#### BALANCAETIQUETA.TIPO

Define se a etiqueta informará a quantidade ou o preço total do produto.

| Valor | Descrição |
| --- | --- |
| 0 | Quantidade (valor **Padrão**) |
| 1 | Preço total |

#### BLOCOXPAF.GERA.ANUAL.ESTOQUE

Ao habilitar o parâmetro, o sistema gerará o arquivo do bloco X com a posição do estoque do dia 31/12 do ano corrente. Além disso, notificará diariamente, após o primeiro dia de janeiro e até 20 de janeiro, caso o arquivo referente à 31/12 ainda não foi transmitido.

| Valor | Descrição |
| --- | --- |
| 0 | Mantem o comportamento atual do sistema (valor **Padrão**). |
| 1 | Altera a geração automática do blocoXEstoque para anual. |

#### BLOCOXPAF.HABILITA.DESABILITA

Responsável por habilitar/desabilitar a funcionalidade do Bloco X no Gestão de Lojas.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Desabilitado (valor **Padrão**) |
| 1 | Habilitado |

#### BLOCOXPAF.PERMITE.ENVIO.SEFAZ

Define se as informações do Bloco X serão enviadas ou não para a SEFAZ. Por padrão, o sistema fará o envio normalmente. Caso o parâmetro esteja desabilitado, o sistema atualizará a situação para "13 - Gerado e não enviado".

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Desabilitado |
| 1 | Habilitado (valor **Padrão**) |

#### BLOQUEIO.MARGEM.CONTRIBUICAO

Define se o sistema vai efetuar o bloqueio por margem de contribuição.

| Valor | Descrição |
| --- | --- |
| 0 | Não |
| 1 | Sim (valor **Padrão**) |

#### CARGACOMPLETA.ATUALIZAAUTOMATICAMENTE

Indica se a atualização completa da base de dados será verificada ao iniciar o sistema.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não |
| 1 | Sim (valor **Padrão**) |

#### CARGACOMPLETA.INTERVALODIAS

Número de dias para fazer a carga completa na inicialização do sistema. É necessário o parâmetro dinâmico CargaCompleta.AtualizaAutomaticamente estar configurado com o valor **1**.

| Valor (Inteiro) | Descrição |
| --- | --- |
| 0 | Nunca realiza a carga |
| 1 | Realiza a carga todo dia (valor **Padrão**) |
| Qualquer outro número | Realiza a carga conforme o número informado |

#### CARGAPARCIAL.MULTIPLOS10SEGUNDOSSINCRONIZACAO

Tempo em múltiplos de 10 segundos para realizar a carga parcial. É necessário o parâmetro dinâmico CargaCompleta.AtualizaAutomaticamente estar configurado com o valor **1**.

| Valor (Inteiro) | Descrição |
| --- | --- |
| 0 | Realiza a carga sem intervalos |
| 1 | Realiza a carga a cada 10 segundos |
| 2 | Realiza a carga a cada 20 segundos |
| 6 | Realiza a carga a cada 60 segundos (valor **Padrão**) |
| Outro número | Realiza a carga conforme o número informado multiplicado por 10 |

#### CHEQUE.DIASVENCIMENTOMAXIMO

Configura o número máximo de dias, no formato inteiro, para cheques pré datados. Se zero ou vazio, significa que não deve validar. Por exemplo: 0, 1, 2, 3, 4.

Valor **Padrão**: 0

Tratamento para a data futura no recebimento:

* caso exista apenas um cliente nos títulos identificados, será utilizado o número de dias do cliente;
* Se existir mais de um cliente ou se o cliente não tiver número de dias pré-datado, será verificado para a filial. Não será bloqueada a digitação da data neste momento, e sim, alertado que a data não é aceita para cheque-pré, conforme: "ATENÇÃO: data fora do período permitido para cheque pré. Dias permitidos <dias\_máximo\_cheque>".

**Observação**

Caso seja informada uma data não permitida, a mensagem: "Data inválida, prazo máximo de vencimento de <dias\_máximo\_cheque>" dias será exibida.

#### CLIENTE.DESABILITAR.EXCLUIR.OBSERVACAO

Desabilita o botão de excluir observações do cadastro de clientes do Retaguarda.

| Valor (Lista) | Descrição |
| --- | --- |
| S | Botão será desativado |
| N | Botão permanece ativo (valor **Padrão**) |

#### COBRANCA.PROTESTO.FILIAL.CÓDIGOBANCO.CÓDIGOINTRUCAO

Recurso para preenchimento dos campos código de protesto para o processo de cobrança escritural via Nexxera. Para mais informações, acesse o manual da Nexxera na documentação da VAN Bancária, campo C026.

#### CONCILIACAOCARTAO.NSU

Determina qual valor o Retaguarda deverá enviar ao Gestão Empresarial | ERP para que seja utilizado na conciliação de vendas por cartão.

| Valor (Inteiro) | Descrição |
| --- | --- |
| 0 | Envia o NSU da transação (valor **Padrão**) |
| 1 | Envia o NSU Rede |

#### CONSIDERA.INTERMEDIACOES.NOTA.FISCAL

Define se será enviado o valor referente a garantia estendida ou seguro para a nota fiscal do produto com a tag vOutros.

| Valor | Descrição |
| --- | --- |
| 0 | Não considera os valores referentes a garantia estendida ou seguro ao acrescentar os valores referentes a tag vOutros da nota fiscal (valor **Padrão**) |
| 1 | Sempre considera os valores referentes a garantia estendida ou seguro para acrescentar a tag vOutros da nota fiscal. |

#### CONSIGNACAO.FORMABUSCA.PRECO

Indica qual a forma de buscar o preço do produto para geração da nota de remessa por consignação.

| Valor | Descrição |
| --- | --- |
| 0 | Tabela preço padrão da filial (valor **Padrão**) |
| 1 | Preço médio |

#### CONSIGNACAO.OPERACAO.REMESSA

Operação de nota fiscal, no formato String, utilizada na emissão de notas fiscais de saída de remessa por consignação. Recebe como valor o código de referência da operação a ser usada para gerar a nota de saída de remessa por consignação.

#### CONSIGNACAO.OPERACAO.RETORNO

Operação de nota fiscal, no formato String, utilizada na emissão de notas fiscais de entrada de retorno por consignação. Recebe como valor o código de referência da operação a ser usada para gerar a nota de entrada de retorno de consignação.

#### CONTASPAGAR.HABILITADO

Define se o PDV realiza pagamentos.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Desabilita (valor **Padrão**) |
| 1 | Habilita |

#### CONTASPAGAR.IMPRIMERELATORIOGERENCIAL

Define se deve ser emitido o comprovante de pagamento (recibo) e a quantidade de vias que deve ser impresso, quando o operador de caixa efetuar o pagamento a um fornecedor.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não imprime |
| 1 | Imprime (valor **Padrão**) |

#### CONTASPAGAR.QUANTIDADEVIASRELATORIOGERENCIAL

Define a quantidade, no formato inteiro, de vias que deve ser impresso do comprovante de pagamento.

Valor **Padrão**: 1

#### CONTASPAGAR.VALORMAXIMO

Define o valor máximo, no formato moeda, que poderá ser pago no caixa, sendo o valor referente a cada título e ao saldo devedor de cada título.

| Valor | Descrição |
| --- | --- |
| 0 | Sem limite (valor **Padrão**) |
| Qualquer outro valor | Determina um limite |

#### CONTASRECEBER.ACEITADIVERSOSCLIENTES

Define se pode ser identificado mais de um cliente para um mesmo recebimento, nas situações em que o recebimento é efetuado consultando títulos de clientes.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não habilita (valor **Padrão**) |
| 1 | Habilita |

#### CONTASRECEBER.ACEITARECEBIMENTOPARCIAL

Define se o sistema permite recebimento parcial de títulos.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não |
| 1 | Sim (valor **Padrão**) |

#### CONTASRECEBER.ALTERAENCARGOS

Define se é permitido alterar o valor dos encargos (juros, multa e desconto por antecipação) no recebimento de títulos.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não altera (valor **Padrão**) |
| 1 | Altera |

#### CONTASRECEBER.DIASFRENTECOMOVENCIDOS

Define quantos dias, no formato inteiro, serão considerados pelo sistema para determinar que um título será exibido como vencido.

Valor **Padrão**: 0.

## Exemplo:

Data atual: 01/10/2012

* Título 1, vencimento: 01/09/2012;
* Título 2, vencimento: 30/09/2012;
* Título 3, vencimento: 01/10/2012;
* Título 4, vencimento: 02/10/2012;
* Título 5, vencimento: 03/10/2012.
* Título 6, vencimento: 10/10/2012.

**Se a configuração for 0 (zero), serão exibidos como vencidos os seguintes títulos:**

Título 1, vencimento: 01/09/2012;

* Título 2, vencimento: 30/09/2012;

**E como a vencer:**

* Título 3, vencimento: 01/10/2012;
* Título 4, vencimento: 02/10/2012;
* Título 5, vencimento: 03/10/2012.
* Título 6, vencimento: 10/10/2012.

**Se a configuração for 1 dia, serão exibidos como vencidos os seguintes títulos:**

* Título 1, vencimento: 01/09/2012;
* Título 2, vencimento: 30/09/2012;
* Título 3, vencimento: 01/10/2012;

**E como a vencer:**

* Título 4, vencimento: 02/10/2012;
* Título 5, vencimento: 03/10/2012.
* Título 6, vencimento: 10/10/2012.

**Se a configuração for 2 dias, serão exibidos como vencidos os seguintes títulos:**

* Título 1, vencimento: 01/09/2012;
* Título 2, vencimento: 30/09/2012;
* Título 3, vencimento: 01/10/2012;
* Título 4, vencimento: 02/10/2012;

**E como a vencer:**

* Título 5, vencimento: 03/10/2012.
* Título 6, vencimento: 10/10/2012.

#### CONTASRECEBER.ESTORNAROFFLINE

Define se é possível receber estornos de maneira off-line.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não habilitado |
| 1 | Habilitado |

#### CONTASRECEBER.EXIBIRNUMEROTITULO

Define se o PDV exibirá somente o número do título na tela principal de consultas de parcelas na função de recebimento. Ao habilitar o parâmetro, o PDV mostrará os campos Número do título, Valor original e Total de encargos. Se estiver desabilitado, o campo Localizador será ocultado.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não |
| 1 | Sim (valor **Padrão**) |

#### CONTASRECEBER.IDENTIFICADORESHABILITADOS

Define com qual identificação é possível efetuar o recebimento de títulos, dentre as opções: Cliente e Localizador.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Ambos (valor **Padrão**) |
| 1 | Cliente |
| 2 | Localizador |

#### CONTASRECEBER.IDENTIFICADORPADRAO

Define a opção de identificação padrão para efetuar o recebimento de títulos, dentre as opções: Cliente e Localizador. É necessário o parâmetro dinâmico ContasReceber.IdentificadoresHabilitados estar configurado com o valor **0**.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Cliente |
| 1 | Localizador (valor **Padrão**) |

#### CONTASRECEBER.IMPRIMECONSULTATITULOSABERTO

Habilita função para imprimir consulta das parcelas em aberto no recebimento de título.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não imprime |
| 1 | Imprime (valor **Padrão**) |

#### CONTASRECEBER.IMPRIMERECIBORESUMIDO

Define se deve ou não imprimir no próprio comprovante não fiscal (recebimento), os dados das parcelas de forma resumida.

| Valor (Texto) | Descrição |
| --- | --- |
| Sim | Imprime comprovante |
| Não | Não imprime comprovante (valor **Padrão**) |

## Exemplo:

![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/imagens/s_reciboresumidoativo_thumb_0_48.png)

#### CONTASRECEBER.IMPRIMERELATORIOGERENCIAL

Define se deve ser emitido o comprovante de pagamento (recibo) quando o operador de caixa efetuar o recebimento de um título de um cliente.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não imprime |
| 1 | Imprime (valor **Padrão**) |

#### CONTASRECEBER.IMPRIMERELATORIOGERENCIALESTORNO

Define se deve ser emitido o comprovante de estorno de recebimento.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não imprime |
| 1 | Imprime (valor **Padrão**) |

#### CONTASRECEBER.INFORMACOESOFFLINE

Define quais informações, no formato lista, serão solicitadas ou exigidas para efetuar o recebimento de títulos off-line, considerando:

* 0 - Não solicita informação;
* 1 - Solicita informação como opcional;
* 2 - Obriga informação.

É necessário o parâmetro dinâmico ContasReceber.ReceberOffline estar configurado com o valor **1**.

| Código | Descrição | Valor Padrão |
| --- | --- | --- |
| 1 | Localizador | 2 |
| 2 | Valor | 2 |
| 3 | Vencimento | 1 |
| 4 | CPF/CNPJ do cliente | 2 |
| 5 | Código do cliente | 1 |
| 6 | Nome do cliente | 2 |
| 7 | Telefone do cliente | 2 |
| 8 | Documento fiscal | 1 |
| 9 | Informações gerais | 1 |

Importante

O campo Valor é considerado como Obrigatório (opção 2), independentemente da configuração.

## Exemplo:

Configuração:

2,2,1,2,1,2,2,1,1

* 2: Localizador, obrigatório
* 2: Valor, obrigatório
* 1: Vencimento, opcional
* 2: CPF/CNPJ, obrigatório
* 1: Código, opcional. Exibido somente se habilitado conforme REQ0012.
* 2: Nome, obrigatório
* 2: Telefone, obrigatório
* 1: Documento fiscal, opcional
* 1: Informações gerais, opcional

#### CONTASRECEBER.INFORMADATARECEBIMENTO

Define se o operador poderá informar a data de recebimento do título.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não permite (valor **Padrão**) |
| 1 | Permite |

#### CONTASRECEBER.PERMITE.ESTORNARTITULOBAIXADO.PDV

Define se será permitido estornar títulos que foram baixados no PDV via Retaguarda, no Gestão de Lojas

| Valor (Lista) | Descrição |
| --- | --- |
| N | Desabilitado (valor **Padrão**) |
| S | Habilitado |

.

#### CONTASRECEBER.PRAZOESTORNO

Define qual o prazo máximo disponível, em dias (D) ou horas (H) e seguido do valor, no formato texto, para realizar estorno de recebimento de título.

Valor **Padrão**: D1

## Exemplo:

O primeiro dígito indica o tipo de período e os restantes o tempo:

* D1 - Nesse caso significa 1 dia;
* H12 - 12 horas.

#### CONTASRECEBER.QUANTIDADEVIASRELATORIOGERENCIAL

Define a quantidade, no formato inteiro, de vias do comprovante de recebimento.

Valor **Padrão**: 1

#### CONTASRECEBER.QUANTIDADEVIASRELATORIOGERENCIALESTORNO

Define a quantidade de vias do comprovante de estorno.

Valor **Padrão**: 1

#### CONTASRECEBER.RECEBEROFFLINE

Habilita função para recebimento de título off-line.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não habilitado (valor **Padrão**) |
| 1 | Habilitado |

#### CONTASRECEBER.RECEBETITULOFORASEQUENCIA

Indica se o sistema permite selecionar títulos fora da sequência.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não permite receber títulos fora da sequência |
| 1 | Permite receber títulos fora da sequência (qualquer título, desde que não esteja bloqueado) (valor **Padrão**) |
| 2 | Permite receber títulos fora da sequência, caso todos os títulos anteriores estejam bloqueados |

#### CONTASRECEBER.TIPOIMPRESSAORECIBO

Define quais informações serão impressas no recibo de um recebimento.

| Valor (Lista) | Descrição |
| --- | --- |
| 1 | Recibo dos Documento Recebidos: Identifica os títulos recebidos (valor **Padrão**) |
| 2 | Recibo de Pagamento/Carnê: Imprime todas as parcelas referentes à venda do título sendo baixado e também imprime o localizador da próxima parcela |

## Exemplo:

Recibo dos Documento Recebidos - Identifica os títulos recebidos:

![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/imagens/1_emulador_impfiscal_thumb_0_48.png)

Recibo de Pagamento/Carnê - Imprime todas as parcelas referentes à venda do título sendo baixado e também imprime o localizador da próxima parcela:

![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/imagens/2_emulador_impfiscal.png)

#### CONTASRECEBER.VALORDESCONTOAUTOMATICO

Define um valor, no formato moeda, para quitar o título, caso o pagamento tenha sido realizado parcialmente.

Valor **Padrão**: 0,00

## Exemplo:

Titulo 1, Valor: 100,02. Pagamento efetuado: 100,00.

Se a configuração descrita estiver configurada com o valor 0,03 (três centavos), como faltou pagar 2 centavos, nesse caso o título seria quitado e os centavos faltantes seriam registrados como desconto.

#### CONTASRECEBER.VALORMINIMORECEBIMENTOPARCIAL

Define o valor mínimo para efetuar recebimento parcial.

| Valor (Moeda) | Descrição |
| --- | --- |
| 0 | Sem limite, ou seja, sem valor mínimo (valor **Padrão**) |
| Qualquer outro valor | Determina um valor mínimo |

#### CONTRATOCOMPRA.APROVACAO.OBRIGAROBSERVACAO

Define se deve ou não obrigar a informar a observação na aprovação multinível do contrato, caso esteja habilitado será solicitada a observação no cancelar e aprovar da tela Aprovações Multinível do Contrato de Compra (F460APR).

| Valor (Lista) | Descrição |
| --- | --- |
| N | Desabilitado (valor **Padrão**) |
| S | Habilitado |

#### CONTRATOVENDA.DATABASE.QTDDIAS

Caso preenchido, sugere quantos dias, no formato número, serão somados ao campo **Data Base Parcelas**, ao abrir a tela de Contratos de venda, do Retaguarda.

Valor **Padrão**: 0

#### CONTRATOVENDA.PRIMEIRA.PARCELA.QTDDIAS

Determina a quantidade de dias entre a data base e a primeira parcela na tela de Contratos de venda, do Retaguarda. Se estiver vazio, pula um mês. Se estiver preenchido, pula . Caso preenchido com **0**, .

| Valor (Numérico) | Descrição |
| --- | --- |
| 0 | a primeira parcela ficará igual a data base |
| Qualquer outro valor diferente de 0 | Pula exatamente a quantidade de dias informada |
| (vazio) | Pula um mês (valor **Padrão**) |

#### CONTRATOVENDA.QTDPARCELAS

Caso preenchido, no formato número, sugere o campo **Qtd Parcelas** ao abrir a tela de Contratos de venda, do Retaguarda.

Valor **Padrão**: 0

#### CONTRATOVENDA.QTDPARCELAS.HABILITADO

Caso preenchido com **0**, o campo **Qtd Parcelas** ficará desabilitado na tela de Contratos de venda, do Retaguarda. Nesse caso, é necessário utilizar em conjunto do parâmetro FILIAL.CONTRATOVENDA.QTDPARCELAS para que o número sugerido de parcelas não seja **0**.

| Valor | Descrição |
| --- | --- |
| 0 | Não |
| 1 | Sim (valor **Padrão**) |

#### CONTRATOVENDA.TIPO

Caso preenchido, sugere o campo **Tipo** ao abrir a tela de Contratos de venda, do Retaguarda.

| Valor | Descrição |
| --- | --- |
| 1 | Consórcio |
| 2 | Seguro |
| 3 | Empréstimo Pessoa Física |
| 4 | Empréstimo Consignado |
| (vazio) | Manter campo Valor vazio (valor **Padrão**) |

#### ControleVerba.MotivoDevolucao

Indica um motivo padrão para devolução. Deve ser informado o código da natureza de gasto associada ao motivo padrão. Caso o código seja inválido, esta configuração será ignorada.

Valor **Padrão**: vazio. Ao efetuar uma devolução e este parâmetro possuir valor, este será utilizado como motivo no título gerado para esta devolução.

#### ControleVerba.MotivoPadrao

Indica um motivo padrão para devolução. Deve ser informado o código da natureza de gasto associada ao motivo padrão. Caso o código seja inválido, esta configuração será ignorada.

Valor **Padrão**: vazio

#### CORRESPONDENTEBANCARIO.MOTIVOLANCAMENTO

Define o motivo, no formato Inteiro, a ser considerado nos movimentos de tesouraria gerados a partir da realização de operações de correspondente bancário. O motivo é utilizado para obter a natureza de gasto do lançamento. Por exemplo: 0, 1, 2, 3, 4.

O número informado para o parâmetro deve ser de acordo com o motivo desejado cadastrado em Cadastros > Identificadores e parâmetros > Motivo de situações/observações (F021MOT).

Valor **Padrão**: 0.

#### CREDENCIAMENTOPAF.PORTA.CONSULTA

Indica a porta do servidor, no formato String, que será consultado o número de credenciamento na Senior.

#### CREDENCIAMENTOPAF.SERVER.CONSULTA

Indica o nome do servidor, no formato String, que será consultado o número de credenciamento na Senior.

#### DANFE.IMPRIMEVENDEDOR

Determine a impressão do vendedor nas notas de saída.

| Valor (Inteiro) | Descrição |
| --- | --- |
| 0 | Não verá impresso o vendedor (valor **Padrão**) |
| 1 | Imprime o vendedor nas notas de saída (área de informações do contribuinte). Caso haja mais de um vendedor, o sistema limitará o nome do vendedor em 20 caracteres (devido à questão de espaço). |

#### DEVOLUCAO.VOUCHERTROCA.IMPRIMIR

Habilita a impressão de Voucher de Troca.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não (valor **Padrão**) |
| 1 | Sim |

#### DEVOLUCAO.VOUCHERTROCA.VALIDADE

Define a quantidade de dias, no formato número, corridos que o voucher será válido, a partir da data da devolução do produto.

Valor **Padrão**: 1

#### DEVOLUCAOTROCA.BAIXA.VALOR.ENTREGA

Indica se o valor referente ao frete é baixado ao efetuar uma devolução de venda.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Desabilitado O valor da entrega é sempre incluído no título a pagar gerado na devolução de venda (valor **Padrão**) |
| 1 | Habilitado. Caso a remessa tenha sido emitida o valor referente a entrega não é incluído no título a pagar gerado na devolução de venda |

#### DEVOLUCAOTROCA.BLOQUEARPROMOCIONAL

Define se a filial bloqueia a devolução de itens vendidos com preço promocional (itens vendidos com tabela de preço de Tablóide ou de Promoção).

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não (valor **Padrão**) |
| 1 | Sim |

#### DEVOLUCAOTROCA.DEVOLUCAOSOMENTECREDIARIO

Define um processo específico de Devolução/Troca, no qual:

* Se nos pagamentos da venda foi usado Crediário, habilita a opção Devolução (checada por padrão), e também solicita confirmação ao concluir a operação;
* Se não, permite realizar somente o processo de Troca.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Desligado (valor **Padrão**) |
| 1 | Ligado |

Observação

Com este parâmetro habilitado, o parâmetro dinâmico DevolucaoTroca.ProcessoPadrao é ignorado pelo sistema.

#### DEVOLUCAOTROCA.FORMAPAGAMENTO

Define a forma de pagamento atribuída a uma Devolução/Troca.

Os valores possíveis para esse parâmetro são os mesmos das formas de pagamento do Gestão Empresarial | ERP.

Valor **Padrão**: vazio.

#### DEVOLUCAOTROCA.IMPRIME.COMPROVANTE

Define que após realizar uma devolução ou troca será impresso o comprovante da operação realizada.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Desabilitado |
| 1 | Habilitado (valor **Padrão**) |

#### DEVOLUCAOTROCA.PORTADORPADRAOTITULOSTROCA

Define o Código de Referência do portador padrão, no formato texto, a ser utilizado ao gerar títulos de troca, no processo de Devolução/Troca.

Valor **Padrão**: vazio.

#### DEVOLUCAOTROCA.PROCESSOPADRAO

Define a forma padrão que a tela de Devolução ou Troca será exibida ao ser acessada.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Devolução |
| 1 | Troca |
| 2 | Recuperação de mercadoria |

#### DEVOLUCAOTROCA.PROCESSOS\_DISPONIVEIS

Define os processos que estarão disponíveis para seleção na tela de Devolução/Troca.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Ambos (valor **Padrão**) |
| 1 | Somente Devolução |
| 2 | Somente Troca |

#### ECF .DATATERMINOHORARIOVERAO

Data de término do horário de verão.

#### ECF.CONTROLASTATUSPAPEL

Habilita recurso para exibir status do papel no ECF.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não |
| 1 | Sim (valor **Padrão**) |

#### ECF.DATAINICIOHORARIOVERAO

Data de início do horário de verão.

#### ECF.EXIGECONFIRMACAOREDUCAOZ

Exige confirmação para realizar redução Z.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não (valor **Padrão**) |
| 1 | Sim |

#### ECF.PICOTAPAPEL

Habilita o picote do papel em relatório gerencial e cupom vinculado.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não habilita e avança o comprovante (valor **Padrão**) |
| 1 | Sim |

#### EDOCS.CLIENTE.PORTA

Porta, no formato numérico, em que está publicado o serviço de web services do eDocs Cliente.

Valor **Padrão**: 8989.

#### EDOCS.CLIENTE.SENHA

Senha, no formato alfanumérico, para conexão com o serviço de web services do eDocs Cliente.

#### EDOCS.CLIENTE.URL

URL, no formato alfanumérico, em que está publicado o serviço de web services do eDocs Cliente (que é um pré-requisito para venda com SAT). Por exemplo: http://127.0.0.1.

#### EDOCS.CLIENTE.USUARIO

Usuário, no formato alfanumérico, para conexão com o serviço de web services do eDocs Cliente.

#### ENTREGA.CONFIRMAR.PENDENTES.APOS.DIAS

Define a quantidade, em dias, que o Retaguarda irá aguardar antes que o status da entrega seja alterada de **Saiu para entrega** para **Entregue** automaticamente.

| Valor | Descrição |
| --- | --- |
| 0 | Não executa a rotina (valor **Padrão**) |
| Qualquer valor diferente de zero | Representará a quantidade em dias para a rotina executar |

## Exemplo:

Definindo o valor para 10 dias, o sistema verifica uma vez por dia se existe alguma entrega com o status **Saiu para entrega** há 10 dias. Caso exista, essas entregas terão seu status definidos para **Entregue**.

#### Entrega.PermiteCancelarControle

Indica se o botão Cancelar Entrega (F9), da tela Controles de Entrega do Retaguarda, estará disponível.

| Valor | Descrição |
| --- | --- |
| S | Sim |
| N | Não (valor **Padrão**) |

Observação

A rotina de devolução cancela automaticamente as entregas vinculadas ao produto devolvido. Caso o cancelamento do controle de entrega seja realizado manualmente, não será possível realizar posteriormente a devolução do produto vinculado a entrega cancelada.

#### ESTOQUE.HABILITAR.CONSISTENCIA

Deixa de efetuar consistência de saldo de estoque ao efetivar movimento.

| Valor | Descrição |
| --- | --- |
| 0 | Não |
| 1 | Sim (valor **Padrão**) |

#### FILIAL.ANALISEEMBARQUE.NOVONUMEROPOREXECUCAO

Indica se, a cada vez que a porta AtenderManualPedidos do web service com.senior.g5.co.mcm.ven.manualpedidos for executada, deve gerar um novo número de análise de embarque.
Se estiver definido como "N - Não", que é o valor padrão, será mantido o comportamento original, ou seja, reutilizará uma análise já existente, gerando apenas uma nova pré-fatura.

| Valor (Lista) | Descrição |
| --- | --- |
| N | Não (valor **Padrão**) |
| S | Sim |

#### FILIAL.CUPOM.LOTE

Com este parâmetro cadastrado permite que a integração de cupom fiscal utilizando o web service Com.senior.g5.co.int.varejo.NotaAutorizada porta ImportarNotaAutorizada execute algum identificadores de regra de sugestão de lote, que irão sobrepor o lote da requisição estando vazio ou mesmo informado.

Permite a entrada de um lote fictício que será sobrescrito pela sugestão de regra e caso não seja, será utilizado em mensagens de retorno facilitando a localização de eventuais consistências.

**Importante**

1. Os identificadores que podem ser executados e sua ordem de prioridade em uma hipótese de todos estarem cadastrados:
   1. VEN-140CFILE01
   2. VEN-140EUDLE02
   3. GER-140EUDLE01
   4. GER-210EUDLE01
2. O código de lote que virá do webservice ou do parâmetro dinâmico será utilizado para compor mensagens em que não encontra lote disponível, ou seja, pode indicar a falta de estoque de maneira implícita. Uma sugestão de um código lote para o parâmetro dinâmico seria uma indicação textual de falta de estoque.

**Valor Padrão:** Lote fictício de fácil identificação usado para eventuais mensagens.

#### FILIAL.FIS.SERIELEGALINTEGRACAOFIS

Para indicar se a série legal deve ser encaminhada para o FIS.

Valor Padrão: N.

| Valor (Lista) | Descrição |
| --- | --- |
| S | Envia a série fiscal |
| N | Envia o código da série (CODSNF) |

#### FILIAL.INTWMS.CFOPRECEBIMENTO

Indica a CFOP padrão que deve ser enviada ao Gestão de Armazenagem em solicitações de alocação de mercadoria. No Gestão de Armazenagem essa informação é obrigatória, e em virtude de nos apontamentos de produção não ter um documento fiscal com uma CFOP, esse parâmetro será utilizado.

Deve ser uma CFOP atrelada à uma transação no Gestão Empresarial, para que seja possível buscar a sua descrição.

#### FILIAL.INTWMS.BLOQUEIAORDEMANTESAUTORIZACAO

**Valores**: S - Sim | N - Não

**Padrão**: N

Impede a geração da ordem de separação no WMS durante o fechamento de NF-e de devolução, quando o documento de separação (DocSep) estiver configurado como **1 - Carga/Pré-fatura**, na integração com o WMS WIS.

Quando parametrizado como **S - Sim**, a ordem de separação não é gerada automaticamente e deve ser criada manualmente pela tela F000GOW, somente após a autorização da nota pela SEFAZ.

#### FILIAL.INTWMS.CFOPSEPARACAO

Indica a CFOP padrão que deve ser enviada ao Gestão de Armazenagem em solicitações de separação de mercadoria. No Gestão de Armazenagem essa informação é obrigatória, e em virtude de não existir um documento fiscal que tenha uma CFOP, esse parâmetro será utilizado.

Deve ser uma CFOP atrelada à uma transação no Gestão Empresarial, para que seja possível buscar a sua descrição.

#### FILIAL.INTWMS.CNPJDEPOSITANTEFILIAL

Indica qual o CNPJ deverá ser enviado ao WMS nos pacotes de integração no campo **cnpjFilialEmitente**.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | CNPJ do Cadastro da filial |
| 1 | CNPJ Configurado nos parâmetros de integração (F185CFG) |

Valor **Padrão**: 0.

#### FILIAL.INTWMS.DEPOSITODIVERGENCIATRANSFERENCIAWMS

Define o código do depósito virtual para receber a quantidade a menor em transferências entre produtos na integração com o WMS WIS.

**Importante**

O depósito informado deve atender aos seguintes requisitos:

* Ser do tipo depósito Virtual;
* Não integrar com o WMS;
* Possuir ligação ativa com o produto.

#### FILIAL.INTWMS.HERDADATAEMISSAOPEDIDO

Indica se ao gerar uma pré-fatura via pedido, ele irá herdar a data de emissão do pedido ao exportar a pré-fatura para o WMS.

* a pré-fatura no Gestão Empresarial | ERP permanecerá com a data de emissão de quando ela foi gerada, esse parâmetro serve somente para manipular a data de emissão enviada ao WMS;
* no caso de pedido agrupado, quando do mesmo cliente, a rotina irá considerar a data de emissão do pedido mais antigo.

Valor **Padrão**: N

#### FILIAL.INTWMS.INTEGRARDADOSAUTORIZACAOSEFAZ

Indica se deve enviar as tags **ProtocoloNfe** e **DataRecebimentoNfe** para o WMS Silt.

| Valor | Descrição |
| --- | --- |
| S | Envia as informações |
| N | Valor padrão. Não envia as informações |

#### FILIAL.INTWMS.INTEGRARDADOSZPLFATURAMENTO

Indica se deve enviar os dados referentes à ZPL na integração, realizado após o faturamento.

* **Valores:** N - Não; S - Sim
* **Padrão:** N

#### FILIAL.INTWMS.INTEGRARROTANAPREFATURA

Indica a integração do código e descrição da rota na pré-fatura para o WMS WIS.

Valor **Padrão**: N

#### FILIAL.INTWMS.MANTERMOVIMENTORETORNOOR

Controla os movimentos de estoque no retorno da conferência de uma nota fiscal de entrada.

**Características:** No processo comum, ao retornar a conferência, são excluídas todas as movimentações para gerar novas conforme as informações retornadas do WMS. Com o parâmetro ativo, no retorno, em vez de excluir todos os movimentos, o estoque é ajustado com novos movimentos, sem alterar os anteriores. Isso permite conferir uma nota que teve retorno apenas após o fechamento do período de estoque no ERP.

Valor **Padrão**: N.

Observação

Este parâmetro é incompatível quando, na transação de estoque da nota fiscal de entrada, o campo Transação Transferência estiver configurado com uma transação de transferência, conforme definido na tela F001TES. Se, nessa configuração, a transação de transferência possuir um depósito padrão informado no campo Depósito Padrão, ocorrerá a incompatibilidade.

#### FILIAL.INTWMS.GERARDEVOLUCAOCANCELANETOREJEITADO

Indica que, caso o cancelamento de uma nota fiscal de saída seja rejeitado, uma nota de devolução deve ser gerada automaticamente.

**Características:** Quando o parâmetro estiver ativo, se o cancelamento for rejeitado pela Sefaz, o sistema gerará automaticamente uma nota fiscal de entrada do tipo "3 - Devolução", a qual não será integrada ao WMS, dispensando qualquer intervenção manual.

Valor **Padrão**: N

#### FILIAL.INTWMS.SERIEPADRAOPRODUCAOEXTERNA

Indica em qual série será gerada a nota fiscal para produção externa.

Observação

Para produção interna, a série será OSM.

#### FILIAL.INTWMS.TIPOPEDIDOPRODUCAOEXTERNA

Indica qual o tipo de pedido padrão deve ser enviado ao Gestão de Armazenagem para indicar uma separação externa. O tipo de pedido não é obrigatório para o Gestão de Armazenagem, porém se desejar que ele entre no fluxo que indica o abastecimento externo, o tipo deve ser informado.

Este tipo de pedido pode ser indicado, além do parâmetro dinâmico, em dois identificadores de regra:

* GER - 000INWMS01: executado antes de gravar a ordem de separação, que é executado para todos os tipos de separação feitos no Gestão Empresarial;
* GER- 000INWMS18: na tela de solicitação de componentes é possível indicar o tipo de pedido.

#### FILIAL.INTWMS.TIPOPEDIDOPRODUCAOINTERNA

Indica qual o tipo de pedido padrão deve ser enviado ao Gestão de Armazenagem para indicar uma separação interna. O tipo de pedido não é obrigatório para o Gestão de Armazenagem, porém se desejar que ele entre no fluxo que indica o abastecimento interno, o tipo deve ser informado.

Este tipo de pedido pode ser indicado, além do parâmetro dinâmico, em dois identificadores de regra:

* GER - 000INWMS01: executado antes de gravar a ordem de separação, que é executado para todos os tipos de separação feitos no Gestão Empresarial;
* GER- 000INWMS18: na tela de solicitação de componentes é possível indicar o tipo de pedido.

#### FILIAL.INTWMS.TIPRECPADRAOPRODUCAOINTERNA

Indica o tipo de recebimento padrão que deve ser enviado ao Gestão de Armazenagem para indicar um recebimento interno para manufatura.

Cadastrar o tipo CONFERENCIA\_INTERNA para enviar as informações do lote ao Gestão de Armazenagem e realizar o processo de conferência de forma automática.

#### FILIAL.INTWMS.TIPRECPADRAOPRODUCAOEXTERNA

Indica o tipo de recebimento padrão que deve ser enviado ao Gestão de Armazenagem para indicar um recebimento externo para manufatura.

#### FILIAL.INTWMS.TRANSACAOCABECALHOPARAITENS

Indica se ao gerar uma pré-fatura via pedido irá herdar a transação do cabeçalho para os itens.

Valor **Padrão**: N

#### FILIAL.INTWMS.TRANSPORTADORAPADRAO

Define o código da transportadora padrão para integração de ordem de recebimento e ordem de separação com WMS, para documentos sem transportadora.

Valor **Padrão**: 0.

#### FILIAL.PRIORIZARTABELAPRECOPADRAO

Indica qual deverá ser a Tabela de Preço padrão que será utilizada para fornecimento de valores de produtos para o vendedor, considerando que:

* Quando configurado com o valor **0**, será utilizado o funcionamento atual de sugestão de tabela de preço, em que o sistema de loja obterá a tabela de preço com data de início de validade mais próxima do dia atual. Já quando configurado com o valor **1**, o sistema de loja obterá a tabela de preço padrão cadastrada na tela F070VAR.   

  Serão consideradas as validades que estejam vigentes, que estejam ativas, que contenham o produto que está sendo vendido e que ele esteja ativo. Será priorizada a validade com data de início mais próxima do dia atual. Caso a tabela de preço padrão esteja inativa ou não exista uma validade que atenda as premissas citadas, o sistema irá considerar como se o parâmetro estivesse com **0**.
* Caso o parâmetro exista e esteja configurado com o valor **1**, será verificado qual é o código da Tabela de Preço Padrão cadastrado. Quando o código de tabela de preço for recebido do Gestão Empresarial | ERP pelo sistema de Gestão de Lojas, será verificado se há tabela de preço está ativa, com o item ativo e ainda, se esta tabela de preço está na validade, pegando a que contenha a data de início de validade que seja a mais próxima do dia atual.   

  Se todas estas condições forem atendidas então será utilizada para fornecimento de preço a tabela de preço padrão cadastrada no ERP, do contrário, será utilizada a tabela que atenda as premissas citadas anteriormente.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não (valor **Padrão**). |
| 1 | Sim |

#### FILIAL.INVENTARIOERP

Permite que um depósito de uma filial varejo, tenha seu inventário inicializado pelo ERP (caso contrário, só pode ser feito pelo sistema de varejo da filial).

**Valor padrão:** 0

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não permite realizar o inventário. |
| 1 | Permite realizar o inventário. |

#### FINANCEIRO.TIPO.ARREDONDAMENTO.PARCELAS.CARTAO

Define o tipo de arredondamento que será utilizado na geração de parcelas de pagamentos por cartões.

Valor Padrão: 0

| Valor | Descrição |
| --- | --- |
| 0 | Arredondamento padrão |
| 1 | Arredondamento forçando o desconto da taxa para cima e descontando a diferença da primeira/última parcela |

## Exemplo

Total: 340,00 Taxa: 1,99

Parâmetro igual a 0

Parcela 1: 170,01 (valor 166,62 + desc taxa 3,39)

Parcela 2: 169,99 (valor 166,61 + desc taxa 3,38)

Parâmetro igual a 1

Parcela 1: 170,00 (valor 166,62 + desc taxa 3,38)

Parcela 2: 170,00 (valor 166,61 + desc taxa 3,39)

#### FISCAL.NFCE.HABILITAR.ENVIO.TAG.CONSUMIDOR

Define se enviará o CPF do cliente à Sefaz ao final da venda no PDV NFC-e.

| Valor | Descrição |
| --- | --- |
| 0 | Não envia o CPF do cliente (mesmo se for informado na venda). |
| 1 | Sempre envia o CPF do cliente (valor **Padrão**). |
| 2 | Pergunta, a cada venda, se deseja enviar o CPF do cliente/consumidor. |

#### FISCAL.NFCE.HABILITAR.ENVIO.TAG.INTERMEDIADOR

Indicativo se deve enviar a tag `indItermed` no XML da NFC-e.

| Valor | Descrição |
| --- | --- |
| S | Envia a tag no XML |
| N | Não envia a tag no XML (valor **Padrão**) |

#### FISCAL.NFE.HABILITAR.ENVIO.TAG.INTERMEDIADOR

Indicativo se deve enviar a tag `indItermed` no XML da NFE.

| Valor | Descrição |
| --- | --- |
| S | Envia a tag no XML |
| N | Não envia a tag no XML (valor **Padrão**) |

#### HABILITAR.ATO.DIAT.79.2022

Criado para atender a legislação do Ato DIAT 79/2022 em Santa Catarina, indica se o sistema deverá realizar os cálculos adicionais de ICMS desonerado.

| Valor | Descrição |
| --- | --- |
| S | Habilitado |
| N | Desabilitado (valor **Padrão**) |

#### HABILITAR.BLOQUEIO.CPF.ENDERECO

Define se deve alterar o comportamento da rotina para automatizar preenchimento de alguns dados no cadastro de endereços de entrega.

| Valor (Texto) | Descrição |
| --- | --- |
| N | Não habilita |
| S | Habilita |

#### HABILITAR.EXPORTAR.CBENEF

Define se a aplicação deve buscar o cBenef (Código de Benefício Fiscal) de outro local além da tabela onde estão contidas as informações fiscais.

| Valor | Descrição |
| --- | --- |
| S | Habilita |
| N | Não habilita (valor **Padrão**). |

#### HABILITAR.NT2021.004

Adequa, à nota técnica 2021.004, os processos e rotinas do sistema Gestão de Lojas.

| Valor | Descrição |
| --- | --- |
| S | Ativa as adequações realizadas para atender a nota técnica 2021.004 |
| N | Desativa as adequações realizadas para atender a nota técnica 2021.004 (valor **Padrão**). |

#### HABILITAR.NT2022.003

Adequa o Gestão de Lojas à nota técnica 2022.003, definindo se deve alterar o comportamento da tag <refNFe> para a <refNFeSig> no arquivo XML.

| Valor | Descrição |
| --- | --- |
| S | Ativa as adequações realizadas para atender a nota técnica, substituindo a tag <refNFe> pela tag <refNFeSig>, que omite os 8 últimos dígitos da chave referenciada na nota fiscal. |
| N | Desativa as adequações realizadas para atender a nota técnica (valor **Padrão**). |

#### HABILITAR.TELA.LOTE

Define se deve habilitar a tela de consulta de lotes.

| Valor | Descrição |
| --- | --- |
| N | Não habilita a tela (valor **Padrão**). |
| S | Habilita a tela |

#### INT.AGR.PESAGEM.CHAMARVEICULOMANUALMENTE

Indica se o usuário pode enviar a placa ao Gestão de Pátio | YMS para que o veículo seja liberado manualmente, sem uma primeira tentativa de reconhecimento de placa.

| Valor (Lista) | Descrição |
| --- | --- |
| H | Habilita liberação manual após não ter sucesso em ao menos uma tentativa de captura automática pelo LPR (Indicado para utilizar quando o LPR permanece bloqueado. (valor **Padrão**) |
| N | Não é permitido liberar manualmente. |
| P | Permitido liberar manualmente a qualquer momento. (Indicado para utilizar quando o LPR permanece desbloqueado. |

#### LAYOUT.REIMPRESSAO.CARNE

Identifica o layout que será utilizado para a reimpressão do carnê no PDV.

| Valor | Descrição |
| --- | --- |
| 1 | Layout com código localizador e código de barras (valor **Padrão**) |
| 2 | Layout sem localizador e código de barras |

#### LOG.NFS.TIT.CRE.140CNFEC01

Indicativo se o log será acionado no início do processo de fechamento das notas fiscais de saída, antes
da geração dos títulos.

| Valor (Inteiro) | Descrição |
| --- | --- |
| S | Sim |
| N | Não (valor **Padrão**) |

#### LOG.NFS.TIT.CRE.140CNFEC02

Indicativo se o log será acionado no final do processo de fechamento das notas fiscais de saída.

| Valor (Inteiro) | Descrição |
| --- | --- |
| S | Sim |
| N | Não (valor **Padrão**) |

#### LOG.NFS.TIT.CRE.140CNFEC03

Indicativo se o log será acionado após o fechamento da nota fiscal, depois da gravação dos dados da
nota fiscal no banco de dados.

| Valor (Inteiro) | Descrição |
| --- | --- |
| S | Sim |
| N | Não (valor **Padrão**) |

#### LOG.NFS.TIT.CRE.EMISSAO

Indicativo se o log será acionado após a emissão da nota fiscal de saída.

| Valor (Inteiro) | Descrição |
| --- | --- |
| S | Sim |
| N | Não (valor **Padrão**) |

#### LOG.NFS.TIT.CRE.GERAR

Indicativo se o log será acionado após a geração de títulos do contas a receber nas Notas Fiscais de
Saída.

| Valor (Inteiro) | Descrição |
| --- | --- |
| S | Sim |
| N | Não (valor **Padrão**) |

#### NFCE.PRAZO.CANCELAMENTO

Permite o cancelamento (prazo em horas) de uma NFC-e, após ela ter sido autorizada pela SEFAZ.

Valor **Padrão**: 0.5 (representando 30 minutos).

#### NFE.HABILITAR.NT2018

Ativa as Notas Técnicas 2018.004 e 2018.005.

| Valor | Descrição |
| --- | --- |
| 0 | Não (valor **Padrão**) |
| 1 | Sim |

#### NOTA.PRAZO.CANCELAMENTO.SUBSTITUICAO

Permite o cancelamento (prazo em horas) de uma nota fiscal eletrônica por substituição e efetuar o cancelamento de uma NFC-e enviada para a SEFAZ que não foi obtido retorno, onde a próxima nota será uma nota idêntica à nota anterior enviada em contingência.

Valor **Padrão**: 168 (7 dias).

#### NOTACUPOM.GERARTAGCOBRANCAXMLNFE

Define se as tags de cobrança deverão ser geradas no XML das notas de cupom geradas a partir de cupons fiscais e, posteriormente, autorizadas na SEFAZ.

| Valor | Descrição |
| --- | --- |
| S | Habilitado |
| N | Não habilitado (valor **Padrão**) |

Observação

As notas de cupom originadas de cupons fiscais que possuem itens de intermediação não serão autorizados na SEFAZ, pois na nota fiscal de cupom não são considerados itens de serviço e os dados da cobrança são preenchidos com o valor total faturado no cupom, causando divergência de valores entre o total de produtos e o valor informado nas parcelas.

#### NOTAFISCAL.DIAS.REMOVER.EM.DIGITACAO

Utilizado para estabelecer um número de dias que as Notas Fiscais de Saída com a situação "Em digitação", e que não foram enviadas à SEFAZ, ficarão disponíveis. Ao completar o número de dias configurado no parâmetro, a Nota Fiscal de Saída será removida.

| Valor | Descrição |
| --- | --- |
| 0 | Desabilitado (valor **Padrão**) |
| Qualquer outro valor | Número de dias que a Nota Fiscal de Saída ficará disponível. |

#### NOTAFISCAL.ICMSDIFERIDO.REMOVERDOPRECOUNITARIO

Utilizado para indicar se, ao incluir um item em uma nota fiscal, deve ser removido o valor do ICMS diferido do valor unitário do produto. Sendo obrigatório informar uma tabela de preço para a operação ser efetuada. Para a nota fiscal de saída, é possível também efetuar o cálculo utilizando um pedido de venda.

| Valor | Descrição |
| --- | --- |
| S | Subtrai o valor do ICMS diferido do valor unitário do produto |
| N | Não subtrai o valor do ICMS diferido do valor unitário do produto (Valor **Padrão**) |

#### NOTAFISCAL.INUTILIZACAO.PRODUTORRURAL

Quando informado "S", permite empresas tipo "7 - Produtor rural" e com CPF (pessoa física), inutilizar notas fiscais de saída.

Valor **Padrão**: "N"

**Observação**

Esta funcionalidade está disponível apenas para o estado do Mato Grosso (MT).

#### NOTAFISCAL.MENSAGEM.SEM.FCP

Parâmetro utilizado para definir se as notas fiscais devem apresentar uma mensagem informativa quando não há cobrança de FCP.

| Valor | Descrição |
| --- | --- |
| N | Não (valor **Padrão**) |
| S | Sim |

#### NOTAFISCAL.TRANSFERENCIA.INTEGRAR.PARCELAS

Indicar se as parcelas enviadas na nota de transferência entre filiais devem integrar.

| Valor | Descrição |
| --- | --- |
| N | Desabilitado (valor **Padrão**) |
| S | Habilitado |

#### NOTAFISCAL.XML.FORMADEPAGAMENTOPADRAO

A função deste parâmetro é definir qual forma de pagamento irá para o XML na geração de NF-e/NFC-e, caso a parcela não possua forma de pagamento definida.

Para o Gestão de Lojas, ao emitir uma NF-e/NFC-e no sistema, utilizando uma forma de pagamento não esperada pela SEFAZ, será enviado no XML a forma "99 - Outros". Desta forma, será feito o envio obrigatório de uma descrição desta forma de pagamento não esperada pela SEFAZ, e o Gestão de Lojas utilizará a descrição da forma de pagamento informada neste parâmetro dinâmico

## Exemplo:

Quando utilizada a forma de pagamento "Acerto" e neste parâmetro dinâmico informado o código "1" (Dinheiro), a SEFAZ não irá esperar a forma de pagamento "Acerto". Neste caso, o Gestão de Lojas enviará no XML da NF-e ou NFC-e a forma de pagamento "99 - Outros" na tag **tPag** com a descrição "Dinheiro" na tag **xPag**.

Valor **Padrão**: 1 - Dinheiro.

#### NOTAFISCAL.XML.ICMS.MONOFASICO.DIFERIMENTO.GERAVICMSMONO

Indica se, na geração do .XML, produtos com tipo de combustível e situação tributária de ICMS 53 (Tributação monofásica sobre combustíveis com recolhimento diferido) vão gerar a tag **vICMSMono** (Valor do ICMS próprio) do Grupo N07a - Grupo Tributação do ICMS= 53, mesmo se ocorrer o diferimento total do ICMS Monofásico.

| Valor | Descrição |
| --- | --- |
| N | Não vai emitir a tag **vICMSMono** quando o valor for 0 (padrão) |
| S | Vai emitir a tag **vICMSMono** quando o valor for 0 |

#### OPERACAOPDV.REPROCESSAR

Define a frequência da rotina de reenvio automático das notificações de erros das operação do PDV, Matriz e Filial. Caso não for informado um valor, o sistema, por padrão, reprocessará em 120 minutos. Se desejar não utilizar a rotina, informe o valor 0 (zero).

Valor **Padrão**: 120.

#### ORDEMCOMPRA.EXIBEESTOQUETRANSITO

Define se o Retaguarda irá exibir ou não a posição de estoque "Em transito" e "Ordem de compra" no grade de geração de ordem de compra. Quando o parâmetro estiver com o valor "1 - Sim", os campos Quant. Ordem e Quant. Trânsito serão apresentados nesta grade.

| Valor | Descrição |
| --- | --- |
| 0 | Não (valor **Padrão**) |
| 1 | Sim |

#### ORDEMCOMPRA.PERIODO.QUANTIDADEVENDA

Define o período, em meses, no qual será utilizado para buscar as últimas vendas do item adicionado na Ordem de Compras.

Valor **Padrão**: 3

#### PEDIDO.EXPIRAR.FINALIZADOS.COM.ANALISE.DE.CREDITO

Define o tempo, em minutos, que o Retaguarda irá aguardar para expirar um pedido com análise de crédito.

| Valor | Descrição |
| --- | --- |
| (vazio) | Não expira o pedido (valor **Padrão**) |
| Valores maiores que zero | O Retaguarda irá aguardar para expirar um pedido com análise de crédito. |

#### PEDIDO.FORMAPAGAMENTO.ORDENACAO

Define a ordenação das formas de pagamento na tela de pedidos/recebimento.

| Valor | Descrição |
| --- | --- |
| 0 | Código da forma de pagamento (valor **Padrão**) |
| 1 | Descrição da forma de pagamento |
| 2 | Ordem de cadastro da forma de pagamento |

#### PEDIDO.LAYOUT

Parâmetro usado para identificar o layout utilizado no Retaguarda. Para **Exibe Ficha**, informe 5.

Valor **Padrão**: 1

#### PEDIDO.QTDEDIAS.PERMITEPOSTERGARPARCELAS

Define a quantidade de dias, no formato numérico, que será permitido postergar o vencimento de uma parcela, levando em consideração seu vencimento original. Caso a data base das parcelas seja alterada, um novo vencimento original será assumido pelo recálculo a partir da data base escolhida.

Valor **Padrão**: 0.

#### PEDIDO.SELLERUP.FINALIZAR

Indica se o sistema finalizará o pedido oriundo do Seller UP.

| Valor | Descrição |
| --- | --- |
| 0 | Não finalizar. O usuário precisará acessar a tela do pedido e finalizar manualmente. (valor **Padrão**) |
| 1 | Finalizar. O sistema finalizará automaticamente o pedido. |

#### PEDIDO.VALIDAR.ESTOQUE.ENTREGA.FUTURA

Define se ao cadastrar uma entrega futura deve validar o estoque.

| Valor | Descrição |
| --- | --- |
| 0 | Não (valor **Padrão**) |
| 1 | Sim |

#### PEDIDO.VALIDARQTDRAE.ONDE.NAOPERMITE

Define quais as telas, rotinas e/ou web services nos quais a validação da quantidade reservada exclusivamente do pedido é permitida.

As informações cadastradas no presente parâmetro tem preferência em relação ao PEDIDO.VALIDARQTDRAE.ONDE.PERMITE. Caso a mesma informação seja inserida nos dois parâmetros, o sistema respeitará o parâmetro PEDIDO.VALIDARQTDRAE.ONDE.NAOPERMITE.

| Valor | Descrição |
| --- | --- |
| (vazio) | Sempre validará a quantidade de reserva exclusiva. |
| Nome de tela, rotina e/ou web service, os quais deverão ser separados por vírgula, conforme regras descritas abaixo. | Não validará nos lugares informados. |

Para as telas, basta inserir o código da tela. Como exemplo: F135FCP.

Para as rotinas, utilize o código informado no campo Rotina Sapiens, na aba Rotina da tela Cadastro de Processo Automático (F000AGE). É necessário o uso do prefixo ROTINA\_. Por exemplo, no caso da rotina 126, deve-se escrever ROTINA\_126.

Para web services, informe a classe de sistema indicada na documentação do respectivo web service e porta. Por exemplo, no caso do web service com.senior.g5.co.mcm.ven.prefatura, porta CancelarPreFatura, a classe seria sr135CancelaPrefatura.

Para saber mais sobre o funcionamento desse parâmetro na validação da quantidade de reserva exclusiva dos pedidos, acesse a documentação correspondente.

#### PEDIDO.VALIDARQTDRAE.ONDE.PERMITE

Define quais as telas, rotinas e/ou web services nos quais a validação da quantidade reservada exclusivamente do pedido é permitida.

| Valor | Descrição |
| --- | --- |
| (vazio) | Sempre validará a quantidade de reserva exclusiva. |
| Nome de tela, rotina e/ou web service, os quais deverão ser separados por vírgula, conforme regras descritas abaixo. | Validará somente nos lugares informados. |

Para as telas, basta inserir o código da tela. Como exemplo: F135FCP.

Para as rotinas, utilize o código informado no campo Rotina Sapiens, na aba Rotina da tela Cadastro de Processo Automático (F000AGE). É necessário o uso do prefixo ROTINA\_. Por exemplo, no caso da rotina 126, deve-se escrever ROTINA\_126.

Para web services, informe a classe de sistema indicada na documentação do respectivo web service e porta. Por exemplo, no caso do web service com.senior.g5.co.mcm.ven.prefatura, porta CancelarPreFatura, a classe seria sr135CancelaPrefatura.

Para saber mais sobre o funcionamento desse parâmetro na validação da quantidade de reserva exclusiva dos pedidos, acesse a documentação correspondente.

#### PORTADOR.PERMITE.BAIXA.PIX

Define os portadores, no formato String, que poderão efetuar baixa de títulos pix mesmo com o campo Permite Baixa Títulos na Loja definido como "N - Não", na tela F039POR do Gestão Empresarial | ERP.

Valor **Padrão**: Null

#### RECEBIMENTO.POSTERGAR.SOMENTE.PARCELA

Indica se a parcela pode ter a data postergada independentemente do bloqueio da data base. O valor padrão é 0.

* Valor 1 - Permite.
* Valor 0 - Não permite.

#### RECEITUARIO.ITENSDARECEITA

Indica se deve mostrar a grade para preenchimento dos dados de itens da receita e se será obrigatório informar os dados na tela de geração de pedido e de nota fiscal.

| Valor | Descrição |
| --- | --- |
| 0 | Não. |
| 1 | Sim. |
| 2 | Sim, e obriga informar os dados dos itens da receita. |

#### RELATORIO.ETIQUETA.CAMINHO.1

Informe o caminho do arquivo JRXML para o relatório de etiqueta de preço do produto - Modelo 1.

#### RELATORIO.ETIQUETA.CAMINHO.2

Informe o caminho do arquivo JRXML para o relatório de etiqueta de preço do produto - Modelo 2.

#### REMOVER.TAG.SEM.CBENEF

Define as CSTs que não devem apresentar a tag cBenef (Código de Benefício Fiscal) no arquivo XML. Devem ser informados, como valor do parâmetro, os códigos das CSTs que não devem apresentar a tag, por exemplo: 00, 11, 22.

Valor **Padrão**: 00

#### RESTRICOES V$PAGUE

**Operações para correspondente bancário e Recarga**

* Para Correspondente e Recarga, a configuração Tef.FinalizadorDinheiro deve estar configurada;
* Recarga: não é possível definir taxas de comissão exclusivas por filial de operadora;
* Correspondente: não é possível definir taxas diferenciadas por tipo de serviço.

**Operações de transação com cartão**

Não são controladas restrições por administradora ou bandeira, os dados da transação são retornados após o término da transação. Sendo assim, serão verificadas as parcelas/taxas e canceladas (não aprovadas) a transações caso não existam as configurações.

Informações adicionais:

* É necessário ter o cliente do V$Pague funcionando ao conectar o PDV após uma queda de energia. Caso contrário, será necessário ajustar manualmente as transações pendentes;
* As informações de usuário e senha da licença do V$Pague (Tef.UsuarioVsPague e Tef.SenhaVsPague), são enviadas junto com a transação para que o cancelamento ou confirmação da transação fiquem definidos.

#### TESOURARIA.BLOQUEARSALDONEGATIVO

Indica se bloqueará uma retirada em conta interna com valor maior que o saldo.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não bloqueia (valor **Padrão**) |
| 1 | Bloqueia |

#### TITULO.VENCIMENTO.ENCARGO

Define qual a data de vencimento do banco de dados deve ser utilizada para cálculo de encargos. Por exemplo, quando há necessidade de controlar se haverá ou não cobrança de juros no pagamento do título.

| Valor | Descrição |
| --- | --- |
| 0 | Campo Vencimento |
| 1 | Campo Vencimento cálculo encargos juros (valor **Padrão**) |

#### TRIBUTOS.ADESAOROTST

Clientes que aderiram ao **ROT-ST (Regime Optativo de Tributação da Substituição Tributária)** não tem direito à restituição e não precisam fazer a complementação do ICMS-ST, porém continuam declarando o ressarcimento através dos registros C176 e C197. Nesse caso, deve-se ativar este parâmetro dinâmico no cadastro de filiais (F070FCA). Com isso, os campos **CtaB57** das tabelas E660RSC, E660RSV e E660RRZ serão preenchidos apenas com os motivos relativos ao ressarcimento. Com o parâmetro ativo, se o controle de médias **não foi** inicializado, o sistema fará o cálculo do imposto 70 (F661IA5) com base no Controle de Entrada e Saída. O valor padrão é **N**.

#### TRIBUTOS.CONSIDERARVALORESBASEICMS

Este parâmetro dinâmico indica quais valores devem ser considerados, por meio da inicialização do Controle de Entrada de Produtos (F075CEP) com origem em Tributos, no cálculo do valor base de ICMS caso a nota não seja geradora de crédito. O caminho é Cadastro de Filiais (F070FCA), botão Par. Dinâmicos (F000PPD).

Valores possíveis:

1. Valor de Isentas + Valor de Outras
2. Valor das mercadorias - Valor dos descontos
3. Valor das mercadorias.

Se não estiver preenchido, considera o valor "1".

#### VENDA.ALTERATABELAPRECO

Define se é permitido alterar a tabela de preço manualmente na venda de itens.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não permite (valor **Padrão**) |
| 1 | Permite |

#### VENDA.AUTOCREDIARIO

Indica se será utilizado o recurso denominado Auto Crediário. É destinado à vendas diretas no PDV. Consulte a documentação de Venda de produtos e serviços para mais informações sobre a tabela de preço.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não (valor **Padrão**) |
| 1 | Sim |

#### VENDA.AVISODOCUMENTOSIMPRESSOS

Define quais mensagens serão exibidas ao operador informando sobre a impressão de documentos em impressora não fiscal, no Retaguarda, considerando:

* 0 - Indica que o item não imprime documento e, logo, não necessita de aviso;
* 1 - Indica que o item imprime documento e que deve ser exibido aviso ao operador.

| Código | Descrição | Valor Padrão |
| --- | --- | --- |
| 1 | Garantida Estendida | 0 |
| 2 | Seguro Parcela Protegida | 0 |
| 3 | Curso | 0 |
| 4 | Nota fiscal de cupom fiscal | 0 |

## Exemplo:

Configuração:

1,0,0,1

* 1: Garantia estendida, quando vendida, imprime documento e exibe aviso;
* 0: Seguro parcela protegida, mesmo se vendido e emita documento, não emite aviso;
* 0: Curso, mesmo se vendido e emita documento, não emite aviso;
* 1: Nota fiscal de cupom fiscal, quando emitida, exibe aviso.

#### VENDA.BOTAOFINALIZADORSUBLINHADO

Define se os botões dos finalizadores terão seu texto sublinhado, quando destacados.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não sublinhado (valor **Padrão**) |
| 1 | Sublinhado |

#### VENDA.BOTAORESTRICAODESTACADO

Define se destaca os botões restringidos pela tabela de preço na tela de finalizador na venda.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não (valor **Padrão**) |
| 1 | Sim |

#### VENDA.CANCELAVARIOSITENSPORVEZ

Define se a função de cancelamento de item irá permitir cancelar vários itens por vez.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não permite (valor **Padrão**) |
| 1 | Permite |

#### VENDA.CARACTERMULTIPLICADORQUANTIDADE

Caractere utilizado na venda de itens como multiplicador de quantidade.

Valor **Padrão**: \*

#### VENDA.CARACTERPESQUISAPORDESCRICAO

Caractere utilizado na venda de itens para pesquisar pela descrição do produto.

Valor **Padrão**: #

#### VENDA.CONDICAOPAGAMENTOAUTOCREDIARIO

Define a condição de pagamento utilizada no recebimento do auto-crediário. Deve ser informado o código da condição de pagamento, no formato inteiro.

#### VENDA.CONTRATOCOMPRAVENDA

Indica qual o comportamento do contrato de compra e venda no momento da venda (quando o Retaguarda recebe uma venda efetuada pelo PDV).

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não gera o contrato posteriormente |
| 1 | Gera e imprime automaticamente na venda. Ainda há a possibilidade de reimprimir na tela de consulta dos cupons/NFCe (valor **Padrão**) |
| 2 | Gera, mas não imprime automaticamente. Há a possibilidade de reimprimir na tela de consulta |

#### VENDA.CONTRATO.COMPRA.VENDA.CAMINHO

Permite customizar o novo modelo do contrato de compra e venda. Deve ser informado o caminho dos arquivos customizados no formato JRXML. Esse modelo somente será carregado se o parâmetro dinâmico VENDA.CONTRATO.COMPRA.VENDA.MODELO estiver definido com o valor 1. Utilize os arquivos JRXML disponíveis na pasta .zip (contém os arquivos contrato\_compra\_venda\_customizado.jrxml e contrato\_compra\_venda\_customizado\_subreport.jrxml) para customização de um novo modelo do contrato de compra e venda.

#### VENDA.CONTRATO.COMPRA.VENDA.MODELO

Define o modelo do contrato de compra e venda.

| Valor | Descrição |
| --- | --- |
| 0 | Utiliza o modelo padrão. (valor **Padrão**) |
| 1 | Utiliza novo modelo. |

#### VENDA.DESCONTOITENS

Define se é permitido conceder desconto para itens em uma venda no PDV.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não permite (valor **Padrão**) |
| 1 | Permite |

#### VENDA.EMISSAONOTAFISCAL

Indica o comportamento da emissão de nota fiscal a partir de cupons fiscais/NFCe.

| Valor (Lista) | Descrição |
| --- | --- |
| 1 | Permite a emissão automática de Nota Fiscal (valor **Padrão**) |
| 2 | Permite a emissão manual com escolha do usuário |
| 3 | Não permite emissão de Nota Fiscal |

**Detalhamento dos valores**:

## 1 - Permite a emissão automática de Nota Fiscal

**No Retaguarda (inclusive gerados pela consulta de preço): Mercado > Gestão de vendas > Pedido (opção Emitir nota fiscal)**:

* Se a operação é futura (tem itens de entrega futura): a opção de emitir nota fica desabilitada, desmarcada e não pode ser marcada automaticamente.
* Se a operação é imediata (somente itens de entrega imediata):
  + a opção de emitir nota fica habilitada para que possa ser marcada manualmente pelo usuário ou automaticamente pelo sistema.
  + a opção de emitir nota é marcada automaticamente ao:
    - adicionar um item que exige emissão de Nota Fiscal.
    - informar um cliente de um estado diferente da filial.

**No Retaguarda: Mercado > Gestão de faturamento > Cupons fiscais (botão Emitir nota fiscal de cupom)**: permite emitir nota fiscal de acordo com as validações do cupom.

**No Retaguarda: Mercado > Gestão de faturamento (botão Emitir NF-e)**: permite emitir nota fiscal de acordo com as validações da NFC-e/CFE-SAT.

**No PDV, tanto PAF quanto NFCe: Outras > ADM > Consultar Operações (botão Nota de cupom)**: permite emitir nota fiscal de acordo com as validações do cupom.

## 2 - Permite a emissão manual com escolha do usuário

**No Retaguarda (inclusive gerados pela consulta de preço): Mercado > Gestão de vendas > Pedido (opção Emitir nota fiscal)**:

* Se a operação é futura (tem itens de entrega futura): a opção de emitir nota fica desabilitada, desmarcada e não pode ser marcada automaticamente.
* Se a operação é imediata (somente itens de entrega imediata):
  + a opção de emitir nota fica habilitada para que possa ser marcada manualmente pelo usuário. Caso seja marcada é questionado ao usuário: "A filial está configurada para não emitir nota fiscal, deseja prosseguir?". Caso escolhida a opção Sim a opção de emitir nota é marcada, caso escolhido Não a opção de emitir nota não é marcada.
  + a opção de emitir nota não é mais marcada automaticamente.

**No Retaguarda: Mercado > Gestão de faturamento > Cupons fiscais (botão Emitir nota fiscal de cupom)**: permite emitir nota fiscal de acordo com as validações do cupom, porém é questionado ao usuário: A filial está configurada para não emitir nota fiscal, deseja prosseguir?. Caso escolhida a opção Sim, gera a nota fiscal, caso escolhido Não, a nota não é gerada.

**No Retaguarda: Mercado > Gestão de faturamento (botão Emitir NF-e)**: permite emitir nota fiscal de acordo com as validações da NFC-e/CFE-SAT, porém é questionado ao usuário: A filial está configurada para não emitir nota fiscal, deseja prosseguir? Caso escolhida a opção Sim, gera a nota fiscal, caso escolhido Não, a nota não é gerada.

**No PDV, tanto PAF quanto NFCe: Outras > ADM > Consultar Operações (botão Nota de cupom)**: permite emitir nota fiscal de acordo com as validações do cupom, porém é questionado ao usuário: A filial está configurada para não emitir nota fiscal, deseja prosseguir? Caso escolhida a opção Sim, gera a nota fiscal, caso escolhido Não, a nota não é gerada.

## 3 - Não permite emissão de Nota Fiscal

**No Retaguarda (inclusive gerados pela consulta de preço): Mercado > Gestão de vendas > Pedido (opção Emitir nota fiscal)**: a opção de emitir nota fica desabilitada, desmarcada e não pode ser marcada automaticamente.

Em:

* **Retaguarda: Mercado > Gestão de faturamento > Cupons fiscais (botão Emitir nota fiscal de cupom)**
* **Retaguarda: Mercado > Gestão de faturamento (botão Emitir NF-e)**
* **PDV, tanto PAF quanto NFCe: Outras > ADM > Consultar Operações (botão Nota de cupom)**

Não permite emitir nota fiscal e apresenta a mensagem "A filial está configurada para não permitir emissão de nota fiscal":

#### VENDA.EXIBEFICHA

Utilizado no PDV para definir se a Filial em uso exibirá o campo Ficha na grade de importar pedidos. Para Exibe Ficha, informe **1**.

| Valor (Inteiro) | Descrição |
| --- | --- |
| 0 | Não permite a importação (valor **Padrão**) |
| 1 | Permite a importação da ficha. |

#### VENDA.FICHA

Permite a importação de ficha, do Retaguarda para o PDV, através do prefixo de ficha.

| Valor (Inteiro) | Descrição |
| --- | --- |
| 0 | Não permite a importação (valor **Padrão**) |
| 1 | Permite a importação da ficha |

#### VENDA.FINALIZADORAUTOCREDIARIO

Define a forma de pagamento,no formato inteiro, utilizada no recebimento do autocrediário. Deve ser informada o código da forma de pagamento crediário.

#### VENDA.GARANTIAESTENDIDA

Habilita venda de garantia estendida no sistema de PDV.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não (valor **Padrão**) |
| 1 | Sim |

#### VENDA.GARANTIAESTENDIDAAVULSA

Define se é permitido vender garantia estendida para produtos de outras vendas.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não permite (valor **Padrão**) |
| 1 | Permite |

#### VENDA.HABILITAITENSRAPIDOS

Habilita função para consultar itens rápidos na venda.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não (valor **Padrão**) |
| 1 | Sim |

#### VENDA.IDENTIFICAVENDEDOR

Define se é permitido identificar vendedor na venda de itens.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não permite (valor **Padrão**) |
| 1 | Permite |

#### VENDA.IMPRIME.GARANTIA.CANCELAMENTO

Indica se imprimirá automaticamente o relatório de cancelamento da garantia estendida no cancelamento do Cupom Fiscal ou da Nota Fiscal.

| Valor | Descrição |
| --- | --- |
| 0 | Não imprime automaticamente (valor **Padrão**) |
| 1 | Imprime automaticamente |

#### VENDA.IMPRIMECESTCUPOM

Define se o CEST e o NCM serão impressos junto a descrição do produto no Cupom Fiscal. O parâmetro será exportado ao Retaguarda e logo aos PDVs nas respectivas filiais.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não |
| 1 | Sim (valor **Padrão**) |

Quando este campo estiver parametrizado como **1** e o produto possuir o código CEST, ele será impresso juntamente com o código NCM na descrição do item, a partir do primeiro caractere, ou seja, antes da descrição do item, separando as informações com **#**. Caso o produto não possua código CEST é impresso somente a descrição do item.

Por padrão, este campo é iniciado como **1**, desta forma, a impressão do CEST no cupom fiscal é realizada conforme demonstrado acima, após a atualização desta versão.

## Exemplo:

Configuração de produto e a impressão no cupom fiscal quando o parâmetro estiver como **Sim**:

| CEST | NCM | Descrição | Resultado |
| --- | --- | --- | --- |
| 20.017.00 | 3305.10.00 | Refrigerante Cola | #20.017.00#3305.10.00# Refrigerante Cola |
|  | 3305.10.00 | Refrigerante Cola | Refrigerante Cola |
| 20.017.00 |  | Refrigerante Cola | #20.017.00# Refrigerante Cola |
|  |  | Refrigerante Cola | Refrigerante Cola |

#### VENDA.IMPRIMECODIGONADESCRICAOCUPOM

O comportamento do sistema é imprimir o código de barras no cupom fiscal, caso o produto possua código de barras. A função deste parâmetro é imprimir o código do produto antes da descrição, nesse caso. O código será impresso entre colchetes.

## Exemplo:

1234567890123 [0001] TV, onde:

* o código de barras é 1234567890123
* o código do produto é 0001; e
* descrição é TV.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não imprime o código do produto (valor **Padrão**) |
| 1 | Sim, imprime o código do produto |

#### VENDA.IMPRIMECUPOMDETROCA

Habilita impressão do Cupom de Troca após a emissão do cupom fiscal.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não (valor **Padrão**) |
| 1 | Sim |

#### VENDA.IMPRIMEFILIALCUPOM

Habilita recurso para impressão da filial no cupom fiscal.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não (valor **Padrão**) |
| 1 | Sim |

#### VENDA.IMPRIMEGARANTIA

Indica se irá imprimir automaticamente o relatório de seguro parcela protegida quando chegar no Retaguarda.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não imprime automaticamente |
| 1 | Imprime automaticamente valor (valor **Padrão**) |

#### VENDA.IMPRIMEMONTAGEMAGRUPADA

Imprime em uma única via os itens de todos os controles de montagem do pedido, utilizando os dados gerais do primeiro controle de montagem adicionado.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Imprime os itens de cada controle de montagem individualmente (valor **Padrão**) |
| 1 | Imprime em uma única via os itens de todos os controles de montagem do pedido |

#### VENDA.IMPRIMEOPERADORCUPOM

Habilita recurso para impressão do operador no cupom fiscal.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não (valor **Padrão**) |
| 1 | Sim |

#### VENDA.IMPRIMESEGURO

Habilita/desabilita a impressão automática do contrato de seguro parcela protegida.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não imprime automaticamente |
| 1 | Imprime automaticamente (valor **Padrão**) |

#### VENDA.IMPRIMEVENDEDORCUPOM

Habilita recurso para impressão do vendedor no cupom fiscal. Caso identificado mais de um vendedor deve ser impresso o último identificado.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não (valor **Padrão**) |
| 1 | Sim |

#### VENDA.IMPRIMIRCODIGOEMBALAGEM

Indica que será impresso o código do produto, lido da embalagem no momento da venda, caso este seja diferente do código do produto (já impresso na DANFE).

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não (valor **Padrão**) |
| 1 | Sim |

#### VENDA.NOTADECUPOM

Habilita funcionalidade para solicitar emissão de nota fiscal de cupom fiscal ao Retaguarda.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não |
| 1 | Sim (valor **Padrão**) |

#### VENDA.PEDIDO

Habilita o uso de pedido no PDV.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não (valor **Padrão**) |
| 1 | Sim |

#### VENDA.PERGUNTAIMPRIMEDANFEENTREGAFUTURA

Ao faturar no PDV uma venda de Entrega Futura, determina se o sistema deve exibir uma mensagem perguntando se o usuário deseja ou não imprimir o DANFE da nota fiscal de simples faturamento. Esta pergunta também será realizada ao finalizar notas fiscais de saída emitidas manualmente no Retaguarda.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não perguntar (neste caso a DANFE será sempre impressa) (valor **Padrão**) |
| 1 | Perguntar |

#### VENDA.PERMITECREDIARIOPARAGARANTIAESTENDIDA

Indica se permite o pagamento com crediário de uma garantia estendida inserida diretamente no PDV para um pedido que já tenha sido pago com crediário. Quando isso ocorrer o sistema irá somar o valor da garantia estendida nas parcelas de crediário do pedido e efetuará o recálculo das parcelas, reajustando os juros com base na condição de pagamento selecionada anteriormente, sem necessidade de reaprovação de crédito.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não (valor **Padrão**) |
| 1 | Sim |

#### VENDA.PREFIXOFICHA

Prefixo utilizado no PDV para importar um pedido vinculado a uma ficha.

Valor **Padrão**: FIC

#### VENDA.PREFIXOPEDIDO

Prefixo, no formato texto, para importar pedido através do visor.

Valor **Padrão**: PED

#### VENDA.PREFIXOPREVENDA

Prefixo, no formato texto, para importar pré-venda através do visor.

Valor **Padrão**: PV

#### VENDA.PREVENDA

Habilita o uso de pré-venda no PDV.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não (valor **Padrão**) |
| 1 | Sim |

#### VENDA.QUANTIDADEMAXIMAITEM

Define o valor máximo, no formato inteiro, para quantidade do item. Para filiais PAF, este parâmetro não é validado.

Valor **Padrão**: 999999

#### VENDA.SEGUROFURTOROUBONUMEROSORTE

Indica se a filial trabalha com números da sorte na venda de seguros furto e roubo.

Ao finalizar um pedido com um ou mais itens de seguro furto e roubo, o Retaguarda fará uma requisição síncrona ao Gestão Empresarial | ERP para buscar os números da sorte. Se a requisição falhar, não será possível finalizar o pedido.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não |
| 1 | Sim (valor **Padrão**) |

#### VENDA.SEGUROPARCELAPROTEGIDA

Habilita a venda de seguro com parcela protegida no sistema de PDV.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não (valor **Padrão**) |
| 1 | Sim |

#### VENDA.TEMPLATECUPOMDETROCA

Define o texto que será impresso no cupom de troca. Utiliza o mesmo mecanismo de substituição de tags da configuração Emitir relatorio pós-venda.

Valor **Padrão**:

<CENTRO>CUPOM DE TROCA</CENTRO>

Código do cliente : <COD\_CLIENTE/>

Nome do cliente : <NOME\_CLIENTE/>

ECF : <COD\_ECF\_CUPOM\_REF mascara=000/>

CRO : <CRO\_CUPOM\_REF mascara=000/>

COO : <COO\_CUPOM\_REF mascara=000/>

Data da venda : <DT\_VENDA mascara=dd/MM/yyyy/>

#### VENDA.TEXTOLIVRE1

Primeira linha de texto para ser impresso no cupom fiscal.

#### VENDA.TEXTOLIVRE2

Segunda linha de texto para ser impresso no cupom fiscal.

#### VENDA.TEXTOLIVRE3

Terceira linha de texto para ser impresso no cupom fiscal.

#### VENDA.TEXTOLIVRE4

Quarta linha de texto para ser impresso no cupom fiscal.

#### VENDA.TEXTOLIVRE5

Quinta linha de texto para ser impresso no cupom fiscal.

#### VENDA.TEXTOLIVRE6

Sexta linha de texto para ser impresso no cupom fiscal.

#### VENDA.TIPOPESQUISAPRODUTO

Tipo de pesquisa do texto na consulta de produto.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Contendo no texto (valor **Padrão**) |
| 1 | Pelo início do texto |

#### VENDA.VENDEITENSINATIVOS

Define se é permitido vender itens inativos.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não permite (valor **Padrão**) |
| 1 | Permite |

## Páginas relacionadas

* [146 - Limpar fotos antigas da Balança](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/processos-automaticos/146-limpar-fotos-antigas-da-balanca.htm)
* [F113REM](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f113rem.htm)
* [F021MOT](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f021mot.htm)
* [Base64 Decode and Encode](https://www.base64encode.org/)
* [Base64 Encode](http://base64encode.net/)
* [documentação da VAN Bancária](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/van-bancaria/van-bancaria-integracao.htm)
* [com.senior.g5.co.mcm.ven.manualpedidos](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/webservices/com_senior_g5_co_mcm_ven_manualpedidos.htm)
* [VEN-140CFILE01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_140cfile01.htm)
* [VEN-140EUDLE02](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_140eudle02.htm)
* [GER-140EUDLE01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ger_140eudle01.htm)
* [GER-210EUDLE01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ger_210eudle01.htm)
* [F000GOW](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000gow.htm)
* [F001TES](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f001tes.htm)
* [GER - 000INWMS01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ger_000inwms01.htm)
* [GER- 000INWMS18](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ger_000inwms18.htm)
* [na geração do .XML](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/leiaute-nf-e-nfc-e.htm)
* [ICMS 53](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/icms-monofasico.htm#icms53)
* [ICMS Monofásico](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/icms-monofasico.htm)
* [validação da quantidade reservada exclusivamente do pedido](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/manual-processos/mercado/gestao-faturamento/validacao-quantidade-reserva-exclusiva-pedidos.htm)
* [F000AGE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_recursos/f000age.htm)
* [documentação  correspondente](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/manual-processos/mercado/gestao-faturamento/validacao-quantidade-reserva-exclusiva-pedidos.htm#execucaovalidacao)
* [F039POR](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f039por.htm)
* [relatório de etiqueta de preço do produto](https://documentacao.senior.com.br/gestaodelojas/6.2.19#ajuda-por-processos/retaguarda/mercado/gestao-de-faturamento/relatorio-de-etiqueta-de-produtos-para-revenda.htm)
* [F070FCA](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070fca.htm)
* [F661IA5](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f661ia5.htm)
* [Controle de Entrada de Produtos (F075CEP)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075cep.htm)
* [Venda de produtos e serviços](https://documentacao.senior.com.br/gestaodelojas/6.2.19#ajuda-por-processos/pdv/rotinas-de-caixa/venda-direta-produto-servico.htm)
* [arquivos  JRXML](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/snippets/parametros-dinamicos/cadastro-filiais/venda.contrato.compra.venda.caminho/arquivos_contrato_modelos.zip)
