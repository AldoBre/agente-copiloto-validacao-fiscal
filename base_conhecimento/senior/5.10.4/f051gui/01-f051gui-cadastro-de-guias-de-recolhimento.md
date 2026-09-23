# F051GUI - Cadastro de Guias de Recolhimento

> **Fonte:** F051GUI - Cadastro de Guias de Recolhimento — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f051gui.htm  
> **Trilha:** Ajuda por telas > Cadastros > Controladoria > Tributos  
> **Telas citadas:** E660IDE, E660NFC, E661GRI, F051GUI, F055PPF  
> **Identificadores de regras:** —

---
Ajuda por telas > Cadastros > Controladoria > Tributos > Guias de Recolhimento

Nesta tela é possível cadastrar guias por estado para todos os tipos de impostos. Lembrando que a guia deve estar ligada ao imposto na tela F055PPF.

## Campos

Guia de Recolhimento

Indica qual o código da guia de recolhimento cadastrada até 4 (quatro) posições. Ao clicar no "botão" de pesquisa de registro, associado a este campo, serão
demonstradas na tela de pesquisa de registro, somente as guias de recolhimento cadastradas
na empresa ativa.

Descrição

Permite cadastrar uma descrição para a Guia de Recolhimento que está sendo
cadastrada, campo obrigatório.

Abreviatura

Permite cadastrar uma abreviatura para a Guia de Recolhimento que está sendo cadastrada
ou alterada.

Estado

Indica qual o estado da Guia de Recolhimento.

Código Fiscal

Indica qual o código fiscal da Guia de Recolhimento, podendo ser o mesmo código fiscal
do imposto.

Documento de Arrecadação

Indica qual o código de arrecadação da Guia de Recolhimento, sendo que deverá
ser o mesmo código do imposto informado na tela F055PPF, para que ao efetuar a ligação da guia de
recolhimento no imposto, não ocorram divergências.

Grupo de Tributo

Indica o grupo de tributos que será utilizado na geração da DCTF (Declaração de Débitos e Créditos Tributários Federais) e pode ser preenchido com as seguintes opções: 01 – IRPJ, 02 – IRRF, 03 – IPI, 04 – IOF, 05 – CSLL, 06 - PIS/PASEP, 07 – COFINS, 08 – CPMF, 09 – CIDE, 10 - RET/Pagamento unificado de tributos, 11 – CSRF, 12 – COSIRF ou 13 – CPSSS.

Código Detalhamento

Indica o código do detalhamento da receita.

Informar em arquivos eletrônicos

Indica se a Guia de Recolhimento deve ser gerada em arquivos magnéticos. É preciso que este esteja "S" - Sim, para geração das informações em
arquivos magnéticos, como por exemplo: SINTEGRA. Caso este campo esteja em branco, será considerado como a opção "N" - Não.

Tipo Guia Recolhimento

Informar um dos itens da lista abaixo, conforme necessidade da guia de recolhimento cadastrada:

1 - Darf;  
2 - Darf Simples;  
3 - GPS;  
4 - DARJ;  
5 - Licenciamento;  
6 - DPVAT;  
7 - Gare-SP ICMS;  
8 - Gare-SP DR;  
9 - Gare-SP ITCMD;  
10 - IPTU;  
11 - FGTS;  
12 - DAR;  
13 - GRU - Guia de Recolhimento da União;  
14 - GNRE.

**Observação**

O item 14 influencia diretamente no SPED Fiscal, na geração do registro C180. Se o cliente tiver uma guia vinculada à Nota Fiscal de entrada e a guia for do tipo **14 - GNRE**, o campo 10 do registro (**COD\_DA**) será gerado como **1**. Caso contrário, será **0**.

Modelo para Impressão

Informar um modelo de relatório para a impressão da Guia de Recolhimento, que
pode ser escolhido conforme o tipo de imposto que se deseja imprimir. Ex.: Modelo
"015.GER" - GNRE (Totalmente Impresso).  
Ao gerar a Guia de Recolhimento, poderá ser gerado o modelo através do Botão
Imprimir da própria tela de guia.

Origem

Informar o código da origem para a guia de recolhimento. As informações desses campos serão utilizadas principalmente no preenchido do
registro "33 - Discriminação dos Pagamentos do Imposto e dos Débitos Específicos
- Quadro 12" da DIME.

Código de Identificação de Débito

Informar o código de identificação do Débito. As informações desse campo serão utilizadas para preenchimento das seguintes declarações:

SPED Fiscal

* Para o estado de Santa Catarina: quando este campo possuir informações, o sistema irá concatenar a informação de Cód. Arrec. da tela F055PPF com o campo Código de Identificação do Débito desta tela para preenchimento do campo 05 dos registros E116, E250, E316;
* Para o estado do Rio de Janeiro: quando este campo possuir informações, o Sistema irá concatenar a informação do campo Código de Identificação do Débito com o campo Cód. Arrec. da tela F055PPF para preenchimento do campo 05 dos registros E116, E250, E316.

Código Dispositivo Fiscal

Código do dispositivo fiscal para justificar o valor a recolher na geração do arquivo do SPED Fiscal.

**Situação**

Indica qual a situação da Guia de Recolhimento, se ativa ou inativa. Para ser possível efetuar sua geração, a situação tem que estar A -
Ativo. Caso este campo esteja em branco, será considerado como a opção "N" -
Não.

Não será permitida a alteração da situação da guia
de recolhimento para "I - Inativa", quando a mesma já estiver informada em algum
imposto na tela F055PPF ou
quando já tenha algum lançamento de guia manualmente.

Detalhamento por produto da GNRE

Indica se haverá detalhamento do código do produto na geração da guia de recolhimento.

Número do Convênio

No momento da geração da guia de recolhimento, o Número do Convênio será sugerido com base no número informado no cadastro.

**Tipo Documento GNRE**

Indicação do tipo de documento na geração da GNRE:

* 1 - NOTA FISCAL AVULSA;
* 4 - DI - DECLARAÇÃO DE IMPORTAÇÃO;
* 6 - DSI - DECLARAÇÃO SIMPLIFICADA DE IMPORTAÇÃO;
* 7 - CONHECIMENTO DE TRANSPORTE RODOVIÁRIO;
* 8 - CONHECIMENTO DE TRANSPORTE AÉREO;
* 10 - NOTA FISCAL;
* 18 - DIRE - DECLARAÇÃO DE IMP DE REMESSA EXPRESSA
* 20 - CONHECIMENTO DE TRANSPORTE AQUAVIÁRIO DE CARGAS;
* 21 - CONHECIMENTO DE TRANSPORTE;
* 22 - CHAVE DA NFe;
* 23 - CHAVE DO CTe/CTe-OS;
* 24 - CHAVE DO DFe;
* 25 - DUIMP - DOCUMENTO ÚNICO DE IMPORTAÇÃO.

Ao gerar as informações na tag **infSenior** da NF-e ou CT-e, se houver um tipo de documento informado neste campo, ele será apresentado nas tags **tipoDocumentoOrigem** e **valorTipoDocumentoOrigem**, conforme abaixo:

| Item da lista | Tag | Conteúdo |
| --- | --- | --- |
| 1 | <documentoOrigem tipo="1">12345</documentoOrigem> | Número da nota fiscal de saída (E661GRI.NumNfv) ou Número da nota fiscal de entrada (E661GRI.NumNfc) |
| 4 | <documentoOrigem tipo="4">12345</documentoOrigem> | Número do documento de importação (E660NFC.NumDoi) |
| 6 | <documentoOrigem tipo="6">12345</documentoOrigem> | Número do documento de importação (E660NFC.NumDoi) |
| 7 | <documentoOrigem tipo="7">12345</documentoOrigem> | Número da nota fiscal de saída (E661GRI.NumNfv) ou Número da nota fiscal de entrada (E661GRI.NumNfc) |
| 8 | <documentoOrigem tipo="8">12345</documentoOrigem> | Número da nota fiscal de saída (E661GRI.NumNfv) ou Número da nota fiscal de entrada (E661GRI.NumNfc) |
| 10 | <documentoOrigem tipo="10">12345</documentoOrigem> | Número da nota fiscal de saída (E661GRI.NumNfv) ou Número da nota fiscal de entrada (E661GRI.NumNfc) |
| 18 | <documentoOrigem tipo="18">12345</documentoOrigem> | Número do documento de importação (E660NFC.NumDoi) |
| 20 | <documentoOrigem tipo="20">12345</documentoOrigem> | Número da nota fiscal de saída (E661GRI.NumNfv) ou Número da nota fiscal de entrada (E661GRI.NumNfc) |
| 21 | <documentoOrigem tipo="21">12345</documentoOrigem> | Número da nota fiscal de saída (E661GRI.NumNfv) ou Número da nota fiscal de entrada (E661GRI.NumNfc) |
| 22 | <documentoOrigem tipo="22">12345</documentoOrigem> | Chave do documento eletrônico (E660NFC.ChvNel ou E660IDE.ChvDoe) |
| 23 | <documentoOrigem tipo="23">12345</documentoOrigem> | Chave do documento eletrônico (E660NFC.ChvNel ou E660IDE.ChvDoe) |
| 24 | <documentoOrigem tipo="24">12345</documentoOrigem> | Chave do documento eletrônico (E660NFC.ChvNel ou E660IDE.ChvDoe) |
| 25 | <documentoOrigem tipo="25">12345</documentoOrigem> | Número do documento de importação (E660NFC.NumDoi) |

**Observação**

O sistema **não calcula** os impostos referentes à tag GNRE para notas de entrada ou notas de saída de devolução (que devolvem notas de entrada), ou seja, a tag GNRE não será gerada para esse tipo de nota. Atualmente não há uma situação em que as opções **4, 6 e 25** possam ser usadas, visto que elas imprimem na tag **valorTipoDocumentoOrigem** o número de documento de importação da nota de entrada, que não gera a tag GNRE.

## Páginas relacionadas

* [Ajuda por telas](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/ajuda-telas.htm)
* [F055PPF](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f055ppf.htm)
