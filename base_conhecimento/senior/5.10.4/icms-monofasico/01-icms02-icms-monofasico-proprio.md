# ICMS02 (ICMS Monofásico próprio)

> **Fonte:** Saiba tudo sobre o ICMS Monofásico — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/icms-monofasico.htm#icms02  
> **Trilha:** Segmentos > Compliance > Configurações para cálculos fiscais > Impostos > ICMS  
> **Telas citadas:** F001TCP, F001TVE, F027STR, F075PRO, F081GTP, F085CAD, F095CAD  
> **Identificadores de regras:** —

---
### Variáveis

| Nome | Descrição |
| --- | --- |
| QtmBic | Quantidade da base do ICMS Monofásico |
| AliImo | Alíquota ad rem do ICMS Monofásico |
| VmoIcm | Valor do ICMS Monofásico |

### Fórmula

* AliImo = Alíquota referente à tabela de tributação de ICMS Monofásico no cadastro do produto (E075Pro.TprImo)
* QtmBic = Quantidade convertida para a unidade de tributação de acordo com a tabela de tributação de ICMS Monofásico
* VmoIcm = **QtmBic \* AliImo**

**Exemplo:**

Venda de 1 galão do produto Biodiesel B100. O produto tem em sua tabela de tributação:

* Alíquota ad rem = 0,9456
* Unidade de tributação = Litros
* Unidade de venda = Galão (12 litros)

Dessa forma:

* AliImo = 0,9456
* QtmBic = 12 (arredondamento em 4 casas decimais)
* VmoIcm = 12 \* 0,9456 = 11,35 (arredonda em 2 casas decimais)

---

### Parametrização

* Cliente/fornecedor, produto e transação devem estar configurados para tributação de ICMS. Isto é feito nas telas de Cadastro de Clientes (F085CAD), Cadastro de Fornecedores (F095CAD), Cadastro de Produtos (F075PRO), Transações de Vendas (F001TVE) (em caso de notas de saída) e Transações de Compras (F001TCP) (em caso de notas de entrada)
  + Ficou com alguma dúvida? Acesse Parametrização para calcular ICMS
* A situação tributária de ICMS deve ser 02. Para cadastrá-la, acesse a tela Situações Tributárias (F027STR)
  + Exemplo: situação tributária de ICMS 02 com origem "0 - Nacional", exceto as indicadas nos códigos 3, 4, 5 e 8:  

    ![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/images/icms/monofasico/revisao/1_thumb_0_48.png)
* O produto deve ter uma tabela de tributação de ICMS Monofásico cadastrada válida e com aplicação **3 ou 5** para operações de saída e **4 ou 5** para operações de entrada. Para criar uma tabela de tributação, acesse a tela Tabela de Preço de Venda (F081GTP)  

  ![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/images/icms/monofasico/1_thumb_0_48.png)

+ **Exemplo de uma tabela cadastrada:**

    
  ![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/images/icms/monofasico/revisao/6_thumb_0_48.png)

    
  ![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/images/icms/monofasico/revisao/7_thumb_0_48.png)

    
  ![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/images/icms/monofasico/revisao/8_thumb_0_48.png)

## Páginas relacionadas

* [Cadastro de Clientes (F085CAD)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f085cad.htm)
* [Cadastro de Fornecedores (F095CAD)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f095cad.htm)
* [Cadastro de Produtos (](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075pro.htm)
* [Transações de Vendas (F001TVE)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f001tve.htm)
* [Transações de Compras (F001TCP)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f001tcp.htm)
* [Parametrização para calcular ICMS](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/impostos-icms.htm#parametrizacao)
* [Situações Tributárias (F027STR)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f027str.htm)
* [Tabela de Preço de Venda (F081GTP)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f081gtp.htm)
