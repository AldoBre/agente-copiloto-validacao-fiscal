# Parâmetros Saída

> **Fonte:** F070PSE - Parâmetros Fiscais de produtos e serviços por filial e estado — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070pse.htm  
> **Trilha:** Ajuda por telas > Cadastros > Mercado e Suprimentos > Parâmetros Fiscais  
> **Telas citadas:** F009PPE, F019TIR, F051DIS, F075PRO  
> **Identificadores de regras:** COM-000ALDIF01, GER-000GRPFS01

---
Permite o cadastro do adicional de ICMS para o FCP dos produtos ou serviços para um determinado estado.

Filial

Código da filial.

Fantasia (Filial)

Exibe o nome fantasia da filial.

Início vigência

Data de início da vigência

Estado

Sigla do estado.

Produto/Serviço

Código do produto/serviço.

Descrição p/Nota Fiscal

Exibe a descrição do produto/serviço para impressão na nota fiscal, informada no campo Descrição da tela Cadastro de Produtos (F075PRO).

% ICMS FCP destino

Alíquota do ICMS para o fundo de combate a pobreza.

Cód. Dis. Fis.

Código do dispositivo cadastrado na tela F051DIS.

% ICMS UF destino

Percentual de ICMS interno especial para o estado de destino.

% Redução Base ICMS Destino

Percentual de redução da base de ICMS na UF de destino.

Tributa Difal

Indica se o produto tributa ICMS na UF de destino. Ao inserir um novo registro, este campo é sugerido de acordo com o cadastro de produto. Através da configuração deste campo para a UF da respectiva filial, é possível definir se a operação deve calcular a parte do DIFAL relacionada a UF de Origem. Antes, o cálculo do DIFAL para UF de Origem só ocorria quando a operação calculasse também o ICMS normal. Com esta parametrização é possível também optar por não calcular o DIFAL na UF de Origem mesmo quando a operação calcular ICMS normal.

Importante

* A partir de 01/01/2022, o Recurso Extraordinário nº 1.287.019/DF tornou o recolhimento do DIFAL inconstitucional, porém a lei complementar 190/2022 oficializa o recolhimento do DIFAL a partir de 04/04/2022 ou 01/01/2023 (aguardando definição da data oficial de retomada).
* Para atender o que foi determinado no julgamento deste recurso, não há mais a necessidade das empresas calcularem este imposto. Desta forma, estando o campo Tributa Difal definido igual "N - Não", desativa o cálculo do DIFAL (inclusive via identificador de regra COM-000ALDIF01) de acordo com o período em que as legislações estão vigentes ou então, para atender a processos administrativos que determinam o não recolhimento do DIFAL.

Mod. ICMS destino

Código da modalidade da base de cálculo do ICMS na UF de destino.

Sit. Trib. ICMS

Código da situação tributária do ICMS na UF de destino.

Observação

Este campo assume a posição que era ocupada pelo campo de usuário habilitado pelo identificador de regras GER-000GRPFS01.

% Diferimento Saída

Percentual de diferimento do item de produto da nota fiscal de saída.

% Diferimento Entrada

Percentual de diferimento do item de produto da nota fiscal de entrada.

Red. Alíquota ICMS

Indica se o percentual de redução da base de cálculo de ICMS deve ser considerado na alíquota de ICMS da UF de origem para fins de cálculo do DIFAL.

## Exemplo - Venda de SP para RO:

Neste exemplo, os produtos do Convênio já possuem ligação com a filial SP e com todos os estados da região Norte, e na ligação está informada a alíquota de ICMS de 5,6% para as UFs de destino.

**Importante**

O campo **% Redução** deve ser previamente cadastrado na tela Reduções e Acréscimos de bases de Cálculos de Impostos - Por Estado (F019TIR) e atribuído ao item da nota fiscal de saída.

Para acessar a documentação mais detalhada sobre cálculo de DIFAL, clique aqui.

* Valor da nota fiscal: **R$ 10.300,00**;
* A NT 2015.003 prevê alíquota de 7%, porém o convênio ICMS 52/91 prevê a alíquota de 4,1% e orienta que a base de cálculo seja reduzida de forma a gerar a mesma carga tributária, então:   
  % Redução ICMS = ((4,1 / 7) - 1) x 100 = **41,42857**;
* O percentual de redução é aplicado na alíquota de ICMS da UF de origem (alíquota do item da nota de venda): **7% - 41,42857% = 4,1%** (alíquota interestadual da UF de origem);
* Cálculo da base de cálculo de ICMS (R$ 10.300,00) desconsiderando o percentual de redução:
  + Cálculo do DIFAL:  
    UF Origem: R$ 10.300,00 x 4,1% = R$ 422,30;  
    UF Destino: R$ 10.300,00 x 5,6% = R$ 576,80;  
    Diferencial: R$ 576,80 - R$ 422,30 = R$ 154,50;
  + Considerando os percentuais de partilha vigentes no ano de 2016:  
    UF de origem = 60% - R$ 92,70;  
    UF de destino = 40% - R$ 61,80.

Base ICMS Integral Origem

Se este campo estiver igual a "S - Sim", no cálculo do DIFAL será considerado o valor da base integral da origem (sem aplicação da redução de base de cálculo).

Observação

* Em caso de venda interestadual para consumidor final, para que o diferencial de alíquota com o ICMS reduzido na nota fiscal seja aplicado no cálculo do DIFAL quando o produto no estado de origem possuir um benefício fiscal de redução de base de cálculo, o cenário deve estar previsto na legislação estadual do contribuinte. Quando não houver previsão legal para efetuar o cálculo com redução na base, o valor do ICMS da operação será considerado sem a redução;
* Quando o campo Red. Alíquota ICMS estiver configurado igual a "S - Sim", a redução será realizada na alíquota, utilizando a base sem redução.

% Red. Base DIFAL

Percentual de redução da base do DIFAL. Esse campo é utilizado para os cálculos de DIFAL do tipo "12 - Dupla c/ aplicação da diferença de alíq. c/ redução de base de cálculo". Para verificar a utilização desse valor no cálculo do DIFAL acesse a documentação da tela F009PPE.

## Páginas relacionadas

* [F075PRO](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075pro.htm)
* [F051DIS](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f051dis.htm)
* [COM-000ALDIF01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/com_000aldif01.htm)
* [F019TIR)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f019tir.htm)
* [aqui](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/diferencial-de-aliquota.htm)
* [F009PPE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f009ppe.htm)
