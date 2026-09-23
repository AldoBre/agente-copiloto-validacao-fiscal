# Identificador de Regra

> **Fonte:** Identificador de Regra — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/com_000alsub01.htm  
> **Trilha:**   
> **Telas citadas:** —  
> **Identificadores de regras:** COM-000ALSUB01, VEN-140ARICS01

---
## COM-000ALSUB01

**Módulo:** COM - Comercial.

**Finalidade:** Alterar os valores (percentual, base e valor) referentes a substituição de PIS, COFINS, ICMS e retenção de ICMS Substituto, quando do cálculo destes valores.  

Chamado quando um item de produto executar um cálculo de substituição de PIS, COFINS e ICMS. A regra não é chamada se o item não calcular o valor de substituição, ou seja, caso exista algum parâmetro que faça com que o sistema não calcule substituição, a regra também não será chamada.

A regra é executada no cálculo do pedido e da nota. Neste caso é necessário que o cálculo seja realizado no pedido ou na nota fiscal, e não em ambos, pois desta forma, o sistema irá recalcular o valor já calculado no pedido.

O identificador poderá ser chamado algumas vezes durante o cálculo do item, seja na alteração ou inclusão.

**Características:** Sempre que este identificador estiver ativo, alterando o cálculo padrão do ERP para a substituição, faz-se necessária a ativação do identificador VEN-140ARICS01 para que não seja efetuada a rotina de ajuste do valor de substituição no fechamento das notas fiscais de saída. Isso garante que o valor de substituição calculado via regra não seja alterado pelo Gestão Empresarial | ERP.

**Transação:** Não se aplica.

**Regra:**

Definir Numero VSICMNOR;

Definir Numero VSVLRIPI;

Definir Numero VSBASINI;

Definir Numero VSQTDE;

Definir Numero VSPREUNI;

Definir Alfa VSCODSUB;

Definir Alfa VSSIGUFS;

Definir Alfa VSCODPRO;

Definir Alfa VSCODDER;

Definir Numero VSCLIFOR;

Definir Alfa VSTIPSUB;

Definir Alfa VSORIGEM;

Definir Alfa VSCLICON;

Definir Alfa VSCODTNS;

Definir Numero VSBSIATU;

Definir Numero VSVLRICS;

Definir Numero VSPERICS;

Definir Numero VSVlrFre;

Definir Numero VSVlrOut;

Definir Numero VSVlrEmb;

Definir Numero VSVlrEnc;

Definir Numero VSVlrSeg;

Definir Numero VSVlrFrd;

Definir Numero VSVlrOud;

Definir Numero VSVlrDzf;

Definir Numero VSVlrRis;

Definir Numero VSVlrDar;

Definir Numero VSNumero;

Definir Alfa VSCodSnf;

Definir Numero VSSeqIte;

Definir Numero VSPerIcm;

Definir Numero VSEmpTpr;

Definir Alfa VSCodTpr;

Definir Numero VSDefBcs;

Definir Numero VenNFilPed;

Definir Numero VenNNumPed;

Definir Numero VenNSeqIpd;

Definir Numero VenNSeqIsp;

Definir Numero VenNVlrBru;

Definir Numero VenNVlrDsc;

Definir Numero VenNVlrDs1;

Definir Numero VenNVlrDs2;

Definir Numero VenNVlrDs3;

Definir Numero VenNVlrDs4;

Definir Numero VenNVlrDs5;

Definir Alfa VenACodStr;

Definir Alfa VenACstCof;

Definir Alfa VenACstIpi;

Definir Alfa VenACstPis;

**Variáveis Disponibilizadas:**

| Nome | Tipo | Observações | Retorna Valor |
| --- | --- | --- | --- |
| VenNNumOct | NÚMERO | Número do orçamento | N |
| VenNVerOct | NÚMERO | Versão do orçamento | N |
| VSMntBsi | ALFA | Mantém a base de substituição tributária com valor de substituição zerado. Valores possíveis para esta variável: S ou N.  **Importante**  Caso o parâmetro global MntBasIst estiver como "S - Sim", a base será mantida independente do retorno dessa variável. | S |
| VSVLRIPI | NÚMERO | Valor de IPI | N |
| VSBASINI | NÚMERO | Valor base Inicial | N |
| VSQTDE | NÚMERO | Quantidade de entrada da unidade de medida de estoque | N |
| VSPREUNI | NÚMERO | Preço unitário na unidade de medida do fornecedor | N |
| VSCODSUB | ALFA | Código da substituição | N |
| VSSIGUFS | ALFA | Estado | N |
| VSCODPRO | ALFA | Código do Produto | N |
| VSCODDER | ALFA | Código da Derivação | N |
| VSCLIFOR | NÚMERO | Código do Cliente ou Fornecedor dependendo da origem. | N |
| VSTIPSUB | ALFA | Indica o tipo da substituição (ICMS,PIS ou COFINS) | N |
| VSORIGEM | ALFA | Origem da chamada da Regra ("PED" - Pedido,"OCP" - Ordem de Compra, "NFS" - Nota Fiscal Saída,"NFE" - Nota Fiscal Entrada, "OCT" - Orçamento, "IMP" - Tributos, UST - Custos) | N |
| VSCLICON | ALFA | Indicativo se o cliente é contribuinte ou não. Terá valor somente quando a nota fiscal de entrada for tipo 2,3,4 ou 5 | N |
| VSCODTNS | ALFA | Transação do item | N |
| VSVlrFre | NÚMERO | Valor de frete do item | N |
| VSVlrEmb | NÚMERO | Valor de embalagens do item | N |
| VSVlrEnc | NÚMERO | Valor de encargos do item | N |
| VSVlrSeg | NÚMERO | Valor de seguros do item | N |
| VSVlrFrd | NÚMERO | Valor de frete destacado do item | N |
| VSVlrOud | NÚMERO | Valor de outras despesas destacado do item | N |
| VSVlrDzf | NÚMERO | Valor do desconto na zona franca | N |
| VSVlrDar | NÚMERO | Valor de arredondamento do item | N |
| VSNumero | NÚMERO | Número do Pedido, Nota de Saída, Ordem de Compra ou Nota de Entrada de acordo com a origem da chamada | N |
| VSCodSnf | ALFA | Vazio quando a origem for Pedido ou Ordem de Compra, e com valor quando a origem for Nota Fiscal de Saída ou Nota Fiscal de Entrada | N |
| VSSeqIte | NÚMERO | Sequência do item que estiver sendo calculado | N |
| VSEmpTpr | NÚMERO | Código da empresa da tabela de preço (Pauta) | N |
| VSCodTpr | ALFA | Código da tabela de preço (Pauta) | N |
| VSDefBcs | NÚMERO | Definição da base de cálculo (1-Preço Pauta, 2-Menor Preço, 3-Maior Preço) | N |
| VenNFilPed | NÚMERO | Filial do pedido vinculado ao item da nota. | N |
| VenNNumPed | NÚMERO | Número do pedido vinculado ao item da nota. | N |
| VenNSeqIpd | NÚMERO | Sequência do item de produto vinculado ao item da nota. | N |
| VenNSeqIsp | NÚMERO | Sequência do item de serviço vinculado ao item da nota. | N |
| VenNPerCtm | NÚMERO | Percentual e carga tributária média | N |
| VenNVlrBru | NÚMERO | Valor bruto do item da nota fiscal de entrada | N |
| VenNVlrDsc | NÚMERO | Valor do desconto do item da nota fiscal de entrada | N |
| VenNVlrDs1 | NÚMERO | Valor do desconto 1 | N |
| VenNVlrDs2 | NÚMERO | Valor do desconto 2 | N |
| VenNVlrDs3 | NÚMERO | Valor do desconto 3 | N |
| VenNVlrDs4 | NÚMERO | Valor do desconto 4 | N |
| VenNVlrDs5 | NÚMERO | Valor do desconto 5 | N |
| VenNBsiMar | NÚMERO | Base de cálculo gerada pela margem | N |
| VenNBsiPre | NÚMERO | Base de cálculo gerada pelo preço unitário de pauta | N |
| VenNIcsMar | NÚMERO | Valor da substituição calculada pela margem | N |
| VenNIcsPre | NÚMERO | Valor da substituição calculada pelo preço unitário de pauta | N |
| VenNPrePau | NÚMERO | Preço unitário de pauta. Variável disponível quando o critério de cálculo for "2 - Pelo Preço Unitário Base" ou "3 - Comparação Margem e Preço Unitário Base". As demais variáveis estarão disponíveis apenas para o critério de cálculo "3 - Comparação Margem e Preço Unitário Base". | N |
| VenNFilNfc | NÚMERO | Código da filial da nota fiscal de entrada. Disponível somente quando for realizada uma devolução. | N |
| VenNForNfc | NÚMERO | Código do fornecedor da nota fiscal de entrada. Disponível somente quando for realizada uma devolução. | N |
| VenNNumNfc | NÚMERO | Número da nota fiscal de entrada. Disponível somente quando for realizada uma devolução. | N |
| VenASnfNfc | ALFA | Série da nota fiscal de entrada. Disponível somente quando for realizada uma devolução. | N |
| VenNSeqItc | NÚMERO | Sequência do item da nota fiscal de entrada (serviço ou produto). Disponível somente quando for realizada uma devolução. | N |
| VenAUfsFil | ALFA | Sigla do estado da filial. | N |
| VenACodFam | ALFA | Código da família do produto. | N |
| VenACodClf | ALFA | Código da classificação fiscal. | N |
| VenACodAge | ALFA | Código de agrupamento para estoques. | N |
| VenACodStr | ALFA | Situação tributária do item da nota fiscal de entrada. | N |
| VenACstCof | ALFA | Código da situação tributária de COFINS. | N |
| VenACstIpi | ALFA | Código da situação tributária de IPI. | N |
| VenACstPis | ALFA | Código da situação tributária de PIS. | N |
| VSTipNot | NÚMERO | Tipo da nota fiscal | N |
| VSICMNOR | NÚMERO | Valor de ICMS Normal | S |
| VSBSIATU | NÚMERO | Valor base de Substituição | S |
| VSVLRICS | NÚMERO | Valor de Substituição | S |
| VSPERICS | NÚMERO | Percentual de Substituição | S |
| VSVlrOut | NÚMERO | Valor de outras despesas do item | S |
| VSVlrRis | NÚMERO | Valor de retenção de ICMS Substituto | S |
| VSPerIcm | NÚMERO | Percentual de ICMS Normal | S |
| VenNVlrBsd | NÚMERO | Valor base do ICMS substituído destacado do item da nota fiscal de venda. | S |
| VenNVlrIsd | NÚMERO | Valor do ICMS substituído destacado do item da nota fiscal de venda. | S |
| VSVlrBic | NÚMERO | Valor base de ICMS | S |
| VSPRECO | NÚMERO | Preço unitário na unidade de medida de estoque | N |
| VSQTDREC | NÚMERO | Quantidade recebida na unidade de medida do fornecedor | N |
| ComNBasIef | NÚMERO | Valor base ICMS entrega futura | N |
| ComNPerIef | NÚMERO | Percentual ICMS entrega futura | N |
| ComNVlrIef | NÚMERO | Valor ICMS entrega futura | N |
| CprAChvNel | ALFA | Apresentará a chave eletrônica da Nota Fiscal de Entrada, caso a variável VSOrigem estiver preenchida com **NFE - Nota Fiscal Entrada** | N |
| ComACodSer | ALFA | Código do serviço | N |
| ComNBstFcp | NÚMERO | Valor base do FCP ST | S |
| ComNAstFcp | NÚMERO | Alíquota do FCP ST | S |
| ComNVstFcp | NÚMERO | Valor do FCP ST | S |
| VSCodEmp | NÚMERO | Código da empresa | N |
| VSCodFil | NÚMERO | Código da filial | N |
| ComNCodCliFor | NÚMERO | Código do Cliente ou Fornecedor dependendo da origem.  A variável VSCliFor tem a mesma função e será mantida no identificador de regras por questão de compatibilidade para clientes que já utilizam a variável. | N |
| ComNMtdIst | NÚMERO | Motivo desoneração ICMS-ST. | N |
| ComNVicStd | NÚMERO | Valor do ICMS-ST desonerado. | N |
| VenASomTst | ALFA | Indicativo se soma ou não o ICMS Substituído. Valores possíveis para esta variável: "S - Sim" ou "N - Não". Valor utilizado somente em notas fiscais de entrada. | S |

**Observação:** No fechamento da nota fiscal o sistema chama este identificador a nível de dados gerais, e não de item. Esta situação ocorre em virtude das variáveis VSCODPRO e VSCODDER estarem em branco, além da variável VSSeqIte (sequência do item que estiver sendo calculado) estar zerada na chamada do identificador durante o fechamento.

Portanto não é possível enviar qualquer tipo de dado relativo ao item de produto, mesmo que exista um único item na nota. A chamada deste identificador durante o fechamento acontece a nível de dados gerais e possibilita ajustes com essa visão, olhando o todo e não item a item. Ou seja, a chamada de fechamento é como uma validação de arredondamento de valores.

Atenção

Caso o parâmetro global LisVarReg esteja habilitado, a variável ListaVariaveis estará disponível em todos os identificadores de regras do sistema. O conteúdo desta variável lista os campos disponibilizados no identificador de regras em questão.

Não é aconselhada a ativação desse parâmetro global para o uso cotidiano. Esse recurso de listagem dos campos de identificadores auxilia a construção de regras e o Suporte para, por exemplo, depuração ou quando não houver acesso à documentação dos identificadores de regras.

## Páginas relacionadas

* [MntBasIst](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#MntBasIst)
* [LisVarReg](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#LisVarReg)
