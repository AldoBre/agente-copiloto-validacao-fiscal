# Sobre as mensagens fiscais

> **Fonte:** F140GNF - Notas Fiscais de Saída — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f140gnf.htm  
> **Trilha:** Ajuda por telas > Mercado > Gestão de Faturamento e Outras Saídas > Notas Fiscais de Saída  
> **Telas citadas:** F001TVE, F027BNF  
> **Identificadores de regras:** VEN-140MSGDZ01

---
As mensagens fiscais dos itens de produtos e serviços são carregadas considerando primeiramente as mensagens vinculadas na Ligação de Situação Tributária x Dispositivo Fiscal (F027BNF), e é possível configurar até quatro mensagens fiscais.

Ao informar um item na grade de Produtos ou Serviços, é realizada a sugestão dos dispositivos fiscais para o item, que pode ser visualizada por meio do botão Dispos. Fiscais localizado no rodapé destas grades.

Caso a ligação da situação tributária com o dispositivo fiscal sugerido para o item não possua todas as quatro mensagens fiscais configuradas, o restante das mensagens fiscais são preenchidas com as mensagens fiscais configuradas no cadastro da Transação (F001TVE).

Quando, no entanto, não há dispositivos fiscais informados na ligação, mas há mensagens fiscais, o sistema sugere as mensagens fiscais e gera o beneficio de acordo com o campo Gera sem Beneficio. Para inativar essa funcionalidade pode-se ativar o Identificador de Regras VEN-140MSGDZ01.

## Exemplo:

Na Ligação de Situação Tributária x Dispositivo Fiscal temos cadastradas as seguintes mensagens fiscais.

| Campo | Código da Mensagem |
| --- | --- |
| CodMs1 | 1 |
| CodMs2 | 2 |
| CodMs3 | 0 |
| CodMs4 | 0 |

E na Transação do item de produto ou serviço temos as seguintes mensagens fiscais configuradas:

| Campo | Código da Mensagem |
| --- | --- |
| CodMs1 | 7 |
| CodMs2 | 5 |
| CodMs3 | 3 |
| CodMs4 | 0 |

Neste caso as mensagens fiscais vinculadas ao item de produto ou serviço seriam as seguintes:

| Campo | Código da Mensagem |
| --- | --- |
| CodMs1 | 1 |
| CodMs2 | 2 |
| CodMs3 | 7 |
| CodMs4 | 5 |

Considerando que o sistema carrega primeiramente as mensagens do benefício fiscal, como os campos de mensagens CodMs3 e CodMs4 não estão configurados, são carregadas as mensagens fiscais que estão vinculadas à transação do item.

## Páginas relacionadas

* [F027BNF](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f027bnf.htm)
* [F001TVE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f001tve.htm)
* [VEN-140MSGDZ01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_140msgdz01.htm)
