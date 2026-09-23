# Gerais

> **Fonte:** F660GDG - Geração de detalhes das Notas Fiscais — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f660gdg.htm  
> **Trilha:** Ajuda por telas > Controladoria > Gestão de Tributos > Escrituração > Lançamentos  
> **Telas citadas:** E001TNS, E001TVE, E066FPG, E070PEE, E075PRO, E085HCL, E140IPV, E140PAR, E140RCI, E140RSV, E301MCR, E301TCR, E440IPC, E440ISC, E440RCI, E660INC, E660INV, E660IRZ, E660NFC, E660NFV, E660PAR, E660PAV, E660REZ, E660RRZ, E660RSC, E660RSV, F019TIS, F070FEF, F075CEP, F075FCI, F075GFP, F075PRO, F660GDG, F660ODC  
> **Identificadores de regras:** —

---
Atualizar Alíquota do PIS/COFINS a Recuperar do Item da NF

Assinalar esta opção para sugerir uma alíquota de PIS/COFINS a recuperar nos itens das notas fiscais, somente para itens
que possuírem Valor Base de PIS/COFINS a recuperar.

Inicializar Valor de ICSM Operações Próprias, ICMS ST, DIf. Alíq. e Frete das Notas Fiscais de CIAP

Serão preenchidos os valores de ICMS ST - CIAP, diferencial de alíquota
- CIAP e ICMS operações próprias - CIAP dos itens das notas fiscais de
ativo imobilizado com base nas notas fiscais do suprimentos.   
Também serão preenchidos os valores de ICMS, ICMS ST, diferencial de
alíquota e valores do ICMS sobre frete das parcelas do CIAP.

Se a nota estiver lançada somente em Tributos fará o seguinte cálculo:

(ICMS Operações próprias = Vlrcip-Vlrist-Vlridf), a data informada no
período inicial e período final, deve abranger o período data de entrada
das notas fiscais de imobilizado.

Inicializar campo da Natureza do PIS/COFINS (Itens Nota, Itens Redução Z e Outros Documentos)

Preencher os campos de natureza da receita de PIS e COFINS dos itens da
nota fiscal de saída e redução z, baseando-se primeiramente na
transação, caso não encontre, busca-se do produto ou serviço informado.  
Preencher os campos de natureza da receita de PIS e COFINS dos outros
documentos conforme produto ou serviço informado.

Período (Período Inicial e
Final)

Informar o período inicial e final desejado para a geração no botão Detalhes.

Atualizar período final do cálculo da FCI

Este parâmetro ajusta o período final do cálculo da FCI (F075FCI)
que já está gravado, para que seja gerado mensalmente e não diariamente.

Inicializar campo cálculo de média fixa de movimentos de
estoques

Tem a finalidade de inicializar as movimentações
e estoques que não possuem o campo Indicativo se a transação utiliza
media fixa mensal informado e, que estejam no prazo do período
informado no cabeçalho. Caso a transação da movimentação não esteja
ligada à transação de estoque, a movimentação será inicializada com "N",
e se a transação do movimento estiver ligada com a transação de
estoques, a movimentação será inicializada com o valor definido na
transação de estoques.

Inicializar Base de Cálculo do ICMS Substituído por
Responsabilidade Solidária

Tem a finalidade de inicializar o campo **Base de Cálculo do ICMS
ST Resp. Solidário**. A inicialização deste campo por esse
processo somente será possível quando o item da nota fiscal de compra
possuir "ICMS ST Resp. Solidário - VLRRIS" e "Valor de ICMS ST - VLRSIC"
. Caso exista valor para estes campos será localizado o "Percentual de
Retenção" da tabela de configuração da ST (F019TIS).
Será considerado como referência o "Código do ICMS substituído"
informado no item da nota fiscal e a partir dele será localizada a
tabela de configuração da ST.

Inicializar o Valor da Intermediação de Serviços

Possui a finalidade de inicializar o campo **Valor Real dos Produtos Intermediários** (E301MCR.VLRINT e E301TCR.VLRINT), da intermediação de serviços, com o valor 0 (zero) quando ele estiver nulo.

Atualizar os valores de IRRF e CSLL - Outros Documentos - Contas a receber

Possui a finalidade de inicializar os campos Base IRRF, Valor IRRF, Base CSLL Retido, Valor CSLL Retido dos Outros Documentos (F660ODC). A inicialização destes campos por esse processo somente será possível quando a retenção ocorrer através do financeiro (Contas a receber).

Integração de Títulos, Rateios e Baixas IRPJ\CSLL

Tem a finalidade de integrar o rateio e as baixas do IRPJ e CSLL dos títulos que já estão integrados com a Gestão de Tributos.

Inicializar o campo Data de Início das Parcelas do CIAP das Notas de Entrada

Inicia o campo Data Início Parcela CIAP nas notas fiscais de entrada já integradas para Tributos, independente se já houver parcelas geradas ou não para a nota.

**Ajustar os valores do DIFAL em Notas de Entrada de Devolução em Tributos**

Serve para corrigir os valores do DIFAL das notas fiscais de entrada de devolução nas tabelas de tributos invertendo/ajustando os valores de acordo com a nota de saída vinculada.

**Inicializar estrutura de apuração do ICMS**

Serve para inicializar a nova estrutura de apuração do ICMS e também para exportar as informações da apuração de ICMS antiga para a nova estrutura.

**Inicializar estrutura de dispositivos fiscais dos itens da nota fiscal de Compra/Entrada**

Serve para inicializar a nova estrutura de dispositivos fiscais das notas fiscais de entrada, e também para exportar as informações dos dispositivos fiscais já existentes para a nova estrutura.

**Inicializar estrutura de dispositivos fiscais dos itens da nota fiscal de Venda/Saída**

Serve para inicializar a nova estrutura de dispositivos fiscais das notas fiscais de saída, e também para exportar as informações dos dispositivos fiscais já existentes para a nova estrutura.

**Inicializar estrutura de mensagens das notas fiscais Venda/Saída**

Serve para inicializar a nova estrutura de armazenamento de mensagem das notas fiscais de saída, e também para exportar as informações das mensagens já existentes para a nova estrutura.

**Inicializar estrutura de mensagens das notas fiscais Compra/Entrada**

Serve para inicializar a nova estrutura de armazenamento de mensagem das notas fiscais de entrada, e também para exportar as informações das mensagens já existentes para a nova estrutura.

**Inicializar o campo Tipo de Cartão das Notas de Saída e Redução Z**

Serve para inicializar o campo **Tipo Cartão (TipCar)** das tabelas E140PAR, E660PAV e E660PAR. Na tabela E140PAR será inicializado com o valor do campo **Tipo Cartão (TipCar)** do cadastro de formas de pagamento (E066FPG). Nas tabelas E660PAV e E660PAR será inicializado com o conteúdo do campo **Tipo Cartão (TipCar)**da parcela da nota fiscal de saída (E140PAR) / cupom fiscal (E140PAR) da Gestão de Mercado, caso não encontre a parcela da nota fiscal de saída/cupom fiscal na Gestão de Mercado, será inicializado o campo com o valor do campo **Tipo Cartão (TipCar)** do cadastro de formas de pagamento (E066FPG). Este processo só será feito nas parcelas onde o conteúdo do campo **Tipo Cartão** for igual a branco ou nulo.

Inicializar natureza da retenção do IRPJ e CSLL

Permite gerar os valores das retenções com base em um período passado (anterior a geração dos valores a partir da apuração).

Importante

* O sistema irá excluir todas as notas fiscais de compra/entrada e suas vendas/saídas lançadas no controle de entrada de produtos, o processo é necessário para garantir que os saldos disponíveis estão corretos;
* O sistema irá lançar no controle de entrada de produtos todas as notas fiscais de compra/entrada/venda e saída desde que o produto da nota fiscal indique que o mesmo é controlado no controle de entrada de produtos;
* O usuário deverá executar a opção em questão quando no Cadastro de Empresas o campo Registra Entrada e Saída de Produtos estiver sinalizado como "S-Sim".

Inicializar os campos Valor ICMS ST e IPI Não Recuperado nos itens das notas fiscais de entrada

Inicia os campos Vlr. IPI Não Rec(E660INC.VlrIpn) e Vlr. ICMS ST Não Rec(E660NFC.VlrIcn, E660INC.VlrIcn).

Vlr. ICMS ST Não Rec - E660NFC.VlrIcn e E660INC.VlrIcn: quando o item for de produto, o campo VlrIcn recebe valor do campo E440IPC.VlrIcs, quando o campo Recupera ICMS estiver parametrizado como **N - Não** nos cadastros de produto, transação, fornecedor ou ligação fornecedor x produto. E quando o item for de serviço, o campo VlrIcn recebe valor do campo E440ISC.VlrIcs quando o campo Recupera ICMS estiver parametrizado como **N - Não** nos cadastros de produto, transação ou fornecedor.

Vlr. IPI Não Rec - E660INC.VlrIpn: o campo VlrIpn recebe o valor do campo E440IPC.VlrIpi ou E440ISC.VlrIpi, caso a base (E440IPC.QtdBip, E440ISC.QtdBip) e o valor do IPI efetivamente creditado (E440IPC.VecIpi, E440ISC.VecIpi) forem igual a zero e o valor do IPI (E440IPC.VlrIpi, E440ISC.VlrIpi) maior do que zero.

Inicializar controle de saldos da origem da retenção do PIS e COFINS 

Tem a finalidade de inicializar os saldos das origens das retenções de PIS e COFINS, quando a filial não efetua este controle e opta por iniciar. Não deve ser utilizado quando ainda não existe controle de retenções e neste caso, a opção existente na guia Impostos Inicializar Estrutura de Comparação das Retenções(DIRF) deve ser utilizada, pois já efetua o controle de origens se o sistema estiver parametrizado.

Sugestão de percentual de PIS e COFINS nos bens

Esta opção inicializa os campos de alíquotas de PIS e COFINS a recuperar dos bens cadastrados na base de dados, de acordo com a seguinte regra:

1. Quando a espécie do bem que for importado indicar que recupera PIS/Cofins, o sistema busca as alíquotas da nota fiscal, ligação fornecedor X produto, classificação, ou tabela de tributação, quando não possuir nota fiscal relacionada;
2. Quando não possuir nota fiscal, sugere os percentuais de acordo com a tabela de tributação dos impostos **41 – PIS não cumulativo** e **42 – COFINS não cumulativo** ligados na filial matriz, definidos como padrão.

Esta ação é necessária para que o valor do crédito do PIS/Cofins Não Cumulativo seja calculado no momento da atualização patrimonial do Bem, tanto quando o crédito é calculado com base na depreciação quando é calculado com base na aquisição.

Inicializar o tipo de produção do produto

Indica se a rotina deve fazer a atualização do campo Tipo de produção no cadastro de produtos individual (F075PRO) e agrupado (F075GFP);

Inicializar conta contábil nos documentos fiscais em tributos conforme conta contábil do produto/serviço  
Quando selecionado o sistema inicializa o campo Conta Contábil nos itens de notas fiscais de entrada/saída, item de cupom fiscal e outros documentos conforme parâmetro definido no cadastro da empresa. Essa rotina só irá funcionar se uma das opções **Atualizar NF de Saída** e **Atualizar NF de Entrada** estiver selecionada.

**Inicializar campos do Controle de Entrada e Saída (PEPS)**

Para atender o leiaute 14 do SPED Fiscal, foram incluídos novos campos no Controle de Entrada e Saída, conforme segue:

* **Controle de Entrada:** Alíquota FCP, Base FCP, Valor FCP;
* **Controle de Saída:** Base FCP Complementar, Valor FCP Complementar, CFOP, CST ICMS, Valor Total do Item, Unidade de medida.

Para inserir esses campos nos registros já presentes nas tabelas do Controle, deve-se utilizar essa rotina.

**Importante**

* A rotina atende **apenas** os campos citados acima, não interferindo nos já existentes no Controle;
* Ao processar a tela Controle de Entrada de Produtos (F075CEP), caso não tenha sido feita essa inicialização, será apresentada a mensagem: **É necessário fazer a inicialização dos campos do Controle de Entrada e Saída através da tela F660GDG para a empresa**. Uma vez feito esse procedimento, não será mais necessário realizá-lo novamente para a Empresa/Filial/Período.

## Os campos serão inicializados da seguinte forma:

**Notas Fiscais de Entrada/Compra - Tributos - E660RSC**

| Campo | Valor |
| --- | --- |
| UniMed | E440IPC.UniMed |
| NopOpe | E440IPC.NopPro |
| VlrTot | E440IPC.VlrLiq - E440IPC.VlrIcs |
| PerFcp | E070PEE.AliFcp |
| BasFcp | E440RCI.VlrBsi |
| VlrFcp | E440RCI.BasFcp \* E440RCI.PerFcp |

**Notas Fiscais de Saída/Venda - Tributos - E660RSV**

| Campo | Valor |
| --- | --- |
| UniMed | E660INV.UniMed |
| NopOpe | E660NFV.NopOpe |
| CodStr | E660INV.CodStr |
| VlrTot | (E660INV.VlrCtb - E660INV.VlrSic ) \* (E660RSV.QtdFat/E660INV.QtdEnt) |
| PerFcp | E660RSC.PerFcp |
| BasFcp | Quando E001TVE.ICMRES = "S" E660RSC.BasFcp \* E660INV.QtdEnt / E660RSC.QtdEnt |
| VlrFcp | Quando E001TVE.ICMRES = "S" E660RSC.VlrFcp \* E660INV.QtdEnt / E660RSC.QtdEnt |
| VlrBsc | (E660INV.VlrCtb - E660INV.VlrSic) \* (E660RSV.QtdFat / E660INV.QtdEnt) quando atendido filtro abaixo |
| VlrIsc | E660RSV.VlrBsc \* E660RSC.PerIcs/ 100 quando atendido filtro abaixo |
| BasFcc | E660RSV.VlrBsc quando atendido filtro abaixo |
| VlrFcc | E660RSV.BasFcc \* (E660RSC.PerFcp / 100) quando atendido filtro abaixo |

* **Filtros:**
  + E001TNS.VenTcf <> [T,D,A]
  + E085HCL.ConFin = "S"
  + E660NFV.NopOpe iniciada em 5
  + E660INV.CodStr com segundo caracter igual a "6"
  + E660RSC.VlrIcs > 0

**Cupons Fiscais - Tributos - E660RRZ**

| Campo | Valor |
| --- | --- |
| UniMed | E660IRZ > E075PRO.UniMed |
| NopOpe | E660NFV.NopOpe |
| CodStr | E660INV.CodStr |
| VlrTot | (E660INV.VlrCtb - E660INV.VlrSic ) \* (E660RSV.QtdFat/E660INV.QtdEnt) |
| PerFcp | E660RSC.PerFcp |
| BasFcp | Quando E001TVE.ICMRES = "S" E660RSC.BasFcp \* E660INV.QtdEnt / E660RSC.QtdEnt |
| VlrFcp | Quando E001TVE.ICMRES = "S" E660RSC.VlrFcp \* E660INV.QtdEnt / E660RSC.QtdEnt |
| VlrBsc | (E660INV.VlrCtb - E660INV.VlrSic) \* (E660RSV.QtdFat / E660INV.QtdEnt) quando atendido filtro abaixo |
| VlrIsc | E660RSV.VlrBsc \* E660RSC.PerIcs/ 100 quando atendido filtro abaixo |
| BasFcc | E660RSV.VlrBsc quando atendido filtro abaixo |
| VlrFcc | E660RSV.BasFcc \* (E660RSC.PerFcp / 100) quando atendido filtro abaixo |

* **Filtros:**
  + E001TNS.VenTcf <> [T,D,A]
  + E085HCL.ConFin = "S" ou sem cliente informado
  + E660REZ > E001TNS.ComNat iniciada em 5
  + E660IRZ.CodStr com segundo caracter igual a "6"
  + E660RSC.VlrIcs > 0

**Notas Fiscais de Venda - Comercial - E140RCI**

| Campo | Valor |
| --- | --- |
| UniMed | E140IPV.UniMed |
| NopOpe | E140IPV.NopPro |
| CodStr | E140IPVCodStr |
| VlrTot | (E140IPV.VlrLiq - E140IPV.VlrIcs) \* (E140RCI.QtdFat / E140IPV.QtdEnt) |
| PerFcp | E440RCI.PerFcp |
| BasFcp | Quando E001TVE.ICMRES = "S" E440RCI.BasFcp \* E140RCI.QtdEnt / E440RCI.QtdEnt |
| VlrFcp | Quando E001TVE.ICMRES = "S" E440RCI.VlrFcp \* E140RSV.QtdEnt / E440RCI.QtdEnt |
| VlrBsc | (E140IPV.VlrLiq - E140IPV.VlrIcs) \* (E140RCI.QtdFat / E140IPV.QtdFat) quando atendido filtro abaixo |
| VlrIsc | E140RCI.VlrBsc \* E440RCI.PerIcs / 100 quando atendido filtro abaixo |
| BasFcc | E140RCI.VlrBsc quando atendido filtro abaixo |
| VlrFcc | E140RCI.BasFcc \* E440RCI.PerFcp / 100 quando atendido filtro abaixo |

* **Filtros:**
  + E001TNS.VenTcf <> [T,D,A]
  + E085HCL.ConFin = "S"
  + E140IPV.NopPro iniciada em 5
  + E140IPV.CodStr com segundo caracter igual a "6"
  + E440RCI.VlrIcs > 0

Inicializar competência de transferência nas parcelas paralisadas do CIAP

Serve para inicializar o campo Competência de transferência do CIAP das parcelas paralisadas ao realizar uma transferência entre filiais. O sistema irá inicializar com o conteúdo do campo Mês e Ano das parcelas do CIAP e serão consideradas todas as parcelas do bem cujo mês e ano seja maior ou igual ao período inicial informado na tela. Esse campo é utilizado para geração dos movimentos de transferência entre filiais e inicio de imobilização no SPED Fiscal.

Inicializar a estrutura de parcelas do ICMS Cobrado Importação

O sistema inicializa a estrutura de parcelamento do ICMS Cobrado na Importação a ser lançado na apuração do ICMS como "Outros Débitos", sendo que o parcelamento será com base na quantidade de parcelas informada na tela Parâmetros da Filial para Tributos (F070FEF).

Inicializar a estrutura de parcelas do ICMS Diferido

O sistema inicializa a estrutura de parcelamento do ICMS Diferido nas operações internas a ser lançado na apuração do ICMS como "Outros Débitos", sendo que o parcelamento será com base na quantidade de parcelas informada na tela Parâmetros da Filial para Tributos (F070FEF).

Gerar guia de recolhimento para nota fiscal de entrada com valor de ICMS ST recolhido pelo fornecedor

O sistema gerará guias de recolhimento para notas fiscais de entrada que tenham os campos Valor ICMS ST Não Recuperado ou Valor ICMS Substituído preenchidos, desde que o campo Código do imposto ST para integrar guia paga pelo remetente na tela Parâmetros da Filial Tributos (F070FEF) esteja devidamente parametrizado.

## Páginas relacionadas

* [F075FCI](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075fci.htm)
* [F019TIS](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f019tis.htm)
* [F660ODC](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f660odc.htm)
* [Cadastro de Empresas](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070emp.htm)
* [F075PRO](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075pro.htm)
* [F075GFP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075gfp.htm)
* [Controle de Entrada de Produtos (F075CEP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075cep.htm)
* [Parâmetros da Filial Tributos  (F070FEF)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070fef.htm)
