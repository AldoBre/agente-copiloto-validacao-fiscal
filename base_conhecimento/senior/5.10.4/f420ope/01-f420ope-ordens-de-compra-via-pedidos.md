# F420OPE - Ordens de Compra via Pedidos

> **Fonte:** F420OPE - Ordens de Compra via Pedidos — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f420ope.htm  
> **Trilha:** Ajuda por telas > Suprimentos > Gestão de Compras > Ordens de Compra  
> **Telas citadas:** E120LPO, F000CRT, F095CAD, F099UCP, F420OPE, F420SPE  
> **Identificadores de regras:** GER-000HFOAU01

---
Ajuda por telas > Suprimentos > Gestão de Compras > Ordens de Compra > Via Pedido

Tela destinada à geração de ordens de compra via carteira de pedidos (somente
produtos).

## Processos

* Permite gerar várias ordens de compras para o mesmo pedido obedecendo o
  limite das quantidade no pedido;
* Para efetuar o processo de ordem de compra é necessário que
  exista pelo menos um fornecedor ligado ao produto em questão (ligação
  produto x fornecedor);
* Pode-se selecionar os itens que pertencerão a ordem de compra e alterar os
  campos da grade;
* Gerará uma ordem de compra diferente para cada diferença encontrada nos campos: Fornecedor, Cond. de Pagamento, Transportadora
  e CIFFOB;>
* As ordens de compra geradas receberão
  como data de entrada a data atual;
* As ordens de compra geradas aqui recebem na sua procedência o valor 11 - Via
  Pedido.;
* A rotina não esta preparada para tratar pedidos com produtos kit. Para estes
  casos cada item do pedido será considerado um item normal.

Observações

* As alterações nos itens de pedido não influenciarão na ordem de compra e
  vice-versa;
* Não será permitido reabilitar o pedido onde algum item tenha servido para geração de
  uma ordem de compra;
* O preço unitário e o percentual de desconto não serão herdados do pedido e
  sim da tabela de preço que está na definição no fornecedor. Não havendo a tabela,
  sua
  validade esteja vencida ou o produto não conste na tabela, o preço e o percentual de
  desconto receberão zero;
* Será permitido ao usuário alterar o preço unitário (estoque) tal como o preço do
  fornecedor. Nestes casos os valores serão convertidos conforme a unidade de
  medida de cada um;
* Alterando o fornecedor, a tabela de preço será sugerida e a unidade de medida da
  ligação Produto X Fornecedor também, com isso o preço e percentual de desconto
  também sofrerão alteração;
* Alterando a tabela de preço, o preço e percentual de desconto também sofrerão alteração;
* Se a situação do pedido for igual <b>8 - Preparação Análise ou NF</b>, a formação da quantidade a comprar realiza o seguinte cálculo: quantidade aberta do pedido - quantidade reserva exclusiva do pedido - quantidade já pedida na OC\*;
* Se a situação do pedido for diferente de <b>8 - Preparação Análise ou NF</b>, a formação da quantidade a comprar realiza o seguinte cálculo: quantidade aberta do pedido - quantidade já pedida na OC\*).

\*quantidade já pedida na OC = Quantidade já utilizada em ordens de compra com base na tabela de ligação Vendas - Pedidos - Ligação de Pedido X Ordens Compra (E120LPO).

**Reforma Tributária – Consulta de Impostos**

Esta tela permite o acesso à Consulta de Impostos da Reforma Tributária (F000CRT), o qual pode ser feito das seguintes formas:

* Por meio do botão CBS e IBS, disponível nos botões de Cálculo para telas de Pedido, Ordem de Compra, Cotação e Nota Fiscal;
* Ou diretamente pelo botão CBS e IBS para as telas de consulta.

Para conferir todas as rotinas impactadas pela Reforma Tributária, acesse esta documentação.

## Campos

Fornecedor

Código do fornecedor da ordem de compra gerada que será sugerido na grade.
Deverá haver ligação Produto X Fornecedor. Se informado no
cabeçalho e sugerido na grade, não permitirá alterá-lo. Se não informado
no cabeçalho, sugerirá o primeiro fornecedor ligado ao produto e na grade
o campo Lig exibirá um asterisco indicando que há mais fornecedores ligados ao
item e então permitirá selecionar ou informar outro.

Filial

Filial do pedido. Sugerirá a filial ativa permitindo selecionar
ou informar outra, porém a ordem de compra será gerada sempre na filial ativa.

Gerar Ordens de Compra Fechadas

Indicativo se as ordens de compra geradas serão geradas já fechadas. Ao sair
da rotina será mantido a sugestão atribuída para a próxima utilização.

Os demais campos servirão de filtro de dados em conjunto com os
campos da tela F420SPE.

## Grade Itens de Pedido (Produto)

Grade para exibição dos registros que atendem aos filtros
informados e aos seguintes critérios:

* somente pedidos desbloqueados e em situação aberto
  total ou aberto parcial;
* somente itens de pedido em situação aberto total ou aberto parcial;
* os produtos com situação ativa e do tipo comprado ou produzido e misto;
* o cliente do pedido deverá estar ativo;
* deverá haver ligação entre o produto e o fornecedor;
* a ordem de exibição na grade é:
  Filial do pedido + Número do pedido + Seq. do Item do pedido + Código do fornecedor da
  ligação Produto X Fornecedor;
* a transação apresentada na grade é a padrão para geração de ordens de
  compra de produtos cadastrada na filial;
* os valores de Cond.Pagamento, Transportadora, Tabela de Preço, CIFFOB, Percentual
  Funrural são os valores padrões para o fornecedor apontado na grade, que neste caso é o
  primeiro fornecedor da ligação Produto X Fornecedor;
* caso as unidades de medida do estoque e da ligação Produto x Fornecedor forem
  diferentes será feita a conversão
* permitirá alterar a transação de produto, a condição de pagamento e o
  indicativo CIFFOB, porém nenhum deles aceitará valor nulo.

### Campos

% Funrural

O percentual do Funrural é buscado do cadastro do fornecedor (F095CAD, campo % Funrural/INSS). Ele pode ser alterado se o usuário possuir permissão na tela F099UCP, campo Alterar Funrural OC/NF.

Observação

O % Funrural já considera o valor do Gilrat em sua porcentagem.

% Senar

O percentual do Senar é buscado do cadastro do fornecedor (F095CAD, campo % SENAR/SENAR). Ele pode ser alterado se o usuário possuir permissão na tela F099UCP, campo Alterar Senar OC/NF.

% Diferimento   
Percentual que será utilizado para o cálculo do valor do ICMS Diferido em cotações, contratos, ordens de compras e notas fiscais de entrada.

Observação

Este campo estará disponível somente quando o código da situação tributária finalizar em 51 (Diferimento). Para mais informações sobre o ICMS Diferido, consulte o processo.

## Identificadores de Regras

| Módulo | Código |
| --- | --- |
| CPR | 420DATEN01 |
| COM | 000DEFFO01 |
| COM | 000DEFCL01 |
| EST | 210PRDEP01 |
| GER | 000HFOAU01 |

**Observação**

Se o identificador de regras GER-000HFOAU01 estiver ativo e a variável GerARetorno definida como "S - Sim", a geração das definições/histórico do fornecedor será feita de forma automática, sem necessidade de intervenção do usuário. Caso não esteja parametrizado dessa forma, o cadastro continua sendo feito de forma manual.

## Páginas relacionadas

* [Ajuda por telas](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/ajuda-telas.htm)
* [Suprimentos](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/menu_suprimentos.htm)
* [Gestão de Compras](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/menu_suprimentos_gestao_compras.htm)
* [Ordens de Compra](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/fluxos/fluxograma_compras_ordemcompra.htm)
* [F000CRT](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000crt.htm)
* [documentação](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/reforma-tributaria/rotinas-impactadas.htm)
* [F420SPE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f420spe.htm)
* [F095CAD](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f095cad.htm)
* [F099UCP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f099ucp.htm)
* [processo](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/impostos-icms.htm)
* [420DATEN01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/cpr_420daten01.htm)
* [000DEFFO01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/com_000deffo01.htm)
* [000DEFCL01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/com_000defcl01.htm)
* [210PRDEP01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/est_210prdep01.htm)
* [000HFOAU01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ger_000hfoau01.htm)
