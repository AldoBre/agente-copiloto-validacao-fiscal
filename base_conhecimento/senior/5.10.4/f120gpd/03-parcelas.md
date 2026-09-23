# Parcelas

> **Fonte:** F120GPD - Entrada de Pedidos Agrupado — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f120gpd.htm  
> **Trilha:** Ajuda por telas > Mercado > Gestão de Vendas > Pedidos  
> **Telas citadas:** F028GCP, F081TCA, F085HCL, F099UVE  
> **Identificadores de regras:** GER-120PEDAP01

---
Parcelas

Lançamento das parcelas quando o pedido tem parcelas especiais.

% Desc. Antecipação

Percentual do desconto de antecipação.

% Desc. Pontualidade

Percentual do desconto de pontualidade. É de uso exclusivo do Agronegócio.

Observação

Os
percentuais dos descontos serão preenchidos no momento da geração das
parcelas. A regra para a busca dos percentuais dos descontos é:

1. F081TCA
2. F028GCP (Guia Itens)
3. F028GCP
4. F085HCL

O identificador de regras GER-120PEDAP01, porém,
fica à frente da sequência descrita acima. Caso tenha uma regra cadastrada, no
momento de geração das parcelas serão sugeridos os percentuais dos
descontos de antecipação e pontualidade informados na regra. Esses
percentuais também poderão ser informados manualmente, desde
que isso esteja parametrizado na tela F099UVE.

Operadora

Nome da operadora financeira. O campo será habilitado somente quando o tipo de pagamento atrelado à forma de pagamento for igual a "2, 3, 4, 6, 7, 8, 12, 14, 15, 16, 17, 18, 19, 20, 22, 23, 24, 25, 27, 28, 29, 30 ou 31".

Autorização da Transação (TEF) 

Número de autorização da transação da operação cartão de crédito e/ou débito

Bandeira

Nome da bandeira do cartão de crédito e/ou débito.

#### Botões

Ficha Emerg.

Este botão abre o modelo de relatório de emissão da Ficha de Emergência do produto, assim, é possível imprimi-lá. Ele está disponível apenas para o Receituário Agronômico.

## Páginas relacionadas

* [F081TCA](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f081tca.htm)
* [F028GCP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f028gcp.htm)
* [F085HCL](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f085hcl.htm)
* [GER-120PEDAP01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ger_120pedap01.htm)
* [F099UVE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f099uve.htm)
* [modelo de relatório](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/relatorios/receituario/ger001.htm)
* [Ficha de Emergência](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/manuais_processos/receituario_agronomico/processos/ficha_emergencia.htm)
