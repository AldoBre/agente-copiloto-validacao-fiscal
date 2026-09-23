# Variáveis Disponibilizadas:

> **Fonte:** Identificador de Regra — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_140neite01.htm  
> **Trilha:**   
> **Telas citadas:** —  
> **Identificadores de regras:** —

---
| Nome | Tipo | Observações | Retorna Valor |
| VSIntProUtr | ALFA | infNFe - det - prod - uTrib | S |
| VSIntProQtr | NÚMERO | infNFe - det - prod - qTrib | S |
| VSIntProVut | NÚMERO | infNFe - det - prod - vUnTrib | S |
| VSIntCodEnq | ALFA | Código do Enquadramento de IPI | S |
| VSIntCodCli | NÚMERO | Código do cliente | N |
| VSIntCodEmp | NÚMERO | Código da Empresa | N |
| VSIntCodFil | NÚMERO | Código da Filial | N |
| VSIntCodSnf | ALFA | Código da Série da NF | N |
| VSIntNumNfv | NÚMERO | Número da NF | N |
| VSIntSeqIpv | NÚMERO | Sequência do Item na Nota Fiscal do Gestão Empresarial | ERP | N |
| VSIntNroIte | NÚMERO | Número do item na NF-e (infNFe - det - nItem) | N |
| VSIntCodPro | ALFA | Código do produto ou serviço (infNFe - det - prod - cProd) | N |
| VSIntCodDer | ALFA | Código da Derivação do Produto | N |
| VSIntCodMun | NÚMERO | Código do Município de incidência do imposto (infNFe - det - imposto - ISSQN - cMun) | S |
| VSIntProSer | ALFA | Indicativo se é um Produto ou Serviço ("P" ou "S") | N |
| VSIntFilPed | NÚMERO | Código da Filial do Pedido (Referencia ao Campo VSIntProPed) | N |
| VSIntProPed | NÚMERO | Número do Pedido/Ordem de Compra (infNFe - det - prod - xPed) | S |
| VSIntProIpe | NÚMERO | Item do Pedido/Ordem de Compra (infNFe - det - prod - nItemPed) | S |
| VSIntProDes | ALFA | Descrição do produto ou serviço (infNFe - det - prod - xProd) | S |
| VSIntProNcm | ALFA | Código NCM com 8 dígitos ou 2 dígitos gênero (infNFe - det - prod - NCM) | S |
| VSIntProExi | ALFA | Código EX da TIPI (infNFe - det - prod - EXTIPI) | S |
| VSIntProEat | ALFA | GTIN (Global Trade Item Number) da unidade tributável (infNFe - det - prod - cEANTrib). **Observação**: este campo recebe o valor do campo **VSIntProEan**. Caso ele não esteja preenchido, então ele recebe o valor preenchido no campo **VSIntProEat**. | S |
| VSIntImpMbc | ALFA | Modalidade de determinação da BC do ICMS (infNFe - det - imposto - ICMS - modBC) | S |
| VSIntImpBst | ALFA | Modalidade de determinação da BC do ICMS ST (infNFe - det - imposto - ICMS - modBCST) | S |
| VSIntImpPcs | NÚMERO | Percentual do imposto do estado do cálculo do ICMS ST | S |
| VSIntInfAdp | ALFA | Informações Adicionais do Produto (infNFe - det - infAdProd) | S |
| VSIntProCif | ALFA | Código de autorização / registro do CODIF (infNFe - det - prod - comb - CODIF) | S |
| VSIntProTem | NÚMERO | Quantidade de combustível faturada à temperatura ambiente (infNFe - det - prod - comb - qTemp) | S |
| VSIntImpOri | ALFA | Origem da mercadoria (infNFe - det - imposto - ICMSSNXXX - orig) | S |
| VSIntIssCmu | NÚMERO | Código do município de ocorrência do fato gerador do ISSQN (infNFe - det - imposto - ISSQN - cMunFG) | S |
| VSIntPedCli | ALFA | Número do pedido no cliente (infNFe - det - prod - xPed) | S |
| VSIntIpeCli | ALFA | Item do Pedido do cliente (infNFe - det - prod - nItemPed) | S |
| VSIntProEan | ALFA | GTIN (Global Trade Item Number) do produto (infNFe - det - prod - cEAN) | S |
| VSIntImpMdi | NÚMERO | infNFe - det - imposto - ICMS - motDesICMS (só disponível quando CST 40, 41 ou 50) | S |
| VSIntImpVic | NÚMERO | infNFe - det - imposto - ICMS - vICMS (só disponível quando CST 40, 41 ou 50) | S |
| VSIntVeiTpo | ALFA | Bloco JA NF-e - Tipo da operação - infNFe - det - prod - veicProd - tpOp 1=Venda concessionária, 2=Faturamento direto para consumidor final 3=Venda direta para grandes consumidores (frotista, governo, ...) 0=Outros | S |
| VSIntVeiCha | ALFA | Bloco JA NF-e - Chassi do veículo - infNFe - det - prod - veicProd - chassi | S |
| VSIntVeiCco | ALFA | Bloco JA NF-e - Cor - infNFe - det - prod - veicProd - cCor | S |
| VSIntVeiCor | ALFA | Bloco JA NF-e - Descrição da Cor - infNFe - det - prod - veicProd - xCor | S |
| VSIntVeiPot | ALFA | Bloco JA NF-e - Potência Motor (CV) - infNFe - det - prod - veicProd - pot | S |
| VSIntVeiCil | ALFA | Bloco JA NF-e - Cilindradas - infNFe - det - prod - veicProd - cilin | S |
| VSIntVeiPel | ALFA | Bloco JA NF-e - Peso Líquido - infNFe - det - prod - veicProd - pesoL | S |
| VSIntVeiPeb | ALFA | Bloco JA NF-e - Peso Bruto - infNFe - det - prod - veicProd - pesoB | S |
| VSIntVeiNse | ALFA | Bloco JA NF-e - Serial (série) - infNFe - det - prod - veicProd - nSerie | S |
| VSIntVeiTco | ALFA | Bloco JA NF-e - Tipo de combustível - infNFe - det - prod - veicProd - tpComb Utilizar Tabela RENAVAM (v2.0)  01=Álcool, 02=Gasolina, 03=Diesel, (...); 16=Álcool/Gasolina; 17=Gasolina/Álcool/GNV 18=Gasolina/Elétrico | S |
| VSIntVeiNmo | ALFA | Bloco JA NF-e - Número de Motor - infNFe - det - prod - veicProd - nMotor | S |
| VSIntVeiCmt | ALFA | Bloco JA NF-e - Capacidade Máxima de Tração - infNFe - det - prod - veicProd - CMT | S |
| VSIntVeiDie | ALFA | Bloco JA NF-e - Distância entre eixos - infNFe - det - prod - veicProd - dist | S |
| VSIntVeiAno | ALFA | Bloco JA NF-e - Ano Modelo de Fabricação - infNFe - det - prod - veicProd - anoMod | S |
| VSIntVeiFab | ALFA | Bloco JA NF-e - Ano de Fabricação - infNFe - det - prod - veicProd - anoFab | S |
| VSIntVeiTpt | ALFA | Bloco JA NF-e - Tipo de Pintura - infNFe - det - prod - veicProd - tpPint | S |
| VSIntVeiTip | ALFA | Bloco JA NF-e - Tipo de Veículo - infNFe - det - prod - veicProd - tpVeic Utilizar Tabela RENAVAM, conforme exemplos abaixo: 02=CICLOMOTO; 03=MOTONETA; 04=MOTOCICLO; 05=TRICICLO; 06=AUTOMÓVEL; 07=MICROÔNIBUS; 08=ÔNIBUS; 10=REBOQUE; 11=SEMIRREBOQUE; 13=CAMINHONETA; 14=CAMINHÃO; 17=C. TRATOR; 22=ESP / ÔNIBUS; 23=MISTO / CAM; 24=CARGA/CAM... | S |
| VSIntVeiEsp | ALFA | Bloco JA NF-e - Espécie de Veículo - infNFe - det - prod - veicProd - espVeic Utilizar Tabela RENAVAM  1=PASSAGEIRO; 2=CARGA; 3=MISTO; 4=CORRIDA; 5=TRAÇÃO; 6=ESPECIAL; | S |
| VSIntVeiVin | ALFA | Bloco JA NF-e - Condição do VIN - infNFe - det - prod - veicProd - VIN Informa-se o veículo tem VIN (chassi) remarcado. R=Remarcado; N=Normal | S |
| VSIntVeiCon | ALFA | Bloco JA NF-e - Condição do Veículo - infNFe - det - prod - veicProd - condVeic 1=Acabado; 2=Inacabado; 3=Semiacabado | S |
| VSIntVeiCma | ALFA | Bloco JA NF-e - Código Marca Modelo - infNFe - det - prod - veicProd - cMod | S |
| VSIntVeiCcd | ALFA | Bloco JA NF-e - Código da Cor - infNFe - det - prod - veicProd - cCorDENATRAN Segundo as regras de pré-cadastro do DENATRAN (v2.0) 01=AMARELO, 02=AZUL, 03=BEGE, 04=BRANCA, 05=CINZA, 06=-DOURADA, 07=GRENÁ, 08=LARANJA, 09=MARROM, 10=PRATA, 11=PRETA, 12=ROSA, 13=ROXA, 14=VERDE, 15=VERMELHA, 16=FANTASIA | S |
| VSIntVeiLtc | ALFA | Bloco JA NF-e - Capacidade máxima de lotação - infNFe - det - prod - veicProd - lota | S |
| VSIntVeiRes | ALFA | Bloco JA NF-e - Restrição - infNFe - det - prod - veicProd - tpRest 0=Não há; 1=Alienação Fiduciária; 2=Arrendamento Mercantil; 3=Reserva de Domínio; 4=Penhor de Veículos; 9=Outras. (v2.0) | S |
| VSIntIndEsc | ALFA | Permite alterar o valor da tag indEscala (Indicador de Produção em Escala Relevante). Valores: S - Sim, N - Não. | S |
| VSIntCgcFab | ALFA | Permite alterar o valor da tag CNPJFab (CNPJ do Fabricante da Mercadoria). | S |
| VSIntImpCst | ALFA | CST do item da nota fiscal | N |
| VSIntProAnp | ALFA | Código ANP do item de produto da nota fiscal | N |
| VSIntProBar | ALFA | Código de barras diferente do padrão GTIN - infNFe - det - prod - cBarra | S |
| VSIntProBat | ALFA | Código de Barras da unidade tributável que seja diferente do padrão GTIN - infNFe - det - prod - cBarraTrib | S |
| VSIntImpBsr | NÚMERO | Valor base de ICMS ST destacado do item da nota fiscal retido na UF do remetente (Retorna valor quando a CST for 60 e produto se enquadrar nos códigos da ANP para gerar o grupo ICMSST) | S |
| VSIntImpIsr | NÚMERO | Valor de ICMS ST destacado do item da nota fiscal retido na UF do remetente (Retorna valor quando a CST for 60 e produto se enquadrar nos códigos da ANP para gerar o grupo ICMSST) | S |
| VSIntImpBsd | NÚMERO | Valor base de ICMS ST da UF de destino (Retorna valor quando a CST for 60 e produto se enquadrar nos códigos da ANP para gerar o grupo ICMSST) | S |
| VSIntImpVsd | NÚMERO | Valor de ICMS ST da UF de destino (Retorna valor quando a CST for 60 e produto se enquadrar nos códigos da ANP para gerar o grupo ICMSST) | S |
| VSIntMarLuc | NÚMERO | Valor da margem de lucro - pMVAST | S |
| VSIntImpRbc | NÚMERO | Percentual da Redução de Base de Cálculo - pRedBC | S |
| VsIntTotAst | NÚMERO | Alíquota suportada pelo Consumidor Final | S |
| VSIntVicSub | NÚMERO | Valor do ICMS Substituto | S |
| VSIntMedPmc | NÚMERO | Permite alterar o valor da tag vPMC (infNFe - det - prod - med - vPMC) -Preço Máximo Consumidor | S |
| VenNBicmStd | NÚMERO | Valor base de ICMS ST destacado do item da nota fiscal retido na UF do remetente (retorna valor quando a CST for 60). Este campo irá carregar na tag ICMS60. O valor definido para esta variável vai alimentar a tag vBCSTRet no .XML da nota de saída. | S |
| VenNVicmStd | NÚMERO | Valor de ICMS ST destacado do item da nota fiscal retido na UF do remetente (retorna valor quando a CST for 60). Este campo irá carregar na tag ICMS60. O valor definido para esta variável vai alimentar a tag vICMSSTRet. no .XML da nota de saída. | S |
