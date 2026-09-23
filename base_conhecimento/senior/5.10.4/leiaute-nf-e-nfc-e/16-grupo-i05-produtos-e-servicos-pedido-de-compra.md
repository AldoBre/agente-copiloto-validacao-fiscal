# Grupo I05 - Produtos e Serviços / Pedido de Compra

> **Fonte:** Leiautes NF-e e NFC-e — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/leiaute-nf-e-nfc-e.htm  
> **Trilha:** Segmentos > Compliance > Documentos Eletrônicos > NF-e | NFC-e (Nota Fiscal Eletrônica) > Nota Fiscal Eletrônica 4.0  
> **Telas citadas:** E120IPD  
> **Identificadores de regras:** VEN-140NEITE01

---
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação | Origem |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 128.40 | I60 | xPed | Número do Pedido de Compra | E | I01 | C | 0-1 | 1 - 15 | Informação de interesse do emissor para controle do B2B. (v2.0) | Ao carregar o pedido de venda na nota fiscal, as informações dos campos Pedido do Cliente e Seq. Ped. Cli geram as tags <xPed> e <nItemPed> de forma automática com os dados do pedido e item informados nos campos E120IPD.PedCli e E120IPD.SeqPcl.  Os dois campos precisam estar preenchidos para que seja gerado na tag <xPed>, o número do pedido do cliente. É necessário informar no item para que esse valor informado seja enviado para a tag <xPed>. Caso não seja informado o valor nos campos Pedido do Cliente e Seq. Ped. Cli, o Gestão Empresarial | ERP irá gerar tag <xPed> e <nItemPed> com o número do pedido e item do ERP.  Pode ser manipulado o valor dessa tag através das variáveis VSIntProPed (tag <xPed>) e VSIntProIpe (tag <nItemPed>) do identificador de regras VEN-140NEITE01. |
| 128.41 | I61 | nItemPed | Item do Pedido de Compra | E | I01 | N | 0-1 | 6 | Informação de interesse do emissor para controle do B2B. (v2.0) |
