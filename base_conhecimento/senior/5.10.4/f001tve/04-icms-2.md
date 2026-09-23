# ICMS 2

> **Fonte:** F001TVE - Transações de Vendas — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f001tve.htm  
> **Trilha:** Ajuda por telas > Cadastros > Transações > Parâmetros por Gestão  
> **Telas citadas:** E660NFV, F019TST  
> **Identificadores de regras:** —

---
Código Red. ICMS preço

Código de redução de ICMS padrão para a transação.

Considera desoneração ICMS  
Indicativo se a transação considera ou não
desoneração de ICMS.

**Código Modalidade ICMS**

Código da modalidade para definição da base de cálculo do ICMS. A pesquisa deste campo busca os códigos de substituição/modalidade de ICMS (tela F019TST).

% Diferimento

Percentual que será utilizado para o cálculo do valor do ICMS Diferido em pedidos, pré-faturas e notas fiscais de saída.

COFINS Faturamento Base ICMS

Indica se o valor do COFINS faturamento é considerado na base de cálculo do ICMS.

PIS Faturamento Base ICMS

Indica se o valor do PIS faturamento é considerado na base de cálculo do ICMS.

Considera Pedágio na base do ICMS

Indica se o valor de pedágio é Somado ou Subtraído da base de cálculo do ICMS.

Prazo retorno mercadorias suspensão ICMS (dias)

Informe a quantidade em dias correspondente ao prazo previsto de retorno da mercadoria.

Cons. Outros ICMS e receitas tributadas calc. CIAP

Indica se o valor de outros ICMS deve ser considerado como receita tributada no cálculo do índice do CIAP. Quando este campo estiver parametrizado com **Sim**, o valor da receita tributada será gerado de acordo com a seguinte fórmula:

* **Base do ICMS (Notas fiscais e Reduções Z) + Exportações (CFOP 5501, 5502, 6501, 6502 e iniciada por 7) + Outros ICMS (Notas fiscais e Reduções Z) / Valor Contábil – IPI (quando parametrizado para descontar) – ICMS ST (quando parametrizado para descontar).**

Quando estiver parametrizado como **Não**, o cálculo do CIAP e a geração do SPED Fiscal não sofrem alteração.

Considerar fator FCA

Define se a transação considera fator FCA.

Cons. Valor Contábil como Valor Tribut. no cálc. CIAP

Indica se o Valor Contábil das operações de venda com substituição tributária deverão ser considerados como Valor Tributado no cálculo do índice do CIAP. O campo tem como valor padrão a opção N-Não.

Valor Isento ICMS como Valor Tribut. Cálc. CIAP

Indica se o Valor Isento de ICMS deve ser considerado como Valor Tributado no cálculo do índice do CIAP. Caso este campo esteja parametrizado como Sim, o valor isento do ICMS (E660NFV.VlrIic) é considerado para compor o valor do somatório das saídas tributadas e saídas para exportação, gerado no campo 6 - VL\_TRIB\_EXP do registro G110 do SPED Fiscal.

Direito ao Ressarcimento de ICMS ST

Dependendo da legislação, apenas algumas operações de saída específicas possuem direito ao ressarcimento do ICMS ST pago na aquisição da mercadoria correspondente à essas operações (saída para outra unidade da federação, saída amparada por isenção ou não-incidência e perecimento, furto, roubo ou qualquer outro tipo de perda).

Para isso, deve-se informar no campo a se a transação da nota fiscal de venda ou cupom fiscal terá direito ao ressarcimento. Possui as opções S-Sim e N-Não.

**Percentual do Diferimento de ICMS relativo ao FCP**

Percentual do diferimento de ICMS relativo ao FCP sugerido para o cálculo do valor do diferimento de ICMS relativo ao FCP nos processos de vendas e faturamento. Este campo não tem preenchimento obrigatório.

Transferência Crédito ICMS

Indicativo se a transação de nota de saída deve calcular transferência de crédito de ICMS entre filiais para notas fiscais que atendam aos requisitos para atender o Convênio ICMS nº 109/2024. O campo somente está disponível para transações cuja Aplicação da Operação seja "T - Transferências".

## Páginas relacionadas

* [Convênio ICMS nº 109/2024](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/convenio-icms-109-2024.htm)
