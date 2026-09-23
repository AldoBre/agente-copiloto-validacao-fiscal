# Serviços

> **Fonte:** F120GPD - Entrada de Pedidos Agrupado — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f120gpd.htm  
> **Trilha:** Ajuda por telas > Mercado > Gestão de Vendas > Pedidos  
> **Telas citadas:** E001TVE, E120PED, F000RPF, F019TIS, F081CTV, F120CAP, F120CAS, F120CIS  
> **Identificadores de regras:** —

---
Serviços

Lançamento dos serviços. A sugestão do % ISS para o serviço obedecerá a seguinte
sequência.

1. ISS da definição do
   Cliente/Fornecedor
2. ISS da ligação Serviço x CEP
3. ISS do CEP do Cliente/Fornecedor
4. ISS das definições do Serviço

Observação

O sistema usa o CEP da filial da nota fiscal/pedido/ordem de
compra/etc. para carregar o valor de ISS definido na ligação.

Ped. Ref

Consultar pedido referente ao serviço.

**Percentual de diferimento ICMS FCP**

Percentual do diferimento de ICMS relativo ao FCP sugerido e calculado com base nas parametrizações do ERP. Na grade de produtos, este campo não é exibido, mas com base nas parametrizações da tela de Fundo de Combate à Pobreza, o valor do diferimento de ICMS para FCP pode ser calculado e pode ser visualizado no cálculo do item (F120CAP).

**Mot. deson ICMS-ST**

Motivo da desoneração do ICMS-ST na grade de produtos e de serviços para calcular o valor do ICMS-ST desonerado. Sugerido a partir das parametrizações definidas na tela F019TIS.

Documento Integrado

Mostra o número do documento integrado recebido do sistema terceiro (E120PED.NUMINT).

Vlr. CBS Ori.

Valor da CBS de origem.

Vlr. IBS Est. Ori.

Valor do IBS Estadual de origem.

Vlr. IBS Mun. Ori.

Valor do IBS Municipal de origem.

Vlr. Ded. IBS/CBS

Valor de dedução/redução da base de cálculo do IBS/CBS.

Vlr. Reemb.

Valor de reembolso.

**Nota**

Os valores informados nos campos Vlr. CBS Ori, Vlr. IBS Est. Ori. e Vlr. IBS Mun. Ori. são utilizados no processo de estorno de crédito do IBS/CBS, quando a transação de emissão de nota de serviço estiver configurada como Estorno de Crédito da CBS/IBS (E001TVE.ESTCRE = "S").

#### Botões

Cálculos

Acesso à tela F120CAS, para exibição dos cálculos efetuados.

Alt.Rateios

Acesso à tela F000RPF, para
exibição da tela de alteração de rateios, desde que o
rateio seja a nível de itens.

Personalizados

Acesso à tela F120CIS, para campos personalizados
de usuário.

Tab.Preço

Acesso à tela F081CTV, para a
consulta da tabela de prelos de venda.

Os botões acima sempre exibirão registros ou aplicarão seus tratamentos ao
item posicionado na grade.

## Páginas relacionadas

* [Fundo de Combate à Pobreza](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/manuais_processos/mercado/nf-e/fcp.htm)
* [F019TIS](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f019tis.htm)
* [F120CAS](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f120cas.htm)
* [F000RPF](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/f000rpf.htm)
* [F120CIS](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f120cis.htm)
* [F081CTV](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f081ctv.htm)
