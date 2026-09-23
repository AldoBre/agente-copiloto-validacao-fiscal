# Impostos

> **Fonte:** F051IMP - Cadastro de Imposto — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f051imp.htm  
> **Trilha:** Ajuda por telas > Cadastros > Controladoria > Tributos  
> **Telas citadas:** F049TTR  
> **Identificadores de regras:** —

---
## Imposto 34 - ICMS Substituto por Estado

Neste imposto, é possível vincular um imposto adicional de tipo 70 - ICMS ST Complementar. O campo do imposto 70 vinculado ao 34 tem aplicação específica para o estado do RS, pois a sua apuração será detalhada na geração do registro 1900 e filhos do SPED Fiscal.

## Imposto 50 - IRRF Exterior - Contratos de Empréstimos de Mercado Externo

Este tipo de imposto é de uso exclusivo para contratos de empréstimo de mercado externo.

## Impostos 53 - IRPJ Lucro Presumido (SPED) e 54 - CSLL Lucro Presumido (SPED)

Para o imposto de tipo 53 - IRPJ Lucro Presumido (SPED), pode ser parametrizado um imposto sobre a diferença de IR devida a mudança de coeficiente (Imposto de tipo 61 - IRPJ - Diferença pela mudança de coeficiente) e um imposto adicional (Imposto de tipo 17 - IRPJ Adicional), esses impostos devem ser cadastrados quando a empresa desejar emitir guias de recolhimento separadas para esses valores (ambos não obrigatórios).

Para que seja possível realizar a apuração do imposto de tipo 54 - CSLL Lucro Presumido (SPED) é necessário que em seu cadastro seja vinculado um imposto do tipo 53 - IRPJ Lucro Presumido (SPED).

## Impostos 55 - IRPJ Lucro Real (SPED) e 56 - CSLL Lucro Real (SPED)

Para o imposto de tipo 55 - IRPJ Lucro Real (SPED), pode ser parametrizado um imposto sobre a diferença de IR devida a mudança de coeficiente (Imposto de tipo 61 - IRPJ - Diferença pela mudança de coeficiente) e um imposto adicional (Imposto de tipo 17 - IRPJ Adicional), esses impostos devem ser cadastrados quando a empresa desejar emitir guias de recolhimento separadas para esses valores (ambos não obrigatórios).

Para que seja possível realizar a apuração do imposto de tipo 55 – IRPJ Lucro Real (SPED) é necessário que em seu cadastro seja vinculado um imposto do tipo 56 - CSLL Lucro Real (SPED).

## Impostos 59 - IRPJ - Imune/Isenta (SPED) e 60 - CSLL - Imune/Isenta (SPED)

Para o imposto de tipo 59 - IRPJ - Imune/Isenta (SPED), opcionalmente, o campo IR Adicional pode ser preenchido com o valor 17 - Adicional. Isso deve ser feito caso queira gerar guias de recolhimento separadas para esses valores.

Quando a empresa possuir a apuração do IRPJ e CSLL é necessário que no cadastro do imposto 59 - IRPJ - Imune/Isenta (SPED) seja vinculado um imposto do tipo 60 - CSLL - Imune/Isenta (SPED).

## Imposto 65 - ISS Retido

Para o imposto 65 - ISS Retido, apenas os campos Código Imposto, Descrição, Tipo, Código Regra e Situação são habilitados para preenchimento. O campo Devido ou Retido é preenchido com **Retido**, não permitido alteração.

Campos disponíveis na regra LSP informada no campo Código Regra:

|  |  |  |  |
| --- | --- | --- | --- |
| Parâmetros de Entrada | | | |
| Campo | Tipo | Descrição | Obrigatório |
| CodEmp | Número | Código empresa | N |
| CodFil | Número | Código filial | N |
| CliFor | Número | Cliente/Fornecedor | S |
| NumNfi | Número | Número da nota | S |
| NumNff | Número | Sequencial da Nota | S |
| SeqIte | Número | Sequência do Item | S |
| DatEmi | Alfa | Data Emissão | S |
| EntSai | Alfa | Entrada ou Saída | S |
| NopOpe | Alfa | Natureza da Operação | S |
| TipMov | Alfa | Tipo Movimento (S = Saída, E = Entrada) | S |
| CodTns | Alfa | Transação | S |
| CodSnf | Alfa | Série | S |
| CodPro | Alfa | Código Produto | S |
| CodSer | Alfa | Código Serviço | S |
| CplPro | Alfa | Descrição complementar Produto/Serviço | S |
| CodDer | Alfa | Derivação | S |
| UniMed | Alfa | Unidade Medida | S |
| ClaFis | Alfa | Classificação Fiscal NCM | S |
| CodClf | Alfa | Classificação Fiscal Interna | S |
| QtdEnt | Número | Quantidade | S |
| VlrCtb | Número | Valor Contábil | S |
| VlrBis | Número | Valor Base ISS | S |
| PerIss | Número | Percentual ISS | S |
| VlrIss | Número | Valor ISS | S |
| ExeReg | Alfa | Define se deve continuar a executar a regra] | S |
| Parâmetros de retorno da regra | | | |
| VlrCtb | Número | Valor Contábil | S |
| VlrBis | Número | Valor Base ISS | S |
| VlrIss | Número | Valor ISS | S |

## Imposto 67 - Débitos especiais

Para o imposto 67 - Débitos especiais é possível associar um imposto do tipo 2 - ICMS, indicando que a base de cálculo é o valor da base de ICMS encontrado nos documentos, ou um imposto do tipo 34 - ICMS ST por estado, indicando que a base de cálculo é o valor da base de ICMS ST encontrado nos documentos.  

Dessa forma pode ser apresentado o recolhimento do Fundo de Combate e Erradicação da Pobreza (FECP) em uma guia estadual separada da apuração do ICMS.  

Quando o imposto 67 é informado, a descrição do campo Imposto Substituto/Secundário é alterado para ICMS/ICMS ST e é possível apenas informar impostos do tipo 02 ou 34.

## Imposto 72 - ISS próprio das instituições financeiras

Permite parametrizar Código,
Descrição,
Tipo,
Código Regra
Situação. Para esse imposto, o campo Imposto Responsabilidade Tributária ficará desabilitado. Para mais informações, confira a documentação sobre a apuração do ISSQN para instituições financeiras.

## Imposto 79 - FAF - Fator de Ajuste de Fruição

No estado do Rio Grande do Sul, o fator de ajuste de fruição é um índice que tem como objetivo ajustar o valor do crédito de ICMS que uma empresa tem direito a utilizar na venda de seus produtos, levando em consideração o percentual de insumos utilizados na produção que foram efetivamente tributados pelo imposto.

A definição deste tipo de imposto pode ser incluído na tela Cadastro de Tabela de Tributação (F049TTR) para a inserção do índice de cálculo da modalidade do FAF.

## Imposto 81 - Fundo de Universalização dos Serviços de Telecomunicações (FUST)

Permite parametrizar o Código, a Descrição, o Tipo, o Código da Regra e a Situação. Para mais informações, consulte a documentação sobre a Apuração do imposto FUST e Funttel (F661I23).

## Imposto 82 - Fundo para o Desenvolvimento Tecnológico das Telecomunicações (Funttel)

Permite parametrizar o Código, a Descrição, o Tipo, o Código da Regra e a Situação. Para mais informações, consulte a documentação sobre a Apuração do imposto FUST e Funttel (F661I23).

### Partilha do ISS

Acessível apenas para os impostos dos tipos "73 - ISS (LC 175/2020)" e "74 - ISS Retido (LC 175/2020)", com o objetivo de detalhar o percentual do imposto a recolher partilhado com o município do prestador do serviço.

**Exemplo:**

| Vigência | Percentual |
| --- | --- |
| 01/2021 | 33,5 |
| 01/2022 | 15 |
| 01/2023 | 0 |

## Impostos 73 - ISS (LC 175/2020) e 74 - ISS Retido (LC 175/2020)

Ao cadastrar um imposto dos tipos 73 ou 74, informe no campo Imposto partilha do ISS um código de imposto do tipo 75 que não tenha sido utilizado em outro imposto dos tipos 73 ou 74. Para estes tipos, é possível também parametrizar os campos a seguir:

* Código do imposto;
* Descrição;
* Tipo;
* Imposto Partilha;
* Código da regra;
* Situação.

## Imposto 75 - ISS Partilha (LC 175/2020)

Cadastre um imposto do tipo 75, informando os campos abaixo:

* Código do imposto;
* Descrição;
* Tipo;
* Situação.

## Páginas relacionadas

* [mercado externo](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_financas/contratos_empréstimos_ mercadoexterno.htm)
* [apuração do ISSQN para instituições financeiras](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/issqn-if.htm)
* [F049TTR](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f049ttr.htm)
* [Apuração do imposto FUST e Funttel (F661I23)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/sped/f661i23 - apuração dos impostos fust e funttel.htm)
