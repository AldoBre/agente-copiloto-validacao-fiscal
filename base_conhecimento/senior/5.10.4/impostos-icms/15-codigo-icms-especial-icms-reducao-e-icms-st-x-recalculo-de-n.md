# Código ICMS especial, ICMS redução e ICMS ST x recálculo de nota de devolução

> **Fonte:** Rotinas de ICMS — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/impostos-icms.htm#codigos-recalculo  
> **Trilha:** Segmentos > Compliance > Configurações para cálculos fiscais > Impostos  
> **Telas citadas:** F070FVE  
> **Identificadores de regras:** —

---
Ao fazer uma devolução e recalcular a nota, o sistema está apagando o código de ICMS Especial/Redução e ICMS ST no item da nota.

Isto pode ocorrer quando há recálculo na devolução. Neste caso, o sistema faz uma nova busca destes códigos.

Nas notas fiscais de devolução de venda ainda deve ser observado o parâmetro Buscar valores no recálculo das N.F.S constante na guia Vendas 2 da tela Cadastros > Filiais > Parâmetros por Gestão > Vendas e Faturamento (F070FVE).

Se este parâmetro estiver configurado igual a S(Sim) ou P(Perguntar) e o usuário optar por Sim na mensagem Deseja buscar os valores padrões(Preços/Impostos) para os itens? apresentada ao recalcular a nota, o sistema fará a busca novamente destes códigos.
