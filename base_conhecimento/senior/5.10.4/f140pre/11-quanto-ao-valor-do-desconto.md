# Quanto ao valor do desconto

> **Fonte:** F140PRE - Preparação da Nota Fiscal de Saída — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f140pre.htm  
> **Trilha:** Ajuda por telas > Mercado > Gestão de Faturamento e Outras Saídas > Notas Fiscais de Saída  
> **Telas citadas:** F001TVE, F140PRE  
> **Identificadores de regras:** —

---
* O sistema nunca aumentará o valor de desconto, mesmo que seja faturado uma quantidade superior a quantidade do pedido;
* A alteração automática do valor de desconto proveniente do pedido irá ocorrer na tela F140PRE, no momento que for gerada uma nota fiscal com a opção Via Pedido (2) e a quantidade a faturar for menor que a quantidade aberta no pedido, exceto quando:
  + O valor do desconto não é alterado automaticamente quando a quantidade pedida for maior que o saldo disponível para faturamento.
  + Neste caso, ao carregar este pedido na tela F140PRE, ocorre que por não ter saldo suficiente, o campo Qtde.Fat. fica zerado;
  + Ao informar uma quantidade no campo Qtde.Fat., o sistema emite uma mensagem, permitindo que o usuário defina como deseja calcular o valor de desconto;
  + A mensagem apresenta o valor de desconto original e o cálculo do valor de desconto com base no percentual que está sendo faturado:

![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/images/mercado/f140pre-valor-desconto.png)

## Ao clicar em Proporção

* O sistema irá calcular o valor do desconto proporcional a quantidade faturada. Exemplo:
  + Se a quantidade a faturar for a metade da quantidade do pedido, então, o valor do desconto será reduzido pela metade;
  + O cálculo do valor do desconto é apresentado na mensagem.

## Ao clicar em Original

* O sistema mantém o valor de desconto original.

Valor a Devolver

Valor de devolução do item, sem quantidade. Esse campo fica disponível quando:

1. O Tipo de nota é "2 - NF Devolução";
2. Em **Opções**, está selecionada "Via Nota Entrada";
3. A transação do item está configurada como Nota fiscal devolução de valor na tela de Transações de Vendas (F001TVE), guia Dados Gerais 2.

## Páginas relacionadas

* [Transações de Vendas (F001TVE)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f001tve.htm)
