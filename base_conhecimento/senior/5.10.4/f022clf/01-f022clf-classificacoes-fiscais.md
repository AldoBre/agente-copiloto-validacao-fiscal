# F022CLF - Classificações Fiscais

> **Fonte:** F022CLF - Classificações Fiscais — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f022clf.htm  
> **Trilha:** Ajuda por telas > Cadastros > Mercado e Suprimentos > Parâmetros Fiscais > Classificações Fiscais  
> **Telas citadas:** F015MED, F022CLF, F403FPR  
> **Identificadores de regras:** —

---
Ajuda por telas > Cadastros > Mercado e Suprimentos > Parâmetros Fiscais > Classificações Fiscais  > Individual

Tabela de Classificações Fiscais - definida segundo a normatização da TIPI (Tabela
de Imposto de Produtos Industrializados - Nomenclatura Comum do Mercosul (NCM).

## Campos

Código CF

Código interno da classificação fiscal. (Este é o código definido junto ao
cadastro de produtos).

Descrição

Descrição da classificação fiscal.

Classificação Fiscal

Código da classificação fiscal (Código oficial da tabela nacional-NBM).

Importante

Quando houver a Proprietária de integração do Gestão Empresarial | ERP com o Gestão de Lojas ou Gestão de Supermercados, será realizada uma verificação que limitará o código da classificação fiscal à oito números, desconsiderando caracteres de uma eventual máscara.

Quando possuir integração com o um sistema de varejo do Tipo Varejo Senior, caso seja exibida a mensagem questionando sobre a geração de pendência, se optar por "Sim", serão geradas as pendências de exportação do produtos vinculado a classificações fiscal em questão. Caso opte pela opção "Não", será necessário, posteriormente, fazer uma integração dos produtos para que ambos os sistemas fiquem sincronizados.

% IPI para Entradas

Percentual de IPI da classificação para entradas. Este percentual é sugerido como
alíquota de IPI na emissão das notas fiscais de entrada.  
Na devolução de
uma nota fiscal de entrada, será considerado o percentual de IPI da nota de origem. Caso
a nota de origem (entrada) não exista, será considerado o percentual de IPI da
classificação fiscal utilizada no produto da nota de devolução.

Observação

Quando o preenchimento deste campo é alterado, ao clicar no botão Alterar, o sistema exibe uma mensagem questionando: "Aplicar o novo %IPI de entrada para todas as ligações Fornecedor x Produto com esta classificação fiscal em qual empresa?"  
Escolhendo qualquer opção apresentada na mensagem, o campo % IPI para Entrada será atualizado.

O campo % IPI na ligação Produto x Fornecedor será atualizado da seguinte forma, conforme a opção escolhida:

"Atual ou Todas": A diferença se aplica a todas as empresas ou apenas à empresa logada, quando o código da classificação fiscal for igual ao código da classificação fiscal informado na Ligação Produto x fornecedor (F403FPR) e o campo % IPI da ligação for igual ao valor anterior deste campo % IPI para Entradas da tela. Caso o valor do campo % IPI da ligação seja diferente, ele não será atualizado na ligação.

Exemplo: Na tela Classificações Fiscais (F022CLF), o código da classificação é 001 e o campo % IPI para Entrada é 7%. Na tela Ligações Fornecedor X Produtos Individual (F403FPR), para o fornecedor 1, a classificação fiscal informada é 001 e o campo % IPI é 7%. Para o fornecedor 2, a classificação fiscal informada é 001 e o campo % IPI é 8%. Ao alterar o campo % IPI para Entrada para 10%, somente o % IPI na ligação com o fornecedor 1 será atualizado, onde o valor de % de IPI é igual entre as telas.

"Cancelar": O % IPI na ligação Produto x Fornecedor não será atualizado.

% IPI para Saídas

Percentual de IPI da classificação para saídas. Este percentual é sugerido no
cadastramento dos produtos, podendo ser alterado, prevalecendo o que for definido no
próprio produto para a emissão das notas fiscais de saída.

Observação

Quando o preenchimento deste campo é alterado, ao clicar no botão Alterar, o sistema exibe na sequência, duas mensagens questionando:

1. "Aplicar o novo %IPI de Saída para todos os PRODUTOS com esta classificação fiscal em qual empresa?"
2. "Aplicar o novo %IPI Cliente para todas as ligações PRODUTO x CLIENTE com esta classificação fiscal em qual empresa?"

Valor Limite e Isenção

Indicativo do valor limite para isenção dos respectivos impostos, conforme parametrizado no cadastro da classificação fiscal do item. Quando a base de cálculo unitária dos impostos não ultrapassar o limite para isenção, a alíquota e o valor destes impostos serão zerados e utilizada a situação tributária "06 – Operação tributável a alíquota zero" para o item.

Recupera PIS

Indicativo se a classificação fiscal recupera PIS.

Recupera COFINS

Indicativo se a classificação fiscal recupera COFINS.

Observação

Ao cadastrar novos produtos, os valores informados nos campos Recupera PIS e Recupera
COFINS serão herdados da família do produto.

Tributa PIS

Indicativo se a classificação fiscal tributa PIS.

Tributa COFINS

Indicativo se a classificação fiscal tributa COFINS.

Observação

Os campos Tributa PIS e Tributa COFINS, são utilizados para sugestão de valores padrões no cadastramento de
produtos. Porém se numa nota fiscal de entrada for informado algum item sem código
(apenas pelo complemento), então esta parametrização será utilizada para os cálculos
destes impostos.

% PIS

O percentual de PIS será buscado sempre que informado conteúdo para o parâmetro da classificação fiscal do método.
Quando o percentual estiver zerado na classificação fiscal o percentual será gerado conforme a tabela de tributação.

% COFINS

O percentual de COFINS será buscado sempre que informado conteúdo para o parâmetro da classificação fiscal do
método. Quando o percentual estiver zerado na classificação fiscal o percentual será gerado conforme a tabela de
tributação.

Exceção

Informa se a classificação fiscal é ou não uma exceção.

Código Exceção

Este campo estará desabilitado quando o campo Exceção estiver com a
opção "N" (não) selecionada.

Tributação de IPI

Implica no cálculo dos valores de isentas/outras de IPI. Quando na transação, em
formas não tributadas for 'Padrão Senior' e este campo for definido com  '3' e
houver cálculo de isentas/outras de IPI, será somado ao valor de outras de IPI o valor
de isentas de IPI, zerando o valor de outras de IPI.

* 0-Normal
* 1-Tributada com Alíquota 0
* 2-Isenta
* 3-Não Tributada
* 4-Imune
* 5-Com Suspensão
* 9-Outros

Este parâmetro
não influencia no cálculo do imposto de IPI.

% II

Percentual de Imposto Importação

REGIME TRIBUTÁRIO

Este campo tem as seguintes opções:

* "C" (Regime cumulativo);
* "U" (Regime não cumulativo) e
* "N" (Nenhum).

Esta opção irá influenciar nos tipos de impostos: "41 (Pis Não Cumulativo (SPED)), 43 (Pis Cumulativo (SPED)), 42
(COFINS Não Cumulativo (SPED)), 43 (Pis Cumulativo (SPED)) e 44 (COFINS Cumulativo (SPED))" e na apuração do
faturamento na gestão de tributos.

Situação Classificação Fiscal

Indicação da situação do registro, pode assumir os valores "A" (ativo) e "I"
(inativo).

Observação

Observações para a classificação fiscal.

Código de enquadramento

Código do enquadramento legal do IPI.

Especificador situação tributária

Código especificador da situação tributária. Ele tem como objetivo estabelecer a sistemática de uniformização e identificação das mercadorias e bens passíveis de sujeição aos regimes de substituição tributária e de antecipação de recolhimento do ICMS.

Unidade Medida Fiscal

Indica a unidade de medida fiscal utilizada para conversão da unidade de medida do estoque, de acordo com o Cadastro de Unidades de Medida (F015MED).

Importante

Quando a operação é de comércio exterior, na geração do arquivo XML o sistema verifica se a unidade de medida fiscal informada difere da unidade de medida do estoque. Caso sim, aplica a conversão cadastrada na guia Conversão da tela F015MED, entre a unidade de medida de estoque e esta unidade. Os valores calculados na conversão serão utilizados para preencher as tags <qTrib> e <vUnTrib>, e a tag <uTrib> será alterada para a unidade de medida da classificação fiscal.

Esta conversão ocorre apenas na versão 4.0 da nota fiscal.

Tributação por Vlr. Min. Unidade Medida

Indica se o valor de imposto calculado por percentual deve ser comparado com o valor parametrizado para o item na tabela de tributação por quantidade cadastrada. Quando o campo estiver parametrizado como **S - Sim**, caso o valor calculado seja inferior ao cadastrado na tabela de tributação, será utilizado o valor cadastrado, ou seja, passará a tributar por quantidade, e não mais por percentual. É possível replicar a definição configurada para os produtos com a classificação fiscal em questão.

**Art. 119 do RICMS/2017**

Está relacionado à geração da ADRC-ST. Identifica se uma NCM tem relação com o art. 119 do RICMS/2017 do estado do Paraná. Sempre que o conteúdo do campo for alterado na Classificação Fiscal, todos os produtos que possuem a mesma Classificação Fiscal serão alterados.

## Parâmetros globais

| Nome | Descrição |
| --- | --- |
| ClfPisCof | Indicativo de que, quando alterado o cadastro da classificação fiscal, deve ser sugerido aos produtos/serviços, a recuperação e tributação do PIS e COFINS de acordo com a classificação fiscal alterada. Valores possíveis: **P** para perguntar; **A** para atualizar produtos/serviços da empresa atual; **T** para atualizar produtos/serviços de todas as empresas; **N** para não perguntar e não atualizar produtos/serviços. |

## Páginas relacionadas

* [Ajuda por telas](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/ajuda-telas.htm)
* [Tipo Varejo Senior](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000sis.htm)
* [F403FPR](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f403fpr.htm)
* [F015MED](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f015med.htm)
* [ClfPisCof](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#ClfPisCof)
