# Cadastro de PDV (F070PDV)

> **Fonte:** F000PPD -  Configuração de parâmetros dinâmicos — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000ppd.htm  
> **Trilha:** Ajuda por telas > Cadastros  
> **Telas citadas:** F070PDV  
> **Identificadores de regras:** —

---
#### LOGIN.CAIXAABERTOPOROUTROUSUARIO

Contém a permissão para a tela de bloqueio do PDV, que é utilizada no momento que o parâmetro LOGIN.SOMENTEUSUARIOQUEABRIUCAIXA exibe a mensagem "Caixa aberto por outro usuário".

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não (valor **Padrão**) |
| 1 | Sim |

#### LOGIN.SOMENTEUSUARIOQUEABRIUCAIXA

Quando estiver definido com o valor 1 e o caixa estiver aberto, o sistema compara o usuário digitado com o usuário de abertura do caixa. Se for o mesmo usuário ou se o usuário digitado tem permissão, o sistema efetua o login. Caso não, exibe a mensagem "Caixa aberto por outro usuário", solicitando usuário com permissão. A validação é feita na tela de login e na tela de bloqueio do PDV.

| Valor (Lista) | Descrição |
| --- | --- |
| 0 | Não (valor **Padrão**) |
| 1 | Sim |

#### PDV.VALORFUNDOTROCO

Indica se o valor de fundo de troco, para o PDV, será pego pelo cadastro de parâmetros da Filial ou se o PDV possui um parâmetro individual de fundo de troco.

| Valor (Numérico) | Descrição |
| --- | --- |
| 0 | Indica que utiliza valor de fundo de troco da filial (valor **Padrão**) |
| Qualquer valor maior que zero | Indica que utiliza tal valor de fundo de troco individual para o PDV |

#### TEF.PDV

Número do PDV para a aplicação Auttar. Não é necessariamente o mesmo número do PDV (F070PDV).

Deve respeitar as configurações existentes no servidor Auttar (obter a informação com a Auttar, se necessário).

## Páginas relacionadas

* [F070PDV](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070pdv.htm)
* [Auttar](https://www.auttar.com.br/)
