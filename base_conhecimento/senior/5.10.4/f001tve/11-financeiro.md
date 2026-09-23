# Financeiro

> **Fonte:** F001TVE - Transações de Vendas — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f001tve.htm  
> **Trilha:** Ajuda por telas > Cadastros > Transações > Parâmetros por Gestão  
> **Telas citadas:** E660RTC  
> **Identificadores de regras:** —

---
Tipo Título Gerado no Contas a Receber

Tipo de título que esta transação gera no contas a receber, pré-definidos em
Cadastros > Finanças > Contas a Pagar/Receber > Tipos Títulos.

Moeda Título Gerado no Contas a Receber

Código da moeda padrão usada nos títulos do contas a receber,  gerados por
esta transação da nota fiscal de saída, pré-definidas em Cadastros > Finanças >
Moedas-Índices > Cadastro/Atualização.

Soma para Financeiro

Indicativo se o valor líquido do item será somado no valor financeiro, se os valores diversos serão distribuidos nos itens e se haverá rateio financeiro.  

Para geração de títulos, serão considerados também o tipo de título e a transação integrada.

Critério Rateio

Critério de rateio para contas e centros de custo.

É o critério de rateio que define de onde que o rateio
será buscado, quando a forma de rateio for igual
a "1 - Pré-definido c/ Confirmação" e "2 - Pré-definido s/ Confirmação". Por
exemplo, na inclusão de um título, o rateio pode ser buscado do fornecedor,
do tipo de título e do portador, entre outras opções. A tabela 01 apresenta a
lista com todos os critérios de rateio disponíveis:

## Lista de critérios de rateio

| Código | Descrição |
| --- | --- |
| A | Transação (VECRPTJOI) |
| B | Natureza Gasto (RPTJ) |
| C | Produto/Serviço (VEC) |
| D | Família (VEC) |
| E | Agrup. Estoque (VEC) |
| F | Agrup. Produção (VEC) |
| G | Agrup. Custos (VEC) |
| H | Agrup. Comercial (VEC) |
| I | Agrup. Fiscal (VEC) |
| J | Cliente (VRI) |
| K | Representante (VRO) |
| L | Fornecedor (CPI) |
| M | Depósito (E) |
| N | Tipo de Título (RP) |
| O | Grupo Rec./Pag (RP) |
| P | Portador (RP) |
| Q | Projeto (VECRPTIJOI) |
| R | Tipo Documento (T) |
| S | Conta Interna (T) |

## Exemplo

* Título: XY;
* Tipo de Título: 01;
* Fornecedor: 999;
* Transação: 90500;
* Critério Rateio da transação 90500: ALN.

Nesse caso, o sistema:

1. Verifica se a transação "90500" tem rateio cadastrado. Existindo rateio
   cadastrado, o movimento de inclusão de título recebe o rateio da transação; caso
   contrário
2. Verifica se o fornecedor "999" tem rateio cadastrado. Existindo rateio
   cadastrado, o movimento de inclusão de título recebe o rateio do fornecedor; caso contrário
3. Verifica se o tipo de título "01" tem rateio cadastrado. Existindo rateio
   cadastrado, o movimento de inclusão de título recebe o rateio do tipo de título; caso contrário
4. Define o rateio conforme os demais parâmetros de busca do sistema, não
   encontrando, impossibilita a inclusão do título ou abre a tela de definição de
   rateio para que o usuário defina o rateio do movimento manualmente.

Observação

Para a formação do rateio no movimento do título, o sistema busca em
cada um dos critérios de rateio, um rateio cadastrado. Fazendo isso do primeiro
critério cadastrado ao último.

Quando informadas opções diferentes de "A - Transação", "I - Agrup.
Fiscal", "J - Cliente", "L - Fornecedor" e "Q - Projeto" para as notas fiscais da
gestão de impostos, ao digitar uma nota fiscal de saída no módulo, será emitida a seguinte
mensagem: "Critério "x" para busca do rateio padrão inválido para: E660RTC!".
Todas as outras opções são dirigidas às gestões de mercado e suprimentos.

Conta Financeira a Classificar

Conta financeira a classificar.

Conta Contábil a Classificar

Conta contábil a classificar.

Centro de Custo a Classificar

Centro de custo a classificar.

## Páginas relacionadas

* [Tipos Títulos](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f002tpt.htm)
* [Moedas-Índices](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f031aim.htm)
