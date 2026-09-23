# Cadastro

> **Fonte:** F085CAD - Cadastro de Clientes — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f085cad.htm  
> **Trilha:** Ajuda por telas > Cadastros > Clientes e Fornecedores > Clientes  
> **Telas citadas:** E070FIL, F000PGS, F040IRF, F070VAR, F085CAD, F085COP, F085ENT, F085SEL, F660NFV  
> **Identificadores de regras:** —

---
Fantasia

Nome de fantasia do cliente.

Tipo Cliente

Tipo de cliente.

Tipo Empresa

Tipo de empresa do cliente para geração de título de PIS/COFINS.

Tipo Direito Propriedade

Indica o tipo do direito da propriedade, Privada ou Pública. Quando o campo Retenção IRRF estiver configurado como **S - Sim** no cadastro do cliente, este campo realiza o controle do percentual do IRRF aplicado nas notas fiscais.

CNPJ/CPF

Número do CNPJ ou CPF do cliente, conforme definido no campo Tipo Cliente. Se o campo Tipo Cliente for alterado enquanto o número do CNPJ ou CPF já estiver informado, o campo CNPJ/CPF ficará em branco para que esta informação seja fornecida novamente, de acordo com o novo tipo definido.

Importante

Não é possível alterar esse campo quando a empresa utilizar proprietária e módulo de Varejo EM.

**Importante**

Em algumas telas, pode ocorrer temporariamente a exibição dos campos CPF/CNPJ atual e CPF/CNPJ Alfanumérico de forma duplicada. Esse comportamento é decorrente de um ajuste dinâmico da interface, controlado pelo parâmetro global HabDocIde (F000PGS), que deve ser utilizado apenas para validações de customizações em ambiente de homologação, não sendo recomendado alterá-lo em produção.

Durante operações de cadastro, alteração ou consulta, o sistema exibirá apenas o campo de CPF/CNPJ conforme a parametrização vigente. Esse é um comportamento temporário, relacionado à migração para o CNPJ alfanumérico, de caráter apenas visual e sem impacto na operação do sistema.

Indicativo Núm. Identificação Fiscal

Indicativo do número de identificação fiscal, possui as opções:

1. Beneficiário com NIF;
2. Beneficiário dispensado do NIF;
3. País não exige NIF.

Identificação Fiscal

Número de Identificação Fiscal.

Ramo Atividade

Escolher o ramo de atividade da empresa.

Rota ou Localidade

Selecionar a rota para a chegada da mercadoria.

Sub Rota

Uma segunda opção de Rota.

Cliente Contribuinte de ICMS

Informe "S - Sim" caso o cliente seja contribuinte de ICMS, caso contrário, informe "N - Não".

Observação

Caso seja escolhida a opção "N - Não", o percentual não será apresentado na nota fiscal de saída.

Inscrição Estadual

Informe a Inscrição Estadual do cliente.

Importante

A biblioteca de validação da Inscrição Estadual (arquivo dllie32.dll) é carregada sempre a partir do local de instalação do produto Gestão Empresarial | ERP dentro do diretório Sapiens. Em caso de execução a partir da DLL de integração do produto Gestão Empresarial (ISapiensDll.dll) com o produto Gestão de Pessoas | HCM, a carga dessa biblioteca é feita a partir do caminho de compartilhamento de rede da instalação do produto Gestão Empresarial, no formato UNC (Uniform Naming Convention), que apresenta a seguinte convenção para acesso a um caminho de rede compartilhado: nome do computador\nome do compartilhamento\diretório.

A instalação do produto Gestão Empresarial | ERP é uma instalação parte estação, ou seja, o arquivo DLL será obtido localmente.

Caso seja utilizado somente um atalho para o Sapiens.exe apontando para um caminho de rede \\servidor\senior\sapiens\sapiens.exe, é necessário copiar a DLL para a unidade local da máquina. Do contrário, haverá problemas no cadastro dos Clientes e Fornecedores.

A orientação referente à DLLIE32.DLL descrita acima se aplica para esta tela ou para qualquer outra rotina que faça utilização da DLL.

Inscrição Municipal

Informe a Inscrição Municipal do cliente.

Grupo Empresas

Código do grupo de empresas. Quando o grupo de empresas **for zerado**, será feita uma análise para
verificar se há outros clientes do antigo grupo do cliente alterado ligados
a produtos. Caso sim, é apresentada a seguinte mensagemAinda existem produtos ligados aos clientes do grupo de empresas xx. Manter as ligações já
existentes dos produtos neste cliente poderá resultar em informações divergentes
quando este cliente for ligado a outro grupo. Excluir as ligações já existentes
para este cliente?. Confirmando, as ligações de produtos com o cliente serão
excluídas; caso contrário, serão mantidas. **Recomendamos a exclusão das ligações**
quando o grupo de empresas do cliente for zerado.

O parâmetro global GruCliExc (F000PGS) pode ser usado para manter as ligações dos produtos de forma automática. Se o valor do parâmetro for "P - Perguntar", o sistema vai perguntar se deve manter as ligações dos produtos ao remover o cliente do grupo de empresas. Isso ocorre ao alterar/remover o valor do campo Grupo Empresas. Os valores "S - Sim" ou "N - Não" são para confirmação ou recusa automáticas.

Quando o grupo de empresas **for
alterado** para outro, será feita uma análise verificando se, para este novo
grupo, há produtos ligados aos seus clientes. Caso sim, é apresentada a seguinte mensagemRealizar a ligação automática dos produtos ligados aos clientes do grupo de empresas xx?.
Confirmando, será apresentada outra mensagemManter as ligações já existentes dos produtos neste cliente poderá resultar em informações divergentes
neste novo grupo. Excluir as ligações já existentes para este cliente antes de
realizar a inclusão automática?. Ao confirmar, antes de fazer a ligação
automática dos produtos vinculados aos clientes do grupo, todas as ligações existentes
de produtos com o cliente serão excluídas.

O parâmetro global GruCliAlt (F000PGS) pode ser usado para fazer a ligação automática dos produtos vinculados aos clientes do grupo de empresas. Se o valor do parâmetro for "P - Perguntar", o sistema vai perguntar se deve manter as ligações dos produtos ao remover o cliente do grupo de empresas. Isso ocorre na tela Cadastro de Clientes (F085CAD) ao incluir/alterar o valor do campo Grupo Empresas. Os valores "S - Sim" ou "N - Não" são para confirmação ou recusa automáticas.

Para saber mais sobre a análise de crédito no pedido, acesse a documentação correspondente.

**Benefício Fiscal**

Código da área beneficiada por isenção de ICMS e/ou IPI da Zona Franca de Manaus. Ao informar código **2 - Zona Franca**, o campo data de validade do Código SUFRAMA
ficará desabilitado.

Código Suframa

Código Suframa do cliente. Esta informação é obrigatória quando o campo Benefício Fiscal for **1 - Zona Franca de Manaus** ou **3 - Área de Livre Comércio**.

Tributa ICMS

Indicativo se o cliente tributa ou não ICMS.

Tributa IPI

Indicativo se o cliente tributa ou não IPI.

Tributa PIS

Indicativo se o cliente tem tributação de PIS.

Tributa COFINS

Indicativo se o cliente tem tributação de COFINS.

Retenção IRRF

Indicativo se as notas fiscais ou títulos poderão ter retenção de IRRF.

No caso de cliente pessoa física, cujo o percentual de IRRF não pode ser informado na nota fiscal, é verificado a tabela progressiva cadastrada na tela Tabelas de Imposto de Renda (F040IRF). Para que a retenção ocorra corretamente, independente do título ser gerado via nota ou manual, este parâmetro deve estar com o valor "S".

Retenção por Produto

Indicativo se o cliente controla retenções de PIS, COFINS, CSLL, IRRF e Outras
Retenções por Produto.

Utiliza Limite Retenção

Indicativo se o cliente utiliza o valor limite para o cálculo das retenções nas
notas fiscais de saída

Telefones

Telefone 1, Telefone 2 e Telefone 3 do cliente.

FAX

Número do FAX do cliente.

Caixa Postal

Número da caixa postal.

E-mail

E-mail do cliente.

E-Mail para documentos eletrônicos

Endereço eletrônico (e-mail) para envio de arquivos de documentos eletrônicos. Quando existir um valor informado nesse campo, este será utilizado para geração da tag de e-mail no XML do documento eletrônico.

CEP

CEP do cliente.

Endereço

Endereço do cliente.  
Para que esse dado seja replicado para os campos Endereço Entrega e Endereço Cobrança, deve-se selecionar as opções Sugerir endereço de entrega e **Sugerir endereço de cobrança** na tela F085SEL.

Número Endereço

Quando utilizado proprietária de varejo, esse campo deve ser informado no cadastro de cliente.

Complemento

Complemento do endereço do cliente.

Proximidade

Ponto de referência ou proximidade do endereço do cliente.

Bairro

Bairro do cliente. Quando utilizado proprietária de varejo, esse campo deve ser informado no cadastro de cliente.

Zip Code

Código de endereçamento postal para cliente do exterior.

Cidade

Cidade do cliente.

Estado

Sigla do estado (U.F.).

Código País

Código do país.

Endereço Entrega

Endereço de entrega do cliente.

Complemento Entrega

Complemento do endereço de entrega do cliente.

Zip Code Entrega

Código de endereçamento postal para clientes do exterior. Esse campo é utilizado para integração para o Gestão de Fretes, e enviado para este quando o cliente é do mercado externo. Quando não informado para cliente de mercado externo, é enviado o CEP.

CEP Entrega

Cep do endereço de entrega do cliente.

Cidade Entrega

Cidade de entrega do cliente.

Estado Entrega

Estado de entrega do cliente.

Inscrição Estadual Entrega

Inscrição estadual do endereço de entrega do cliente.

CNPJ Entrega

CNPJ do endereço de entrega do cliente. Quando houver integração com o Gestão de Armazenagem | WMS Senior, é obrigatório que o CNPJ da entrega seja válido.

Telefone de entrega

Telefone do endereço de entrega do cliente.

E-mail de entrega

E-mail do endereço de entrega do cliente.

Observação

O grupo <entrega>, com as informações do endereço de entrega da mercadoria, é gerado no arquivo XML da NF-e **somente** quando o endereço informado na tela Endereço de Entrega do Cliente (F085ENT) for **diferente** do endereço informado nessa tela. Quando o parâmetro global 'UsaEntOri' estiver como 'S', o endereço de entrega será assumido como endereço do destinatário e o grupo <entrega> não será gerado no XML.

Vide demais regras de geração da página parametrizações para NF-e 4.0.

Endereço Cobrança

Endereço de cobrança do cliente.

Complemento Cobrança

Complemento do Endereço de cobrança do cliente.

CEP Cobrança

CEP do endereço de cobrança do cliente.

Bairro Cobrança

Bairro de cobrança do cliente.

Cidade Cobrança

Cidade de cobrança do cliente.

Estado Cobrança

Estado de cobrança do cliente.

CNPJ Cobrança

CNPJ de cobrança do cliente.

CEP p/ Cálculo Frete

CEP para cálculo de frete. Este campo é utilizado exclusivamente para o cálculo do frete no pedido e será empregado no momento de faturar o pedido na geração de uma nota fiscal via pedido. No processo de geração de nota fiscal através de uma carga/pré-fatura, o CEP definido nesse campo não será considerado, de modo que o sistema efetuará o cálculo do frete no fechamento da nota fiscal de saída via carga/pré-fatura sem verificar o valor informado neste campo.

Correspondência

Indicativo de entrega de correspondência.

Cliente como Fornecedor

Código do cliente como fornecedor. Para utilizá-lo, faça as verificações abaixo:

* Primeiro passar pelo campo CNPJ/CPF para que o sistema faça as devidas validações e habilite ou não o campo;
* Caso não habilite, é necessário verificar no Cadastro da Filial se a filial logada está com o campo Indicativo se os códigos de cliente e fornecedor são iguais definido como "N - Não" (E070FIL.VENCFI = N). Destaca-se que se este campo estiver igual a "S - Sim", o campo Cliente como Fornecedor não será habilitado.

Cliente como Representante

Código do cliente como representante.

Cliente como Transportadora

Código do cliente como transportadora.

Bloqueia Crédito Cliente

Indicativo se o motivo bloqueia crédito de cliente.

Marca

Marca do cliente.

Identificação do Cliente

Código para identificação do cliente

Motivo Situação

Código do motivo da situação do cliente.

Observação Motivo

Observação do motivo da situação do cliente.

Usuário Motivo

Usuário responsável pelo motivo da situação do cliente.

Data Motivo

Data e hora do motivo motivo da situação do cliente.

% Adicional INSS

O percentual informado neste campo será somado a alíquota de INSS definida
no cadastro do serviço na inclusão de itens de serviços:  em pedidos,
contratos de venda e notas fiscais de saída.

Tipo Acerto (arredondamento)

Este campo vai influenciar no valor bruto da nota e no preço unitário dos itens.

* **Arredonda**: os valores são arredondados em duas casas decimais de acordo com as regras do arredondamento matemático (de 0 a 4 conserva-se o valor da segunda decimal e de 5 a 9 soma-se uma unidade).
* **Trunca**: trunca os valores em duas casas decimais, sem arredondamento.

Para sistemas que integram com o Gestão de Lojas, é considerado o campo Arrendondar/Truncar da tela F070VAR para saber o tipo de acerto que deve ser feito.

Cooperado

Este campo serve para definir se o Cliente/Fornecedor é cooperado.  
Não será possível alterar o parâmetro se existir um cooperado
ativo cadastrado para o cliente/fornecedor na tela Informações do Cooperado (F085COP).

Ao realizar o cadastro de um cliente/fornecedor na tela de Informações do Cooperado (F085COP) e informar a Situação "Ativo", este campo será atualizado para "Sim". Ao informar a situação "Em análise", "Recusado" ou "Desligado", o campo será preenchido automaticamente com "Não".

Código do Regime Tributário 

Definição do código do Regime Tributário com as seguintes opções:

* "1 - Simples Nacional";
* "2 - Simples Nacional - excesso de sublimite de receita bruta";
* "3 - Regime Normal";
* "4 - Simples Nacional - Microempreendedor Individual - MEI".

Observação

As rotinas de entradas, saídas, apuração e obrigações acessórias foram atualizadas para aplicar ao regime "4 - Simples Nacional - Microempreendedor Individual - MEI", o mesmo tratamento do regime "1 - Simples Nacional".

Mensagem - 1, Mensagem - 2, Mensagem - 3 e Mensagem - 4  
Permitem parametrizar um padrão de mensagens fiscais para a nota fiscal de saída, conforme a regra de sugestão.

Natureza Retenção

Informar a natureza de retenção.

Natureza Retenção CSLL(SPED)

Indicador de natureza de retenção na fonte de CSLL(SPED).

Natureza Retenção IRPJ(SPED)

Indicador de natureza de retenção na fonte de IRPJ(SPED).

Natureza Receita PIS

Informa a natureza da receita do PIS de acordo com códigos existentes nas tabelas da Receita Federal. O código é exigido na escrituração fiscal do SPED Contribuições. Para mais informações, consulte a ajuda da tela Notas Fiscais de Saída (F660NFV), guia Itens.

Natureza Receita COFINS

Informa a natureza da receita do COFINS de acordo com códigos existentes nas tabelas da Receita Federal. O código é exigido na escrituração fiscal do SPED Contribuições. Para mais informações, consulte a ajuda da tela Notas Fiscais de Saída (F660NFV), Guia Itens.

Número Identificação Fiscal

 Campo apenas informativo e opcional.

Entidade PAA

Indicativa se a empresa está cadastrada no Programa de Aquisição de Alimentos.

Classificação Tributária Reinf

Código da classificação tributária para o Reinf.

Estes campos podem ser informados manualmente no ERP ou integrados do Gestão de Lojas, através do web service com.senior.g5.co.int.varejo.cliente:

* Data Consulta SPC
* Cidade SPC/Intercâmbio
* Informação SPC

O campo Usuário Atualização SPC também pode ser integrado do Gestão de Lojas mas, no ERP, é preenchido automaticamente com o usuário logado no sistema.

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

Tipo de Assinante

Indicativo do tipo de assinante do cliente para geração da NFCom. As opções de preenchimento são:

* "1 - Comercial";
* "2 - Industrial";
* "3 - Residencial/Pessoa Física";
* "4 - Produtor Rural";
* "5 - Órgão da administração pública estadual direta e suas fundações e autarquias, quando mantidas pelo poder público estadual e regidas por normas de direito público, nos termos do Convênio ICMS 107/95";
* "6 - Prestador de serviço de telecomunicação responsável pelo recolhimento do imposto incidente sobre a cessão dos meios de rede do prestador do serviço ao usuário final, nos termos do Convênio ICMS 17/13";
* "7 - Missões Diplomáticas, Repartições Consulares e Organismos Internacionais, nos termos do Convênio ICMS 158/94";
* "8 - Igrejas e Templos de qualquer natureza";
* "99 - Outros não especificados anteriormente".

Aplicação da CBS/IBS

Aplicação da CBS/IBS (Campo FinCib).

Tipo Ente Governamental

Informa o tipo de ente governamental, para fins de distribuição do CBS/IBS.

Serviço prestado Fisicamente

Indicativo se o serviço é prestado fisicamente.

Mecanismo apoio ao Comércio Exterior do Serviço

Mecanismo de apoio/fomento ao Comércio Exterior utilizado pelo prestador do serviço. Com as opções:

* 01 - Nenhum;
* 02 - Adm. Pública e Repr. Internacional;
* 03 - Alugueis e Arrend. Mercantil de maquinas, equip., embarc. e aeronaves;
* 04 - Arrendamento Mercantil de aeronave para empresa de transporte aéreo público;
* 05 - Comissão a agentes externos na exportação;
* 06 - Despesas de armazenagem, mov. e transporte de carga no exterior;
* 07 - Eventos FIFA (subsidiária);
* 08 - Eventos FIFA;
* 09 - Fretes, arrendamentos de embarcações ou aeronaves e outros;
* 10 - Material Aeronáutico;
* 11 - Promoção de Bens no Exterior;
* 12 - Promoção de Dest. Turísticos Brasileiros;
* 13 - Promoção do Brasil no Exterior;
* 14 - Promoção Serviços no Exterior;
* 15 - RECINE;
* 16 - RECOPA;
* 17 - Registro e Manutenção de marcas, patentes e cultivares;
* 18 - REICOMP;
* 19 - REIDI;
* 20 - REPENEC;
* 21 - REPES;
* 22 - RETAERO;
* 23 - RETID;
* 24 - Royalties, Assistência Técnica, Científica e Assemelhados;
* 25 - Serviços de avaliação da conformidade vinculados aos Acordos da OMC;
* 26 - ZPE.

CAEPF

Cadastro de Atividade Econômica da Pessoa Física

## Páginas relacionadas

* [HabDocIde](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#HabDocIde)
* [GruCliExc](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#GruCliExc)
* [F000PGS](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm)
* [GruCliAlt](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#GruCliAlt)
* [documentação correspondente](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/analise-credito-pedido.htm)
* [isenção de ICMS e/ou IPI da Zona Franca de Manaus](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/deduzir_icms_pis_cofins_.htm)
* [Tabelas de Imposto de Renda (F040IRF)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f040irf.htm)
* [F085SEL](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f085sel.htm)
* [parametrizações para NF-e 4.0](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/parametrizacoes.htm)
* [F070VAR](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070var.htm)
* [F085COP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f085cop.htm)
* [regra de sugestão](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/manuais_processos/mercado/nf-e/regras-e-sugestoes-valores.htm#mensagens-fiscais)
* [F660NFV](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f660nfv.htm)
* [com.senior.g5.co.int.varejo.cliente](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/webservices/com_senior_g5_co_int_varejo_cliente.htm)
* [SCANC](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f669sca.htm)
