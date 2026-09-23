# Grupo W - Total da NF-e

> **Fonte:** Leiautes NF-e e NFC-e — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/leiaute-nf-e-nfc-e.htm  
> **Trilha:** Segmentos > Compliance > Documentos Eletrônicos > NF-e | NFC-e (Nota Fiscal Eletrônica) > Nota Fiscal Eletrônica 4.0  
> **Telas citadas:** —  
> **Identificadores de regras:** —

---
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação | Origem |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 326 | W01 | total | Grupo Totais da NF-e | G | A01 |  | 1-1 |  | O grupo de valores totais da NF-e deve ser informado com o somatório do campo correspondente dos itens | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 327 | W02 | ICMSTot | Grupo Totais referente ao ICMS | G | W01 |  | 1-1 |  |  | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 328 | W03 | vBC | Base de Cálculo do ICMS | E | W02 | N | 1-1 | 13v2 |  | Gera o valor que consta no campo E140Nfv.VlrBic + E140Tnf.BasIdf. |
| 329 | W04 | vICMS | Valor Total do ICMS | E | W02 | N | 1-1 | 13v2 |  | Gera o valor que consta no campo E140Nfv.VlrIcm. |
| 329.01 | W04a | vICMSDeson | Valor Total do ICMS desonerado | E | W02 | N | 1-1 | 13v2 |  | Gera o valor, conforme consta no campo E140Nfv.VlrIcd. |
| 329.03 | W04c | vFCPUFDest | Valor total do ICMS relativo ao Fundo de Combate à Pobreza (FCP) da UF de destino | E | W02 | N | 0-1 | 13v2 | Valor total do ICMS relativo ao Fundo de Combate à Pobreza (FCP) para a UF de destino. (Incluído na NT 2015/003) | Gera o valor, conforme consta no campo E140Tnf.IcmVfc. |
| 329.05 | W04e | vICMSUFDest | Valor total do ICMS Interestadual para a UF de destino | E | W02 | N | 0-1 | 13v2 | Valor total do ICMS Interestadual para a UF de destino, já considerando o valor do ICMS relativo ao Fundo de Combate à Pobreza naquela UF. (Incluído na NT 2015/003) | Gera o valor, conforme consta no campo E140Ipv.IcmVde (soma de todos os itens). |
| 329.07 | W04g | vICMSUFRemet | Valor total do ICMS Interestadual para a UF do remetente | E | W02 | N | 0-1 | 13v2 | Valor total do ICMS Interestadual para a UF do remetente. Nota: a partir de 2019, este valor será zero. (Incluído na NT 2015/003) | Gera o valor, conforme consta no campo E140Ipv.IcmVde (soma de todos os itens). |
| 329.08 | W04h | vFCP | Valor Total do FCP (Fundo de Combate à Pobreza) | E | W02 | N | 1-1 | 13v2 | Corresponde ao total da soma dos campos id:N17c (Incluído na NT2016.002) | Gera o valor, conforme consta no campo E140Tnf.VlrFcp. |
| 330 | W05 | vBCST | Base de Cálculo do ICMS ST | E | W02 | N | 1-1 | 13v2 |  | Gera o valor, conforme consta no campo E140Nfv.VlrBst. |
| 331 | W06 | vST | Valor Total do ICMS ST | E | W02 | N | 1-1 | 13v2 |  | Gera o valor, conforme consta no campo E140Nfv.VlrSic. |
| 331.01 | W06a | vFCPST | Valor Total do FCP (Fundo de Combate à Pobreza) retido por substituição tributária | E | W02 | N | 1-1 | 13v2 | Corresponde ao total da soma dos campos id:N23d (Incluído na NT2016.002) | Gera o valor, conforme consta no campo E140PvdVstFcp. |
| 331.02 | W06b | vFCPSTRet | Valor Total do FCP retido anteriormente por Substituição Tributária | E | W02 | N | 1-1 | 13v2 | Corresponde ao total da soma dos campos id:N27d (Incluído na NT2016.002) | Gera o valor, conforme consta no campo E140Pvd.VreFcp. |
| 331.02a | W06b.1 | qBCMono | Valor total da quantidade tributada do ICMS Monofásico próprio | E | W02 | N | 0-1 | 13v2 | Correspondente ao total da soma dos campos id:N37a |  |
| 331.03 | W06c | vICMSMono | Valor total do ICMS Monofásico próprio | E | W02 | N | 0-1 | 13v2 | Correspondente ao total da soma dos campos id:N39 |  |
| 331.03a | W06c.1 | qBCMonoReten | Valor total da quantidade tributada do ICMS Monofásico sujeito a retenção | E | W02 | N | 0-1 | 13v2 | Correspondente ao total da soma dos campos id:N39a |  |
| 331.04 | W06d | vICMSMonoReten | Valor total do ICMS Monofásico sujeito a retenção | E | W02 | N | 0-1 | 13v2 | Correspondente ao total da soma dos campos id: N41 |  |
| 331.04a | W06d.1 | qBCMonoRet | Valor total da quantidade tributada do ICMS Monofásico retido anteriormente | E | W02 | N | 0-1 | 13v2 | Correspondente ao total da soma dos campos id: N43a |  |
| 331.05 | W06e | vICMSMonoRet | Valor total do ICMS Monofásico retido anteriormente | E | W02 | N | 0-1 | 13v2 | Correspondente ao total da soma dos campos id: N45 |  |
| 332 | W07 | vProd | Valor Total dos produtos e serviços | E | W02 | N | 1-1 | 13v2 |  | Gera o valor, conforme consta no campo E140Ipv.VlrBru (soma de todos os itens). |
| 333 | W08 | vFrete | Valor Total do Frete | E | W02 | N | 1-1 | 13v2 |  | Gera o valor, conforme consta no campo E140Nfv.VlrFre. |
| 334 | W09 | vSeg | Valor Total do Seguro | E | W02 | N | 1-1 | 13v2 |  | Gera o valor, conforme consta no campo E140Nfv.VlrSeg. |
| 335 | W10 | vDesc | Valor Total do Desconto | E | W02 | N | 1-1 | 13v2 |  | Gera o valor, conforme consta no campo E140Ipv.VlrDsc (soma de todos os itens). |
| 336 | W11 | vII | Valor Total do II | E | W02 | N | 1-1 | 13v2 |  | Gera o valor, conforme consta no campo E140Nfv.VlrIim. |
| 337 | W12 | vIPI | Valor Total do IPI | E | W02 | N | 1-1 | 13v2 |  | Gera o valor, conforme consta no campo E140Nfv.VlrIpi. |
| 337.01 | W12a | vIPIDevol | Valor Total do IPI devolvido | E | W02 | N | 1-1 | 13v2 | Deve ser informado quando preenchido o Grupo Tributos Devolvidos na emissão de nota finNFe = 4 (devolução) nas operações com não contribuintes do IPI. Corresponde ao total da soma dos campos id:UA04 (incluído na NT 2016.002) | Gera o valor, conforme consta no campo E140Tnf.IcmVde. |
| 338 | W13 | vPIS | Valor do PIS | E | W02 | N | 1-1 | 13v2 |  | Gera o valor conforme consta no campo E140Nfv.VlrPif |
| 339 | W14 | vCOFINS | Valor da COFINS | E | W02 | N | 1-1 | 13V2 |  | Gera o valor, conforme consta no campo E140Nfv.VlrCff. |
| 340 | W15 | vOutro | Outras Despesas acessórias | E | W02 | N | 1-1 | 13v2 |  | Gera o valor, conforme a soma dos campos E140Nfv.VlrEmb + E140Nfv.VlrEnc + E140Nfv.VlrOut + E140Nfv.VlrOui. |
| 341 | W16 | vNF | Valor Total da NF-e | E | W02 | N | 1-1 | 13v2 | Vide validação para esse campo na regra de validação "W16-xx" | Gera o valor, conforme consta no campo E140Nfv.VlrLic. |
| 341a | W16a | vTotTrib | Valor aproximado total de tributos federais, estaduais e municipais | E | W02 | N | 0-1 | 13v2 | (NT 2013/003) | Gera o valor, conforme consta no campo E140Nfv.VlrTot. |
