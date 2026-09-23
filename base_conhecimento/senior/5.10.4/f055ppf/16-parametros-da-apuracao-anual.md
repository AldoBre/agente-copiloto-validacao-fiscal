# Parâmetros da Apuração Anual

> **Fonte:** F055PPF - Configuração de Impostos para a Filial — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f055ppf.htm  
> **Trilha:** Ajuda por telas > Cadastros > Controladoria > Tributos  
> **Telas citadas:** F051GUI  
> **Identificadores de regras:** —

---
Nesta guia é possível parametrizar nos impostos IRPJ e CSLL do tipo SPED (55, 56, 59 e 60) com apuração anual, as informações para emissão da guia de recolhimento, título e forma de contabilização para a apuração de encerramento do período (13ª apuração).

Competência Início

Data de Competência do início da parametrização.

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

Tipo de título que será gerado (DUP, FAT,...).

Trans

Transação de entrada de título (90500,...).

Filial Pag

Este campo tem o objetivo de informar o
destino do título de imposto gerado para o módulo do Financeiro de
uma filial para a matriz.

Gera Aut.

Se título será gerado automaticamente no momento do cálculo, ou será gerado através dos botões disponíveis de
geração de títulos.

Atu.Guia

Atualização da Guia, deve estar com a opção S - Sim, para poder ligar uma guia ao imposto e para
efetuar a geração da Guia de Recolhimento.

Guia Rec.

Deve-se informar o número da guia que foi cadastrada na tela F051GUI, é preciso observar o campo do **Código do documento de arrecadação do impostos**,
pois é obrigatório ser o mesmo código do cadastro da guia. Foi realizada esta implementação para poder gerar a
guia de recolhimento, onde é preciso fazer antes a ligação da guia ao imposto devido.

Código Forma Contabilização

Neste campo deve ser informado o código da forma de contabilização previamente cadastrada para o devido imposto. Com isso, será possível contabilizar o cálculo do imposto. É possível ligar a mesma forma de contabilização
para mais de um imposto.

Vlr Mínimo

Indica o valor mínimo do imposto, para que seja necessário seu pagamento.

Qtd. Parc.

Quantidade de Parcelas para o imposto.
