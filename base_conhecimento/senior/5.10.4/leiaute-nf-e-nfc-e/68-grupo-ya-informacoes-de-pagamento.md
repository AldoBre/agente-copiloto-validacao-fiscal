# Grupo YA - Informações de Pagamento

> **Fonte:** Leiautes NF-e e NFC-e — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/leiaute-nf-e-nfc-e.htm  
> **Trilha:** Segmentos > Compliance > Documentos Eletrônicos > NF-e | NFC-e (Nota Fiscal Eletrônica) > Nota Fiscal Eletrônica 4.0  
> **Telas citadas:** —  
> **Identificadores de regras:** VEN-140ALTPG01

---
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação | Origem |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 398.01 | YA01 | pag | Grupo de Informações de Pagamento | G | A01 |  | 1-1 |  | Obrigatório o preenchimento do Grupo Informações de Pagamento para NF-e e NFC-e. Para as notas com finalidade de Ajuste ou Devolução o campo Meio de Pagamento deve ser preenchido com 90=sem Pagamento. | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 398.10 | YA01a | detPag | Grupo Detalhamento do Pagamento | G | YA01 |  | 1-100 |  |  | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 398.11 | YA01b | indPag | Indicador da Forma de Pagamento | E | YA01a | N | 0-1 | 1 | 0=Pagamento à Vista; 1=Pagamento à Prazo (Incluído na NT2016.002) | Gera por padrão o valor do campo E140Par.IndPag. |
| 398.14 | YA02a | xPag | Descrição detalhada da forma de pagamento utilizada no documento fiscal eletrônico. | E | YA01a (detPag – Grupo Detalhamento do Pagamento) | Texto | 0-1 (Opcional, ocorre no máximo uma vez para cada grupo detPag) | Até 60 caracteres | Preenchido apenas se o tipo de pagamento (tPag) for "99-Outros" e houver uma descrição informada | O conteúdo da tag xPag é preenchido a partir do campo DesPag do grupo de pagamento, informado pelo usuário ou proveniente do cadastro de formas de pagamento do sistema. |
| 398.12 | YA02 | tPag | Meio de pagamento | E | YA01a | N | 1-1 | 2 | 01=Dinheiro; 02=Cheque; 03=Cartão de Crédito; 04=Cartão de Débito; 05=Crédito Loja; 10=Vale Alimentação; 11=Vale Refeição; 12=Vale Presente; 13=Vale Combustível; 15=Boleto Bancário; 16=Depósito Bancário; 17=Pagamento Instantâneo (PIX); 18=Transferência Bancária, Carteira digital; 19=Programa de fidelidade, Cashback, Crédito Virtual;23=PIX Automático; 24=TEF - Book Transfer; 90=Sem Pagamento; 91=Pagamento Posterior;99=Outros. (Atualizado na NT2016.002, NT2020.006, NT nº 2025.001, v.1.03) | Gera por padrão utilizando a variável VenATipPag do identificador de regras VEN-140ALTPG01. |
| 398.13 | YA03 | vPag | Valor do Pagamento | E | YA01a | N | 1-1 | 13v2 |  | Caso o tipo de pagamento seja igual a "90" ou "91", a tag é preenchida com valor padrão "0.00". |
| 398.13a | YA03a | dPag | Data do Pagamento | E | YA01a | D | 0-1 |  | Formato: “AAAA-MM-DD” | Gera a tag com a data do pagamento conforme informação do campo Indicativo da forma de pagamento informado na parcela da nota fiscal for Pagamento à Vista. |
| 398.13c | YA03c | CNPJPag | CNPJ transacional do pagamento | E | YA03b | N | 1-1 | 14 | Preencher informando o CNPJ do estabelecimento onde o pagamento foi processado/transacionado/recebido quando a emissão do documento fiscal ocorrer em estabelecimento distinto. | Gera por padrão o valor do campo E140Par.CgcTpp. |
| 398.13d | YA03d | UFPag | UF do CNPJ do estabelecimento onde o pagamento foi processado/transacionado/recebido | E | YA03b | C | 1-1 | 2 | UF do CNPJ do estabelecimento onde o pagamento foi processado/transacionado/recebido. | Gera por padrão o valor do campo E140Par.UfsPgr. |
| 398.20 | YA04 | card | Grupo de Cartões | G | YA01a |  | 0-1 |  |  | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 398.21 | YA04a | tpIntegra | Tipo de Integração para pagamento | E | YA04 | N | 1-1 | 1 | Tipo de Integração do processo de pagamento com o sistema de automação da empresa:  1=Pagamento integrado com o sistema de automação da empresa (Ex.: equipamento TEF, Comércio Eletrônico);  2=Pagamento não integrado com o sistema de automação da empresa (Ex.: equipamento POS). | Gera por padrão o valor do campo E140Par.TipInt.. |
| 398.22 | YA05 | CNPJ | CNPJ da instituição de pagamento | E | YA04 | C | 0-1 | 14 | Informar o CNPJ da instituição de pagamento, adquirente ou subadquirente. Caso o pagamento seja processado pelo intermediador da transação, informar o CNPJ deste (Atualizado na NT 2020.006) | Gera por padrão o valor do campo E140Par.CgcCre. |
| 398.23 | YA06 | tBand | Bandeira da operadora de cartão de crédito e/ou débito | E | YA04 | N | 0-1 | 2 | 01=Visa; 02=Mastercard; 03=American Express; 04=Sorocred; 05=Diners Club; 06=Elo; 07=Hipercard; 08=Aura; 09=Cabal; 99=Outros (Atualizado na NT2016.002) | Gera por padrão o valor do campo E140Par.BanOpe. |
| 398.24 | YA07 | cAut | Número de autorização da operação com cartões, PIX, boletos e outros pagamentos eletrônicos | E | YA04 | C | 0-1 | 1-128 | Identifica o número da autorização da transação da operação com cartões, PIX, boletos e outros pagamentos eletrônicos | Gera por padrão o valor do campo E140Par.CatTef. |
| 398.24a | YA07a | CNPJReceb | CNPJ do beneficiário do pagamento | E | YA04 | C | 0-1 | 14 | Informar o CNPJ do estabelecimento beneficiário do pagamento | Gera por padrão o valor do campo E140Par.CgcBpr. |
| 398.24b | YA07b | idTermPag | Identificador do terminal de pagamento | E | YA04 | C | 0-1 | 40 | Identificar o terminal em que foi realizado o pagamento | Gera por padrão o valor do campo E140Par.IdeTpg. |
| 398.25 | YA09 | vTroco | Valor do troco | E | YA01 | N | 0-1 | 13v2 | Valor do troco (Incluído na NT2016.002).  A tag será gerada para troco até 300.000,00. | Gera por padrão o valor do campo E140Par.VlrTro. |

## Páginas relacionadas

* [EN-140ALTPG01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_140altpg01.htm)
