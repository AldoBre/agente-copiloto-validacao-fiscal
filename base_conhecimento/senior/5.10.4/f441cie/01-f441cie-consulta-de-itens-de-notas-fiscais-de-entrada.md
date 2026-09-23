# F441CIE - Consulta de Itens de Notas Fiscais de Entrada

> **Fonte:** F441CIE - Consulta de Itens de Notas Fiscais de Entrada — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f441cie.htm  
> **Trilha:** Ajuda por telas > Suprimentos > Gestão de Recebimento > Notas Fiscais de Entrada > Consultas  
> **Telas citadas:** F000CRT, F441CIE  
> **Identificadores de regras:** —

---
Ajuda por telas > Suprimentos > Gestão de Recebimento > Notas Fiscais de Entrada > Consultas > Itens

Esta tela permite a consulta dos itens das notas fiscais de entrada.

**Reforma Tributária – Consulta de Impostos**

Esta tela permite o acesso à Consulta de Impostos da Reforma Tributária (F000CRT), o qual pode ser feito das seguintes formas:

* Por meio do botão CBS e IBS, disponível nos botões de Cálculo para telas de Pedido, Ordem de Compra, Cotação e Nota Fiscal;
* Ou diretamente pelo botão CBS e IBS para as telas de consulta.

Para conferir todas as rotinas impactadas pela Reforma Tributária, acesse esta documentação.

## Campos

Selecionar  
Define quais registros serão filtrados para exibição na tela com as opções de:

* **Produtos**: filtra todos os produtos existentes, ignorando os serviços
* **Serviços**: filtra todos os serviços existentes, ignorando os produtos
* **Todos**: filtra todos os registros existentes, tanto de produto quanto de serviço

Princípio Ativo

Este campo tem dupla função, sendo a primeira filtro para seleção de produto e derivação e a segunda como filtro geral para filtro geral de dados com exclusividade no filtro tipo abrangência. Na grade, a coluna Princípio Ativo, mostra o valor cadastrado na derivação.

Produto   
Filtra pelo código do produto.

Deriv.   
Filtra pelo código da derivação.

Serviço   
Filtra pelo código do serviço.

Entrada   
Período da data de entrada da nota.

Emissão   
Período da data de emissão da nota.

Filial   
Código da filial.

Forn.   
Código do fornecedor.

Série   
Código da série.

N.F.

Consulta dos itens pelo número da nota fiscal.

Fabricante   
Código do fabricante.

Finalidade NF-e

Finalidade da nota fiscal.

* "1 - Normal"
* "5 - Nota de crédito"

Tipo nota crédito

Tipo da nota de crédito.

* "01 - Multa e Juros"

**Observação**

Sobre a fórmula de cálculo do Preço de Estoque e Preço Unitário, o sistema verifica as unidades de medida para realizar o cálculo.

* Se as Unidades de Medida forem iguais, o sistema só atribui o mesmo Preço Unitário do Item ao Preço de Estoque;
* Caso as Unidades de Medida estejam diferentes, o sistema realiza a seguinte equação atribuindo ( (PreUni \* QtdRec) / QtdEst );

## Grade Produtos

Exibe as informações dos itens de produtos da nota fiscal de entrada consultada.

Quantidade Recebida   
Quantidade recebida na unidade de medida do fornecedor.

Qtde.Dev.   
Quantidade devolvida do item da nota fiscal de entrada.

Quantidade Estoque   
Quantidade da entrada no estoque já na unidade de medida do produto.

Importante

Caso tenha ocorrido alguma devolução referente ao item da nota fiscal de entrada consultada, esta não influenciará nos valores mostrados dos campos de Quantidade Recebida e Quantidade Estoque, já que será listada a quantidade de entrada no estoque no item da nota fiscal e não a quantidade de estoque do produto.

Complemento

Este campo recebe a descrição da tag **<prod|xProd>** do .XML, sendo que o seu conteúdo será listado no registro C170 - Itens do documento do SPED ICMS/IPI.

Compl. (ERP)

O complemento é buscado do cadastro do produto/derivação, não é editável e será formado da seguinte maneira: Descrição do Produto + Descrição Complementar do Produto + Descrição da Derivação + Descrição Complementar da Derivação.  
Com a **ordem de compra informada**, o complemento será formado: Descrição do Produto + Descrição Complementar do Produto + Descrição da Derivação + Descrição Complementar da Derivação + Complemento da Ordem de Compra.

Qtde. Base ICMS Monofásico

Quantidade da Base de ICMS Monofásico.

Vlr. ICMS Monofásico

Valor do ICMS Monofásico dos Itens de Produto da Nota Fiscal de Saída.

Aliq. ICMS Monofásico

Alíquota ad rem de ICMS Monofásico

Qtde. Base ICMS Mono. Ret

Quantidade da Base de ICMS Monofásico Retido.

Vlr. ICMS Mono. Ret

Valor do ICMS Monofásico Retido dos Itens de Produto da Nota Fiscal de Saída.

Aliq. ICMS Mono. Ret

Alíquota ad rem de ICMS Monofásico Retido.

Qtde. Base ICMS Mono. Dif

Quantidade da Base de ICMS Monofásico Diferido.

Vlr. ICMS Mono. Dif

Valor do ICMS Monofásico Diferido dos Itens de Produto da Nota Fiscal de Saída.

Perc. ICMS Mono. Dif

Percentual de Diferimento do ICMS Monofásico.

Qtde. Base ICMS Mono. Des

Quantidade da Base de ICMS Monofásico Destacado.

Vlr. ICMS Mono. Des

Valor do ICMS Monofásico Destacado dos Itens de Produto da Nota Fiscal de Saída.

Alíq. ICMS Mono. Des

Alíquota ad rem de ICMS Monofásico Destacado.

Alíq. ICMS Mono. Ori

Alíquota ad rem de ICMS Monofásico Original.

## Grade Serviços

Exibe as informações dos itens de serviços da nota fiscal de entrada consultada.

Complemento

Este campo recebe a descrição da tag **<prod|xProd>** do .XML, sendo que o seu conteúdo será listado no registro C170 - Itens do documento do SPED ICMS/IPI.

Compl. (ERP)

O complemento é buscado do cadastro do serviço, não é editável e será formado da seguinte maneira: Descrição do Serviço + Descrição Complementar do Serviço.  
Com a **ordem de compra informada**, o complemento será formado: Descrição do Serviço + Descrição Complementar do Serviço + Complemento da Ordem de Compra.

## Parâmetros globais

| Nome | Descrição |
| PerDocBlo | Indica se as notas fiscais de entrada com transação bloqueada para algum usuário devem ser exibidas nas telas de consulta. |

## Identificadores de regras

| Módulo | Código |
| GER | 000SELEF01 |

## Páginas relacionadas

* [Ajuda por telas](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/ajuda-telas.htm)
* [Suprimentos](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/menu_suprimentos.htm)
* [Gestão de Recebimento](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/menu_suprimentos_gestao_recebimento.htm)
* [Notas Fiscais de Entrada](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/fluxos/fluxograma_recebimento_nfentrada.htm)
* [F000CRT](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000crt.htm)
* [documentação](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/reforma-tributaria/rotinas-impactadas.htm)
* [C170 - Itens do documento](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/sped/fiscal-icms-ipi/bloco-c.htm#C170)
* [PerDocBlo](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#PerDocBlo)
* [000SELEF01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ger_000selef01.htm)
