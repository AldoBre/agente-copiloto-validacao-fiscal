# Isentas/Outras x IPI na base de ICMS

> **Fonte:** Rotinas de ICMS — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/impostos-icms.htm#isentas  
> **Trilha:** Segmentos > Compliance > Configurações para cálculos fiscais > Impostos  
> **Telas citadas:** —  
> **Identificadores de regras:** COM-000AISOU01

---
Exemplo:

Valor do produto: 4.300,63

Base do IPI: 4300,63

Valor do IPI: 430,06

Base do ICMS: 4730,69

Isentas ICMS: 4300,63

Porém, neste caso o valor de Outras/Isentas de ICMS deveria ser 4.730,69. Há alguma parametrização para fazer com que o sistema considere neste caso o valor de IPI?

Neste caso, deve-se utilizar o identificador de regras COM-000AISOU01 para manipular o valor do campo Outras/Isentas ICMS.

O cálculo de Outras/Isentas segue o que prescreve a legislação do ICMS:

Coluna Outras: valor da prestação ou da operação, deduzida a parcela do IPI, se consignada no documento fiscal, quando se tratar de utilização de serviço ou de entrada de mercadoria que não confira ao estabelecimento destinatário crédito do imposto a abater, ou quando se tratar de prestação ou operação realizada com diferimento ou suspensão e outras prestações que não confiram crédito a deduzir.

## Páginas relacionadas

* [COM-000AISOU01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/com_000aisou01.htm)
