# Mensagem ao incluir item na nota

> **Fonte:** Rotinas de ICMS — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/impostos-icms.htm#mensagem  
> **Trilha:** Segmentos > Compliance > Configurações para cálculos fiscais > Impostos  
> **Telas citadas:** —  
> **Identificadores de regras:** —

---
MENSAGEM: Valor contábil é diferente do somatório de Isentas ICMS + Outras ICMS + Base de Cálculo ICMS + Valor ICMS Substituto. Prosseguir?

A mensagem em questão é apresentada nativamente pelo ERP. Esta mensagem é apresentada para informar/alertar o usuário sobre uma possível divergência que pode ocorrer nos livros fiscais (esta consistência é antiga). A consistência pode ocorrer somente para determinados produtos ou situações, pois depende de vários assinalamentos no cadastro do produto/transação. Esta consistência não interfere no processo é somente um alerta/aviso conforme informado anteriormente.

Abaixo segue detalhes do processo que é verificado para que ocorra a consistência nativa do ERP:

1. A transação deve estar marcada ara recuperar ICMS;
2. O produto de estar para recuperar ICMS;
3. O fornecedor deve estar para recuperar ICMS.

Se o sistema estiver configurado para recuperar ICMS, serão somados os valores de: ICMS isentas + ICMS outras + ICMS base + ICMS valor verificando se o total é igual ao valor líquido do item. Se não for, exibe a mensagem.
