# Grupo JA - Detalhamento Específico de Veículos novos

> **Fonte:** Leiautes NF-e e NFC-e — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/leiaute-nf-e-nfc-e.htm  
> **Trilha:** Segmentos > Compliance > Documentos Eletrônicos > NF-e | NFC-e (Nota Fiscal Eletrônica) > Nota Fiscal Eletrônica 4.0  
> **Telas citadas:** —  
> **Identificadores de regras:** VEN-140NEITE01

---
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação | Origem |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 129 | J01 | veicProd | Detalhamento de Veículos novos | CG | I90 |  | 1-1 |  | Informar apenas quando de tratar de veículos novos | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 130 | J02 | tpOp | Tipo da operação | E | J01 | N | 1-1 | 1 | 1 = Venda concessionária; 2 = Faturamento direto para consumidor final; 3 = Venda direta para grandes consumidores (frotista, governo, ...); 0 = Outros. | Tag gerada via identificador de regra VEN-140NEITE01 através da variável VSIntVeiTpo. |
| 131 | J03 | chassi | Chassi do veículo | E | J01 | C | 1-1 | 17 | VIN (código-identificação-veículo) | Tag gerada via identificador de regra VEN-140NEITE01 através da variável VSIntVeiCha. |
| 132 | J04 | cCor | Cor | E | J01 | C | 1-1 | 1 - 4 | Código de cada montadora | Tag gerada via identificador de regra VEN-140NEITE01 através da variável VSIntVeiCco. |
| 133 | J05 | xCor | Descrição da Cor | E | J01 | C | 1-1 | 1 - 40 |  | Tag gerada via identificador de regra VEN-140NEITE01 através da variável VSIntVeiCor. |
| 134 | J06 | pot | Potência Motor (CV) | E | J01 | C | 1-1 | 1 - 4 |  | Tag gerada via identificador de regra VEN-140NEITE01 através da variável VSIntVeiPot. |
| 135 | J07 | cilin | Cilindradas | E | J01 | C | 1-1 | 1 - 4 | Potência máxima do motor do veículo em cavalo vapor (CV). (potência-veículo) | Tag gerada via identificador de regra VEN-140NEITE01 através da variável VSIntVeiCil. |
| 136 | J08 | pesoL | Peso Líquido | E | J01 | C | 1-1 | 9v4 | Em toneladas - 4 casas decimais | Tag gerada via identificador de regra VEN-140NEITE01 através da variável VSIntVeiPel. |
| 137 | J09 | pesoB | Peso Bruto | E | J01 | C | 1-1 | 9v4 | Peso Bruto Total - em toneladas - 4 casas decimais | Tag gerada via identificador de regra VEN-140NEITE01 através da variável VSIntVeiPeb. |
| 138 | J10 | nSerie | Serial (série) | E | J01 | C | 1-1 | 1 - 9 |  | Tag gerada via identificador de regra VEN-140NEITE01 através da variável VSIntVeiNse. |
| 139 | J11 | tpComb | Tipo de combustível | E | J01 | C | 1-1 | 1 - 2 | Utilizar Tabela RENAVAM (v2.0) 01 = Álcool; 2 = Gasolina; 3 = Diesel; (...); 16 = Álcool/Gasolina; 17 = Gasolina/Álcool/GNV; 18 = Gasolina/Elétrico | Tag gerada via identificador de regra VEN-140NEITE01 através da variável VSIntVeiTco. |
| 140 | J12 | nMotor | Número de Motor | E | J01 | C | 1-1 | 1 - 21 |  | Tag gerada via identificador de regra VEN-140NEITE01 através da variável VSIntVeiNmo. |
| 141 | J13 | CMT | Capacidade Máxima de Tração | E | J01 | C | 1-1 | 9v4 | CMT - Capacidade Máxima de Tração - em Toneladas 4 casas decimais (v2.0) | Tag gerada via identificador de regra VEN-140NEITE01 através da variável VSIntVeiCmt. |
| 142 | J14 | dist | Distância entre eixos | E | J01 | C | 1-1 | 1 - 4 |  | Tag gerada via identificador de regra VEN-140NEITE01 através da variável VSIntVeiDie. |
| 144 | J16 | anoMod | Ano Modelo de Fabricação | E | J01 | N | 1-1 | 4 |  | Tag gerada via identificador de regra VEN-140NEITE01 através da variável VSIntVeiAno. |
| 145 | J17 | anoFab | Ano de Fabricação | E | J01 | N | 1-1 | 4 |  | Tag gerada via identificador de regra VEN-140NEITE01 através da variável VSIntVeiFab. |
| 146 | J18 | tpPint | Tipo de Pintura | E | J01 | C | 1-1 | 1 |  | Tag gerada via identificador de regra VEN-140NEITE01 através da variável VSIntVeiTpt. |
| 147 | J19 | tpVeic | Tipo de Veículo | E | J01 | N | 1-1 | 1 - 2 | Utilizar tabela RENAVAM, conforme exemplos abaixo: 02 = CICLOMOTO;03=MOTONETA; 04=MOTOCICLO; 05=TRICICLO; 06=AUTOMÓVEL; 07=MICROÔNIBUS; 08=ÔNIBUS; 10=REBOQUE; 11=SEMIRREBOQUE; 13=CAMINHONETA; 14=CAMINHÃO; 17=C. TRATOR; 22=ESP / ÔNIBUS; 23=MISTO / CAM; 24=CARGA/CAM; ... | Tag gerada via identificador de regra VEN-140NEITE01 através da variável VSIntVeiTip. |
| 148 | J20 | espVeic | Espécie de Veículo | E | J01 | N | 1-1 | 1 | Utilizar tabela RENAVAM 1=PASSAGEIRO; 2=CARGA; 3=MISTO; 4=CORRIDA; 5=TRAÇÃO; 6=ESPECIAL; | Tag gerada via identificador de regra VEN-140NEITE01 através da variável VSIntVeiEsp. |
| 149 | J21 | VIN | Condição do VIN | E | J01 | C | 1-1 | 1 | Informa se o veículo tem VIN (chassi) remarcado. R=Remarcado; N=Normal | Tag gerada via identificador de regra VEN-140NEITE01 através da variável VSIntVeiVin. |
| 150 | J22 | condVeic | Condição do Veículo | E | J01 | N | 1-1 | 1 | 1=Acabado; 2=Inacabado; 3=Semiacabado | Tag gerada via identificador de regra VEN-140NEITE01 através da variável VSIntVeiCon. |
| 151 | J23 | cMod | Código Marca Modelo | E | J01 | N | 1-1 | 1 - 6 | Utilizar tabela RENAVAM | Tag gerada via identificador de regra VEN-140NEITE01 através da variável VSIntVeiCma. |
| 151a | J24 | cCorDENATRAN | Código da Cor | E | J01 | N | 1-1 | 1 - 2 | Segundo as regras de pré-cadastro do DENATRAN (v2.0) 01=AMARELO; 02=AZUL; 03=BEGE; 04=BRANCA; 05=CINZA; 06=DOURADO; 07=GRENÁ; 08=LARANJA; 09=MARROM; 10=PRATA; 11=PRETA; 12=ROSA; 13=ROXA; 14=VERDE; 15=VERMELHA; 16=FANTASIA | Tag gerada via identificador de regra VEN-140NEITE01 através da variável VSIntVeiCcd. |
| 151b | J25 | lota | Capacidade máxima de lotação | E | J01 | N | 1-1 | 1 - 3 | Quantidade máxima permitida de passageiros sentados, inclusive o motorista (v2.0) | Tag gerada via identificador de regra VEN-140NEITE01 através da variável VSIntVeiLtc. |
| 151c | J26 | tpRest | Restrição | E | J01 | N | 1-1 | 1 | 0=Não há; 1=Alienação Fiduciária; 2=Arrendamento Mercantil; 3=reserva de Domínio; 4=Penhora de Veículos; 9=Outras. (v2.0) | Tag gerada via identificador de regra VEN-140NEITE01 através da variável VSIntVeiRes. |
