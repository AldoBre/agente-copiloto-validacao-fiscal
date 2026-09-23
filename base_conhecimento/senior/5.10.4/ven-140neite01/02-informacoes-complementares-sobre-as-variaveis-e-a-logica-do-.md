# Informações complementares sobre as variáveis e a lógica do sistema para geração das tags através das variáveis

> **Fonte:** Identificador de Regra — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_140neite01.htm  
> **Trilha:**   
> **Telas citadas:** E120IPD  
> **Identificadores de regras:** —

---
## Sobre as variáveis VSIntPedCli e VSIntIpeCli

* São variáveis do tipo ALFA;
* O valor retornado para a variável VSIntPedCli será gerado na tag xPed;
* O valor retornado para a variável VSIntIpeCli será gerado na tag nItemPed;
* Se não for retornado valor para a variável VSIntPedCli, não serão geradas as duas tags (xPed e nItemPed);
* Se não for retornado valor para a variável VSIntIpeCli, mas for retornado valor para a variável VSIntPedCli, será gerada a tag xPed e não será gerada a tag nItemPed.

## Sobre as variáveis VSIntProPed e VSIntProIpe

* São variáveis do tipo NUMERO;
* O valor retornado para a variável VSIntProPed será gerado na tag xPed;
* O valor retornado para a variável VSIntProIpe será gerado na tag nItemPed;
* Se não for retornado valor para a variável VSIntProPed não serão geradas as duas tags (xPed e nItemPed);
* Se não for retornado valor para a variável VSIntProIpe, mas for retornado valor para a variável VSIntProPed será gerada a tag xPed e não será gerada a tag nItemPed.

## Sobre utilização das variáveis

* As variáveis devem ser utilizadas conforme o tipo. Sendo assim, ou utiliza-se as variáveis do tipo NUMERO ou utiliza-se as variáveis do tipo ALFA (não é possível definir o numero do pedido na variável VSIntProPed e definir a sequência do pedido na variável VSIntIpeCli, por exemplo, pois o sistema não gerará adequadamente as tags no XML);
* Dependendo de onde o dado é buscado para retornar para cada variável, poderá precisar usar funções para conversão do tipo de dado.

## Sobre a definição incorreta de valores para estas variáveis

Caso se retorne na regra um valor incorreto para uma dessas variáveis, o sistema poderá levar em consideração a lógica interna para geração das tags.

### Exemplo:

Se for retornado um número de pedido maior que quinze caracteres na variável e o sistema localizar o número do pedido do cliente digitado no campo E120IPD.PedCli, o sistema poderá respeitar esse número digitado, ao invés do número retornado na variável.
