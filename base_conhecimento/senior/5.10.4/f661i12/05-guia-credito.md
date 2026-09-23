# Guia Crédito

> **Fonte:** F661I12 - Resumo de Apuração do Imposto — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f661i12.htm  
> **Trilha:** Ajuda por telas > Controladoria > Gestão de Tributos > Operações e Cálculos Fiscais > Cálculos > Apuração  
> **Telas citadas:** E660INC, E660ODC, E660RCX, E661OCS, E670MOV, F055PPF, F070FEF, F661AJS, F661OPC  
> **Identificadores de regras:** —

---
A
guia Resumos faz a apuração do crédito relativo à contribuição para o PIS/Pasep e a COFINS apurado no período. O cálculo é feito somente pelo método do rateio proporcional com base na receita bruta. Para o cálculo do crédito do PIS e COFINS são realizadas algumas etapas até chegar ao valor final do crédito.

O
sistema irá gerar uma matriz de créditos baseada na Tabela 4.3.6 - Código de Tipo de Crédito.

**A tabela é divida
em três grupos:**

* 100 - Créditos vinculados à receita tributada no mercado interno (TMI);
* 200 - Créditos vinculados à receita não tributada no mercado interno (ÑTMI);
* 300 - Créditos vinculados à receita de exportação (EXP).

Esta matriz é montada com
base no faturamento bruto não cumulativo, encontrando as participações para cada CST de entrada com direito a crédito
em seu grupo.

## Regra

i. CST 50/60 = o crédito é destinado 100% para o grupo 100;

ii. CST 51/61 = o crédito é destinado 100% para o grupo 200;

iii. CST 52/62 = o crédito é destinado 100% para o grupo 300;

iv. CST 53/63 = o crédito é distribuído para os grupos 100 e 200 com a regra:

1. Grupo 100 = TMI / (TMI + ÑTMI)

2. Grupo 200 = ÑTMI / (TMI + ÑTMI)

v. CST 54/64 = o crédito é distribuído para os grupos 100 e 300 com a regra:

1. Grupo 100 = TMI / (TMI + EXP)

2. Grupo 300 = EXP / (TMI + EXP)

vi. CST 55/65 = o crédito é distribuído para os grupos 200 e 300 com a regra:

1. Grupo 200 = ÑTMI / (ÑTMI + EXP)

2. Grupo 300 = EXP / (ÑTMI + EXP)

vii. CST 56/66 = o crédito é distribuído para os grupos 100, 200 e 300 com a regra:

1. Grupo 100 = TMI / (TMI + ÑTMI + EXP)

2. Grupo 200 = ÑTMI / (TMI + ÑTMI + EXP)

3. Grupo 300 = EXP / (TMI + ÑTMI + EXP)

Após montar a matriz de
crédito será percorrido todos os itens das notas fiscais de compra (E660INC), as entradas dos outros documentos
(E660ODC) e os créditos por depreciação (E670MOV). Assim será agrupado estes movimentos pelos campos de CST, base de crédito da transação (Lista 4.3.7 SPED PIS/COFINS),
alíquota percentual, alíquota valor e CFOP iniciada em 3.

Com esse agrupamento é possível localizar quais são as CSTs
de compras do período, isso irá relatar quais grupos (100, 200 ou 300) serão gerados na apuração, pela intersecção
entre grupo e CST conforme a matriz anterior. Se o percentual for maior que 0, terá um ou mais registro para este
grupo.

O filtro para todos os
movimentos declarados acima devem considerar a CST de PIS e COFINS com os códigos que dão direito a crédito (50-56 e
60-66).

Para que os créditos
relativos ao ativo imobilizado sejam buscados no cálculo deverá ser parametrizado o crédito na tela F055PPF. Essa configuração deverá ser feita nos impostos dos Tipos 41 e 42 na
guia Imposto Não-Cumulativo. Os campos que devem ser preenchidos são: Data Base, Transação, Valor Movimento Patrimônio e Valor Desconto.

Ao calcular o imposto na gestão de Tributos, será verificado se já houve cálculo da depreciação para o período. Se
houver, gravará o valor do PIS/COFINS a recuperar na guia Créditos.

Créditos relativos à
depreciação são gerados fixos com a CST 50 e para montar a parte final
do código serão verificadas as alíquotas conforme abaixo:

## Alíquotas

* Se a alíquota por percentual for igual a 1,65% (PIS) ou 7,6% (COFINS) o complemento do código é 01;
* Se a alíquota por percentual for diferente de 1,65% (PIS) ou 7,6% (COFINS) o complemento do código é 02;
* Se a alíquota for por unidade de medida de produto e maior que 0, o complemento do código é 03;
* Se a nota fiscal de compra possuir CST do 60 a 66, o complemento do código sempre será 06;
* Se a CFOP da nota fiscal
  de compra iniciar com “3” ele gera o complemento do código 08.

Desta forma, o código 4.3.6 foi montado
possibilitando a geração do registro M105 do SPED PIS/COFINS que será gravado na tabela E661OCS.

Ainda é necessário
descobrir o valor correspondente a base de cálculo de crédito do PIS/COFINS não cumulativo. Se o complemento do
código for 01, 02, 06 ou 08, deve-se pegar o valor da base de cálculo do crédito agrupada conforme acima multiplicar
pela participação da receita bruta cumulativa no período, subtraí-se da base do crédito agrupada o valor descoberto
da participação cumulativa, o resultado multiplica-se pelo índice para o CST conforme constar na matriz de crédito
(Base de Cálculo Não Cumulativa = Base de Cálculo do Crédito \* (Receita Bruta Cumulativa / Receita Bruta Total)).

Se o complemento do
código for 03, o valor da base de cálculo do crédito deve ser diretamente a proporção Valor da Base de Cálculo do
PIS/COFINS a recuperar com a aplicação do índice para o CST conforme constar na matriz de crédito.

### Guia Resumo

Tip. Créd.

Código do tipo do crédito cujo crédito está sendo totalizado no campo, conforme a Tabela 4.3.6 (Tabela Código de
Tipo de Crédito). Os códigos dos tipos de créditos são definidos a partir das informações de CST e Alíquota
constante nos documentos fiscais e outros documentos.

Alíq. Imp.

Alíquota aplicável à base de crédito informada no campo anterior.

Vlr. Bas. Cálc.

Somatória dos campos Vlr. Bas. Cál. Cré. da guia Detalhamento do Resumo do Crédito.

Tot. Créd.

O valor total do respectivo crédito apurado no período deverá ser igual à multiplicação dos campos Alíq. Imp. e Vlr.
Bas. Cálc.

Ajust. Acr.

Informar o valor a ser adicionado por ajuste ao crédito do período. Para buscar valores nesse campo deve ser
informado um Dispositivo Fiscal ou uma Forma de Busca de dados na guia de Ajustes.

Ajust. Red.

Informar o valor a ser subtraído por ajuste ao crédito do período. A busca desses valores ocorre através da
guia de
Ajustes onde existe a opção de informar um Dispositivo Fiscal ou uma Forma de Busca de dados.

Observação

* O campo Ajust. Red. 1 buscará os valores referentes à devolução de compra do regime de tributação
  não-cumulativo;
* As notas fiscais de saída do tipo 2 são levadas em consideração e os valores do imposto referente à
  devolução serão buscados dos campos: VlrBpr, QtdBpi, PerPir, AliPIS, VlrPir, VlrBcr, QtdBco, PerCor, AliCof, VlrCor:
  + Para buscar as informações nesse campo, é necessário ter cadastrado um dispositivo fiscal específico
    para devolução. A aplicação do dispositivo deverá ser 02, não estar associado a documento, ter mensagem de devolução
    e informar o respectivo código de ajuste para SPED PIS/COFINS;
  + Esse dispositivo será gerado automaticamente na apuração do PIS e COFINS na
    guia Crédito,
    em Ajustes no campo Ajust. Red 1.

Vlr. Dif.

O sistema irá buscar o valor dos créditos da não cumulatividade vinculados às receitas ainda
não recebidas decorrentes da celebração de contratos com pessoa jurídica de direito público, empresa pública,
sociedade de economia mista ou suas subsidiárias, relativos à construção por empreitada ou a fornecimento a preço
predeterminado de bens ou serviços (parágrafo único e no caput do art. 7º da Lei nº 9.718, de 1998).

Total Créd.

Informar o valor total do respectivo crédito relativo ao período, correspondendo à Tot. Créd. mais Ajust. Acr. menos Ajust.
Red. menos Vlr. Dif.

### Guia Detalhamento

Base Cálc. Créd.

O código da Base Cálculo do Crédito será gerado conforme: 10 (Máquinas, equipamentos e outros bens incorporados ao ativo imobilizado - crédito com base no valor de aquisição) quando o campo Origem da Parcela de PIS/COFINS Mês (ORIPPI) for igual a "Q - Quantidade de mês" e o campo Base Cálculo Crédito (BASCRE) não estiver previamente preenchido na nota ou na transação de depreciação. Caso não se enquadre na situação anterior, irá buscar o código do campo Base Cálculo Crédito (BASCRE) da tabela da nota do bem ou da transação do movimento do bem.

Sit. Trib.

Código da Situação Tributária referente ao crédito de PIS/Pasep e COFINS vinculado ao tipo de crédito escriturado.

Tot. Bas. Cálc.

Valor Total da Base de Cálculo escriturada nos documentos Fiscais e Outros Campos, referente ao CST informada no
campo anterior e código do campo Base Cálc. Créd.

Tot. Bas. Cál. Cum.

Parcela do Valor Total da Base de Cálculo informada no campo anterior, vinculada a receitas com incidência
cumulativa (Tot. Bas. Cálc x Percentual Receita Cumulativa no período).

Bas. Cál. Não Cum.

Valor Total da Base de Cálculo do Crédito, vinculada a receitas com incidência não-cumulativa (Tot. Bas. Cálc. menos Tot.
Bas. Cál. Cum.).

Vlr. Bas. Cál. Cré.

Valor da Base de Cálculo do Crédito, vinculada ao tipo de Crédito escriturado (Bas. Cál. Não Cum. X Percentual da
Matriz de Crédito correspondente ao CST que consta no campo Sit. Trib).

Descr.

Informar descrição do crédito (Opcional – preenchido manualmente).

### Guia Ajustes

Os dispositivos e forma de busca de dados têm a função de informar do que se trata os valores informados na tela de
cálculo. Os dispositivos fiscais apresentados no campo Associar a Documento Fiscal que são igual a "S - Sim" e foram
a associados nas
notas fiscais com valor de ajuste, o valor será carregado automaticamente ao ser informado para a linha que esta
posicionado.

## Exemplo

Se houver valor para a apuração do Cumulativo na linha Contribuição Cumulativa Apurada a alíquota
básica e estiver posicionado na guia Ajustes os campos de Dispositivos e Formas de Busca de dados serão
referente a esta linha. Ou seja, a guia de Ajustes é válida para cada linha da guia Descrição (Contr. Soc.).

### Botões

Origens

Abre a tela Consulta das Origens de
PIS/COFINS (F661OPC), que lista as informações das origens de PIS/COFINS
nas guias Item Saída, Item Redução Z ou Outros Documentos. Para os impostos 47 e 48, as origens listadas serão os movimentos da
tabela E660RCX.

Ajustes

Abre a tela de lançamento de ajustes (F661AJS).

Exclusões

Este botão fica visível apenas quando o parâmetro **Tipo de Sociedade Cooperativa** (F070FEF) estiver preenchido. Ao excluir o cálculo de uma contribuição, o seu total será recalculado. As informações apuradas e digitadas nessa tela serão utilizadas como base para gerar os registros M211 e M611
do SPED Contribuições.

## Páginas relacionadas

* [F055PPF](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f055ppf.htm)
* [F661AJS](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f661ajs.htm)
* [F070FEF](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070fef.htm)
