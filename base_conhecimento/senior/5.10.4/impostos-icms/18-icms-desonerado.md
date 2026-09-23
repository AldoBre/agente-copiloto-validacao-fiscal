# ICMS Desonerado

> **Fonte:** Rotinas de ICMS — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/impostos-icms.htm#icms-desonerado  
> **Trilha:** Segmentos > Compliance > Configurações para cálculos fiscais > Impostos  
> **Telas citadas:** F001TVE, F019TIR, F051DIS, F070FVE, F075GFP, F075PCA, F075PFI, F075PRO, F085CAD, F085HCL, F095CAD  
> **Identificadores de regras:** CPR-000ALICD01, VEN-000ALICD01, VEN-140DISFS01

---
Para que o cálculo do ICMS desonerado ocorra, deve haver um motivo de desoneração no item da nota fiscal de entrada ou saída. O motivo de desoneração pode ser sugerido para o item da nota fiscal através do campo Motivo desoneração ICMS das rotinas:

1. Definições do Cliente (F085CAD e F085HCL)
2. Ligação Produto x Filial (F075PFI)
3. Dados do Produto (F075PRO e F075GFP)
4. Ligação Cliente x Produto (F075PCA)

Fique atento às seguintes situações para que o cálculo seja feito:

1. Situação Tributária igual X40 ou x41 ou x50 e Motivo Desoneração diferente de 2 e 12
2. Situação Tributária igual a X30 e Motivo Desoneração igual a 6, 7 ou 9
3. Situação Tributária igual a X20, X70 ou X90 e Motivo Desoneração igual a 3, 9 ou 12

Observação

O Motivo desoneração (motDesICMS) só será enviada no XML caso houver valor desonerado calculado (vICMSDeson).

Caso o motivo da desoneração seja 7 - SUFRAMA, uma das seguintes CFOPs devem constar na nota fiscal: 1203, 1204, 1208, 1209,2203, 2204, 2208, 2209, 5109, 5110, 5120, 5151,5152, 5651, 5652, 5654,5655, 5658, 5659, 5910,6109, 6110, 6120, 6122, 6123, 6151, 6152, 6651,6652, 6654, 6655, 6658, 6659, 6910. Se constar alguma dessas CFOPs e o motivo for diferente de 7 - SUFRAMA, a desoneração será calculada.

Para que a nota fiscal fique com o valor líquido, informe "S - Sim" no parâmetro **Considera desoneração ICMS** na tela (F001TVE), aba ICMS 2 (1). Caso contrário, a nota fiscal ficará com o valor bruto. Este campo é responsável pela geração da tag <indDeduzDeson> indicando se o ICMS Desonerado foi deduzido ou não do valor total líquido do produto. Esta tag também é carregada com "1 - Deduz valor" caso o motivo da desoneração seja "7 - SUFRAMA".

Na nota fiscal de entrada, é necessário informar o motivo de desoneração na grade de item de produto e serviço para realizar o cálculo do ICMS desonerado. Este motivo deve estar de acordo com a situação tributária, seguindo a mesma regra descrita acima.

O valor de ICMS desonerado pode ser alterado na grade de itens de produto e serviço e, quando alterado, o valor informado é mantido. Ele sempre leva em consideração o % ICMS das parametrizações do sistema, mesmo que o % ICMS do documento seja diferente.

Ao gerar uma nota de devolução de venda ou compra, o motivo de desoneração e o valor de ICMS desonerado são importados do documento de origem (nota fiscal de venda ou nota fiscal de compra que foi devolvida).

É possível alterar o valor do ICMS desonerado e o motivo de desoneração do item por meio de identificadores de regras. Para vendas, a alteração dos valores do item de produto pode ser feita via identificador de regras VEN-000ALICD01. A chamada desse identificador vale também para itens de serviço. No caso de valores do item de produto de compras, há o identificador de regras CPR-000ALICD01, que tem a mesma função do identificador de regras de vendas.

**Observação**

* Para o estado do **RJ**, o valor de ICMS desonerado deve ser a soma da alíquota de ICMS + FCP (se houver). Nesse caso, a alíquota de **% FCP Normal** será adicionada à **% ICMS** no cálculo do valor de ICMS desonerado quando o campo **Cálculo de Desoneração de ICMS** for **1 - Resolução 13/2019 RJ** nas telas F070FVE (notas de saída) ou F095CAD (notas de entrada)
* Para o estado de **SC**, de acordo com o Guia Prático de Escrituração de incentivos e benefícios fiscais aprovado pelo Decreto Estadual nº 2.870/2001, o valor de ICMS desonerado deve ser calculado conforme o CST vinculado ao produto. Seguem os cálculos dos respectivos CSTs:
  + Para os CSTs 30 e 40 de ICMS isento ou não tributado:  
    Preço do produto \* Alíquota

    ## Exemplo

    Valor Bruto: R$ 880,00

    Valor Base de ICMS: R$ 0,00

    % ICMS no documento: 0%

    Valor ICMS: R$ 0,00

    % ICMS que seria nesta operação: 17%

    Valor ICMS Desonerado: 880,00 \* 0,17

    Valor ICMS Desonerado: R$ 149,60
  + Para os CSTs 20 e 70 de redução de ICMS na base de cálculo:  
    (Percentual de redução da BC / (1 - Percentual de redução da BC) \* valor do ICMS

    ## Exemplo

    Valor Bruto: R$ 1.000,00

    % Redução Base de Cálculo: 51,11%

    Valor Base de ICMS: R$ 488,90

    % ICMS no documento: 17%

    Valor ICMS: R$ 83,11

    Valor ICMS Desonerado: (0,5111 / (1 – 0,5111)) \* 83,11

    Valor ICMS Desonerado: (0,5111 / 0,4889) \* 83,11

    Valor ICMS Desonerado: 1,0454 \* 83,11

    Valor ICMS Desonerado: R$ 86,88
  + CST 50 de suspensão de ICMS:  
    Valor da base de cálculo do ICMS \* Alíquota

    ## Exemplo

    Valor Bruto: R$ 1.000,00

    Valor Base de ICMS: R$ 0,00

    % ICMS no documento: 0%

    Valor ICMS: R$ 0,00

    % ICMS que seria nesta operação: 17%

    Valor ICMS Desonerado: 1.000,00 \* 0,17

    Valor ICMS Desonerado: R$ 170,00

  Esse cálculo é habilitado quando o campo Cálculo de Desoneração de ICMS for "2 - Resolução 79/2022 SC" nas telas F070FVE (notas de saída) ou F095CAD (notas de entrada).
* Nas operações com CSTs 20, 30, 40, 50 e 70, o guia prático de escrituração de incentivos e benefícios fiscais ressalta que o valor integral do ICMS faz parte do valor total bruto do produto que, por sua vez, deve compor o seu valor unitário do produto. Dessa forma, clientes que usam tabela de preço devem alterar os preços dos produtos para incluir o ICMS. Fontes:
  + Isenções (CSTs 30 e 40): página 8 do Guia prático de escrituração Incentivos e Benefício Fiscais v3
  + Redução de base de cálculo (CSTs 20 e 70): página 9 do Guia prático de escrituração Incentivos e Benefício Fiscais v3
  + Suspensão (CSTs 50): página 10 do Guia prático de escrituração Incentivos e Benefício Fiscais v3

Saiba como configurar o dispositivo fiscal para atender a Ato Diat nº 79/2022 do estado de SC.

## Cálculo do valor do ICMS Dispensado

Para produtos e serviços que utilizam redução de base para cálculo de ICMS, pode-se usar o valor do ICMS dispensado. Através do parâmetro Considera desoneração ICMS na transação de venda (F001TVE), é possível indicar se o valor do ICMS desonerado calculado no item da nota fiscal de venda será descontado ou não do valor líquido da nota fiscal.

Para um item, caso haja configuração de código de redução de imposto vinculado à transação, esse código será buscado das definições de redução de imposto e poderá impactar no cálculo do valor líquido do item.

Este valor de redução de imposto será considerado como fator de alteração do valor líquido, caso o identificador de regras VEN-140DISFS01 esteja cadastrado e ligado a uma regra onde a variável VENNIcmDis seja atribuída ao campo VlrAjs, da tabela de itens de produto ou serviço; e onde haja código de dispositivo fiscal sendo atribuído ao campo CodDfs, da tabela de itens de produto ou serviço.

## Passos para o cálculo da redução da base

* Cadastrar um dispositivo fiscal através da tela Cadastro de Dispositivos Fiscais (F051DIS)
* Cadastrar um código de redução de imposto na tela Reduções e Acréscimos de bases de Cálculos de Impostos - Por Estado (F019TIR), e configurar um percentual de redução (30% exemplo) para os estados listados
* Vincular este código de redução de imposto a uma transação através do campo Código Redução Imposto, da tela Transações de Vendas (F001TVE). Ainda nessa tela, o parâmetro Considerar desoneração ICMS deverá estar como S - Sim
* Cadastrar o identificador de regras VEN-140DISFS01 e ligá-lo a uma regra, conforme abaixo:

```
definir numero VENNIcmDis;  
e140ipv.vlrajs = VENNIcmDis;  
e140ipv.coddfs = 2; /* código do dispositivo.
```

A regra informa a rotina que o valor de redução da base de cálculo será enviado ao campo **Valor do ajuste**. O valor de ajuste retornado pela regra não será considerado no cálculo da nota, sendo apenas informativo. O que influência no cálculo da nota é o valor ICMS Desonerado/Dispensado quando o parâmetro Considera desoneração ICMS estiver como S-Sim.

### Exemplo

Item de produto com uma transação que tenha um código de redução vinculado com quantidade 1 e valor unitário de R$ 717,77;  
Produto: R$ 717,77;  
Redução da base de cálculo = 30% (configurado na tela F019TIR);  
Valor da base de cálculo com redução = R$ 215,33 (R$ 717,77 \* 30%);  
ICMS sobre base de cálculo reduzida = R$ 36,61 (R$ 215,33 \* 17%);  
Valor líquido do item da nota fiscal deve ficar R$ 681,16 (R$ 717,77 - R$ 36,61).

## Páginas relacionadas

* [F085CAD](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f085cad.htm)
* [F085HCL](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f085hcl.htm)
* [F075PFI](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075pfi.htm)
* [F075PRO](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075pro.htm)
* [F075GFP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075gfp.htm)
* [F075PCA](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075pca.htm)
* [F001TVE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f001tve.htm)
* [VEN-000ALICD01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_000alicd01.htm)
* [CPR-000ALICD01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/cpr_000alicd01.htm)
* [F070FVE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070fve.htm)
* [F095CAD](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f095cad.htm)
* [Guia prático de escrituração Incentivos e Benefício Fiscais v3](https://www.sef.sc.gov.br/arquivos_portal/assuntos/108/Guia_Pratico_de_Escrituracao_de_Incentivos_e_Beneficios_Fiscais___3_edicao.pdf)
* [configurar o dispositivo fiscal](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/geracao-beneficio-fiscal.htm)
