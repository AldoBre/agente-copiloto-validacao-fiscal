# Composição Base Cálculo

> **Fonte:** F055PPF - Configuração de Impostos para a Filial — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f055ppf.htm  
> **Trilha:** Ajuda por telas > Cadastros > Controladoria > Tributos  
> **Telas citadas:** E001TNS, F660IFI  
> **Identificadores de regras:** —

---
Esta guia tem por finalidade informar as transações do Financeiro e Patrimônio que devem ser tratados pelos
impostos PIS
Não Cumulativo (tipo 20), PIS Não Cumulativo SPED (tipo 41), COFINS Não Cumulativo (tipo 21),
COFINS Não Cumulativo SPED (tipo 42), PIS Cumulativo SPED (tipo 43),
COFINS Cumulativo SPED (tipo 44), PIS Regime de Caixa SPED (tipo 47) e
COFINS Regime de Caixa SPED (tipo 48).

Nela deve-se informar a Data Base, Transações Financeiras
e Patrimoniais( Baixa do Contas a Pagar, Baixa Contas a Receber, Baixa da Tesouraria Débito e Crédito e a
Depreciação do Bem Patrimonial), e informar se deseja somar(+), subtrair(-) ou nenhum(N) os valores.

Ela é visualizada somente quando o curso estiver
posicionado sobre os impostos PIS
Não Cumulativo (tipo 20), PIS Não Cumulativo SPED (tipo 41), COFINS Não Cumulativo (tipo 21),
COFINS Não Cumulativo SPED (tipo 42), PIS Cumulativo SPED (tipo 43),
COFINS Cumulativo SPED (tipo 44), PIS Regime de Caixa SPED (tipo 47) e
COFINS Regime de Caixa SPED (tipo 48).

É possível cadastrar transações de movimentação cambial para compor a base de cálculo do PIS/COFINS. As transações de movimentação cambial são identificadas a partir do seu módulo (E001TNS.LisMod), que será igual a **CRV - Contas a Receber** e **CPV - Contas a Pagar**.

Data Base

Define a validade inicial desta base.

Transação

Indica uma transação do patrimônio que o sistema deve tratar, aplicando o que será informado nos campos abaixo.

Mov. Adiantamento CR

Indicativo de que a movimentação a ser integrada para outros documentos deverá ser tratada como adiantamento.

Permite integrar a entrada do título de adiantamento para a apuração do PIS/COFINS no regime de caixa. Neste cenário, títulos vinculados a outros documentos que estiverem assinalados como adiantamento serão integrados com baixa na data de entrada do adiantamento no Contas a Receber, desconsiderando qualquer acerto posterior realizado entre o adiantamento e o título da nota fiscal.

Este campo fica disponível apenas para transações do módulo Contas a Receber.

Observação

Todos os campos referentes aos valores devem ser preenchidos com a indicação do que a rotina deve fazer com eles: **Adicionar**, **Subtrair** ou **Nenhum**.

A coluna **Sep. ODC** - Indicativo se devem ser gerados dois outros documentos, sendo um para Multa e outro para Juros funciona conforme abaixo:

* Apenas para os impostos Pis/Cofins apurados pelo regime de competência (tipos 41, 42, 43 e 44)
* Se informado "S-Sim" o sistema irá preencher automaticamente com "+ - Somar" as colunas Multa e Juros (será lançado a mensagem "Para que seja feita a separação dos valores de juros/multas ao integrar os outros documentos via tela Integração de Outros Documentos (F660IFI) será necessário alterar Juros e Multas para "+"?" antes da alteração)
* Habilitado apenas para transações utilizadas no Contas a Receber

A guia permite redimensionar o seu tamanho. É possível movimentá-la para melhor visualização das informações cadastradas.

## Páginas relacionadas

* [Integração de Outros Documentos (F660IFI)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f660ifi.htm)
