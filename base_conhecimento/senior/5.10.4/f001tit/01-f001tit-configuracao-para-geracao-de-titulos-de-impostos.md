# F001TIT - Configuração para Geração de Títulos de Impostos

> **Fonte:** F001TIT - Configuração para Geração de Títulos de Impostos — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f001tit.htm  
> **Trilha:** Ajuda por telas > Cadastros > Transações > Parâmetros por Gestão  
> **Telas citadas:** E001TNS, E051DIS, E051IMP, F001TIT, F055PPF, F070FEF  
> **Identificadores de regras:** —

---
Ajuda por telas > Cadastros > Transações > Parâmetros por Gestão > Configuração para geração de títulos de impostos (Compras/Vendas)

Tela destinada à configuração da geração de títulos de impostos no
Contas a Pagar no fechamento de notas fiscais de entrada e saída.

Transação

Código da transação ligada ao tipo de título, para transações de nota fiscal, o sistema verifica apenas a transação dos Dados Gerais do documento.

Filial

Código da filial ligada ao tipo de título.

Tipo Imposto

Código do tipo de imposto que gerará o título.

* 1 - IPI
* 2 - ICMS
* 3 - ICMS Dif. Alíquota
* 5 - ISS
* 7 - PIS Substituto
* 8 - COFINS Substituto
* 9 - FUNRURAL
* 10 - INSS
* 11 - IRRF
* 22 - COFINS - Retenção
* 23 - PIS - Retenção
* 24 - CSLL - Retenção
* 25 - Outras - Retenção
* 29 - INSS Empresa
* 52 - SENAR/SENAT
* 76 - Agronegócio
* 97 - Livre

Exibir apenas registros ativo

Quando marcado, exibe na grade apenas os registros ativos.

Código  Imposto

Código do imposto que gerará o título.  
Registros gravados na tabela E051IMP e cadastrados em
Tabelas > Contábil > Impostos > Cadastro.

Fornecedor

Código do fornecedor do título a gerar.

Tipo Título

Código do tipo do título a gerar.  
Registros gravados na tabela E051IMP e cadastrados em
Tabelas > Financeiro > Tipos Títulos.

Transação

Código da transação do Contas Pagar integrada com a transação que gerará o título.  
Registros gravados na tabela E001TNS.

## Parâmetros para Geração de Títulos no Contas a Pagar

Grid para a configuração das informações necessárias para a geração dos títulos.

A tela de configuração da grade é acessada através do caractere "C" em azul no
seu canto superior esquerdo.   
As opções habilitadas são exibir/ocultar, ordenar, alterar tamanho e alterar a
posição das colunas.

## Campos da Grid

Sel

Campo para marcação dos registros a processar, tanto nas inclusões como nas
alterações.

Transação

Código da transação da nota fiscal de entrada ou saída.

Descrição (Transação)

Descrição da transação da nota fiscal de entrada ou saída.

Filial

Código da filial configurada para a geração do título.

Informando "0"(zero) significa que a configuração
valerá para todas as filiais. Informando um código existente, a configuração
valerá somente
para esta filial.

Tipo

Tipo do imposto.

Descrição  (Tipo)   
Descrição do tipo de imposto.

Cód. Imposto   
Código imposto.

Nota

Se o campo Tipo Imposto for especificado como "76 - Agronegócio", apenas os impostos que foram configurados na tela de Configuração de Impostos para a Filial (F055PPF) com a opção Apurar definida como "N - Não" serão exibidos nesse campo.

Forn.Tit

Fornecedor cadastrado na tabela E095For ao qual pertencerá o título de imposto.

Nome (Forn.Tit)

Nome do fornecedor.

Tipo Tit.   
Código do tipo do título gerado.

Descrição (Tipo Tit)

Descrição do tipo de titulo conforme código atribuído ao campo Tip Tit.

Trans. Tit.

Código da transação integrada com a transação da nota fiscal de compras ou vendas.

Descrição (Trans.Tit)

Descrição da transação integrada com a transação da nota fiscal de compras ou vendas.

Data Fato Ger.Tit Fis.

Data do fator gerador pessoa física. O período de apuração do título e da guia de recolhimento serão preenchidos conforme a opção selecionada do campo:

* "1 - Data de Emissão": data da emissão da nota fiscal;
* "2 - Data de Entrada": data de entrada da nota fiscal;

* "3 - Data Primeiro Vencimento": data do primeiro vencimento das parcelas da nota fiscal;

* "4 - Data Último Vencimento": data do último vencimento das parcelas da nota fiscal.;
* "5 - Todas parcelas com ajuste na Primeira": data de todos os vencimentos das parcelas da nota fiscal e com ajuste de valor na primeira parcela. Ou seja, se a nota tiver três parcelas, serão gerados três títulos/guias para o imposto com base na data de emissão das parcelas da nota fiscal;
* "6 - Todas parcelas com ajuste na Última": data de todos os vencimentos das parcelas da nota fiscal e com ajuste de valor na última parcela. Ou seja, se a nota tiver três parcelas, serão gerados três títulos/guias para o imposto com base na data de emissão das parcelas da nota fiscal;
* "7 - Último dia do mês da Data de Emissão": último dia do mês a partir da data de emissão da nota fiscal;
* "8 - Último dia do mês da Data de Entrada": último dia do mês a partir da data de entrada da nota fiscal.

Data Fato Ger.Tit Jur.  
Data do fator gerador pessoa jurídica. Para preenchimento desse campo siga as opções elencadas no campo Data Fato Ger.Tit Fis.

Notas

* A data de emissão das parcelas da nota fiscal, nas opções "5 - Todas parcelas com ajuste na Primeira" e "6 - Todas parcelas com ajuste na Última", corresponde a data escolhida para geração das parcelas (data de emissão ou data de entrada), nos casos em que a data de emissão seja diferente da data de entrada da nota fiscal.
* Para o "INSS parte Empresa"  o fato gerador sugerido é "2", para os demais
  impostos é "1", permitindo alteração.

Cód.Trib.

Campo informativo livre, não relacionado a nenhuma tabela.

Regra

Poderá ser informada uma regra para cálculo ou sugestão.

Observação

Disponibilizada a variável "VSGriImp" (Código do imposto da
guia), podendo ser associada a uma regra para a geração de títulos e na baixa
dos títulos do contas a pagar.

Sit

Situação do registro.

Cód. Dis. Fis.   
Código do Dispositivo Fiscal, relacionada a tabela E051DIS. Este campo possui o valor padrão "0 - Zero".

Descrição (Cód. Dis. Fis.)

Descrição relacionada ao campo Cód. Dis. Fis..

Dias Vcto.   
Indica o número de dias que irá somar a data de vencimento calculada pelo parâmetro Data Fato Ger.Tit Jur.. Este campo possui o valor padrão "0 - Zero".

Crit. Vct.   
Indicativo do critério de definição de vencimento do título a pagar.

Descrição (Crit. Vct.)   
Descrição relacionada ao campo Crit. Vct..

**Importante**

Os campos "Cód. Dis. Fis.", "Dias Vcto.", "Crit. Vct." e "Descrição (Crit. Vct.)" estarão disponíveis para a parametrização quando na tela de Parâmetros da Filial para Tributos (F070FEF), o campo "Programa de Incentivo ao Algodão" estiver parametrizado com uma das opções homologadas.

Quando houver o preenchimento destes campos, e o Tipo de imposto for "02 - ICMS":

* O título será gerado com o valor calculado na nota fiscal para o código do dispositivo fiscal informado;
* Com relação aos campos "Dias Vcto." e "Crit. Vct.", caso informados, serão considerados para cálculo da data de vencimento do título quando os campos "Data Fato Ger.Tit Fis" e "Data Fato Ger.Tit Jur." forem informados o valor: "1 - Data de Emissão", que indica a data da emissão da nota fiscal.

## Botões

Mostrar

Exibe na grade os registros que atendem aos filtros informados.

Processar

Processa os registros marcados na grade.

Duplicar

Duplica registros existentes marcados na grade. Na tela de duplicação existe a caixa de seleção Duplica já existente. Se esta opção for marcada, os registros selecionados para duplicação serão duplicados para empresas, filiais ou transações que já possuírem os registros cadastrados. Se estiver desmarcada, os registros selecionados para duplicação não serão duplicados caso as empresas, filiais ou transações já possuírem os registros cadastrados.

Cancelar

Cancela o a exibição dos registros e limpa a tela.  
Não altera a situação de registro já
gravados.

Marcar

Marca todos os registros na grade simultaneamente.

Desmarcar  
Desmarca todos os registros na grade simultaneamente.

Aplicar

Aplica um determinado valor informado para todas as linhas da mesma coluna.

Transação

Exibe a tela de consulta de
transações do registro posicionado na grade referente ao campo
Transação.

Fornecedor

Exibe a tela de informações de fornecedores do registro posicionado na *grid*.

Tran.Geração

Exibe a tela de consulta de
transações do registro posicionado na grade referente ao campo
Trans.Tit..

Tipo de remessa para o exterior

 Esse campo somente ficará ativo quando o tipo do imposto
informado for igual a "50-IRRF Exterior" sendo obrigatório. Esse
campo servirá como base na busca das definições cadastradas para
a geração dos títulos de IRRF Exterior, ou seja, para cada tipo
de remessa poderá (em teoria será diferente) haver uma
parametrização diferente para o mesmo imposto.

Descrição Rem.(tipo Rem.Ext.)   
 Mostra a descrição do tipo de remessa para o exterior.

## Identificadores de Regra

|  |  |
| --- | --- |
| CPR | 440GERTI01 |

## Páginas relacionadas

* [Ajuda por telas](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/ajuda-telas.htm)
* [Tabelas > Contábil > Impostos > Cadastro](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f051imp.htm)
* [Tabelas > Financeiro > Tipos Títulos](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f002tpt.htm)
* [F070FEF](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070fef.htm#Programa_de_Incentivo_Ao_Algodao)
* [informações de fornecedores](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f095inf.htm)
* [440GERTI01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/cpr_440gerti01.htm)
