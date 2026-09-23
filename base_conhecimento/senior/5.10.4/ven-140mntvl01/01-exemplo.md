# Exemplo:

> **Fonte:** Identificador de Regra — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_140mntvl01.htm  
> **Trilha:**   
> **Telas citadas:** —  
> **Identificadores de regras:** —

---
* Total de ICMS da nota Fiscal: 100,99
* Total de ICMS somado nos itens: 100,98

O funcionamento padrão nesta situação é efetuar o arredondamento do valor de ICMS nos itens com o intuito de igualar com o valor dos dados gerais. Caso o usuário não queira que o valor do ICMS seja alterado nos itens, este identificador deverá ser habilitado e a variável VSMntIcm deverá ser retornada como "N", indicando ao sistema que o arredondamento NÃO será feito.
