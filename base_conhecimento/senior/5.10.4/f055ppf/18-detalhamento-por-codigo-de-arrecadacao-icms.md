# Detalhamento por Código de Arrecadação - ICMS

> **Fonte:** F055PPF - Configuração de Impostos para a Filial — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f055ppf.htm  
> **Trilha:** Ajuda por telas > Cadastros > Controladoria > Tributos  
> **Telas citadas:** —  
> **Identificadores de regras:** —

---
Quando houver detalhamento de operação da transação a apuração do imposto 2 - ICMS gera um o título a pagar e/ou guia de recolhimento para cada detalhamento cadastrado.

O sistema totaliza por código de arrecadação os valores das notas fiscais conforme as transações parametrizadas na respectiva tela.

Exemplo:

* Código de Arrecadação: 1449;
* Transações: 1101, 1102, 5101, 5102 entre outras.

O total por código de arrecadação é obtido através da operação: **Notas fiscais de saída - notas fiscais de entrada**. Caso possuir mais notas fiscais de entrada que notas fiscais de saída o sistema mantem **0 como imposto a pagar**.

Período

Indica a periodicidade do imposto. Este campo é obrigatório e possui as seguintes opções:

* L - Livre;
* O - Diário;
* U - Quadrimestral;
* R - Semestral;
* S - Semanal;
* B - Bimestral;
* D - Decendial;
* Q - Quinzenal;
* M - Mensal;
* T - Trimestral;
* A - Anual.

Dias Vcto. (Dias Vencimento)

Indica o Número de dias após a data final de apuração que incidirá o vencimento do imposto.

Início Contagem

Este campo é utilizado para informar o período inicial para a contagem do vencimento do imposto a ser calculado. Campo obrigatório. Tipos de contagem:

* 1 - Normal;
* 2 - Fora Semana;
* 3 - Fora Decêndio;
* 4 - Fora Quinzena;
* 5 - Fora Mês;
* 6 - Último dia Semana Seguinte;
* 7 - Último dia Decêndio Seguinte;
* 8 - Último dia Quinzena Seguinte;
* 9 - Último dia Mês Seguinte.

Vcto. não útil

A - Dias Corridos - Antecipa, S - Dias Corridos - Mantém, N - Dias Corridos - Posterga, U - Só Dias Úteis.

Para mais informações sobre a geração do detalhamento no ICMS, consulte a documentação da apuração.

## Páginas relacionadas

* [documentação da apuração](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/processo_geracao_calculo_icms.htm#detalhamento)
