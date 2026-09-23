# Cidade ISS

> **Fonte:** F055PPF - Configuração de Impostos para a Filial — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f055ppf.htm  
> **Trilha:** Ajuda por telas > Cadastros > Controladoria > Tributos  
> **Telas citadas:** E055ISS, E055PAR, F051GUI  
> **Identificadores de regras:** —

---
Nesta guia devem ser informadas as cidades em que o imposto será apurado, podendo ser parametrizados os impostos tipo:

* "65 - ISS Retido";
* "66 - ISS Retido - RPA";
* "73 - ISS (LC 175/2020)";
* "74 - ISS Retido (LC 175/2020)".

Observação

Nesta tela, para os impostos tipo 73 e 74, os parâmetros Gera Atu. (E055PAR.AutFin) e Atu. Guia (E055PAR.AtuGri), devem estar exatamente iguais entre a guia Impostos e todos os municípios parametrizados na guia Cidade ISS (E055ISS.AutFin/AtuGri), assim como no imposto tipo 75 correspondente.

Devido ao imposto 75 ser consequência dos valores apurados no 73 ou 74, as rotinas de cálculo, geração de títulos, exclusão dos títulos ou da apuração devem ocorrer simultaneamente para os municípios do prestador e tomador.

Data

Data de início das configurações. A apuração do imposto irá considerar as cidades e parâmetros observando esta data, e somente os municípios que estiverem parametrizados para esta data.

Exemplo:

|  |
| --- |
| ``` A partir de 01/01/2022 a empresa deseja apurar o ISS para São Paulo e Campinas. Para estes municípios, irá configurar: 01/01/2022 - São Paulo 01/01/2022 - Campinas  Em 01/01/2023, precisa apurar também para Ribeirão Preto. Terá que configurar uma data inicial para apurar este novo município, incluindo nesta nova data os demais municípios que devem continuar sendo apurados:  01/01/2023 - São Paulo 01/01/2023 - Campinas 01/01/2023 - Ribeirão Preto Dessa forma, a partir de 2023 serão apurados estes 3 municípios e, caso seja realizada uma apuração retroativa de 2022, serão apurados somente os 2 municípios que estavam cadastrados para aquela data.  Em 01/01/2024, a IM de Campinas foi baixada e o ISS não deve mais ser apurado. Incluir uma nova data informando somente os municípios que devem ser apurados a partir desta competência: 01/01/2024 - São Paulo 01/01/2024 - Ribeirão Preto Dessa forma, a partir de 2024 serão apurados somente estes 2 municípios e, caso seja realizada uma apuração retroativa de 2023, serão apurados todos os municípios que estavam cadastrados para aquela data. ``` |

Cidade ISS

Código da cidade.

Nome

Exibe o nome da cidade informada no campo Cidade ISS.

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

Vcto. não útil

A - Dias Corridos - Antecipa, S - Dias Corridos - Mantém, N - Dias Corridos -
Posterga e U - Só Dias Úteis.

Cód. Arrec.

Indica o código de arrecadação a ser utilizado no documento de recolhimento do imposto.

Vlr. Mínimo

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

Transação de entrada de título. (90500,...).

Gera Aut.  
 Definir se título será gerado automaticamente no momento do cálculo ou será gerado através dos botões disponíveis de
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

**Tipo de retenção do ISS**

Indica se o recolhimento se dará pela data de entrada ou pela data de execução do serviço.

Duplicar

Permite duplicar municípios para a data inicial mais recente cadastrada.

Para utilizar esta função, cadastre um município informando a nova data inicial (que deve ser posterior às demais datas já existentes). Selecione na grade os municípios que deseja duplicar para esta nova data. Clique no botão "Duplicar" e, nesse momento, todos os municípios selecionados serão gravados para a nova data inicial mais recente.

## Páginas relacionadas

* [data de entrada ou pela data de execução do serviço.](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f661pai.htm#Apura%C3%A7%C3%A3o)
