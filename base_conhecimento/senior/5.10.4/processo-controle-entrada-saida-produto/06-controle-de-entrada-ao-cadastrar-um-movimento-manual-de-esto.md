# Controle de Entrada ao cadastrar um movimento manual de estoque pela tela F210MVP

> **Fonte:** Processo para Controle de Entrada e Saída de Produtos (PEPS/FIFO) — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/processo-controle-entrada-saida-produto.htm  
> **Trilha:** Segmentos > Compliance  
> **Telas citadas:** F210MVP, F215FES, F440RCI  
> **Identificadores de regras:** —

---
Ao cadastrar um movimento manual de estoque pela tela Geração Individual de Movimentos de Estoque (F210MVP) serão verificadas as seguintes informações:

* Movimento de estoque deve ser de "E - Entrada";
* Produto deve estar parametrizado para Registrar entradas e saídas de produtos;
* Produto deve estar parametrizado para ser Vendido;
* Produto deve ser do tipo Comprado ou Produzido que pode ser vendido (misto);
* Movimento não deve ter vínculo com Nota Fiscal de Entrada ou Saída;
* Quantidade do movimento deve ser maior que zero;
* Tipo do estoque movimentado deve ser "NO - Normal".

Dessa forma, se o movimento manual de estoque gerar o Controle de Entrada, ao salvá-lo será gravado um registro na tela Manutenção de Controle de Entrada de Produtos (F440RCI). Esse registro não terá vinculo com Nota Fiscal de Entrada e Saída e seus valores de ICMS ST serão gerados conforme a parametrização de ICMS ST Presumido.

Na rotina de Fechamento de Estoque (acionada pela tela Fechamento dos Estoques (F215FES) ou pelo web service com.senior.g5.co.mcm.est.estoques, porta Fechar), nos processamentos onde for gerado um movimento de acerto que ajuste quantidade, seja gerado também o Controle de Entrada e Saída de Produtos para controle de imposto.

Será gerado um registro para cada movimento de acerto de estoque. Para consultar os registros de Controle de Entrada e Saída gerados, acesse a tela de Manutenção de Controle de Entrada de Produtos (F440RCI).

Além disso, para que o Controle de Entrada e Saída de Produtos seja atualizado quando o fechamento de estoque estiver sendo regerado, ou seja, quando processado novamente um fechamento de estoque, serão excluídos os movimentos de acerto gerados anteriormente e serão gerados novos.

## Páginas relacionadas

* [F440RCI](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f440rci.htm)
