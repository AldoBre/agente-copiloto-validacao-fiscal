# Campos

> **Fonte:** F140LOT - Faturamento de Pedidos Agrupado — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f140lot.htm  
> **Trilha:** Ajuda por telas > Mercado > Gestão de Faturamento e Outras Saídas > Notas Fiscais de Saída > Via Pedido  
> **Telas citadas:** E120PED, F001LTE, F009PTE, F070FVE, F140ENL  
> **Identificadores de regras:** VEN-000TNSDE01

---
Série NF

Código da série da nota fiscal.

Última NF

Número da última nota fiscal emitida.

Data Emissão

Data de emissão.

Data Saída

Data de saída.

Data Entrega

Data de entrega inicial e final.

Data Gravação

Data de gravação inicial e final dos pedidos.

Data Emissão Pedido

Ao informar a data de emissão inicial e final do pedido, este efetuará o
filtro sobre os pedidos na tabela E120PED, visualizando somente os pedidos que
estiverem no período informado.

Tipo  
Será gerado nota fiscal de saída conforme o tipo selecionado.  Tipo 1-NF
Saída (padrão). Tipo 4-NF Remessa (outros). Para nota fiscal tipo 4, caso no
pedido possuir serviço, para a sugestão da transação de serviço para a nota
fiscal é necessário que seja cadastrado uma transação cuja transação de pedido
esteja ligada a uma transação de remessa na Tabelas > Comercial > Fiscais >
Parâmetros p/Transação e Estado (F009PTE).

Máx. de Itens na Nota

Número máximo de itens (até 990) de cada nota.

Perc. Fat

Permissão do faturamento parcial de pedidos na rotina deverá ser informado o
percentual a ser faturado do pedido. O padrão deste campo é ser sugerido como
100%.

Modalidade  
Indicativo da modalidade utilizada para o filtro de pedidos na geração de notas
fiscais.
Este campo possui as opções: Produto, Serviço e Todos. A opção selecionada
será salva por usuário ao sair da tela.

Sugerir Trans. Dados Gerais nos Itens X Identificador VEN-000TNSDE01

Indicativo se deve ser sugerida a transação dos dados gerais nos itens. Ao
sair da rotina será mantida a sugestão atribuída para a próxima utilização.

Quando o campo Sugerir Trans. Dados Gerais nos Itens está marcado, o sistema não executa o identificador VEN-000TNSDE01. Este comportamento ocorre pois, quando esse campo está marcado, a transação dos dados gerais é sugerida para os itens. Já o identificador de regras em questão é apenas acionado quando a sugestão de transação é dos itens para os dados gerais.

Observação

A busca da transação de produto e serviço considera a ligação de transação com o tipo de empresa do cliente e a espécie do documento fiscal, definidos na tela Transação X Tipo Empresa e Espécie Documento (F001LTE).

Agrupar Pedidos

Indicativo se os itens devem ser agrupados.

Observação

Para agrupar pedidos em uma única nota fiscal,
os pedidos devem possuir o mesmo cliente, marca,
representante, condição de pagamento (exceto se a filial estiver configurada para agrupar pedidos com condições de pagamento diferentes),
mesmos percentuais de desconto 1, 2, 3, 4 e 5;
de oferta 1 e 2;
mesma sequência de entrega, de cobrança, mesma data de agendamento
e não devem conter parcelas especiais (exceto se for marcada em tela a opção Com Parcelas Especiais). Nos casos de agrupamento, os dados gerais da nota fiscal serão criados a partir do primeiro pedido processado.

Com seq. de entrega diferentes

Indica se
os pedidos com sequências de entrega diferentes devem ser agrupados ao
gerar o faturamento.

Com seq. de cobrança diferentes  
Indica
se os pedidos com sequências de cobrança diferentes devem ser agrupados
ao gerar o faturamento.

Emitir automaticamente a(s) nota(s) gerada(s)

Permite parametrizar se a nota fiscal será emitida automaticamente. Quando este campo estiver selecionado, será exibida uma mensagem na abertura da tela de Emissão de Nota Fiscal de Saída Agrupada (F140ENL) questionando se deseja emitir as notas, e caso opte-se por “Sim”, todas as notas fiscais serão geradas. Esta opção é salva por usuário, portanto, a opção definida pelo usuário será exibida na tela novamente em um próximo acesso (marcado/desmarcado).

Pedidos

Grade para exibição dos pedidos que atendem aos filtros informados.

**Observação**

Ao buscar os pedidos, o sistema realizará a importação dos pedidos junto com os dados itens da receita informados no pedido e irá salvar na tabela de dados dos itens da receita das notas de saída.

Ind. Presencial e Data Prest. Serviço

 Terão seus valores carregados do pedido. Se o pedido não possuir um
valor para o indicativo presencial do consumidor, o carregamento irá
sugerir um valor conforme o critério:

1. Utilizar o indicativo presencial informado nas definições do cliente;
2. Se não encontrar nas definições do cliente, irá buscar da transação
   da transação de produto, se o pedido não possuir uma transação de
   produto, então será buscado da transação de serviço.
3. Se não encontrar nas definições do cliente e nas transações, será
   utilizado o indicativo presencial informado nas definições da filial
   para as operações de vendas, tela F070FVE.  
   Os novos campos podem ter seus valores alterados.  
    A opção Agrupar Pedidos irá fazer a quebra de notas fiscais de saída
   de acordo com o indicativo presencial carregado/informado na grade.

% Diferimento

Percentual que será utilizado para o cálculo do valor do ICMS Diferido em pedidos, pré-faturas e notas fiscais de saída.

Observação

Este campo estará disponível somente quando o código da situação tributária finalizar em 51 (Diferimento). Para mais informações sobre o ICMS Diferido, consulte o processo.

% ICMS Diferido

Esse campo será calculado automaticamente quando houver percentual de diferimento informado.

## Páginas relacionadas

* [VEN-000TNSDE01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_000tnsde01.htm)
* [F001LTE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f001lte.htm)
* [F140ENL](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f140enl.htm)
* [processo](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/impostos-icms.htm)
