# Tabelas disponibilizadas

> **Fonte:** Adequação aos leiautes do SPED Fiscal — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/sped/fiscal-icms-ipi/adequacoes-leiautes.htm  
> **Trilha:** Segmentos > Compliance > Escriturações Fiscais Digitais (SPED) > SPED Fiscal (EFD ICMS/IPI)  
> **Telas citadas:** E001TNS, E001TVE, E085HCL, E660INC, E660NFC, E660NFV, E660RSV, F070FCA, F075CEP  
> **Identificadores de regras:** —

---
Confira abaixo as tabelas disponibilizadas pelos estados:

**Para filiais optantes pelo ROT-ST que precisam declarar as operações como "Não se aplica ICMS-ST":**

* Cadastro de Filiais (F070FCA): editar o parâmetro dinâmico TRIBUTOS.ADESAOROTST = "S" para as filiais optantes pelo ROT-ST
* Controle de Entrada de Produtos (F075CEP): ao atualizar a média móvel ponderada, as operações internas com consumidor final recebem o código de operação onde não se aplica restituição ou complementação de ICMS ST (UF000), de acordo com a Tabela 5.7 publicada pela UF

## Mato Grosso do Sul

| Estado | Valor | Descrição | Especificação conforme lei | Documentação |
| --- | --- | --- | --- | --- |
| MS | 000 | Não se aplica restituição ou complementação de ICMS/ST | Saída sem valores de ICMS complementar ou Ressarcimento | VL\_UNIT\_ICMS\_ST\_CONV\_REST + VL\_UNIT\_ICMS\_ST\_CONV\_COMPL for igual 0 |
| MS | 100 | Restituição de ICMS/ST, em razão do valor de saída da mercadoria final ser inferior ao da BC/ST | Restituição (onde a base do ST pago na compra foi **superior** ao valor de venda) | **Restituição:** ConsumidorFinal, Valor de Ressarcimento > 0 e não for uma transação de Ressarcimento |
| MS | 200 | Restituição de ICMS/ST, em razão da não ocorrência do fato gerador presumido | Operações com ressarcimento | **Ressarcimento:** Valor de Ressarcimento > 0, for uma transação de Ressarcimento e Código Fiscal de Operação e Prestação (CFOP) não iniciar em 6 |
| MS | 201 | Restituição de ICMS/ST, em razão da saída interestadual | Operações com ressarcimento em razão da saída interestadual | Valor de Ressarcimento > 0, for uma transação de Ressarcimento e e Código Fiscal de Operação e Prestação (CFOP) iniciar em 6 |
| MS | 300 | Complementação de ICMS/ST, em razão do valor de saída da mercadoria a consumidor final ser superior ao da BC/ST | Complementação (onde a base do ST pago na compra foi **inferior** ao valor de venda) | ConsumidorFinal e Valor de Complementação > 0 |

**Legenda:**

* Transação com ressarcimento: E001TVE.IcmRes = S
* Cliente não consumidor final: E085HCL.ConFin <> (diferente de) S
* Venda interna a consumidor final: E660RSV.NopOpe=5xxx, E660RSV.CodStr=x60 e cliente consumidor final
* Aplicação da operação: E001TNS.VenTcf
* Operação sem complementação: E660RSV.VlrBsc = 0
* Média ponderada móvel: E66RSM.MedIcm + E66RSM.MedIcs + E66RSM.MedFcp (esse valor é confrontado com o imposto complementar E660RSV.VlrIsc, E660RSV.VlrFcc e determina se a operação tem restituição ou complemento)
* Cliente órgão público: E085Cli.TipEmc = 2

## Minas Gerais

| Código do Ajuste | Descrição do Ajuste | Condição |
| --- | --- | --- |
| MG000 | Não se aplica restituição ou complementação de ICMS/ST | Cliente não consumidor final + transação sem ressarcimento OU venda interna a consumidor final com valor de venda igual ao da média ponderada móvel |
| MG100 | Restituição de ICMS/ST, em razão do valor de saída da mercadoria final ser inferior ao da BC/ST | Venda interna a consumidor final por valor inferior ao da média ponderada móvel |
| MG200 | Restituição de ICMS/ST, em razão da não ocorrência do fato gerador presumido | Transação com ressarcimento |
| MG300 | Complementação de ICMS/ST, em razão do valor de saída da mercadoria a consumidor final ser superior ao da BC/ST | Venda interna a consumidor final por valor superior ao da média ponderada móvel |
| MG400 | Devolução de entradas | CFOP iniciada em 5 ou 6 + E660NFV.TipNfs = 2 |
| MG500 | Devolução de saídas em que não se aplicou restituição, ressarcimento ou complemento | E660NFV.TipNfs = 2 ou 3 + Codigo57 da NF de Saida for = MG000 |
| MG600 | Estorno da restituição/ressarcimento do imposto, calculado com base no valor saída inferior ao valor da BC ICMS ST | E660NFV.TipNfs = 2 ou 3 + Codigo57 da NF de Saida for = MG100 |
| MG800 | Estorno do complemento do imposto, calculado com base no valor de saída da mercadoria superior ao valor da BC ICMS ST | E660NFV.TipNfs = 2 ou 3 + Codigo57 da NF de Saida for = MG300 |

**Legenda:**

* Transação com ressarcimento: E001TVE.IcmRes = S
* Cliente não consumidor final: E085HCL.ConFin <> (diferente de) S
* Venda interna a consumidor final: E660RSV.NopOpe=5xxx, E660RSV.CodStr=x60 e cliente consumidor final
* Aplicação da operação: E001TNS.VenTcf
* Operação sem complementação: E660RSV.VlrBsc = 0
* Média ponderada móvel: E66RSM.MedIcm + E66RSM.MedIcs + E66RSM.MedFcp (esse valor é confrontado com o imposto complementar E660RSV.VlrIsc, E660RSV.VlrFcc e determina se a operação tem restituição ou complemento)
* Cliente órgão público: E085Cli.TipEmc = 2

**Observação**

Caso não seja possível atribuir o código do motivo da Tabela 5.7 conforme os parâmetros descritos acima, será atribuído o código **MG000** (se for saída) ou **MG500** (se devolução).

## Pará

| COD\_MOT\_REST\_COMPL | Descrição | Documentação |
| --- | --- | --- |
| PA000 | Não se aplica restituição ou complementação de ICMS-ST | Cliente não consumidor final + transação sem ressarcimento **ou** venda interna a consumidor final com valor de venda igual ao da média ponderada móvel |
| PA100 | Ressarcimento de ICMS-ST, em razão do valor de saída da mercadoria final ser inferior ao da BC-ST | Cliente ConsumidorFinal, Valor de Ressarcimento > 0 e não for uma transação de Ressarcimento |
| PA200 | Ressarcimento de ICMS-ST, em razão da não ocorrência do fato gerador presumido | Valor de Ressarcimento > 0 e for uma transação de Ressarcimento e não tratar-se de devolução de entrada (E660NFV.TipNfs <> 2) |
| PA300 | Complementação de ICMS/ST, em razão do valor de saída da mercadoria a consumidor final ser superior ao da BC/ST | Cliente ConsumidorFinal e Valor de Complementação > 0 |

## Rio de Janeiro

| COD\_MOT\_REST\_COMPL | Descrição | Documentação |
| --- | --- | --- |
| RJ000 | Não se aplica restituição, ressarcimento ou complemento | Cliente não consumidor final + transação sem ressarcimento ou venda interna a consumidor final com valor de venda igual ao da média ponderada móvel |
| RJ100 | Direito a restituição/ressarcimento do imposto, calculado com base no valor de saída inferior ao valor da BC ICMS ST | Cliente ConsumidorFinal, Valor de Ressarcimento > 0 e não for uma transação de Ressarcimento |
| RJ300 | Complemento do imposto, calculado com base no valor de saída da mercadoria superior ao valor da BC ICMS ST | Cliente ConsumidorFinal e Valor de Complementação > 0 |
| RJ400 | Devolução de entradas | CFOP iniciada em 5 ou 6 + E660NFV.TipNfs = 2 |
| RJ500 | Devolução de saídas em que não se aplicou restituição, ressarcimento ou complemento | E660NFC.TipNfs = 2 ou 3 + Codigo57 da NF de Saida for = RO000 |
| RJ600 | Estorno da restituição/ressarcimento do imposto, calculado com base no valor de saída inferior ao valor da BC ICMS ST | E660NFC.TipNfs = 2 ou 3 + Codigo57 da NF de Saida for = RO100 |
| RJ800 | Estorno do complemento do imposto, calculado com base no valor de saída da mercadoria superior ao valor da BC ICMS ST | E660NFC.TipNfs = 2 ou 3 + Codigo57 da NF de Saida for = RO300 |

## Rio Grande do Sul

**Observação**

* Caso não seja possível atribuir o código do motivo da Tabela 5.7 conforme os parâmetros descritos acima, será atribuído o código **RS000** (se for saída) ou **RS500** (se devolução)
* Os registros de ICMS ST não serão gerados no SPED fiscal para optantes pelo ROT-ST do estado do RS, no qual a apuração do ressarcimento ocorre via registros C176/C197

| Código do Ajuste | Descrição do Ajuste | Condição |
| --- | --- | --- |
| RS000 | saída sem RESSARCIMENTO-ST ou COMPLEMENTO-ST, tal como a saída de mercadoria com ST não destinada a consumidor final deste Estado - RICMS, Livro III, art. 11 | Cliente não consumidor final + transação sem ressarcimento **ou** venda interna a consumidor final com valor de venda igual ao da média ponderada móvel |
| RS001 | saída com RESSARCIMENTO-ST pela sistemática do RICMS, Livro III, arts. 24 e 24-A | Cliente órgão público + CFOP iniciada em 5 + transação sem ressarcimento |
| RS011 | baixa sem RESSARCIMENTO-ST - Furto ou Roubo - mercadoria recebida de contribuinte substituído | - |
| RS012 | baixa sem RESSARCIMENTO-ST - Perda, extravio ou Deterioração - mercadoria recebida de contribuinte substituído | CFOP 5927 + aplicação da transação diferente de 'S' + transação sem ressarcimento |
| RS015 | baixa sem RESSARCIMENTO-ST - Mercadoria destinada para uso e Consumo ou para fim alheio à atividade do estabelecimento - mercadoria recebida de contribuinte substituído | CFOP 5927 + aplicação da transação = 'S' + transação sem ressarcimento + operação sem complementação |
| RS100 | saída com RESSARCIMENTO-ST - calculado com base no valor de saída inferior ao valor da BC ICMS ST - RICMS, Livro III, art. 25-B | Venda interna a consumidor final por valor inferior ao da média ponderada móvel |
| RS211 | baixa com RESSARCIMENTO-ST - Furto ou Roubo - mercadoria recebida de contribuinte substituto - RICMS, Livro III, art. 22 | - |
| RS212 | baixa com RESSARCIMENTO-ST - Perda, extravio ou Deterioração - mercadoria recebida de contribuinte substituto - RICMS, Livro III, art. 22 | CFOP 5927 + aplicação da transação diferente de 'S' + transação com ressarcimento |
| RS213 | saída com RESSARCIMENTO-ST - Saída para outra UF (RICMS, Livro III, art.23, I) ou devolução para fornecedor de outra UF, quando a retenção inicial foi realizada pelo próprio remetente da devolução, nos moldes do RICMS, Livro III, art. 53-A (RICMS, Livro III, art. 25) | CFOP iniciada em 6 + transação com ressarcimento + Média Ponderada Móvel ICMS ST>0 |
| RS214 | saída com RESSARCIMENTO-ST - Exportação - RICMS, Livro III, art. 23, I | CFOP= x501, x502 ou iniciada em 7 + transação com ressarcimento |
| RS215 | baixa com RESSARCIMENTO-ST - Mercadoria destinada para uso e consumo ou para fim alheio à atividade do estabelecimento - mercadoria recebida de contribuinte substituto - RICMS, Livro III, art.22 | CFOP = 5927 + aplicação da transação = 'S' + transação com ressarcimento |
| RS217 | saída com RESSARCIMENTO-ST - Saída Interna com nova ST - RICMS, Livro III, art.23, III | CFOP iniciada em 5 + transação com ressarcimento |
| RS219 | saída com RESSARCIMENTO-ST - Saída de mercadorias beneficiadas com a isenção de que trata o art. 9º, CXX ou CLXIV, do Livro I - RICMS, Livro III, art.23, V | CFOP iniciada em 5 + Transação com ressarcimento + cliente órgão público |
| RS300 | saída com COMPLEMENTO-ST - calculado com base no valor de saída da mercadoria superior ao valor da BC ICMS ST- RICMS, Livro III, art. 25-B | Venda interna a consumidor final por valor superior ao da média ponderada móvel |
| RS400 | saída sem RESSARCIMENTO-ST ou COMPLEMENTO-ST - saída em devolução | CFOP iniciada em 5 ou 6 + E660NFV.TipNfs = 2 |
| RS413 | saída sem RESSARCIMENTO-ST ou COMPLEMENTO-ST - saída em devolução para OUF, quando a retenção inicial foi realizada pelo próprio remetente da devolução, nos moldes do RICMS, Livro III, art. 53-A (RICMS, Livro III, art. 25) | CFOP iniciada em 5 ou 6 + E660NFV.TipNfs = 2 + Valor de ICMS-ST Solidário maior do que zero na nota que está sendo devolvida (E660INC.VlrRis) |
| RS500 | entrada sem estorno de RESSARCIMENTO-ST ou de COMPLEMENTO-ST - entrada em devolução ou retorno de mercadoria não entregue que na saída teve registro no código RS000 | E660NFV.TipNfs = 2 ou 3 + Codigo57 da NF de Saida for = RS000 |
| RS501 | entrada em devolução ou retorno de mercadoria não entregue que na saída teve registro no código RS001 | E660NFV.TipNfs = 2 ou 3 + Codigo57 da NF de Saida for = RS001 |
| RS600 | entrada com estorno do RESSARCIMENTO-ST - entrada em devolução ou retorno de mercadoria não entregue que na saída teve registro no código RS100 | E660NFV.TipNfs = 2 ou 3 + Codigo57 da NF de Saida for = RS100 |
| RS713 | entrada com estorno do RESSARCIMENTO-ST - entrada em devolução ou retorno de mercadoria não entregue que na saída teve registro no código RS213 | E660NFV.TipNfs = 2 ou 3 + Codigo57 da NF de Saida for = RS213 |
| RS714 | entrada com estorno do RESSARCIMENTO-ST - entrada em devolução ou retorno de mercadoria não entregue que na saída teve registro anterior no código RS214 | E660NFV.TipNfs = 2 ou 3 + Codigo57 da NF de Saida for = RS214 |
| RS717 | entrada com estorno do RESSARCIMENTO-ST - entrada em devolução ou retorno de mercadoria não entregue que na saída teve registro anterior no código RS217 | E660NFV.TipNfs = 2 ou 3 + Codigo57 da NF de Saida for = RS217 |
| RS719 | entrada com estorno do RESSARCIMENTO-ST - entrada em devolução ou retorno de mercadoria não entregue que na saída teve registro anterior no código RS219 | E660NFV.TipNfs = 2 ou 3 + Codigo57 da NF de Saida for = RS219 |
| RS800 | entrada com estorno do COMPLEMENTO-ST - entrada em devolução ou retorno de mercadoria não entregue que na saída teve registro no código RS300 | E660NFV.TipNfs = 2 ou 3 + Codigo57 da NF de Saida for = RS300 |

**Legenda:**

* Transação com ressarcimento: E001TVE.IcmRes = S
* Cliente não consumidor final: E085HCL.ConFin <> (diferente de) S
* Venda interna a consumidor final: E660RSV.NopOpe=5xxx, E660RSV.CodStr=x60 e cliente consumidor final
* Aplicação da operação: E001TNS.VenTcf
* Operação sem complementação: E660RSV.VlrBsc = 0
* Média ponderada móvel: E66RSM.MedIcm + E66RSM.MedIcs + E66RSM.MedFcp (esse valor é confrontado com o imposto complementar E660RSV.VlrIsc, E660RSV.VlrFcc e determina se a operação tem restituição ou complemento)
* Cliente órgão público: E085Cli.TipEmc = 2

## Rondônia

| COD\_MOT\_REST\_COMPL | Descrição | Documentação |
| --- | --- | --- |
| RO000 | Não se aplica ressarcimento ou complementação de ICMS/ST - Operações com gasolina, óleo diesel e álcool etílico hidratado carburante | Cliente não consumidor final + transação sem ressarcimento **ou** venda interna a consumidor final com valor de venda igual ao da média ponderada móvel |
| RO100 | Ressarcimento de ICMS/ST, em razão do valor de saída da mercadoria final ser inferior ao da BC/ST - Operações com gasolina, óleo diesel e álcool etílico hidratado carburante | Cliente ConsumidorFinal, Valor de Ressarcimento > 0 e não for uma transação de Ressarcimento |
| RO200 | Ressarcimento de ICMS/ST, em razão da não ocorrência do fato gerador presumido - Operações com gasolina, óleo diesel e álcool etílico hidratado carburante | Valor de Ressarcimento > 0 e for uma transação de Ressarcimento |
| RO300 | Complementação de ICMS/ST, em razão do valor de saída da mercadoria a consumidor final ser superior ao da BC/ST - Operações com gasolina, óleo diesel e álcool etílico hidratado carburante | Cliente ConsumidorFinal e Valor de Complementação > 0 |
| RO400 | Devolução de entradas - Operações com gasolina, óleo diesel e álcool etílico hidratado carburante | CFOP iniciada em 5 ou 6 + E660NFV.TipNfs = 2 |
| RO500 | Devolução de saídas em que não se aplicou ressarcimento ou complemento - Operações com gasolina, óleo diesel e álcool etílico hidratado carburante | E660NFC.TipNfs = 2 ou 3 + Codigo57 da NF de Saida for = RO000 |
| RO600 | Estorno do ressarcimento do imposto, calculado com base no valor saída inferior ao valor da BC ICMS ST - Operações com gasolina, óleo diesel e álcool etílico hidratado carburante | E660NFC.TipNfs = 2 ou 3 + Codigo57 da NF de Saida for = RO100 |
| RO700 | Estorno do ressarcimento do imposto, por não ocorrência do fato gerador presumido - Operação com combustíveis - Operações com gasolina, óleo diesel e álcool etílico hidratado carburante | E660NFC.TipNfs = 2 ou 3 + Codigo57 da NF de Saida for = RO200 |
| RO800 | Estorno do complemento do imposto, calculado com base no valor de saída da mercadoria superior ao valor da BC ICMS ST - Operações com gasolina, óleo diesel e álcool etílico hidratado carburante | E660NFC.TipNfs = 2 ou 3 + Codigo57 da NF de Saida for = RO300 |

## Sergipe

| Código do Ajuste | Descrição do Ajuste | Condição |
| --- | --- | --- |
| SE000 | Não se aplica restituição ou complementação de ICMS/ST | Cliente não consumidor final + transação sem ressarcimento OU venda interna a consumidor final com valor de venda igual ao da média ponderada móvel |
| SE100 | Restituição de ICMS/ST, em razão do valor de saída da mercadoria final ser inferior ao da BC/ST | Venda interna a consumidor final por valor inferior ao da média ponderada móvel |
| SE200 | Restituição de ICMS/ST, em razão da não ocorrência do fato gerador presumido | Transação com ressarcimento |
| SE220 | Ressarcimento de ICMS-ST em razão da saída interestadual da mercadoria já alcançada pela ST. | - |
| SE300 | Complementação de ICMS/ST, em razão do valor de saída da mercadoria a consumidor final ser superior ao da BC/ST | Venda interna ao consumidor final por valor maior que a média ponderada móvel |
| SE400 | Devolução de entradas | CFOP iniciada em 5 ou 6 + E660NFV.TipNfs = 2 |
| SE500 | Devolução de saídas em que não se aplicou restituição, ressarcimento ou complemento | E660NFV.TipNfs = 2 ou 3 + Codigo57 da NF de Saida for = SE000 |
| SE600 | Estorno da restituição/ressarcimento do imposto, calculado com base no valor saída inferior ao valor da BC ICMS ST | E660NFV.TipNfs = 2 ou 3 + Codigo57 da NF de Saida for = SE100 ou SE200 |
| SE620 | Estorno da ressarcimento de ICMS-ST em razão da saída interestadual da mercadoria já alcançada pela ST. | E660NFV.TipNfs = 2 ou 3 + Codigo57 da NF de Saida for = SE220 |
| SE800 | Estorno do complemento do imposto, calculado com base no valor de saída da mercadoria superior ao valor da BC ICMS ST | E660NFV.TipNfs = 2 ou 3 + Codigo57 da NF de Saida for = SE300 |

**Observação**

Caso não seja possível atribuir o código do motivo da Tabela 5.7 conforme os parâmetros descritos acima, será atribuído o código **SE000** (se for saída) ou **SE500** (se devolução).

## Páginas relacionadas

* [Cadastro de Filiais (F070FCA)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070fca.htm)
* [parâmetro dinâmico](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000ppd.htm)
* [Controle de Entrada de Produtos (F075CEP)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075cep.htm)
* [C176/C197](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/sped/fiscal-icms-ipi/bloco-c.htm#C176)
