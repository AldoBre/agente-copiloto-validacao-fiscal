# Cadastro de perfis de usuários (F090PFU)

> **Fonte:** F000PPD -  Configuração de parâmetros dinâmicos — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000ppd.htm  
> **Trilha:** Ajuda por telas > Cadastros  
> **Telas citadas:** F028GCP, F090PFU, F140GNF, F670BEM  
> **Identificadores de regras:** —

---
#### CLIENTE.BLOQUEARCAMPOSIDENTIFICACAO

Desabilita a edição dos campos Nome, CPF, RG e Data de nascimento no cadastro de um cliente que esteja informado em nota ou pedido (finalizado ou faturado), para evitar problemas na análise de crédito. Caso o parâmetro esteja habilitado (valor 1), somente o usuário responsável na matriz consegue editar os dados do cliente.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não bloqueia a edição dos campos no cadastro o cliente (valor **Padrão**) |
| 1 | Bloqueia a edição dos campos no cadastro do cliente |

#### NOTAFISCAL.ENVIA.COBR

Define se a tag de cobrança `<cobr>` será enviada ou não para SEFAZ.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Desabilitado |
| 1 | Habilitado (valor **Padrão**) |

#### NOTAFISCAL.IMPRIMEVALORTOTALRECEBIDO

Indica se deve gerar a tag `<ValorTotalRecebido>` na geração do XML de notas fiscais de serviço.

| Valor | Descrição |
| --- | --- |
| 0 | Não |
| 1 | Sim (valor **Padrão**) |

#### NOTAFISCAL.OBRIGAOPERACAO

Habilita a obrigatoriedade de preenchimento de operação no momento da inclusão de uma Nota Fiscal, de entrada ou de saída.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não obriga inserção de Operação |
| 1 | Obriga inserção de Operação na geração de NF (valor **Padrão**) |

#### NOTAFISCAL.OPERACOESPERMITIDAS

Relaciona quais operações de nota fiscal são liberadas por perfil de usuário na geração manual de uma Nota Fiscal.

| Valor (Texto) | Descrição |
| --- | --- |
| Códigos de referência das operações liberadas | Listar os códigos de referência das operações liberadas separados por vírgula |
| (vazio) | Manter campo **Valor** vazio (valor **Padrão**) |

#### NOTAFISCAL.SUGERIRPRECOCONFORMEBEM

É responsável por levar à grade de produtos da tela de Digitação de Notas manuais (F140GNF), o **Valor Unitário Aquisição** da tela de Controle de Bens / Bem / Individual (F670BEM).

Para o funcionamento da rotina, seguir as condições abaixo:

1. o parâmetro deve estar definido como S;
2. ter preenchido o campo **Valor Unitário Aquisição** na tela F670BEM;
3. informar na tela F140GNF, guia Produtos, o campo **Cód. Bem**.

Após isso serão preenchidos automaticamente os campos **Preço Unitário Liq.** e **Preço Bruto** da grade de produtos.

| Valor (Lista) | Descrição |
| --- | --- |
| S | Habilita o funcionamento da rotina |
| N | Mantém o funcionamento padrão da tela (valor **Padrão**) |

#### PERFIL.ASSISTENCIA.CRIA.PENDENCIA.COLETA

Define se o segundo passo da assistência é para gerar pendência no Gestão Empresarial | ERP ou para somente coletar na Filial.

| Valor | Descrição |
| --- | --- |
| 0 | Não |
| 1 | Sim (valor **Padrão**) |

#### PERFIL.ASSISTENCIA\_PERMITE\_CANCELAMENTO\_INTEGRADO

Define se o usuário poderá efetuar o cancelamento de uma assistência técnica já integrada com o Gestão Empresarial | ERP.

| Valor | Descrição |
| --- | --- |
| 0 | Não (valor **Padrão**) |
| 1 | Sim |

#### PERFIL.ASSISTENCIA\_PERMITE\_DEVOLUCAO

Indica se o perfil tem permissão para realizar devolução pela assistência técnica.

| Valor | Descrição |
| --- | --- |
| N | Não (valor **Padrão**) |
| S | Sim |

#### PERFIL.FILTRAR\_APENAS\_VENDEDORES\_E\_GERENTES

Indica se nas telas de pedidos, orçamento, consulta de preço e de pré-venda e do Retaguarda serão listados todos os usuários ou apenas os vendedores/gerentes.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não. Será exibido na pesquisa todos os usuários ativos, independentemente do perfil |
| 1 | Sim. Será exibido na pesquisa todos os usuarios ativos, que pertençam ao perfil de vendedores e/ou gerentes (valor **Padrão**) |

#### PERFIL.LIBERA\_FORMA\_PAGTO\_COM\_DESCONTO

Define se o usuário pode ou não desbloquear pedidos que tiveram desconto acima do máximo permitido pela forma ou condição de pagamento.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não (valor **Padrão**) |
| 1 | Sim |

#### PERFIL.MOSTRA\_CARTAO\_PRESENTE

Determina se os quatro últimos dígitos do cartão presente devem ou não ser apresentados no campo Cartão Presente da tela de contas a pagar.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não (valor **Padrão**) |
| 1 | Sim |

#### PERFIL.PERCENTUAL\_PERMITE\_TROCA\_VALOR\_SUPERIOR

Define o percentual, no formato numérico, do valor que pode exceder do valor do produto que está sendo trocado.

## Exemplo:

* Produto sendo trocado: R$ 100,00
* Percentual informado: 20

Será permitido trocar por um produto de até R$ 120,00. Para que não seja permitida a troca de produtos com valor superior, esse percentual deve ficar zerado.

#### PERFIL.PERMITE.ALTERAR.CADASTRO.CLIENTE.ABA.CONVENIOS

Responsável pelo cadastro de informações referentes a guia Convênios na tela de cadastro do cliente no Retaguarda.

| Valor | Descrição |
| --- | --- |
| 1 | Permite edição (valor **Padrão**) |
| 0 | Não permite edição |

#### PERFIL.PERMITE.ALTERAR.CADASTRO.CLIENTE.ABA.ENDERECOS

Responsável pelo cadastro de informações referentes à guia de Endereços.

| Valor | Descrição |
| --- | --- |
| 0 | Não. Todos os campos dessa guia ficarão bloqueados para inserção/edição |
| 1 | Sim (valor **Padrão**) |

#### PERFIL.PERMITE.ALTERAR.CADASTRO.CLIENTE.ABA.IMAGENS

Responsável pelo cadastro de informações referentes à guia Imagem.

| Valor | Descrição |
| --- | --- |
| 0 | Não. Todos os campos dessa guia ficarão bloqueados para inserção/edição |
| 1 | Sim (valor **Padrão**) |

#### PERFIL.PERMITE.ALTERAR.CADASTRO.CLIENTE.ABA.OBSERVACOES

Responsável pelo cadastro de informações referentes à guia Observações.

| Valor | Descrição |
| --- | --- |
| 0 | Não. Todos os campos dessa guia ficarão bloqueados para inserção/edição |
| 1 | Sim (valor **Padrão**) |

#### PERFIL.PERMITE.ALTERAR.CADASTRO.CLIENTE.ABA.OUTRAS.AVALISTAS

Responsável pelo cadastro de informações referentes à guia Avalistas, presente na guia Outras Informações.

| Valor | Descrição |
| --- | --- |
| 0 | Não. Todos os campos dessa guia ficarão bloqueados para inserção/edição |
| 1 | Sim (valor **Padrão**) |

Observação

A configuração do parâmetro dinâmico PERFIL.PERMITE.ALTERAR.CADASTRO.CLIENTE.ABA.OUTRAS prevalece sobre essa para bloqueios, ou seja, se configurado com o valor **0**, as configurações filhas não surtem efeito.

#### PERFIL.PERMITE.ALTERAR.CADASTRO.CLIENTE.ABA.OUTRAS.BLOQUEIOS

Responsável pelo cadastro de informações referentes à guia Bloqueio, presente na guia Outras Informações.

| Valor | Descrição |
| --- | --- |
| 0 | Não. Todos os campos dessa guia ficarão bloqueados para inserção/edição |
| 1 | Sim (valor **Padrão**) |

Observação

A configuração do parâmetro dinâmico PERFIL.PERMITE.ALTERAR.CADASTRO.CLIENTE.ABA.OUTRAS prevalece sobre essa para bloqueios, ou seja, se configurado com o valor **0**, as configurações filhas não surtem efeito.

#### PERFIL.PERMITE.ALTERAR.CADASTRO.CLIENTE.ABA.OUTRAS

Responsável pelo cadastro de informações referentes à guia Outras Informações.

| Valor | Descrição |
| --- | --- |
| 0 | Não. Todos os campos na guia Outras Informações ficarão bloqueados para inserção/edição. |
| 1 | Sim (valor **Padrão**) |

#### PERFIL.PERMITE.ALTERAR.CADASTRO.CLIENTE.ABA.OUTRAS.GERAL

Responsável pelo cadastro de informações referentes à guia Geral, presente na guia Outras Informações.

| Valor | Descrição |
| --- | --- |
| 0 | Não. Todos os campos dessa guia ficarão bloqueados para inserção/edição |
| 1 | Sim (valor **Padrão**) |

Observação

A configuração do parâmetro dinâmico PERFIL.PERMITE.ALTERAR.CADASTRO.CLIENTE.ABA.OUTRAS prevalece sobre essa para bloqueios, ou seja, se configurado com o valor **0**, as configurações filhas não surtem efeito.

#### PERFIL.PERMITE.ALTERAR.CADASTRO.CLIENTE.ABA.OUTRAS.GERAL.SPC

Responsável pelo cadastro de informações referentes ao SPC, presentes na guia Geral que, por sua vez, está presente na guia Outras Informações.

| Valor | Descrição |
| --- | --- |
| 0 | Não. Os campos **Data da consulta SPC**, **Cidade da consulta SPC** e **Situação SPC** ficarão bloqueados para inserção/edição |
| 1 | Sim (valor **Padrão**) |

Observação

As configurações dos parâmetros dinâmicos PERFIL.PERMITE.ALTERAR.CADASTRO.CLIENTE.ABA.OUTRAS e PERFIL.PERMITE.ALTERAR.CADASTRO.CLIENTE.ABA.OUTRAS.GERAL prevalecem sobre essa para bloqueios, ou seja, se configurado com o valor **0**, as configurações filhas não surtem efeito.

#### PERFIL.PERMITE.ALTERAR.CADASTRO.CLIENTE.ABA.OUTRAS.PREFERENCIA

Responsável pelo cadastro de informações referentes à guia Preferências, presente na guia Outras Informações.

| Valor | Descrição |
| --- | --- |
| 0 | Não. Todos os campos dessa guia ficarão bloqueados para inserção/edição |
| 1 | Sim (valor **Padrão**) |

Observação

A configuração do parâmetro dinâmico PERFIL.PERMITE.ALTERAR.CADASTRO.CLIENTE.ABA.OUTRAS prevalece sobre essa para bloqueios, ou seja, se configurado com o valor **0**, as configurações filhas não surtem efeito.

#### PERFIL.PERMITE.ALTERAR.CADASTRO.CLIENTE.ABA.OUTRAS.REFERENCIAS

Responsável pelo cadastro de informações referentes à guia Referências, presente na guia Outras Informações.

| Valor | Descrição |
| --- | --- |
| 0 | Não. Todos os campos dessa guia ficarão bloqueados para inserção/edição |
| 1 | Sim (valor **Padrão**) |

Observação

A configuração do parâmetro dinâmico PERFIL.PERMITE.ALTERAR.CADASTRO.CLIENTE.ABA.OUTRAS prevalece sobre essa para bloqueios, ou seja, se configurado com o valor **0**, as configurações filhas não surtem efeito.

#### PERFIL.PERMITE.ALTERAR.CLIENTE.APROVCREDITO

Define se o usuário pode alterar o cliente no momento de selecionar os títulos para aproveitamento de crédito na tela de pedido e na baixa manual de contas a receber no Retaguarda.

| Valor | Descrição |
| --- | --- |
| 0 | Não. O campo Cliente fica bloqueado na tela |
| 1 | Sim. O campo Cliente fica habilitado, podendo consultar títulos de qualquer cliente (valor **Padrão**) |

#### PERFIL.PERMITE.ALTERAR.CLIENTE.DUPLO.CLIQUE.GRID

Define se os detalhes do cliente abrem em modo edição ao realizar duplo clique na grade. E se abrem em modo edição após importar um novo cliente da rede.

| Valor | Descrição |
| --- | --- |
| S | Sim (valor **Padrão**) |
| N | Não |

#### PERFIL.PERMITE.ENTREGA.FUTURA.SEM.ESTOQUE

Define se o usuário pode finalizar um pedido de entrega futura pela loja (própria ou outras) faltando estoque para os produtos ou sem validação do estoque.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não (valor **Padrão**) |
| 1 | Sim |

#### PERFIL.PERMITE\_ALTERAR\_CATEGORIA\_CREDITO\_CLIENTE

Define se o usuário possui, ou não, permissão para alterar a categoria de crédito do cliente.

| Valor | Descrição |
| --- | --- |
| 0 | Não permite alterar |
| 1 | Permite alterar (valor **Padrão**) |

#### PERFIL.PERMITE\_ALTERAR\_VALORES\_BAIXA

Define se o perfil poderá alterar os valores de Juros, Multa, Desconto e Acréscimo nas movimentações financeiras. Caso esteja desativado, ao efetuar as baixas das movimentações financeiras o sistema não vai permitir alterar os campos.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não |
| 1 | Sim (valor **Padrão**) |

#### PERFIL.PERMITE\_DESCONTO\_EM\_ITENS\_PROMOCIONAIS

Define se o perfil poderá conceder descontos em itens promocionais no pedido (ou seja, cuja tabela de preços é do tipo Tablóide ou Promoção). Caso esteja desativado, ao vender itens promocionais no pedido e conceder descontos no item ou no subtotal do pedido, o sistema irá incluir um bloqueio no pedido que poderá ser liberado apenas por usuários que possuem este parâmetro ativado.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não |
| 1 | Sim (valor **Padrão**) |

#### PERFIL.PERMITE\_ENTRADA\_MENOR\_CONDICAO\_PAGAMENTO

Indica se o usuário tem permissão para diminuir o valor de entrada calculado pela condição de pagamento. É necessária que a condição de pagamento esteja configurada com o tipo "3 - Parcelas Diferentes" na tela F028GCP.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não (valor **Padrão**) |
| 1 | Sim |

#### PERFIL.PERMITE\_MODO\_OFFLINE\_QUANDO\_DESATUALIZADO

Habilita o usuário a usar o PDV em uma versão desatualizada em relação ao servidor do Retaguarda.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | O usuário não terá permissão para operar com o PDV desatualizado (valor **Padrão**) |
| 1 | O usuário poderá usar o PDV desatualizado ou autorizar outros usuários a fazê-lo |

#### PERFIL.PERMITE\_MOVIMENTAR\_CONTA\_BANCO

Indica se o perfil de usuário pode movimentar valores de uma conta banco através de saída ou transferência.

| Valor (Lista) | Descrição |
| --- | --- |
| N | Não permite movimentar (valor **Padrão**) |
| S | Permite movimentar |

#### PERFIL.PERMITEIMPORTARIBPT

Habilita/desabilita a tela de importação da tabela IBPT, através do Retaguarda.

| Valor | Descrição |
| --- | --- |
| S | Sim |
| N | Não (valor **Padrão**) |

#### PERFIL.TIPOS\_BAIXA\_PERMITIDA

Indica quais tipos de ações financeiras são permitidas para efetuar uma baixa nas movimentações financeiras. Lista os códigos de referência das ações liberadas separados por vírgula.

| Valor (Inteiro) | Descrição |
| --- | --- |
| 0 | Tesouraria |
| 1 | Contas a Receber |
| 2 | Contas a Pagar |
| 4 | Conta corrente |
| 10 | Cheque próprio |
| 11 | Cheque terceiro |
| 12 | Depósito de cheque |
| 13 | Endosso (Troca por título a receber) |
| 15 | Baixa por abatimento |
| 16 | Endosso (Troca por título a pagar) |
| 17 | Cartão |
| (vazio) | Manter campo Valor (valor **Padrão**) |

## Páginas relacionadas

* [Digitação de Notas manuais (F140GNF)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f140gnf.htm)
* [Controle de Bens / Bem / Individual (F670BEM)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f670bem.htm#F670BEM)
