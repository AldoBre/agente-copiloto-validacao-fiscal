# Cadastro de formas de pagamento (F066FPG)

> **Fonte:** F000PPD -  Configuração de parâmetros dinâmicos — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000ppd.htm  
> **Trilha:** Ajuda por telas > Cadastros  
> **Telas citadas:** F066FPG  
> **Identificadores de regras:** —

---
#### FORMAPAGAMENTO.EXIGECONDICAOPAGAMENTO

Indica se a forma de pagamento exige ou não condição de pagamento somente no processo de venda.

| Valor (Lista) | Descrição |
| --- | --- |
| N | Não (valor **Padrão**) |
| S | Sim |

#### FORMAPAGAMENTO.IMPRESSAOBOLETO.AUTOMATICO

Responsável por indicar se os boletos deverão ser impressos na loja, quando a loja receber um retorno de integração de venda que gerou boleto. Quando esse parâmetro for cadastrado como **N** em uma forma de pagamento que gera boleto, quando os boletos forem integrados com a loja, eles não serão impressos.

| Valor | Descrição |
| --- | --- |
| N | Não |
| S | Sim (valor **Padrão**) |

#### FORMAPAGAMENTO.PORTADORBANCO

Informe o código do portador que deseja utilizar como padrão. Deve ser um portador cadastrado no sistema.

Observações

* Ao alterar manualmente a forma de pagamento da nota/parcela/pedido, o portador das parcelas não será alterado.
* O valor do parâmetro dinâmico é obtido com base na Forma de Pagamento da Nota Fiscal de Saída, e não na Forma de Pagamento da Parcela da Nota. Caso seja necessário considerar a Forma de Pagamento da Parcela, consulte a documentação do parâmetro global SugPorFpg.

#### FORMAPAGAMENTO.CARTEIRABANCO

Informe o código da carteira, obrigatoriamente cadastrada no sistema, que deseja utilizar como padrão.

Observações

* Ao alterar manualmente a forma de pagamento da nota/parcela/pedido, a carteira das parcelas não será alterada.
* O valor do parâmetro dinâmico é obtido com base na Forma de Pagamento da Nota Fiscal de Saída, e não na Forma de Pagamento da Parcela da Nota. Caso seja necessário considerar a Forma de Pagamento da Parcela, consulte a documentação do parâmetro global SugCrtFpg.

## Páginas relacionadas

* [SugPorFpg](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#SugPorFpg)
* [SugCrtFpg](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#SugCrtFpg)
