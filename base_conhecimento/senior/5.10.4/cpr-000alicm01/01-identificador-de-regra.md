# Identificador de Regra

> **Fonte:** Identificador de Regra — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/cpr_000alicm01.htm  
> **Trilha:**   
> **Telas citadas:** —  
> **Identificadores de regras:** CPR-000ALICM01

---
## CPR-000ALICM01

**Módulo:** CPR - Compras.

**Finalidade:**Informar o percentual de ICMS, o valor de ICMS e o valor base de ICMS para cada item, através de uma regra e de acordo com as variáveis disponibilizadas.   

A regra não é chamada se o item não calcular o valor de ICMS, ou seja, caso exista algum parâmetro que faça com que o sistema não calcule ICMS, a regra também não será chamada.

Atenção!

Ao alterar apenas um dos campos, certifique-se de que os demais estejam condizentes com o valor alterado. Isso porque, em alguns casos, o sistema pode considerar os valores já calculados.

Por exemplo, se apenas a alíquota for alterada em uma regra e o valor do ICMS já não corresponde ao resultado da nova alíquota, algumas rotinas poderão considerar apenas o valor já calculado do ICMS que, neste caso, seria o valor incorreto em relação à nova alíquota. Dito isso, para um bom funcionamento do identificador de regras, é aconselhável sempre verificar se os campos estão corretamente relacionados.

**Características:** \* Quando em processos automáticos (SID, web service, importação), mesmo que o sistema esteja configurado corretamente para calcular o ICMS, e mesmo que o controle do SID ou Web service de recálculo esteja setado para "SIM - Recalcular", o sistema só fará o recálculo (consequentemente a chamada do identificador) se um dos 3 campos abaixo não estiverem informados.  
 - VlrBic: Valor base do ICMS.  
 - VlrIcm: Valor do ICMS do item da nota fiscal de entrada.  
 - PerIcm: Percentual do ICMS do item da nota fiscal de entrada.  

\* A partir da versão 5.5.2.3 foi disponibilizada a variável VSCODDEP referente ao código de depósito.  

\* A partir da versão 5.5.2.4 foi disponibilizada a variável VSUFSCIC referente a sigla do estado base para o cálculo do ICMS.  

\* A partir da versão 5.8.6.8 foi disponibilizada a variável CPRNSeqOrm referente a sequência de origem da mercadoria.  

\* A partir da versão 5.8.6.19 foi disponibilizada as variáveis "VENNBASIDF", "VENNPERIDF", "VENNVLRIDF" e "VENNPERDIF" referente a ICMS Diferido.

**Tela:** NFE/OC

**Transação:** Não se aplica.

**Variáveis Disponibilizadas:**

| Nome | Tipo | Observações | Retorna Valor |
| --- | --- | --- | --- |
| VSORIGEM | ALFA | Qual a origem da chamada do identificador. Pode ser: PED - Pedido, NFS - Nota fiscal de saída, NFE - Nota fiscal de Entrada, OCP - Ordem de compra ou OCT - Orçamento | N |
| VSCodEmp | NÚMERO | Código da Empresa | N |
| VSCodFil | NÚMERO | Código da Filial | N |
| VSCodSnf | NÚMERO | Código da Série | N |
| VSNumero | NÚMERO | Número da Nota Fiscal de Entrada ou Ordem de Compra | N |
| VSSeqIte | ALFA | Sequencia do Item da Nota Fiscal de Entrada ou Ordem de Compra | N |
| VSCodFor | ALFA | Código do Fornecedor - Disponível quando VSOrigem for 'NFE' ou 'OCP' | N |
| CPRNSeqOrm | ALFA | Sequência de Origem da Mercadoria - Disponível quando VSOrigem for 'NFE' ou 'OCP' | N |
| VSCODPRO | ALFA | Código do Produto | N |
| VSCODDER | ALFA | Código da Derivação | N |
| VSCODFAM | ALFA | Código da Família | N |
| VSTNSPRO | NÚMERO | Transação do item | N |
| VSCODTRD | NÚMERO | Código de Redução de ICMS | N |
| VSCODTIC | NÚMERO | Código de ICMS Especial | N |
| VSVLRBRU | NÚMERO | Valor Bruto | N |
| VSVLRDSC | NÚMERO | Valor Desconto | N |
| VSVLRDS1 | NÚMERO | Valor Desconto 1 | N |
| VSVLRDS2 | NÚMERO | Valor Desconto 2 | N |
| VSVLRDS3 | NÚMERO | Valor Desconto 3 | N |
| VSVLRDS4 | NÚMERO | Valor Desconto 4 | N |
| VSVLRDS5 | NÚMERO | Valor Desconto 5 | N |
| VSPERDS1 | NÚMERO | Percentual de desconto 1 | N |
| VSPERDS2 | NÚMERO | Percentual de desconto 2 | N |
| VSPERDS3 | NÚMERO | Percentual de desconto 3 | N |
| VSPERDS4 | NÚMERO | Percentual de desconto 4 | N |
| VSPERDS5 | NÚMERO | Percentual de desconto 5 | N |
| VSPEROF1 | NÚMERO | Percentual de oferta 1 | N |
| VSPEROF2 | NÚMERO | Percentual de oferta 2 | N |
| VSVLRIPI | NÚMERO | Valor de IPI | N |
| VSQTDITE | NÚMERO | Quantidade do produto/serviço | N |
| VSPREUNI | NÚMERO | Preço unitário do item da nota fiscal de entrada | N |
| VSVlrFei | NÚMERO | Valor de frete de importação | N |
| VSVlrSei | NÚMERO | Valor de seguro de importação | N |
| VSVlrOui | ALFA | Valor de outras despesas de importação | N |
| VSVLRFRE | ALFA | Valor do Frete | N |
| VSCIFFOB | NÚMERO | Indicativo se o frete é CIF ou FOB | N |
| VSSomFre | NÚMERO | Indicativo se o frete deve ser somado ao valor líquido da nota fiscal | N |
| VSVLRSEG | NÚMERO | Valor do Seguro | N |
| VSVLREMB | NÚMERO | Valor das Embalagens | N |
| VSVLRENC | NÚMERO | Valor dos Encargos | N |
| VSVLROUT | NÚMERO | Valor Outros | N |
| VSVLRDAR | NÚMERO | Valor de Arredondamento | N |
| VSVLRFRD | ALFA | Valor Frete Destacado | N |
| VSVLROUD | ALFA | Valor Outras Despesas Destacado | N |
| VSCODDEP | ALFA | Código do depósito | N |
| VSUFSCIC | ALFA | Sigla do estado base para o cálculo do ICMS | N |
| VSCODLOT | NÚMERO | Código do lote do item de produto na nota fiscal de saída | N |
| VSCODSTR | ALFA | Consulta da situação tributária do ICMS do item da nota fiscal | N |
| CPRNVlrAfm | ALFA | Valor AFRMM | N |
| CPRAFREIIM | ALFA | Transação considera o frete na base do II | N |
| CPRASEGIIM | ALFA | Transação considera o seguro na base do II | N |
| CPRAEMBIIM | ALFA | Transação considera a embalagem na base do II | N |
| CPRAENCIIM | ALFA | Transação considera os encargos na base do II | N |
| CPRAOUTIIM | ALFA | Transação considera outras despesas na base do II | N |
| CPRADARIIM | ALFA | Transação considera valor arredondamento na base do II | N |
| CPRAFRDIIM | ALFA | Transação considera o frete destacado na base do II | N |
| CPRAOUDIIM | ALFA | Transação considera outras despesas destacadas na base do II | N |
| CPRAIIMIPI | ALFA | Transação considera valor do II na base do IPI | N |
| CPRAIIMICM | ALFA | Transação considera valor do II na base do ICMS | N |
| CPRACPRFIM | ALFA | Soma valor de frete de importação na base do ICMS | N |
| CPRACPRSIM | ALFA | Soma valor de seguro de importação na base do ICMS | N |
| CPRACPROIM | ALFA | Soma valor de outras despesas de importação na base do ICMS | N |
| CPRACPRAIM | ALFA | Soma valor adicional ao frete para renovação da marinha mercante na base do ICMS | N |
| CPRACPRFII | ALFA | Soma valor do frete de importação na base do IPI | N |
| CPRACPRSII | ALFA | Soma valor de seguro de importação na base do IPI | N |
| CPRACPROII | ALFA | Soma valor de outras despesas de importação na base do IPI | N |
| CPRAFRIIIM | ALFA | Soma valor de frete de importação na base do II | N |
| CPRASGIIIM | ALFA | Soma valor de seguro de importação na base do II | N |
| CPRAOTIIIM | ALFA | Soma valor de outras despesas de importação na base do II | N |
| CPRACPRFIP | ALFA | Soma valor de frete de importação na base do PIS | N |
| CPRACPRSIP | ALFA | Soma valor de seguro de importação na base do PIS | N |
| CPRACPROIP | ALFA | Soma valor de outras despesas de importação na base do PIS | N |
| CPRACPRFIC | ALFA | Soma valor de frete de importação na base do cofins | N |
| CPRACPRSIC | ALFA | Soma valor de seguro de importação na base do cofins | N |
| CPRACPROIC | ALFA | Soma valor de outras despesas de importação na base do cofins | N |
| CprAOriMer | ALFA | Código de origem fiscal (do produto ou serviço), conforme item de nota fiscal de entrada, item de ordem de compra | N |
| ComNIcmAor | NÚMERO | Alíquota ICMS Partilha UF Origem - Disponível quando VSOrigem for 'NFE' | N |
| ComNIcmVor | NÚMERO | Valor ICMS Partilha UF Origem - Disponível quando VSOrigem for 'NFE' | S |
| ComNIcmAde | NÚMERO | Alíquota ICMS Partilha UF Destino - Disponível quando VSOrigem for 'NFE' | S |
| ComNIcmVde | NÚMERO | Valor ICMS Partilha UF Destino - Disponível quando VSOrigem for 'NFE' | S |
| ComNIcmBde | NÚMERO | Base ICMS Partilha UF Destino - Disponível quando VSOrigem for 'NFE' | S |
| ComNIcmAfc | NÚMERO | Alíquota ICMS Fundo de combate a pobreza - Disponível quando VSOrigem for 'NFE' | S |
| ComNIcmVfc | NÚMERO | Valor ICMS Fundo de combate a pobreza - Disponível quando VSOrigem for 'NFE' | S |
| ComNBasFcp | NÚMERO | Valor base do FCP | S |
| ComNAliFcp | NÚMERO | Alíquota do FCP | S |
| ComNVlrFcp | NÚMERO | Valor do FCP | S |
| VSPERICM | NÚMERO | Percentual de ICMS | S |
| VSVLRICM | NÚMERO | Valor de ICMS | S |
| VSVLRBIC | NÚMERO | Valor Base de ICMS | S |
| VSPERICI | NÚMERO | Percentual de ICMS de importação | S |
| ComNIcmAor | NÚMERO | (DIFAL) Percentual de ICMS partilha do estado de origem | S |
| ComNIcmVor | NÚMERO | (DIFAL) Valor de ICMS partilha do estado de origem | S |
| ComNIcmAde | NÚMERO | (DIFAL) Percentual de ICMS partilha do estado de destino | S |
| ComNIcmVde | NÚMERO | (DIFAL) Valor de ICMS partilha do estado de destino | S |
| ComNIcmBde | NÚMERO | (DIFAL) Base de ICMS partilha do estado de destino | S |
| ComNIcmAfc | NÚMERO | (DIFAL) Alíquota de fundo de combate à pobreza | S |
| ComNIcmVfc | NÚMERO | (DIFAL) Valor do fundo de combate à pobreza | S |
| ComNIcmBfc | NÚMERO | Base de cálculo do FCP na UF de destino (Difal) | S |
| VSCodSer | ALFA | Código do serviço | N |

Atenção

Caso o parâmetro global LisVarReg esteja habilitado, a variável ListaVariaveis estará disponível em todos os identificadores de regras do sistema. O conteúdo desta variável lista os campos disponibilizados no identificador de regras em questão.

Não é aconselhada a ativação desse parâmetro global para o uso cotidiano. Esse recurso de listagem dos campos de identificadores auxilia a construção de regras e o Suporte para, por exemplo, depuração ou quando não houver acesso à documentação dos identificadores de regras.

## Páginas relacionadas

* [LisVarReg](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#LisVarReg)
