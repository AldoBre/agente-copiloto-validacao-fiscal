# Via Cupom Fiscal (ECF, NFC-e, CF-e)

> **Fonte:** F140PRE - Preparação da Nota Fiscal de Saída — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f140pre.htm  
> **Trilha:** Ajuda por telas > Mercado > Gestão de Faturamento e Outras Saídas > Notas Fiscais de Saída  
> **Telas citadas:** F001TVE, F027STR  
> **Identificadores de regras:** —

---
**Sobre o código da situação tributária ICMS de produto:**

* A sugestão da situação tributária é feita com base no documento a partir do qual a nota é criada.
* Se a transação do item de produto for a mesma do item de produto da nota de origem ou quando o cupom original não tributou então herda as situações tributárias.
* Se não enquadrar no item acima, apesar de sugerida pode ser sobreescrita conforme documentação da tela Situações Tributárias (F027STR)
* Caso o usuário altere a situação tributária, esta alteração irá prevalecer sobre todas as situações acima citadas.

Ao selecionar esta opção, os campos para filtro de cupom/nota são exibidos. Ao selecionar uma série os campos Cód.Equipamento e Cupom Fiscal são habilitados conforme o Dispositivo de Autorização da série. Se o dispositivo for **5 - ECF** os campos são habilitados, caso contrário (10 ou 11) os campos ficam desabilitados.

Na geração de notas fiscais de saída de retorno(tipo 5) ou devolução(tipo 2) ao informar um pedido que gerou uma nota fiscal de entrada, através do parâmetro: Gerar NF de Entrada ao Fechar Pedido (F001TVE), será exibida a nota ligada ao pedido e carregados os dados da nota fiscal de entrada ligada.

## Páginas relacionadas

* [F027STR](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f027str.htm#menu_cadastros/F027STR.htm)
