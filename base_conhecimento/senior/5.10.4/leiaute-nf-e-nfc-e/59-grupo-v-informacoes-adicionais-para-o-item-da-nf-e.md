# Grupo V - Informações adicionais (para o item da NF-e)

> **Fonte:** Leiautes NF-e e NFC-e — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/leiaute-nf-e-nfc-e.htm  
> **Trilha:** Segmentos > Compliance > Documentos Eletrônicos > NF-e | NFC-e (Nota Fiscal Eletrônica) > Nota Fiscal Eletrônica 4.0  
> **Telas citadas:** E024MSG, E140IPM, E140IPV, F024MSG  
> **Identificadores de regras:** VEN-140NEITE01

---
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação | Origem |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 325 | V01 | infAdProd | Informações Adicionais do produto | E | H01 | C | 0-1 | 1-500 | Norma referenciada, informações complementares, etc | O sistema busca no item da nota fiscal as informações das mensagens vinculadas neste (Tabela Vendas - Notas Fiscais de Saída - Itens de Produto - Mensagens (E140IPM), campo Texto da Mensagem do Item de Produto da Nota Fiscal de Saída (MSGIPM). Podem existir até 4 mensagens cadastradas no item. Para a mensagem encontrada será retornado o conteúdo dessa mensagem, proveniente da tabela de mensagens (E024MSG), desde que o campo Mensagem Fiscal da tela Mensagens da Nota fiscal (F024MSG) seja igual a “S - Simˮ e o campo Interesse Mens. da mesma tela seja igual a “P - Produto Inf. Adic". Caso houver mais de uma mensagem no item da nota, o sistema trará apenas a primeira encontrada. O sistema concatena o resultado obtido pela busca efetuada no parágrafo anterior com a observação descrita no item do produto (Tabela Vendas - Notas fiscais de saída - Itens de Produtos (E140IPV), campo ObsIpv).Também é possível alterar o resultado desse campo através da variável VSIntInfAdp do identificador de regra VEN-140NEITE01. |

## Páginas relacionadas

* [F024MSG](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f024msg.htm)
* [VEN-140NEITE01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_140neite01.htm)
