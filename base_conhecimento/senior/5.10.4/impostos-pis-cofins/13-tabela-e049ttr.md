# Tabela E049TTR

> **Fonte:** PIS/COFINS — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/impostos_pis_cofins.htm  
> **Trilha:** Segmentos > Compliance > Configurações para cálculos fiscais > Impostos  
> **Telas citadas:** E049TTR, F049TTR  
> **Identificadores de regras:** —

---
Ao incluir um item em pedido, nota fiscal de saída, ordem de compra ou nota fiscal de entrada, é apresentada a mensagem "Na tabela de Tributação - E049Ttr não foi informado o percentual para cálculo da base calculada do imposto 41 e grupo fiscal GAF para este período com faixa de valor de R$12.000,00.". Por que esta mensagem ocorre?

Esta mensagem ocorre porque o sistema está configurado para calcular PIS/COFINS a recuperar/faturamento e não há registro na tabela "E049TTR". É necessário preencher esta tabela a partir da tela "Cadastros > Controladoria > Tributos > Tabelas de tributação (F049TTR)".
