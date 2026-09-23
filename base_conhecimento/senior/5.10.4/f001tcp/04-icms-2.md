# ICMS 2

> **Fonte:** F001TCP - Transações de Compras — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f001tcp.htm  
> **Trilha:** Ajuda por telas > Cadastros > Transações > Parâmetros por Gestão > Compras  
> **Telas citadas:** F019TST, F660INT  
> **Identificadores de regras:** —

---
Considera desoneração ICMS

Indica se o valor de ICMS Desonerado deve ser abatido do valor líquido do item.

**Código Modalidade ICMS**

Código da modalidade para definição da base de cálculo do ICMS. A pesquisa deste campo busca os códigos de substituição/modalidade de ICMS (tela F019TST).

% Diferimento

Percentual que será utilizado para o cálculo do valor do ICMS Diferido em cotações, contratos, ordens de compras e notas fiscais de entrada.

COFINS Recuperar Base ICMS

Indica se o valor do COFINS a Recuperar é considerado na base de cálculo do ICMS. Caso seja diferente de "N - Nenhum", o valor do ICMS calculado não será considerado no valor da base de cálculo do COFINS a recuperar.

PIS Recuperar Base ICMS

Indica se o valor do PIS a Recuperar é considerado na base de cálculo do ICMS. Caso seja diferente de "N - Nenhum", o valor do ICMS calculado não será considerado no valor da base de cálculo do PIS a recuperar.

II na Base ICMS

Indicativo se o valor do Imposto de Importação deve ser considerado na base de ICMS.

Frete Importação Base ICMS

Indicativo se o valor do Frete de Importação deve ser considerado na base de ICMS.

Seguro Importação Base ICMS

Indicativo se o valor do Seguro de Importação deve ser considerado na base de ICMS.

Outras Despesas Importação Base ICMS

Indicativo se o valor de Outras Despesas de Importação deve ser considerado na base de ICMS.

Crédito do ICMS Imobilizado na Nota Fiscal Compra

Quando este campo estiver parametrizado como **Sim**, na integração da nota fiscal, através da tela Integração de Notas Fiscais (F660INT), o crédito do ICMS decorrente da compra de um ativo imobilizado é lançado de forma integral na nota fiscal de compra através dos campos de ICMS. Caso contrário, os créditos do ICMS são controlados diretamente no CIAP.

Código ICMS Antecipação

Este campo permite a parametrização da transação para utilizar ICMS Antecipação ou não.

Considera Pedágio na base do ICMS

Indica se o valor de pedágio é Somado ou Subtraído da base de cálculo do ICMS.

**Percentual do Diferimento de ICMS relativo ao FCP**

Percentual do diferimento de ICMS relativo ao FCP sugerido para o cálculo do valor do diferimento de ICMS relativo ao FCP nos processos de compras e recebimento. Este campo não tem preenchimento obrigatório.

Adicionar ICMS Diferido

Indicativo para Adicionar o valor do ICMS Diferido no valor líquido do item na nota fiscal de entrada.

## Páginas relacionadas

* [Integração de Notas Fiscais (F660INT)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f660int.htm#menu_controladoria/F660INT.htm)
* [ICMS Antecipação](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/impostos-icms.htm#icms-antecipacao)
