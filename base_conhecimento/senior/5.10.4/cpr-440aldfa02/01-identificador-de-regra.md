# Identificador de Regra

> **Fonte:** Identificador de Regra — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/cpr_440aldfa02.htm  
> **Trilha:**   
> **Telas citadas:** E001TNS  
> **Identificadores de regras:** CPR-440ALDFA02

---
## CPR-440ALDFA02

**Módulo:** CPR - Compras.

**Finalidade:** Manipular o valor do diferencial de alíquota nas notas fiscais de entrada.

**Características:** Chamado sempre que atender as condições normais de cálculo do diferencial da alíquota, EXCETO a aplicação da natureza de operação E001TNS.CPRTCF, ou seja, o identificador de regras é chamado independente a aplicação da natureza de operação.  

A variável "VSVlrDfa - Valor da diferença das alíquotas entre os Estados" é enviada a regra ligada ao identificador com valor 0,00 (zero), pois ainda não foi calculado, a regra permite manipular esse valor (variável VSVlrDfa).

**Tela:** Notas Fiscais de Entrada

**Transação:** Pode estar ou não ligado a uma transação.

**Variáveis Disponibilizadas:**

| Nome | Tipo | Observações | Retorna Valor |
| --- | --- | --- | --- |
| VSProSer | ALFA | Indicativo se um item produto (P) ou serviço (S) | N |
| VSSigUfs | ALFA | Estado da nota fiscal de entrada | N |
| VSTipNfe | NÚMERO | Tipo da nota fiscal de entrada | N |
| VSOrigem | ALFA | Origem da chamada (nesse caso será NFE) | N |
| VSCodEmp | NÚMERO | Empresa da nota fiscal de entrada | N |
| VSCodFil | NÚMERO | Filial da nota fiscal de entrada | N |
| VSCodSnf | ALFA | Série da nota fiscal de entrada | N |
| VSNumNfc | NÚMERO | Número da nota fiscal de entrada | N |
| VSSeqIte | NÚMERO | Sequência do item sendo calculado | N |
| VSCodFor | NÚMERO | Fornecedor da nota fiscal de entrada | N |
| VSTnsIte | ALFA | Transação do item | N |
| VSNopIte | ALFA | Natureza de operação do item | N |
| VSCodPro | ALFA | Código do produto | N |
| VSCodDer | ALFA | Código da derivação do produto | N |
| VSCodSer | ALFA | Código do serviço | N |
| VSCodFam | ALFA | Código da família | N |
| VSCodTic | ALFA | Código do ICMS especial | N |
| VSCodTrd | ALFA | Código de redução do ICMS | N |
| VSCodTst | ALFA | Código do ICMS substituído | N |
| VSCodStc | ALFA | Código de substiuição do COFINS | N |
| VSCodStp | ALFA | Código de substituição do PIS | N |
| VSCodStr | ALFA | Código da situação tributária | N |
| VSCodClf | ALFA | Código da classificação fiscal | N |
| VSCodTpr | ALFA | Código da tabela de preço do item | N |
| VSQtdRec | NÚMERO | Quantidade recebida na unidade de medida do fornecedor | N |
| VSUniNfc | ALFA | Unidade de medida do fornecedor | N |
| VSQtdEst | NÚMERO | Quantidade recebida na unidade de medida do estoque | N |
| VSUniMed | ALFA | Unidade de medida do estoque | N |
| VSPreUni | NÚMERO | Preço unitário na unidade de medida do fornecedor | N |
| VSPreEst | NÚMERO | Preço unitário na unidade de medida do estoque | N |
| VSPerIpi | NÚMERO | Percentual de IPI | N |
| VSPerIcm | NÚMERO | Percentual de ICMS | N |
| VSPerFun | NÚMERO | Percentual de FUNRURAL | N |
| VSPerSen | NÚMERO | Percentual do Senar | N |
| VSNumPrj | NÚMERO | Número do projeto | N |
| VSCodFpj | NÚMERO | Fase do projeto | N |
| VSCtaFin | NÚMERO | Conta financeira | N |
| VSCtaRed | NÚMERO | Conta contábil | N |
| VSCodCcu | ALFA | Centro de custos | N |
| VSVlrFre | NÚMERO | Valor de frete | N |
| VSVlrSeg | NÚMERO | Valor de seguros | N |
| VSVlrEmb | NÚMERO | Valor de embalagens | N |
| VSVlrEnc | NÚMERO | Valor de encargos | N |
| VSVlrOut | NÚMERO | Valor de outras despesas | N |
| VSVlrDar | NÚMERO | Valor de arredondamento | N |
| VSVlrFrd | NÚMERO | Valor frete destacado | N |
| VSVlrOud | NÚMERO | Valor de outras despesas destacado | N |
| VSVlrBru | NÚMERO | Valor bruto do item | N |
| VSPerDsc | NÚMERO | Percentual de desconto | N |
| VSVlrDsc | NÚMERO | Valor de desconto | N |
| VSPerDs1 | NÚMERO | Percentual de desconto 1 | N |
| VSVlrDs1 | NÚMERO | Valor de desconto 1 | N |
| VSPerDs2 | NÚMERO | Percentual de desconto 2 | N |
| VSVlrDs2 | NÚMERO | Valor de desconto 2 | N |
| VSPerDs3 | NÚMERO | Percentual de desconto 3 | N |
| VSVlrDs3 | NÚMERO | Valor de desconto 3 | N |
| VSPerDs4 | NÚMERO | Percentual de desconto 4 | N |
| VSVlrDs4 | NÚMERO | Valor de desconto 4 | N |
| VSPerDs5 | NÚMERO | Percentual de desconto 5 | N |
| VSVlrDs5 | NÚMERO | Valor de desconto 5 | N |
| VSVlrDzf | NÚMERO | Valor de desconto na zona franca | N |
| VSVlrBip | NÚMERO | Valor base do IPI | N |
| VSVlrIpi | NÚMERO | Valor do IPI | N |
| VSVlrBid | NÚMERO | Valor base IPI presumido | N |
| VSVlrIpd | NÚMERO | Valor do IPI presumido | N |
| VSVlrBic | NÚMERO | Valor base do ICMS | N |
| VSVlrIcm | NÚMERO | Valor do ICMS | N |
| VSVlrBsi | NÚMERO | Valor base ICMS SUbstituído | N |
| VSVlrIcs | NÚMERO | Valor do ICMS substituído | N |
| VSVlrBsd | NÚMERO | Valor base ICMS substituto destacado | N |
| VSVlrIsd | NÚMERO | Valor ICMS susbtituto destacado | N |
| VSVlrBsp | NÚMERO | Valor base subsituição do PIS | N |
| VSVlrStp | NÚMERO | Valor substituição do PIS | N |
| VSVlrBsc | NÚMERO | Valor base subsituição do COFINS | N |
| VSVlrStc | NÚMERO | Valor da substituição do COFINS | N |
| VSVlrBpi | NÚMERO | Valor base PIS recuperar | N |
| VSVlrPis | NÚMERO | Valor PIS recuperar | N |
| VSVlrBcr | NÚMERO | Valor base COFINS recuperar | N |
| VSVlrCor | NÚMERO | Valor COFINS recuperar | N |
| VSPerIim | NÚMERO | Percentual do imposto de importação | N |
| VSVlrIim | NÚMERO | Valor do imposto de importação | N |
| VSPerIss | NÚMERO | Percentual de ISS | N |
| VSPerIrf | NÚMERO | Percentual de IRRF | N |
| VSPerIns | NÚMERO | Percentual de INSS | N |
| VSVlrBis | NÚMERO | Valor base do ISS | N |
| VSVlrIss | NÚMERO | Valor do ISS | N |
| VSVlrBir | NÚMERO | Valor base do IRRF | N |
| VSVlrIrf | NÚMERO | Valor do IRRF | N |
| VSVlrBin | NÚMERO | Valor base do INSS | N |
| VSVlrIns | NÚMERO | Valor do INSS | N |
| VSVlrBct | NÚMERO | Valor base COFINS retido | N |
| VSVlrCrt | NÚMERO | Valor COFINS retido | N |
| VSPerCrt | NÚMERO | Percentual COFINS retido | N |
| VSVlrBpt | NÚMERO | Valor base PIS retido | N |
| VSPerPit | NÚMERO | Percentual PIS retido | N |
| VSVlrBcl | NÚMERO | Valor base CSLL retido | N |
| VSVlrCsl | NÚMERO | Valor de CSLL retido | N |
| VSPerCsl | NÚMERO | Percentual de CSLL retido | N |
| VSVlrBor | NÚMERO | Valor base outras retenções | N |
| VSVlrOur | NÚMERO | Valor de outras retenções | N |
| VSPerOur | NÚMERO | Percentual de outras retenções | N |
| VSPerIce | NÚMERO | Percentual de ICMS do Estado | N |
| VSVlrIce | NÚMERO | Valor de ICMS do Estado | N |
| VSCprTcf | ALFA | Aplicação da natureza de Operação | N |
| VSVlrPit | NÚMERO | Valor PIS retido | N |
| VSVlrDfa | NÚMERO | Valor da diferença das alíquotas entre os Estados | S |

Atenção

Caso o parâmetro global LisVarReg esteja habilitado, a variável ListaVariaveis estará disponível em todos os identificadores de regras do sistema. O conteúdo desta variável lista os campos disponibilizados no identificador de regras em questão.

Não é aconselhada a ativação desse parâmetro global para o uso cotidiano. Esse recurso de listagem dos campos de identificadores auxilia a construção de regras e o Suporte para, por exemplo, depuração ou quando não houver acesso à documentação dos identificadores de regras.

## Páginas relacionadas

* [LisVarReg](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#LisVarReg)
