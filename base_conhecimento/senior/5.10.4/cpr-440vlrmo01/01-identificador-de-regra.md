# Identificador de Regra

> **Fonte:** Identificador de Regra — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/cpr_440vlrmo01.htm  
> **Trilha:**   
> **Telas citadas:** E440IPC, F440VPR  
> **Identificadores de regras:** CPR-440PRMED01, CPR-440VLRMO01, CPR-440VLRMO02

---
## CPR-440VLRMO01

**Módulo:** CPR - Compras.

**Finalidade:** manipular o valor do movimento de estoque através de regra e das variáveis disponibilizadas.

**Importante**

Não havendo regra ligada ao identificador, o sistema considerará como valor do movimento **apenas o valor líquido do item** (E440IPC.VLRLIQ).

**Características:**

1. essa possibilidade ocorre apenas quando tratar-se de um movimento que será calculado pela nota fiscal de entrada, ou seja, quando não for herdado do movimento de origem ou aplicação do preço médio atual.  
   Ao fechar a nota fiscal de entrada, caso o valor do movimento ainda não esteja calculado ao executar o identificador e não seja atribuído o valor da variável VSVLRMOV na regra, a mesma será retornada como 0 e para notas fiscais que não sejam dos tipos 9 ou 10, será retornada a consistência "Informe Valor do Movimento maior que zero. Produto X, Derivação X, Sequência X" e a nota não será fechada. Nesses casos, é necessário atribuir um valor para a variável VSVLRMOV na regra.

Para notas do tipo 4 - Retorno (Industrialização), 5 - Retorno (Outros) e 7 - NF Geração Manual para produtos, o sistema se comporta da seguinte forma:

* com o identificador de regras CPR-440PRMED01: substitui o valor líquido do item pelo preço médio do produto; senão
* com o identificador de regras CPR-440VLRMO01: o valor do movimento será o valor líquido do item e, havendo uma regra ligada, o valor do movimento será gerado via regra; senão
* cálculo normal de valorização do estoque.

Ainda para esses tipos de notas, quando incluído um novo produto pela tela Valorização do Produto (F440VPR), ele será valorizado com base nos produtos e serviços da nota:

* o identificador é executado uma vez para esse item novo a ser valorizado e uma vez para cada produto/serviço selecionado para compor a valorização. Nesses casos, as variáveis do identificador de regras a ser consideradas são CprANovPro, CprANovDer, CprANovDep, CprNNovQtd e CprATnsEst;
* caso queira acessar as informações dos itens de produto e serviços da nota fiscal de retorno, utilize um cursor na regra buscando por essas informações através da chave da nota, acessada pelas variáveis VSCODEMP, VSCODFIL, VSCODFOR, VSNUMNFC, VSCODSNF do identificador de regras;
* ao contrário dos itens de produto, nos itens de serviço os identificadores de regras CPR-440PRMED01 e CPR-440VLRMO01 não são considerados;

2. o identificador também será executado no fechamento de notas fiscais de entrada quando o produto for do tipo KIT.
3. para notas fiscais do tipo 8 - NF Frete/Serviços Agregados, o identificador será executado somente se a nota possuir um item de produto e a transação do item da nota fiscal de frete possuir uma transação de estoque integrada. Ou seja, o identificador será executado somente para alterar o valor do movimento do próprio item da nota de frete (nota principal). Se a necessidade for alterar a valorização do estoque dos itens das notas de origem, deve-se utilizar o identificador de regras CPR-440VLRMO02.

**Transação:** pode estar ligado a uma transação.

**Variáveis Disponibilizadas:**

| Nome | Tipo | Observações | Retorna Valor |
| --- | --- | --- | --- |
| PerCor | NÚMERO | Percentual de COFINS a Recuperar | N |
| PerPim | NÚMERO | Percentual de PIS a Recuperar na Importação | N |
| VSCODEMP | ALFA | Código da empresa | N |
| VSCODFIL | ALFA | Código da filial | N |
| VSCODFOR | NÚMERO | Código do fornecedor da NFE | N |
| VSNUMNFC | NÚMERO | Número da NFE | N |
| VSCODSNF | ALFA | Código da série da NFE | N |
| VSTIPNFE | NÚMERO | Tipo de NFE | N |
| VSDATENT | DATA | Data da Entrada da NFE | N |
| VSDATEMI | DATA | Data de Emissão da NFE | N |
| VSTNSPRO | ALFA | Transação da NFE para produtos | N |
| VSCODCPG | ALFA | Código da condição de pagamento da NFE | N |
| VSCODPRO | ALFA | Código do produto Movimentado | N |
| VSCODDER | ALFA | Código da derivação do produto Movimentado | N |
| VSCODDEP | ALFA | Código do depósito Movimentado | N |
| VSCODLOT | ALFA | Código do Lote de Fabricação p/ estocagem | N |
| VSDATFAB | DATA | Data de fabricação do Lote | N |
| VSDATVLT | DATA | Data de validade do Lote | N |
| VSQTDREC | NÚMERO | Quantidade recebida do Item | N |
| VSVLRLIQ | NÚMERO | Valor Líquido do Item | N |
| VSVLRICM | NÚMERO | Valor do ICMS do Item | N |
| VSVLRISD | NÚMERO | Valor ICMS substituído destacado do Item | N |
| VSVLRICS | NÚMERO | Valor do ICMS substituído do Item | N |
| VSVLRIPI | NÚMERO | Valor do IPI do Item | N |
| VSVLRIPD | NÚMERO | Valor do IPI presumido do Item | N |
| VSVLRPIS | NÚMERO | Valor do PIS a recuperar do Item | N |
| VSVLRFUN | NÚMERO | Valor do Funrural ou INSS do Item | N |
| VSVLRSEN | NÚMERO | Valor do Senar | N |
| VSVLRDFA | NÚMERO | Valor da diferença de alíquota inter-estadual do Item | N |
| VSVLRBIC | NÚMERO | Valor base do ICMS do Item | N |
| VSVLRBRU | NÚMERO | Valor bruto do Item | N |
| VSVLRDS1 | NÚMERO | Valor do desconto - 1 do fornecedor para o Item | N |
| VSVLRDS2 | NÚMERO | Valor do desconto - 2 do fornecedor para o Item | N |
| VSVLRDSC | NÚMERO | Valor do desconto do Item | N |
| VSVLRDZF | NÚMERO | Valor do desconto referente zona franca para o Item | N |
| VSVLREMB | NÚMERO | Valor embalagem do Item | N |
| VSVLRENC | NÚMERO | Valor encargos financeiros do Item | N |
| VSVLRFIN | NÚMERO | Valor financeiro do Item | N |
| VSVLRFRE | NÚMERO | Valor frete do Item | N |
| VSVLROUT | NÚMERO | Valor outras despesas do Item | N |
| VSVLRSEG | NÚMERO | Valor do seguro do Item | N |
| VSVLRCOR | NÚMERO | Valor do Cofins a recuperar | N |
| VSVLRFEI | NÚMERO | Valor de frete de importação | N |
| VSVLRSEI | NÚMERO | Valor de seguro de importação | N |
| VSVLROUI | NÚMERO | Valor de outras despesas de importação | N |
| VSBCOIMP | NÚMERO | Valor base do cofins a recuperar na importação | N |
| VSCOFIMP | NÚMERO | Valor do cofins a recuperar na importação | N |
| VSBPIIMP | NÚMERO | Valor base do pis a recuperar na importação | N |
| VSPISIMP | NÚMERO | Valor do pis a recuperar na importação | N |
| VSVLRRIS | NÚMERO | Valor de Retenção do ICMS substituído do item da nota fiscal de entrada | N |
| VSVLRIIM | NÚMERO | Valor do imposto de importação do item da nota fiscal de entrada | N |
| VSSEQIPC | NÚMERO | Seqüência do item na nota fiscal de entrada | N |
| CprNVecIcm | NÚMERO | Valor ICMS Cred. Efetivamente | N |
| CprANovPro | ALFA | Novo Produto (Valorização) | N |
| CprANovDer | ALFA | Nova Derivação(Valorização) | N |
| CprANovDep | ALFA | Novo Depósito (Valorização) | N |
| CprNNovQtd | NÚMERO | Nova Quantidade (Valorização) | N |
| CprATnsEst | ALFA | Transação de Estoque (Valorização) | N |
| CPRNVlrAfm | NÚMERO | Valor AFRMM | N |
| VSVLRMOV | NÚMERO | Valor do Movimento do Item | S |
| CprATipIte | ALFA | Tipo do Item (P - Produto / S - Serviço) | N |

Atenção

Caso o parâmetro global LisVarReg esteja habilitado, a variável ListaVariaveis estará disponível em todos os identificadores de regras do sistema. O conteúdo desta variável lista os campos disponibilizados no identificador de regras em questão.

Não é aconselhada a ativação desse parâmetro global para o uso cotidiano. Esse recurso de listagem dos campos de identificadores auxilia a construção de regras e o Suporte para, por exemplo, depuração ou quando não houver acesso à documentação dos identificadores de regras.

## Páginas relacionadas

* [LisVarReg](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#LisVarReg)
