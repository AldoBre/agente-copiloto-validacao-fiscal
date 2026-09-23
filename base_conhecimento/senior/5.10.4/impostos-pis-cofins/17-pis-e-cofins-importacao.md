# PIS e COFINS Importação

> **Fonte:** PIS/COFINS — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/impostos_pis_cofins.htm  
> **Trilha:** Segmentos > Compliance > Configurações para cálculos fiscais > Impostos  
> **Telas citadas:** F001TCP, F022CLF, F075PRO, F095CAD, F403FPR  
> **Identificadores de regras:** —

---
Para gerar o PIS/COFINS importação e a recuperar em notas de entrada de importação, são necessários os seguintes passos:

**Cadastro Fornecedores (F095CAD):**

* Para o cadastro de fornecedores, acesse: Cadastros > Clientes e Fornecedores > Fornecedores > Cadastro (F095CAD) e defina os campos da seguinte maneira:
  + No campo Recupera PIS, selecione a opção "S - Sim";
  + No campo Recupera COFINS, selecione a opção "S- Sim";
  + No campo % Recuperação PIS Diferenciado, informe o percentual de pis a recuperar diferenciado, se houver;
  + No campo % Recuperação COFINS Diferenciado, informe o percentual de cofins a recuperar diferenciado, se houver.

**Cadastro de Produto (F075PRO):**

* Acesse Cadastros > Produtos e Serviços > Produtos > Individual (F075PRO) e utilize os seguintes processos:
  + No campo Recupera PIS, selecione a opção "S - Sim";
  + No campo Recupera COFINS, selecione a opção "S - Sim";
  + No campo Calcula PIS importação, selecione a opção "S - Sim";
  + No campo Calcula COFINS importação, selecione a opção "S - Sim";
  + No campo % PIS importação Diferenciado, informar o percentual de importação diferenciado desejado;
  + No campo % COFINS importação Diferenciado, informar o percentual de importação diferenciado desejado.

**Transações de Compras (F001TCP):**

* Acesse Cadastros > Transações > Parâmetros por Gestão > Compras > Ordem Compra / NF Entrada / Fatura (F001TCP):
  + No campo Recupera PIS, selecione a opção "S - Sim";
  + No campo Recupera COFINS, selecione a opção "S - Sim";
  + No campo Calcula PIS importação, selecione a opção "S - Sim";
  + No campo Calcula COFINS importação, selecione a opção "S - Sim".

**Cadastro de Classificação Fiscal (F022CLF):**

* Acesse Cadastros > Mercado e Suprimentos > Parâmetros Fiscais > Classificações Fiscais > Individual (F022CLF):
  + No campo Recupera PIS, selecione a opção "S - Sim";
  + No campo Recupera COFINS, selecione a opção "S - Sim";
  + No campo % PIS, informe o valor desejado. Serve tanto para o % de importação quanto para o % a recuperar nas notas de importação;
  + No campo % COFINS, informe o valor desejado. Serve tanto para o % de importação quanto para o % a recuperar nas notas de importação.

  Atenção

  Caso o sistema não encontre a parametrização do % de importação, nem o % a recuperar nos outros cadastros, como por exemplo: produto, fornecedor ou ligação produto X fornecedor, ele assumirá os valores informados, no campo % PIS e % COFINS, na tela de Classificação Fiscal (F022CLF) tanto para o % de importação, quanto para o % a recuperar do item nas notas de entrada de importação. Se a classificação estiver informada no cadastro do produto.

**Ligação Fornecedor X Produtos Individual (F403FPR):**

* Acesse Cadastros > Clientes e Fornecedores > Fornecedores > Ligações > Fornecedor X Produtos > Individual (F403FPR):
  + No campo Recupera PIS, selecione a opção "S - Sim";
  + No campo Recupera COFINS, selecione a opção "S - Sim";
  + No campo Calcula PIS importação, selecione a opção "S - Sim";
  + No campo Calcula COFINS importação, selecione a opção "S - Sim";
  + No campo % PIS importação Diferenciado, informar o percentual de importação diferenciado desejado;
  + No campo % COFINS importação Diferenciado, informar o percentual de importação diferenciado desejado;
  + No campo % PIS Recuperar, informar o percentual a recuperar desejado;
  + No campo % COFINS Recuperar, informar o percentual a recuperar desejado.

  Atenção

  Para que seja possível editar esses campos e para que o sistema considere esses valores na nota de entrada de importação, é necessário informar no campo "Usa Produto X Fornecedor", da tela F075PRO, o valor de "S". Dessa forma o sistema irá buscar os parâmetros fiscais da ligação Produto X Fornecedor e não dos demais cadastros

**Hierarquia de Parâmetros**

* Para o % de importação diferenciado:
  + 1. Tela F403FPR, campos % PIS/COFINS importação Diferenciado se a ligação: "Produto X Fornecedor" existir;
  + 2. Tela F075PRO, campos % PIS/COFINS importação Diferenciado;
  + 3. Tela F022CLF, campos % PIS/COFINS se a classificação estiver informada no produto.
* Para o % a recuperar:
  + 1. Tela F403FPR, campos % PIS/COFINS Recuperar se a ligação: "Produto X Fornecedor" existir;
  + 2. Tela F095CAD, campos % Recuperação PIS/COFINS Diferenciado;
  + 3. Tela F022CLF, campos % PIS/COFINS se a classificação estiver informada no produto.

Após essas etapas, será possível lançar o PIS/COFINS importação e a recuperar nas notas fiscais de entrada de importação.
