# Identificador de Regra

> **Fonte:** Identificador de Regra — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/cpr_440gerti01.htm  
> **Trilha:**   
> **Telas citadas:** E001TIT, E501RAT, E501TCP, F000MRT, F000RPF, F501TCP  
> **Identificadores de regras:** CPR-440GERTI01

---
## CPR-440GERTI01

**Módulo:** CPR - Compras.

**Finalidade:** alterar o Código do Fornecedor, Transação e Tipo de Título padrão na geração de **alguns tipos de títulos** gerados no fechamento da nota fiscal de entrada. Esse identificador atende todos os impostos.

Alguns impostos tratados nesse identificador possuem uma variável específica. Veja o exemplo do PIS:

* VSFORPIS - Código do fornecedor para a geração do título de PIS
* VSTNSPIS - Transação padrão para geração do título PIS
* VSTPTPIS - Tipo de título padrão para geração do título de PIS

Há 3 variáveis genéricas para tratar os demais impostos. A variável que vai diferenciar o seu conteúdo é a VSTIPTIT. Exemplo:

* VSFORIMP - Código do fornecedor para a geração do título (IPI/ICMS/ICMSDif/PISSubs/COFINSSubs/LIVRE)
* VSTNSIMP - Transação padrão para geração do título (IPI/ICMS/ICMSDif/PISSubs/COFINSSubs/LIVRE)
* VSTIPIMP - Tipo de título padrão para geração do título (IPI/ICMS/ICMSDif/PISSubs/COFINSSubs/LIVRE)

Quando a VSTIPTIT for igual a IPI, o valor das 3 variáveis acima vão corresponder ao IPI. Essa lógica aplica-se aos demais impostos, exceto os que têm variáveis próprias.

**Características:** além de permitir a alteração de fornecedor, transação e tipo para geração do título de imposto, esse identificador tem variáveis com outros conteúdos e objetivos específicos. Veja abaixo:

* VSTIPTIT - Tem os seguintes valores, dependendo do tipo de título gerado pelo sistema no momento da execução da regra:  
  + Geração de título de IPI >> VSTipTit = IPI
  + Geração de título de ICMS >> VSTipTit = ICMS
  + Geração de título de ICMS Dif.Aliquota >> VSTipTit = ICMSDif
  + Geração de título de ICMS Substituto >> VSTipTit = RETICMSSUBST
  + Geração de título de ISS >> VSTipTit = ISS
  + Geração de título de PIS Substituto >> VSTipTit = PISSubs
  + Geração de título de COFINS Substituto >> VSTipTit = COFINSSubs
  + Geração de título de Funrural >> VSTipTit = Funrural
  + Geração de título de INSS >> VSTipTit = INSS
  + Geração do título de IRRF >> VSTipTit = IRRF
  + Geração do título COFINS Retido >> VSTipTit = COFINS
  + Geração do título PIS Retido >> VSTipTit = PIS
  + Geração do título CSLL Retido >> VSTipTit = CSLL
  + Geração de título de Outras Retenções >> VSTipTit = OUTRAS
  + Geração de título de INSS Parte Empresa >> VSTipTit = INSSEMP
  + Geração de título Livre >> VSTipTit = LIVRE

* Campos informativos da nota fiscal de entrada:  
  + VSCODFOR = Código do fornecedor da Nota Fiscal de Entrada
  + VSTNSPRO = Transação de Produto da Nota Fiscal de Entrada
  + VSTNSSER = Transação de Serviço da Nota Fiscal de Entrada

  Nota

  Para impostos com os valores zerados, o tipo de título **LIVRE** não vai gerar o título ao final do processo.
* As variáveis VSNUMPRJ, VSNUMFPJ, VSCTAFIN, VSCTARED e VSCODCCU não recebem valores do sistema no envio para a regra, mas permitem que eles sejam informados na regra e devolvidos para o sistema:

  Observação

  Esse identificador de regras permite retornar um valor para as variáveis de Conta Reduzida (variável VSCTARED), Conta Financeira (variável VSCTAFIN) e Centro de Custo (variável VSCODCCU). O valor retornado por meio dessas variáveis será gravado na tabela de rateio do título (tabela E501RAT) e não na tabela do título em si (tabela E501TCP)

  O sistema grava o rateio na tabela E501RAT, pois lá é possível fazer o rateio para diversas linhas, sendo possível informar, em cada uma delas, um valor diferente para os campos Conta Reduzida, Conta Financeira e Centro de Custo. Todas as telas de processos que envolvem rateios no sistema tem como base a tabela E501RAT e não a tabela do título E501TCP.

  A finalidade de mostrar esses campos no título, por meio da tela Títulos/Manutenção do Contas a Pagar (F501TCP), é gerar relatórios quando o usuário utiliza apenas um registro. Para visualizar os rateios gerados na tabela E501RAT, siga os passos abaixo:

  + Abra a tela Manutenção de Rateios (F000MRT)
  + Informe o tipo de Rotina "12 - Contas a Pagar"
  + Informe o Título e o Tipo
  + Clique no botão Mostrar
  + Com o título carregado, clique no botão Rateio
  + Com isso, o sistema vai exibir a tela Rateios (F000RPF), onde é possível visualizar os campos de Conta Financeira, Conta Reduzida e Centro de Custo

  + VSGERTIT = Variável que possibilita o cancelamento da geração de um título específico. Tem como padrão o valor "S - Sim". Caso "N - Não", o título não será gerado
  + VSCODTRI = Permite modificar o código de tributação na geração do título em questão
  + VSBUSORI = Permite informar qual opção de busca dos rateios para o título em questão ("S - Nota Fiscal"/"N - Transação Títulos")
  + VSVLRIMP = Permite alterar o valor do título de imposto gerado pelo sistema no Contas a Pagar. Para o imposto livre (VSTipTit = LIVRE), é de uso obrigatório, pois nesse caso não há valor pré-definido no sistema: o usuário deve definir qual valor vai compor a geração do título, por isso a nomenclatura "Livre"
  + Todas as variáveis retornam valor para o sistema, exceto VSCODFOR, VSTNSPRO e VSTNSSE. As variáveis de retorno informadas pelo usuário são validadas e, caso haja incoerência nas informações, a nota fiscal não será fechada:  
    - O Fornecedor informado deve estar cadastrado
    - A Transação informada deve estar cadastrada, ter integração com o Contas a Pagar e o campo **Adiciona ou Subtrai** (no cadastro de transações Contas a Pagar) deve ser igual a "1 - Adiciona Duplicatas/Outros"
    - O Tipo de título deve estar cadastrado e deve ser coerente com a transação informada

**Transação:** não se aplica.

**Regra:**

1. Na tabela E001TIT (Tabelas > Transações > Cadastro > Compras > Configuração para geração de títulos de impostos) é possível configurar uma regra para ser executada no momento da geração do título. Nesse caso, não é verificada a existência do identificador de regras CPR-440GERTI01, mas sim a presença da regra na tabela E001TIT. Isso indica ao sistema que o imposto deve ser gerado mediante execução da regra vinculada a ele
   * **Obs.:** nesse cenário, não há a possibilidade de cancelar a geração do título de imposto através da variável **VSGERTIT**. Essa variável está disponível apenas quando a execução for via identificador de regras CPR-440GERTI01 (item 2)
2. Na geração do título de ICMS Substituto, o sistema verifica a existência do identificador de regras CPR-440GERTI01 e executa a regra vinculada a ele

Esta distinção ocorre pois o **ICMS Substituto** não tem as mesmas características de geração dos demais impostos.

**Variáveis disponibilizadas:**

| Nome | Tipo | Observações | Retorna Valor |
| --- | --- | --- | --- |
| VSTIPTIT | ALFA | É uma constante, que dependendo do tipo de título assume os valores definidos na documentação. | N |
| VSCODFOR | NÚMERO | Código do fornecedor da Nota Fiscal de Entrada | N |
| VSTNSPRO | ALFA | Transação de Produto da Nota Fiscal de Entrada | N |
| VSTNSSER | ALFA | Transação de Serviço da Nota Fiscal de Entrada | N |
| VSCODEMP | NÚMERO | Código da empresa da Nota Fiscal de Entrada | N |
| VSCODFIL | NÚMERO | Código da filial da Nota Fiscal de Entrada | N |
| VSNUMNFC | NÚMERO | Número da nota Fiscal de Entrada | N |
| VSCODSNF | ALFA | Código da série da nota Fiscal de Entrada | N |
| VSNUMNFV | NÚMERO | Número da nota fiscal de saída | N |
| VSCPRFIS | NÚMERO | Código fornecedor padrão para geração do título INSS/Funrural | S |
| VSCPRFOI | NÚMERO | Código fornecedor padrão para geração do título IRRF | S |
| VSFORISS | NÚMERO | Código fornecedor da NF para geração do título ISS | S |
| VSFORPIS | NÚMERO | Código do fornecedor para a geração do título de PIS | S |
| VSFORCOF | NÚMERO | Código do fornecedor para a geração do título de COFINS | S |
| VSFORCSL | NÚMERO | Código do fornecedor para a geração do título de CSLL | S |
| VSFOROUR | NÚMERO | Código do fornecedor para a geração do título de Outras Retenções | S |
| VSFORINE | NÚMERO | Código do fornecedor para a geração do título de INSS parte Empresa | S |
| VSCPRTIN | ALFA | Transação padrão para geração do título INSS/Funrural | S |
| VSCPRTRI | ALFA | Transação padrão para geração do título IRRF | S |
| VSCPRTRS | ALFA | Transação padrão para geração do título ISS | S |
| VSTNSPIS | ALFA | Transação padrão para geração do título PIS | S |
| VSTNSCOF | ALFA | Transação padrão para geração do título COFINS | S |
| VSTNSCSL | ALFA | Transação padrão para geração do título CSLL | S |
| VSTNSOUR | ALFA | Transação padrão para geração do título Outras Retenções | S |
| VSTNSINE | ALFA | Transação padrão para geração do título de INSS parte Empresa | S |
| VSCPRTIS | ALFA | Tipo de título padrão para geração do título de INSS/Funrural | S |
| VSCPRTTI | ALFA | Tipo de título padrão para geração do título de IRRF | S |
| VSCPRTTS | ALFA | Tipo de título padrão para geração do título de ISS | S |
| VSTPTPIS | ALFA | Tipo de título padrão para geração do título de PIS | S |
| VSTPTCOF | ALFA | Tipo de título padrão para geração do título de COFINS | S |
| VSTPTCSL | ALFA | Tipo de título padrão para geração do título de CSLL | S |
| VSTPTOUR | ALFA | Tipo de título padrão para geração do título de Outras Retenções | S |
| VSTPTINE | ALFA | Tipo de título padrão para geração do título de INSS parte Empresa | S |
| VSCODTRI | ALFA | Código de tributação do título | S |
| VSBUSORI | ALFA | Opção de Busca dos rateios (S-Nota Fiscal, N-Transação Títulos) | S |
| VSNUMPRJ | NÚMERO | Numero do Projeto | S |
| VSNUMFPJ | NÚMERO | Fase do Projeto | S |
| VSCTAFIN | NÚMERO | Conta Financeira | S |
| VSCTARED | NÚMERO | Conta Contábil Reduzida | S |
| VSCODCCU | ALFA | Centro de Custos | S |
| VSGERTIT | ALFA | Se atribuído 'N' para este campo não irá gerar o titulo | S |
| VSFORRSU | NÚMERO | Código do fornecedor para a geração do título de retenção de ICMS Substituto | S |
| VSTNSRSU | ALFA | Transação padrão para geração do título de retenção de ICMS Substituto | S |
| VSTPTRSU | ALFA | Tipo de título padrão para geração do título de retenção de ICMS Substituto | S |
| VSFORIMP | NÚMERO | Código do fornecedor para a geração do título (IPI/ICMS/ICMSDif/PISSubs/COFINSSubs/LIVRE) | S |
| VSTNSIMP | ALFA | Transação padrão para geração do título (IPI/ICMS/ICMSDif/PISSubs/COFINSSubs/LIVRE) | S |
| VSTIPIMP | ALFA | Tipo de título padrão para geração do título (IPI/ICMS/ICMSDif/PISSubs/COFINSSubs/LIVRE) (ATENÇÃO: é recomendado o uso da variável CprATipImp) | S |
| VSVLRIMP | NÚMERO | Valor do imposto (exclusivo para a geração do título do tipo LIVRE) | S |
| VSGRIIMP | ALFA | Código da guia do imposto | S |
| CprATipImp | ALFA | Tipo de título padrão para geração do título (IPI/ICMS/ICMSDif/PISSubs/COFINSSubs/LIVRE) (igual a variável VSTipImp) | S |
| CPRACODPOR | ALFA | Código do portador do título a pagar | S |
| CPRACODCRT | ALFA | Código da carteira do título a pagar | S |
| CPRNCODNTG | NÚMERO | Código da natureza de gasto | S |

Atenção

Caso o parâmetro global LisVarReg esteja habilitado, a variável ListaVariaveis estará disponível em todos os identificadores de regras do sistema. O conteúdo desta variável lista os campos disponibilizados no identificador de regras em questão.

Não é aconselhada a ativação desse parâmetro global para o uso cotidiano. Esse recurso de listagem dos campos de identificadores auxilia a construção de regras e o Suporte para, por exemplo, depuração ou quando não houver acesso à documentação dos identificadores de regras.

## Páginas relacionadas

* [Títulos/Manutenção do Contas a Pagar (F501TCP)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_financas/f501tcp.htm)
* [Manutenção de Rateios (F000MRT)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_financas/f000mrt.htm)
* [Rateios (F000RPF)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/f000rpf.htm)
* [LisVarReg](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#LisVarReg)
