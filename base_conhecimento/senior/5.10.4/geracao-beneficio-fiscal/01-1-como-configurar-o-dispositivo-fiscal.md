# 1. Como configurar o Dispositivo Fiscal?

> **Fonte:** Configuração de Dispositivo e Benefício Fiscais — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/geracao-beneficio-fiscal.htm  
> **Trilha:** Segmentos > Compliance > Documentos Eletrônicos > NF-e | NFC-e (Nota Fiscal Eletrônica) > Nota Fiscal Eletrônica 4.0  
> **Telas citadas:** F001TAG, F001TCP, F001TDC, F001TDV, F001TVE, F009PPE, F027BNF, F051DIS, F070PSE, F075PFI, F075PPC, F075PRO, F075PXT, F080SER, F403FPR, F403FSE  
> **Identificadores de regras:** —

---
Use a tela Cadastro de Dispositivos Fiscais (F051DIS). Para mais detalhes sobre a configuração, acesse a página da tela.

**Observação**

Por conta da legislação referente aos ajustes fiscais no SPED Fiscal, o Gestão Empresarial | ERP permite o uso de vários dispositivos fiscais por item da nota. Como a NF-e permite apenas um código de Benefício Fiscal por item, o ERP irá considerar o código Benefício Fiscal do **primeiro Dispositivo Fiscal localizado**. A localização é feita através de um select único, onde o primeiro registro localizado será utilizado.

Após a criação, os Dispositivos Fiscais podem ser parametrizados nas seguintes estruturas:

* **Transação de compra:** F001TDC (formato antigo) e F001TCP (Entrada);
* **Fornecedor x Produto:** F403FPR (Entrada);
* **Fornecedor x Serviço:** F403FSE (Entrada);
* **Transação de venda:** F001TDV (formato antigo) e F001TVE (Saída);
* **Cliente x Produto:** F075PPC (Saída);
* **Parâmetros por Filial:** F075PFI (Entrada e Saída);
* **Produto:** F075PRO (Entrada e Saída);
* **Produto X Transação:** F075PXT (Entrada e Saída);
* **Serviço:** F080SER (Entrada e Saída);
* **Parâmetros por estado:** F009PPE (Entrada e Saída);
* **Produto/Serviço por Estado:** F070PSE (Entrada e Saída);
* **Situação Tributária x Dispositivo Fiscal:** F027BNF (Entrada e Saída).
* **Transações do Agronegócio:** F001TAG (Entrada e Saída).

A sequência acima não caracteriza uma hierarquia e não abrange todas as rotinas que podem ser parametrizadas.

## Páginas relacionadas

* [Cadastro de Dispositivos Fiscais (F051DIS)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f051dis.htm)
* [F001TCP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f001tcp.htm)
* [F403FPR](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f403fpr.htm)
* [F403FSE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f403fse.htm)
* [F001TVE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f001tve.htm)
* [F075PPC](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075ppc.htm)
* [F075PFI](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075pfi.htm)
* [F075PRO](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075pro.htm)
* [F075PXT](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075pxt.htm)
* [F080SER](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f080ser.htm)
* [F009PPE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f009ppe.htm)
* [F070PSE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070pse.htm)
* [F027BNF](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f027bnf.htm)
* [F001TAG](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f001tag.htm)
