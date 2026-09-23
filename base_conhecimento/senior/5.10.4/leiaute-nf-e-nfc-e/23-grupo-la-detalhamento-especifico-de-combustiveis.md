# Grupo LA - Detalhamento Específico de Combustíveis

> **Fonte:** Leiautes NF-e e NFC-e — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/leiaute-nf-e-nfc-e.htm#la  
> **Trilha:** Segmentos > Compliance > Documentos Eletrônicos > NF-e | NFC-e (Nota Fiscal Eletrônica) > Nota Fiscal Eletrônica 4.0  
> **Telas citadas:** F075PCB, F075PRO  
> **Identificadores de regras:** VEN-140NEITE01

---
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação | Origem |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 162a | LA01 | comb | Informações específicas para combustíveis líquidos e lubrificantes | CG | I90 |  | 1-1 |  | Informar apenas para operações com combustíveis líquidos e lubrificantes. | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 162b | LA02 | cProdANP | Código de produto da ANP | E | LA01 | N | 1-1 | 9 | Utilizar codificação de produtos do Sistema de Informações de Movimentação de Produtos - SIMP (http://www.anp.gov.br/simp/). (NT 2012/003) | Gera por padrão utilizando a variável VSIntProAnp do identificador de regra VEN-140NEITE01. |
| 162b1 | LA03 | descANP | Descrição do produto conforme ANP | E | LA01 | N | 1-1 | 2-95 | Utilizar a descrição de produtos do Sistema de Informações de Movimentação de Produtos - SIMP (http://www.anp.gov.br/simp/). (Incluído na NT2016/002) | Gera a informação que consta no campo E075Pro.DesAmp. |
| 162b2 | LA03a | pGLP | Percentual do GLP derivado do petróleo no produto GLP (cProdANP=210203001) | E | LA01 | N | 0-1 | 3v4 | Informar em número decimal o percentual do GLP derivado de petróleo no produto GLP. Valores de 0 a 100. (Incluído na NT2016.002) | Gera a informação que consta no campo E075Pro.PerGlp. |
| 162b3 | LA03b | pGNn | Percentual de Gás Natural Nacional - GLGNn para o produto GLP (cProdANP=210203001) | E | LA01 | N | 0-1 | 3v4 | Informar em número decimal o percentual do Gás Natural Nacional - GLGNn para o produto GLP. Valores de 0 a 100. (Incluído na NT2016.002) | Gera a informação que consta no campo E075Pro.PerGas. |
| 162b4 | LA03c | pGNi | Percentual de Gás Natural Importado - GLGNi para o produto GLP (cProdANP=210203001) | E | LA01 | N | 0-1 | 3v4 | Informar em número decimal o percentual do Gás Natural Importado - GLGNi para o produto GLP. Valores de 0 a 100. (Incluído na NT2016.002) | Gera a informação que consta no campo E075Pro.PerGni. |
| 162b5 | LA03d | vPart | Valor de partida (cProdANP=210203001) | E | LA01 | N | 0-1 | 13v2 | Deve ser informado neste campo o valor por quilograma sem ICMS. (Incluído na NT2016.002) | Gera a informação que consta no campo E075Pro.VlrPar. |
| 162c | LA04 | CODIF | Código de Autorização / registro do CODIF | E | LA01 | N | 0-1 | 1 - 21 | Informar apenas quando a UF utilizar o CODIF (Sistema de Controle do Diferimento do Imposto nas Operações com AEAC - Álcool Etílico Anidro Combustível). | Gera por padrão utilizando a variável VSIntProCif do identificador de regra VEN-140NEITE01. |
| 162d | LA05 | qTemp | Quantidade de combustível faturada à temperatura ambiente | E | LA01 | N | 0-1 | 12v4 | Informar quando a quantidade faturada informada no campo "prod/qCom" (id:I10) tiver sido ajustada para uma temperatura diferente da ambiente. | Gera por padrão utilizando a variável VSIntProTem do identificador de regra VEN-140NEITE01. |
| 162e | LA06 | UFCons | Sigla da UF de consumo | E | LA01 | C | 1-1 | 2 | Informar a UF de consumo. Informar "EX" para Exterior. | Gera a informação que consta no campo E085Ent.EstEnt. |
| 162f | LA07 | CIDE | Informações da CIDE | G | LA01 |  | 0-1 |  | Grupo de informações da CIDE | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 162g | LA08 | qBCProd | BC da CIDE | E | LA07 | N | 1-1 | 12v0-4 | Informar a BC da CIDE em quantidade | Gera a informação que consta no campo E140Ipv.QtdFat. |
| 162h | LA09 | vAliqProd | Valor da alíquota da CIDE | E | LA07 | N | 1-1 | 11v4 | Informar o valor da alíquota em reais da CIDE | Gera a informação que consta no campo E140Ipv.VlrCid. |
| 162i | LA10 | vCIDE | Valor da CIDE | E | LA07 | N | 1-1 | 13v2 | Informar o valor da CIDE | Gera a informação que consta no campo E140Ipv.TotCid. |
| 162j | LA11 | encerrante | Informações do grupo "encerrante" | G | LA01 |  | 0-1 |  | Informações do grupo "encerrante" disponibilizado por hardware específico acoplado à bomba de Combustível, definido no controle da venda do Posto Revendedor de Combustível. (Grupo incluído na NT 2015/002) | Este grupo e as tags abaixo não são gerados pelo ERP, pois trata-se de informações específicas referente à bomba de combustível do controle de venda do posto de combustível. |
| 162k | LA12 | nBico | Número de identificação do bico utilizado no abastecimento | E | LA11 | N | 1-1 | 1 - 3 | Informar o número do bico utilizado no abastecimento |  |
| 162l | LA13 | nBomba | Número de identificação da bomba ao qual o bico está interligado | E | LA11 | N | 0-1 | 1 - 3 | Caso exista, informar o número da bomba utilizada |  |
| 162m | LA14 | nTanque | Número de identificação do tanque ao qual o bico está interligado | E | LA11 | N | 1-1 | 1 - 3 | Informar o número do tanque utilizado |  |
| 162n | LA15 | vEnclni | Valor do Encerrante no início do abastecimento | E | LA11 | N | 1-1 | 12v3 | Informar o valor da leitura do contador (Encerrante) no início do abastecimento |  |
| 162o | LA16 | vEncFin | Valor do Encerrante no final do abastecimento | E | LA11 | N | 1-1 | 12v3 | Informar o valor da leitura do contador (Encerrante) no término do abastecimento |  |
| 162p | LA17 | pBio | Percentual do índice de mistura do Biodiesel (B100) no Óleo Diesel B instituído pelo órgão regulamentador | E | LA01 | N | 0-1 | 3v4 | Informar, em número decimal, o percentual do índice de mistura do Biodiesel para o produto Óleo Diesel B. Valores maiores que 0 e menores ou iguais a 100 | Gera a tag conforme o campo Índice de mistura do cadastro do produto (F075PRO) |
| 162q | LA18 | origComb | Grupo indicador da origem do combustível | G | LA01 |  | 0-30 |  | Obrigatoriedade de preenchimento do grupo conforme a Tabela de Combustíveis Sujeitos à Tributação Monofásica (publicada no Portal Nacional da NF-e, no grupo “Documentos”, opção “Diversos”) | Gerado conforme o padrão do leiaute da SEFAZ. Os dados emitidos nesse grupo devem ser parametrizados na tela de cadastro de origem de produtos do tipo combustível (F075PCB) |
| 162r | LA19 | indImport | Indicador de importação | E | LA18 | N | 1-1 | 1 | 0 = Nacional 1 = Importação | Gera a tag conforme o campo Ind. de Importação do cadastro de origem de produtos do tipo combustível (F075PCB) |
| 162s | LA20 | cUFOrig | Código da UF | E | LA18 | N | 1-1 | 2 | UF de origem do produtor ou do importador. Use a tabela do IBGE | Gera a tag conforme o campo Cód. UF Origem do cadastro de origem de produtos do tipo combustível (F075PCB) |
| 162t | LA21 | pOrig | Percentual originário para a UF | E | LA18 | N | 1-1 | 3v4 | Informar, em número decimal, o percentual originário da UF. Esse valor será obtido por meio dos Anexos de Combustíveis previstos em Ato Cotepe. Valores maiores que 0 e menores ou iguais a 100 | Gera a tag conforme o campo do Percentual originário para a UF do cadastro de origem de produtos do tipo combustível (F075PCB) |

## Páginas relacionadas

* [VEN-140NEITE01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_140neite01.htm)
* [F075PRO](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075pro.htm)
* [Diversos](https://www.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=/NJarYc9nus=)
* [F075PCB](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075pcb.htm)
