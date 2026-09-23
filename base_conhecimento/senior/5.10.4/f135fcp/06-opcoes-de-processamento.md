# Opções de processamento

> **Fonte:** F135FCP - Formação de Cargas (via Pedidos) — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f135fcp.htm  
> **Trilha:** Ajuda por telas > Mercado > Gestão de Distribuição > Cargas > Formação  
> **Telas citadas:** E120IPD, F070FVE, F135LIB  
> **Identificadores de regras:** COM-135CGFCA01, COM-135CGFCA02, VEN-135AGRUP01

---
Gravar a cada pré-fatura

Para diminuir o consumo de memória, se definida, terá por finalidade gravar a pré-fatura após a mesma ter sido criada, reduzindo o consumo de memória ao processar a carga. Esta opção ficará gravada por usuário.

Observação

Esta opção não poderá ser utilizada juntamente com o identificador de regras COM-135CGFCA01. Utilize o identificador de regras COM-135CGFCA02 para consistir o pedido/pré-fatura.

Fechar a cada pré-fatura

Indica se o sistema deve fechar a carga a cada pré-fatura gerada. Essa funcionalidade só tem feito quando a opção gravar a cada pré-fatura estiver selecionada também, caso contrário essa funcionalidade não irá funcionar na rotina.

Gerar Pré-fatura por transação de item

Indicativo se as pré-faturas serão geradas conforme a transação do item do pedido. Dessa forma, para cada transação diferente do item de pedido será gerada uma nova pré-fatura.
Ao marcar esta opção a rotina irá automaticamente mudar a ordenação dos produtos para Filial/Pedido/Trans.Prod. a fim de que a grade (grade) de produtos seja ordenada por transação de produto, não permitindo uma ordenação diferente quando mostrar. Esta opção ficará gravada por usuário.

Agrupar pedidos por cliente

Faz a quebra de cargas de acordo com o indicativo presencial carregado do pedido. Exemplo de cenário: gerar apenas uma pré-fatura para dois ou mais pedidos com transações diferentes, porém do mesmo cliente, ao gerar uma carga.

## Lista de condições

* Filial;
* Cliente;
* Representante;
* Condição Pagamento;
* Marca;
* Percentual desconto 1, 2, 3, 4
* Percentual de oferta 1 e 2;
* Sequência de entregue (endereço de entrega);
* Sequência de cobrança Endereço de cobrança;
* Indicativo presencial do consumidor ou se tiver identificador VEN-135AGRUP01 e não agrupar o pedido;
* Indicativo se possui parcela especial;
* Data de agendamento no processo de cobrança.

**Observação**

Pedidos realizados pelo Centro de Distribuição não serão agrupados com os demais pedidos.

**Manter Informações de Transporte**

Quando marcado, ao final do processamento de geração da carga os campos referentes às **Informações de transporte** da tela não serão zerados, mantendo o que havia sido informado antes do processamento.

Mostrar itens em preparação

Indicativo se deverá considerar na geração da carga os itens de pedido com situação 8 (em preparação) e que a diferença entre as quantidades em aberto (E120IPD.QTDABE) e em análise (E120IPD.QTDRAE) seja maior que zero, ou seja, deve-se ter um saldo disponível para gerar novas pré-faturas.

## Exemplo

* Quantidade pedida com quantidade 100.
* Pedido está na situação 8 pois já possui quantidades em notas ou cargas com quantidade 50.
* Sobrou um saldo de 50 disponível.
* Assim, com o campo marcado irá mostrar o pedido com quantidade a faturar de 50.

Analisar Crédito

Indicativo de análise de crédito do cliente no fechamento. Quando marcado e se o cliente tiver problemas de crédito será exibida mensagem questionando a continuidade ou bloqueio do processo.

Exigir liberação de estoque

Quando esta opção estiver selecionada, a pré-fatura será gerada com a situação 8 – Sem Estoque / Em Requisição e a reserva exclusiva de itens na carga não será efetuada.

**Observação**

* A liberação da carga no estoque pode ser realizada na tela F135LIB, selecionando no campo Modalidade a opção Liberar Estoque. Desta maneira, serão exibidas as pré-faturas que possuem situação 8. Após a liberação, a pré-fatura terá a situação 2 - Em Preparação, gerando reservas exclusivas no estoque. Caso o pedido possuir reserva normal de estoque, essa reserva será mantida;
* Quando o parâmetro Gerar requisição ao fechar carga (F070FVE) estiver definido como "S - Sim", a tela se comportará como se o campo Exigir liberação de estoque estivesse marcado;
* Ao excluir ou cancelar a pré-fatura, as reservas exclusivas não serão mantidas, evitando que haja estoque negativo.

## Páginas relacionadas

* [COM-135CGFCA01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/com_135cgfca01.htm)
* [COM-135CGFCA02](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/com_135cgfca02.htm)
* [F135LIB](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f135lib.htm)
* [F070FVE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070fve.htm)
