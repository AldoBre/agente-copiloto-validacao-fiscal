# Cadastro de clientes (F085CAD)

> **Fonte:** F000PPD -  Configuração de parâmetros dinâmicos — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000ppd.htm#cadcli  
> **Trilha:** Ajuda por telas > Cadastros  
> **Telas citadas:** F085CAD  
> **Identificadores de regras:** —

---
#### CHEQUE.DIASVENCIMENTOMAXIMO

Configura o número (inteiro) máximo de dias para cheques pré-datados. Por exemplo, 1, 5, 10. Se informado zero ou vazio, significa que não deve validar.

Este parâmetro pode ser informado tanto por cliente como por filial.
Para recebimentos de títulos com cheque pré-datado, o sistema irá apenas emitir um alerta indicando que a data não é aceita ao invés de bloquear a operação. Será considerada a seguinte regra: caso exista apenas um cliente nos títulos selecionados, será utilizado o número de dias parametrizado no cliente. Se existir mais de um cliente ou se o cliente não tiver um número de dias parametrizado, será considerado o número de dias da filial.

No Retaguarda, a validação de dias será feita:

* No recebimento de Pedido cuja forma de pagamento seja cheque pré-datado;
* No Contas a Receber ao incluir um título com tipo Cheque;
* No Contas a Receber ao efetuar uma baixa de título com tipo Cheque;
* No Contas a Receber ao alterar o vencimento do título pela opção Mais opções > Alterar o vencimento.

#### CLIENTE.OBSERVACAO.MOTIVO.PADRAO

Define o código (valor inteiro) do motivo padrão para observação de clientes, quando o tipo de observação for diferente de "R - Recuperação financeira" e o motivo não informado.

Este parâmetro serve para controlar a integração no Retaguarda, quando receber a integração de observações de clientes. Quando o campo Tipo de observação for igual a "R - Recuperação financeira", da tela Observações do Cliente, o sistema irá assumir o valor informado no parâmetro. Quando não informado na integração, o sistema irá assumir o valor informado no parâmetro.

#### CLIENTE.OBSERVACAO.MOTIVO.PADRAO.RECUPERACAOFINANCEIRA

Define o código (valor inteiro) do motivo de padrão para observação de clientes quando tipo de observação for "R - Recuperação financeira".

Este parâmetro serve para controlar a integração no Retaguarda, quando receber a integração de observações de clientes. Quando o campo Tipo de observação for igual a "R - Recuperação financeira", da tela Observações do Cliente, o sistema irá assumir o valor informado no parâmetro. Quando não informado na integração, o sistema irá assumir o valor informado no parâmetro.

#### CLIENTE.PERMITE\_ENTRADA\_MENOR\_CONDICAO\_PAGAMENTO

Indica se é permitido diminuir o valor de entrada calculado pela condição de pagamento para o cliente.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não (valor **Padrão**) |
| 1 | Sim |

#### CONTRIBUINTE.ICMS.MONOFASICO

Este parâmetro indica se o cliente é contribuinte de ICMS Monofásico a fim de fazer a partilha entre o estado de origem e destino na apuração do imposto 78. Caso não esteja preenchido, considera como **não contribuinte**. Valores: "N - Não" e "S - Sim".

## Páginas relacionadas

* [ICMS Monofásico](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/icms-monofasico.htm)
* [apuração](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/icms-monofasico.htm#apuracao)
