# Controle único de retenção para os regimes de tributação cumulativo e não cumulativo

> **Fonte:** PIS/COFINS — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/impostos_pis_cofins.htm  
> **Trilha:** Segmentos > Compliance > Configurações para cálculos fiscais > Impostos  
> **Telas citadas:** E070IMP, F070FEF, F661PAI, F661REP, F661UCR  
> **Identificadores de regras:** —

---
Empresas que apuram PIS/COFINS cumulativo e não cumulativo podem compensar as retenções nas duas apurações, conforme exemplo:

**01/2018:**

* **PIS cumulativo:**
  + Débito = 100,00
  + Retenção = 150,00
  + Imposto a Recolher = 0,00
  + Saldo Controle de Retenção = 50,00
* **PIS não cumulativo:**
  + Débito = 200,00
  + Retenção = 50,00 (a sobra do valor retido da apuração do regime cumulativo pode ser utilizada na compensação)
  + Imposto a recolher = 150,00

Para isso, utilize o campo **Retenção Unificada** na tela Método de Utilização Retenções/Créditos (F661UCR). Ele Indica se as retenções de PIS/COFINS serão controladas de maneira unificada entre os regimes cumulativos e não cumulativos. Será habilitado apenas quando se tratar de impostos não cumulativos 41 (PIS) ou 42 (COFINS) e eles estiverem ligados ao seus respectivos impostos cumulativos (41 ao 43 ou 42 ao 44). Se essa premissa não for atendida, o parâmetro ficará como **N-Não.**

Com isso, na tela Controle de Retenções PIS/COFINS (F661REP), para os impostos cumulativos 43 e 44 (PIS/COFINS) será verificado se existe a configuração de retenção unificada para os seus respectivos impostos não cumulativos. Caso sim, será exibida uma mensagem impedindo a movimentação das retenções dos impostos cumulativos.

Ao calcular o PIS/COFINS cumulativo e não cumulativo simultaneamente na tela Apuração dos Impostos (F661PAI), com o campo **Retenção Unificada** da tela F661UCR igual a **S-Sim**, o imposto cumulativo (TipImp = 43 ou 44) não aparecerá na tela de apuração.

No primeiro mês em que for apurado o PIS/COFINS após habilitar o campo **Retenção Unificada**, caso haja saldo de retenção no regime cumulativo será apresentada a mensagem **As retenções serão transferidas do regime Cumulativo para o Não Cumulativo. Deseja prosseguir?** Após confirmar, a transferência ocorrerá da seguinte forma:

1. as retenções do regime cumulativo com saldo serão transferidas para o regime não cumulativo. Havendo um registro no regime não cumulativo para o mesmo período de apuração e natureza de rendimento, os valores dos dois regimes serão somados;
2. o valor das retenções do regime cumulativo será zerado;
3. quando houver a parametrização para gerar a origem da retenção do PIS/COFINS (**E070IMP.OriRpc = S**), as origens do regime cumulativo serão transportadas para o regime não cumulativo.

Na tela Resumo de Apuração do Imposto (F661I12), todas as retenções serão carregadas/utilizadas, independentemente do regime de origem, a partir do regime não cumulativo, que passará a agir como uma conta corrente única de saldo de retenções. **Pré-requisitos:**

1. estar logado na filial **Matriz**;
2. preencher o campo **OriRpc = S** na tela F070FEF para que as origens das retenções sejam gravadas;
3. configurar a tela F661UCR para os impostos não cumulativos.

## Páginas relacionadas

* [Método de Utilização Retenções/Créditos (F661UCR)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f661ucr.htm)
* [Controle de Retenções PIS/COFINS (F661REP)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f661rep.htm)
* [Apuração dos Impostos (F661PAI)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f661pai.htm)
* [Resumo de Apuração do Imposto (F661I12)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f661i12.htm)
* [F070FEF](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070fef.htm)
