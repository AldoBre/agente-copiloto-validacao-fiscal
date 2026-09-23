# F403FSE - Ligações Fornecedor X Serviços Individual

> **Fonte:** F403FSE - Ligações Fornecedor X Serviços Individual — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f403fse.htm  
> **Trilha:** Ajuda por telas > Cadastros > Clientes e Fornecedores > Fornecedores > Ligações > Fornecedor X Serviços  
> **Telas citadas:** F001TCP, F075PRO, F118PSI, F403FSE, F440GNE, F660NFC  
> **Identificadores de regras:** CPR-000INESR01

---
Ajuda por telas > Cadastros > Clientes e Fornecedores > Fornecedores > Ligações > Fornecedor X Serviços > Individual

Tela destinada às ligações entre os fornecedores e serviços de
forma individualizada.

## Campos

Campos de Usuário

 Preenchimento de campos referente, data, hora e usuário da Geração/Atualização.

Código Fiscal Federal

 Inserir o código fiscal federal, este campo não tem preenchimento obrigatório.

Código Fiscal Estadual

 Inserir o código fiscal estadual, este campo não tem preenchimento obrigatório.

Código Fiscal Municipal

 Inserir o código fiscal municipal, este campo não tem preenchimento obrigatório.

Guia de Recolhimento

 Informa-se o código da guia de recolhimento.

Ao inserir uma nota fiscal com item de serviço, caso o serviço não tenha o campo Guia de Recolhimento preenchido, será mostrado automaticamente no campo Código Tributação da nota fiscal o valor do campo Código Tributação p/DARF do cadastro do serviço.

Ao inserir uma nota fiscal com item de serviço, caso o serviço tenha o campo Guia de Recolhimento preenchido e esta guia não tenha o campo Documento de Arrecadação preenchido, será mostrado automaticamente no campo Código Tributação da nota fiscal o valor do campo Código Tributação p/DARF do cadastro do serviço.

Ao inserir uma nota fiscal com item de serviço, caso o serviço tenha o campo Guia de Recolhimento preenchido e esta guia tenha o campo Documento de Arrecadação preenchido, será mostrado automaticamente no campo Código Tributação da nota fiscal o valor do campo Documento de Arrecadação.

**Valor Serviço**

Para integração Varejo Senior: Este campo preenche o campo Preço
Unitário da tela F118PSI.

% Diferimento   
Percentual que será utilizado para o cálculo do valor do ICMS Diferido em cotações, contratos, ordens de compras, pedidos, pré-faturas e notas fiscais de entrada e saída.

% PIS Recuperar

Percentual do PIS a recuperar. O valor deste campo será sugerido apenas quando o parâmetro Usa Produto X Fornecedor, no cadastro de produto (F075PRO), estiver ativo.

% COFINS Recuperar

Percentual do COFINS a recuperar. O valor deste campo será sugerido apenas quando o parâmetro Usa Produto X Fornecedor, no cadastro de produto (F075PRO), estiver ativo.

Transação NF Ent. Serviço

Possibilita definir a transação de serviço que deve ser ligada ao fornecedor para ser considerada pelas notas fiscais de entrada no recebimento eletrônico.

Código Dispositivo Fiscal

O dispositivo fiscal informado neste campo será gerado como sugestão nas Notas Fiscais de Entrada (F660NFC e F440GNE), caso o documento seja emitido para o Fornecedor e Serviço conforme a parametrização desta tela.

Transação de recebimento para serviço

Possibilita listar as transações em que a Operação de Compra for do tipo **R - Recebimento**, na guia Dados Gerais da tela Transações de Compras (F001TCP), e a transação de serviço for do módulo **COS - Compras - NF Entrada Serviços**.

Transação de pagamento para serviço

Possibilita listar as transações em que a Operação de Compra for do tipo **P - Pagamento**, na guia Dados Gerais da tela Transações de Compras (F001TCP), e a transação de serviço for do módulo **COS - Compras - NF Entrada Serviços**.

% INSS Empresa

Indica o percentual de INSS da empresa.

Código Serviço no Fornecedor

Indica qual o código do serviço no fornecedor, e assim, no recebimento eletrônico de uma nota fiscal de remessa para industrialização, caso este código conste no arquivo XML, o ERP utiliza o serviço da ligação com o fornecedor.

Este campo é exclusivo para identificar o item de serviço nas notas de retorno de industrialização através do recebimento eletrônico, e deve ser utilizado em conjunto do identificador de regras **CPR-000INESR01**.

**Percentual do Diferimento de ICMS relativo ao FCP**

Percentual do diferimento de ICMS relativo ao FCP sugerido para o cálculo do valor do diferimento de ICMS relativo ao FCP nos processos de compras e recebimento. Este campo não tem preenchimento obrigatório.

## Páginas relacionadas

* [Ajuda por telas](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/ajuda-telas.htm)
* [F118PSI](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_servicos/f118psi.htm)
* [F075PRO](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075pro.htm)
