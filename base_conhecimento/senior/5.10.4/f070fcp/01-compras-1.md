# Compras 1

> **Fonte:** F070FCP - Parâmetros da Filial para Compras — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070fcp.htm  
> **Trilha:** Ajuda por telas > Cadastros > Filiais > Parâmetros por Gestão  
> **Telas citadas:** F440GNE  
> **Identificadores de regras:** —

---
Período Inicial/Final Compras

Data inicial e final do período em aberto para operações de entrada.

Série NF Entrada Padrão

Série padrão das operações de compras.

CNPJ/CPF Fornecedor

Indicativo se o CNPJ/CPF é obrigatório.

CNPJ/CPF Fornecedor Repetido

Indicativo se o CNPJ/CPF pode ser repetido na base, ou seja, se poderá haver mais de
um código de fornecedor com o mesmo CNPJ/CPF.

Transação OC Produto

Transação padrão das operações de ordens de compra de produto.

Transação OC Serviço

Transação padrão das operações de ordens de compra de serviço.

Transação OC Produção

Transação padrão das operações de ordens de compra via produção. A transação
a ser cadastrada necessita que o campo Aceita manual esteja com a indicação igual a "N - Não".

Quantidade Mínima Cotações

Quantidade mínima de cotações exigida pela filial para as solicitações de compra.

Exige Digitação Valor NFe

Indicativo se exige a digitação do valor da nota fiscal de entrada, para fins de
consistência com o valor apurado pelo sistema.

Valor Diferença Aceito

Quando informado, exige o valor da nota fiscal de entrada. Deve ser informado um limite de diferença aceito entre o valor digitado e o valor apurado pelo sistema na digitação de notas fiscais de entrada. Caso haja diferença entre os valores no fechamento da nota, será apresentada uma mensagem informando os valores que estão incidindo na inconsistência do cálculo. Exemplo: **Diferença entre o valor informado (XXX) e o valor líquido (XXX) da nota fiscal é maior do que o valor informado no campo Valor da Diferença Aceito (0,00)**.

**Importante**

A consistência do campo **Valor Líquido Informado** da tela F440GNE com base no **Valor Diferença Aceito** não ocorre para notas fiscais de acerto e transferência (9, 10 e 11). Esse comportamento é o mesmo para todas as telas/processos de geração de nota fiscal de entrada.

Inscrição Estadual Fornecedor Válida

Define como o sistema deve se comportar ao validar IE de fornecedores conforme as opções:

* "S - Sim": Sempre valida e bloqueia a operação se IE for inválida ou não informada;
* "I - Sim quando informada": Valida apenas se informada e bloqueia se inválida;
* "N - Não": Valida mas apenas avisa, ou seja, permite prosseguir caso desejar mesmo que a IE esteja incorreta.

Transação Entrada Ajuste

Código da transação que será utilizada pelo sistema na digitação da nota fiscal de
entrada, para ajustar as diferenças de pesos constantes na nota com os
registrados na balança.

Transação Saída Ajuste

Código da transação que será utilizada pelo sistema na digitação
da nota fiscal de entrada, para ajustar as diferenças de pesos constantes na nota com os
registrados na balança.

## Páginas relacionadas

* [F440GNE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f440gne.htm)
