# Campos

> **Fonte:** F075PRO - Cadastro de Produtos — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075pro.htm  
> **Trilha:** Ajuda por telas > Cadastros > Produtos e Serviços > Produtos  
> **Telas citadas:** —  
> **Identificadores de regras:** —

---
Produto

No que se refere a codificação de produtos, devem ser
tomados alguns cuidados na codificação. Não é
aconselhável utilizar alguns caracteres na formação dos
códigos, por exemplo aspas (A), apóstrofo (A;),
percentual (A%), espaços (A A) e pontos (A.A). Esses caracteres provocam erro de sintaxe
nos SQLs executados, prejudicando o funcionamento normal
das rotinas.

Observação

Quando o campo Usa Produto X Fornecedor estiver como S, ao alterar determinados campos da tela a mensagem Produto usa ligação Fornecedor X Produto. Deseja atualizar este parâmetro fiscal nas Ligações? é exibida. O parâmetro global ExiAtuFis permite configurar outras opções de exibição:

* P - Perguntar: a mensagem sempre será exibida, questionando o usuário qual ação será tomada (Valor Padrão do Parâmetro)
* S - Sim: a mensagem não será exibida e será automaticamente selecionada a opção Sim
* N - Não: a mensagem não será exibida e será automaticamente selecionada a opção Não
