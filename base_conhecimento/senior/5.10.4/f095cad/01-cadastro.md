# Cadastro

> **Fonte:** F095CAD - Cadastro de Fornecedores — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f095cad.htm  
> **Trilha:** Ajuda por telas > Cadastros > Clientes e Fornecedores > Fornecedores  
> **Telas citadas:** E070FIL, F000PGS, F040IRF, F051FCI, F085CAD, F085COP, F095CAD, F095CBO, F095SEL, F410CAF, F410PCT  
> **Identificadores de regras:** —

---
Fantasia

Nome de fantasia.

Tipo Fornecedor

Informe o tipo do fornecedor estabelecido.

Tipo Mercado

Em tipo mercado, indique entre as opções "I - Interno (Nacional)", "E - Externo (Exterior)" ou "P - Prospect".

Tipo Empresa

Indique o tipo de empresa a ser cadastrada.

Tipo Direito Propriedade

Indica o tipo do direito da propriedade, Privada ou Pública.

CNPJ/CPF

CNPJ ou CPF.

> Importante
>
> Não é possível alterar esse campo quando a empresa utilizar proprietária e módulo de Varejo EM.

**Importante**

Em algumas telas, pode ocorrer temporariamente a exibição dos campos CPF/CNPJ atual e CPF/CNPJ Alfanumérico de forma duplicada. Esse comportamento é decorrente de um ajuste dinâmico da interface, controlado pelo parâmetro global HabDocIde (F000PGS), que deve ser utilizado apenas para validações de customizações em ambiente de homologação, não sendo recomendado alterá-lo em produção.

Durante operações de cadastro, alteração ou consulta, o sistema exibirá apenas o campo de CPF/CNPJ conforme a parametrização vigente. Esse é um comportamento temporário, relacionado à migração para o CNPJ alfanumérico, de caráter apenas visual e sem impacto na operação do sistema.

RG

Número do RG.

Ramo Atividade

Código do ramo de atividade.

Inscrição Estadual

Inscrição estadual.

Importante

* A biblioteca de validação da Inscrição Estadual (arquivo dllie32.dll) é carregada sempre a partir do local de instalação do produto Gestão Empresarial | ERP dentro do diretório Sapiens. Em caso de execução a partir da DLL de integração do produto Gestão Empresarial (ISapiensDll.dll) com o produto Gestão de Pessoas | HCM, a carga dessa biblioteca é feita a partir do caminho de compartilhamento de rede da instalação do produto Gestão Empresarial, no formato UNC (Uniform Naming Convention), que apresenta a seguinte convenção para acesso a um caminho de rede compartilhado: nome do computador\nome do compartilhamento\diretório
* A instalação do produto Gestão Empresarial | ERP é uma instalação parte estação, ou seja, o arquivo DLL será obtido localmente
* Caso seja utilizado somente um atalho para o Sapiens.exe apontando para um caminho de rede \\servidor\senior\sapiens\sapiens.exe, é necessário copiar a DLL para a unidade local da máquina. Do contrário, haverá problemas no cadastro dos Clientes e Fornecedores
* A orientação referente à DLLIE32.DLL descrita acima se aplica para esta tela ou para qualquer outra rotina que faça utilização da DLL

**Importante**

Não é permitido informar o caractere barra (/), no campo Inscrição Estadual.

Inscrição Municipal

Inscrição municipal.

Grupo Empresa

Código do grupo de empresas.

Suframa

Código na Suframa.

Marca

Marca do fornecedor.

Código do Endereço

Código do endereço.

CEP

Informe o CEP.

Endereço

Informe o endereço.

Número do Endereço

Número numérico de localização.

Complemento

Complemento do endereço.

Bairro

Bairro.

Zip Code

Código da cidade do fornecedor externo.

Cidade

Cidade.

Estado

Estado.

Código País

Código do país.

Telefones

Telefones.

FAX

FAX.

Caixa Postal

Número da caixa postal.

E-Mail

Endereço de e-mail.

E-Mail para documentos eletrônicos

Este campo não é utilizado em nenhuma rotina específica do módulo de Suprimentos. O campo existe para manter a compatibilidade entre o registro do cliente e fornecedor, já que este mesmo campo existe no cadastro do cliente (F085CAD).

Dessa forma, nos casos onde existe a ligação entre cliente e fornecedor, quando o e-mail do cliente ou do fornecedor forem alterados e for solicitado para atualizar o registro do cliente/fornecedor ligado, este campo também recebe a mesma informação.

Nome Vendedor

Nome do vendedor ou representante autorizado.

Telefone/Ramal Vendedor

Telefone e ramal do vendedor ou representante.

Fax Vendedor

Fax do vendedor ou representante.

Rota ou Localidade

Rota ou localidade e sequência.

Sub Rota

Código sub rota.

Fornecedor como Cliente

Código do fornecedor como cliente. Para utiá-lo, faça as verificações abaixo:

* Primeiro passar pelo campo **CNPJ/CPF** para que o sistema faça as devidas validações e habilite ou não o campo
* Caso não habilite, é necessário verificar no Cadastro da Filial se a filial logada está com o campo **Indicativo se os códigos de cliente e fornecedor são iguais** igual a **N - Não**. (E070FIL.VENCFI = N)

Cliente e/ou Fornecedor

Indicativo se o registro representa um cliente, um fornecedor ou ambos.

Fornecedor como Representante

Código do fornecedor como representante.

Fornecedor como Transportadora

Código do fornecedor como transportadora.

Gera dados DIRF

Indicativo se devem ser exportados os dados do fornecedor para DIRF.

Código Tributação /p DARF

Código de tributação para emissão de DARF/DIRF.

Tributa ISS

Indicativo se o fornecedor tributa ISS.

Quantidade Dependentes

Quantidade de dependentes do fornecedor.

Situação

Indicativo de situação do fornecedor.

Recupera IPI

Indicativo se as notas fiscais poderão ter recuperação de IPI.

Recupera ICMS

Indicativo se as notas fiscais poderão ter recuperação de ICMS.

Recupera PIS

Indicativo se as notas fiscais poderão ter recuperação de PIS.

% Recuperação PIS Diferenciado

Percentual de PIS diferenciado.

Recupera Cofins

Indicativo se as notas fiscais poderão ter recuperação de Cofins.

% Recuperação Cofins Diferenciado

Percentual de Cofins diferenciado.

Retenção Cofins

Indicativo se as notas fiscais poderão ter retenção de Cofins.

Retenção CSLL

Indicativo se as notas fiscais poderão ter retenção de CSLL.

Retenção PIS

Indicativo se as notas fiscais poderão ter retenção de PIS.

Out.Ret.

Indicativo se as notas fiscais poderão ter retenção de Outras Retenções.

Retenção IRRF

Indicativo se as notas fiscais ou títulos poderão ter retenção de IRRF.

No caso de fornecedor pessoa física, cujo o percentual de IRRF não pode ser informado na nota fiscal, é verificado a tabela progressiva cadastrada na tela Tabelas de Imposto de Renda (F040IRF). Para que a retenção ocorra corretamente, independente do título ser gerado via nota ou manual, este parâmetro deve estar com o valor S - Sim.

Observação

Caso este parâmetro esteja definido como S - Sim e as demais configurações de retenção de IR não estejam preenchidas, será exibida a seguinte mensagem de confirmação:

"O percentual de IRRF não foi informado na tela Cadastros > Clientes e Fornecedores > Fornecedores > Cadastro (F095CAD). O Imposto de Renda não será gerado. Cancelar o processo?"

Retenção por Produto

Indicativo se o fornecedor controle retenção de PIS, COFINS, CSLL e Outras
Retenções por Produto.

Utiliza Limite Retenção

Indicativo de como é utilizado o valor limite para cálculos de retenção para o fornecedor nas notas fiscais de entrada, sendo possível parametrizá-lo com as opções abaixo:

* **P - Produto:** apenas será verificado o limite em NF-e de produto
* **E - Serviço:** apenas será verificado o limite em NF-e de serviço
* **S - Ambos:** verifica o limite em todas as notas fiscais de entrada
* **N - Não utiliza:** não verifica o limite

Observação

* O controle de retenção tem como base os dados gerais da Nota Fiscal de entrada. Desta forma, caso uma Nota Fiscal contemplar tanto produto como serviço, será realizado o mesmo comportamento da opção **S - Ambos**, independente se o parâmetro estiver definido como **P - Produto** ou **E - Serviço**, pois não há possibilidade de tratar produto e serviço de maneira diferenciada dentro da mesma Nota Fiscal
* Quando esse parâmetro estiver definido diferente de **N - Não utiliza**, o cálculo de controle de retenção de IRRF é influenciado

Tributa IPI

Indicativo se o fornecedor tem tributação de IPI.

Tributa ICMS

Indicativo se o fornecedor tem tributação de ICMS.

Motivo Situação

Código do motivo da situação do fornecedor.

Observação Motivo

Observação do motivo.

Identidade do Fornecedor

Código para identificação do fornecedor.

Código da instalação

Código da instalação conforme
cadastro da ANP.

Observação

Esse campo estará habilitado apenas se a opção **Código da instalação** na tela F095SEL estiver
desmarcada.

Cooperado

Este campo serve para definir se o Cliente/Fornecedor é cooperado. Não será possível alterar o parâmetro se existir um cooperado
ativo cadastrado para o cliente/fornecedor na tela Informações do Cooperado (F085COP).

Ao realizar o cadastro de um o cliente/fornecedor na tela de Informações do Cooperado (F085COP) e informar a Situação Ativo, este campo será atualizado para Sim. Ao informar a situação Em análise, Recusado ou Desligado, o campo será preenchido automaticamente com Não.

Código do Regime Tributário

Definição do código do Regime Tributário com as seguintes opções:

* "1 - Simples Nacional"
* "2 - Simples Nacional - excesso de sublimite de receita bruta"
* "3 - Regime Normal"
* "4 - Simples Nacional - Microempreendedor Individual - MEI"

Regime Especial de Tributação

Definição do código de regime especial de tributação.

## Opções

* 1 - Microempresa municipal
* 2 - Estimativa
* 3 - Sociedade de profissionais
* 4 - Cooperativa
* 5 - Microempresário Individual (MEI)
* 6 - Microempresário e Empresa de Pequeno Porte (ME EPP)
* 7 – Tributação por Faturamento (Variável)
* 8 – Fixo
* 9 – Isenção
* 10 – Imune
* 11 - Exigibilidade suspensa por decisão judicial
* 12 - Exigibilidade suspensa por procedimento administrativo

Observação

As rotinas de entradas, saídas, apuração e obrigações acessórias foram atualizadas para aplicar ao regime "4 - Simples Nacional - Microempreendedor Individual - MEI", o mesmo tratamento do regime "1 - Simples Nacional".

CPF do Micro Empreendedor Ind.

Utilizado na exportação dos arquivos do eSocial e MANAD.

%ICMS

Utilizado na sugestão do percentual de ICMS de notas fiscais de entrada
de fornecedores, com o regime tributário simples nacional. Este campo
somente estará habilitado para digitação se o parâmetro **Recupera ICMS**
estiver preenchido como **S-Sim** e o parâmetro **Regime Tributário** como
**1** ou **2 (Simples Nacional)**.

Identificação Fiscal

Neste campo deve-se indicar se o beneficiário possui o NIF ou é dispensado, ou se o país-objeto não exige o NIF. Essa informação é exportada para a Senior X para atender o Siscoserv. O NIF se refere ao Número de Identificação Fiscal das empresas residentes e domiciliadas no Exterior, que atuam como prestadoras ou tomadoras de serviços, intangíveis ou outras operações, em relação à uma parte residente e domiciliada no Brasil.

No site da OECD é possível consultar os países que possuem NIF.

Número Identificação Fiscal

Deve ser informado o Número de Identificação Fiscal quando o campo Identificação Fiscal for 1 - Beneficiário com NIF ou 2 - Beneficiário dispensado do NIF.

Percentual Deságio

Visível
apenas com proprietária agronegócio.  
Permite cadastrar o percentual (%) de deságio para pagamento do crédito do ICMS.

Permite Redução Base IRRF

Este campo é habilitado apenas se o fornecedor for do tipo Pessoa Física.

Entidade PAA

Indique se a entidade está inscrita no Programa de Aquisição de Alimentos.

Data do Laudo

Utilizado por portadores de moléstia.

Fonte Pagadora

Informe a fonte pagadora/beneficiário que será utilizada no registro **BRPDE** (Beneficiário dos rendimentos pagos a residentes ou domiciliados no exterior) ao gerar o arquivo da DIRF. São exibidas para seleção as opções de acordo com o anexo II do leiaute da DIRF, disponibilizado pela Receita Federal.

Órgão Emissor RG

Órgão expedidor do documento, quando pessoa física.

Data Expedição

Data da expedição do documento.

Data Nascimento Fornecedor

Data de nascimento do fornecedor pessoa física.

Número CBO

Número da classificação brasileira de ocupações, conforme cadastrado na tela F095CBO.

Categoria RPA

Categoria do recibo de pagamento autônomo. Para mais informações, verifique as documentações RPA - Parametrização, RPA - Recibo Pagamento Autônomo e RPA - Controladoria.

Número de Inscrição do Segurado

Número de Inscrição do Segurado - NIS, NIT e PIS/PASEP.

Fornecedor Assistência Técnica

Indicativo se é um fornecedor de assistência técnica.

Fornecedor é aposentado

Indica se o fornecedor é aposentado ou não. Caso a definição do campo seja **S - Sim**, o fornecedor recebe dedução do valor correspondente a primeira faixa de alíquota do imposto de renda no valor da base de IRRF. Essa dedução é concedida apenas uma vez por mês, ou seja, quando o fornecedor possuir duas ou mais notas no mesmo mês, a dedução será abatida do somatório total das notas.

Importante

Esse campo somente é habilitado quando o Tipo do Fornecedor é igual a **F - Pessoa Física**.

Tipo de desconto IRRF

Tipo de desconto de base de IRRF que será aplicado no recebimento de notas fiscais e nas baixas de título.  
Opções:

* "1 - Deduções Legais": Leva em consideração as deduções legais Pensão judicial, dependentes e desconto para aposentados.
* "2 - Simplificada": Leva em consideração o valor parametrizado na tela F040IRF, no campo Valor de desconto para optantes do tipo de desconto simplificado. Para fins de cálculo do IRRF na baixa do título, será utilizado o valor proporcional de INSS gerado no fechamento da Nota Fiscal condicionado ao proporcional de movimento de baixa dos títulos.
* "3 - Mais vantajosa": Executa os cálculos das opções anteriores e leva em consideração o de melhor valor.

Tipo acerto (arredondamento) previdenciário

Indica como serão acertados os valores dos impostos previdenciários no recebimento de notas fiscais de serviço:

* **Arredonda**: os valores são arredondados em duas casas decimais de acordo com as regras do arredondamento matemático (de 0 a 4 conserva-se o valor da segunda decimal e de 5 a 9 soma-se uma unidade). Exclusivamente para o INSS, se o campo **Utiliza regra de arredondamento ABNT** estiver configurado como **Sim**, será aplicada a regra de arredondamento da ABNT neste valor.
* **Trunca**: trunca os valores em duas casas decimais, sem arredondamento.

Exemplo de valores:

| Produto/Serviço | Valor | INSS (13%) | Apo. Especial (2%) | Funrural (14%) | Gilrat (2%) | Senar (5%) |
| --- | --- | --- | --- | --- | --- | --- |
| 001 | R$ 596,9536 | R$ 77,603968 | R$ 11,939072 | - | - | - |
| 002 | R$ 423,8672 | R$ 55,102736 | R$ 8,477344 | - | - | - |
| 003 | R$ 368,4298 | R$ 47,895874 | R$ 7,368596 | - | - | - |
| 004 | R$ 605,531 | R$ 78,71903 | R$ 12,11062 | - | - | - |
| 101 | R$ 257,4596 | - | - | R$ 36,044344 | R$ 5,149192 | R$ 12,87298 |
| 102 | R$ 325,6321 | - | - | R$ 45,588494 | R$ 6,512642 | R$ 16,281605 |
| 103 | R$ 439,9416 | - | - | R$ 61,591824 | R$ 8,798832 | R$ 21,99708 |

| Produto/Serviço | Truncado | | | | | Arredondado | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| INSS | Apo. Especial | Funrural | Gilrat | Senar | INSS | Apo. Especial | Funrural | Gilrat | Senar |
| 001 | R$ 77,6 | R$ 11,93 | - | - | - | 77,6 | 11,94 | - | - | - |
| 002 | R$ 55,1 | R$ 8,47 | - | - | - | 55,1 | 8,48 | - | - | - |
| 003 | R$ 47,89 | R$ 7,36 | - | - | - | 47,9 | 7,37 | - | - | - |
| 004 | R$ 78,71 | R$ 12,11 | - | - | - | 78,72 | 12,11 | - | - | - |
| 101 | - | - | R$ 36,04 | R$ 5,14 | R$ 12,87 | - | - | 36,04 | 5,15 | 12,87 |
| 102 | - | - | R$ 45,58 | R$ 6,51 | R$ 16,28 | - | - | 45,59 | 6,51 | 16,28 |
| 103 | - | - | R$ 61,59 | R$ 8,79 | R$ 21,99 | - | - | 61,59 | 8,8 | 22 |

Importante

Este parâmetro define apenas o comportamento para impostos previdenciários, não impactando outros valores.

Utiliza regra arredondamento ABNT

Esse parâmetro indica se o sistema deve utilizar a regra de arredondamento da ABNT para arredondar os valores dos itens de serviço (apenas itens de serviços) dos pedidos, notas fiscais de saída, ordens de compra e notas fiscais de entrada. Quando o parâmetro estiver ativo, são arredondados os seguintes valores dos itens de serviço: Valor Bruto, PIS Retido, COFINS Retido, CSLL, Outras Retenções, INSS, IRRF e ISS.

A regra de arredondamento ABNT é aplicada apenas aos itens de serviço devido à necessidade de integração das notas fiscais de serviço das prefeituras. Para as notas fiscais eletrônicas que possuem itens de produto, a SEFAZ não obriga a utilização da regra ABNT, sendo válido o uso do arredondamento padrão do ERP.

Indicativo da forma de tributação da CP

Esse parâmetro é utilizado durante o processo de emissão da nota fiscal para definição dos cálculos previdenciários e composição das informações enviadas no evento R-2055 da EFD-Reinf.

Ele serve para indicar a forma de tributação da Contribuição Previdenciária do produtor rural pessoa física para o eSocial. Há duas opções disponíveis:

* **1-Sobre a comercialização da sua produção**

  Quando o produtor rural for optante pela tributação incidente sobre a receita bruta da comercialização da produção rural, o campo deve ser configurado com o valor 1 – Sobre a comercialização da sua produção.  
  Há retenção de Funrural e Gilrat;.  
  O campo indOpcCP não deve ser informado no envio do evento R-2055.
* **2-Sobre a folha de pagamento**

  Quando o produtor rural estiver configurado para realizar o recolhimento do Funrural por meio da folha de pagamento, o campo deve permanecer configurado com o valor 2 – Sobre a folha de pagamento.  
  Não ocorre retenção de Funrural e Gilrat;  
  No envio do evento R-2055, o campo indOpcCP deve ser informado com o valor S.

Código do CAEPF

Este campo permite informar o Cadastro de Atividade Econômica da Pessoa Física, que tem por objetivo guardar informações relativas às atividades econômicas exercidas pela pessoa física.

Observação

O CAEPF, em produção de forma facultativa desde 1º de outubro de 2018, tornou-se obrigatório em 15 de janeiro de 2019. Esse campo é utilizado para envio das informações referente ao produtor rural pessoa física para atender o eSocial.

Cálculo de Desoneração de ICMS

Indica qual fórmula será usada para calcular o ICMS Desonerado e o ICMS Diferido nas notas fiscais de entrada. O valor informado será utilizado no web service de exportação dos movimentos de aquisição da produção rural.

* "0 - Padrão": aplica a fórmula de cálculo padrão do sistema para o ICMS (base de cálculo X % ICMS);
* "1 - Resolução 13/2019 RJ": faz o cálculo do ICMS conforme consta na resolução:

  Para o ICMS **desonerado**, é aplicada a seguinte fórmula: *Preço na Nota Fiscal / (1 - Alíquota) \* Alíquota*, sendo que:  
  Preço da Nota fiscal: base de cálculo do ICMS da operação;  
  Alíquota: Alíquota do ICMS + alíquota do FCP da operação.

  Se o produto possuir redução de base de cálculo, o valor do ICMS desonerado deverá ser: % da Redução de base de cálculo = 1 - Percentual da Base de Cálculo Reduzida, e a fórmula aplicada é *Valor do ICMS desonerado = Preço na Nota Fiscal \* (1 - (Alíquota \* (1 - Percentual de redução da BC))) / (1- Alíquota) - Preço na Nota Fiscal*, sendo que:  
  Percentual da Base de Cálculo Reduzida: percentual de redução de base de cálculo indicado na parametrização da tabela de redução;  
  Preço da Nota fiscal: base de cálculo do ICMS da operação;  
  Alíquota: Alíquota do ICMS + alíquota do FCP da operação.

  Para o ICMS **diferido**, a fórmula é *Valor do ICMS diferido = (Preço na Nota Fiscal / (1 - Alíquota)) \* Alíquota*, onde:  
  Preço da Nota fiscal: base de cálculo do ICMS diferido;  
  Alíquota: percentual do ICMS diferido.

  No caso de diferimento parcial é aplicado o percentual de diferimento, que é o diferimento sobre o valor do imposto.
* "2 - Resolução 79/2022 SC": faz o cálculo do ICMS conforme consta na resolução.

  Seguem os cálculos dos respectivos CSTs. Para os CSTs 30 e 40 de ICMS isento ou não tributado:  
  Preço do produto \* Alíquota.

  Para os CSTs 20 e 70 de redução de ICMS na base de cálculo:  
  (Percentual de redução da BC / (1 - Percentual de redução da BC) \* valor do ICMS.

  CST 50 de suspensão de ICMS:  
  Valor da base de cálculo do ICMS \* Alíquota

  Essa opção foi revogada pelo estado de Santa Catarina e atualmente está em desuso. Recomenda-se o uso da opção "0 - Padrão", que aplica a fórmula de cálculo padrão do sistema para o ICMS (base de cálculo \* % ICMS).

* "2 - Resolução 79/2022 SC": faz o cálculo do ICMS conforme consta na resolução.

  Seguem os cálculos dos respectivos CSTs. Para os CSTs 30 e 40 de ICMS isento ou não tributado:  
  Preço do produto \* Alíquota.

  Para os CSTs 20 e 70 de redução de ICMS na base de cálculo:  
  (Percentual de redução da BC / (1 - Percentual de redução da BC) \* valor do ICMS.

  CST 50 de suspensão de ICMS:  
  Valor da base de cálculo do ICMS \* Alíquota

  CST 51 de suspensão de ICMS:  
  Atenção: O uso do cálculo de desoneração de ICMS tipo 2 em conjunto com a CST 51, pode implicar na busca de valores da tabela de preço de um item de nota fiscal, independente da configuração do Indicativo se deve buscar os percentuais e preço do produto/serviço no faturamento não respeitando o que está no pedido localizado na filial de vendas.

  Essa opção foi revogada pelo estado de Santa Catarina e atualmente está em desuso. Recomenda-se o uso da opção "0 - Padrão", que aplica a fórmula de cálculo padrão do sistema para o ICMS (base de cálculo \* % ICMS).

Informações sobre isenção e imunidade

Serve para detalhar as informações de isenção e imunidade do fornecedor. Necessário para atender o EFD-Reinf.

**Inscrição RENASEM**

Permite informar sua inscrição no Registro Nacional de Sementes e Mudas. Esse campo permite uma inscrição de até 30 caracteres.

**Participante Monsanto?**

Este campo indica que a empresa ou pessoa é um parceiro da empresa Monsanto e que possui um contrato com a mesma. Se parametrizado como Parceiro, significa que na origem do produto já é garantida a fiscalização e o pagamento do royalties à Monsanto, caso esteja comercializando um produto transgênico.

Os valores disponíveis deste campo são:

* **Participante:** apenas variedades que em seu cadastro estejam parametrizadas como **Participante** devem ficar disponíveis para serem selecionadas/utilizadas nas movimentações do fornecedor.

  Quando indicado com valor **Participante Monsanto** será gerada pendência de integração e, integração com o Hub de Royalties.
* **Não participante:** apenas variedades que em seu cadastro estejam parametrizadas como **Não Participante** devem ficar disponíveis para serem selecionadas/utilizadas nas movimentações do fornecedor.

  Os valores **Não participante** e **Não informado** não irão gerar pendência de integração, nem integração com o Hub de Royalties.
* **Não informado:** apenas variedades que em seu cadastro estejam parametrizadas como **Não Informado** devem ficar disponíveis para serem selecionadas/utilizadas nas movimentações do fornecedor.

Forma de Tributação para Rendimentos de Ben. Ext.

Serve para indicar a forma de tributação para rendimentos de beneficiários no exterior. Necessário para atender o EFD-Reinf.

**Calcula CDO**   
Indica o cálculo da cobrança da Taxa de Cooperação e Defesa Orizicultura (Taxa CDO). Esse campo ficará visível na tela somente quando o parâmetro global HabCalCdo estiver com valor S-Sim.

**Nota Avaliação Fornecedor**

Esta nota é a média resultante da soma das notas de avaliação do fornecedor dividida pela quantidade de notas, geradas no processo de cotação das solicitações de compras. Para saber mais, acesse as telas F410CAF e F410PCT.

Categoria do estabelecimento

Utilizado no arquivo SCANC. Este campo possui as seguintes opções:

* ARM - Armazenador
* CFC - Consumidor Final Contribuinte
* CNF - Consumidor Final Não Contribuinte
* CPQ - Central Petroquímica
* DIS - Distribuidor
* ECE - Empresa Comercializadora de Etanol
* FOR - Formulador
* IMP - Importador
* PRV - Posto Varejista
* REF - Refinaria
* TRR - Transportador e Revendedor Retalhista
* USI - Usina
* VGL - Varejista de GLP

Calcula CBS/IBS

Parâmetro utilizado pare definir se calcula ou não CBS/IBS para este fornecedor.

Aplicação da CBS/IBS

Código da aplicação, cadastrado na tela F051FCI.

## Páginas relacionadas

* [HabDocIde](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#HabDocIde)
* [F085CAD](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f085cad.htm)
* [Tabelas de Imposto de Renda (F040IRF)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f040irf.htm)
* [controle de retenção de IRRF](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/processo-geracao-controle-de-retencao-irrf-por-dia.htm)
* [F095SEL](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f095sel.htm)
* [F085COP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f085cop.htm)
* [Siscoserv](https://documentacao.senior.com.br/gestaoempresarialerp/7.0.0/index.htm#compliance/siscoserv/introducao.htm)
* [site da OECD](http://www.oecd.org/tax/automatic-exchange/crs-implementation-and-assistance/tax-identification-numbers)
* [arquivo da DIRF](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_financas/relatorios/financeiros/fpcp072.htm)
* [F095CBO](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f095cbo.htm)
* [RPA - Parametrização](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/manuais_processos/suprimentos/rpa/parametrizacao.htm)
* [RPA - Recibo Pagamento Autônomo](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/manuais_processos/suprimentos/rpa/rpa-recibo-pagamento-autonomo.htm)
* [RPA - Controladoria](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/manuais_processos/suprimentos/rpa/controladoria/rpa-controladoria.htm)
* [HabCalCdo](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#HabCalCdo)
* [F410CAF](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f410caf.htm)
* [F410PCT](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f410pct.htm)
* [SCANC](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f669sca.htm)
* [F051FCI](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f051fci.htm)
