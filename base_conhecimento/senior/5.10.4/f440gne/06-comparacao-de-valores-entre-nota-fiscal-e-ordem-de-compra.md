# Comparação de valores entre nota fiscal e ordem de compra

> **Fonte:** F440GNE - Nota Fiscal de Entrada Agrupada — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f440gne.htm  
> **Trilha:** Ajuda por telas > Suprimentos > Gestão de Recebimento > Notas Fiscais de Entrada  
> **Telas citadas:** F420GOC  
> **Identificadores de regras:** —

---
No fechamento da nota fiscal de entrada, o sistema compara o valor líquido da nota fiscal com o valor líquido da ordem de compra vinculada. Se a diferença ultrapassar os limites configurados no Cadastro de Usuários, o sistema exibe a mensagem "Diferença entre o valor total da Nota Fiscal e da Ordem de Compra é maior que o valor permitido para o usuário."

**Importante**

Essa comparação só é realizada quando os campos de moeda das despesas acessórias da Ordem de Compra (Moeda do Frete, Moeda do Frete de Importação, Moeda do Seguro de Importação e Moeda de Outras Despesas de Importação), na tela de Valores da OC (botão Valores da tela Ordem de Compra Agrupada - F420GOC), estiverem todos configurados na moeda da empresa. Se qualquer um desses campos estiver em moeda diferente da moeda da empresa, o sistema considera a Ordem de Compra como importação e não realiza a comparação, pois o cálculo não contempla a conversão cambial dessas despesas.

| Campo | Local (Tela) | Descrição | Comportamento |
| --- | --- | --- | --- |
| Moeda do Frete / Frete de Importação / Seguro de Importação / Outras Despesas de Importação | Valores da Ordem de Compra | Define a moeda de cada despesa acessória da OC | Se algum desses campos estiver em moeda estrangeira, a comparação de valores não é feita no fechamento da NF |
| Diferença de valor aceita entre NF e OC | Cadastro de Usuários, aba de parâmetros de compras | Valor máximo de diferença tolerado | Acima desse valor, a mensagem de divergência é exibida |
| Diferença percentual aceita entre NF e OC | Cadastro de Usuários, aba de parâmetros de compras | Percentual máximo de diferença tolerado | Acima desse percentual, a mensagem de divergência é exibida |
