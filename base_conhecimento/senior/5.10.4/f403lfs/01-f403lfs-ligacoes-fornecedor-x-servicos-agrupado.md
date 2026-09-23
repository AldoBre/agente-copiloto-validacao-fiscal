# F403LFS - Ligações Fornecedor X Serviços Agrupado

> **Fonte:** F403LFS - Ligações Fornecedor X Serviços Agrupado — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f403lfs.htm  
> **Trilha:** Ajuda por telas > Cadastros > Clientes e Fornecedores > Fornecedores > Ligações > Fornecedor X Serviços  
> **Telas citadas:** F001TCP, F075PRO, F118PSI, F403LFS  
> **Identificadores de regras:** CPR-000INESR01, GER-000HFOAU01

---
Ajuda por telas > Cadastros > Clientes e Fornecedores > Fornecedores > Ligações > Fornecedor X Serviços > Agrupado

Tela destinada às ligações entre fornecedores e serviços de forma agrupada.

**Observação**

Se o identificador de regras GER-000HFOAU01 estiver ativo e a variável GerARetorno definida como "S - Sim", a geração das definições/histórico do fornecedor será feita de forma automática, sem necessidade de intervenção do usuário. Caso não esteja parametrizado dessa forma, o cadastro continua sendo feito de forma manual.

## Campos

Grupo Empresas

Código do grupo de empresas.

Família

Código da família.

Serviço

Código do serviço.

Fornecedor

Código do fornecedor.

Opção

Definição da opção da operação.

Ordenar

Definição da ordenação aplicada a *grid*.

Complemento

Descrição complementar do registro posicionado na *grid*.

GRID Fornecedores X Serviços

Grid para exibição dos registros que atendem aos filtros informados.

Valor Serviço

 Para integração Varejo Senior: Este campo preenche o campo Preço
Unitário da tela F118PSI.

% Diferimento   
Percentual que será utilizado para o cálculo do valor do ICMS Diferido em cotações, contratos, ordens de compras, pedidos, pré-faturas e notas fiscais de entrada e saída.

% PIS Recuperar

Percentual do PIS a recuperar. O valor deste campo será sugerido apenas quando o parâmetro Usa Produto X Fornecedor, no cadastro de produto (F075PRO), estiver ativo.

% COFINS Recuperar

Percentual do COFINS a recuperar. O valor deste campo será sugerido apenas quando o parâmetro Usa Produto X Fornecedor, no cadastro de produto (F075PRO), estiver ativo.

T. NFE Serviço

Possibilita definir a transação de serviço que deve ser ligada ao fornecedor para ser considerada pelas notas fiscais de entrada no recebimento eletrônico.

Transação de recebimento para serviço

Possibilita listar as transações em que a Operação de Compra for do tipo **R - Recebimento**, na guia Dados Gerais da tela Transações de Compras (F001TCP), e a transação de serviço for do módulo **COS - Compras - NF Entrada Serviços**.

Transação de pagamento para serviço

Possibilita listar as transações em que a Operação de Compra for do tipo **P - Pagamento**, na guia Dados Gerais da tela Transações de Compras (F001TCP), e a transação de serviço for do módulo **COS - Compras - NF Entrada Serviços**.

Código Serviço no Fornecedor

Indica qual o código do serviço no fornecedor, e assim, no recebimento eletrônico de uma nota fiscal de remessa para industrialização, caso este código conste no arquivo XML, o ERP utiliza o serviço da ligação com o fornecedor.

Este campo é exclusivo para identificar o item de serviço nas notas de retorno de industrialização através do recebimento eletrônico, e deve ser utilizado em conjunto do identificador de regras **CPR-000INESR01**.

**Per. do Dif. de ICMS FCP**

Percentual do diferimento de ICMS relativo ao FCP sugerido para o cálculo do valor do diferimento de ICMS relativo ao FCP nos processos de compras e recebimento. Este campo não tem preenchimento obrigatório.

## Identificadores de regra

| Módulo | Código |
| --- | --- |
| GER | 000HFOAU01 |

## Páginas relacionadas

* [Ajuda por telas](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/ajuda-telas.htm)
* [GER-000HFOAU01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ger_000hfoau01.htm)
* [F118PSI](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_servicos/f118psi.htm)
* [F075PRO](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075pro.htm)
