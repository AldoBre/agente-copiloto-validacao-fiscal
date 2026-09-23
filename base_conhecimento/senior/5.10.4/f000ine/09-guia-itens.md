# Guia Itens

> **Fonte:** F000INE - Via Recebimento de Documento Eletrônico — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f000ine.htm  
> **Trilha:** Ajuda por telas > Suprimentos > Gestão de Recebimento > Notas Fiscais de Entrada  
> **Telas citadas:** E000IPC, E000ISC, E000PAR, E000PCD, E015MED, E075PRO, E080SER, E095FOR, E403FPP, E403FPR, E440IPC, E440ISC, E440PCD, F000DPL, F000INE, F001TCP, F191CPT, F403FSE, F422COC, F440CIP, F440GNE, F440NPR  
> **Identificadores de regras:** CPR-000IEPAR01

---
Apresenta os registros obtidos dos itens, parcelas, distribuição por lotes e notas de frete da nota fiscal de entrada, através do arquivo XML após a execução do web service.

Número do ato concessório de Drawback (campo adicionado para adequar esta tela para recebimentos de documentos eletrônicos 3.10, está disponível para consulta e será editável quando o tipo de mercado do fornecedor for (E095FOR.TIPMER) (Externo/Exterior) e nenhum deles interferirá no processo de nota.

Observações

* Caso o usuário queira dividir em ordens de compra diferentes os itens de produto ou serviço que vêm agrupados em uma nota fiscal (através do botão Dividir Item), os campos Número da OC e Sequência do item na OC devem ser preenchidos na guia Itens dessa tela.
* Nos casos de inconsistências referentes as quantidades distribuídas em lotes o sistema poderá exibir um valor um pouco maior do que o verdadeiro quando houver conversão de unidades de medidas. Porém ainda assim há diferença entre as quantidades distribuídas em lotes e a quantidade total do item.
* Após realizar a divisão dos itens, caso o produto tenha controle por lote ou série, é necessário acessar o botão **Dist.Lote (J)** ou **Dist.Série (9)** para redistribuir as quantidades para o item que já existia na nota fiscal, bem como para os demais itens que foram inseridos com a utilização da opção **Dividir Item (0)**, uma vez que a redistribuição não é realizada de forma automática.

## Produto

**Unidade de Medida Fiscal (XML)**

Somente leitura. Carrega o campo E000IPC.UniNfc para a guia (6 posições). Ele tem por objetivo apresentar ao usuário qual foi a unidade de medida que veio informada no XML. Esta coluna não será utilizada no processamento, é apenas visual. Essa UM sequer precisa existir na base.

**Unidade de Medida Nota (ERP)**

Representa a unidade de medida fiscal da nota (E440IPC.UniNfc). O sistema utiliza a Unidade de Medida Fiscal do .XML para encontrar uma unidade de medida equivalente no sistema seguindo os critérios abaixo:

1. Busca a unidade de medida cadastrada na ligação Fornecedor por Produto x Fornecedor (E403FPP)
2. Busca uma unidade de medida do sistema equivalente à Unidade de Medida Fiscal do .XML através do campo E015MED.UniFis
3. Busca uma unidade de medida do sistema equivalente à Unidade de Medida para ECF do .XML através do campo E015MED.UniEcf (Apenas para Clientes do Varejo)
4. Busca a unidade de medida informada na ligação Produto x Fornecedor E403FPR.UNIMED (unidade do produto no fornecedor)
5. Busca a unidade de medida informada no cadastro do produto E075PRO.UNIMED

Esta coluna preenche o campo E440IPC.UniNfc no processamento

Importante

Após alterar essa coluna, as colunas Qtde. Estoque e Preço Est. da guia Itens serão recalculadas.

Para as notas fiscais do tipo 2, 3, 4, 5, 7, 8, e 11, o campo Tipo Cálculo Devolução da F001TCP, pode impactar nas conversões. Recomenda-se a opção "R – Recálculo de Valores" para estas notas.

Para as notas fiscais do tipo 2 e 3, quando o campo Tipo Cálculo Devolução da F001TCP estiver definido como "P - Cálculo Proporcional", a conta contábil definida na nota fiscal de origem da devolução também é considerada. Caso a conta contábil esteja definida como inativa, é necessário alterá-la para ativa para que a nota seja processada. Também é recomendado utilizar a opção "R – Recálculo de Valores" para estas notas.

Produto no Fornecedor (XML)

Este campo recebe a descrição da tag <prod|cProd> do XML, para que o usuário também tenha em tela esta informação, pois, o campo Produto no Fornecedor do item é sugerido de acordo com os cadastros do sistema.

**Unidade de Medida Estoque (ERP)**

Campo somente leitura, nada mais é do que a busca do campo E075PRO.UNIMED. Ele é somente leitura pois é este o comportamento da F440GNE, trata-se da unidade de medida do estoque do produto, o usuário não altera esta informação. Esta coluna alimentará no processamento o campo E440IPC.UniMed.

**Origem Fiscal da Mercadoria**

Será carregado apenas quando o fornecedor da nota fiscal for do regime tributário **Simples Nacional**. Nesses casos, a Origem Fiscal da Mercadoria pode ser diferente da origem informada na Situação Tributária.

Para os fornecedores do regime **Normal**, a Origem Fiscal da Mercadoria sempre será o primeiro dígito contido na Situação Tributária do item. Portanto, esse campo estará zerado e apenas no processamento será carregado para os itens da nota gerada, utilizando o primeiro dígito contido na Situação Tributária.

Natureza da Operação (XML)

Campo somente leitura, que carregará o campo E000IPC.NopPro para a guia (5 posições). Ele tem por objetivo apresentar a natureza da operação (CFOP) que veio informada no XML. Esta coluna não será utilizada no processamento, é apenas visual.

Complemento

Este campo recebe a descrição da tag **<prod|xProd>** do .XML, sendo que o seu conteúdo será listado no registro C170 - Itens do documento do SPED ICMS/IPI.

Compl. (ERP)

O complemento é buscado do cadastro do produto/derivação, não é editável e será formado da seguinte maneira: Descrição do Produto + Descrição Complementar do Produto + Descrição da Derivação + Descrição Complementar da Derivação.  
Com a **ordem de compra informada**, o complemento será formado: Descrição do Produto + Descrição Complementar do Produto + Descrição da Derivação + Descrição Complementar da Derivação + Complemento da Ordem de Compra.

**Contrato**

Este campo pode ser editado/manipulado quando:

* O campo **Contrato** estiver zerado, ou seja, quando ele não foi manipulado via regra pela rotina de importação de .XML
* O tipo da nota posicionada for **1**, **7** ou **8**. Os demais tipos não irão permitir edição do campo de **Contrato**
* A nota não possuir informação de ordem de compra

Ao editar o campo **Contrato**, ele irá funcionar da seguinte forma na tela:

* Será possível informar apenas contratos do tipo **10**, validando se o contrato ainda possui saldo, se está ativo e dentro da sua vigência
* Ao listar várias notas da tela, caso alguma tenha um contrato já definido pela importação de XML, o mesmo deverá aparecer normalmente na tela, porém, não será possível editar o campo de **Contrato** desse registro. **Observação:** quando alimentado via importação de XML, pode ser usado outros tipos de contrato
* Ao informar o **Contrato** na guia de Notas Fiscais de Entrada, o mesmo será sugerido para os itens dessa nota. Para editar o campo de **Contrato** dos itens, é necessário que os dados gerais da nota tenham informação de **Contrato**

Ao processar a tela Via Recebimento de Documento Eletrônico, será gerada a nota fiscal de entrada com a informação de **Contrato**, conforme definido em tela. A atualização do saldo do **Contrato** de tipo **10** é realizada ao fechar a nota fiscal de entrada.

**Observação**

Ao realizar o vínculo do contrato no item de produto/serviço, o sistema não fará a herança dos códigos de produto/serviço do item do contrato.

Dividir Item

Esse botão tem o objetivo de dividir um item de produto ou serviço da nota fiscal para que o usuário possa separar os itens e referenciá-los a ordens de compra diferentes. A tela F000DPL é acessada através desse botão para que a divisão seja feita.

Classif. Fiscal

Por padrão, a classificação fiscal do item é carregada conforme o cadastro do produto durante o processamento, ou seja, apenas será carregado na tela F440GNE, quando a nota fiscal estiver como "Processada" via tela F000INE. Isso ocorre em virtude do campo não ser carregado através das informações do XML.   
Caso o usuário informe uma classificação fiscal, ela será mantida na geração da nota, ou seja, não será populado da rotina F000INE. O campo será gravado apenas na tela F440GNE.

Vlr do ICMS-ST desonerado

Valor do ICMS-ST desonerado.

Mot. deson. ICMS-ST

Motivo da desoneração do ICMS-ST.

Per. do dif. de ICMS FCP

Percentual diferido de ICMS FCP.

Vlr dif. do ICMS FCP

Valor diferido de ICMS FCP.

Vlr efe. do ICMS FCP

Valor efetivo de ICMS FCP.

Sequencial para Impressão da Nota Fiscal   
Esse campo será carregado com conteúdo da tag <det nItem="SEQUENCIA"> do XML, sendo que o usuário poderá realizar qualquer manutenção nas sequências e é de sua responsabilidade garantir que não exista um item de serviço com a mesma sequência.

Observação

Qualquer alteração nesse campo impacta na geração do registro C170 - Itens do documento do SPED ICMS/IPI.

Qtde. Base ICMS Monofásico

Quantidade da Base de ICMS Monofásico.

Vlr. ICMS Monofásico

Valor do ICMS Monofásico dos Itens de Produto da Nota Fiscal de Saída.

Alíq. ICMS Monofásico

Alíquota ad rem do ICMS Monofásico.

Qtde. Base ICMS Mono. Ret

Quantidade Base de ICMS Monofásico Retido.

Vlr. ICMS Mono. Ret

Valor do ICMS Monofásico Retido dos Itens de Produto da Nota Fiscal de Saída.

Alíq. ICMS Mono. Ret

Aliquota ad rem de ICMS Monofásico Retido.

Qtde. Base ICMS Mono. Dif

Quantidade Base de ICMS Monofásico Diferido.

Vlr. ICMS Mono. Dif

Valor do ICMS Monofásico Diferido dos Itens de Produto da Nota Fiscal de Saída.

Perc. ICMS Mono. Dif

Percentual de Diferimento do ICMS Monofásico.

Qtde. Base ICMS Mono. Des

Quantidade Base de ICMS Monofásico Destacado.

Vlr. ICMS Mono. Des

Valor do ICMS Monofásico Destacado dos Itens de Produto da Nota Fiscal de Saída.

Alíq. ICMS Mono. Des

Alíquota ad rem de ICMS Monofásico Destacado.

Alíq. ICMS Mono. Ori

Alíquota ad rem de ICMS Monofásico Original.

Base ICMS Simp. Nac.

O campo Base ICMS Simp. Nac. não possui tag específica, por isso, durante o carregamento da Nota Fiscal, é feito um cálculo reverso para saber qual seria o valor aproximado da base. Esse valor pode ter alguns centavos de imprecisão, o que não é um problema, já que o valor do Simples Nacional calculado será o mesmo do XML.

Sit. Trib. Ori.  
Ao importar uma nota fiscal, a CST do item da nota será informada nesse campo. Esse campo não pode ser editado pelo usuário e tem a finalidade de armazenar a CST original do documento, enquanto a Situação Tributária do ICMS receberá a CST da operação sob o enfoque do adquirente.

Empresa NFS

Permite informar no campo a empresa relacionada a Nota Fiscal de Saída do produto.

Filial NFS

Permite indicar a filial relacionada a Nota Fiscal de Saída do produto.

Série NFS

Possibilita inserir a série relacionada a Nota Fiscal de Saída.

Nr. NFS

Indica o número da Nota Fiscal de Saída do produto.

Série NFC Ref.

Série da nota fiscal de entrada ligada ao item.

For. NFC Ref.

Código de fornecedor da nota fiscal de entrada ligada ao item.

Nr. NFC Ref.

Número da nota fiscal de entrada ligada ao item.

Seq. NFC Ref.

Sequência do item de produto na nota fiscal de entrada ligada ao item.

Sit. Trib. Ori.

Esse campo (E000PCD.StrOri) não é editável. Ele é formado durante a importação da nota fiscal, pela junção dos valores de <orig> e <CST>. Por exemplo, se <orig> = 5 e <CST> = 00, o sistema forma o código "500", que alimenta os campos Sit. Trib. (E000IPC.CodStr) e depois Sit. Trib. Ori. (E000PCD.StrOri).

Observação

Na tela Nota Fiscal de Entrada Agrupada (F440GNE), o campo Sit. Trib. Ori. (E440PCD.StrOri) é editável. Ele será preenchido automaticamente somente quando o campo Sit. Trib. Ori. (E000PCD.StrOri) estiver informado na tela atual (F000INE).

Ind. Devolução

Campo opcional e que serve para indicar que o produto é uma dedução. Quando o item tiver esta coluna igual a "S - Sim" os impostos referentes a ele serão negativados, deduzindo do valor total da nota.

## Serviço

**Unidade de Medida Fiscal (XML)**

Campo somente leitura, que carregará o campo E000ISC.UniMed para a guia (6 posições). Ele tem por objetivo apresentar ao usuário qual
foi a unidade de medida que veio informada no XML. Esta coluna não será utilizada no processamento, é apenas visual. Essa UM sequer precisa existir na base.

**Unidade de Medida Serviço (ERP)**

Campo para edição, que representa a unidade de medida do serviço (E440ISC.UniMed). Ele será carregado através dos cadastros do sistema,
seguindo esta ordem, até encontrar a unidade de medida:

1. Busca uma unidade de medida do sistema, equivalente a Unidade de Medida Fiscal contida no XML, através do campo E015MED.UniFis
2. Busca a unidade de medida informada no cadastro do serviço E080SER.UNIMED

Esta coluna alimentará no processamento o campo E440ISC.UniMed.

**Origem Fiscal da Mercadoria**

Este campo será carregado apenas quando o fornecedor da nota fiscal for do regime tributário **Simples Nacional**. Nestes casos a Origem Fiscal da Mercadoria pode ser diferente da origem informada na Situação Tributária. Para os fornecedores do regime **Normal**, a Origem Fiscal da Mercadoria sempre será o primeiro dígito contido na Situação Tributária do item. Portanto, este campo estará zerado e apenas no processamento será carregado para os itens da nota gerada, utilizando o primeiro dígito contido na Situação Tributária.

Natureza da Operação (XML)

Campo somente leitura, que carregará o campo E000IPC.NopPro para a guia (5 posições). Ele tem por objetivo apresentar a natureza da operação (CFOP) que veio informada no XML. Esta coluna não será utilizada no processamento, é apenas visual.

Complemento

Este campo recebe a descrição da tag **<prod|xProd>** do .XML, sendo que o seu conteúdo será listado no registro C170 - Itens do documento do SPED ICMS/IPI.

Compl. (ERP)

O complemento é buscado do cadastro do serviço, não é editável e será formado da seguinte maneira: Descrição do Serviço + Descrição Complementar do Serviço.  
Com a **ordem de compra informada**, o complemento será formado: Descrição do Serviço + Descrição Complementar do Serviço + Complemento da Ordem de Compra.

Itens da OC

Abre a tela de Consulta da Ordem de Compra (F422COC) quando a nota possui uma ordem de compra vinculada, tanto para produto como para serviço.

Dividir Item

Esse botão tem o objetivo de dividir um item de produto ou serviço da nota fiscal para que o usuário possa separar os itens e referenciá-los a ordens de compra diferentes. A tela F000DPL é acessada através desse botão para que a divisão seja feita.

**Contrato**

Este campo pode ser editado/manipulado quando:

* O campo **Contrato** estiver zerado, ou seja, quando ele não foi manipulado via regra pela rotina de importação de .XML
* O tipo da nota posicionada for **1**, **7** ou **8**. Os demais tipos não irão permitir edição do campo de **Contrato**
* A nota não possuir informação de ordem de compra

Ao editar o campo **Contrato**, ele irá funcionar da seguinte forma na tela de Via Recebimento de Documento Eletrônico:

* Será possível informar apenas contratos do tipo **10**, validando se o contrato ainda possui saldo, se está ativo e dentro da sua vigência
* Ao listar várias notas da tela, caso alguma tenha um contrato já definido pela importação de XML, o mesmo deverá aparecer normalmente na tela, porém, não será possível editar o campo de **Contrato** desse registro. **Observação:** quando alimentado via importação de XML, pode ser usado outros tipos de contrato
* Ao informar o **Contrato** na guia de Notas Fiscais de Entrada, o mesmo será sugerido para os itens dessa nota. Para editar o campo de **Contrato** dos itens, é necessário que os dados gerais da nota tenham informação de **Contrato**

Ao processar a tela Via Recebimento de Documento Eletrônico, será gerada a nota fiscal de entrada com a informação de **Contrato**, conforme definido em tela. A atualização do saldo do **Contrato** de tipo **10** é realizada ao fechar a nota fiscal de entrada.

**Observação**

Ao realizar o vínculo do contrato no item de produto/serviço, o sistema não fará a herança dos códigos de produto/serviço do item do contrato.

Tipo Serviço

Tipo de Serviço no contexto fiscal com base na LC 116/2003.

Cód. Trib. NFS-e

Código de tributação do serviço para nota fiscal de serviço eletrônica. Considera o tipo de serviço e localiza o primeiro serviço encontrado na tabela Cadastros - Serviços (E080SER).

ISS retido

Indica se o serviço possui ISS Retido.

**Vlr. Ded. Base Imp.**

Valor de dedução na base dos impostos.

Classif. Fiscal

Por padrão, a classificação fiscal do item é carregada conforme o cadastro do serviço durante o processamento, ou seja, apenas será carregado na tela F440GNE, quando a nota fiscal estiver como "Processada" via tela F000INE. Isso ocorre em virtude do campo não ser carregado através das informações do XML.   
Caso o usuário informe uma classificação fiscal, ela será mantida na geração da nota, ou seja, não será populado da rotina F000INE. O campo será gravado apenas na tela F440GNE.

Vlr do ICMS-ST desonerado

Valor do ICMS-ST desonerado.

Mot. deson. ICMS-ST

Motivo da desoneração do ICMS-ST.

Per. do dif. de ICMS FCP

Percentual diferido de ICMS FCP.

Vlr dif. do ICMS FCP

Valor diferido de ICMS FCP.

Vlr efe. do ICMS FCP

Valor efetivo de ICMS FCP.

Sequencial para Impressão da Nota Fiscal   
Esse campo será carregado com conteúdo da tag <det nItem="SEQUENCIA"> do .XML, sendo que o usuário poderá realizar qualquer manutenção nas sequências e é de sua responsabilidade garantir que não exista um item de produto com a mesma sequência.

Observação

Qualquer alteração nesse campo impacta na geração do registro C170 - Itens do documento do SPED ICMS/IPI.

Base ICMS Simp. Nac.

O campo Base ICMS Simp. Nac. não possui tag específica, por isso, durante o carregamento da Nota Fiscal, é feito um cálculo reverso para saber qual seria o valor aproximado da base. Esse valor pode ter alguns centavos de imprecisão, o que não é um problema, já que o valor do Simples Nacional calculado será o mesmo do XML.

Sit. Trib. Ori.

Ao importar uma nota fiscal, a CST do item da nota será informada nesse campo. Esse campo não pode ser editado pelo usuário e tem a finalidade de armazenar a CST original do documento, enquanto a Situação Tributária do ICMS receberá a CST da operação sob o enfoque do adquirente.

Empresa NFS

Permite informar no campo a empresa relacionada a Nota Fiscal de Saída relacionada ao serviço.

Filial NFS

Permite indicar a filial relacionada a Nota Fiscal de Saída.

Série NFS

Possibilita inserir a série relacionada a Nota Fiscal de Saída.

Nr. NFS

Indica o número da Nota Fiscal de Saída relacionada ao serviço.

Ind. Devolução

Campo opcional e que serve para indicar que o serviço é uma dedução. Quando o item tiver esta coluna igual a "S - Sim" os impostos referentes a ele serão negativados, deduzindo do valor total da nota.

## Parcelas

A guia de parcelas é carregada através de duas situações:

* Quando as parcelas estão informadas no XML da nota fiscal, são passadas através das tags de duplicata cobr|dup e gravadas na tabela intermediária E000PAR
* Quando as parcelas não vem informadas no XML, mas a nota possui valor financeiro e transação sugerida no carregamento da nota, possui integração com o contas a pagar/receber

Nestes casos, ao carregar a nota o sistema irá gerar as parcelas de acordo com a condição de pagamento da nota.

Observação

Caso as duas opções citadas acima não forem atendidas, a guia de parcelas ficará vazia. Porém, se no processamento da nota o sistema gerar valor financeiro e as parcelas não estiverem geradas, o sistema irá gerar as parcelas durante o processamento da nota.

Banco, Agência e Nº CC

Informe o código do banco e da agência e o número da conta corrente. O preenchimento de cada campo deve ser feito manualmente (não considera o cadastro do fornecedor) ou manipulado através do Identificador de Regras CPR-000IEPAR01 executado ao processar o registro.

## Notas de Frete

Há dois tipos de nota fiscal relacionada que o sistema pode receber:

**Com Chave Eletrônica**: essas notas vêm com uma chave eletrônica informada. Com isso o campo **Chv. NF-e Relac** é carregado na guia e o sistema busca todos os dados da nota fiscal cadastrada na base (CNPJ/CPF do Fornecedor, número e série da nota). Por padrão, ao buscar a nota fiscal de origem, o sistema verifica primeiro se a nota referenciada é uma nota de entrada, considerando os tipos de nota "1, 3, 6, 7, 10, 11". Caso não encontre, passa a buscar entre as notas de saída.

Observação

Para casos em que existe tanto uma nota de saída quanto uma nota de entrada com a mesma chave eletrônica, e deseja-se que a saída seja vinculada em vez da entrada, é possível ignorar o tipo da nota de entrada durante a busca utilizando o identificador de regra CPR-000EXFTP-1.

**Sem Chave Eletrônica:** essas notas vêm apenas com o CNPJ/CPF do Fornecedor, o número da nota e a série fiscal da nota relacionada. Essas informações estão representadas na guia pelos seguintes campos: **CGC Forn. NFE Relac. (XML), Nº NF Relac. (XML) e Série NF Relac. (XML)**. Eles trazem o que veio no .XML e servem apenas para leitura. As alterações são feitas nos campos de sugestão:

* **Filial NF Relac. (Sugerido):** a filial da nota referenciada manual não está disponível no XML, por isso, será sugerida a filial da nota eletrônica
* **Forn. NFE Relac. (Sugerido):** o sistema irá buscar o código do fornecedor através do CNPJ/CPF, informado no campo CGC Forn. NFE Relac. (XML)
* **Nº NF Relac. (Sugerido):** será carregado o mesmo número do campo Nº NF Relac. (XML)
* **Série NF Relac. (Sugerido):** utiliza a Filial NF Relac. (Sugerido) para sugerir a série

**Validação da Sugestão:**

* Utilizando a filial e série sugerida, é verificado se há uma nota fiscal no sistema correspondente
* Caso encontre-a, o sistema fará uma nova busca, verificando se não há a mesma nota em outras filiais
* Não havendo, será utilizada essa nota sugerida para o processamento. Do contrário não será sugerida a filial e o usuário terá de informar manualmente os dados da nota relacionada, via tela

## Notas Recebimento/Pagamento

A guia de Notas Pagamento/Recebimento representa parte do processo já realizado pela tela F440NPR. Para fazer a ligação das notas de pagamento/recebimento, o .XML da nota importada deve referenciar outra nota fiscal por meio da tag **NFref|refNFe**.  

O .XML terá apenas a chave eletrônica da nota fiscal referenciada, porém o sistema buscará as demais informações da nota referenciada já existente no ERP ao carregar a nota fiscal importada. Para que a guia de Notas Recebimento/Pagamento seja carregada, as notas importadas e referenciadas devem ser do tipo 1 (NF Entrada). Além disso, a nota referenciada existente no sistema **deve possuir transação integrada de Estoques ou Contas a Pagar, nunca os dois juntos**.  

Ao processar as notas fiscais, será criada a ligação das notas de recebimento e pagamento. Se a nota fiscal de Recebimento/Pagamento ligada não possuí saldo disponível, a nota fiscal ficará como inconsistente, não permitindo o processamento.

**Observação**

A ligação entre a nota fiscal de entrada e as notas fiscais relacionadas do tipo Recebimento ou Pagamento é feita através dos itens, os quais utilizam o código do produto/derivação e o código do serviço para estabelecer a conexão. Isso significa que notas fiscais de entrada com produtos/serviços idênticos podem ter a sugestão incorreta nos campos Seq. Rel. Prod. e Seq. Rel. Serv.. Nessas situações, esta tela não permite a alteração da sequência sugerida, e a nota deve ser gerada manualmente.

## Cálculo realizado para verificação

**Movimento Normal:**

Quantidade recebida da nota Pagamento/Recebimento - Quantidade Devolvida da nota Pagamento/Recebimento - Quantidade disponível na nota fiscal Pagamento/Recebimento.

* Se a Quantidade Recebida da nota fiscal Pagamento/Recebimento ligada a nota fiscal Eletrônica for maior que a quantidade calculada acima, a nota fiscal eletrônica ficará como Inconsistente

**Movimento Consignado Fornecedor/Cliente:**

Quantidade recebida da nota Pagamento/Recebimento - Quantidade disponível na nota fiscal Pagamento/Recebimento.

* Se a Quantidade Recebida da nota fiscal Pagamento/Recebimento ligada a nota fiscal Eletrônica for maior que a quantidade calculada acima, a nota fiscal eletrônica ficará como Inconsistente

## Notas de Recebimento/Pagamento sem integrações com o Contas a Pagar e Estoques

Agora é possível importar notas de Recebimento/Pagamento que não possuam integrações com os módulos Contas a Pagar e Estoques, para isso é preciso parametrizar as seguintes informações:

1. Na tela Parâmetros de Integração (F191CPT), defina a Empresa e Filial desejada (caso seja necessário manter todas as filias, basta informar a filial "0");
   1. Em Grupo, selecione "Documentos Fiscais de Entrada";
   2. Em Subgrupo, selecione a opção "Gerais" e clique em Mostrar;
   3. Na grade, selecionar a opção "Considerar integração das transações nas notas fiscais geradas, obrigatório ser compatível" e informar o valor "0 - Não considerar" (Obs.: As outras duas opções vão gerar a obrigação da integração).
2. Na tela de Transações de Compras (F001TCP):
   1. Na guia Dados Gerais 2, o campo Operação de Compra, deve estar preenchido de acordo com a natureza da operação, ou seja, se for a nota de recebimento, deve-se estar marcado: "R - Recebimento" e se for pagamento "P - Pagamento".

**Observações**

* Quando a opção "Considerar integração das transações nas notas fiscais geradas, obrigatório ser compatível" estiver em branco, a opção "2 - Perguntar" é assumida, porém, a tela F000INE trata de processos automáticos e não há interação. Sendo assim, na tela F000INE se for diferente de "0 - Nunca Considerar" o sistema tratará como se estivesse sendo obrigatório a integração, e desta forma, mostrará uma mensagem de inconsistência obrigando a integração.
* Para que o sistema valide notas de recebimento/pagamento apenas com base no campo Operação Compra da transação, desconsiderando a configuração da tela F191CPT, é necessário ativar o parâmetro global ValPagRec.

## Inconsistências

A guia de logs é carregada apenas quando há inconsistências na nota fiscal posicionada. Ou seja, os valores apresentados serão unicamente desta nota.

Exportar

Gera uma apresentação na tela de todos os logs em um NotePad e um arquivo .txt na pasta configurada na Central de Configurações Senior, contendo todos os logs apresentados na guia.

## Botões

Cálculos

Acessa a tela F440CIP, para a consulta dos valores dos itens da nota fiscal, ou seja, serão exibidos apenas os valores carregados do XML, pois esta tela não realiza cálculos ou modificações nos valores originais.

Aplicar

Quando acionado é exibida uma mensagem questionando se deseja aplicar o valor da primeira linha da coluna para as demais linhas e caso seja selecionado Sim, o valor da primeira linha da coluna será replicado às demais linhas da mesma coluna.

Observação

Ambas as guias possuem campos editáveis, ou seja, aceitam a informação de dados ou alteração. Isso é necessário para garantir que os dados do arquivo .XML sejam gravados corretamente no Gestão Empresarial, pois podem haver algumas divergências em cálculos decorrentes de critérios de arredondamento. Também garante-se que as codificações do próprio Gestão Empresarial, tais como condição de pagamento, transações, etc. sejam corretamente consideradas.

Os campos % Diferimento e Valor ICMS Dif. estão disponíveis nas guias dos itens da nota fiscal de entrada, para que esses valores possam ser visualizados e editados. Ao processar o recebimento da nota fiscal de entrada, o valor e o percentual do ICMS diferido serão gravados nesse documento.

Os campos **Empresa NFS**, **Série NFS**, **Nr. NFS** e **Seq. NFS** possuem dependência entre si, ou seja, o campo **Série NFS** somente fica habilitado depois de ser informado o campo **Empresa NF**, assim como o campo **Nr. NFS** depende do campo **Série NFS** e o campo **Seq. NFS** depende do campo **Série NFS**.

* Sugestão dos valores referentes ao ICMS Simples Nacional

Forn X Serv.

Realiza a abertura da tela Ligações Fornecedor X Serviços Individual (F403FSE), para manipular a ligação fornecedor x serviço.

## Páginas relacionadas

* [F001TCP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f001tcp.htm)
* [C170 - Itens do documento](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/sped/fiscal-icms-ipi/bloco-c.htm#C170)
* [F000DPL](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f000dpl.htm)
* [F440GNE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f440gne.htm)
* [CPR-000EXFTP-1](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/cpr_000exftp01.htm)
* [F440NPR](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f440npr.htm)
* [ValPagRec](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#ValPagRec)
* [F440CIP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f440cip.htm)
* [Sugestão dos valores referentes ao ICMS Simples Nacional](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/geracao-beneficio-fiscal.htm#suprimentos-simples)
* [F403FSE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f403fse.htm)
