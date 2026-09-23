# Rateios

> **Fonte:** F440GNE - Nota Fiscal de Entrada Agrupada — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f440gne.htm  
> **Trilha:** Ajuda por telas > Suprimentos > Gestão de Recebimento > Notas Fiscais de Entrada  
> **Telas citadas:** F001TCP, F440GNE  
> **Identificadores de regras:** CPR-440ESTRT01

---
Informação dos dados referentes aos rateios da nota fiscal. A tela de configuração da guia é acessada através do caractere C, em azul no canto superior esquerdo da própria guia. A opção habilitada para esta guia é a alteração do tamanho das colunas.

Nota

* Para notas de acerto onde não são informados produtos, ou seja, somente é informado o complemento, deve-se ter a parametrização dos campos Conta Financeira a Classificar e Centro Custo a Classificar, localizados na guia Financeiro da tela F001TCP. Sem essa parametrização, o rateio não será gerado por item
* Quando o rateio da nota fiscal é feito por itens, é necessário que o identificador de regras CPR-440ESTRT01 esteja ativo, para que o centro de custo do movimento de estoque seja igual ao do rateio. Nos casos em que já exista um centro de custo no cadastro do usuário, ele será utilizado no movimento de estoque

A tela de configuração da guia é acessada através do caractere **C**, em azul no canto superior esquerdo da própria guia. A opção habilitada para esta guia é a alteração do tamanho das colunas.

Observação

Exclusão de notas fiscais de entrada geradas a partir da rotina de Fixação de Preços não serão tratadas via tela F440GNE. São consideradas notas fiscais geradas pelo processo de fixação quando:

* For do tipo 10 - NF Acerto
* Possuir um Número de Fixação informado

**ou**

* Não possuir um Número de Fixação
* A transação usada na Ordem de Compra tiver definida com o Tipo de Recebimento igual a 3 - Compra Imediata
* O item da Ordem de Compra possuir um contrato informado

## Páginas relacionadas

* [F001TCP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f001tcp.htm)
* [CPR-440ESTRT01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/cpr_440estrt01.htm)
