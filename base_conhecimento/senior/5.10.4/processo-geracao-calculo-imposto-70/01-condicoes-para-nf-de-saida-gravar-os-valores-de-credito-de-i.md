# Condições para NF de saída gravar os valores de crédito de ICMS e ICMS ST

> **Fonte:** Cálculo do imposto 70 - ICMS ST Complementar — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/processo-geracao-calculo-imposto-70.htm  
> **Trilha:** Ajuda por telas > Controladoria > Gestão de Tributos > Operações e Cálculos Fiscais > Cálculos > Apuração > F661IA5  
> **Telas citadas:** E001TNS, F019TIS  
> **Identificadores de regras:** —

---
Não terão direito ao ressarcimento as notas fiscais de saída que se enquadrarem em uma das condições abaixo:

* Campo **DIFAL como ICMS ST** da tela F019TIS igual a **S-Sim**;
* Nota fiscal de retorno (TipNfs igual a 5 - NF Retorno (Industrialização) ou igual a 6 - NF Retorno (Outros).

Terão direito ao ressarcimento as notas fiscais de saída que se enquadrarem em umas das condições abaixo:

* Não atender nenhum dos requisito citados acima;
* Código de Situação Tributária de ICMS com o segundo dígito igual a 4 (Isenta - não incidência do ICMS);
* CFOP inicializada em 6 (inter-estadual);
* CFOP inicializada em 7 ou CFOP terminada em 55 (Exportação). Obs.: CFOP (E001TNS.COMNAT) não é código de transação (E001TNS.CodTns).
