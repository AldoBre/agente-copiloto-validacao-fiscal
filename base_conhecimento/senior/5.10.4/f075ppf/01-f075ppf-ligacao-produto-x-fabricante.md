# F075PPF - Ligação Produto X Fabricante

> **Fonte:** F075PPF - Ligação Produto X Fabricante — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075ppf.htm  
> **Trilha:** Ajuda por telas > Cadastros > Produtos e Serviços > Ligações > Produto X Fabricante  
> **Telas citadas:** E076FAB, F075GFP, F075PFL, F075PPF, F075PRO, F410CEA, F420GOC  
> **Identificadores de regras:** —

---
Ajuda por telas > Cadastros > Produtos e Serviços > Ligações > Produto X Fabricante > Individual

Esta tela permite a ligação entre o Produto e o Fabricante através do **Código
Fabricante** e do **Cód. Prod. Fabricante**.

## Processo

* no item da nota fiscal
  de entrada, o usuário poderá identificar qual é o fabricante do produto em
  questão. Esta identificação tem o objetivo de rastrear quem são os fabricantes de
  determinados produtos que a empresa utiliza ou revende, sendo que não é necessariamente o próprio fornecedor;
* quando for informado o campo fabricante, este deverá estar
  cadastrado na tabela de fabricantes (E076FAB);
* o campo fornecedor indica que
  pode haver um código de produto no fabricante exclusivo, porém se o referido
  campo estiver definido, o código em questão será sugerido para todos os
  fornecedores;
* o parâmetro global UtiPpfCpr indicará se será possível visualizar e utilizar
  os código CODFAB e PROFAB como facilitadores nos documentos de compra
  gerados através das telas de cotação (F410CEA)
  e ordem de compra (F420GOC).

#### Venda de um produto kit separadamente

Para isso, o produto deve estar ligado a um fabricante na tela F075PPF. Em seguida, acesse a tela F075PFL, pesquise pelo kit e altere a coluna **Vender separado?**. Assim, a caixa de seleção **Vender separadamente** ficará marcada no cadastro do kit no Retaguarda (Gestão de Lojas).

## Campos

Produto  
Código do produto.

Derivação  
Código da derivação.

Código Fabricante 

Código do fabricante.

Fornecedor  
Código do fornecedor.

Código do Produto no Fabricante 

Código do produto no fabricante.

Descrição  
Descrição do produto.

Observação  
Observação da ligação.

Unidade Medida Fabricante 

Código de medida do produto no fabricante.

Classificação Fiscal 

Código da classificação fiscal do produto no fabricante.

Código Barras 

Código de barras do produto no fabricante.

Quantidade Múltipla 

Código múltipla do produto no fabricante, meramente informativo.

Motivo da Situação 

Código do motivo da situação da ligação.

Observação Motivo 

Observação do motivo da situação da ligação.

Situação da Ligação 

Indicativo da situação da ligação.

Data de término fabricação 

Indica a data de término da fabricação do produto pelo fabricante.

**Importante**

Esse campo fica disponível apenas quando a proprietária do Varejo Senior estiver sendo utilizada.

Prazo de Garantia 

Indica a quantidade de meses padrão para o prazo de garantia pelo fabricante.

Prazo de Troca

Indica a quantidade de meses padrão para o prazo de troca pelo fabricante.

Produção em Escala Relevante

Informe se o produto é produzido em escala relevante ou não.

Os produtos produzidos em escala não relevante cuja NCM esteja relacionada no Anexo XXVII do Convênio 52/2017 devem ser preenchidas com o valor **N - Produzido em Escala Não Relevante**.

Ao inserir uma nova ligação, o valor do campo Prod. Esc. Relevante será sugerido conforme cadastrado na guia Derivação da tela Cadastro de Produto Individual (F075PRO) ou na grade Derivações da tela Cadastro de Produto Agrupado (F075GFP).

Para mais informações, consulte a documentação do Indicador de Escala Relevante.

## Identificadores de regra

|  |  |
| --- | --- |
| Módulo | Código |
| CPR | 410CONIP01 |

## Páginas relacionadas

* [Ajuda por telas](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/ajuda-telas.htm)
* [F410CEA](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f410cea.htm)
* [F420GOC](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f420goc.htm)
* [F075PFL](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075pfl.htm)
* [F075PRO](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075pro.htm)
* [F075GFP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075gfp.htm)
* [Indicador de Escala Relevante](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/manuais_processos/mercado/nf-e/regras-e-sugestoes-valores.htm#indicador_de_escala_relevante)
* [410CONIP01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/cpr_410conip01.htm)
