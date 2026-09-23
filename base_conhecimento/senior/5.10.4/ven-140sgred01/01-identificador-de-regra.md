# Identificador de Regra

> **Fonte:** Identificador de Regra — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_140sgred01.htm  
> **Trilha:**   
> **Telas citadas:** —  
> **Identificadores de regras:** VEN-140SGRED01

---
## VEN-140SGRED01

**Módulo:** VEN - Vendas.

**Finalidade:** O objetivo desde identificador de regras é sugerir o código de redução de ICMS e/ou o ICMS Especial do item de produto ou serviço que está sendo digitado na nota fiscal.

**Características:** A sequência para a sugestão do código de redução de impostos e para o ICMS Especial é: Cadastro Transação > Definições do Cliente > Cadastro do produto / Serviço.

Após essa sequência de sugestões, o ponto de regra é acionado. Para a identificação de qual sugestão está sendo alterada, deverá ser utilizada a variável VenATipImp, sendo “Eˮ (ICMS Especial) e “Rˮ (Redução de imposto). Quando executada a sugestão do código de redução de imposto, as variáveis do código de ICMS Especial irão zeradas, e vice-versa.

**Tela:** Faturamento

**Transação:** Não se aplica.

**Regra:**

definir numero VenNCodFil;  
definir alfa VenATipImp;  
definir alfa VenACodTrd;  
definir alfa VenACodTrdTns;  
definir alfa VenACodTrdCli;  
definir alfa VenACodTrdProSer;  
definir alfa VenACodTic;  
definir alfa VenACodTicTns;  
definir alfa VenACodTicCli;  
definir alfa VenACodTicProSer;  

se (VenATipImp = "R")  
{  
se (VenNCodFil > 1)  
VenACodTrd = "R20";  
}  

se (VenATipImp = "E")  
{  
se (VenNCodFil > 1)  
VenACodTic = "12";

**Variáveis Disponibilizadas:**

| Nome | Tipo | Observações | Retorna Valor |
| --- | --- | --- | --- |
| VenAOriMer | ALFA | Código de origem fiscal (do produto ou serviço), conforme item da nota fiscal de saída. | N |
| VenACodStr | ALFA | Código da situação tributária de ICMS do item de produto ou de serviço, conforme item que estiver sendo processado . | N |
| VenACodTrdTns | ALFA | Código de redução de impostos padrão informado no cadastro da transação. | N |
| VenACodTrdCli | ALFA | Código de redução de impostos padrão informado no cadastro do cliente. | N |
| VenACodTrdProSer | ALFA | Código de redução de impostos padrão infromado no cadastro do produto. | N |
| VenNCodEmp | NÚMERO | Código da empresa da nota fiscal que está sendo digitada. | N |
| VenNCodFil | NÚMERO | Código da filial da nota fiscal que está sendo processada. | N |
| VenACodSnf | ALFA | Código da série da nota fiscal que está sendo processada. | N |
| VenNNumNfv | NÚMERO | Número da nota fiscal que está sendo processada. | N |
| VenNSeqIte | NÚMERO | Sequência do item da nota fiscal que está sendo processada. | N |
| VenATipIte | ALFA | Tipo do item, "P" para produtos, "S" para serviços. | N |
| VenACodProSer | ALFA | Código do produto ou serviço que está sendo processado. | N |
| VenACodDer | ALFA | Código da derivação, para o caso de processamento de produto. | N |
| VenACodDep | ALFA | Código do depósito do produto que está sendo processado. | N |
| VenACodTns | ALFA | Código da transação do item que está sendo processado. | N |
| VenNCodCli | NÚMERO | Código do cliente da nota fiscal que está sendo processada. | N |
| VenACodTrd | ALFA | Código da redução de imposto. | S |
| VenATipImp | ALFA | Código de identificação de qual sugestão está sendo executada. Se "E" (ICMS Especial) ou "R" (Redução de impostos). | N |
| VenACodTic | ALFA | Código do ICMS Especial. | S |
| VenACodTicTns | ALFA | Código do ICMS Especial padrão informado no cadastro da transação. | N |
| VenACodTicCli | ALFA | Código do ICMS Especial padrão informado no cadastro do cliente. | N |
| VenACodTicProSer | ALFA | Código do ICMS Especial padrão informado no cadastro do produto. | N |

Atenção

Caso o parâmetro global LisVarReg esteja habilitado, a variável ListaVariaveis estará disponível em todos os identificadores de regras do sistema. O conteúdo desta variável lista os campos disponibilizados no identificador de regras em questão.

Não é aconselhada a ativação desse parâmetro global para o uso cotidiano. Esse recurso de listagem dos campos de identificadores auxilia a construção de regras e o Suporte para, por exemplo, depuração ou quando não houver acesso à documentação dos identificadores de regras.

## Páginas relacionadas

* [LisVarReg](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#LisVarReg)
