# Produtos

> **Fonte:** F120GPD - Entrada de Pedidos Agrupado — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f120gpd.htm  
> **Trilha:** Ajuda por telas > Mercado > Gestão de Vendas > Pedidos  
> **Telas citadas:** E120PED, E210DLS, E210EMB, E210EST, F000AVL, F000DLS, F000RPF, F075CPD, F075EPP, F075MCP, F081CTV, F120CAI, F120FEM, F120GMP, F120GPD, F120GRD, F120MCK, F120PCE, F120PCR, F120PIP, F120PVE, F121CEB, F141CUF, F211CEE, F211CPR, F213CSL, F621APC, F621AVC, F810GCS, F813GNE  
> **Identificadores de regras:** VEN-120PRODU01

---
Principio Ativo

Mostra o valor cadastrado na derivação para registros já lançados e serve como filtro para Produto/Derivação para novas linhas.  
O campo Princípio Ativo na grade de produtos deve obrigatoriamente estar entre os campos Transação e Produto, pois o mesmo tem a função de pré-filtrar produtos. No botão C da grade o campo pode ser reposicionado para essa posição quando o mesmo estiver deslocado;

Produtos

Lançamento dos produtos.

Observação

Produtos produzidos não consistirão estoque disponível por padrão, para consistir deve-se ativar o identificador VEN-120PRODU01.

Nº Lote do cliente

Número do lote do cliente informado no pedido, essa informação pode ser inserida, alterada ou removida da grade, mesmo que os dados foram originários de uma integração, como web service.

**Nº Remessa do cliente**

Número de remessa do cliente informado no pedido, essa informação pode ser inserida, alterada ou removida da grade, mesmo que os dados foram originários de uma integração, como web service.

**Nº Pedido do cliente**

Número do pedido cliente informado no pedido, essa informação pode ser inserida, alterada ou removida da grade, mesmo que os dados foram originários de uma integração como, web service.

Data Ent. Prod.

Informa no pedido quando ele deveria entrar em produção. Não tem nenhuma consistência e não é atualizado por nenhum processo. O campo existe na tela F813GNE para ser filtrado no momento de gerar as necessidades.

**Sit. Trib. ICMS**

Situação tributária do ICMS do item do pedido. Essa informação não pode ser inserida, alterada ou removida da grade, sendo somente um informativo da sugestão dada pelo sistema.

Documento Integrado

Mostra o número do documento integrado recebido do sistema terceiro (E120PED.NUMINT).

Observação

Ao alterar as informações sobre a quantidade pedida, quantidade cancelada e a data de precisão de entrga, o produto ligado ao serviço terá seus campos alterados de forma automática. Os demais campos do item de serviço produzido não serão levados ao produto ligado ao serviço produzido quando for realizada uma alteração no serviço produzido. Isso acontece porque somente campos que influenciam na produção são considerados.

Reserva

Reservar quantidade de estoque

**Observação**

Quando o item é controlado por série e foi optado por reservar estoque, caso seja utilizada uma série que não possua saldo na E210DLS,a reserva não será gravada nessa tabela. Isso ocorre porque a série adota o conceito de um para um, ou seja, a cada movimento de entrada é gerado um novo registro na E210DLS. Assim, se a série não tiver saldo, ao realizar a entrada será criado um novo registro, impossibilitando que, no fechamento do pedido com reserva de estoque, seja vinculada uma quantidade a uma série sem saldo.

Já na E210EST, a reserva ocorrerá normalmente, garantindo que a quantidade do produto esteja corretamente reservada.

#### Botões

Cálculos 

Acesso à tela F120CAI, para exibição dos cálculos efetuados.

Estoque

Acesso à tela F211CPR, para consulta da posição do estoque.

Produto

Acesso às telas F075CPD, para consulta de produtos e suas derivações,
F075EPP, para a consulta de estoque/preço e
F075MCP, para montagem do código do produto/serviço. A opção "Montagem de Código de Produto" via entrada de pedido, apenas permite utilizar famílias que a geração do produto é por combinação.

Tab.Preço

Acesso à tela F081CTV, para a consulta da tabela de preços de venda.

Grade

Acesso à tela F120GRD, para digitação dos produtos de forma agrupada.

Grade II

Acesso à tela F120GMP, para digitação dos produtos pela derivação de forma agrupada.

Saldo Lote

Acesso a tela F213CSL, para a
consulta de posição de estoques por lote. Habilitado somente se o item for controlado por lote.

Alt. Rateios

Acesso à tela F000RPF, para exibição
da tela de alteração de rateios, desde que o
rateio seja a nível de itens.

Ult.Faturam.

Acesso à tela F141CUF, para exibição da tela de
consulta dos últimos faturamentos. A tela pode ser aberta em modo consulta ou
para carregamento dos itens na grade da tela F120GPD pelos últimos
faturamentos, maiores vendas ou produtos similares por família.

Edição Kit

Acesso à tela F120MCK, para manutenção de produtos
tipo KIT e seus componentes.

Personalizados

Acesso à tela F120PIP, para os campos personalizados
de usuário.

Carga Rec.

Acesso à tela F810GCS, para simulação de carga.

Comp.Exc

Acesso à tela F120PCE, para exibição da composição exclusiva para este pedido/item.

Proces.Exc:

Acesso à tela F120PCR, para definição dos processos exclusivos a partir do pedido.

Dist. Série

Acesso à tela F000DLS, para a distribuição por lotes
ou séries. Habilitado somente se o item posicionado na grade estiver
sujeito a um destes controles e a descrição do botão será correspondente, Lote
ou Série.

Custos

Acesso às telas F621AVC, para
análise valorizada do produto e F621APC,
para o cálculo do preço de venda para o comércio. Ambas as telas pertencem à
Gestão de Custos.

Embalagem

Acesso às telas F211CEE, para
consulta das embalagens de estocagem (tabela E210EMB), 
F121CEB, para consulta das embalagens já formadas para o pedido e
F120FEM, para formar embalagens para o pedido.

Itens via Emb.

Acesso à tela F120PVE, para informar os itens via
embalagens de estocagem. Ao sair da tela, os itens processados serão
considerados na grade da tela F120GPD. Os botões acima sempre exibirão registros ou aplicarão seus tratamentos ao
item posicionado na grade.

Vol. Agrup.

Acesso à tela F000AVL para a consulta de produtos
acabados e avulsos formados por volumes dos itens do pedido.

## Páginas relacionadas

* [VEN-120PRODU01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_120produ01.htm)
* [F813GNE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_manufatura/f813gne.htm)
* [F120CAI](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f120cai.htm)
* [F211CPR](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f211cpr.htm)
* [F075CPD](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075cpd.htm)
* [F075EPP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f075epp.htm)
* [F075MCP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075mcp.htm)
* [F081CTV](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f081ctv.htm)
* [F120GRD](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f120grd.htm)
* [F120GMP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f120gmp.htm)
* [F213CSL](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f213csl.htm)
* [F000RPF](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/f000rpf.htm)
* [F141CUF](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f141cuf.htm)
* [F120MCK](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f120mck.htm)
* [F120PIP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f120pip.htm)
* [F810GCS](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_manufatura/f810gcs.htm)
* [F120PCE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f120pce.htm)
* [F120PCR](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f120pcr.htm)
* [F000DLS](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000dls.htm)
* [F621AVC](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_custos/f621avc.htm)
* [F621APC](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_custos/f621apc.htm)
* [F211CEE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f211cee.htm)
* [F121CEB](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f121ceb.htm)
* [F120FEM](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f120fem.htm)
* [F120PVE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f120pve.htm)
* [F000AVL](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f000avl.htm)
