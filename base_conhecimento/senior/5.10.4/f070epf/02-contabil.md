# Contábil

> **Fonte:** F070EPF - Cadastro de Parâmetros Fiscais — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070epf.htm  
> **Trilha:** Ajuda por telas > Cadastros > Empresas  
> **Telas citadas:** E140IPC, E140IPV, E140ISC, E140ISV, E140IXV, E140RAT, E205DEP, E440IXC, E440RAT, E660INC, E660INV, E660RTC, E660RTV, F660IDN, F660IFI, F660INZ  
> **Identificadores de regras:** —

---
Nessa guia deve ser parametrizada, para a Entrada e Saída, a origem da conta contábil por: **Produto**, **Serviço**, **Família**, **Transação** e **Depósito**.

Além das opções acima é possível parametrizar para considerar a conta contábil do rateio da nota fiscal de origem, cujo o percentual seja o mais relevante. No caso de possuir mais de uma conta contábil com o mesmo percentual, considera a primeira conta contábil lançada. O rateio é considerado, primeiramente, pelo item do documento fiscal. Caso não haja rateio no item, mas existir apenas um único rateio (apenas um registro na tabela de rateio) no cabeçalho da nota fiscal, considera o rateio desse documento.

Após configuradas todas as origens da conta contábil, é preciso configurar a ordenação de busca dessas informações, através do botão Configurar.

A sugestão da conta contábil se dará conforme o sequenciamento definido. As origens serão consideradas conforme abaixo:

* **Produto e Família**

  Conta contábil 1; Conta contábil 2; Conta contábil 3; Conta contábil 4; Conta contábil 5; Conta contábil 6.

* **Serviço e Transação**

  Conta contábil 1; Conta contábil 2; Conta contábil 3; Conta contábil 4.

* **Documento fiscal (apenas nota fiscal)**

  E660INV.CtaRed = E140IPV/E140ISV.CtaRed

  E660INC.CtaRed = E140IPC/E140ISC.CtaRed

* **Rateio documento fiscal (apenas nota fiscal)**
  + Quando a nota fiscal for de origem em Mercado/Suprimentos (OriMim = C ou D)

    E660INV/E660INC.CtaRed - E140RAT/E440RAT que possuir o maior rateio
  + Quando a nota fiscal for de origem em Importada ou Digitada (OriMim = D ou I)

    E660INV.CtaRed = E660RTV.CtaRed que produzir o maior rateio

    E660INC.CtaRed = E660RTC.CtaRed que produzir o maior rateio

* Depósito

  E660INV/E660INC.CtaRed = E140IXV/E440IXC.CodDep > E205DEP.CtaRed

Na integração de cupom fiscal (F660INZ) documentos não fiscais (F660IDN) e outros documentos (F660IFI) a conta contábil é sugerida de acordo com a parametrização, conforme:

* **Produto/serviço**: Conta contábil 1; Conta contábil 2; Conta contábil 3; Conta contábil 4; Conta contábil 5; Conta contábil 6;
* **Família**: Conta contábil 1; Conta contábil 2; Conta contábil 3; Conta contábil 4;
* **Transação**: Conta contábil 1; Conta contábil 2; Conta contábil 3; Conta contábil 4.
