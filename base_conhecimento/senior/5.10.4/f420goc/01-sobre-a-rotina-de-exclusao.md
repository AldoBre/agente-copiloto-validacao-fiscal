# Sobre a rotina de exclusão:

> **Fonte:** F420GOC - Ordem de Compra Agrupada — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f420goc.htm  
> **Trilha:** Ajuda por telas > Suprimentos > Gestão de Compras > Ordens de Compra  
> **Telas citadas:** E420OCP, F099UCA, F420GOC, F420OCB, F426CEQ  
> **Identificadores de regras:** —

---
## 1 - Primeiramente, a rotina de exclusão executará a consistência básica, aplicada à todas as Ordens de Compra, antes de proceder efetivamente com a exclusão:

1.1 - Verifica se a Ordem de Compra foi gerada pela produção. Caso tenha sido, a exclusão não será permitida.

1.2 - Verifica se a Ordem de Compra está com a situação "9 - Digitada". Caso esteja com uma situação diferente, a exclusão não será permitida.

1.3 - Verifica se a Ordem de Compra está em processo de aprovação, ou seja, se algum usuário de qualquer nível de aprovação já a aprovou; caso esteja em processo de aprovação, a exclusão não será permitida.

1.4 - Verifica se a Ordem de Compra é a base de outra Ordem de Compra, nos casos em que tenha sido gerada através da tela Ordem de Compra via Ordem de Compra Base (F420OCB); caso seja base de outra Ordem de Compra, a exclusão não será permitida.

1.5 - Verifica se a Ordem de Compra é proveniente de uma coleta; caso tenha sido gerada via coleta, a exclusão não será permitida pela tela Ordem de Compra Agrupada (F420GOC), mas poderá ser realizada pela tela Definição de Fornecedores em Coletas de Produtos (F426CEQ).

1.6 - Verifica se a Ordem de Compra é proveniente de mercado eletrônico; caso tenha sido gerada dessa forma, a exclusão não será permitida pela tela Ordem de Compra Agrupada (F420GOC), mas poderá ser cancelada através do mercado eletrônico.

## 2 - Após as consistências básicas já descritas acima, caso exista integração com o Aplicativo Gestor Senior:

2.1 - Caso exista integração das aprovações multinível de ordens de compra com o Aplicativo Gestor Senior, nenhuma ordem de compra poderá ser excluída, e sim, apenas cancelada. Isso mantém a integridade entre o ERP e o aplicativo, evitando erros de integração. Apenas usuários ligados aos níveis de aprovação do documento podem cancelar. Caso o usuário seja um usuário aprovador válido, será questionado se deseja realmente cancelar o documento, onde, optando pelo cancelamento, a ordem de compra será mantida no ERP com situação "5 - Cancelada", reprovando também o processo de aprovação do documento e a tarefa será expirada no aplicativo após o envio das tarefas.

2.2 - Caso a ordem de compra seja de fato cancelada antes de sua integração com o aplicativo, ela não será mais integrada.

## 3 - Se não existir integração com o Aplicativo Gestor Senior outras consistências serão executadas caso haja configuração de aprovação multinível para ordens de compra, conforme segue:

3.1 - Verifica se o usuário logado no ERP é o mesmo que gerou a ordem de compra; caso atenda a essa condição, o usuário terá permissão para realizar a exclusão.

3.2 - Se a condição acima não for atendida, é verificado se o usuário logado possui vínculo com algum nível necessário para a aprovação da ordem de compra; caso atenda a essa condição, o usuário terá permissão para realizar a exclusão.

3.3 - Caso nenhuma das condições acima seja atendida, é verificado se o usuário logado é o superior imediato do usuário que gerou a ordem de compra; caso atenda a essa condição, o usuário terá permissão para realizar a exclusão.

3.4 - Caso nenhuma das três condições acima seja atendida, será realizada uma busca pelos usuários subordinados ao usuário logado no ERP. Em seguida, conferido se o usuário que gerou a ordem de compra está incluído nessa lista de subordinados; caso atenda a essa condição, o usuário terá permissão para realizar a exclusão.

3.5 - Caso alguma das verificações acima seja atendida, o usuário será questionado se deseja realmente excluir a ordem de compra. Ao optar por "Sim", a ordem de compra será excluída do sistema.

3.6 - Se nenhuma das verificações for atendida, será exibida uma mensagem informando que o usuário não tem permissão para excluir/cancelar a ordem de compra.

**Observações**

* Nos casos onde a ordem de compra já é inserida no sistema com situação aprovada pelo controle de aprovação multinível (E420OCP.SITAPR = "APR") a exclusão/cancelamento acontece normalmente caso as consistências básicas sejam atendidas. Se existir configuração para integração com o Aplicativo Gestor Senior estas ordens de compra que já nascem aprovadas, não serão integradas com o aplicativo.
* A configuração para obter os níveis hierárquicos de usuários é feita através da tela Cadastro de Usuários (F099UCA), no campo Superior Imediato.

## Páginas relacionadas

* [F420OCB](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f420ocb.htm)
* [F426CEQ](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f426ceq.htm)
* [F099UCA)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f099uca.htm)
