# Forma Apuração

> **Fonte:** F055PPF - Configuração de Impostos para a Filial — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f055ppf.htm  
> **Trilha:** Ajuda por telas > Cadastros > Controladoria > Tributos  
> **Telas citadas:** F046VIS, F055PPF  
> **Identificadores de regras:** —

---
Esta guia permite a configuração da base imposto liga filial dos impostos 55 – IRPJ Lucro Real (SPED) e 59 - IRPJ - Imune/Isenta (SPED). É possível configurar o imposto 60 - CSLL - Imune/Isenta (SPED) quando a empresa não possuir tributação para o IRPJ imune e isenta.

Competência Ref.

Informar a competência de início da parametrização cadastrada.

F. Estimativa Mensal

Informar se apuração do imposto será com base na Receita Bruta ou com base no Balanço/Balancete.

Observação

Quando a apuração dos impostos for trimestral, só poderá ser informado "B – Balanço/Balancete".

Visão Contábil DRE

Informar uma visão do tipo SPED, que seja igual a tabela L300 do SPED ECF, que servirá como base para apuração do IRPJ/CSLL Lucro Real. Para os impostos 59 - IRPJ - Imune/Isenta (SPED) e 60 - CSLL - Imune/Isenta (SPED) deve ainda ser informada uma visão que seja igual à tabela U150 do SPED ECF.

Observação

* A Senior disponibiliza visões padrões do tipo SPED para atender essa necessidade. É possível importar essas visões através da tela Cadastro de Visões Contábeis (F046VIS)
* A apuração do imposto do tipo 56 - CSLL Lucro Real (SPED) utilizará as informações cadastradas no imposto do tipo 55 - IRPJ Lucro Real (SPED)
* A apuração do imposto 60 - CSLL - Imune/Isenta (SPED) utilizará as informações cadastradas no imposto 59 - IRPJ - Imune/Isenta (SPED) quando existir um vínculo entre os dois
* São listadas somente as visões contábeis cadastradas como do Tipo S-SPED, Tipo Demonstração igual a 2 - Resultado do Exercício e que sejam padrões do sistema (campo Visão de Sistema)

Ctb. Aut.

Define se a contabilização do imposto será feita de forma automática no momento de processamento do cálculo do imposto:

* Sim: é o valor padrão e indica que a contabilização do imposto será feita de forma automática após o termino do seu processamento e título financeiro gerado.
* Não: indica que a contabilização do imposto não será feita de forma automática, ou seja, a contabilização ocorrerá através da rotina de integração contábil que será executada manualmente pelo usuário.

**Simular Apu. Oposta**

Este campo automaticamente virá selecionado como **S - Sim**, na tela Configuração de Impostos para a Filial (F055PPF), com isso, ele será disponibilizado para visualização na tela Apuração dos Impostos IRPJ - Lucro Real (SPED) e CSLL - Lucro Real (SPED) (F661I15), será apresentado a apuração do imposto conforme indicado no campo **Forma de Apuração** e também será apresentada uma simulação da apuração do imposto com a forma de apuração inversa à qual foi parametrizada.

Ao marcá-lo como **N - Não** , não será apresentada na tela (F661I15) a simulação do imposto a recolher com a forma de apuração inversa a parametrizada.

## Páginas relacionadas

* [F046VIS](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f046vis.htm)
* [F661I15](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f661i15.htm)
