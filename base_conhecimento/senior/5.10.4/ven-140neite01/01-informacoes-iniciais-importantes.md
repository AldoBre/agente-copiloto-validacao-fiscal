# Informações iniciais importantes

> **Fonte:** Identificador de Regra — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_140neite01.htm  
> **Trilha:**   
> **Telas citadas:** —  
> **Identificadores de regras:** VEN-140NEITE01

---
O identificador de Regras VEN-140NEITE01 possuem quatro variáveis para manipular o grupo "I05 - Pedido de Compra" do XML da NF-e (grupo composto das tags xPed e nItemPed);

As variáveis existem dessa forma para haver compatibilidade com dados que podem estar inseridos na base do Gestão Empresarial | ERP e os formatos diferentes das tags xPed e nItemPed no XML da NF-e;

Atualmente a tag xPed é do tipo "C - Caracter" e a tag nItemPed é do tipo "N - Número". Desta forma, se a tag xPed deva ser gerada como "C - Caracter" deve ser utilizada a variável VSIntPedCli (maiores informações sobre as variáveis devem ser verificadas abaixo);

Atualmente as tags possuem os seguintes tamanhos no leiaute da NF-e:

* xPed:  até quinze caracteres;
* nItemPed: até seis caracteres.

Se for retornado para as variáveis da regra correspondentes a geração de cada tag um número maior do que o previsto no leiaute, o valor retornado será desconsiderado.
