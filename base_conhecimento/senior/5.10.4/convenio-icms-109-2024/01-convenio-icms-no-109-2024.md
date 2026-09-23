# Convênio ICMS nº 109/2024

> **Fonte:** Convênio ICMS nº 109/2024 — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/convenio-icms-109-2024.htm  
> **Trilha:** Segmentos > Compliance > Configurações para cálculos fiscais  
> **Telas citadas:** F001TVE, F024MSG, F440RCI  
> **Identificadores de regras:** —

---
Segmentos > Compliance > Configurações para cálculos fiscais  > Convênio ICMS nº 109/2024

O Convênio ICMS nº 109/2024 disponibiliza ao contribuinte que realizar a transferência interestadual entre estabelecimentos do mesmo titular a opção de:

* Transferir o crédito para o estabelecimento de destino da operação, correspondente ao imposto apurado nas operações anteriores (cláusula quarta do Convênio ICMS nº 109/2024 );

O crédito apropriado pelo estabelecimento destinatário será transferido pelo estabelecimento remetente, correspondendo ao imposto efetivamente pago nas operações anteriores, limitado à aplicação das alíquotas interestaduais do ICMS. Portanto, se a alíquota da compra for inferior à de saída, o crédito transferido será limitado ao valor tributado na operação anterior. Caso a operação anterior tenha sido isenta ou não tenha incidido ICMS, não haverá transferência de créditos.

O crédito a ser transferido deverá ocorrer mediante emissão de nota fiscal, com destaque do ICMS, conforme Ajuste SINIEF 33/2024 (DOU de 12.12.2024) conforme segue:

1. Natureza da Operação: o texto "Transferência de Mercadoria - Estabelecimentos mesmo titular". Para isso será necessário a utilização de uma transação de venda no item da nota fiscal (F001TVE) cujo campo Transferência Crédito ICMS seja definido como "S";
2. Informações Adicionais de Interesse do Fisco: o texto "Procedimento autorizado conforme Convênio ICMS nº 109/2024. Esta informação será adicionada a nota fiscal através do controle de mensagens do ERP (F024MSG) e controle de mensagem da transação de venda do item (F001TVE);
3. Código Fiscal de Operações e de Prestações - CFOP: um dos códigos do grupo "6.150 - Transferências de produção própria ou de terceiros", conforme o caso.

A emissão do referido documento fiscal será com finalidade 1 - NF-e Normal, CFOP 6.151/6.152. seguindo as demais disposições previstas no Ajuste relativo ao CST, base de cálculo e ICMS e deve antender os seguintes requisitos legais/operacionais:

1. A empresa deve estar definida para registrar o controle de entrada e saída dos produtos (Registra entrada e saída dos produtos igual a "S - Sim");
2. Deve ter notas fiscais de compra registradas para impostos (F440RCI);
3. A transação do item da nota fiscal deve ter indicativo de Transferência Crédito ICMS igual a "S - Sim";
4. O produto/derivação deve registrar o controle de entrada e saída para impostos (Reg. Ent.Sai igual a "S - Sim") e deve ser um produto do tipo "C-Comprado";
5. O cliente da nota fiscal de saída por transferência deve ser de mesma titularidade da filial que está emitindo a nota fiscal. O ERP não barra a geração da nota, mas o não atendimento deste requisito pode barrar a autorização da nota fiscal;
6. Código de Situação Tributária do item da nota fiscal - CST: o código 090.

O atendimento dos requisitos descritos faz com que o item da nota fiscal seja gerado com as seguintes características:

1. Valor Base de Cálculo do ICMS: "valor zerado";
2. Alíquota do imposto: "valor zerado";
3. Valor do ICMS: o valor do crédito a ser transferido, caso exista, deve obedecer aos limites previstos no Convênio ICMS nº 109/2024.

O valor do ICMS será definido utilizando como base de cálculo o menor valor entre o preço médio das notas fiscais de compra registradas na estrutura de controle de entrada e saída - valor das compras pelo saldo disponível das notas de compras, e o valor do item da nota fiscal.

O documento gerado (.XML) irá apresentar apenas o valor do ICMS e a mensagem de interesse do FISCO conforme segue:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Natureza da Operação | | | | |
| Transferência de Mercadoria - Estabelecimentos mesmo titular | | | | |
| CFOP | CST | Valor da base de cálculo | Alíquota do ICMS | Valor do ICMS |
| 6151 a 6156 | 90 | 0,00 | 0,00 | R$ Valor a ser transferido, caso exista |
| Informações adicionais de interesse do fisco | | | | |
| Procedimento autorizado conforme Convênio ICMS nº 109/24 | | | | |

**Importante**

O preço médio para cálculo de ICMS para atender ao convênio somente começa a ser calculado a partir da geração ou alteração de uma nota fiscal de compra.

## Páginas relacionadas

* [F001TVE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f001tve.htm)
* [F024MSG](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f024msg.htm)
* [F440RCI](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f440rci.htm)
