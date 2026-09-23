# Base de ICMS x valor do desconto

> **Fonte:** Rotinas de ICMS — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/impostos-icms.htm#base-desconto  
> **Trilha:** Segmentos > Compliance > Configurações para cálculos fiscais > Impostos  
> **Telas citadas:** —  
> **Identificadores de regras:** CPR-000ALICM01

---
O valor de desconto na nota fiscal é sempre descontado da base de cálculo de ICMS. Não há parâmetro ou identificador para alterar este conceito.

Alternativas:

* **Opção 1**: Atribuir um arredondamento negativo na nota no lugar do desconto. Utilizando o arrendodamento no lugar do desconto, é possível parametrizar na transação para que o valor do arredondamento não reduzar o valor da base de cálculo do ICMS.  

  Há o campo Arredondamento Base ICMS constante na tela de cadastro de transações do compras, onde é feita esta parametrização;
* **Opção 2**: Utilizar o identificador de regras CPR-000ALICM01 para manipular a base de ICMS, adicionando à base o valor dos descontos.
