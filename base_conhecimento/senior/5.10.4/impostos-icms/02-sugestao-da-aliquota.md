# Sugestão da alíquota

> **Fonte:** Rotinas de ICMS — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/impostos-icms.htm#sugestao-aliquota  
> **Trilha:** Segmentos > Compliance > Configurações para cálculos fiscais > Impostos  
> **Telas citadas:** F009PPE, F019TIE  
> **Identificadores de regras:** CPR-000ALICM01, VEN-000ALICM01, VEN-140SGRED01

---
Por padrão, a alíquota é atribuída nas definições por estado. É possível definir uma alíquota específica para contribuintes e não contribuintes e para entradas e saídas. Esta alíquota é definida por estado e por filial. Ao incluir os itens nos documentos fiscais, o sistema verifica qual é a unidade fiscal do cliente/fornecedor e o código da filial onde a nota está sendo emitida e faz a busca da alíquota.

É também possível definir uma alíquota válida para todas as filiais definindo “0” como filial. A parametrização da filial “0” serve para aquelas filiais específicas que não tem parametrização definida.

Cadastros > Mercado e Suprimentos > Parâmetros Fiscais > Parâmetros por Estado > Cadastro (F009PPE)

Caso seja uma alíquota específica para determinadas condições, pode também ser cadastrado um código de ICMS especial.

Cadastros > Mercado e Suprimentos > Parâmetros Fiscais > ICMS especiais (F019TIE)

Uma vez cadastrado o ICMS especial, este código pode ser vinculado à transação, nas definições do cliente para a filial, no cadastro do produto/serviço, na ligação produto x cliente ou na ligação produto x fornecedora. O ICMS especial tem prioridade sobre as demais alíquotas do sistema.

A base, valor e alíquota também podem ser alterados via identificador de regras VEN-000ALICM01 e CPR-000ALICM01.

Para notas de entrada de devolução, tipos "2 - Devolução (NF do Cliente)" e "3 - Devolução (NF de Saída)", ou notas de entrada de retorno, tipos "4 - Retorno (Industrialização)" e "5 -Retorno (Outro)", com a aplicação da operação sendo "O - Retornos", o sistema buscará a alíquota do ICMS nos campos % ICMS Saída Não Contribuinte e % ICMS Saída Não Contribuinte da tela Parâmetros por Estado (F009PPE).

A sequência para a sugestão do código de redução de impostos e para o ICMS Especial é: Cadastro Transação Definições do Cliente Cadastro do produto/Serviço. Caso haja necessidade de alterar a sugestão do ICMS Especial, pode-se utilizar o Identificador de Regras VEN-140SGRED01. Para saber mais sobre o identificador de regras, clique aqui.

## Páginas relacionadas

* [Cadastro](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f009ppe.htm)
* [ICMS especiais](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f019tie.htm)
* [VEN-000ALICM01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_000alicm01.htm)
* [CPR-000ALICM01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/cpr_000alicm01.htm)
* [VEN-140SGRED01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_140sgred01.htm)
