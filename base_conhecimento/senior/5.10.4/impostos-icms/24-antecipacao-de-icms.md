# Antecipação de ICMS

> **Fonte:** Rotinas de ICMS — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/impostos-icms.htm#icms-antecipacao  
> **Trilha:** Segmentos > Compliance > Configurações para cálculos fiscais > Impostos  
> **Telas citadas:** E440IPC, F001TCP, F019TIS, F019TST, F051DIS, F070FCA, F070FCP, F075GFP, F075PRO, F440CIP, F440GNE, F441CIE  
> **Identificadores de regras:** —

---
## Conceito

Em operações interestaduais, podem acontecer casos nos quais o Estado destinatário prevê em sua legislação do ICMS a antecipação do recolhimento do imposto ao dar entrada da mercadoria em seu território. Tal antecipação pode ser feita pelo remetente, antes da saída da mercadoria, por guia de recolhimento em nome do destinatário.

A antecipação ICMS é o recolhimento do imposto devido pelo destinatário de sua própria operação, pago pelo adquirente.

## Parametrizações

É necessário realizar as seguintes parametrizações:

1. O campo Diferença Alíquota deve estar definido como S - Sim na tela Cadastro de Filiais (F070FCA)
2. O parâmetro Calcular diferencial de alíquota precisa estar preenchido com a opção T - Todas as operações, na guia Compras 2 da tela Parâmetros da Filial para Compras (F070FCP)
3. Na guia ICMS da tela Transações de Compras (F001TCP) o campo Calcula diferença de alíquota deve ser S - Sim.
4. O código de ICMS deve ser cadastrado no campo Tipo ICMS Substituído na tela Cadastros - Substituição de ICMS (F019TST), o parâmetro Critério Cálculo Substituição deve ser definido como 1 - Pela Margem de Lucro e o parâmetro Código da Antecipação deverá estar informado.

Observação

Caso seja definido outro critério ou o código da antecipação não esteja informado, o código do ICMS Antecipação não será utilizado para o cálculo.

5. Ao cadastrar a antecipação no Cód. Imposto Subst. / Mod. Base Cálc. na tela Tipos Substituições Impostos / Modalidade Base Cálculo / Antecipação - Por Estado (F019TIS), seleciona-se o código de ICMS Substituição, e o campo Aplicação Subst. deve ser preenchido com a opção E - Entrada.
6. Na tela Dispositivos fiscais (F051DIS) deve ser criado um dispositivo fiscal de aplicação Geral (campo Associar a documento preenchido com Sim) que reflete na apuração do ICMS como Estorno de Créditos, assim o campo Tipo de Ajuste do Documento Fiscal é preenchido com Diferencial de alíquota, e o dispositivo fiscal é associado à transação de compra destes produtos.

   Preencher os seguintes campos na tela Dispositivos fiscais (F051DIS):

   * Aplicação: SPED
   * Reflexo Apuração ICMS: 5 - D Estorno de Crédito
   * Tipo Ajuste Documento Fiscal: D - Diferencial de Alíquota.
7. Como o valor informado no campo Diferencial de alíquota já é preenchido na apuração do ICMS como Outros Créditos, este ajuste é gerado com o dispositivo para facilitar o seu estorno na apuração do ICMS. Com isso, na parametrização da apuração do ICMS será necessário associar este dispositivo fiscal como estorno de créditos, facilitando a geração do arquivo do ICMS antecipado como estorno de créditos.  

   ![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/images/suprimentos/icms-antecipacao-4_thumb_0_48.jpg)

## Processo

Ao lançar a Nota Fiscal de Entrada, o sistema segue o seguinte critério de busca para o cálculo de antecipação do ICMS: primeiramente procura pela informação do parâmetro Código ICMS Antecipação nas telas de Cadastro de Produtos (F075PRO e F075GFP). Caso não estiver preenchido, busca no campo Código ICMS Antecipação na guia ICMS do Cadastro de Transações de Compra (F001TCP). Se estes campos não estiverem preenchidos, não haverá cálculo de ICMS antecipado.

O ICMS Antecipação só é calculado para operações interestaduais.

O valor é apresentado no campo Valor Dif. de Alíquota (E440IPC.VlrDfa), da tela Nota Fiscal de Entrada - Cálculos do Item de Produto (F440CIP), acessada pelo botão Cálculos da guia Produtos das telas Nota Fiscal de Entrada Agrupada (F440GNE) e Consulta de Itens de Notas Fiscais de Entrada (F441CIE).

![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/images/suprimentos/icms-antecipacao_thumb_0_48.jpg)

### Cálculo

Na fórmula de cálculo da antecipação tributária o valor da operação é adicionado à margem de valor agregado (MVA), configurada pelo campo % Margem/Base na tela Tipos Substituições Impostos / Modalidade Base Cálculo / Antecipação - Por Estado (F019TIS), e sobre esse resultado aplica-se a alíquota interna do Estado destinatário. Desta forma:

ICMS da operação própria – R$ 1.000,00 x 12% (origem RS destino SC) = R$ 120,00  
Base cálculo da ST – R$ 1.000,00 + 40% (margem de valor agregado) = R$ 1.400,00  
R$ 1.400,00 x 17% (alíquota interna praticada no Estado de SC) = R$ 238,00  
Valor ICMS Antecipação: 238,00 - 120,00 = 118,00

O valor de R$ 118,00 constará no campo Valor Dif. de Alíquota, no item de produto da Nota Fiscal de Entrada.

Observação

A formação da base de cálculo considera as parametrizações da tela Tipos Substituições Impostos / Modalidade Base Cálculo / Antecipação - Por Estado (F019TIS).

## Apuração do ICMS

Este valor do ICMS antecipado deve ser apurado pelo imposto próprio do ICMS Diferencial de alíquota desvinculado da apuração do ICMS, ou seja, na filial a parametrização de Somar Diferencial de Alíquota na apuração do ICMS deve estar como Nunca, possibilitando com isso a geração da guia de recolhimento independente com o valor do ICMS antecipado mais o valor do diferencial de alíquota.

Na apuração do ICMS deve ser inserido o valor do ICMS antecipado como outros créditos (que já é realizado de forma automática), assim como este mesmo valor deve ser inserido como Estorno de Crédito (configuração do valor de ajuste no próprio documento, facilitando a sua automação), para que o valor possa ser demonstrado em conta gráfica na apuração, sem influenciar no valor do ICMS a recolher/creditar.

![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/images/suprimentos/icms-antecipacao-5_thumb_0_48.jpg)

## Geração da SEF

Os seguintes registros da SEF são impactados:

* Registro E020 (Lançamento - Nota Fiscal) campo 23 (Valor do ICMS creditado na operação de venda) deve ser preenchido com o valor do campo diferencial de alíquota da nota fiscal de compra
* Registro E330 (Totalização das operações do ICMS) campo 12 (Valor total do ICMS da antecipação tributária creditado) deve ser preenchido com o valor do campo diferencial de alíquota da nota fiscal de compra
* Registro E360 (Obrigações do ICMS a recolher) Neste registro além da geração da guia de recolhimento do ICMS normal, também deve considerar a guia de recolhimento do ICMS Dif. de alíquota, referente ao imposto que está associado ao ICMS
* Registro E340 (Saldos da apuração do ICMS):
  + Campo 05 (Valor do crédito do ICMS da antecipação tributária nas entradas) deve reconhecer os acertos de Outros Créditos da apuração do ICMS com dispositivos fiscais associado a este valor com tipo de ajuste do documento fiscal igual a diferencial de alíquota e inserir neste campo
  + Campo 06 (Valor dos outros créditos) deve subtrair dos valores de outros créditos da apuração do ICMS o valor inserido no campo 05
  + Campo 12 (Valor dos estornos de crédito) este campo já está sendo preenchido corretamente mediante a informação do valor a estornar o crédito conforme indicado na apuração do ICMS
  + Campo 19 (Valor do ICMS da antecipação tributária nas entradas) quando o imposto ICMS que está sendo gerado no SEF PE possuir o imposto do tipo 3 - ICMS Dif. Alíquota, apresentar neste campo o valor da pagar o diferencial de alíquota
  + Campo 23 (Valor total das obrigações a recolher para o estado) somar ao valor a recolher do ICMS normal, também considerar o valor do ICMS Dif. Alíquota (campo 19)

## Páginas relacionadas

* [F070FCA](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070fca.htm)
* [F070FCP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070fcp.htm)
* [F001TCP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f001tcp.htm)
* [F019TST](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f019tst.htm)
* [F019TIS](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f019tis.htm)
* [F051DIS](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f051dis.htm)
* [F075PRO](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075pro.htm)
* [F075GFP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075gfp.htm)
* [F440CIP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f440cip.htm)
* [F440GNE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f440gne.htm)
* [F441CIE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f441cie.htm)
