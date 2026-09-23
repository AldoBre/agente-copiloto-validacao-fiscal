# Guia Documentos Eletrônicos

> **Fonte:** F070FVE - Parâmetros da Filial para Vendas — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070fve.htm  
> **Trilha:** Ajuda por telas > Cadastros > Filiais > Parâmetros por Gestão  
> **Telas citadas:** F075PPC  
> **Identificadores de regras:** VEN-140NEDGE01

---
Ambiente NF-e/MD-e/MDF-e

Indicativo de qual ambiente que ficará registrado na nota eletrônica
ou manifesto eletrônico. Este ambiente refere-se a NF-e, MDF-e e Manifestação de Destinatário.

Observação

Caso o identificador de regras
VEN-140NEDGE01 estiver cadastrado e ativo, e se for
informado um ambiente diferente do informado neste campo para a 
regra, prevalecerá o que for determinado na regra deste identificador.

Ambiente CT-e

Indicativo de qual ambiente que ficará registrado no
conhecimento eletrônico.

Observação

Caso o identificador de regras
VEN-140CT00000 estiver cadastrado e ativo,
e se for informado um ambiente diferente do informado neste campo para a
regra, prevalecerá o que for determinado na regra deste identificador.

Integração NF-e

Indica a forma de integração e a versão de leiaute para notas fiscais eletrônicas.

Integração NFS-e

Indica a forma de integração e o leiaute para notas eletrônicas de
serviço.

Lista das integrações disponíveis para NFS-e:

* 0 - Não utiliza
* 1 - Padrão (ABRASF) - Retorno Manual
* 2 - NDDigital
* 3 - Converge.NET
* 4 - Padrão (ABRASF) - Retorno Automático
* 5 - 2a Geração (ABRASF) - Retorno Manual
* 6 - 2a Geração (ABRASF) - Retorno Automático
* 7 - NFS-e.net(Moderna)
* 8 - Senior 2.0

Observação

Os tipos **5 -2ª Geração (ABRASF) - Retorno Manual** e **6 - 2ª Geração (ABRASF) - Retorno Automático** de NFS-e não podem ser utilizados quando houver integração com o Documentos Eletrônicos. Mesmo que o município utilize ABRASF 2.0, o padrão de integração é 1.0.

Emissor NF-e

Indica o sistema utilizado para emissão de NF-e.

Integração MDF-e

Indica a forma de retorno para o manifesto eletrônico no padrão MDF-e 3.00. As opções de preenchimento são:

* 3ª Geração - Retorno automático
* 3ª Geração - Retorno Manual

Software Emissor NF-e

Para informações sobre as formas de integração com o eDocs, verifique a documentação do processo.

A opção 99 – Outros Emissores – Retornos Automáticos é utilizada quando existe integração do Gestão Empresarial | ERPcom sistemas de terceiros. Já a opção 01 – Emissor Sefaz / Terceiros – Retorno Manual é utilizada quando se usa o Emissor Gratuito para autorização das NF-e. A assinatura digital será gerada pelo Gestão Empresarial | ERPnos .XMLs apenas quando forem utilizadas as opções 01 ou 99.

Para verificar os módulos necessários para a emissão de documentos eletrônicos, verifique o tópico Validações de módulos da proprietária do ERP necessários para execução dos processos da documentação de integração do Gestão Empresarial | ERP com o eDocs.

Observação

Se houver integração do ERP com WMS WIS, este campo precisa estar parametrizado com a opção "00-eDocs - Envio via Arquivo e Retorno via Web Service ERP", pois toda a homologação da integração com WMS WIS foi criada baseada nesse processo.

Visualizar NF-e

Indica se a NF-e deverá ser visualizada antes do envio.

Mod. Relatório Visualização NF-e

Código do modelo de relatório.

Prazo Canc. NF-e (horas)

Indica o prazo em horas para cancelamento da Nota Fiscal Eletrônica após
o retorno do SEFAZ. Não é possível configurar uma quantidade de horas
maior do que 24 Horas, conforme o ATO COTEPE/ICMS n° 35, de 24 de novembro de 2010.

Prazo Canc. por Sub. Nf-e (horas)

Indica o prazo em horas para cancelamento por substituição da Nota Fiscal Eletrônica após o retorno do SEFAZ. Não é possível configurar uma quantidade de horas
maior do que 168 horas, conforme nota técnica 2018.004.  
Conforme a legislação, este evento está implementado somente para a NFC-e (Modelo 65).

Valor limite NF-e

Conforme determinações da nota técnica 2011.004,
este campo indica o valor máximo que uma nota fiscal, para uma série fiscal com
dispositivo
autorizado 6 (nota fiscal eletrônica) informado em seu cadastro, poderá possuir. Este valor será consistido
já no fechamento da nota fiscal. Como zero é o valor padrão do campo, este valor
não será consistido.

Diretório Retorno NFS-e

Diretório de retorno da nota fiscal eletrônica. Este campo estará disponível apenas quando a filial emissora da NFS–e for do município de Florianópolis - SC. Confira a documentação do processo para a emissão da NSF–e para esse município, através do arquivo Emissão NFS–e para Florianópolis.

Gerar Carga Tributária NFS-e

Indica se as informações de carga tributária serão geradas na NFS-e.

Fonte da Carga Tributária NFS-e 

Nome da fonte da carga tributária NFS-e.

Observação

Os campos Gerar Carga Tributária NFS-e e Fonte da Carga Tributária NFS-e estarão disponíveis apenas quando o tipo de integração for ABRASF. Abrasf é um modelo de integração da nota fiscal

Utiliza prorrogação suspensão ICMS

Indica se a filial utiliza a prorrogação de suspensão de ICMS por evento eletrônico.

Ambiente para prorrogação de suspensão de ICMS

Identifica o ambiente utilizado para comunicar com a SEFAZ os eventos de prorrogação de suspensão de ICMS. Quando o ambiente da NF-e estiver configurado como **2 - Homologação**, o ambiente para prorrogação de suspensão de ICMS também deverá ser **2 - Homologação**.

Gerar informações do ICMS Efetivo na NF-e

Indica se devem ser gerados os campos <pRedBCEfet>, <vBCEfet>, <pICMSEfet> e <vICMSEfet>, referentes ao ICMS Efetivo, no arquivo XML da NF-e. Essas informações são opcionais, mas podem ser exigidas, a critério de cada UF.

Gerar informações de veículos na NF-e

Indicativo se a geração do arquivo XML da NF-e deve considerar as informações do Veículo (grupo veicTransp) e do Reboque (grupo reboque) em operações intermunicipais dentro do Estado.  
Caso uma determinada UF não permita a impressão destes campos em operações internas, todas as filiais da respectiva UF deverão estar com esse parâmetro igual a N - Não.

Qtd. Comercial no Lote

Indica se quantidade de produto no lote será convertida conforme a unidade comercial, na geração da tag <qLote> no arquivo XML da NF-e. A parametrização desse campo será considerada apenas se o campo Qtd. Comercial no Lote da tela F075PPC não for informado.

A regra completa para geração dessa informação está disponível no leiaute da NF-e.

Forma de envio do ICMS 51

Como o tratamento dos valores de diferimento de ICMS total variam de acordo com o estado, este campo tem por finalidade indicar qual será a forma de envio. Ficará habilitado para edição somente quando o campo **Tipo Cálculo Diferimento**, localizado na guia **Vendas 2**, for igual a **0 - Diferimento de ICMS por base**. Possui duas opções:

* C - Completa: nesse caso, na geração do .XML da nota, quando houver percentual de diferimento igual a 100%, serão geradas todas as tags abaixo do CST x51.
* R - Resumida: nesse caso, na geração do .XML da nota, quando houver percentual de diferimento igual a 100%, serão geradas apenas as tags Origem e CST.

Observação:

Quando o percentual de diferimento for menor que 100%, o ICMS 51 sempre será enviado da forma completa.

Ambiente NFCom

Indicativo de qual ambiente que ficará registrado a NFCom. As opções de preenchimento são:

* "1 - Produção";
* "2 - Homologação".

Tipo de emissão da NFCom

Indicativo o tipo padrão para emissão da NFCom. As opções de preenchimento são:

* "0 - NFCom Normal";
* "3 - NFCom de Substituição";
* "4 - NFCom de Ajuste".

Tipo de faturamento da NFCom

Indicativo da finalidade padrão para emissão da NFCom. As opções de preenchimento são:

* "0 - Faturamento normal";
* "1 - Faturamento centralizado";
* "2 - Cofaturamento".

Versão do leiaute da NFS-e

Indicativo da versão do leiaute a ser utilizado na geração do XML da NFS-e.

* "0 - 1.01";
* "1 - 1.02".

## Páginas relacionadas

* [documentação](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/edocs/integracao-erp-edocs.htm)
* [Validações de módulos da proprietária do ERP necessários para execução dos processos](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/edocs/integracao-erp-edocs.htm#4_-_Valida%C3%A7%C3%B5es_de_m%C3%B3dulos_da_propriet%C3%A1ria_do_ERP_necess%C3%A1rios_para_execu%C3%A7%C3%A3o_dos_processos)
* [2011.004](http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=ysYXxjwjYyk=)
* [dispositivo 
autorizado 6](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f020snf.htm)
* [Emissão NFS–e para Florianópolis](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/integracao_nfse_florianopolis.htm)
* [leiaute da NF-e](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/nf-e-4-0-leiaute.htm#qLote)
