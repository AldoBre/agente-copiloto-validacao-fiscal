# Apuração dos impostos dos tipos 41 e 42

> **Fonte:** Apuração dos impostos dos tipos 41 e 42 — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/sped/contribuicoes-pis-cofins/lucro-real/apuracao-imposto-41-42.htm  
> **Trilha:** Segmentos > Compliance > Escriturações Fiscais Digitais (SPED) > SPED Contribuições > Pessoa Jurídica Tributada pelo Lucro Real  
> **Telas citadas:** E070IMP, E661UCR, F661CAD, F661PAI, F661UCR  
> **Identificadores de regras:** —

---
Segmentos > Compliance > Escriturações Fiscais Digitais (SPED) > SPED Contribuições > Pessoa Jurídica Tributada pelo Lucro Real > Apuração dos impostos do tipo 41 e 42

Após realizar a Apuração do Faturamento por Regime Tributário (H), faça o cálculo dos impostos do tipo 41- PIS não cumulativo - SPED e 42 - Cofins não cumulativo - SPED somente na **Filial Matriz**.

**Veja também:**

* Conceito - Escrituração das Contribuições Sociais (Pessoa Jurídica Tributada pelo Lucro Real)
* Parametrizações para geração da EFD Contribuições (Lucro Real)

Esse cálculo é feito na tela através da tela Apuração dos impostos (F661PAI).

**Apuração 41 - PIS Não Cumulativo e 42 - COFINS Não Cumulativo - Crédito de apropriação direta:**

Na apuração dos impostos 41 e 42, são considerados os créditos apropriados de forma direta informados na tela Crédito Apropriação Direta (F661CAD), que podem ser consultados através do botão Apropriação Direta.

A forma de calculo do imposto é realizada de acordo com a parametrização do campo Compensar Crédito da tela F661CAD:

* **Não**: o sistema lança automaticamente como Saldo Crédito Futuro os créditos parametrizados desta forma;
* **Sim e com Valor Crédito igual a zero**: o sistema utiliza o saldo do crédito identificado na apuração pelo método de apropriação indireta baseada na receita bruta para abater o imposto a pagar, respeitando o sequenciamento definido na tela F661UCR;
* **Sim e com Valor Crédito maior que zero**: o sistema compensa o crédito de apropriação direta conforme créditos identificado na apuração do imposto, ou seja, o sistema distribui conforme sequenciamento definido na tela F661UCR o saldo informado para os créditos do período da apuração e de períodos anteriores (ou vice-versa e sempre que necessário para abater o total do imposto a pagar). Caso o crédito identificado a partir do cálculo do imposto seja maior que o crédito de apropriação direta este saldo será lançado como Saldo Crédito Futuro.

Para que o sistema considere os créditos apropriados de forma direta é necessário configurar um sequenciamento de utilização do créditos na tela Método Utilização/Retenções/Creditos (F661UCR), onde deve-se priorizar quais tipos de créditos e períodos devem ser utilizados primeiramente.

## Ligação dos impostos

É possível fazer a ligação dos impostos cumulativos 43 e 44, para as empresas que apuram impostos no regime cumulativo e no regime não cumulativo simultaneamente:

![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/images/sped-contribuicoes/lucro-real/ligacao-imposto-43_thumb_0_48.png)

![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/images/sped-contribuicoes/lucro-real/f661i12-apuracao_thumb_0_48.png)

## Proporção do crédito cumulativo e não cumulativo

**Exemplo**:

* NF Saída 10.000 Cumulativo
* NF Saída 10.000 Não-Cumulativo
* NF Entrada 20.000 Não-Cumulativo

O Gestão Empresarial | ERP faz a proporção de crédito conforme a venda não cumulativa. Dessa forma, o valor para crédito cumulativo é 10.000:

![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/images/sped-contribuicoes/lucro-real/f661pai-proporcao_thumb_0_48.png)

## Transferência do saldo de retenção do regime cumulativo para o não cumulativo

No primeiro mês em que for apurado o PIS/COFINS após habilitar o campo **Retenção Unificada** da tela F661UCR (**E661UCR.RetUni = S**), caso haja saldo de retenção no regime cumulativo, será apresentada a mensagem **As retenções serão transferidas do regime Cumulativo para o Não Cumulativo. Deseja prosseguir?** Após confirmar, a transferência ocorrerá da seguinte forma:

1. as retenções do regime cumulativo com saldo serão transferidas para o regime não cumulativo. Havendo um registro no regime não cumulativo para o mesmo período de apuração e natureza de rendimento, os valores dos dois regimes serão somados;
2. o valor das retenções do regime cumulativo será zerado;
3. quando houver a parametrização para gerar a origem da retenção do PIS/COFINS (**E070IMP.OriRpc = S**), as origens do regime cumulativo serão transportadas para o regime não cumulativo.

## Páginas relacionadas

* [Escriturações Fiscais Digitais (SPED)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/sped/compliance.htm)
* [SPED Contribuições](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f669spc.htm)
* [Pessoa Jurídica Tributada pelo Lucro Real](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/sped/contribuicoes-pis-cofins/lucro-real/conceitual-de-negocio.htm)
* [Apuração do Faturamento por Regime Tributário (H)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/sped/contribuicoes-pis-cofins/lucro-real/faturamento-regime-tributario.htm)
* [Parametrizações para geração da EFD Contribuições (Lucro Real)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/sped/contribuicoes-pis-cofins/lucro-real/parametrizacoes.htm)
* [F661PAI](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f661pai.htm)
* [Crédito Apropriação Direta (F661CAD)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f661cad.htm)
* [Método Utilização/Retenções/Creditos (F661UCR)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f661ucr.htm)
