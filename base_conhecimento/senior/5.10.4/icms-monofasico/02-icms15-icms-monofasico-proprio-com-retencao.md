# ICMS15 (ICMS Monofásico próprio com retenção)

> **Fonte:** Saiba tudo sobre o ICMS Monofásico — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/icms-monofasico.htm#icms15  
> **Trilha:** Segmentos > Compliance > Configurações para cálculos fiscais > Impostos > ICMS  
> **Telas citadas:** E075PRO, F000PPD, F001TCP, F001TVE, F019TIM, F019TIR, F027STR, F075PRO, F081GTP, F085CAD, F095CAD  
> **Identificadores de regras:** —

---
### Variáveis

| Nome | Descrição |
| --- | --- |
| QtmBic | Quantidade da base do ICMS Monofásico |
| AliImo | Alíquota ad rem do ICMS Monofásico |
| VmoIcm | Valor do ICMS Monofásico |
| QtmBir | Quantidade da base do ICMS Monofásico retido |
| AliImr | Alíquota ad rem do ICMS Monofásico retido |
| VmoIcr | Valor do ICMS Monofásico retido |

### Fórmulas

#### ICMS Monofásico próprio

* AliImo = Alíquota referente à tabela de tributação de ICMS Monofásico no cadastro do produto (E075Pro.TprImo) com redução aplicada
  + O cadastro da redução deve ser feito na tela Reduções e Acréscimos de bases de Cálculos de Impostos - Por Estado (F019TIR), no registro de redução aplicado ao produto (E075PRO.CodTrd)
* QtmBic = Quantidade convertida para a unidade de tributação de acordo com a tabela de tributação de ICMS Monofásico, sem a quantidade referente à quantidade do produto misturado
  + O Produto Misturado (E075PRO.ProMis) e o percentual de mistura (E075PRO.PerMis) são cadastrados na tela Cadastro de Produtos (F075PRO)
* VmoIcm = **QtmBic \* AliImo**

#### ICMS Monofásico com retenção

* AliImr = Alíquota referente à tabela de tributação de ICMS Monofásico no cadastro do produto misturado com percentual de partilha aplicado
  + Os percentuais de partilha aplicados ao cálculo são cadastrados na tela Cadastro de partilha ICMS Monofásico (F019TIM) e inicializados na atualização de sistema
* QtmBir = Quantidade referente à quantidade do produto misturado (quantidade total convertida – quantidade base do ICMS Monofásico próprio)
* VmoIcr = **QtmBir \* AliImr**

**Exemplo:**

Venda de 10 galões do produto Óleo Diesel B.

* O **produto** tem em sua tabela de tributação:
  + Alíquota ad rem = 0,9456
  + Unidade de tributação = Litros
  + Unidade de venda = Galão (12 litros)
* E em seu cadastro:
  + Índice de mistura de 15% do produto Biodiesel B100
  + Redução de 10% na alíquota
* O **produto misturado** tem em sua tabela de tributação:
  + Alíquota ad rem = 0,9456

Dessa forma:

* PercentualMistura = 15
* PercentualReducao = 10
* PercentualDestino = 33,33

| ICMS Monofásico próprio | ICMS Monofásico com retenção |
| --- | --- |
| * AliImo = 0,9456 – (0,9456 \* (PercentualReducao /100)) = 0,8510 (arredonda em 4 casas decimais) * QtmBic = 120 – (120 \* (PercentualMistura /100)) = 102 (arredonda em 4 casas decimais) * VmoIcm = 102 \* 0,8510 = 86,80 (arredonda em 2 casas decimais) | * AliImr = 0,9456 \* (PercentualDestino/100) = 0,3152 (arredonda em 4 casas decimais) * QtmBir = QtmBic /(1 - (PercentualMistura / 100)) \* (PercentualMistura / 100) = 18 (arredonda em 4 casas decimais) * VmoIcr = 0,3152 \* 18 = 5,67 (arredonda em 2 casas decimais) |

---

### Parametrização

* Cliente/fornecedor, produto e transação devem estar configurados para tributação de ICMS. Isto é feito nas telas de Cadastro de Clientes (F085CAD), Cadastro de Fornecedores (F095CAD), Cadastro de Produtos (F075PRO), Transações de Vendas (F001TVE) (em caso de notas de saída) e Transações de Compras (F001TCP) (em caso de notas de entrada)
  + Ficou com alguma dúvida? Acesse Parametrização para calcular ICMS
* A situação tributária de ICMS deve ser 15. Para cadastrá-la, acesse a tela Situações Tributárias (F027STR)
  + Exemplo: situação tributária de ICMS 15 com origem "0 - Nacional", exceto as indicadas nos códigos 3, 4, 5 e 8:  

    ![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/images/icms/monofasico/revisao/9_thumb_0_48.png)
* O **produto** deve ter uma tabela de tributação de ICMS Monofásico cadastrada válida e com aplicação **3 ou 5** para operações de saída e **4 ou 5** para operações de entrada. Para criar uma tabela de tributação, acesse a tela Tabela de Preço de Venda (F081GTP)  

  ![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/images/icms/monofasico/1_thumb_0_48.png)  
  + **Exemplo de uma tabela cadastrada:**  

    ![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/images/icms/monofasico/revisao/6_thumb_0_48.png)  

    ![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/images/icms/monofasico/revisao/7_thumb_0_48.png)  

    ![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/images/icms/monofasico/revisao/8_thumb_0_48.png)
* O produto deve ter Tipo de Combustível, Índice de Mistura e Produto Misturado preenchidos em Cadastro de Produtos (F075PRO)  

  ![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/images/icms/monofasico/2_thumb_0_48.png)
* O **produto misturado** deve ter uma tabela de tributação de ICMS Monofásico cadastrada válida e com aplicação **3 ou 5** para operações de saída e **4 ou 5** para operações de entrada. Em caso de dúvida, confira o exemplo anterior
* Cadastre o parâmetro dinâmico CONTRIBUINTE.ICMS.MONOFASICO na tela Configuração de parâmetros dinâmicos (F000PPD), acessada por meio do botão Par. Dinâmicos da guia Cadastro, tela Cadastro de Clientes (F085CAD) para indicar se o cliente é contribuinte de ICMS Monofásico. Isto a fim de fazer a partilha entre o estado de origem e de destino. Caso não esteja preenchido, considera como **não contribuinte**

## Páginas relacionadas

* [Reduções e Acréscimos de bases de Cálculos de Impostos - Por Estado (F019TIR)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f019tir.htm)
* [Cadastro de Produtos (F075PRO)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075pro.htm)
* [Cadastro de partilha ICMS Monofásico (F019TIM)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f019tim.htm)
* [Cadastro de Clientes (F085CAD)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f085cad.htm)
* [Cadastro de Fornecedores (F095CAD)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f095cad.htm)
* [Transações de Vendas (F001TVE)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f001tve.htm)
* [Transações de Compras (F001TCP)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f001tcp.htm)
* [Parametrização para calcular ICMS](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/impostos-icms.htm#parametrizacao)
* [Situações Tributárias (F027STR)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f027str.htm)
* [Tabela de Preço de Venda (F081GTP)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f081gtp.htm)
* [Configuração de parâmetros dinâmicos (F000PPD)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000ppd.htm#cadcli)
