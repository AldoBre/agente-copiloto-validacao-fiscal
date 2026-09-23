# Botões

> **Fonte:** F075GFP - Cadastro de Produtos — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075gfp.htm  
> **Trilha:** Ajuda por telas > Cadastros > Produtos e Serviços > Produtos  
> **Telas citadas:** F000CMV, F055PPF, F075CPF, F075CPR, F075CRF, F075EAN, F075IMP, F075LPF, F075MAE, F075OPC, F204PXN, F700CMC, F710CRP  
> **Identificadores de regras:** —

---
Opções

Exibe a tela Opções do cadastro de Produto agrupado (F075OPC). Verifique a documentação para mais informações sobre as opções e configurações disponíveis na tela.

EAN 13

Exibe a tela F075EAN. o botão somente estará ativo se a família tiver o valor N no campo
Gerar EAN13 automático.

Característica

Mostra todas as características cadastradas na família do produto. Para isso
é necessário que na família o campo Tem Característica esteja como S (Sim) e
na página Característica tenha alguma característica inclusa.

Para fazer a ligação desta ao produto é necessário que no campo Seq. seja
relacionado o componente que deseja ligar a esse produto. Ao excluir uma
característica, apenas irá eliminar a mesma do banco (F075CPR), pois nesta tela
sempre aparecerá todas as características que estão cadastradas na família. Ao
estar posicionado sobre uma característica e o botão Excluir não habilitar,
significa que ela não está ligada ao produto.

O campo Descrição Livre somente poderá ser alterado se as características não
tiverem componentes.
Não será permitido cadastrar características com componentes sem informar a
sequência deste.

Con. Fotos

Este botão será habilitado sempre que o cursor estiver posicionado na
grade
Produtos ou quando estiver posicionado sobre uma derivação marcada na grade
Derivações.
Se o cursor estiver no produto, ao clicar neste botão a tela
F075CPF será
chamada e serão exibidas as fotos de todas as derivações do produto em questão.
Se o cursor estiver na derivação, serão exibidas somente as fotos da derivação
posicionada.

Prod. X Foto

Ao clicar nesse botão abrirá a tela F075LPF que permite fazer a ligação da foto ao produto.

Observação

Se o cursor estiver posicionado na
grade dos produtos, a tela
será aberta com o campo Produto preenchido e
automaticamente serão listadas as fotos já cadastradas para todas as derivações
deste produto. Se o cursor estiver posicionado na grade
Derivações Possíveis, a tela será aberta com os campos Produto e Derivação
preenchidos automaticamente e serão listadas as fotos
já cadastradas para este produto/derivação.

Inf. Manus

Ao clicar nesse botão abrirá a tela F075MAE para
inserir informações de manuseio.

Múlt. Vol.(L)

Exibe a tela F000CMV para a conferência e consulta dos códigos de barras
para produtos com múltiplos volumes.

Modelo

Ao clicar neste botão, será aberta a tela
F700CMC.

* Se o usuário estiver posicionado sobre um produto que possuir modelo cadastrado,
  este será carregado automaticamente na tela;
* Se o produto não possuir modelo, a tela será aberta em modo de inserção,
  sugerindo a família, o código e a descrição do produto para o modelo.

Observação

Este botão somente ficará habilitado para produtos que
pertençam a família do tipo "P - Produzido" ou "M - Montagem".

Inf. Técnicas

Ao clicar neste botão, é aberta a tela de Características do produto no fabricante (F075CRF).

**Roteiro**

Este botão é desabilitado quando o foco do cursor estiver na linha do produto e o campo **Liga Rot.Prod** estiver = "N", porém quando o foco do cursor estiver na linha da derivação o botão é habilitado. Quando o campo **Liga Rot.Prod** estiver igual a "S - Sim" é o inverso, botão é habilitado na linha do produto e desabilitado na linha da derivação. Quando o roteiro ainda não estiver cadastrado no produto ou na derivação, ao acessar o botão a tela de Roteiro (Fluxo do processo) (F710CRP) será aberta com o nome do roteiro igual ao código do produto.

**Prod. X Imp.**   
A partir desse botão é aberta a tela Impostos por Produto (F075IMP). Os impostos só estarão disponíveis na tela se forem do tipo 76 - Agronegócio e estiverem cadastrados na tela F055PPF.

Lig. Prod. x Cur.

Acesso a tela de Ligação de Produto x Níveis de Curvas de Estoque (F204PXN).

## Páginas relacionadas

* [F075OPC](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075opc.htm)
* [F075CPF](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075cpf.htm)
* [F075LPF](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075lpf.htm)
* [F075MAE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075mae.htm)
* [F700CMC](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_manufatura/f700cmc.htm)
* [Características do produto no fabricante (F075CRF)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075crf.htm)
* [Impostos por Produto (F075IMP)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075imp.htm)
* [F055PPF](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f055ppf.htm)
* [F204PXN](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f204pxn.htm)
