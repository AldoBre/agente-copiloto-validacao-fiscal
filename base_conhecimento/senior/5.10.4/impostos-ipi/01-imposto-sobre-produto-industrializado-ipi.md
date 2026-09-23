# Imposto sobre Produto Industrializado (IPI)

> **Fonte:** Imposto sobre Produto Industrializado (IPI) — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/impostos_ipi.htm  
> **Trilha:** Segmentos > Compliance > Configurações para cálculos fiscais > Impostos  
> **Telas citadas:** E440IPC, E440ISC, E440NFC, F001TCP, F001TVE, F022CLF, F070EMP, F075PRO, F081GTP, F081TPA, F095CAD, F095HFO, F403FPR, F660GDG  
> **Identificadores de regras:** COM-000ALIPI01, COM-000ALSTR02, CPR-000ECIPI01, CPR-440GERCS01

---
Segmentos > Compliance > Configurações para cálculos fiscais  > Impostos  > IPI

|  |  |
| --- | --- |
|  | Veja também: |

* Cálculo do IPI
* Enquadramento e Situações Tributárias de IPI

## Definir se o fornecedor/cliente tributa IPI

* Informe no campo Tributa IPI a opção "S - Sim", na tela Cadastro de Fornecedores (F095CAD);
* Defina que a transação tributa IPI. Para isso, informe no campo Isenta IPI a opção "N - Não", na tela Transações de Vendas (F001TVE)
* Informe no campo É Industria a opção está como "S - Sim", na tela Definições/Histórico do Fornecedor (F095HFO)
* Informe no campo Possui Serviços c/ ICMS/IPI a opção "S - Sim", na tela Cadastro de Empresa (F070EMP)

## Sugestão da alíquota

* Para cotações, ordens de compra e notas fiscais de entrada, a alíquota é informada no campo % IPI para Entradas, da tela Classificações Fiscais (F022CLF)
* A alíquota para saída na classificação fiscal serve apenas para sugestão no cadastro do produto
* Para pedidos e notas de venda, a alíquota é definida no campo % IPI, da guia Dados Gerais da tela Cadastro de Produtos (F075PRO). Se houver ligação produto x cliente, o sistema busca desse cadastro a alíquota do IPI
* O identificador de regras COM-000ALIPI01 pode ser utilizado para manipular a base, valor e percentual de IPI

## Recuperação do IPI

Durante a apuração do IPI em Tributos, o sistema busca do campo IPI Creditado Efetivamente – Base/Valor/Percentual da nota fiscal os valores a recuperar de IPI.

![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/images/imposto_ipi006_thumb_0_48.png)

Por padrão, os campos de ICMS/IPI Creditado Efetivamente não ficam habilitados, exceto nas notas fiscais de devolução para o campo de IPI Creditado Efetivamente e para qualquer tipo de nota quando o fornecedor for optante do Simples.

Nas notas de devolução, há IPI somente no campo de IPI Cred. Efetivamente, pois nas notas de devolução não há IPI destacado, mas somente a possibilidade de recuperação – verificar solução 10254.

Para que esse campo no item da nota fiscal seja preenchido, é necessário que os cadastros envolvidos no item da nota estejam parametrizado para recuperar IPI. O valor deste campo pode ser manipulado via identificador CPR-000ECIPI01.

### Configurações para recuperar o IPI

* Informe a opção "S - Sim" no campo Recupera IPI da guia IPI, tela Transações de Compras (F001TCP)
* Informe a opção "S - Sim" no campo Recupera IPI da tela Cadastro de Fornecedores (F095CAD)
* Informe a opção "S - Sim" no campo É Industria na tela Definições/Histórico do Fornecedor (F095HFO)
* Na tela Cadastro de Produtos (F075PRO), se o campo Usa Produto x Fornecedor estiver parametrizado como "N - Não", o campo Recupera IPI deve ser igual a "S - Sim"
* Para calcular IPI em serviços, o campo Possui Serviços c/ ICMS/IPI deve estar parametrizado como "S - Sim" na tela Cadastro de Empresa (F070EMP)

## Configurar o IPI Creditado efetivamente por quantidade:

* Cadastre uma tabela de preço de venda na tela Tabela de Preço de Venda (F081GTP), com o tipo de aplicação **4 - Cálculo por Quantidade (Compras)** ou **5 - Cálculo por Quantidade (Vendas)**
* Na tela Cadastro de Produtos (F075PRO), se o campo Usa Produto x Fornecedor estiver parametrizado como:
  + "N - Não": informe a tabela de preço criada no campo Código Tabela Preço IPI
  + "S - Sim": informe a tabela de preço criada na tela Ligações Fornecedor X Produtos Individual (F403FPR)

## IPI Creditado Efetivamente x F660GDG

Quando não há IPI Creditado Efetivamente no item da nota fiscal de entrada e todos os parâmetros estão configurados para recuperar IPI, os campos Atualizar NF Entrada e Inicializar valores de IPI E ICMS Creditados Efetivamente em Suprimentos, da tela Geração de detalhes (F660GDG), devem estar marcados.

Para que o item da nota seja considerado nesse processo, é necessário que a nota fiscal não esteja integrada com Tributos – E440NFC.IntImp = N.

## Campos das tabelas onde é gravado o IPI

* **Dados Gerais:** BecIpi(Base IPI Cred. Efetivamente), VecIpi(Valor IPI Cred. Efetivamente) - E440NFC
* **Itens - Produtos:** BecIpi(Base IPI Cred. Efetivamente), VecIpi(Valor IPI Cred. Efetivamente), PecIpi(Percentual IPI Cred. Efetivamente) - E440IPC
* **Itens - Serviços:** BecIpi(Base IPI Cred. Efetivamente), VecIpi(Valor IPI Cred. Efetivamente), PecIpi(Percentual IPI Cred. Efetivamente) - E440ISC

## Base de IPI x valor do desconto

Através do parâmetro Considerar descontos na base do IPI, das telas Transações de Venda (F001TVE) e Transações de compras (F001TCP), é definido se o valor de desconto na nota fiscal será ou não descontado da base de cálculo de IPI.

## IPI presumido

Para calcular valor de IPI presumido, o IPI deve estar configurado para ser recuperado. A mensagem "Produtos com sugestão de IPI Destacado/Presumido" é apresentada quando o sistema calcula o valor de IPI presumido. Não há parâmetro/identificador para oculta-la.

O sistema utiliza 50% do valor da mercadoria como base de cálculo para o IPI presumido, porém a legislação permite um percentual maior que 50%, como no art. 237 do RIPI. Nesse caso, utilize o campo Percentual IPI Presumido da tela Ligações Fornecedor X Produtos Individual (F403FPR) para selecionar a quantidade de valor da mercadoria que será utilizada como base no cálculo do valor de IPI presumido.

O valor padrão é de 50%/100%. Será calculado 50% somente se o fornecedor estiver configurado como Indústria = "N - Não". Será considerado 100% caso o fornecedor esteja configurado como Indústria = "S - Sim" e tenha as seguintes parametrizações:

1. "S - Sim" no campo Calcula IPI Presumido da tela Ligações Fornecedor X Produtos Individual (F403FPR)
2. "S - Sim" no campo Recupera IPI da tela Cadastro de Produtos (F075PRO)
3. "S - Sim" no campo Recupera IPI da tela Transações de Compras (F001TCP)
4. "S - Sim" no campo Recupera IPI da tela Cadastro de Fornecedores (F095CAD)
5. Valor no campo Percentual de IPI na tela Classificações Fiscais (F022CLF). O valor cadastrado será utilizado para calcular o valor do IPI presumido

**Exemplo:**

* Valor total da mercadoria da nota fiscal de entrada: 1000
* Percentual do IPI presumido configurado na tela F403FPR: 100%
* Percentual do IPI presumido configurado na tela F022CLF: 3%

**Cálculo do IPI presumido:**

* 1000 x 0,5 = 500 (valor base utilizado no cálculo do IPI presumido)
* 500 x 0,03 = 15 (valor final de IPI presumido)

## Sugestão da situação tributária do IPI

A situação tributária é sugerida nos itens das notas fiscais primeiramente a partir da transação e, se não houve na transação, busca a situação tributária constante no cadastro do produto. Esta ordem é válida tanto para notas de entrada quanto para notas de saída.

Pode-se utilizar o identificador de regras COM-000ALSTR02 para alterar o código da situação tributária do ICMS no item da nota fiscal.

Para fazer com que na geração de notas fiscais de entrada dos tipos 3, 6, 7 e 10, que por sua vez geram notas fiscais de saída, o sistema faça a sugestão das CSTs nas notas de saída a partir da codificação do módulo de Mercado deve-se utilizar o identificador de regras CPR-440GERCS01. Com este identificador ativo, o sistema fará a sugestão dos CSTs nas notas de saída conforme condições do módulo de Mercado e também fará com que o identificador COM-000ALSTR02 seja executado para os itens das notas de saída.

## Cálculo do IPI por quantidade

Cadastre uma tabela de preço de venda na tela Tabela de Preço Vendas Agrupada (F081TPA), com o tipo de aplicação **4 - Cálculo por Quantidade (Compras)** ou **5 - Cálculo por Quantidade (Vendas)**. Na guia Itens Produto deve ser informado o Valor do imposto por cada unidade constante no documento fiscal. No cadastro do produto, informe no Código Tabela Preço IPI a tabela de preço cadastrado.

Campos da tela de cálculo do item da nota de entrada:

![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/images/imposto_ipi012_thumb_0_48.png)

## Páginas relacionadas

* [Cálculo do IPI](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/processo_geracao_calculo_ipi.htm)
* [Enquadramento e Situações Tributárias de IPI](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/enquadramento-de-ipi.htm)
* [Cadastro de Fornecedores (F095CAD)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f095cad.htm)
* [Transações de Vendas (F001TVE)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f001tve.htm)
* [Definições/Histórico do Fornecedor (F095HFO)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f095hfo.htm)
* [Cadastro de Empresa (F070EMP)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070emp.htm)
* [Classificações Fiscais (F022CLF)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f022clf.htm)
* [Cadastro de Produtos (F075PRO)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075pro.htm)
* [COM-000ALIPI01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/com_000alipi01.htm)
* [CPR-000ECIPI01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/cpr_000ecipi01.htm)
* [Transações de Compras (F001TCP)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f001tcp.htm)
* [Tabela de Preço de Venda (F081GTP)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f081gtp.htm)
* [Ligações Fornecedor X Produtos Individual (F403FPR)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f403fpr.htm)
* [Geração de detalhes (F660GDG)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f660gdg.htm)
* [COM-000ALSTR02](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/com_000alstr02.htm)
* [CPR-440GERCS01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/cpr_440gercs01.htm)
* [Tabela de Preço Vendas Agrupada (F081TPA)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f081tpa.htm)
