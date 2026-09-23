# Conceito - Suprimentos

> **Fonte:** Conceito - Suprimentos — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/menu_suprimentos.htm  
> **Trilha:** Ajuda por telas  
> **Telas citadas:** —  
> **Identificadores de regras:** —

---
Ajuda por telas > Conceito - Suprimentos

![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/fluxos/fluxograma_area_suprimentos_thumb_0_48.jpg)

## Conceito das Gestões

### Gestão de Compras

Solicitação de Compra

* Permite o registro de todas as solicitações de compras (Produtos ou
  Serviços), que podem ser geradas manualmente, via atendimento de uma
  requisição que não tem estoque suficiente, via rotina de análise de
  reposição de estoques, via explosão de necessidades gerada pela produção. É
  a estrutura base para o registro das cotações levantadas junto aos
  fornecedores.

Cotação de Preço

* Registra as cotações de preços para as solicitações de compra.
* Junta solicitações do mesmo produto para ter maior poder de barganha.
* Sugere o preço na cotação quando da existência de uma tabela de preço do
  fornecedor cotado.
* Sugere a melhor cotação com base no valor presente.
* Possibilita o registro da cotação via WEB.
* Atualiza o histórico financeiro de todos os fornecedores.
* Exige a aprovação de uma determinada cotação, considerando usuário e
  respectivo nível de aprovação.
* Mantêm as cotações aprovadas e não aprovadas.
* Trata a aprovação de itens cotados obedecendo a limites definidos por
  usuário.
* Benefícios
* Descrever os benefícios oferecidos por cada processo (“Resultado proposto”
  do SAST atual).

Ordens de Compra

* Gera as ordens de compra efetivando a compra junto ao fornecedor.
* Trata tanto a compra de produtos como a de serviços.
* Pode ser considerada para efeito do fluxo de caixa através de parâmetros no
  fluxo.
* Sugere envio de e-mail com cópia da ordem de compra para o fornecedor.
* Permite a emissão da ordem de compra em qualquer layout.
* É gerada por diversas rotinas: manual, via cotação ou via produção.
* Trata os contratos comerciais de compra (contrato com Empresa de Limpeza ou
  Segurança, por exemplo), através da criação de uma Ordem de Compra com um
  item para cada mês, baixando o item correspondente ao mês quando da entrada
  da nota fiscal de serviço.
* Trata a geração de ordens de compra com programação de entrega para os
  clientes distribuidores e atacadistas.

Contratos

* Descrever os benefícios oferecidos por cada processo (“Resultado proposto”
  do SAST atual).

### Gestão de Recebimento

Notas Fiscais de Entrada

* Permite o registro das notas fiscais de entrada, aproveitando as informações
  das OC’s.
* Integra com estoques, contabilidade, impostos, contas a pagar, patrimônio e
  ordem de compra quando do fechamento da nota.
* Controla mercadorias de terceiros.
* Aceita entrada de mercadorias com unidade de medida diferente do estoque,
  efetuando a conversão automática.
* Trata o conceito de nota fiscal de produtor com a emissão da nota fiscal de
  entrada.
* Faz controle do retorno dos componentes enviados para industrialização.
* Processa a entrada de notas fiscais de forma simplificada para estes nichos
  de mercado.

Entrada Via Balança

* Controla as entradas de veículos para descarga de produtos (captura dos
  pesos da balança na entrada e saída), apontando a diferença entre a entrada
  da Nota Fiscal digitada com a conferência dos produtos.
* Preparado para atender empresas de extração de produtos de qualquer
  natureza.
* Benefícios
* Descrever os benefícios oferecidos por cada processo (“Resultado proposto”
  do SAST atual).

### Gestão de Estoque

Controle de Estoque

* Determina as quantidades em estoques de cada produto através das entradas e
  saídas.
* Mantêm todos os movimentos relacionados a um determinado depósito e seus
  produtos estocados.
* É a base para a rotina de fechamento, sendo recalculado o preço médio pelas
  entradas e revalorizadas as saídas pelo preço médio recalculado. Permite movimento com estoque negativo através de parametrizações especiais.
* Permite a contabilização de forma integra, garantindo a conciliação com a
  contabilidade.
* São gerados de forma manual ou via faturamento, notas fiscais de entrada,
  análise de reposição, inventário, explosão de necessidades, importação, etc.
* Possibilita o controle de movimentos com estoques bloqueados, consignados e
  reservados.
* Trata movimento de estoques em quarentena, bloqueando seus consumos e
  liberando-os conforme período pré-determinado.

Requisição Eletrônica

* Permite a geração das requisições de materiais ou serviços de forma
  eletrônica, eliminando assim o uso do papel.
* Determina produtos ou serviços, quantidades e centro de custo requisitante.
* Mantém registrado todo o controle de quem requisitou, aprovou, quem atendeu,
  etc.
* Mantêm informações gerenciais relacionadas aos centros de custos
  consumidores.
* É a estrutura base para a aprovação e posterior atendimento dos materiais ou
  serviços solicitados.

Análise de Reposição

* Calcula automaticamente as necessidades de compra, produção e transferência de materiais.
* Analisa estoques disponíveis, reservas, pedidos e ordens em andamento.
* Sugere reposições com base em parâmetros de estoque mínimo, máximo e ponto de pedido.
* Permite consolidar necessidades de diversos produtos em uma única análise.
* Exibe o saldo atual, consumo previsto e necessidade futura de cada item.
* Fornece rastreabilidade das informações utilizadas no cálculo das necessidades.
* Possibilita geração automática de Ordens de Compra a partir das sugestões aprovadas.
* Permite parametrizar a origem considerada para cálculo da necessidade dos materiais.

Inventário

* Permite a geração de inventários esporádicos, registrando as contagens e
  comparando-as com os estoques.
* Gera movimentos de acertos dos estoques a depender das diferenças apuradas.

## Páginas relacionadas

* [Ajuda por telas](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/ajuda-telas.htm)
