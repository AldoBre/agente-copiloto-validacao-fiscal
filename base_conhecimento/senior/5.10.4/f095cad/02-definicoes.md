# Definições

> **Fonte:** F095CAD - Cadastro de Fornecedores — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f095cad.htm  
> **Trilha:** Ajuda por telas > Cadastros > Clientes e Fornecedores > Fornecedores  
> **Telas citadas:** F095HFO, F439FIX  
> **Identificadores de regras:** CPR-440VLRMO02

---
Vide tela F095HFO.

**Percentual do Diferimento de ICMS relativo ao FCP**

Percentual do diferimento de ICMS relativo ao FCP sugerido para o cálculo do valor do diferimento de ICMS relativo ao FCP nos processos de compras e recebimento. Este campo não tem preenchimento obrigatório.

Tipo de Rateio Valor Conhecimento de Frete

Tipo de rateio do valor do conhecimento de frete para efetuar o movimento de estoque (acerto).

**Data de Início de Vigência Contr. Previdenciária**

Data de início de vigência de contribuição previdenciária.

**Data Final de Vigência Contr. Previdenciária**

Data final de vigência de contribuição previdenciária.

**Observação**

A rotina de geração de NF no processo de Compras - Fixação de Preços (F439FIX) é feito através dos campos Data de Início de Vigência Contr. Previdenciária e Data Final de Vigência Contr. Previdenciária, que possuem a finalidade de não reter o FUNRURAL/GILRAT para quando informado um período de vigência de uma liminar, tendo o seguinte funcionamento:

* Quando o indicativo da forma de tributação da CP for igual a 2 (sobre a folha de pagamento) e a data atual estiver dentro do periodo de vigência informado, não irá reter o FUNRURAL / GILRAT (valor = 0)
* Quando o indicativo da forma de tributação da CP for igual a 2 (sobre a folha de pagamento) e o período de vigência estiver vencido, o processo será bloqueado e uma mensagem informativa será apresentada solicitando que o cadastro do fornecedor seja alterado
* Quando o indicativo da forma de tributação da CP for igual a 1 (sobre a comercialização da sua produção), não será considerado o período de vigência e irá reter normalmente o FUNRURAL / GILRAT (valor calculado)

**Importante**

Há uma particularidade em relação às movimentações de estoque em uma nota fiscal de frete ligada a uma nota fiscal de industrialização, onde o sistema não verifica o campo **Tipo de Rateio Valor Conhecimento de Frete** no fornecedor. Isso ocorre com notas fiscais do tipo **4 - Industrialização**, que podem não gerar um movimento para cada item, sendo necessário aplicar o cálculo com base no valor, desconsiderando o referido campo.

**Obs.:** o identificar de regras CPR-440VLRMO02 pode ser utilizado para customizar o cálculo padrão do sistema.

Emitir Contra Nota

Permite indicar entre "S - Sim" ou "N - Não" para emitir contra nota para as notas fiscais de entrada do tipo 1, 9 ou 11.

## Páginas relacionadas

* [F095HFO](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f095hfo.htm)
* [Compras -  Fixação de Preços (F439FIX)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f439fix.htm)
* [CPR-440VLRMO02](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/cpr_440vlrmo02.htm)
