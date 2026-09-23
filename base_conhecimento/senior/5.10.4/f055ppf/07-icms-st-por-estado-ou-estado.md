# ICMS ST por Estado ou Estado

> **Fonte:** F055PPF - Configuração de Impostos para a Filial — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f055ppf.htm  
> **Trilha:** Ajuda por telas > Cadastros > Controladoria > Tributos  
> **Telas citadas:** F051GUI  
> **Identificadores de regras:** —

---
Data

Informar a data do preenchimento da guia.

Data

Data/competência de início das configurações. A apuração do imposto considerará os estados e parâmetros observando esta data, e somente os estados que estiverem parametrizados para ela.  
Exemplo:

```

A partir de 01/01/2022 a empresa possui IE nos estados SC e RS. Para apurar estes estados, irá configurar:
 

01/01/2022 - SC
01/01/2022 - RS 

Em 01/01/2023, passa a ter também IE para RJ. Terá que configurar uma data inicial para apurar este novo estado, incluindo nesta nova data os demais estados que devem continuar sendo apurados:

01/01/2023 - RJ 
01/01/2023 - SC
01/01/2023 - RS 

Dessa forma, a partir de 2023 serão apurados estes 3 estados e, caso seja realizada uma apuração retroativa de 2022, serão apurados somente os 2 estados que estavam cadastrados para aquela data.  

Em 01/01/2024, a IE do RS foi baixada. Incluir uma nova data informando somente os estados que devem ser apurados a partir desta competência:

01/01/2024 - RJ
01/01/2024 - SC 
Dessa forma, a partir de 2024 serão apurados somente estes 2 estados e, caso seja realizada uma apuração retroativa de 2023, serão apurados todos os estados que estavam cadastrados para aquela data.  

```

**Estado**

Informe o estado.

Dias Vcto.

Indica o número de dias após a data final de apuração que incidirá o vencimento do imposto.

Início contagem

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

**Fator Gerador**

Data do fato gerador para geração.

Vcto. não útil

A - Dias Corridos - Antecipa, S - Dias Corridos - Mantém, N - Dias Corridos -
Posterga e U - Só Dias Úteis.

Cód. Arrec.

Indica o código de arrecadação a ser utilizado no documento de recolhimento do imposto.

Vlr. Mínimo

Indica o valor mínimo do imposto, para que seja necessário seu pagamento.

Acumula?

Indica se, quando o imposto não atingir o valor mínimo para pagamento, deve acumular para o próximo período ou
ignorar a apuração atual.

**Vlr. Acu.**

Valor acumulado do imposto a ser comparado com o valor mínimo.

Últ. Data

Indica qual a última data da formação da base de cálculo do imposto e do processamento do último cálculo do
imposto (Mantida pelo sistema).

Cta. Dev

Informar uma Conta Contábil Devedora para este Imposto, que pode ser utilizada nas formas de contabilização.

Cta. Cred

Informar uma Conta Contábil Credora para este Imposto, que pode ser utilizada nas formas de contabilização.

Forn. Pad.

Serve para geração de títulos no contas a pagar dos impostos calculados, através do módulo de impostos, fornecedor
que será gerado o título para pagamento.

Tipo Tít

Tipo de título que será gerado (DUP, FAT...).

Trans

Transação de entrada de título (90500...).

Gera Aut.

Se título será gerado automaticamente no momento do cálculo, ou será gerado através dos botões disponíveis de
geração de títulos.

Atu.Guia

Atualização da Guia, deve estar com a opção S - Sim, para poder ligar uma guia ao imposto e para
efetuar a geração da Guia de Recolhimento.

Guia Rec.

Deve-se informar o número da guia que foi cadastrada na tela F051GUI, é preciso observar o campo do **código do documento de arrecadação do impostos**,
pois é obrigatório ser o mesmo código do cadastro da guia. Foi realizada esta implementação para poder gerar a
guia de recolhimento, onde é preciso fazer antes a ligação da guia ao imposto devido.

Código Forma Contabilização

Neste campo deve ser informado o código da forma de contabilização previamente cadastrada para o devido imposto. Com isso, será possível contabilizar o cálculo do imposto. É possível ligar a mesma forma de contabilização
para mais de um imposto.

Possui IE para a UF

Indicar se a empresa possui inscrição estadual para a unidade federativa.

Observação

O campo só ficará disponível para edição se o imposto for do tipo 63 (Dif. Alíq. do ICMS interestadual com consumidor final). Caso o campo estiver como S-Sim, as notas fiscais de devolução serão utilizadas na apuração do imposto. Caso o campo estiver como N-Não, as notas fiscais de devolução não serão consideradas.

O campo só ficará disponível para edição se o imposto for dos tipos 34 (ST Substituto por Estado) ou 63 (Dif. Alíq. do ICMS interestadual com consumidor final). Exclusivamente para o imposto tipo 63: caso o campo esteja definido como "S – Sim", as notas fiscais de devolução serão utilizadas na apuração do imposto. Caso esteja definido como "N – Não", as notas fiscais de devolução não serão consideradas.

Duplicar

Permite duplicar estados para a data inicial mais recente cadastrada.

Para utilizar esta função:  
Cadastre um estado informando a nova data inicial (que deve ser posterior às demais datas já existentes). Selecione, na grade, quais estados deseja duplicar para esta nova data. Clique no botão Duplicar e, neste momento, todos os estados selecionados serão registrados para esta nova data inicial mais recente.

Observação

Para duplicar uma competência, é necessário que a data-base esteja dentro do período da filial para Gestão de Tributos. Caso seja preciso duplicar uma competência com data anterior à abertura do período, deve-se alterar a data de início do período, de forma que a data-base da competência seja igual ou posterior à data de início do período.
