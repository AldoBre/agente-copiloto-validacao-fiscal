# F440CIP - Nota Fiscal de Entrada - Cálculos do Item de Produto

> **Fonte:** F440CIP - Nota Fiscal de Entrada - Cálculos do Item de Produto — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f440cip.htm  
> **Trilha:** Ajuda por telas > Suprimentos > Gestão de Recebimento > Notas Fiscais de Entrada > Agrupada  
> **Telas citadas:** E440IPC, F000CRT, F440CIP, F440GNE, F440IMP, F441CIE  
> **Identificadores de regras:** —

---
Ajuda por telas > Suprimentos > Gestão de Recebimento > Notas Fiscais de Entrada > Agrupada > F440CIP - Nota Fiscal de Entrada - Cálculos do Item de Produto

Esta tela mostra os cálculos dos itens de produtos das notas fiscais de entrada agrupadas. É acessada por meio do botão **Cálculos** da guia Produtos das telas Nota Fiscal de Entrada Agrupada (F440GNE) e Consulta de Itens de Notas Fiscais de Entrada (F441CIE).

A publicação da Portaria SEF 013/2021 em seu art. 3º traz a forma de emissão de uma nota fiscal de ajuste referente ao estorno do valor do ICMS ST, onde na aquisição os valores do ICMS ST foram calculados a maior e não foram canceladas no prazo legal. Neste cenário, os campos **Valor base ICMS substituído destacado** (E440IPC.VlrBsd) e **Valor ICMS substituído destacado** (E440IPC.VlrIsd), informados na nota fiscal de entrada de acerto (tipo 10), terão o valor de ajuste (informado no item), **não sendo** zerados/recalculados no fechamento da nota fiscal.

A nota fiscal de acerto (tipo 10) gerada com natureza de operação (dados gerais) **998 - Estorno do ICMS-ST de NF-e emitida pelo substituído não cancelada no prazo legal** irá gerar o .XML com finalidade de emissão (FinNfe) igual a **3**. Os campos **vBCSTDest e vICMSSTDest** receberão **0** (zero) e os campos **vBCSTRet** e **vICMSSTRet** terão o valor informado na nota de acerto.

**Reforma Tributária – Consulta de Impostos**

Esta tela permite o acesso à Consulta de Impostos da Reforma Tributária (F000CRT), o qual pode ser feito das seguintes formas:

* Por meio do botão CBS e IBS, disponível nos botões de Cálculo para telas de Pedido, Ordem de Compra, Cotação e Nota Fiscal;
* Ou diretamente pelo botão CBS e IBS para as telas de consulta.

Para conferir todas as rotinas impactadas pela Reforma Tributária, acesse esta documentação.

Observação

O processo de antecipação de ICMS utiliza o campo Valor Dif. Alíquota para apresentar a informação.

O botão **Adicionar** exibe a tela de Apresentação dos cálculos dos Impostos (F440IMP), com a lista de cálculos dos impostos de agronegócio.

## Páginas relacionadas

* [Ajuda por telas](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/ajuda-telas.htm)
* [Suprimentos](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/menu_suprimentos.htm)
* [Gestão de Recebimento](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/menu_suprimentos_gestao_recebimento.htm)
* [Notas Fiscais de Entrada](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/fluxos/fluxograma_recebimento_nfentrada.htm)
* [Agrupada](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f440gne.htm)
* [F441CIE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f441cie.htm)
* [F000CRT](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000crt.htm)
* [documentação](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/reforma-tributaria/rotinas-impactadas.htm)
* [antecipação de ICMS](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/impostos-icms.htm#icms-antecipacao)
* [Apresentação dos cálculos dos Impostos (F440IMP)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f440imp.htm)
