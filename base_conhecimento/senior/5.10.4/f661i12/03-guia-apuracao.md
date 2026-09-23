# Guia Apuração

> **Fonte:** F661I12 - Resumo de Apuração do Imposto — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f661i12.htm  
> **Trilha:** Ajuda por telas > Controladoria > Gestão de Tributos > Operações e Cálculos Fiscais > Cálculos > Apuração  
> **Telas citadas:** E070IMP, E301MCR, E660BXT, E660NFV, E660ODC, E661UCR, E667SMC, F055PPF, F661CCC, F661DED, F661GRI, F661PRE  
> **Identificadores de regras:** —

---
### Cumulativo

Total Contribuição

O sistema busca o valor total da contribuição cumulativa do período, correspondendo a soma do campo Vlr. Cont.
da guia Contribuição / Cumulativa.

Crédito Desconto

Campo zerado porque é uma apuração Cumulativa.

Crédito Período Anterior

Campo zerado porque é uma apuração Cumulativa.

Total Não Cumulativa

Campo zerado porque é uma apuração Cumulativa.

Valor Retido

| Parâmetros | Origem dos valores |
| --- | --- |
| Retenção Data Baixa Título = Não (E070IMP.RetRec ou E661UCR.RetRec = "N") | São carregados os valores de retenção das notas fiscais (E660NFV.VLRPIT ou E660NFV.VLRCRT) quando o parâmetro da transação “PIS Retido NF Saída/ COFINS Retido NF Saída estiver como "-" e os valores de retenção de outros documentos de saída (E660ODC.VLRPIT ou E660ODC.VLRCRT) emitidos no período da apuração. |
| Calcular Pis/Cofins/IRPJ/CSLL Financeiro = Caixa (E070IMP.CalFin = 3) e Retenção Data Baixa Título = Sim (E070IMP.RetRec ou E661UCR.RetRec = "S") | São carregados os valores de retenção das notas fiscais (E660NFV.VLRPIT ou E660NFV.VLRCRT) quando o parâmetro da transação “PIS Retido NF Saída/ COFINS Retido NF Saída estiver como "-" e os valores de retenção de outros documentos de saída (E660ODC.VLRPIT ou E660ODC.VLRCRT) cujos títulos foram baixados no período levanto em conta a gestão tributos (E660BXT). |
| Calcular Pis/Cofins/IRPJ/CSLL Financeiro <> Caixa (E070IMP.CalFin <> 3) e Retenção Data Baixa Título = Sim (E070IMP.RetRec ou E661UCR.RetRec = "S") | São carregados os valores de retenção das notas fiscais (E660NFV.VLRPIT ou E660NFV.VLRCRT) quando o parâmetro da transação “PIS Retido NF Saída/ COFINS Retido NF Saída estiver como "-" e os valores de retenção de outros documentos de saída (E660ODC.VLRPIT ou E660ODC.VLRCRT) cujos títulos foram baixados no período levanto em conta a gestão financeira (E301MCR).  Para Outros documentos deverá ser feita a retenção e controle pela baixa do contas a receber. |

Observação

* Quando houver mudança no regime de utilização das retenções (E661UCR.RetRec <> E070IMP.RetRec) haverá um tratamento diferenciado;
* Caixa para Competência: No mês em que ocorrer a mudança de regime, além de serem consideradas as retenções das notas de venda com emissão no mês, serão consideradas também as retenções proporcionais referentes às parcelas das notas com emissão anterior ao mês, onde o pagamento tenha ocorrido dentro do mês ou que ainda não tenham sido pagas;
* Competência para Caixa: Serão consideradas as retenções proporcionais as parcelas das notas fiscais de venda, cujo pagamento aconteceu no mês, desde que a data de emissão seja maior ou igual a última alteração de regime.

Valor Dedução

Valor das deduções usadas no período para abater o valor da
contribuição a recolher, previamente cadastradas na tela
F661DED. O valor das deduções, só serão abatidos do valor da
contribuição a recolher, depois do abatimento do valor retido.

Dispositivo / FBD / Vlr. Dedução

Informar o valor de outras deduções do valor da contribuição cumulativa devida no período. Para gerar valores nesses
campos deve ser informado um Dispositivo Fiscal ou uma Forma de Busca de dados.

Valor Contribuição a Recolher

Valor da contribuição cumulativa a recolher/pagar no período da escrituração, correspondendo à operação dos
campos Total Contribuição menos Valor Retido menos Valor Dedução.

Vencimento

Vencimento da Contribuição para o período, conforme configuração feita na tela
F055PPF para a
filial matriz.

### Não-Cumulativo

Observação

Ao apurar o PIS/COFINS não cumulativo, caso o período da apuração seja igual ou maior que 04/2023, os tipos de crédito "199, 299 e 399 (Outros)" **não vão** compor o cálculo do crédito. A vigência desses códigos vai até 31/03/2023, conforme a publicação de 19/12/2022 do SPED Contribuições.

Total Contribuição

O sistema busca o valor total da contribuição não-cumulativa do período, correspondendo à soma do campo Vlr.
Cont. da guia Contribuição da guia Não-Cumulativo.

Crédito Desconto

Valor do crédito descontado, apurado no próprio período da escrituração, correspondendo ao somatório do campo Total
Créd. da guia Crédito da guia Resumo.

Crédito Período Anterior

Valor do crédito descontado, apurado em período de apuração anterior.

Total Não Cumulativa

Valor total da contribuição não cumulativa devida, correspondendo a Total Contribuição menos Crédito Desconto menos Crédito
Período Anterior.

Valor Retido

| Parâmetros | Origem dos valores |
| --- | --- |
| Retenção Data Baixa Título = Não (E070IMP.RetRec ou E661UCR.RetRec = "N") | São carregados os valores de retenção das notas fiscais (E660NFV.VLRPIT ou E660NFV.VLRCRT) quando o parâmetro da transação “PIS Retido NF Saída/ COFINS Retido NF Saída estiver como "-" e os valores de retenção de outros documentos de saída (E660ODC.VLRPIT ou E660ODC.VLRCRT) emitidos no período da apuração. |
| Calcular Pis/Cofins/IRPJ/CSLL Financeiro = Caixa (E070IMP.CalFin = 3) e Retenção Data Baixa Título = Sim (E070IMP.RetRec ou E661UCR.RetRec = "S") | São carregados os valores de retenção das notas fiscais (E660NFV.VLRPIT ou E660NFV.VLRCRT) quando o parâmetro da transação “PIS Retido NF Saída/ COFINS Retido NF Saída estiver como "-" e os valores de retenção de outros documentos de saída (E660ODC.VLRPIT ou E660ODC.VLRCRT) cujos títulos foram baixados no período levanto em conta a gestão tributos (E660BXT). |
| Calcular Pis/Cofins/IRPJ/CSLL Financeiro <> Caixa (E070IMP.CalFin <> 3) e Retenção Data Baixa Título = Sim (E070IMP.RetRec ou E661UCR.RetRec = "S") | São carregados os valores de retenção das notas fiscais (E660NFV.VLRPIT ou E660NFV.VLRCRT) quando o parâmetro da transação “PIS Retido NF Saída/ COFINS Retido NF Saída estiver como "-" e os valores de retenção de outros documentos de saída (E660ODC.VLRPIT ou E660ODC.VLRCRT) cujos títulos foram baixados no período levanto em conta a gestão financeira (E301MCR). |

Observação

* Quando houver mudança no regime de utilização das retenções (E661UCR.RetRec <> E070IMP.RetRec) haverá um tratamento diferenciado;
* Caixa para Competência: No mês em que ocorrer a mudança de regime, além de serem consideradas as retenções das notas de venda com emissão no mês, serão consideradas também as retenções proporcionais referentes às parcelas das notas com emissão anterior ao mês, onde o pagamento tenha ocorrido dentro do mês ou que ainda não tenham sido pagas;
* Competência para Caixa: Serão consideradas as retenções proporcionais as parcelas das notas fiscais de venda, cujo pagamento aconteceu no mês, desde que a data de emissão seja maior ou igual a última alteração de regime.

Valor Dedução

Valor das deduções usadas no período para abater o valor da
contribuição a recolher, previamente cadastradas na tela
F661DED. O valor das deduções, só serão abatidas do valor da
contribuição a recolher, depois do abatimento do valor retido.

Dispositivo / FBD / Vlr. Dedução

Informar o valor de outras deduções do valor da contribuição não-cumulativa devida no período. Para buscar valores
nesse campo deve ser informado um Dispositivo Fiscal ou uma Forma de Busca de dados.

Valor Contribuição a Recolher

Valor da contribuição não-cumulativa a recolher/pagar no período da escrituração, correspondendo à operação dos
campos Total Não Cumulativa menos Valor Retido menos o Vlr. Dedução.

Vencimento

Vencimento da Contribuição para o período, conforme configuração feita na tela
F055PPF para a
filial matriz.

Observação

Para considerar Outros Documentos como Crédito na apuração, a transação utilizada no
movimento deve estar configurada na base imposto liga filial, guia Imposto Não Cumulativo; Em Dados Complementares deve estar vinculada a transação a uma base cálculo crédito;
Conter valor de PIS/PASEP e COFINS e ter CST informada.

### Botões

Guias

Apresenta a tela F661GRI - Guia de Recolhimento
gerada através da apuração do cálculo do Imposto. Quando não estiver parametrizado para geração de Guia de Recolhimento automaticamente,
ao clicar nesse botão a Guia é gerada e acessada a tela da mesma.

Imprimir

É habilitado quando houver um ou mais identificador de modelo associado, com
isso ao processar o cálculo, o botão Imprimir será habilitado e a guia do imposto poderá ser
impressa.  

Quando houver mais de um um identificador ligado abrirá uma tela de Seleção de
Modelos, contendo os modelos de relatórios (Guias) ligados ao cálculo. Essa guia deve ser um modelo CIOR de 001 a 014. Os modelos CIOR015.GER e
CIOR016.GER são para as telas de guias de recolhimento.  

Quando no imposto houver
filial de pagamento informada em F055PPF e esta for diferente da filial ativa, listará a seguinte
mensagem: Não é possível imprimir a guia de recolhimento através da tela de
cálculo de impostos.

**Gravar Prévia**

Registra os dados da apuração dos impostos no formato de prévia.

**Consultar Prévia**

Abre a tela F661PRE para consulta das prévias.

**Observação**

Para mais informações, acesse a documentação sobre o processo de geração de prévias dos impostos.

### Contr. Créditos

Matriz Crédito

Exibe uma tabela para controle dos
créditos disponíveis. Esta tela retorna as
informações presentes na tabela E667SMC.

Consultar

Exibe a tela consulta de como serão utilizados os créditos disponíveis.

### Contr. Diferido

Consultar

Este botão permite consultar os valores débitos/créditos diferido
em períodos anteriores, adicionada a este período de escrituração, referente às receitas diferidas recebidas no mês
da escrituração.

Orig. Contribuições

Abre a tela Consulta Controle Crédito/Retenções (F661CCC) com base na opção escolhida:

* **Período Atual**: permite consultar as origens dos valores da contribuição a diferir no período;
* **Período Anterior**: permite consultar as origens dos valores da contribuição a diferir do período anterior.

Apuração

Permite consultar o valor dos créditos da não cumulatividade
vinculados às receitas não recebidas.

Observação

* Quando houver mais de um tipo de crédito (exemplo: 101, 202, 303...), o valor da contribuição será dividido
  proporcionalmente aos códigos do tipo de crédito e ao valor das
  bases dos créditos;
* A geração do registro M230, representada no cálculo pelo botão Apuração, **não deve** gerar mais
  créditos do que débitos; caso isto ocorra, eles serão lançados como Créditos Futuros na apuração do imposto.

### Cont. Retenções

Consultar

Exibe a tela consulta do controle das retenções de PIS/PASEP/COFINS.

### Deduções Diversas

Consultar

Exibe a tela de consulta das deduções de PIS/PASEP/COFINS.

## Páginas relacionadas

* [F055PPF](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f055ppf.htm)
* [F661GRI](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f661gri.htm)
* [F661PRE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f661pre.htm)
* [processo de geração de prévias dos impostos](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/previa-impostos.htm)
* [créditos disponíveis.](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f661cre.htm)
* [de como serão utilizados os créditos disponíveis.](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f661ccc.htm)
