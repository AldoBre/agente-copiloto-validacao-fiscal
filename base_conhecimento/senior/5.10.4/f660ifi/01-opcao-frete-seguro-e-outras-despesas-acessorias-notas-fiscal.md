# Opção Frete, seguro e outras despesas acessórias - Notas Fiscal:

> **Fonte:** F660IFI - Integração de Outros Documentos — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f660ifi.htm  
> **Trilha:** Ajuda por telas > Controladoria > Gestão de Tributos > Escrituração > Integrações  
> **Telas citadas:** E001TVE, E660NFV  
> **Identificadores de regras:** —

---
Ao selecionar essa opção serão localizadas as notas fiscais de venda
(E660NFV), cujo indicativo do frete seja CIF (CIFFOB = C), e possua
valores de Frete, Seguro ou Outras Despesas Acessórias. Esta opção gera
os documentos financeiros sobre o Frete, Seguro e Outras Despesas
Acessórias presentes no faturamento.

Os documentos serão gerados de
forma consolidada, ou seja, um documento para cada tipo de despesa. E os valores serão gerados conforme as movimentações das notas fiscais de
venda (E660NFV) cuja a transação indique que o respectivo valor não é
considerado na composição do valor de Base de Cálculo do PIS e da
COFINS, e que o indicativo do frete seja "C" (por conta do emitente).

* Caso haja notas fiscais de venda com valor de frete (E660NFV.VLRFRE),
  cujas transações indicarem que este valor não compõe a Base de Cálculo
  de PIS e COFINS (E001TVE.VENFRP = "N" e E001TVE.VENFRC = "N"), estas
  serão agrupadas em um único documento na tabela de Outros Documentos.
* Caso haja notas fiscais de venda com valor de seguro
  (E660NFV.VLRSEG), cujas transações indicarem que este valor não compõe a
  Base de Cálculo de PIS e COFINS (E001TVE.VENSEP = "N" e E001TVE.VENSEP =
  "N"), estas serão agrupadas em um único documento na tabela dos outros
  documentos.
* Caso haja notas fiscais de venda com de outras despesas acessórias
  (E660NFV.VLRDAC), cujas transações indicarem que este valor não compõe a
  Base de Cálculo de PIS e COFINS (E001TVE.VENOUP = "N" e E001TVE.VENOUP =
  "N"), estas serão agrupadas em um único documento na tabela dos outros
  documentos.
* Ao efetuar uma reintegração do período, devem excluir estes tipos de
  movimentações e incluir novamente. O campo com o TIPO não terá aplicação
  nesta situação.
