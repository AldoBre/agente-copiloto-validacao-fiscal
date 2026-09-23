# Grupo W01 - Total da NF-e / ISSQN

> **Fonte:** Leiautes NF-e e NFC-e — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/leiaute-nf-e-nfc-e.htm  
> **Trilha:** Segmentos > Compliance > Documentos Eletrônicos > NF-e | NFC-e (Nota Fiscal Eletrônica) > Nota Fiscal Eletrônica 4.0  
> **Telas citadas:** —  
> **Identificadores de regras:** —

---
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação | Origem |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 342 | W17 | ISSQNtot | Grupo Totais referentes ao ISSQN | G | W01 |  | 0-1 |  |  | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 343 | W18 | vServ | Valor total dos Serviços sob não - incidência ou não tributados pelo ICMS | E | W17 | N | 0-1 | 13v2 |  | Gera o valor, conforme consta no campo E140Ipv.VlrBru (soma de todos os itens). |
| 344 | W19 | vBC | Valor total Base de Cálculo do ISS | E | W17 | N | 0-1 | 13v2 |  | Gera o valor, conforme consta no campo E140Nfv.VlrBis. |
| 345 | W20 | vISS | Valor total do ISS | E | W17 | N | 0-1 | 13v2 |  | Gera o valor, conforme consta no campo E140Nfv.VlrIss. |
| 346 | W21 | vPIS | Valor total do PIS sobre serviços | E | W17 | N | 0-1 | 13v2 |  | Gera o valor, conforme consta no campo E140NfvVlrPis. |
| 347 | W22 | vCOFINS | Valor total da COFINS sobre serviços | E | W17 | N | 0-1 | 13v2 |  | Gera o valor, conforme consta no campo E140Nfv.VlrCor. |
| 347a | W22a | dCompet | Data da prestação do serviço | E | W17 | N | 1-1 | 8 | Formato: "AAA-MM-DD" | Gera o valor, conforme consta no campo E140Tnf.DatPre. |
| 347b | W22b | vDeducao | Valor total dedução para redução da Base de Cálculo | E | W17 | N | 0-1 | 13v2 |  | Gera o valor, conforme consta no campo E140Nfv.VlrDed. |
| 347c | w22c | vOutro | Valor total outras retenções | E | W17 | N | 0-1 | 13v2 | Valor declaratório | Gera o valor, conforme a soma dos campos E140Nfv.VlrEmb + E140Nfv.VlrEnc + E140Nfv.VlrOut + E140Nfv.VlrOui. |
| 347d | W22d | vDescIncond | Valor total desconto incondicionado | E | W17 | N | 0-1 | 13v2 |  | Gera o valor, conforme consta no campo E140Ipv.VlrDsc, VlrDs1, VlrDs2,VlrDs3, VlrDs4, VlrDs5. |
| 347e | W22e | vDescCond | Valor total desconto condicionado | E | W17 | N | 0-1 | 13v2 |  | Gera o valor, conforme consta no campo E140Ipv.VlrDsc, VlrDs1, VlrDs2,VlrDs3, VlrDs4. |
| 347f | W22f | vISSRet | Valor total renteção ISS | E | W17 | N | 0-1 | 13v2 |  | Gera o valor, conforme consta no campo E140Nfv.VlrLiq. |
| 347g | W22g | cRegTrib | Código do Regime Especial de Tributação | E | W17 | N | 0-1 | 2 | 1. Microempresa 2. Estimativa 3. Sociedade de Profissionais 4. Cooperativa 5. Microempresário Individual (MEI) 6. Microempresário e Empresa de Pequeno Porte | Essa tag não é gerada pelo ERP. |
