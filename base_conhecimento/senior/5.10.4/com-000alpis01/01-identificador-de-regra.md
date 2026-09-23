# Identificador de Regra

> **Fonte:** Identificador de Regra — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/com_000alpis01.htm  
> **Trilha:**   
> **Telas citadas:** —  
> **Identificadores de regras:** COM-000ALPIS01

---
## COM-000ALPIS01

**Módulo:** COM - Comercial.

**Finalidade:** alterar o valor base e o valor do PIS a recuperar.

**Características:** chamado nos cálculos de nota fiscal de entrada, ordem de compra e notas fiscais de saída, podendo ser analisado na variável VSOrigem.

**Tela:** NFC, ordens de compra e NFV.

**Transação:** tem de estar ligado a uma transação

**Variáveis disponibilizadas:**

| Nome | Tipo | Observações | Retorna Valor |
| --- | --- | --- | --- |
| VSORIGEM | ALFA | Origem da chamada do identificador (NFE = Nota Fiscal de Entrada; NFS = Nota Fiscal de Saída; OCP = Ordem de Compra) | N |
| VSPROSER | ALFA | Indica se é produto (P) ou serviço (S) | N |
| VSCODEMP | NÚMERO | Código da empresa | N |
| VSCODSNF | ALFA | Série | N |
| VSCODFIL | NÚMERO | Código da Filial | N |
| VSNUMERO | NÚMERO | Número da Nota Fiscal de Entrada ou Saída | N |
| VSSEQITE | NÚMERO | Sequência do item (produto ou serviço) | N |
| VSCODTNS | ALFA | Transação do item (pode ser de produto ou de serviço) | N |
| VSCODFOR | NÚMERO | Código do fornecedor quando a origem for NFE | N |
| VSCODCLI | NÚMERO | Código do cliente quando a origem for NFS | N |
| VSCODPRO | ALFA | Código do produto | N |
| VSCODDER | ALFA | Código da derivação | N |
| VSCODSER | ALFA | Código do serviço | N |
| VSCODFAM | ALFA | Código da família | N |
| VSCODCLF | ALFA | Código da classificação fiscal | N |
| VSVLRBRU | NÚMERO | Valor Bruto do item | N |
| VSVLRDSC | NÚMERO | Valor de desconto do item | N |
| VSVLRDS1 | NÚMERO | Valor de desconto 1 do item | N |
| VSVLRDS2 | NÚMERO | Valor de desconto 2 do item | N |
| VSVLRDS3 | NÚMERO | Valor de desconto 3 do item | N |
| VSVLRDS4 | NÚMERO | Valor de desconto 4 do item | N |
| VSVLRDS5 | NÚMERO | Valor de desconto 5 do item | N |
| VSVLRIPI | NÚMERO | Valor de IPI | N |
| VSVLRFRE | NÚMERO | Valor de Frete | N |
| VSVLRSEG | NÚMERO | Valor de Seguros | N |
| VSVLREMB | NÚMERO | Valor de Embalagens | N |
| VSVLRENC | NÚMERO | Valor de Encargos | N |
| VSVLROUT | NÚMERO | Valor de Outras despesas | N |
| VSVLRDAR | NÚMERO | Valor de Arredondamento | N |
| VSVLRFRD | NÚMERO | Valor de frete destacado | N |
| VSVLROUD | NÚMERO | Valor de outras despesas destacado | N |
| VSPERDS1 | NÚMERO | % de desconto 1 | N |
| VSPERDS2 | NÚMERO | % de desconto 2 | N |
| VSPERDS3 | NÚMERO | % de desconto 3 | N |
| VSPERDS4 | NÚMERO | % de desconto 4 | N |
| VSPEROF1 | NÚMERO | % de oferta 1 | N |
| VSPEROF2 | NÚMERO | % de oferta 2 | N |
| VSPerIcm | NÚMERO | Percentual de ICMS | N |
| VSVlrBic | NÚMERO | Valor base do ICMS | N |
| VSVlrIcm | NÚMERO | Valor do ICMS | N |
| VSPerIpi | NÚMERO | Percentual de IPI | N |
| VSVlrBip | NÚMERO | Valor base do IPI | N |
| VSVlrBid | NÚMERO | Valor base IPI presumido | N |
| VSVlrIpd | NÚMERO | Valor do IPI presumido | N |
| VSPerIrf | NÚMERO | Percentual de IRRF | N |
| VSPerFun | NÚMERO | Percentual de FUNRURAL | N |
| VSPerSen | NÚMERO | Percentual do Senar | N |
| VSVlrBsi | NÚMERO | Valor base ICMS SUbstituído | N |
| VSVlrIcs | NÚMERO | Valor ICMS SUbstituído | N |
| VSVlrBsd | NÚMERO | Valor base ICMS substituto destacado | N |
| VSVlrIsd | NÚMERO | Valor ICMS substituto destacado | N |
| VSVlrBsp | NÚMERO | Valor base subsituição do PIS | N |
| VSVlrStp | NÚMERO | Valor subsituição do PIS | N |
| VSVlrBsc | NÚMERO | Valor base subsituição do COFINS | N |
| VSVlrStc | NÚMERO | Valor subsituição do COFINS | N |
| VSVlrDzf | NÚMERO | Valor de desconto zona franca | N |
| VSPerCrt | NÚMERO | Percentual de COFINS retido | N |
| VSPerPit | NÚMERO | Percentual de PIS retido | N |
| VSPerCsl | NÚMERO | Percentual de CSLL retido | N |
| VSPerOur | NÚMERO | Percentual de outras retenções | N |
| VSPerIss | NÚMERO | Percentual de ISS | N |
| VSPerIns | NÚMERO | Percentual de INSS | N |
| VSPerIim | NÚMERO | Percentual de imposto de importação | N |
| VSCodTic | ALFA | Código do ICMS especial | N |
| VSCodTrd | ALFA | Código de redução do ICMS | N |
| VSCodTst | ALFA | Código do ICMS substituído | N |
| VSCodStc | ALFA | Código de substiuição do COFINS | N |
| VSCodStp | ALFA | Código de substituição do PIS | N |
| VSPerPis | NÚMERO | Percentual de PIS a recuperar | N |
| VSDatEmi | DATA | Data de Emissão da Nota Fiscal de Entrada | N |
| VSDatEnt | DATA | Data de Entrada da Nota Fiscal de Entrada | N |
| VSQTDITE | NÚMERO | Quantidade do Item (Qtdade..Aberta quando VSOrigem = "PED" ou "OCP", Qtdade..Recebida quando VSOrigem = "NFE" e Qtdade..Faturada quando VSOrigem = "NFS") | N |
| VSCODDEP | ALFA | Código do depósito | N |
| VSNumPed | NÚMERO | Número do pedido | N |
| VSFilPed | NÚMERO | Código da filial | N |
| VSSeqIpd | NÚMERO | Sequência do item de produto do pedido | N |
| VSSeqIsp | NÚMERO | Sequência do item de serviço do pedido | N |
| VSVLRBPI | NÚMERO | Valor base do PIS a recuperar | S |
| VSVLRPIS | NÚMERO | Valor do PIS a recuperar | S |
| CprNAliPis | NÚMERO | Alíquota Valor PIS Recuperar | S |
| CprNPerPir | NÚMERO | Percentual de PIS a recuperar | S |
| VSRedIss | NÚMERO | Alterar valor base e valor do PIS a recuperar. | N |
| CprNBasIef | NÚMERO | Valor base ICMS entrega futura | N |
| CprNPerIef | NÚMERO | Percentual ICMS entrega futura | N |
| CprNVlrIef | NÚMERO | Valor ICMS entrega futura | N |
| ComNVlrFcp | NÚMERO | Valor FCP | N |
| ComNIcmVfc | NÚMERO | Valor FCP Difal | N |
| ComNIcmVde | NÚMERO | Valor ICMS Partilha Destino | N |
| ComNVecIcm | NÚMERO | Valor do ICMS Creditado Efetivamente | N |
| ComNBecIcm | NÚMERO | Valor da base ICMS Creditado Efetivamente | N |
| ComNPecIcm | NÚMERO | Percentual do ICMS Creditado Efetivamente | N |
| ComNVmoIcm | NÚMERO | Soma dos valores do ICMS Monofásico | N |
| ComNVmoIcr | NÚMERO | Soma dos valores do ICMS Monofásico Retido | N |
| ComNVmoIcf | NÚMERO | Soma dos valores do ICMS Monofásico Diferido | N |
| ComNVmoIcd | NÚMERO | Soma dos valores do ICMS Monofásico Destacado | N |

Atenção

Caso o parâmetro global LisVarReg esteja habilitado, a variável ListaVariaveis estará disponível em todos os identificadores de regras do sistema. O conteúdo desta variável lista os campos disponibilizados no identificador de regras em questão.

Não é aconselhada a ativação desse parâmetro global para o uso cotidiano. Esse recurso de listagem dos campos de identificadores auxilia a construção de regras e o Suporte para, por exemplo, depuração ou quando não houver acesso à documentação dos identificadores de regras.

## Páginas relacionadas

* [LisVarReg](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#LisVarReg)
