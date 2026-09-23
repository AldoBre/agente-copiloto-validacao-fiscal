# F075PCA - Relação Produto X Cliente agrupado

> **Fonte:** F075PCA - Relação Produto X Cliente agrupado — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075pca.htm  
> **Trilha:** Ajuda por telas > Cadastros > Produtos e Serviços > Ligações > Produto X Cliente  
> **Telas citadas:** E001TDV, E001TNS, E001TVE, E009PPE, E012FAM, E028CPG, E031MOE, E070FIL, E070VEN, E075PPC, E075PRO, E081TAB, E083ORI, E085CLI, F001TVE, F012FAM, F070FCA, F075PCA, F075PRO, F075SPC, F081TPA, F083ORI, F085CAD, F121CIP, F121CPD, F141CIS, F141CNS  
> **Identificadores de regras:** VEN-000TABPR01

---
Ajuda por telas > Cadastros > Produtos e Serviços > Ligações > Produto X Cliente > F075PCA - Relação Produto X Cliente agrupado

Destinada ao cadastramento de forma agrupada das ligações
entre clientes e produtos.

**Observação**

Utilizando os campos UF da Filial ou Transação, será possível incluir mais de uma relação entre Produto X Cliente, possibilitando que um produto possua várias configurações para o mesmo cliente filtrando por Estado ou Transação de venda do produto. O preferencial de retorno para as relações é na seguinte ordem:

* UF da Filial e Transação;
* UF da Filial;
* Transação;
* UF da Filial e Transação não informado.

## Campos

Origem

Código de origem. Estes registros estão gravados na tabela Cadastros - Origens de Produto (E083ORI) e cadastrados na tela de Cadastro de Origem de Produto (F083ORI).

Família

Código da família. Estes registros estão gravados na tabela Cadastros - Famílias (E012FAM) e cadastrados na tela de Cadastro de Famílias (F012FAM).

Tabela Preços

Código da tabela de preços. Estes registros estão gravados na tabela de Preço de Venda - Dados Gerais (E081TAB) e cadastrados na tela de Cadastro de Tabelas de Preço de Vendas Agrupada (F081TPA).

Cliente

Código do cliente. Estes registros estão gravados na tabela Cadastros - Clientes (E085CLI) e cadastrados na tela de Cadastro de Clientes (F085CAD).

Produto

Código do produto. Estes registros estão gravados na tabela Cadastros - Produtos (E075PRO) e cadastrados na tela de Cadastro de Produtos (F075PRO).

UF da Filial

Sigla do Estado da Filial. Estes registros estão gravados na tabela Cadastros - Filiais (E070FIL) e cadastrados na tela de Cadastro de Filiais (F070FCA).

Transação

Código da Transação de Venda. Estes registros estão gravados na tabela Transações - Vendas (E001TVE) e cadastrados na tela de Cadastro de Transações de Vendas (F001TVE).

Opção

Opções de processamento:

* Inserir
* Alterar
* Excluir.

Propor só

Defina a opção de exibição dos itens na grade, de acordo com as informações abaixo:

* Produtos: os registros são exibidos agrupados por produto. Quando processado, o cliente é ligado com o produto e todas as derivações recebem as mesmas informações.
* Derivações: os registros são exibidos agrupados por derivação. Quando processado, o cliente é ligado com o produto e o usuário pode ajustar cada derivação com valores diferentes entre si.

Observação

O agrupamento por derivação é semelhante ao feito na tela Relação Produto X Cliente individual (F075PPCCadastros > Clientes e Fornecedores > Clientes > Ligações > Cliente X Produto > Individual). A diferença é que, através desta, é possível ter uma visão macro, ou seja, visualizar todas as derivações dos produtos e processá-los de uma só vez.

Mostrar Somente Produtos Ativos

Quando marcado, são apresentados somente os produtos ativos.  
\* este campo fica habilitado apenas quando definido para serem apresentados os produtos
na grade.

Mostrar Somente Derivações Ativas

Quando marcado, são apresentadas somente as derivações ativas.

Observação

Este campo fica habilitado apenas quando definido para serem apresentadas as
derivações na
grade.

Código de Enquadramento Legal do IPI

Define a ligação do Código de Enquadramento de IPI entre produto e transação. Este valor pode ser sugerido nos itens das notas fiscais de entrada e saída . Para mais informações, consulte a documentação do Enquadramento de IPI.

## Grade

Cliente X Produto

Grade para exibição dos registros que atendem aos filtros informados e definições dos dados específicos para a ligação entre os produtos e clientes.

Informações oriundas das tabelas de produtos(E075PRO) e clientes(E085CLI). A configuração da
grade permite exibir/ocultar, ordenar e alterar tamanho e posição dos campos, com acesso através do caractere C, em azul no canto superior esquerdo da própria
grade.

**Per. do Diferimento de ICMS relativo ao FCP**

Percentual do diferimento de ICMS relativo ao FCP sugerido para o cálculo do valor do diferimento de ICMS relativo ao FCP nos processos de vendas e faturamento. Este campo não tem preenchimento obrigatório.

Buscar Parâmetros Fiscais

 Indica se, ao sugerir os dados do produto, devem ser sugeridos também os parâmetros fiscais da ligação do produto por cliente. O valor padrão deste campo será “S - Sim”, a fim de manter a compatibilidade. Quando o campo estiver definido com “N - Não”, os parâmetros fiscais não serão sugeridos da ligação do produto por cliente.

Simulações

Painel para simulações do preço final de venda.

Observação

Simulações permitidas somente se a opção
Propor Só estiver definida como derivações.

 Campos Passíveis de Alteração pelo Usuário

Trans. Prod. Padrão Cliente

Transação padrão para produtos.

Registros gravados nas tabelas E001TNS e E001TDV, cadastrados em
Tabelas > Transações > Cadastro > Vendas e sugeridos a partir de
Tabelas > Comercial > Fiscais > Parâmetros p/Estado.

Moeda

Moeda para cálculo do campo preço final moeda estrangeira.

Registros gravados na tabela E031MOE e cadastrados a partir de
Tabelas > Financeiro > Moedas/Índices > Cadastro/Atualização.

%Desc. Promocional

Percentual de desconto promocional.

%Desc. Extra

Percentual de desconto extra.

%Desc. Especial

Percentual de desconto especial.

Observação

Cada um dos três campos anteriores são
sucedidos de um campo Destacar com as opções:

* S - o desconto será somado ao desconto do produto no pedido ou nota fiscal, ou
  seja será destacado do preço.
* N - o desconto será aplicado diretamente no preço final de venda, ou seja estará
  embutindo no preço.

Valor Acrésc. Outras Desp.

 Valor acréscimo referente outras despesas irá compor no
cálculo do preço final de venda.

Valor Líquido

 Valor líquido pretendido no pedido ou nota fiscal.

Observação

O campo
Valor Líquido permite alteração e consequentemente poderá gerar um
%Desc.Extra ou Valor Acrésc. Outras Desp., dependendo da diferença entre o
valor informado e o preço calculado ser positiva ou negativa.

## Campos de Caráter Informativo

Produto Tributa ICMS

Indicativo se o produto tributa ICMS.

Sugerido a partir de Cadastros > Produto > Cadastro.

Cliente Tributa ICMS

Indicativo se o cliente tributa ICMS.

Sugerido a partir de Cadastros > Clientes > Cadastro.

ICMS Preço Venda

Indicativo se o ICMS é considerado no preço de venda.

Sugerido a partir de Tabelas > Transações > Cadastro > Vendas.

% ICMS

Percentual de ICMS.

Sugerido a partir de Tabelas > Comercial > Fiscais > Parâmetros p/Estado.

Considera Red.Base ICMS

Indicativo se considera o percentual de redução de base de ICMS.

Sugerido a partir de Tabelas > Transações > Cadastro > Vendas.

Redução Base ICMS

Percentual de redução de base de ICMS.

Nota

Fórmula de cálculo atual do sistema para considerar o ICMS no preço unitário
:

Preço= (Preço / ((100 - %ICMS)/100))  

Considerando que a transação soma o ICMS no preço unitário:  
Preço = 10  
ICMS = 17%  
Preço + ICMS = 12,0482  

Caso o sistema passe a considerar a redução na formação do preço, a redução é
aplicada na alíquota:  
Redução = 70%  
%ICMS com Redução = 17 - 70% = 5,1%  
Preço + ICMS = 10,5374.

% Preço Venda(Cond.Pgto)

Percentual de preço de venda da condição de pagamento.

Sugerido a partir de
Tabelas > Comercial > Condições Pagamento > Cadastro.

% Preço Venda(Parâm.p/ Est)

Percentual de preço de venda dos parâmetros por estado.

Sugerido a partir de
Tabelas > Comercial > Fiscais > Parâmetros p/Estado.

% Acréscimo Fin. (Cond.Pgto)

Percentual de acréscimo financeiro da condição de pagamento.

Sugerido a partir de
Tabelas > Comercial > Condições Pagamento > Cadastro.

% Acrésc. Preço (Sug.Valores)

Percentual de acréscimo de preço referente sugestão de valores.

Sugerido a partir de
Tabelas > Comercial > Sugestão de Valores > Valores por Sugestão.

% Desc. Cliente por Pgto. Vcto

Percentual padrão de desconto para os títulos gerados.

Sugerido a partir de
Cadastros > Clientes > Definições/Histórico.

Condição de Pagamento

Código da condição de pagamento.

Sugerido a partir de
Cadastros > Clientes > Definições/Histórico.

Tabela de Preços

Código da tabela de preços.

Sugerido a partir de
Cadastros > Clientes > Definições/Histórico.

Tabela de Preço Frete

Código da tabela de preços de frete.

Sugerido a partir de
Cadastros > Clientes > Definições/Histórico.

Preço Base

Preço base da tabela de preços.

Sugerido a partir da tabela de preços definida em
Cadastros > Clientes > Definições/Histórico,
utilizando a data atual para consistir a validade.

Preço Mínimo

Preço mínimo.

Calculado aplicando-se o percentual de tolerância a menos da
tabela de preços.

Preço Máximo

Preço máximo.

Calculado aplicando-se o percentual de tolerância a mais da
tabela de preços.

Preço Final Moeda Estrangeira

Preço final em moeda estrangeira.

Calculado aplicando-se o índice da moeda informada.

Valor de frete

Valor do frete.

Calculado conforme os dados do
cliente e produto/derivação selecionados e se o parâmetro 
E070VEN.USATPF(indicativo se usa tabela de preços de frete em pedidos,
pré-faturas e notas fiscais) estiver definido como S.

O valor de frete será calculado baseando-se na tabela de frete e transportadora associadas ao cliente bem como seu estado e cidade.

Também serão considerados o peso da derivação do produto e seu volume.

O preço unitário será utilizado para verificar se existe alguma faixa de valor onde este preço se encontre para assim também buscar o valor de frete por faixa de valor.

A soma dos valores de frete por cada critério formarão o valor de frete.

O valor de frete calculado nos pedidos e notas fiscais de venda, é o resultado da soma de todos os critérios de valor apresentados na tabela de preço de frete: Peso, Valor, Volume e Estado/Cidade.

Observação: caso exista valor de frete por critério de Distância, este não será contemplado no cálculo, da mesma forma que não é contemplado no cálculo do frete dos pedidos e notas fiscais de venda
.

Preço Final de Venda

Preço final de venda.

Cálculo do Preço Final de
Venda

1. busca do preço base na tabela de preço de vendas
2. se o parâmetro global IcmPreFin estiver definido como N-Não, aplica a Soma ou Diminuição do ICMS no preço considerando ou não a redução de base de ICMS (parâmetros da transação)
3. se o parâmetro global SomPerPre estiver definido como S-Sim, soma os seguintes descontos/acréscimos que interferem no preço de venda:
   - %Preço Venda Parâm. p/ Est. (E009PPE.VEVDSC). Pode ser positivo ou negativo
   - %Preço Venda Cond. Pagto. (E028CPG.VENDSC). Pode ser positivo ou negativo
   - %Desconto Promocional (E075PPC.DSCPRM)
   - %Desconto Extra (E075PPC.DSCEXT)
   - %Desconto Especial (E075PPC.DSCESP)
4. aplica no preço o resultado da soma acima considerando também o Valor de acréscimo unitário (E075PPC.ACRUNI)
5. se o parâmetro global SomFrePre estiver como S-Sim, soma o valor do frete no preço calculado
6. aplica o percentual de acréscimo financeiro cadastrado na condição de pagamento
7. se o parâmetro global IcmPreFin estiver definido como S-Sim, aplica a Soma ou Diminuição do ICMS no preço considerando ou não a redução de base de ICMS(parâmetros da transação)
8. aplica o percentual a acrescentar no preço unitário cadastrado nas definições para sugestão de valores
9. executa o identificador de regras VEN-000TABPR01 para alterar o preço calculado
   .

Observação

 Observação do registro posicionado na grade.

Código Fiscal Federal  
 Inserir o código fiscal federal, este campo não tem preenchimento obrigatório.

Código Fiscal Estadual  
 Inserir o código fiscal estadual, este campo não tem preenchimento obrigatório.

Código Fiscal Municipal  
 Inserir o código fiscal municipal, este campo não tem preenchimento obrigatório.

% Diferimento   
Percentual que será utilizado para o cálculo do valor do ICMS Diferido em cotações, contratos, ordens de compras, pedidos, pré-faturas e notas fiscais de entrada e saída.

Calcula FUST

Indica se o produto calcula o FUST para itens da NFCom.

Percentual FUST

Percentual do FUST para aplicar nos itens da NFCom.

Calcula FUNTTEL  
Indica se o produto calcula o FUNTTEL para itens da NFCom.

Percentual FUNTTEL

Percentual do FUNTTEL para aplicar nos itens da NFCom.

## Botões

Controle e Processamento da Tela

Seleção

Filtro complementar que acessa a tela Relação Produto x Cliente Agrupado - Seleção (F075SPC).

Mostrar

Exibe na grade os registros que atendem aos filtros informados e parâmetros
configurados.

Marcar

Marca simultaneamente todos os registros na
grade.

Desmarcar

Desmarca simultaneamente todos os registros na
grade.

Processar

Processa simultaneamente todos os registros na
grade.

Cancelar

Cancela os filtros informados no cabeçalho e a exibição dos registros.

Observação

Não cancela os processos efetuados ou registros gerados.

Ajuda

Exibe arquivo de ajuda da tela.

Sair

Sai e fecha a tela.

## Rodapé

Aplicar

Aplica as alterações efetuadas em determinado registro da
grade para
toda a coluna. Os campos com este recurso são: ICMS substituto, % desconto
promocional, % desconto extra, % desconto especial, Valor acrécimo
unitário, Indicativo de destaque de desconto promocional, Indicativo de
desta de desconto extra, Indicativo de desconto extra, Tem ICMS, Trib.Pis e Trib.Cof.. Também pode ser
executado com os campos de usuários incluídos pelo configurador.

Aplica as alterações efetuadas em determinado registro da grade para toda a coluna, para cima ou para baixo. Este recurso é aplicável para todas as colunas, exceto: Seleção, Empresa, Produto, Derivação, Cliente e campos do tipo Descrição.

A funcionalidade ainda se extende aos campos de usuários incluídos pelo configurador.

Pedidos

Consulta dos dados gerais dos pedidos. Acesso a tela F121CPD.

Itens Ped.

Consulta dos itens de pedidos. Acesso a tela F121CIP.

Notas Fiscais

Consulta dos dados gerais. Acesso a tela F141CNS.

Itens Nota

Consulta dos itens da nota fiscal. Acesso a tela F141CIS.

Mov. Estoque

Consulta dos movimentos de estoque.

Observação

A ação dos botões acima refere-se sempre ao
registro posicionado na grade.

## Identificadores de regra

|  |  |
| --- | --- |
| COM | 170VLFRE01 |
| VEN | 000TABPR01 |
| VEN | 000TNSDE01 |
| GER | 075PPCAO01 |
| GER | 081DERGN01 |

## Páginas relacionadas

* [Ajuda por telas](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/ajuda-telas.htm)
* [F083ORI](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f083ori.htm)
* [F012FAM](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f012fam.htm)
* [F081TPA](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f081tpa.htm)
* [F085CAD](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f085cad.htm)
* [F075PRO](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075pro.htm)
* [F070FCA](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070fca.htm)
* [F001TVE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f001tve.htm)
* [Enquadramento de IPI](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/enquadramento-de-ipi.htm)
* [Tabelas > Comercial > Fiscais > Parâmetros p/Estado](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f009ppe.htm)
* [Tabelas > Financeiro > Moedas/Índices > Cadastro/Atualização](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f031aim.htm)
* [Tabelas > Comercial > Condições Pagamento > Cadastro](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f028gcp.htm)
* [Tabelas > Comercial > Sugestão de Valores > Valores por Sugestão](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f037vds.htm)
* [Cadastros > Clientes > Definições/Histórico](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f085hcl.htm)
* [tabela de preços](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f081gtp.htm)
* [E070VEN.USATPF](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070fve.htm)
* [F075SPC](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075spc.htm)
* [170VLFRE01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/com_170vlfre01.htm)
* [000TABPR01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_000tabpr01.htm)
* [000TNSDE01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_000tnsde01.htm)
* [075PPCAO01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ger_075ppcao01.htm)
* [081DERGN01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ger_081dergn01.htm)
