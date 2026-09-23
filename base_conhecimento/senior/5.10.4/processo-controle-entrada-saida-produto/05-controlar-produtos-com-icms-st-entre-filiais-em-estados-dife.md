# Controlar produtos com ICMS ST entre filiais em estados diferentes

> **Fonte:** Processo para Controle de Entrada e Saída de Produtos (PEPS/FIFO) — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/processo-controle-entrada-saida-produto.htm  
> **Trilha:** Segmentos > Compliance  
> **Telas citadas:** F075APF, F075GFP, F075PFI, F075PRO  
> **Identificadores de regras:** —

---
Quando uma empresa possui duas ou mais filiais em estados diferentes e comercializa produtos com ICMS ST em um estado, enquanto em outro o produto não é controlado pelo ICMS ST, este último não pode ser considerado no Controle de Entrada e Saída; o primeiro, sim.

**Exemplo:** no estado de SC, o produto A não tem ICMS ST. No estado do RS, sim; ou seja, deve passar pelos processos de ressarcimento, restituição e complementação. Como o processo parte do produto registrado nas estruturas de Entrada e Saída, se o produto para determinada filial não estiver no Controle, ele não será apresentado na declaração para o estado. Diante disso, é necessário parametrizar a nível de filial se o produto deve ou não entrar no Controle:

Ao tratar uma nota/cupom fiscal, o sistema analisa o conteúdo do campo **Reg. entradas e saídas para controle de impostos** das telas F075PFI/F075APF, juntamente com as parametrizações das telas F075PRO/F075GFP:

* **Quando não há ligação do produto com a filial**: o sistema gera um registro no Controle de Entrada e Saída de produtos apenas se na derivação for informado **S-Sim** para o campo **Reg. entradas e saídas para controle de impostos**;
* **Quando há ligação do produto com a filial:** o sistema gera um registro no Controle de Entrada e Saída de produtos apenas se na derivação e na ligação for informado **S-Sim** para o campo **Reg. entradas e saídas para controle de impostos**;
* Caso contrário, o sistema não gera um registro no Controle de Entrada e Saída de produtos.
