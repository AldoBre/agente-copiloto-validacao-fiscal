# Identificar compra ou venda em movimentação do controle de entrada e saída

> **Fonte:** Processo para Controle de Entrada e Saída de Produtos (PEPS/FIFO) — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/processo-controle-entrada-saida-produto.htm  
> **Trilha:** Segmentos > Compliance  
> **Telas citadas:** F001TCP, F001TDC, F001TDV, F001TVE  
> **Identificadores de regras:** —

---
Para que o sistema identifique se uma compra ou venda deve movimentar o Controle de Entrada e Saída, ele irá se basear na transação da nota fiscal de entrada, saída ou cupom fiscal. Para isso, informe o campo **Mov. Contr. Ent. Prod.** nas telas de Transações de Compra e Venda (F001TDV, F001TVE, F001TDC ou F001TCP), guia Dados Gerais. Se o produto controlar entradas e saídas e a transação possuir o parâmetro como "S - Sim", o registro irá para o Controle, independentemente da origem (módulo Comercial ou Tributos).
