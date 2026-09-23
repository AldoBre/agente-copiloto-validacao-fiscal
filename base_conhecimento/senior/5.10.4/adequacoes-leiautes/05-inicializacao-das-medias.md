# Inicialização das médias

> **Fonte:** Adequação aos leiautes do SPED Fiscal — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/sped/fiscal-icms-ipi/adequacoes-leiautes.htm  
> **Trilha:** Segmentos > Compliance > Escriturações Fiscais Digitais (SPED) > SPED Fiscal (EFD ICMS/IPI)  
> **Telas citadas:** E660RSM  
> **Identificadores de regras:** —

---
**Importante**

Para gerar as médias do dia é necessário:

1. Integrar as notas fiscais ao módulo de **Tributos** (independentemente do cliente utilizar a opção **online** ou carregar o Controle por meio desta tela utilizando o módulo **Comercial**;
2. Atualmente, as médias do dia serão geradas apenas para filiais do MG, MS e RS;
3. O campo **Módulo Origem** deve ser igual a **Tributos**.

* A rotina deve ser executada uma única vez no primeiro dia da competência em que a empresa passar a entregar os registros de informações complementares de ICMS ST no SPED Fiscal;
* Não é possível inicializar as médias de um período anterior a 01/01/2021;
* A inicialização das médias grava, para cada produto, o saldo de unidades disponíveis no Controle e os valores médios de bases de cálculo e impostos ICMS, ICMS ST e FCP ST sobre o estoque. Tabela: E660RSM.
  + Se após a inicialização forem feitas alterações no Controle em registros anteriores, **será preciso fazer a inicialização novamente**;
  + Se já houver registros na tabela E660RSM para a filial, ao refazer a inicialização das médias **todos os registros da tabela E660RSM serão excluídos**, sendo necessário rodar a atualização de períodos posteriores à inicialização.
