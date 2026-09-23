# F070FCA - Cadastro de Filiais

> **Fonte:** F070FCA - Cadastro de Filiais — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070fca.htm  
> **Trilha:** Ajuda por telas > Cadastros > Filiais  
> **Telas citadas:** E070AFI, F000PPD, F008CEP, F070DUP, F070FCA  
> **Identificadores de regras:** —

---
Ajuda por telas > Cadastros > Filiais > F070FCA - Cadastro de Filiais

Esta tela permite parametrizar o cadastro das filiais da empresa.

## Processo

Na sugestão da transação dos dados gerais da nota fiscal de saída do tipo 1, 10 o
sistema sugere a Transação padrão para NF saída de produtos do
estabelecimento quando o tipo da empresa for 1, caso contrário sugere a
Transação padrão para NF saída de produtos adquiridos p/comercialização.

Obrigatoriedade do Fornecedor, Unidade de Medida e Valor de Frete por UM: Quando o tipo
de empresa for 5 e o frete for CIF estes campos são obrigatórios. Quantidade a Entregar
nos itens de pedido: Quando o tipo de empresa for 5 o sistema mostra este campo permitindo
que o mesmo seja utilizado na rotina de programação de entregas do pedido. Este campo é
utilizado para representar a quantidade máxima a entregar (programar) do item.

Tratamentos para empresas do tipo 4: Quando o tipo de empresa for 4 o sistema libera os
seguintes processo e informações para o usuário: - Rotina de preparação de CTRC via
coleta. - Campos Estado Veículo, Tipo Remetente, CNPJ Remetente, Insc.Est. Remetente,
Estado Remetente, Município Remetente, Código Remetente, Código Destinatário,
Distância (em Km), Forma Cálculo do Frete, SEC/CAT, Ademe, Taxa de Coleta, Pedágio nas
telas de nota fiscal Comercial/Impostos. - Página Composição do Conhecimento de
Transporte na tela de nota fiscal Comercial/Impostos.

## Campos

Filial

Código e nome da filial.

Tipo Empresa

Tipo de empresa.

Observação

Quando esse campo for configurado como "7 - Produtor rural", a emissão da Nota Fiscal Eletrônica será feita por pessoa física (CPF). Para mais informações sobre o processo, consulte a documentação. Se o produtor rural possuir CNPJ, o tipo de empresa deve ser "99 - Outros" para evitar problemas ao inutilizar notas.

Para inutilização de produtor rural com CPF, deve-se cadastrar na tela de configuração de parâmetros dinâmicos (F000PPD) o parâmetro NOTAFISCAL.INUTILIZACAO.PRODUTORRURAL igual a "S". Esta funcionalidade está disponível apenas para o estado do MT.

**Importante**

Para empresas que são apenas transportadoras, deve ser utilizada a opção **04 - Transportadora/Rev./Retalhista)**, e não a **06 - Indústria e Transporte**, pois para transportadoras o campo 15 do registro 0000 do SPED Fiscal deve ser gerado com valor **1 (Outros)**, e não **0 (Industrial ou equiparado a industrial)**, sendo que ele toma por base o preenchimento do campo **Tipo Empresa**.

Benefício Fiscal

Indicativo do tipo de benefício fiscal. Esse campo é utilizado no módulo de mercado para balizar o cálculo do imposto de zona franca. Caso o campo esteja configurado com os valores "1", "2", "3" ou "4", o sistema permite o cálculo de zona franca nos documentos do módulo de mercado. Caso esteja zerado, o cálculo não será realizado.

Código SUFRAMA

Campo esta ligado ao campo Beneficio fiscal quando informado e necessário que
seja informado o código da suframa.

Utiliza tabela CEP

Indicativo se utiliza a tabela de CEP.

Utiliza Período Venda

Indicativo se utiliza a período de venda.

Filial como Cliente

Código da filial como cliente.

Filial como Fornecedor

Código da filial como fornecedor.

Fantasia

Nome de fantasia da filial.

Inscrição Estadual

Inscrição estadual.

**Importante**

Não é permitido informar o caractere barra (/), no campo Inscrição Estadual.

Inscrição Municipal

Inscrição municipal.

Inscrição Municipal NFs

Inscrição municipal da filial da empresa que será impressa na NFS-e. Quando este campo não for informado, é utilizada a inscrição municipal informada no campo Inscrição Municipal.

CNPJ

Número do CNPJ. Para que não seja possível cadastrar mais uma filial para o
mesmo CNPJ, é necessário definir o valor do parâmetro global FilCgcRep para N (Não).

Identificação Fiscal

Número de Identificação Fiscal.

Observação

Caso o parâmetro global FilCgcRep estiver definido como **S-Sim**, o sistema avisa se existe outra filial com a mesma identificação fiscal, porém não bloqueia seu cadastro.

CEP

Número do CEP.

CEP Inicial

Receberá o número
inicial da faixa do CEP informado para a filial. Este campo será usado na
validação da ligação Serviço x CEP, permitindo que o sistema encontre
a faixa a qual ele pertence para verificar o percentual da ligação Serviço x
CEP.

Observação

Era usado o CEP da filial da Nota Fiscal/Pedido/Ordem de
Compra/etc. para carregar o percentual de ISS definido na ligação Serviço x
CEP, o que obrigava o cadastro de um CEP inicial da tabela de
CEPs (e não um CEP entre o intervalo inicial e final de uma localidade) para
que ele pudesse ser usado na ligação Serviço x CEP.

Endereço/Número

Endereço e número.

Complemento

Complemento do endereço

Código Cidade ISS

Código do ISS da cidade.

Bairro

Bairro.

Cidade

Cidade.

Estado

Unidade da Federação.

CEP Entrega

CEP do endereço de entrega.

Endereço Entrega

Endereço de entrega.

Complemento Entrega

Complemento do endereço de entrega.

Bairro Entrega

Bairro da entrega.

Cidade Entrega

Cidade da entrega.

**Estado Entrega**

Unidade da federação da entrega.

CEP Cobrança

CEP do endereço de cobrança.

Endereço Cobrança

Endereço de cobrança.

Complemento Cobrança

Complemento do endereço de cobrança.

Bairro Cobrança

Bairro da cobrança.

Cidade Cobrança

Cidade da cobrança.

Estado Cobrança

Unidade da Federação da cobrança.

Telefone

Os dois primeiros dígitos indicam o DDD, caso a quantidade total de números é dez ou onze. Os últimos oito ou nove dígitos indicam o telefone.

FAX

Número do FAX.

Caixa Postal

Endereço postal.

E-mail

Endereço eletrônico.

Diferença Alíquota

Indicativo se tem diferencial de alíquota.

Agrupamento de Filiais

permite configurar uma filial com pertencente a um agrupamento de filiais (E070AFI).

Filial Matriz

Indicativo se a filial cadastrada é a matriz da empresa. Não será permitido ter mais de uma filial matriz por empresa. Caso estiver como "S - Sim" no cadastro de uma filial e a empresa já tiver
outra filial parametrizada como filial matriz, será apresentada a mensagem **Para a
Empresa X já existe a Filial Y configurada como filial matriz**.

**Cadastro de atividade econômica da pessoa física**

Utilizado na geração do registro R-2055 da EFD-Reinf.

Mecanismo apoio ao Comércio Exterior do Serviço

Mecanismo de apoio/fomento ao Comércio Exterior utilizado pelo prestador do serviço. Com as opções:

* 01 - Nenhum;
* 02 - ACC - Adiantamento sobre Contrato de Câmbio – Redução a Zero do IR e do IOF;
* 03 - ACE – Adiantamento sobre Cambiais Entregues - Redução a Zero do IR e do IOF;
* 04 - BNDES-Exim Pós-Embarque – Serviços;
* 05 - BNDES-Exim Pré-Embarque - Serviços;
* 06 - FGE - Fundo de Garantia à Exportação;
* 07 - PROEX - EQUALIZAÇÃO
* 08 - PROEX - Financiamento.

## Botões

Par. Dinâmicos

Abre a tela Configuração de parâmetros (F000PPD).

**Duplicar**

Abre a tela Duplicação de Filial (F070DUP).

## Parâmetros globais

| Nome | Descrição |
| --- | --- |
| UtiViaCep | Utilizar o WebService ViaCep para buscar dados de CEPs não cadastrados na tela F008CEP |

## Páginas relacionadas

* [Ajuda por telas](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/ajuda-telas.htm)
* [documentação](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/manuais_processos/nota-fiscal/nfe-pessoa-fisica.htm)
* [F000PPD](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000ppd.htm)
* [FilCgcRep](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm)
* [Duplicação de Filial (F070DUP)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070dup.htm)
* [UtiViaCep](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#UtiViaCep)
