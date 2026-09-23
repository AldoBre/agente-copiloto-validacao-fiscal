# Guia Notas Fiscais de Entrada

> **Fonte:** F000INE - Via Recebimento de Documento Eletrônico — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f000ine.htm  
> **Trilha:** Ajuda por telas > Suprimentos > Gestão de Recebimento > Notas Fiscais de Entrada  
> **Telas citadas:** E000NFC, E095FOR, F000INE, F008RAI, F440CNE, F440GNE, F462CTR  
> **Identificadores de regras:** CPR-000INECM01, CPR-000INECM02

---
Apresenta os registros obtidos dos dados gerais da nota fiscal de entrada, através do arquivo XML após a execução do web service. As notas fiscais apresentadas, após clicar em Mostrar, serão destacadas com a fonte em itálico quando no sistema não existir o cadastro do fornecedor ou da transportadora, conforme CNPJ ou CPF informando no XML da Nota Fiscal Eletrônica ou do Conhecimento de Transporte Eletrônico.

Para identificar qual dos cadastros não existe no sistema, a fonte dos campos CNPJ/CPF Fornecedor ou CNPJ/CPF Transportadora será exibida em vermelho.

Para adequar esta tela para recebimentos de documentos eletrônicos 3.10, os campos Valor adicional ao frete para renovação da marinha mercante, Forma de importação quanto a intermediação , CNPJ do adquirente ou do encomendante e Sigla da UF do adquirente ou do encomendante estão disponíveis para
consulta e serão editáveis quando o tipo de mercado do fornecedor (E095FOR.TIPMER) for **E (Externo/Exterior)** e nenhum deles interferirá no processo de nota.

Natureza da Operação Produto (XML)

Somente para leitura. Esta coluna não será utilizada no processamento, é apenas visual. Carrega o campo E000NFC.NopPro para a guia (5 posições). Ele tem por objetivo apresentar a natureza da operação (CFOP) que veio informada no XML e será carregado somente na versão do documento (XML) 1.10, no entanto, como no modelo "55 - NFe" não existe mais a tag NatOpe, por padrão o campo virá vazio.

Natureza da Operação Serviço (XML)

Somente para leitura. Esta coluna não será utilizada no processamento, é apenas visual. Carrega o campo E000NFC.NopSer para a guia (5 posições). Ele tem por objetivo apresentar a natureza da operação (CFOP) que veio informada no XML e será carregado somente na versão do documento (XML) 1.10, no entanto, como no modelo "55 - NFe" não existe mais a tag NatOpe, por padrão o campo virá vazio.

**Observação**

Este campo poderá receber a natureza de operação através dos identificadores CPR-000INECM01 e CPR-000INECM02 utilizando por exemplo a CPRA\_IDE\_NATOPE na personalização, somente na versão do XML 1.10.

Cond. Pagto.

Condição de pagamento determina as parcelas e vencimentos dos títulos a pagar referentes à nota. Este campo pode ser importado e/ou digitado pelo usuário. Sempre que o parâmetro SugCdPIne estiver como "S - Sim", o sistema atualizará o campo conforme o valor da ordem de compra.

**Observação**

A mensagem "A condição de pagamento sugerida para a nota é "X" e na ordem de compra está "Y". Deseja atualizar a nota com a condição de pagamento da ordem de compra?" será apresenta na seguinte condição:

1. O fornecedor da nota fiscal precisa ser o mesmo da ordem de compra;
2. A filial da ordem de compra na grade do item precisa ser maior que 0 - zero;
3. O número da ordem de compra na grade do item precisa ser maior que 0 - ­zero;
4. Não deve ser sugerida a **Forma de pagamento** na tela F000INE, por exemplo, sugestão vinda das definições do fornecedor. Neste caso, o campo Forma Pgto. Sugestão deve vir zerado ao carregar as notas fiscais.

Após as condições acima estiverem de acordo, os itens abaixo serão analisados para mostrar ou não a mensagem.

* A condição de pagamento na ordem de compra for diferente de zero **E**
* A forma de pagamento da tela F000INE for diferente da forma de pagamento da ordem de compra.

Obs.

Observação da nota fiscal eletrônica. Este campo pode ser alterado e, após processamento da nota fiscal, o seu conteúdo será gravado nas Observações da nota fiscal de entrada gerada (F440GNE).

Ver. Doc. Eletrônico

Permite informar a versão do documento eletrônico.

Importante

Quando a nota fiscal de entrada estiver pendente de processamento, esse campo ficará vazio. A informação será exigida e deverá ser inserida de forma manual.

**Contrato**

Este campo pode ser editado/manipulado quando:

* O campo Contrato estiver zerado, ou seja, quando ele não foi manipulado via regra pela rotina de importação de XML
* O tipo da nota posicionada for "1 - NF Entrada", "6 - NF Produtor", "7 - NF Geração Manual" ou "8 - NF Frete/Serviços Agregados". Os demais tipos não irão permitir edição do campo de Contrato
* A nota não possuir informação de número de ordem de compra nos itens

Ao editar o campo Contrato, ele irá funcionar da seguinte forma na tela:

* Será possível informar contratos do tipo "10 - Financeiro com Saldo", validando se o contrato ainda possui saldo, se está ativo e dentro da sua vigência
* Informando o contrato nos dados gerais, ele será atribuído aos itens
* Ao listar várias notas da tela, caso alguma tenha um contrato já definido pela importação de XML, o mesmo deverá aparecer normalmente na tela, porém, não será possível editar o campo de Contrato desse registro. Um ponto importante é que quando alimentado via importação de XML, pode ser usado outros tipos de contrato
* Ao informar o Contrato na guia de Notas Fiscais de Entrada, o mesmo será sugerido para os itens dessa nota. Para editar este campo, é necessário que os dados gerais da nota tenham informação de Contrato

Ao processar a tela Via Recebimento de Documento Eletrônico, será gerada a nota fiscal de entrada com a informação de Contrato, conforme definido em tela. A atualização do saldo do Contrato do tipo "10 - Financeiro com Saldo", é realizada ao fechar a nota fiscal de entrada.

Cid. ISS

Código da cidade para recolhimento do ISS (Tabela RAIS). Esse código deve ser cadastrado na tela F008RAI.

## Botões

Cálculos

Acessa a tela F440CNE, para a consulta dos valores dos dados gerais da nota fiscal, ou seja, serão exibidos apenas os valores carregados do XML, pois esta tela não realiza cálculos ou modificações nos valores originais.

Parcelas via OC

Este botão é habilitado somente quando a opção Considerar Parcelas da Ordem de Compra estiver selecionada no botão Seleção, o item possuir filial e número da ordem de compra informados e a nota fiscal estiver com situação diferente de **Processada**. Ele permite realizar a herança das parcelas especiais das ordens de compra conforme o item selecionado.

**Contratos**

Abre a tela F462CTR, que permite a consulta dos contratos de compra.

* Nos itens da nota fiscal de entrada será possível informar um contrato de compra dos tipos 1 e 2, além do sequencial do item do contrato
* Será possível informar um contrato comercial apenas se as notas fiscais forem do tipo **1 - NF Entrada, 6 - NF Produtor ou 7 - NF Geração Manual**
* Nos dados gerais da nota fiscal de entrada é permitido informar apenas contratos do tipo **10**. Nesse caso, contratos do tipo **1 e 2** não poderão ser relacionados nos itens

Para mais informações, confira a documentação sobre Contratos de Compra Comerciais (Tipos 1 e 2) no Recebimento Eletrônico.

eDocs

Salva em XML ou PDF os documentos recebidos através do eDocs.

## Páginas relacionadas

* [CPR-000INECM01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/cpr_000inecm01.htm)
* [CPR-000INECM02](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/cpr_000inecm02.htm)
* [SugCdPIne](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#SugCdPIne)
* [F008RAI](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f008rai.htm)
* [F440CNE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f440cne.htm)
* [F462CTR](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f462ctr.htm)
* [Contratos de Compra Comerciais (Tipos 1 e 2) no Recebimento Eletrônico](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/manuais_processos/recebimento-eletronico/recebimento-eletronico.htm#contratos-tipo-1-2)
