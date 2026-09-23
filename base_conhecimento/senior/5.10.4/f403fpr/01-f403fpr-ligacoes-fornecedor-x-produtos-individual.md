# F403FPR - Ligações Fornecedor X Produtos Individual

> **Fonte:** F403FPR - Ligações Fornecedor X Produtos Individual — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f403fpr.htm  
> **Trilha:** Ajuda por telas > Cadastros > Clientes e Fornecedores > Fornecedores > Ligações > Fornecedor X Produtos  
> **Telas citadas:** E001TCP, E070FIL, E075PRO, E403FPR, F001TCP, F012FAM, F013AGP, F075PRO, F083ORI, F085COP, F102CEI, F403FPP, F403FPR, F435CCC, F440GNE, F660NFC  
> **Identificadores de regras:** EST-210CSTLT01, GER-000HFOAU01, SGQ-102INSPE03

---
Ajuda por telas > Cadastros > Clientes e Fornecedores > Fornecedores > Ligações > Fornecedor X Produtos > Individual

Esta tela permite cadastrar a ligação entre produtos e fornecedores de forma
individualizada para as operações de compra entre o fornecedor e o produto em
questão.

Os campos comuns entre a ligação com o cadastro de produtos
tem sua prioridade subordinada ao campo Usa Produto X
Fornecedor (E075PRO.INDFPR). Para os campos comuns com o cadastro do fornecedor, prevalecerá a ligação.

**Observação**

Se o identificador de regras GER-000HFOAU01 estiver ativo e a variável GerARetorno definida como "S - Sim", a geração das definições/histórico do fornecedor será feita de forma automática, sem necessidade de intervenção do usuário. Caso não esteja parametrizado dessa forma, o cadastro continua sendo feito de forma manual.

## Campos

Fornecedor

Código do fornecedor.

Produto

Código do produto.

Derivação

Derivação do produto.

Estado da Filial

Sigla do Estado da Filial. Estes registros estão gravados na tabela E070FIL e cadastrados em Cadastros > Filiais > Cadastro.

Transação

Código da Transação de Compra. Estes registros estão gravados na tabela Transações - Compras (E001TCP) e cadastrados na tela Transações de Compras (F001TCP).

**Observação**

Utilizando os campos Estado da Filial e/ou Transação, é possível cadastrar mais de uma relação entre Fornecedor x Produto, permitindo que um mesmo produto possua diferentes configurações para o mesmo fornecedor, conforme o Estado da filial ou a transação de compra utilizada.

Quando o Estado da Filial e/ou a Transação são informados, a busca pela ligação torna-se mais específica. Por exemplo:

Ao existir uma ligação cadastrada para o Fornecedor 1, Produto 5000 e Transação 90400, essa ligação somente será considerada quando o processo que realizar a consulta corresponder exatamente a esses mesmos parâmetros. Em cenários em que sejam informados apenas o produto e o fornecedor, essa ligação específica não será retornada.

Para situações mais abrangentes, recomenda-se o cadastro de uma ligação Fornecedor x Produto contendo apenas o fornecedor e o produto, sem informar Estado da Filial ou Transação.

A ordem de prioridade utilizada na busca das ligações é a seguinte:

Estado da Filial e Transação > Estado da Filial >Transação > Estado da Filial e sem Transação.

Código Produto no Fornecedor

Código do produto no fornecedor.

Descrição

Descrição do produto no fornecedor.

Unidade de Medida

Unidade de medida do produto no fornecedor.

Prazo Entrega

Quantidade de dias de prazo de entrega do fornecedor.

Quantidade Múltipla

Quantidade múltipla de compra.

Quantidade Mínima

Quantidade mínima de compra.

Quantidade Máxima

Quantidade máxima de cada item da ordem de compra.

Nota

Os três campos anteriores sempre serão utilizados para definir a quantidade e itens da ordem de compra, independente do conteúdo dos campos Qtde Múltipla, Qtde. Mínima, Qtde. Máxima e Usa Produto X Fornecedor disponíveis na tela Cadastro de Produtos (F075PRO), nas seguintes rotinas:

* Cotação de Produto: consistências efetuadas para as
  quantidades mínima e
  múltipla na aprovação uma quantidade para compra. O usuário recebe um aviso
  apenas
* Ordem de Compra via Cotação (Produtos): a ordem nunca sairá com quantidades
  incoerentes. As quantidades sempre serão
  ajustadas de acordo com o parâmetro correspondente
* Ordem de Compra Agrupada: permitido somente informar quantidades coerentes
  com a parametrização

Percentual p/ Sugestão de Compra

Percentual para sugestão de compra do produto junto ao fornecedor. Para melhor entendimento do conceito, acesse esta documentação.

Pontuação Qualidade

Pontuação atribuída ao quesito qualidade.

Bloqueio do Fornecedor

Indicativo de bloqueio de compra do produto no fornecedor.

Código Barras

Código de barras do produto no fornecedor (EAN13).

Nota do Produto

Nota do produto. Esta informação é preenchida somente através da variável **VSNotEpi** do identificador de regras SGQ-102INSPE03. Este identificador está relacionado à gestão de qualidade e é executado na tela Registro de execução de Plano de Inspeções (F102CEI) e no web service com.senior.g5.co.sgq.execucaoinspecao porta execução. Para mais informações consulte a documentação do identificador de regras.

Classificação Fiscal

Classificação fiscal.

Origem Fiscal da Mercadoria

 Permite informar a origem fiscal da mercadoria.

Código ICMS Especial

Código do ICMS especial.

Código Redução ICMS

Código de redução do ICMS.

Código ICMS Substituído

Código do ICMS substituído.

Código Substituição Tributária PIS

Código de substituição tributária do PIS.

Código Substituição Tributária
COFINS

Código de substituição tributária do COFINS.

Recupera ICMS

Indicativo de recuperação de ICMS.

Recupera IPI

Indicativo de recuperação de IPI.

Recupera PIS

Indicativo de recuperação de PIS.

Recupera COFINS

Indicativo de recuperação de COFINS.

Calcula IPI Presumido:

Indicativo se deve ser verificada a indústria do fornecedor para IPI normal e presumido dos produtos nas notas fiscais de entrada.

Calcula ICMS Importação

Indicativo se calcula ICMS importação nas notas fiscais de importação e
ordens de compra.

Soma ICMS ao valor líquido Importação

Indicativo se deve ser somado o valor do ICMS no valor líquido das notas
fiscais de importação e ordens de compra.

Calcula PIS Importação

Indicativo se calcula PIS importação nas notas fiscais de importação e ordens
de compra.

Soma PIS ao valor líquido Importação

Indicativo se deve ser somado o valor do PIS no valor líquido das notas
fiscais de importação e ordens de compra.

Calcula COFINS Importação

Indicativo se calcula COFINS importação nas notas fiscais de importação e
ordens de compra.

Soma COFINS ao valor líquido
Importação

Indicativo se deve ser somado o valor do COFINS no valor líquido das notas
fiscais de importação e ordens de compra.

% GILRAT

Percentual de Gilrat que compõe a alíquota de Funrural.

% SENAR/SENAT

Percentual do imposto SENAT/SENAR.

Observação Motivo

Observação do motivo do bloqueio.

Usuário Motivo

Usuário responsável pelo motivo do bloqueio.

Data Motivo

Data do motivo do bloqueio.

Hora Motivo

Hora do motivo do bloqueio.

Campos de Usuário

Para atendimento das regras do processo de Controle de Qualidade (Skip Lote),
 é necessária a criação de uma estrutura para controle da quantidade sequencial
de lote para cada produto marca do Fabricante na Empresa.

Referencia o skip lote correspondente cuja qualidade efetuou os testes. Este
campo será inserido na tabela de produtos E403FPR - Ligação produto x
fornecedor, pois o skip lote trata da frequência de execução dos testes para
produto, ou seja, de quantos em quantos lotes um é retirado para análise do
laboratório. Será informado somente para produtos controlados por lote.

O controle deverá ser feito fazendo a criação de três campos de usuário na
tabela "E403FPR": Skip Lote, Entrada Lotes Produto (contador) e Status para
skip. Os campos citados deverão ser atualizados via regra através do identificador
"EST-210CSTLT01", que é
executado para cada item ao processar uma nota fiscal de entrada.

Código Fiscal Federal

Inserir o código fiscal federal, este campo não tem preenchimento obrigatório.

Código Fiscal Estadual

Inserir o código fiscal estadual, este campo não tem preenchimento obrigatório.

Código Fiscal Municipal

Inserir o código fiscal municipal, este campo não tem preenchimento obrigatório.

Código Modalidade ICMS

O Código da Modalidade ICMS do produto é sugerido, somente se o produto
indicar "Sim", no campo Usa Produto X Fornecedor, da tela
F075PRO.

% Diferimento   
Percentual que será utilizado para o cálculo do valor do ICMS Diferido em cotações, contratos, ordens de compras, pedidos, pré-faturas e notas fiscais de entrada e saída.

% IPI

Percentual de IPI válido para o produto.

|  |  |
| --- | --- |
|  | Veja também: |

* IPI
* Cálculo do IPI

Código Tabela Tributação IPI

Código da tabela de preço para o cálculo de IPI por unidade de medida.

% PIS Recuperar

Percentual do PIS a recuperar. O valor deste campo será sugerido apenas quando o parâmetro Usa Produto X Fornecedor, no cadastro de produto (F075PRO), estiver ativo.

Código Tabela Tributação PIS

Código da tabela de preço para o cálculo de PIS por unidade de medida.

% COFINS Recuperar

Percentual do COFINS a recuperar. O valor deste campo será sugerido apenas quando o parâmetro Usa Produto X Fornecedor, no cadastro de produto (F075PRO), estiver ativo.

Código Tabela Tributação COFINS

Código da tabela de preço para o cálculo de COFINS por unidade de medida.

Transação NF Ent. Produto

Possibilita definir a transação de produto que deve ser ligada ao fornecedor para ser considerada pelas notas fiscais de entrada no recebimento eletrônico.

Ato cooperado

Este campo define se o produto ligado ao fornecedor caracteriza movimentos de Ato Cooperado. O preenchimento padrão deste campo é Sim.

Para que a operação (nota fiscais de saída ou entrada) seja considerada como Ato Cooperado, é necessário também, que o fornecedor seja um cooperado ativo (F085COP) e que o campo Ato cooperado esteja preenchido com Sim, nas seguintes telas:

* Cadastro de Produtos (F075PRO)
* Cadastro de Famílias (F012FAM)
* Origem de Produtos (F083ORI)
* Agrupamento de produtos - produção (F013AGP)

Código Dispositivo Fiscal

O dispositivo fiscal informado neste campo será gerado como sugestão nas Notas Fiscais de Entrada (F660NFC e F440GNE), caso o documento seja emitido para o Fornecedor, Produto e Derivação conforme a parametrização desta tela.

Transação de recebimento para produto

Possibilita listar as transações em que a Operação de Compra for do tipo **R - Recebimento**, na guia Dados Gerais da tela Transações de Compras (F001TCP), e a transação de produto for do módulo **COF - Compras - NF Entrada Produtos**.

Transação de pagamento para produto

Possibilita listar as transações em que a Operação de Compra for do tipo **P - Pagamento**, na guia Dados Gerais da tela Transações de Compras (F001TCP), e a transação de produto for do módulo **COF - Compras - NF Entrada Produtos**.

Código de Enquadramento Legal do IPI

Define a ligação do Código de Enquadramento de IPI entre produto e transação. Este valor pode ser sugerido nos itens das notas fiscais de entrada e saída. Para mais informações, consulte a documentação do Enquadramento de IPI.

Transação Recebimento Grãos

Define uma transação para ser utilizada como sugestão no processo de recebimento de grãos em Compras - Controle de Entradas e Saídas (Expedição via Contrato com Classificação) (F435CCC).

**Percentual IPI Presumido**

Indica o percentual de IPI presumido a ser utilizado nas notas fiscais de entrada. O valor padrão do campo é **0 - 50%**. Pode ser utilizado quando a legislação permitir um percentual de IPI presumido maior que 50%, como no caso do art. 237 do RIPI.

Nesse casos, utilize o campo Percentual IPI Presumido da tela F403FPR. Este campo é responsável por indicar o percentual de IPI presumido a ser utilizado nas notas fiscais de entrada e possui o valor padrão 50% - 100%, que só será considerado caso o fornecedor seja indústria.

Sit. Trib. IPI

Código de Situação Tributária IPI.

Sit. Trib. PIS

Código de Situação Tributária PIS.

Sit. Trib. COFINS

Código de Situação Tributária COFINS.

**Nota**

Uma vez possuindo a ligação de fornecedor x produto, com os campos Sit. Trib. IPI, Sit. Trib. PIS e Sit. Trib. COFINS preenchidos, a sugestão de CST para IPI, PIS e COFINS são consideradas para as notas fiscais de compra, utilizando a seguinte ordem: Herança > Ligação Fornecedor X Produto > Cadastro de Produto. Caso contrário, segue o processo de sugestão atual (Cadastro de Produto > Transação de Compra).

**Percentual do Diferimento de ICMS relativo ao FCP**

Percentual do diferimento de ICMS relativo ao FCP sugerido para o cálculo do valor do diferimento de ICMS relativo ao FCP nos processos de compras e recebimento. Este campo não tem preenchimento obrigatório.

Botão Variações

Abre a tela de Relacionamento entre Produtos Fornecedor e Produtos (F403FPP).

## Identificadores de regra

| Módulo | Código |
| --- | --- |
| CPR | 000CPLGE01 |
| CPR | 403ATPCG01 |
| CPR | 403UFTNS01 |
| GER | 000HFOAU01 |

## Páginas relacionadas

* [Ajuda por telas](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/ajuda-telas.htm)
* [GER-000HFOAU01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ger_000hfoau01.htm)
* [F001TCP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f001tcp.htm)
* [F075PRO](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075pro.htm)
* [esta documentação](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f211aro_percom.htm)
* [SGQ-102INSPE03](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/sgq_102inspe03.htm)
* [F102CEI](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_qualidade/f102cei.htm)
* [210CSTLT01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/est_210cstlt01.htm)
* [IPI](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/impostos_ipi.htm)
* [Cálculo do IPI](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/processo_geracao_calculo_ipi.htm)
* [Ato Cooperado](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/manuais_processos/agronegocio/processos/ato-cooperado/inicio.htm)
* [F085COP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f085cop.htm)
* [F012FAM](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f012fam.htm)
* [F083ORI](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f083ori.htm)
* [F013AGP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f013agp.htm)
* [F660NFC](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f660nfc.htm)
* [F440GNE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f440gne.htm)
* [Enquadramento de IPI](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/enquadramento-de-ipi.htm)
* [Compras - Controle de Entradas e Saídas (Expedição via Contrato com Classificação) (F435CCC)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f435ccc.htm)
* [F403FPP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f403fpp.htm)
* [000CPLGE01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/cpr_000cplge01.htm)
* [403ATPCG01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/cpr_403atpcg01.htm)
* [403UFTNS01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/cpr_403uftns01.htm)
