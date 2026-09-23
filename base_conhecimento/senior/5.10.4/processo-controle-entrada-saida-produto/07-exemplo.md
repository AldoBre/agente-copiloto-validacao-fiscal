# Exemplo:

> **Fonte:** Processo para Controle de Entrada e Saída de Produtos (PEPS/FIFO) — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/processo-controle-entrada-saida-produto.htm  
> **Trilha:** Segmentos > Compliance  
> **Telas citadas:** —  
> **Identificadores de regras:** —

---
O produto 510101 possui duas notas de entrada, que foram registradas na inicialização, a nota 5.369 e a nota 32.541. Depois, foi feita a entrada da nota 74.859 com quantidade 1.000,00 do mesmo produto. Ao consultar as entradas na tela Manutenção de Controle de Entrada de Produtos por meio da opção Consultar entradas, verifica-se que foi registrada a nota 74.859 para o produto 510101.

![](../resources/images/processo-controle-entrada-saída-produtos/peps 1_thumb_0_48.png)

Todas as notas fiscais de saída geradas para os produtos controlados pelo PEPS, consumirão a quantidade disponível em estoque da nota fiscal de entrada mais antiga. Por exemplo, foi gerada uma nota fiscal de saída para o produto 510101 com quantidade 1.000,00. Ao consultar os registros de entrada e saída na tela Manutenção de Controle de Entrada de Produtos, verifica-se que nas entradas do produto 510101, foi consumida uma quantidade de 1.000,00 da nota fiscal de entrada 32.541, que foi a primeira nota de entrada gerada para este produto.

![](../resources/images/processo-controle-entrada-saída-produtos/peps 2_thumb_0_48.png)

Gerando outra nota fiscal de saída para o produto 510101 com quantidade 1.000,00, verifica-se que foi consumida a quantidade de 500,00 que havia ainda disponível na nota de entrada 32.541, e mais 500,00 da nota seguinte 5.369.

![](../resources/images/processo-controle-entrada-saída-produtos/peps 3_thumb_0_48.png)

## Páginas relacionadas

* [Manutenção de Controle de Entrada de Produtos](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f440rci.htm)
