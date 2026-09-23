# F420OCC - Ordens de Compra via Contratos de Compra

> **Fonte:** F420OCC - Ordens de Compra via Contratos de Compra — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f420occ.htm  
> **Trilha:** Ajuda por telas > Suprimentos > Gestão de Compras > Ordens de Compra  
> **Telas citadas:** E420IPO, E420ISO, E460CTR, F000CRT, F000RCU, F070EMP, F420OCC, F422SCC  
> **Identificadores de regras:** GER-000HFOAU01

---
Ajuda por telas > Suprimentos > Gestão de Compras > Ordens de Compra > Via Contrato

Permite a geração de ordens de compra via contratos de
tipo 9 (Comercial de Abastecimento).

## Processos

As seguintes
condições deverão ser atendidas para
carregar os contratos na grade:

* atender a todos os filtros da tela F422SCC;
* ter como fornecedor um dos códigos informados no cabeçalho da tela;
* situação do
  contrato deverá ser ativa (E460CTR.SITCTR = A);
* o contrato deverá ser do tipo 9 (E460CTR.TIPCTR = 9);
* início de vigência contrato de compras deve ser menor ou igual a data atual
  (E460CTR.INIVIG <= Data Atual)
* final da vigência do contrato de compras deve ser maior ou igual a data atual
  (E460CTR.FIMVIG >= Data Atual);
* contrato sem controle de aprovação (E460CTR.NUMAPR = 0) ou com situação do
  controle de aprovação igual a aprovado (E460CTR.SITAPR = APR);
* quando o filtro do campo Filial Contrato estiver informado,
  serão buscados os registros onde a filial do contrato é igual a
  informada no filtro. Caso este campo não possua filtro, serão buscados
  os registros em que a filial do contrato é igual a logada no sistema.

Ao clicar em Mostrar para efetuar a consulta dos registros, caso
exista um número de contrato para mais de uma filial, será apresentada a
mensagem **O(s) contrato(s) X existe(m) em mais de uma filial. Necessário
definir o filtro de Filial Contrato**.

**Observações:**

* o fornecedor, a
  condição de pagamento, a transportadora e a forma de pagamento serão obtidos do
  contrato;
* os descontos,
  valores e preços serão obtidos do próprio item de contrato;
* os
  itens serão carregados com quantidade zerada;
* a
  ordem de compra será gerada fechada;
* caso
  exista informações de projeto e rateio no contrato, estas serão carregas para a
  ordem de compra;
* pode-se alterar o
  centro de custo por item de contrato na grade;
* para
  cada contrato carregado na tela será gerada uma ordem de compra correspondente;
* depois
  de gerada a ordem de compra, o contrato não será alterado, continuando com a
  mesma situação;
* para fins de
  registro, os itens da ordem de compra (produto (tabela E420IPO) ou
  serviço (tabela E420ISO)) gerados, recebem os campos FILCTR, NUMCTR,
  DATCPT e SEQCCP/SEQCCS do contrato base;
* a rotina de carga de
  contratos pode visualizar todas as filiais da empresa ativa;
* não há controle para a geração de ordens de compra via contrato tipo 9,
  portanto pode-se gerar quantas ordens de compra forem necessárias, dentro do
  período de vigência do contrato.
* não serão listados itens de contrato que possuem produtos e/ou serviços inativos.

Pode-se optar por duas formas de completar o rateio de centro de
custo:

1. Processando a tela sem informar nenhum centro de custo;

   Observação

   O sistema automaticamente irá herdar o centro de custo do contrato de compra para a nova ordem de compra, quando não informado nenhum centro de custo na tela, seja no campo **Centro Custos** ou no botão **Definir. C. Custo**.
2. Informar apenas um centro de custo individualmente na grade para cada item de produto/serviço;

   Observação

   Percentual para o centro de custo será sempre 100% na forma descrita acima.
3. Pelo botão **Definir C.Custos** no rodapé da tela, para viabilizar o rateio em diferentes centros de custo na tela F000RCU.  

   Observação

   Caso sejam informados centros de custo na modalidade **b**, o centro de custo informado na grade não será considerado para qualquer das duas formas. Todo rateio informado no contrato será usando (Projeto, Fase, Conta Contábil e Conta Financeira e percentuais para as contas), alterando-se apenas os centros de custo com seus respectivos percentuais

**Reforma Tributária – Consulta de Impostos**

Esta tela permite o acesso à Consulta de Impostos da Reforma Tributária (F000CRT), o qual pode ser feito das seguintes formas:

* Por meio do botão CBS e IBS, disponível nos botões de Cálculo para telas de Pedido, Ordem de Compra, Cotação e Nota Fiscal;
* Ou diretamente pelo botão CBS e IBS para as telas de consulta.

Para conferir todas as rotinas impactadas pela Reforma Tributária, acesse esta documentação.

## Campos

Os campos do cabeçalho juntamente com os campos da tela F422SCC
servirão de filtro de dados ao clique do botão Mostrar.

C. C. Aplicação

Caso este campo seja preenchido, os centros de custos utilizados no rateio na geração do contrato serão desconsiderados.

Impressão ao Processar

Indicativo de impressão das ordens de compra geradas ao final do processamento.

Grades Produtos e Serviços

Grades para exibição dos registros que atendem aos filtros informados.

% Diferimento   
Percentual que será utilizado para o cálculo do valor do ICMS Diferido em cotações, contratos, ordens de compras e notas fiscais de entrada.

Observação

Este campo estará disponível somente quando o código da situação tributária terminar em 51 (Diferimento). Para mais informações sobre o ICMS Diferido, consulte o processo. Para que o percentual de diferimento seja sugerido/preenchido para os serviços, é necessário que o parâmetro Possui serviços c/ ICMS/IPI (F070EMP) esteja preenchido com S-Sim.

## Botões

Seleção

Acesso à tela F422SCC.

Aplicar

Aplicar os valores informados para os campos Qtd.Comprar e Seq.Contrato do
registro posicionado para os demais registro da grade.

## Identificadores de regras

|  |  |
| --- | --- |
| Módulo | Código |
| CPR | 420OCPAO01 |
| EST | 210PRDEP01 |
| GER | 000PRRAT01 |
| GER | 000HFOAU01 |

**Observação**

Se o identificador de regras GER-000HFOAU01 estiver ativo e a variável GerARetorno definida como "S - Sim", a geração das definições/histórico do fornecedor será feita de forma automática, sem necessidade de intervenção do usuário. Caso não esteja parametrizado dessa forma, o cadastro continua sendo feito de forma manual.

## Parâmetro global

| Nome | Descrição |
| AltFreCpr | Define se deve alterar o Tipo de Frete para "X - Sem Frete" quando o valor do frete for 0 (zero) - Módulo Compras. |
| CodClfCtr | Indicativo se na geração da ordem de compra via contrato (F420OCC), o produto/serviço deve herdar o código da classificação fiscal do contrato |
| CodMoeEmp | Indica se o sistema deve sugerir o código da moeda da empresa (em vez de herdar do contrato) na geração da ordem de compra via contrato (F420OCC). |

## Páginas relacionadas

* [Ajuda por telas](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/ajuda-telas.htm)
* [Suprimentos](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/menu_suprimentos.htm)
* [Gestão de Compras](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/menu_suprimentos_gestao_compras.htm)
* [Ordens de Compra](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/fluxos/fluxograma_compras_ordemcompra.htm)
* [F422SCC](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f420scc.htm)
* [F000RCU](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f000rcu.htm)
* [F000CRT](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000crt.htm)
* [documentação](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/reforma-tributaria/rotinas-impactadas.htm)
* [processo](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/impostos-icms.htm)
* [F070EMP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070emp.htm)
* [420OCPAO01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/cpr_420ocpao01.htm)
* [210PRDEP01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/est_210prdep01.htm)
* [000PRRAT01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ger_000prrat01.htm)
* [000HFOAU01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ger_000hfoau01.htm)
* [AltFreCpr](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#AltFreCpr)
* [CodClfCtr](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#CodClfCtr)
* [CodMoeEmp](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#CodMoeEmp)
