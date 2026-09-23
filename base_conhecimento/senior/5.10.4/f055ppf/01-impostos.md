# Impostos

> **Fonte:** F055PPF - Configuração de Impostos para a Filial — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f055ppf.htm  
> **Trilha:** Ajuda por telas > Cadastros > Controladoria > Tributos  
> **Telas citadas:** F049TTR, F051GUI, F661PAI  
> **Identificadores de regras:** —

---
Quando o cursor estiver sobre um imposto cadastrado, será exibido a descrição do mesmo e o seu tipo no
rodapé.

Imposto

Indica o imposto cadastrado para a filial. Campo obrigatório.

Observação

Só será possível configurar os impostos dos tipos 53/54 - IRPJ/CSLL Lucro presumido (SPED), 55/56 - IRPJ/CSLL Lucro Real (SPED), 57/58 - IRPJ/CSLL Lucro Arbitrado e 59/60 - IRPJ/CSLL Imune/Isenta na filial matriz.

Quando cadastrado o imposto IRPJ adicional (tipo 17) e IRPJ - diferença pela mudança de coeficiente (tipo 61) estes também deverão ser vinculados a filial matriz.

Padrão

Indica qual é o imposto padrão de um determinado tipo de imposto. Apenas um imposto de um determinado tipo será padrão, não sendo possível definir mais de um imposto do mesmo
tipo como padrão, exceto para o imposto do tipo 6 - Outros (Base Faturamento), que poderá ter mais de
um imposto como padrão, ou até mesmo nenhum definido como padrão.  

Esse campo será utilizado pelas gestões Mercados, Suprimentos e Custos, para cálculo do DVV (Despesas
Variáveis de Vendas). Para o imposto 64 - FCP - Fundo de Combate a Pobreza, indicado como Padrão, o parâmetro Apurar deve estar marcado. Essa parametrização é necessária caso houver mais de um imposto 64

Apurar

Este campo lista "S - Sim" e "N - Não". O Objetivo é ser ou não apresentado para apuração na tela F661PAI e o seu preenchimento é obrigatório.

Adic/Exc (Adicionais/Exclusões)

Indica se o imposto permite a entrada de valores adicionais ou exclusões quando for calculado. Este campo é obrigatório.

Período

Indica a periodicidade do imposto. Este campo é obrigatório e possui as seguintes opções:

* L - Livre
* O - Diário
* U - Quadrimestral
* R - Semestral
* S - Semanal
* B - Bimestral
* D - Decendial
* Q - Quinzenal
* M - Mensal
* T - Trimestral
* A - Anual

Observação

Só será permitido selecionar a opção T - Trimestral para os impostos dos tipos 53 - IRPJ Lucro presumido (SPED), 54 - CSLL Lucro presumido (SPED), 57 - IRPJ Lucro Arbitrado (SPED) e 58 - CSLL Lucro Arbitrado (SPED).

Será permitido selecionar a opção A-Anual ou T-Trimestral para os impostos dos tipos 55 – IRPJ Lucro Real (SPED), 56 – CSLL Lucro Real (SPED), 59 - IRPJ - Imune/Isenta (SPED) e 60 - CSLL - Imune/Isenta (SPED).

Dias Vcto (Dias Vencimento)

Indica o Número de dias após a data final de apuração que incidirá o vencimento do imposto.

Início Contagem

Este campo é utilizado para informar o período inicial para a contagem do vencimento do
imposto a ser calculado. Campo obrigatório. Tipos de contagem:

* 1 - Normal
* 2 - Fora Semana
* 3 - Fora Decêndio
* 4 - Fora Quinzena
* 5 - Fora Mês
* 6 - Último dia Semana Seguinte
* 7 - Último dia Decêndio Seguinte
* 8 - Último dia Quinzena Seguinte
* 9 - Último dia Mês Seguinte

Esse campo já virá parametrizado como 1 - Normal, não afetando a data de vencimento.
Caso seja informado 1 - Normal, a data inicial para a contagem do vencimento é o dia seguinte ao
período final do período. Se for informado 2 - Fora Semana, a contagem do vencimento ocorrerá a partir
da próxima semana, tendo como primeiro dia da semana o Domingo.

Por exemplo, se o período de apuração for
01/08/2004 à 31/08/2004, a data inicial para contagem iniciará no dia 05/09/2004 (primeira semana subseqüente ao
período de apuração). Se for informado ainda 7 dias de vencimento para o imposto, o vencimento seria para
11/09/2004, então esta data será ajustada conforme o parâmetro de Vcto não útil (se posterga, antecipa
ou mantém).

Se for informado 9 – Último dia Mês Seguinte, a contagem do vencimento ocorrerá a partir do
último dia do mês seguinte. Por exemplo, se o período de apuração for 01/03/2008
à 31/03/2008, a data inicial para contagem iniciará
no dia 30/04/2008 (último dia do mês seguinte). Para impostos que vencem no último dia útil do mês seguinte
deve-se ainda informar no parâmetro Dias Vcto = 0 e no parâmetro do Vcto não útil = Antecipa.

Vcto. não útil

A - Dias Corridos - Antecipa, S - Dias Corridos - Mantém, N - Dias Corridos -
Posterga, U - Só Dias Úteis.

Cod Arrec

Indica o código de arrecadação a ser utilizado no documento de recolhimento do imposto. Campo obrigatório.

Faixa Lim. Alíq.

Este campo tem por finalidade definir qual o valor que será utilizado para definir a faixa de limite na
Tabela de Tributação e assim buscando a alíquota que deve ser aplicada no cálculo do devido imposto
na tela F049TTR. Possui as seguintes opções:

* 1 - Faturamento Bruto
* 2 - Faturamento Líquido
* 3 - Base de Cálculo do Imposto

## Exemplo

Se for definido a opção 1 - Faturamento Bruto, ao efetuar o cálculo do imposto do tipo
06 a faixa de limite para busca da alíquota considerará o valor do faturamento bruto. Se for definido
a opção 2 - Faturamento Líquido, ao efetuar o cálculo do imposto do tipo 06, a faixa de
limite para busca da alíquota irá considerar o valor do faturamento líquido. Se for definido a opção 3 -
Base de Cálculo do Imposto, ao efetuar o cálculo do imposto do tipo 06, a faixa de limite para
busca da alíquota considerará o valor da base de cálculo do imposto.  

Essa coluna somente será habilitada para o imposto do tipo 06 - Outros (Base Faturamento), sendo
obrigatório definir uma das opções.

Importante

O padrão do sistema para este tipo de imposto é a opção 03 - Base de Cálculo do Imposto,
assim para as empresas que já possuem o imposto cadastrado na base, não será preciso efetuar a definição de valor
para este campo, pois na geração do cálculo, mesmo não tendo valor definido, será considerado a base de cálculo
do imposto.

Somente será obrigatório definir uma das opções, caso for efetuado algum tipo de alteração ou na ligação do
imposto na base.

Vlr Mínimo

Indica o valor mínimo do imposto, para que seja necessário seu pagamento.

Acumula?

Indica se quando o imposto não atingir o valor mínimo para pagamento deve acumular para o próximo período ou
desprezar a apuração atual.

Valor Acumulado

Indica qual o valor acumulado pelo imposto no momento (Mantido pelo sistema). Será disponível apenas para visualização o campo Valor acumulado de uma competência para outra (Vlr. Acumulado), onde o mesmo deverá apresentar o valor acumulado que não foi recolhido de uma competência para outra.

Últ Data

Indica qual a última data da formação da base de cálculo do imposto e do processamento do último cálculo do
imposto (Mantida pelo sistema).

Cta Dev

Informar uma Conta Contábil Devedora para este Imposto, que pode ser utilizada nas formas de contabilização.

Cta Cred

Informar uma Conta Contábil Credora para este Imposto, que pode ser utilizada nas formas de contabilização.

Forn. Pad.

Serve para geração de títulos no contas a pagar dos impostos calculados, através do módulo de impostos, fornecedor
que será gerado o título para pagamento.

Tipo Tít

Tipo de título que será gerado(DUP, FAT,...).

Trans

Transação de entrada de título. (90500,...)

Filial Pag

Este campo tem o objetivo de informar o
destino do título de imposto gerado para o módulo do Financeiro de
uma filial para a matriz.

## Exemplo

O título de imposto, retido na baixa do contas a pagar ou na entrada de nota
fiscal  da filial &#39;2&#39;, será gerado na matriz (filial &#39;1&#39;), código informado
neste campo.

Para fazer uso deste campo já deverá ter o imposto previamente configurado nas duas filiais.  
Este campo está disponível para os impostos do tipo: IA1; IA2; IA3;
IA4; IA5; IA6; IA7; IA9. Exemplo:

Imposto ICMS - Filial 3(Totalizadora): Configurada para geração de títulos na filial 1.  
Quando se faz a configuração na filial 3, a filial 1 já deve ter (obrigatoriamente) este imposto configurado,
para que a gravação da configuração seja efetuada com sucesso.

Os dados para a geração do título (Forn. Pad., Tipo Tít. e Trans. )
devem ter sido informados na filial de destino.

Filial 3 (Totalizadora): Gera títulos do imposto ICMS para filial 1, logo os
dados de Forn. Pad., Tipo Tít. e Trans. herdados da filial 1 (Destino da
geração de títulos).

Na tela de cálculo de imposto, quando o imposto é calculado em uma filial
destino de acordo com a configuração dos impostos uma mensagem é mostrada, questionando o usuário se deseja
realmente gerar o título nesta filial, sendo que há outra filial configurada para geração do título na filial
atual do cálculo.  

A geração tanto de títulos quanto de guias devem obedecer a configuração em Base Imposto (Liga Filial).
Para geração de títulos, as informações de Forn. Pad., Tipo Tít. e Trans. para
a geração de títulos para o financeiro são buscados da filial de destino campo (Filial Pag.).  

Para a geração de guias é buscada da filial de cálculo, conforme definido em Base Imposto (Liga Filial) . No cálculo do imposto tipo 30 (Simples Nacional) não será tratada filial totalizadora. Neste caso quando for
calculado imposto para este tipo de imposto.

Gera Aut.

Se título será gerado automaticamente no momento do cálculo, ou será gerado através dos botões disponíveis de
geração de títulos.

Atu. Guia

Atualização da Guia, deve estar com a opção **S - Sim** para que seja possível ligar uma guia ao imposto e
efetuar a geração da guia de recolhimento.

Guia Rec.

Deve-se informar o número da guia que foi cadastrada na tela F051GUI, é preciso observar o parâmetro do código do documento de arrecadação do impostos,
pois é obrigatório ser o mesmo código do cadastro da guia. Foi realizada esta implementação para poder gerar a
guia de recolhimento, onde é preciso fazer antes a ligação da guia ao imposto devido.

Código Forma Contabilização

Neste campo deve ser informado o código da forma de contabilização previamente cadastrada para o devido imposto.  
Com isso, será possível contabilizar o cálculo do imposto. É possível ligar a mesma forma de contabilização
para mais de um imposto.

Observação

* Para o imposto 34 serão listadas somente as formas de contabilização em que a ORIFCT (origem da forma de
  contabilização) for igual a IUF
* Para o imposto 45 serão listadas somente as formas de contabilização em que a ORIFCT (origem da forma de
  contabilização) for igual a ICF
* Para os impostos 41, 42, 43 e 44 somente as formas de contabilização em que a ORIFCT (origem da forma de
  contabilização) for igual a ISP
* Para os impostos 53, 54, 55, 56, 57, 58, 59 e 60 somente as formas de contabilização em que a ORIFCT (origem da forma de contabilização) for igual a IRJ

Ori.Cal.Imp

Neste campo deve ser informado para impostos do tipo 18(COFINS), 19(PIS),20
(PIS - Não Cumulativo) e 21(COFINS - Não Cumulativo), se será preenchido com M(Movimento)
ou F(Faturamento).

Quando o impostos cadastrado na guia Base Liga Filial estiver com a opção M(Movimento)
então o cálculo do imposto gerará a partir do movimento, ou seja, na nota fiscal Entrada/Saída há um campo chamado
de Base/Valor PIS Faturamento e Base/Valor COFINS Faturamento quando informado valor
nesses campos o cálculo gerará a partir desses valores.

Composição

Esse campo somente estará habilitado para os impostos do tipo 96(Imposto Totalizador) e 97
(Imposto Livre). Nesse campo deve ser informada a montagem do imposto, indicando se o valor refere-se a
B (Base de Cálculo) ou I (Imposto).

Data Reg. Caixa

Data inicial para entrada de títulos.

Vlr. Mín. Parc. Imp.

Valor mínimo para parcelar o imposto.

Qtd. Parc.

Quantidade de Parcelas para o imposto.

Reg. Apuração

Indica o regime de apuração do imposto, podendo ser: "Regime de Competência" ou "Regime de Caixa". Quando "Regime de Competência", o sistema considera o documento fiscal com a retenção do imposto pela data de entrada. Quando "Regime de Caixa", considera pela data de pagamento (conforme o pagamento dos títulos do documento fiscal).

Esse campo é habilitado para seguintes os impostos:

* 10 - INSS
* 11 - IRRF
* 22 - COFINS Retido
* 23 - PIS Retido
* 24 - CSLL Retido
* 25 - Outras retenções
* 65 - ISS Retido
* 73 - ISS (LC 175/2020)
* 74 - ISS Retido (LC 175/2020)

Lançar Valor Acumul.

Indica a forma que o valor acumulado de IPI é lançado na apuração do imposto. Possui as seguintes opções:

* O - Outros Débitos: o valor acumulado é gerado no campo de outros débitos
* G - Guia de Recolhimento: o valor acumulado é somado ao valor líquido do título do financeiro e no valor da Guia de Recolhimento

Filtrar exec. serviço

Indica como será a apuração dos impostos tipo "5 - ISS" e "11 - IRRF" por meio das opções "S - Sim" (data de prestação de serviço) ou "N - Não" (data de emissão da nota fiscal).

Tipo de Comércio

Campo disponível apenas para o imposto tipo 70. Determina o tipo de cálculo que será aplicado na apuração do imposto. Possui as seguintes opções:

* V - Varejo
* A - Atacado
* T - Todos

**Observação**

Ao selecionar a opção **T - Todos**, será apresentada a seguinte mensagem: **É preciso selecionar o tipo de comércio para que a substituição tributária do ICMS seja calculada corretamente!**. Portanto, a opção não deve ser utilizada.

Para mais informações sobre a apuração do imposto 70, consulte a documentação do processo.

Rec. ISS. Agrup. Alíq.

Indicativo se o cálculo do ISS próprio (tipo 5) deve recalcular o montante do ISS apurado aplicando novamente a alíquota do ISS sobre o total das bases de cálculo das notas fiscais, ou considerar o ISS calculado na própria nota fiscal (valor padrão).

## Páginas relacionadas

* [documentação do processo](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/processo-geracao-calculo-imposto-70.htm)
