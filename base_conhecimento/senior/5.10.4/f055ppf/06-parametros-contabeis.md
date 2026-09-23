# Parâmetros Contábeis

> **Fonte:** F055PPF - Configuração de Impostos para a Filial — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f055ppf.htm  
> **Trilha:** Ajuda por telas > Cadastros > Controladoria > Tributos  
> **Telas citadas:** —  
> **Identificadores de regras:** —

---
Esta guia tem por finalidade informar as contas contábeis reduzidas que influenciaram no cálculo do imposto do
tipo 98 - Livre, onde é possível apurar impostos através de qualquer movimento ou saldo contábil.

Conta Reduzida

Código da conta contábil reduzida. É possível informar contas contábeis sintéticas e analíticas.

Data Base

Data inicial para considerar na apuração desta conta contábil.

Valor Débitos

Parametrizar os valores dos débitos deve ser adicionados(+), subtraídos(-) ou desconsiderados(N) da base de
cálculo.

Valor Créditos

parametrizar os valores dos créditos deve ser adicionados(+), subtraídos(-) ou desconsiderados(N) da base de
cálculo.

Saldo Contábil

Especifica se o saldo do último dia do período da apuração da conta contábil associada, deve ser somado(+),
subtraído(-) ou desconsiderado(N) da base de cálculo. Exemplo:  
Temos uma conta contábil nº 179, cuja natureza é devedora e temos efetuado um lançamento à débito no valor de
R$ 800,00 e outra conta nº 747 que é de natureza credora e efetuado um lançamento de crédito no valor de
R$ 1.200,00.   

Na base do imposto informamos que a conta contábil nº 179 deve somar os valores dos
Créditos e a conta contábil nº 747 deverá subtrair os valores dos Débitos. Na tabela de tributação temos a alíquota de 3,2% para valores inferiores à 10.000,00.

Apurando o imposto no período temos:

* Adições na Base: R$ 1.200,00
* Subtrações na Base: R$ 800,00
* Base Líquida: R$ 400,00
* Alíquota: 3,2%
* Imposto a Pagar: R$ 12,80

Recurso da guia: essa guia possui o recurso de possibilitar ao usuário redimensionar o tamanho,
com isso, será possível movimentar a guia para melhor visualização das informações cadastradas.

Relatório: as informações que compõem a base do imposto para cada imposto
da empresa podem serem impressas pelo modelo de relatório DACT031.GER (Tributos - Base Imposto).
