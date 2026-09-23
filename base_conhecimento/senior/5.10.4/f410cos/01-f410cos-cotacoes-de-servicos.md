# F410COS - Cotações de Serviços

> **Fonte:** F410COS - Cotações de Serviços — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f410cos.htm  
> **Trilha:** Ajuda por telas > Suprimentos > Gestão de Compras > Cotação de Preço  
> **Telas citadas:** E410COT, F000ANX, F000PGS, F000SAM, F009COE, F021MOT, F068FNA, F099UCP, F405ASS, F410APR, F410CEA, F410COS, F410CSA, F410HCS, F410NQC, F410PES, F410QCP, F420APR, F425FOA  
> **Identificadores de regras:** COM-000ALCRT01, COM-000ALCSL01, COM-000ALINS01, COM-000ALIPI01, COM-000ALISS01, COM-000ALOUR01, COM-000ALPIT01, CPR-000ALICM01, CPR-000ALIIM01, CPR-000ALIRF01, CPR-410OBRMO01, GER-000HFOAU01

---
Ajuda por telas > Suprimentos > Gestão de Compras > Cotação de Preço > F410COS - Cotações de Serviços

Esta tela permite cotações de preços das solicitações de compras dos serviços.

## Processos

Ao clicar em Mostrar são exibidas na grade todas as solicitações que atendem aos filtros informados nos campos do cabeçalho em conjunto com os campos da tela associada ao botão Seleção. Diretamente nesta tela é executa-se o processo de cotação de preços individual e a partir do botão Cotar Agr. executa-se o processo agrupado.

O processo individual permite que sejam marcadas na grade superior apenas solicitações de compras do mesmo produto. Em seguida clica-se no botão Cotar, que habilitará a grade inferior onde informa-se os dados pertinentes a cada cotação. Cada registro na grade inferior será relativo a um fornecedor.

Com base nas diversas informações de cada fornecedor a rotina calculará o Valor Presente e preencherá o campo Melhor Cot. com um asterisco indicando a melhor cotação. Se por ventura houver mais cotações com o mesmo valor presente que representem a melhor cotação, o referido campo será preenchido apenas para o
primeiro registro gravado na tabela E410COT.

Se na aprovação de uma cotação o identificador de regras CPR-410OBRMO01 estiver cadastrado e ativo, será obrigatório informar o código do motivo no registro correspondente da grade inferior.

Após cotar os preços deve-se clicar no botão Finalizar, liberando as cotações para aprovação. Quando existir controle de aprovação multinível
cadastrado e a filial estiver configurada com o campo Estado de inicialização da cotação de preço preenchido com PRE - Em preparação, a liberação da cotação não será efetuada momento. O finalizar mantém a cotação em Processo de Cotação.

Se alguma solicitação de compra for gerada com o indicativo que necessita aprovação pelo solicitante, antes de Aprovar efetivamente suas cotações, deve-se executar a rotina associada à tela F405ASS.

Caso a rotina 9 - Cotação esteja configurada na tela F068FNA (Aprovação Multinível), a aprovação deverá ser efetuada pela tela F410APR, pois os botões Aprovar e Desaprovar destinam-se a aprovação sem controle multinível.

Os cálculos da rotina de cotação de preços serão efetuados de forma centralizada, utilizando as rotinas já existentes para a ordem de compra e nota fiscal de saída.

Ao realizar uma cotação com moda diferente da empresa, os valores de Desconto, Frete, Arredondamento, Encargos Financeiros, Outras Despesas, Seguro e Embalagens são apresentados na moeda da cotação, assim como Valor Cotação também é apresentado na moeda cotada. Os impostos aplicados na cotação também serão gravados na mesma moeda de geração da cotação. Para permitir a escolha do melhor fornecedor, o Valor Presente, Valor Unitário Presente e Valor Futuro recebem o valor final da cotação convertido para moeda da empresa.

Quando existir Aprovação Multinível, para efetuar alterações na cotação de preço é necessário que a filial esteja configurada com o campo Estado de inicialização da cotação de preço preenchido com PRE - Em preparação.

#### Desconto

O desconto pode ser aplicado ao item da cotação (serviço ou produto) através dos campos **Valor Desconto** e **% Desconto**, que funcionam da seguinte maneira:

* **% Desconto**: ao preenchê-lo, o sistema efetua automaticamente o cálculo para o campo **Valor Desconto**, considerando **(Valor Bruto do Item \* % Desconto) / 100**
* **Valor Desconto**: ao preenchê-lo, o **% Desconto** não é calculado, ficando zerado. Nesse caso, o valor do desconto não é alterado quando o item da OC, gerada por meio de uma cotação, for utilizado em uma Nota Fiscal (quantidade total ou parcial). Isso ocorre porque é necessário que haja um registro no item indicando que o desconto foi aplicado  

  Apesar do campo **Valor Desconto** não ser alterado, o cálculo do valor líquido em aberto do item considera o valor em aberto de desconto a ser aplicado. O sistema sempre rateia o desconto para cada quantidade do item. O valor de desconto em aberto é baseado no seguinte cálculo:
  + (Valor Desconto / Quantidade Pedida) \* Quantidade em Aberto.

**Exemplo:**

* Valor Desconto 1 = ( (Valor Bruto - Valor Desconto) \* % Desconto 1) / 100
* Valor Desconto 2 = ( (Valor Bruto - (Valor Desconto + Valor Desconto 1) ) \* % Desconto 1) / 100

E assim sucessivamente.

## Campos

Os campos do cabeçalho em conjunto com os campos da tela associada ao botão Seleção tem a finalidade de filtrar os registros a exibir na grade.

## Grade Solicitações de Compra

Exibe as solicitações de compras que atendem aos filtros informados.

Motivo

Código do motivo da observação de Solicitação de compra.  
São exibidos apenas os códigos ligados à Aplicação Motivo 47- Solicitação de compras, na tela F021MOT. A informação é exibida na tela F009COE (Consulta de Observações em Estoques).

Descrição do Motivo

A informação é exibida na tela F009COE (Consulta de Observações em Estoques).

Liberar

Permite que as cotações sejam marcadas para serem liberadas. Estará disponível para ser marcado quando há aprovação multinível, onde o status de inicialização de cotações na filial estiver como "PRE - Em preparação" e quando não há aprovação multinível, onde a situação da cotação estiver como "1- Processo de cotação".

## Grade Cotações/Aprovações de Compra

Permite informar as cotações dos produtos selecionados na grade de superior, incluir novas cotações, alterar e excluir cotações já cadastradas. Caso a cotação não tenha sido gravada, linhas digitadas na grade poderão ser excluídas.

Aprovar

Indicativo das cotações a aprovar.

Aprovado

Indicativo se a cotação está aprovada.

Melhor Cot.

Indicativo de melhor cotação, será preenchido pelo sistema com um.

Fornecedor

Código do fornecedor com o qual o produto esta sendo cotado.

Qtde. Cot. Fornec.

Quantidade cotada na unidade de medida do fornecedor.

UM Fornec.

Unidade de medida do produto no fornecedor.

Critério de Cotação

Critério de cotação utilizado na aprovação da cotação. A única tela que utiliza critérios de cotação diferentes de Menor valor presente é a tela F410NQC.

Preço Uni. Fornec.

Preço unitário no fornecedor.

Preço Unitário

Preço unitário na unidade de medida do produto.

Vlr. Unitário Presente

Valor unitário presente da cotação.

Vlr. Presente

Valor presente da cotação calculado pela rotina, indicará a melhor cotação.

% Diferimento

Percentual que será utilizado para o cálculo do valor do ICMS Diferido em cotações, contratos, ordens de compras e notas fiscais de entrada.

Observação

Este campo estará disponível somente quando o código da situação tributária finalizar em 51 (Diferimento). Para mais informações sobre o ICMS Diferido, consulte o processo.

% Redução ISS

Neste campo é exibido o percentual de redução do imposto sobre serviço. Para detalhes acesse a documentação do processo Redução de ISS.

Código ICMS Substituído

Este campo refere-se ao indicativo do ICMS Substituído, conforme produto. Seu preenchimento não é obrigatório, mas é sugerido de acordo com a documentação. Se a cotação for aprovada e gerar uma Ordem de Compra, as informações do ICMS Substituído parametrizadas, serão herdadas.

**Observação**

Serão exibidos na grade os percentuais definidos pelos identificadores de regras quando ativos:

* % IPI : COM-000ALIPI01
* % ICMS e % Diferimento: CPR-000ALICM01
* % I.I. : CPR-000ALIIM01
* % IRPF: CPR-000ALIRF01
* % Pis: COM-000ALPIT01
* % Cofins: COM-000ALCRT01
* % CSLL: COM-000ALCSL01
* % Out.Ret.: COM-000ALOUR01
* % ISS: COM-000ALISS01
* % INSS: COM-000ALINS01

O valor definido na regra sobrepõe o valor digitado.

## Botões

Cotar Agr.

Acesso a tela F410CSA para cotação de preços em modo agrupado.

Cotar

Habilita a grade inferior permitindo efetuar as cotações de preços das solicitações marcadas na grade superior. Somente é permitido marcar solicitações de um mesmo produto. Este botão considera as linhas selecionadas na grade Solicitações de Compra.

Observação

Não é permitido cotar juntas, solicitações cujo número de cotação seja diferente.

Eliminar

Elimina as solicitações de compra marcadas na grade Solicitações de Compra. Este botão considera a linha posicionada na grade. Caso a solicitação selecionada já estiver Cotada, ela pode ser excluí-la quando:

* o usuário logado foi o que gerou a solicitação;
* o usuário logado for superior;
* o usuário logado possuir parametrizado que **Permite excluir Solicitação a partir da Cotação** igual a **Sim**.

Serviço

Este botão considera a linha posicionada na grade Solicitações de Compra.

Requisição

Este botão considera a linha posicionada na grade Solicitações de Compra.

O.C. Pend.

Este botão considera a linha posicionada na grade Solicitações de Compra.

Liberar

Quando não existir controle de aprovação multinível, libera cotações que encontram-se em processo de cotação para aprovar. Se existir controle de aprovação multinível cadastrado e a filial estiver configurada para iniciar em "PRE - Preparação", é efetuada a liberação alterando a situação da cotação de "Em Processo de Cotação" para "A Aprovar" ou "Aprovada" e a situação do controle de aprovação para "Em Análise" ou "Aprovado". Este botão considera as linhas selecionadas na grade Solicitações de Compra, campo Liberar.

Observação

Já iniciará aprovada a cotação que se encaixar em uma faixa de valores que não possuí nível cadastrado (F068FNA).

Solicitações

Este botão considera a linha posicionada na grade Solicitações de Compra.

Quadro C.

Este botão só é habilitado ao selecionar um registro na grade Solicitações de Compra. Abre a tela F410NQC com os dados de comparação das propostas. A tela de abertura pode ser alterada para a tela F410QCP através do parâmetro global Uti410Nqc, na tela de Parâmetros Globais (F000PGS).

Finalizar

Libera as cotações marcadas na grade inferior para aprovação. Este botão considera a linha posicionada na grade Cotações/Aprovações de Compra.

Aprovar

Aprovação as cotações marcadas na grade inferior. Este botão considera as linhas selecionadas na grade Cotações/Aprovações de Compra.

Desaprovar

Desaprovação das cotações marcadas na grade inferior, permitindo nova aprovação. Este botão considera as linhas selecionadas na grade Cotações/Aprovações de CompraSolicitações de Compra.

Fornecedor

Este botão considera a linha posicionada na grade Cotações/Aprovações de Compra.

Últimas Cot.

Acesso a tela F410HCS. Este botão considera a linha posicionada na grade Cotações/Aprovações de Compra.

Parcelas Ent.

Acesso a tela F410PES. Este botão considera a linha posicionada na grade Cotações/Aprovações de Compra.

Texto Cot.

Este botão considera a linha posicionada na grade Cotações/Aprovações de Compra.

Multinível

Acesso a tela F000SAM, caso a cotação possua aprovação multinível. Este botão considera a linha posicionada na grade Cotações/Aprovações de Compra.

Excluir - Grade Cotações

Exclui cotações. Somente estará habilitado se na tela F099UCP o campo Excluir Cotações estiver definido como sim para o usuário ativo e o filtro Modalidade deverá estar exibindo apenas cotações Em Processo de Cotação ou A Aprovar. Este botão considera a linha posicionada na grade.

Observação

Ao confirmar a exclusão da cotação:

* quando a cotação excluída for originada de um Processo de Cotação, é solicitada a confirmação da exclusão destas cotações em conjunto;
* quando existir controle de aprovação multinível é exibida a informação em conjunto no momento da confirmação de exclusão. Após a exclusão, uma observação de que a cotação foi excluída com controle de aprovação em andamento é gravada na solicitação de compra;
* após excluir a cotação posicionada na grade será verificado se para a solicitação em questão ainda existe alguma cotação, caso contrário esta será liberada para novas cotações;
* ao final do processo será emitida mensagem informando que a cotação foi excluída e se foi liberada a solicitação.

Anex. Arquivo

Exibe a tela Controle de Anexos (F000ANX), permitindo anexar arquivos na cotação da solicitação. Este campo apenas estará habilitado se a solicitação selecionada possuir cotações geradas.

## Parâmetros Globais

| Nome | Descrição |
| --- | --- |
| Uti410Nqc | Indica que a tela utilizada para a comparação de propostas chamada através das telas F410CEA, F410COS, F420APR e F425FOA será a tela F410NQC. |

## Identificadores de regras

| Módulo | Código |
| --- | --- |
| CPR | 405ITCPL01 |
| CPR | 410RPFOR01 |
| CPR | 410FILLO01 |
| GER | 000APRMU01 |
| GER | 000HFOAU01 |

**Observação**

Se o identificador de regras GER-000HFOAU01 estiver ativo e a variável GerARetorno definida como "S - Sim", a geração das definições/histórico do fornecedor será feita de forma automática, sem necessidade de intervenção do usuário. Caso não esteja parametrizado dessa forma, o cadastro continua sendo feito de forma manual.

## Páginas relacionadas

* [Ajuda por telas](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/ajuda-telas.htm)
* [Suprimentos](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/menu_suprimentos.htm)
* [Gestão de Compras](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/menu_suprimentos_gestao_compras.htm)
* [Cotação de Preço](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/fluxos/fluxograma_compras_cotacao.htm)
* [CPR-410OBRMO01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/cpr_410obrmo01.htm)
* [F405ASS](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f405ass.htm)
* [F068FNA](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f068fna.htm)
* [F410APR](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f410apr.htm)
* [F021MOT](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f021mot.htm)
* [F009COE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f009coe.htm)
* [F410NQC](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f410nqc.htm)
* [presente](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f410_calculovalorpresente.htm)
* [processo](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/impostos-icms.htm)
* [Redução de ISS](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/manuais_processos/suprimentos/cadastro-reducao-iss.htm)
* [documentação](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/manuais_processos/mercado/nf-e/regras-e-sugestoes-valores.htm#codigo-icms-st)
* [F410CSA](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f410csa.htm)
* [F410QCP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f410qcp.htm)
* [Uti410Nqc](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#Uti410Nqc)
* [F410HCS](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f410hcs.htm)
* [F410PES](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f410pes.htm)
* [F099UCP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f099ucp.htm)
* [F000ANX](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/f000anx.htm)
* [405ITCPL01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/cpr_405itcpl01.htm)
* [410RPFOR01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/cpr_410rpfor01.htm)
* [410FILLO01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/cpr_410fillo01.htm)
* [000APRMU01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ger_000aprmu01.htm)
* [000HFOAU01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ger_000hfoau01.htm)
