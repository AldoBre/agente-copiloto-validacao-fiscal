# Campos

> **Fonte:** F075GFP - Cadastro de Produtos — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075gfp.htm  
> **Trilha:** Ajuda por telas > Cadastros > Produtos e Serviços > Produtos  
> **Telas citadas:** F084MPR  
> **Identificadores de regras:** —

---
Produto 

Informação de código do produto - campo de preenchimento obrigatório, caso não seja preenchido, será emitida uma mensagem de alerta informando a obrigação do preenchimento.

Observação

Caso a Família que está sendo usada possuir uma ou mais máscaras de Produto e estas possuírem o campo Tipo Componente igual a numérico e o campo Valor Incremental for maior que 0 (F084MPR), ao sair do campo Produto sem preencher alguma informação, é gerado um código único automaticamente.

Sit. Produto

Situação do produto. Quando estiver em branco,
exibe todos os produtos cadastrados.

Derivação

Tem como objetivo facilitar a seleção de produtos que tem a mesma
derivação. Quando este campo estiver preenchido, a grade Derivações
Possíveis irá mostrar apenas as derivações informadas, podendo ser
informada mais de uma derivação. Permite informar apenas as derivações
que fazem parte da máscara de derivação que consta na família.

Sit. Derivação

Se este campo
estiver com a  situação como Inativo, ao ser
feita uma consulta, o sistema irá apresentar como retorno, todo produto
que tenha ao menos uma derivação inativa, exemplo: se a família possuir
uma derivação inativa, e for consultado os produtos da família com a
situação da derivação como inativa, todos os produtos da família devem
ser retornados.  

Se, ainda como exemplo, um produto possuir uma ou todas
as derivações como inativas, mesmo que a família não tenha derivações
inativadas, o produto também deverá ser retornado nesta seleção acima
citada.

Apenas o produto informado

Se este campo estiver marcado, ao ser realizada uma consulta, será utilizado o código informado no campo
Produto, e caso este campo esteja desmarcado, serão utilizados os códigos de produto que forem maiores ou iguais ao código informado.

Exemplo: se for informado o código 10010 e o código 15375 também estiver na família/origem, ele será utilizado, pois é maior que o informado (10010).

Código do Item NFCom

Campo para preenchimento da classificação do item para NFCom, conforme as opções disponíveis no Portal da Nota Fiscal Fatura de Serviço de Comunicação Eletrônica - SVRS

Proc. Suframa

Número do processo na Suframa para CBS zero.

## Páginas relacionadas

* [Portal da Nota Fiscal Fatura de Serviço de Comunicação Eletrônica - SVRS](https://dfe-portal.svrs.rs.gov.br/NFCOM/tabelacclass)
