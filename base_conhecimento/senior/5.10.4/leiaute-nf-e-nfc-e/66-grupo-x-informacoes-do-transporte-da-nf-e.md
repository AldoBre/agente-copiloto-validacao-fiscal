# Grupo X - Informações do Transporte da NF-e

> **Fonte:** Leiautes NF-e e NFC-e — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/leiaute-nf-e-nfc-e.htm  
> **Trilha:** Segmentos > Compliance > Documentos Eletrônicos > NF-e | NFC-e (Nota Fiscal Eletrônica) > Nota Fiscal Eletrônica 4.0  
> **Telas citadas:** —  
> **Identificadores de regras:** VEN-140NEDGE01, VEN-140NEDGE02, VEN-140NELAC01

---
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação | Origem |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 356 | X01 | transp | Grupo Informações do Transporte | G | A01 |  | 1-1 |  |  | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 357 | X02 | modFrete | Modalidade do frete | E | X01 | N | 1-1 | 1 | 0=Contratação do Frete por conta do Remetente (CIF); 1=Contratação do Frete por conta do Destinatário (FOB); 2=Contratação do Frete por conta de Terceiros; 3=Transporte Próprio por conta do Remetente; 4=Transporte Próprio por conta do Destinatário; 9=Sem Ocorrência de Transporte (Atualizado na NT2016.002) | O ERP respeita a geração da tag conforme já descrito na documentação de Regras e sugestão de valores. |
| 358 | X03 | transporta | Grupo Transportador | G | X01 |  | 0-1 |  |  | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 359 | X04 | CNPJ | CNPJ do Transportador | CE | X03 | N | 0-1 | 14 | Preencher os zeros não significativos  Se for NF-e de saída (tpNF=1) e Modalidade do Frete <> 0, 1, 2 , 3 ou 4 (id: X02, campo: modFrete), o CNPJ Base (id: X04, campo: CNPJ) ou CPF (id: X05, campo: CPF) do transportador deve ser DIFERENTE do CNPJ Base (id: C02, campo: CNPJ) ou CPF do Remetente (id: C02a, campo: CPF)  **Exceção**: Regra de validação não se aplica quando CNPJ Base ou CPF do emitente for igual ao CNPJ Base ou CPF do destinatário e CFOP é de operação com combustíveis (indComb= 2), conforme Tabela CFOP.  Se for NF-e de entrada (tpNF=0) e Modalidade do Frete <> 0, 1, 2, 3 ou 4 (id: X02, campo: modFrete), o CNPJ Base (id: X04, campo: CNPJ) ou CPF (id: X05, campo: CPF) do transportador deve ser DIFERENTE do CNPJ Base (id: E02, campo: CNPJ) ou CPF do Remetente (id: E03, campo: CPF)  **Exceção**: Regra de validação não se aplica quando CNPJ Base ou CPF do emitente for igual ao CNPJ Base ou CPF do destinatário e CFOP é de operação com combustíveis (indComb= 2), conforme Tabela CFOP.  Lista de CFOPs válidas para operações com combustíveis: 1.651, 1.652, 1.653, 1.657, 1.658, 1.659, 1.660, 1.661, 1.662, 2.651, 2.652, 2.653, 2.657, 2.658, 2.659, 2.660, 2.661, 2.662, 3.667, 5.651, 5.652, 5.654, 5.655, 5.657, 5.658, 5.659, 5.660, 5.661, 5.662, 5.666, 6.651, 6.652, 6.653, 6.654, 6.655, 6.656, 6.657, 6.658, 6.659, 6.660, 6.661, 6.662, 6.666, 6.667, 7.651, 7.654, 7.667. | Gera por padrão o valor do campo E073Tra.CgcCpf. |
| 360 | X05 | CPF | CPF do Transportador | CE | X03 | N | 0-1 | 11 | Gera por padrão o valor do campo E073Tra.CgcCpf. |
| 361 | X06 | xNome | Razão Social ou nome | E | X03 | C | 0-1 | 2 - 60 |  | Gera por padrão o valor do campo E073Tra.NomTra. |
| 362 | X07 | IE | Inscrição Estadual do Transportador | E | X03 | C | 0-1 | 2 - 14 | Informar:  -Inscrição Estadual do transportador contribuinte do ICMS, sem caracteres de formatação (ponto, barra hífen, etc);  -Literal "ISENTO" para transportador isento de inscrição no cadastro de contribuintes ICMS;  -Não informar a tag para não contribuinte do ICMS.  A UF deve ser informada se informado uma IE. (v2.0) | Gera por padrão o valor do campo E073Tra.InsEst. |
| 363 | X08 | xEnder | Endereço Completo | E | X03 | C | 0-1 | 1 - 60 |  | Gera por padrão o valor do campo E073Tra.EndTra. |
| 364 | X09 | xMun | Nome do Município | E | X03 | C | 0-1 | 1 - 60 |  | Gera por padrão o valor do campo E073Tra.CidTra. |
| 365 | X10 | UF | Sigla da UF | E | X03 | C | 0-1 | 2 | A UF deve ser informada se informado uma IE. (v2.0). Informar "EX" para Exterior | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 366 | X11 | retTransp | Grupo Retenção ICMS transporte | G | X01 |  | 0-1 |  |  | Gera por padrão o valor do campo E007Ufs.SigUfs. |
| 367 | X12 | vServ | Valor do Serviço | E | X11 | N | 1-1 | 13v2 |  | Gera por padrão o valor do campo E140Tnf.VlrStr. |
| 368 | X13 | vBCRet | BC da Retenção do ICMS | E | X11 | N | 1-1 | 13v2 |  | Gera por padrão o valor do campo E140Nfv.VlrBif. |
| 369 | X14 | pICMSRet | Alíquota da Retenção | E | X11 | N | 1-1 | 3v2-4 |  | Gera conforme o valor do campo E140Nfv.PerIcf. |
| 370 | X15 | vICMSRet | Valor do ICMS Retido | E | X11 | N | 1-1 | 13v2 |  | Gera por padrão o valor do campo E140Nfv.IcmFre. |
| 371 | X16 | CFOP | CFOP | E | X11 | N | 1-1 | 4 | CFOP de Serviço de Transporte (Seção 8.10 do MOC - Visão Geral) | Gera por padrão o valor do campo E140Tnf.CodCfp. |
| 372 | X17 | cMunFG | Código do município de ocorrência do fato gerador do ICMS do transporte | E | X11 | N | 1-1 | 7 | Utilizar a Tabela do IBGE (Seção 8.2 do MOC - Visão Geral, Tabela de UF, Município e País) | Gera por padrão o valor do campo E140Tnf.CodMfg. |
| 372.1 | X17.1 | -x- | Sequência XML | CG | X01 |  | 0-1 |  | Transporte por Veículo, Vagão ou Balsa | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 373 | X18 | veicTransp | Grupo Veículo Transporte | G | X17.1 |  | 0-1 |  | Informar o veículo trator (v2.0) | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 374 | X19 | placa | Placa do Veículo | E | X18 | C | 1-1 | 7 | Informar em um dos seguintes formatos: XXX9999, XXX999, XX9999 ou XXXX999. Informar a placa em informações complementares quando a placa do veículo tiver lei de formação diversa. (NT 2011/005) | Gera por padrão o valor do campo E07Vei.PlaVei. |
| 375 | X20 | UF | Sigla da UF | E | X18 | C | 1-1 | 2 | Informar "EX" se Exterior | Gera por padrão o valor do campo E073Vei.NrnTrc. |
| 376 | X21 | RNTC | Registro Nacional de Transportador de Carga (ANTT) | E | X18 | C | 0-1 | 1 - 20 |  | Gera por padrão o valor do campo E073Tra.SigUfs. |
| 377 | X22 | reboque | Grupo Reboque | G | X17.1 |  | 0-5 |  | Informar os reboques/Dolly (v2.0) | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 378 | X23 | placa | Placa do Veículo | E | X22 | C | 1-1 | 7 | Informar em um dos seguintes formatos: XXX9999, XXX999, XX9999 ou XXXX999. Informar a placa em informações complementares quando a placa do veículo tiver lei de formação diversa. (NT 2011/005) | Gera por padrão o valor do campo E073Lvv.PlaReb. |
| 379 | X24 | UF | Sigla da UF | E | X22 | C | 1-1 | 2 | Informar "EX" se Exterior | Gera por padrão o valor do campo E073Vei.UfsVei. |
| 380 | X25 | RNTC | Registro Nacional de Transportador de Carga (ANTT) | E | X22 | C | 0-1 | 1 - 20 |  | Gera por padrão o valor do campo E073Vei.NrnTrc. |
| 380a | X25a | vagao | Identificação do vagão | CE | X01 | C | 0-1 | 1 - 20 | (v2.0) | Tag gerada via identificador de regra VEN-140NEDGE01 através da variável VSIntTraVag. |
| 380b | X25b | balsa | Identificação da balsa | CE | X01 | C | 0-1 | 1 - 20 | (v2.0) | Tag gerada via identificador de regra VEN-140NELAC01 através da variável VSIntTraVag. |
| 381 | X26 | vol | Grupo Volumes | G | X01 |  | 0-5000 |  | (NT 2012/003) | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 382 | X27 | qVol | Quantidade de volumes transportados | E | X26 | N | 0-1 | 1 - 15 |  | Gera por padrão o valor do campo E140Emb.QtdEmb. |
| 383 | X28 | esp | Espécie dos volumes transportados | E | X26 | C | 0-1 | 1 - 60 |  | Gera por padrão o valor do campo E059Emb.DesEmb. |
| 384 | X29 | marca | Marca dos volumes transportados | E | X26 | C | 0-1 | 1 - 60 |  | Tag gerada via identificador de regra VEN-140NEDGE02 através da variável VSIntVolMar. |
| 385 | X30 | nVol | Numeração dos volumes transportados | E | X26 | C | 0-1 | 1 - 60 |  | Gera por padrão o valor do campo E140Emb.NumEmb. |
| 386 | X31 | pesoL | Peso Líquido (em kg) | E | X26 | N | 0-1 | 12v3 |  | Gera por padrão o valor do campo E140Emb.PesLiq. |
| 387 | X32 | pesoB | Peso Bruto (em kg) | E | X26 | N | 0-1 | 12v3 |  | Gera por padrão o valor do campo E140Emb.PesBru. |
| 387a | X33 | lacres | Grupo Lacres | G | X26 |  | 0-5000 |  | (NT 2012/003) | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 388 | X34 | nLacre | Número dos Lacres | E | X33 | C | 1-1 | 1 - 60 |  | Tag gerada via identificador de regra VEN-140NELAC01 através da variável VSIntNumLac. |

## Páginas relacionadas

* [Regras e sugestão de valores](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/manuais_processos/mercado/nf-e/regras-e-sugestoes-valores.htm#modalidade_de_frete)
* [VEN-140NEDGE01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_140nedge01.htm)
* [VEN-140NELAC01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_140nelac01.htm)
