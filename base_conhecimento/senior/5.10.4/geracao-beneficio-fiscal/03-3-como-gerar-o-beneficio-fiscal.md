# 3. Como gerar o Benefício Fiscal?

> **Fonte:** Configuração de Dispositivo e Benefício Fiscais — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/geracao-beneficio-fiscal.htm  
> **Trilha:** Segmentos > Compliance > Documentos Eletrônicos > NF-e | NFC-e (Nota Fiscal Eletrônica) > Nota Fiscal Eletrônica 4.0  
> **Telas citadas:** E051DIS, E140IPV  
> **Identificadores de regras:** VEN-140BENEF01

---
O Benefíco Fiscal é um regime especial de tributação que envolve uma vantagem fiscal perante o regime normal, por exemplo isenção, redução de alíquotas, direito a crédito ou outras medidas fiscais.

No ERP, a seguinte lógica será utilizada para geração da tag **cBenef**:

* Campo **Aplicação**: deve ser **02-SPED**;
* Campo **Doc. Fiscal**: deve ser **S-Sim**;
* Campo Tipo Ajuste Documento Fiscal: deve estar informado com uma das opções disponíveis. Caso contrário, a tag não é gerada;
* Campo Inf. Adic. Ben. Fis: deve estar definido como **S-Sim**, indicando que o Dispositivo Fiscal irá gerar o Benefício Fiscal na NF-e, através do campo Cod. Adicional (E051DIS.CodInf);
* Campo **Cód. Adicional**: deve ser informado o código do Benefício Fiscal que deve ser gerado na tag **cBenef** da NF-e;
* Identificador de regras VEN-140BENEF01: possibilita personalizar, via regra, o código do Benefício no cálculo da nota fiscal. É obrigatório possuir um Dispositivo Fiscal, caso contrário o identificador não será executado.

Importante

* O valor da tag <cBenef> será gerado com base no valor do campo E140IPV.CodBnf. Ou seja, o código do Benefício Fiscal não é gerado dinamicamente na geração do .XML. Ele será gerado no processamento da NF e depois o sistema buscará do campo indicado acima a informação para gerar a tag do .XML;
* Quando o item da nota fiscal possuir dois ou mais Dispositivos Fiscais com a opção Inf. Adic. Ben. Fis igual a **S-Sim**, será gerado o código do Benefício Fiscal apenas do primeiro dispositivo.
* A Nota Técnica 2019.001
  - Criação e Atualização de Regras de Validação exige que o CST corresponda ao tipo de código de Benefício Fiscal informado. Para itens sem Benefício Fiscal, a UF poderá exigir a informação da literal **SEM CBENEF**, conforme tabela disponibilizada no Portal da Nota Fiscal Eletrônica - SVRS, **tabela cBenef x CST**. Para mais informações, consulte o tópico 4 da página.

**Exemplo:**

| Estado | Reflexo Apuração ICMS | Tipo Apuração | Responsabilidade | Influência Recolhimento | Origem Tributação | Ajuste ICMS | Código do Benefício Fiscal |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SC | 1 - Outros créditos | 0 - Operação Própria | 0 - Própria | 0 - A Apurar | 1 - Transporte | 999 | SC10001999 |

A Nota Técnica 2019.001
- Criação e Atualização de Regras de Validação exige que o CST corresponda ao tipo de código de Benefício Fiscal informado. Para itens sem Benefício Fiscal, a UF poderá exigir a informação da literal **SEM CBENEF**, conforme tabela disponibilizada no Portal da Nota Fiscal Eletrônica - SVRS, **tabela cBenef x CST**.

## Páginas relacionadas

* [VEN-140BENEF01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_140benef01.htm)
* [Nota Técnica 2019.001
- Criação e Atualização de Regras de Validação](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/notas-tecnicas-nfe-nfce.htm)
* [Portal da Nota Fiscal Eletrônica - SVRS](https://dfe-portal.svrs.rs.gov.br/Nfe)
