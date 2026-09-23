# ICMS53 (ICMS Monofásico diferido)

> **Fonte:** Saiba tudo sobre o ICMS Monofásico — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/icms-monofasico.htm#icms53  
> **Trilha:** Segmentos > Compliance > Configurações para cálculos fiscais > Impostos > ICMS  
> **Telas citadas:** E019TIM, F000PPD, F001TCP, F001TVE, F019TIM, F027STR, F070FCA, F075PRO, F081GTP, F085CAD, F095CAD  
> **Identificadores de regras:** —

---
### Variáveis

| Nome | Descrição |
| --- | --- |
| QtmBic | Quantidade da base do ICMS Monofásico |
| AliImo | Alíquota ad rem do ICMS Monofásico |
| VmoIcm | Valor do ICMS Monofásico |
| QtmBif | Quantidade da base do ICMS Monofásico diferido |
| AliImf | Percentual de diferimento de ICMS Monofásico |
| VmoIcf | Valor do ICMS Monofásico diferido |

### Fórmulas

* AliImf = Percentual de diferimento de ICMS Monofásico referente ao percentual de destino da tabela E019TIM
  + Os percentuais de partilha aplicados ao cálculo são cadastrados na tela Cadastro de partilha ICMS Monofásico (F019TIM) e inicializados na atualização de sistema
* QtmBif = QtmBic
* VmoIcm = **AliImo \* QtmBic** (ICMS Monofásico total)
* VmoIcf = **VmoIcm \* (AliImf/100)** (ICMS Monofásico diferido)
* VmoIcm = **VmoIcm - VmoIcf** (ICMS Monofásico próprio)

**Exemplo:**

Venda de 1 galão do produto Biodiesel B100. O produto tem em sua tabela de tributação:

* Alíquota ad rem = 0,9456
* Unidade de tributação = Litros
* Unidade de venda = Galão (12 litros)

Dessa forma:

* PercentualDestino = 33,33
* AliImo = 0,9456
* QtmBic = 12 (arredonda em 4 casas decimais)
* QtmBif = 12 (arredonda em 4 casas decimais)

Cálculo:

* ValorTotalICMSMonofasico = 12 \* 0,9456 = 11,35 (arredonda em 2 casas decimais)
* VmoIcf = ValorTotalICMSMonofasico \* (33,33/100) = 3,78 (arredonda em 2 casas decimais)
* VmoIcm = ValorTotalICMSMonofasico - 3,78 = 7,57

---

### Parametrização

* Cliente/fornecedor, produto e transação devem estar configurados para tributação de ICMS. Isto é feito nas telas de Cadastro de Clientes (F085CAD), Cadastro de Fornecedores (F095CAD), Cadastro de Produtos (F075PRO), Transações de Vendas (F001TVE) (em caso de notas de saída) e Transações de Compras (F001TCP) (em caso de notas de entrada)
  + Ficou com alguma dúvida? Acesse Parametrização para calcular ICMS
* A situação tributária de ICMS deve ser 53. Para cadastrá-la, acesse a tela Situações Tributárias (F027STR)
  + Exemplo: situação tributária de ICMS 53 com origem "0 - Nacional", exceto as indicadas nos códigos 3, 4, 5 e 8:  

    ![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/images/icms/monofasico/revisao/10_thumb_0_48.png)
* O produto deve ter uma tabela de tributação de ICMS Monofásico cadastrada válida e com aplicação **3 ou 5** para operações de saída e **4 ou 5** para operações de entrada. Para criar uma tabela de tributação, acesse a tela Tabela de Preço de Venda (F081GTP)  

  ![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/images/icms/monofasico/1_thumb_0_48.png)  
  + **Exemplo de uma tabela cadastrada:**  

    ![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/images/icms/monofasico/revisao/6_thumb_0_48.png)  

    ![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/images/icms/monofasico/revisao/7_thumb_0_48.png)  

    ![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/images/icms/monofasico/revisao/8_thumb_0_48.png)
* Cadastre o parâmetro dinâmico CONTRIBUINTE.ICMS.MONOFASICO na tela Configuração de parâmetros dinâmicos (F000PPD), acessada por meio do botão Par. Dinâmicos da guia Cadastro, tela Cadastro de Clientes (F085CAD) para indicar se o cliente é contribuinte de ICMS Monofásico. Isto a fim de fazer a partilha entre o estado de origem e de destino. Caso não esteja preenchido, considera como **não contribuinte**

Observação

O parâmetro dinâmico NOTAFISCAL.XML.ICMS.MONOFASICO.DIFERIMENTO.GERAVICMSMONO indica se, na geração do .XML, produtos com tipo de combustível e situação tributária de ICMS 53 (Tributação monofásica sobre combustíveis com recolhimento diferido) vão gerar a tag **vICMSMono** (Valor do ICMS próprio) do Grupo N07a - Grupo Tributação do ICMS= 53, mesmo se ocorrer o diferimento total do ICMS Monofásico. Esse parâmetro é acessado a partir da tela Cadastro de Filiais (F070FCA), botão Par. Dinâmicos.

## Páginas relacionadas

* [Cadastro de partilha ICMS Monofásico (F019TIM)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f019tim.htm)
* [Cadastro de Clientes (F085CAD)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f085cad.htm)
* [Cadastro de Fornecedores (F095CAD)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f095cad.htm)
* [Cadastro de Produtos (](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075pro.htm)
* [Transações de Vendas (F001TVE)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f001tve.htm)
* [Transações de Compras (F001TCP)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f001tcp.htm)
* [Parametrização para calcular ICMS](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/impostos-icms.htm#parametrizacao)
* [Situações Tributárias (F027STR)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f027str.htm)
* [Tabela de Preço de Venda (F081GTP)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f081gtp.htm)
* [Configuração de parâmetros dinâmicos (F000PPD)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000ppd.htm#cadcli)
* [NOTAFISCAL.XML.ICMS.MONOFASICO.DIFERIMENTO.GERAVICMSMONO](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000ppd.htm)
* [na geração do .XML](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/leiaute-nf-e-nfc-e.htm)
* [Cadastro de Filiais (F070FCA)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070fca.htm)
