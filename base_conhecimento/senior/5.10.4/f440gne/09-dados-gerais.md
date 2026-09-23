# Dados Gerais

> **Fonte:** F440GNE - Nota Fiscal de Entrada Agrupada — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f440gne.htm  
> **Trilha:** Ajuda por telas > Suprimentos > Gestão de Recebimento > Notas Fiscais de Entrada  
> **Telas citadas:** E001TNS, E020SNF, E024MSG, E028CPG, E031MOE, E059EMB, E066FPG, E073TRA, E095FOR, E095ORM, E140NFC, E400NFC, E440NFC, E460CTR, F000PGS, F001TIT, F008CEP, F009PPE, F020SNF, F070EMP, F070ENT, F070FCA, F070FCP, F095CAD, F095FXS, F113SAF, F460CTR  
> **Identificadores de regras:** CPR-440CONID01

---
Registros gravados na tabela de dados gerais da nota fiscal de compras (E140NFC).

Situação

Situação da nota fiscal.

* 1 - Digitada
* 2 - Fechada
* 3 - Cancelada
* 4 - Documento Fiscal Emitido (saída)

Valor Líquido Informado

Valor total da nota fiscal para consistência com o valor final da nota fiscal calculado pelo sistema. O parâmetro global **DesVlrInf** define se o campo deverá ser desabilitado após o seu preenchimento. O valor padrão o parâmetro global é **N - Não**. Ao defini-lo como **S - Sim**, ele permanecerá desabilitado após informar o valor do campo.  

Ao informar um valor incorreto para o campo, a nota fiscal deverá ser digitada novamente. Em notas fiscais de entrada já processadas com um valor incorreto, será necessário excluir a nota e digitá-la de novo, não sendo possível fechá-la. A verificação do parâmetro global e bloqueio do campo serão feitos apenas se os parâmetros Exige Digitação Valor NFE (F070FCP) e Gravar apenas cabeç. NFE (F070EMP) estiverem, respectivamente, definidos como **S - Sim** e diferente de **S - Sim** e o tipo da nota fiscal de entrada for diferente de 9 - NF Acerto, 10 - NF Acerto (NF Saída) e 10 - Transferências entre Empresas/Filiais.

Fica habilitado apenas se o campo Exige Digitação Valor NFE estiver definido como **S - Sim** na tela F070FCP.

**Importante**

A consistência do campo com base no **Valor Diferença Aceito** definido na tela F070FCP não ocorre para notas fiscais de acerto e transferência (9, 10 e 11). Esse comportamento é o mesmo para todas as telas/processos de geração de nota fiscal de entrada.

Série/Sub Série Legal

Código da série e sub-série legal. A sugestão de informação desse campo ocorre da seguinte forma:

1. Busca na ligação do Fornecedor X Série Nota Fiscal da tela F095FXS, acessada através do menu Cadastros > Clientes e Fornecedores > Fornecedores > Ligações > Fornecedor X Série Nota Fiscal.  
   Se a série legal não estiver preenchida nesta tela, ao gerar a nota o campo respectivo ficará sem preenchimento também.
2. Se não existir, é feita a busca do cadastro da série da tela F020SNF, acessada através do menu Cadastros > Mercado e Suprimentos > Parâmetros Fiscais > Séries Notas Fiscais > Cadastro.

Entrada

Data de entrada da nota fiscal. Exibida mensagem de consistência caso haja uma diferença maior que 10 dias entre a data informada e a data atual.

Emissão

Data de emissão da nota fiscal.

Trans.Prod.

Transação de produtos. Registros gravados na tabela E001TNS e sugeridos a partir da tela  F009PPE.

Trans.Serv.

Transação de serviços.

C.Pagto

Código da condição de pagamento. Registros gravados na tabela E028CPG, cadastrados em  e sugeridos a partir das definições do fornecedor.

Chave NF-e

Chave eletrônica da nota fiscal de entrada. Quando o campo Consistir chave eletrônica da nota fiscal (F070FCP) estiver parametrizado como "S - Sim" e o dispositivo autorizado da nota digitada for Nota Fiscal Eletrônica, o preenchimento deste campo torna-se obrigatório.

Chave da nota fiscal eletrônica gerada pelo fornecedor. A validação da chave eletrônica não será efetuada para notas fiscais avulsas, independente do recebimento de pessoas físicas ou jurídicas.

Para que a consistência de documentos fiscais do modelo 66 (NF3-e - Nota Fiscal de Energia Elétrica Eletrônica) seja executada, é necessária a parametrização do campo Dispositivo autorizado como 10 - Nota Fiscal Consumidor Eletrônica no cadastro da série (F020SNF).

Para as NFS-e, a chave eletrônica só será validada se tiver 50 caracteres, pois isso caracteriza uma chave do Padrão Nacional. Caso contrário, a chave não será validada, já que as NFS-e de Prefeitura possuem chaves com tamanhos variados, o que impossibilita a consistência. Atualmente, a única forma de distinguir entre essas duas notas é pelo tamanho da chave. Isso também significa que será permitido deixar a chave eletrônica vazia, diferentemente do que ocorre para outros tipos de nota.

Importante

Mesmo que o parâmetro Consistir chave eletrônica da nota fiscal, nos Parâmetros da Filial para Compras (F070FCP), esteja definido como Sim, a validação não será realizada apenas no campo CNPJ para as notas fiscais avulsas.

Para as NFS-e, quando o número da nota fiscal contiver uma sequência com mais de três dígitos 0, esses zeros serão eliminados antes da comparação com o número digitado.

* Exemplo 1

  Chave de acesso: 31062001225095994000106250000000105725095654697957

  Número extraído da chave: 2500000001057

  Como há uma sequência de 7 zeros, eles são eliminados, resultando no número da nota: 251057.
* Exemplo 2

  Chave de acesso: 31062001225095994000106202500099105725095654697957

  Número extraído da chave: 2025000991057

  Como a sequência contém apenas 3 zeros, eles são mantidos, resultando no número da nota: 2025000991057.

Espécie documento

A informação sugerida nesse campo é proveniente do parâmetro Espécie Documento  do cadastro da série (F020SNF) . Outro ponto que serve de sugestão para esse campo é o parâmetro Espécie Documento da tela Definição do Fornecedor (F095CAD). Porém, quando ambos estão preenchidos, prevalece à informação definida no cadastro da série.

Número DFS

Número da nota fiscal eletrônica de serviços. Somente habilitado se a nota estiver em situação "1 - Aberto Total" e se o tipo de dispositivo autorizado para a série de nota fiscal for "8 - Nota Fiscal Eletrônica de Serviço".

## Exemplos de cada tipo para poder sugerir o que fazer com cada documento

O campo Número do Documento Fiscal de Serviço (NumDfs), presente na tabela E400NFC, possui a capacidade de armazenamento de 15 posições. Desta forma, pode-se armazenar o número da nota fiscal de serviço enviado pelas prefeituras.

![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/images/numero-dsf/exemplo-1_thumb_0_48.png)

E no campo Número da Nota Fiscal de Retorno de Serviços p/ Terceiros (NumNfc) pode ser armazenado o número do RPS.

![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/images/numero-dsf/exemplo-2_thumb_0_48.png)

### Exemplo 1

Mesmo contendo o ano antes do número da nota, a numeração possui 15 posições e, desta forma, o campo Número do Documento Fiscal de Serviço (NumDfs) comporta a capacidade deste documento.

![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/images/numero-dsf/exemplo-3_thumb_0_48.png)

### Exemplo 2

O número possui 9 posições, também possibilitando o armazenamento no campo Número do Documento Fiscal de Serviço (NumDfs).

![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/images/numero-dsf/exemplo-4_thumb_0_48.png)

### Exemplo 3

Mesma situação citada no Exemplo 1: possui 15 posições e é possível armazenar no Número do Documento Fiscal de Serviço (NumDfs).

![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/images/numero-dsf/exemplo-5_thumb_0_48.png)

### Exemplo 4

O número do RPS (14350) pode ser atribuído ao campo Número da Nota Fiscal de Retorno de Serviços p/ Terceiros (NumNfc) e o número da nota ao campo Número do Documento Fiscal de Serviço (NumDfs).

![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/images/numero-dsf/exemplo-6_thumb_0_48.png)

### Exemplo 5

O número do documento é 000427244 e o F01 pode ser utilizado como série.

![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/images/numero-dsf/exemplo-7_thumb_0_48.png)

Importante

Nos locais onde era utilizado como base o campo E440NFC.NumNfc, será necessário alterar para E440NFC.NumDfs.

Ver. Doc. Eletrônico

Permite informar a versão do documento eletrônico.

Importante

O ERP (Gestão Empresarial | ERP) não preencherá a informação de versão do documento para as notas fiscais de entrada que já se encontram na base. Para os documentos ainda não fechados, será necessária a digitação da versão de forma manual.

Cód.Tribut.DARF

Código tributário para DARF.

Rateio Peso

Quando esta opção estiver marcada, haverá o rateio dos pesos bruto e líquido para os itens da nota fiscal de entrada. Os valores refletem as somas dos campos correspondentes dos produtos.

Estado Cálculo ICMS

Estado para cálculo do ICMS. Sugerido pelo sistema conforme o estado do fornecedor. Deverá ser informado manualmente quando o estado da transportadora for diferente.

Cidade Remetente 

Código da cidade do remetente da prestação do CT-e. A informação deste campo é considerado no recebimento eletrônico, ao processar o CT-e ou CT-e OS, e gerados nas seguintes tags:

* CT-e: tag <cMun>, subgrupo <enderReme> do grupo <rem>;
* CT-e OS: tag <cMunIni> do grupo <ide>.

Cidade Destinatário

Código da cidade de destino da prestação do CT-e. A informação deste campo é considerado no recebimento eletrônico, ao processar o CT-e ou CT-e OS, e gerados nas seguintes tags:

* CT-e: tag <cMun>, subgrupo <enderReme> do grupo <dest>;
* CT-e OS: tag <cMunFim> do grupo <ide>.

Fornecedor ISS

Código do fornecedor de ISS. Registros gravados na tabela E095FOR. Esse campo é sugerido da parametrização da tela F001TIT. No entanto, se o campo não estiver preenchido nessa rotina, a informação será buscada no cadastro de CEP da tela F008CEP, conforme parametrização do CEP do fornecedor.

Transportadora

Código da transportadora. Registros gravados na tabela E073TRA.

Redespacho

Código da transportadora para redespacho.

Placa/Estado Veículo

Placa e estado do veículo. Sugerido a partir do cadastro da transportadora.

Qtde Embalagem

Quantidade de embalagens.

Embalagem

Código da embalagem. Registros gravados na tabela E059EMB.

Numeração Embalagem

Número da embalagem.

Mensagem - 1 - Mensagem - 2 - Mensagem - 3 - Mensagem - 4  
Código da mensagem 4. Registros gravados na tabela E024MSG e sugeridos a partir do cadastro da transação de produtos.

Peso Bruto/Líquido

Pesos bruto e líquido da nota fiscal.

Forma de Pagamento

Código da forma de pagamento. Registros gravados na tabela E066FPG.

Código Moeda

Código da moeda. Registros gravados na tabela E031MOE.

Valor Cotação

Valor da cotação.

Data Cotação

Data da cotação.

Cotação Fechada

Indicativo se a cotação é fechada. Os quatro campos anteriores são apenas informativos, são herdados da ordem de compra ligada a nota fiscal. Lembrando que a moeda nos dados gerais da ordem de compra também é meramente informativa servindo apenas de sugestão para os itens no momento do digitação.

Na transferência da ordem de compra para nota fiscal de entrada os itens são convertidos para a moeda da empresa baseados exclusivamente nos dados da moeda cadastrados para o respectivo item.

Código Fator Correção

Código da moeda ou índice como fator de correção(financeiro).

Data Fator Correção

Data da cotação da moeda ou índice para o fator de correção(financeiro).

Cliente Recebimento

Código do cliente para recebimento da mercadoria. Código do cliente recebedor da mercadoria industrializada no retorno da remessa para industrialização (operação triangular). Posteriormente, numa nota fiscal de saída do tipo 5 (retorno de industrialização), será verificado se o cliente para o qual está sendo enviado o retorno é o mesmo gravado na nota fiscal de entrada como Cliente Recebimento.  

Se forem iguais, o tratamento do sistema será semelhante a uma nota fiscal de devolução, ou seja, as quantidades devolvidas da nota fiscal de entrada (E440NFC.QTDDEV) serão atualizadas e desta forma o saldo será controlado, impedindo que sejam remetidas ou devolvidas quantidades maiores do que as recebidas.

Contrato

Número do contrato, somente contratos de tipo 10 (financeiro com saldo). Caso o valor total das notas fiscais ultrapasse o valor do contrato será exibida mensagem abortando o processo. Registros gravados na tabela E460CTR.

Pode-se utilizar contratos com fornecedores diferentes do fornecedor da nota fiscal de entrada, quando o campo Forn dif Ctr da tela Contrato de Compra (F460CTR) estiver como **S - Sim**. E quando o campo Herdar bem estiver igual a S - Sim, é herdado o bem principal do contrato e verificado se existem divergências entre o bem principal do contrato e o bem principal do item da nota fiscal de entrada.

Somente podem ser adicionados contratos a Notas Fiscais do tipo **1 - NF Entrada**, **7 - NF Geração Manual** e **8 - NF Frete/Serviços Agregados**. Notas Fiscais de outros tipos não podem ser ligadas a nenhum contrato.

Ident.Único NFE

Identificador único da nota fiscal de entrada. Se o parâmetro global ObrIdeNfv estiver definido como S(sim) a informação será obrigatória. A princípio será sugerido o mesmo número da nota fiscal,
permitindo alterar, porém deverá ser único por fornecedor. O identificador de regras CPR-440CONID01 permite consistir o campo pela regra associada.

Origem Mercadoria

Origem da mercadoria. Registros gravados na tabela E095ORM. Caso haja registros nesta tabela para o fornecedor da nota fiscal, a informação será obrigatória.

Tipo CTe

Código do Tipo do CT-e, sendo eles:

* 0 - CT-e Normal
* 1 - CT-e de Complemento de Valores
* 2 - CT-e de Anulação
* 3 - CT-e Substituto
* 5 - CT-e Simplificado
* 6 - CT-e Simplificado Substituto

Chave CTe Substituído

Chave de acesso do CT-e Substituído.

Safra

Permite informar a safra na geração de uma nota de Entrada. Ela é cadastrada através da tela F113SAF. O campo está disponível com proprietária Agronegócio, assim como o parâmetro global UtiCtrPrd, que também possibilita a habilitação desse campo.

Para atendimento das rotinas específicas do Agronegócio foram criados os parâmetros globais UtiCtrCoo e UtiCtrPrd, na tela Manutenção dos parâmetros globais do sistema (F000PGS). Com a inclusão desses parâmetros, o sistema passa a exigir apenas a existência da liberação das áreas de Mercado e Suprimentos (ou Backoffice, que libera as duas áreas).

Para mais informações acerca da Proprietária, acesse ERP - Proprietária - Onde encontrar informações completas sobre as formas de licenciamento do Gestão Empresarial | ERP

Nº Lote Contábil

Número do lote contábil. Campo meramente informativo, estará sempre desabilitado.

Código Equipamento

Código do equipamento fiscal.

Data de Previsão de Entrega

Data prevista para a entrega dos produtos informados na nota fiscal de entrada.

Data de Prestação do Serviço

Para atender as legislações que consideram o fato gerador do imposto o momento da prestação do serviço, deve-se utilizar este campo. Ex.: recolhimento de ISS pela data de prestação do serviço. A data pode ser menor que a data atual ou a data de entrada da nota fiscal.

## SPED Contribuições

O número do documento fiscal que será enviado é o Número do Documento Fiscal de Serviço (NumDfs).

**Exemplo:** geração de uma nota de serviço com o número 123.456.789.012.345. O valor foi exportado completo no registro A100.

![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/images/numero-dsf/exemplo-9_thumb_0_48.png)

Nº CF

Número do cupom fiscal. Os dois campos anteriores referem-se a dados herdados em devoluções de notas fiscais de saída.

Código da Cidade ISS

Para definir qual código será sugerido, configure o parâmetro **Origem Código Cidade Tributação ISS** na tela F070FCP.

Endereço entrega 

Sequência do endereço de entrega cadastrada na tela Endereço de Entrega (F070ENT). Caso este campo permaneça com zero, é considerado o endereço de entrega informado na tela Cadastro de Filiais (F070FCA).

Observações

Observações da nota fiscal.

## Bloco Importação

Documento Importação

Tipo de documento de importação. Somente habilitado para notas fiscais de tipo 1 e para fornecedor externo.

Número DI

Número do documento de importação.

Data Registro DI

Data de registro do documento de importação.

Local de Desembaraço

Local do desembaraço da mercadoria.

Data Desembaraço

Data do desembaraço da mercadoria.

Estado desembaraço

Sigla da UF onde ocorreu o desembaraço aduaneiro.

Via transp. inter.

Via de transporte internacional informada na DI.

Intermediação Imp.

Forma de importação quanto à intermediação.

Tipo Adq./Encom.

Indicativo do tipo de pessoa do adquirente ou do encomendante ("J - Jurídica" ou "F - Física").

CNPJ/CPF Adq./Encom.

CNPJ/CPF do adquirente ou do encomendante.

UF Adq./Encom.

Sigla da UF do adquirente ou do encomendante.

Data permanência

Este campo é utilizado no cálculo dos impostos federais para produtos importados que atendam o processo de Admissão Temporária.  
Caso o produto da nota fiscal esteja parametrizado com Suspensão Parcial, defina neste campo até que data o produto permaneceu na aduaneira.

Código Exportador

Código do exportador da mercadoria. Os seis campos anteriores somente estarão habilitados se o estado do fornecedor(E095FOR.SIGUFS) for igual a
EX(exterior).

## Bloco Defensivos Agrícolas

Numero do Receituário

Número do receituário.

CPF resp. téc. emis. receituário

CPF do responsável técnico pela emissão do receituário.

## Bloco Guia de Trânsito

Tipo de Guia

Tipo de guia agrícola.

UFGuia

UF de emissão da guia.

Série de Emissão da Guia

Série da emissão da guia.

Nº Guia

Número da guia.

Finalidade NF-e

Finalidade da nota fiscal.

* "1 - Normal"
* "5 - Nota de crédito"
* "6 - Nota de Débito"

**Nota**

O campo Finalidade NF-e somente é habilitado para dispositivo autorizado da série "6 - NFe" (E020SNF.DisAut). Ao informar uma nota de débito ou crédito, o ERP não gerará movimentações de estoque e financeiras. A opção "6 - Nota de Débito" somente está disponível para notas do Tipo NF-e "1 - Entrada Normal" (TipNfe = 1).

Tipo Nota Crédito

Tipo da nota de crédito.

* "01 - Multa e Juros"

Tipo Nota Débito

Tipo da nota de débito.

* "04 - Multa e Juros"
* "06 - Pagamento Antecipado"

## Páginas relacionadas

* [F070FCP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070fcp.htm)
* [F095FXS](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f095fxs.htm)
* [F020SNF](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f020snf.htm)
* [F009PPE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f009ppe.htm)
* [F001TIT](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f001tit.htm)
* [F008CEP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f008cep.htm)
* [Contrato de Compra (F460CTR)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f460ctr.htm)
* [CPR-440CONID01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/cpr_440conid01.htm)
* [F113SAF](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f113saf.htm)
* [Manutenção dos parâmetros globais do sistema (F000PGS)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm)
* [ERP - Proprietária - Onde encontrar informações completas sobre as formas de licenciamento do Gestão Empresarial | ERP](https://suporte.senior.com.br/hc/pt-br/articles/4409365819924-ERP-Proprietária-Onde-encontrar-informações-completas-sobre-as-formas-de-licenciamento-do-Gestão-Empresarial-ERP)
* [recolhimento de ISS pela data de prestação do serviço](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f661pai.htm#Apura%C3%A7%C3%A3o)
* [F070FCP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070fcp.htm#origem-iss)
* [F070ENT](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070ent.htm)
* [F070FCA](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070fca.htm)
* [Admissão Temporária](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/manuais_processos/suprimentos/admissao-temporaria/processo-admissao-temporaria.htm)
* [Suspensão Parcial](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/manuais_processos/suprimentos/admissao-temporaria/processo-admissao-temporaria.htm#suspensao)
