# Identificador de Regra

> **Fonte:** Identificador de Regra — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/cpr_440gercs01.htm  
> **Trilha:**   
> **Telas citadas:** F440GNE  
> **Identificadores de regras:** CPR-440GERCS01

---
## CPR-440GERCS01

**Módulo:** CPR - Compras.

**Finalidade:** Na geração de notas fiscais de entrada dos tipos 3, 6, 7 e 10, que por sua vez geram notas fiscais de saída, o sistema carrega nos itens as informações dos campos abaixo da entrada para saída:  
CODSTR - Código da situação tributária de ICMS  
CSTIPI - Código da situação tributária de IPI  
CSTPIS - Código da situação tributária de PIS  
CSTCOF - Código da situação tributária de COFINS  

Ou seja, não executado a geração dos códigos em questão. Com isso não executada também a chamada dos identificadores relacionados a estes códigos.  

Este identificador de regras serve para que na geração desta modalidade de nota fiscal de saída o sistema também execute a sugestão de códigos de situação tributária, e como consequência a execução dos identificadores relacionados a eles.

**Características:** A partir da versão 5.6.2.1 este identificador de regra passou a trabalhar com a possibilidade de regra com objetivo de permitir informar quais códigos das situações tributárias não devem ser herdados da nota fiscal de entrada para a nota fiscal de saída e consequentemente venham a sofrer a geração pelo sistema.  

OBS.01: Com o identificador de regras inexistente ou inativo, o sistema herda as situações tributárias da nota fiscal de entrada para a nota fiscal de saída e não são executadas as rotinas de geração de código de situação tributária.  

OBS.02: Com o identificador de regras existente e ativo (e sem regra), o sistema não herda as situações tributárias da nota fiscal de entrada para a nota fiscal de saída e serão executadas as rotinas de geração de código de situação tributária.  

OBS.03: Com o identificador de regras existente e ativo (e com uso de regra), o sistema permite parametrizar quais situações tributárias deseja herdar (obviamente que os que não forem herdados serão gerados). Para isso a funcionalidade se dá desta forma.  

CprNHerStr = 0 (não herda e executa a geração)  
CprNHerStr = 1 (herda e não executa a geração)

**Tela:** F440GNE

**Transação:** Não se aplica.

**Regra:**

Definir Alfa VCprNHerStr;  
Definir Alfa VCprNHerIpi;  
Definir Alfa VCprNHerPis;  
Definir Alfa VCprNHerCof;  

  
Definir Alfa Quebra;  
Definir Alfa StrAux;  

inicio  

RetornaAscii(13, Quebra);  

IntParaAlfa(CprNHerStr, VCprNHerStr);  
IntParaAlfa(CprNHerIpi, VCprNHerIpi);  
IntParaAlfa(CprNHerPis, VCprNHerPis);  
IntParaAlfa(CprNHerCof, VCprNHerCof);  

StrAux =   
 "CprNHerStr: " + VCprNHerStr + Quebra +   
 "CprNHerIpi: " + VCprNHerIpi + Quebra +   
 "CprNHerPis: " + VCprNHerPis + Quebra +   
 "CprNHerCof: " + VCprNHerCof + Quebra +   
 "[&OK]";  
Mensagem(Retorna,StrAux);  

XX = 0;  
fim

**Variáveis Disponibilizadas:**

| Nome | Tipo | Observações | Retorna Valor |
| --- | --- | --- | --- |
| CprNHerStr | NÚMERO | Indicativo para herdar o código da situação tributária de ICMS [ 0 (zero) não herda / 1 (um) herda ] | S |
| CprNHerIpi | NÚMERO | Indicativo para herdar o código da situação tributária de IPI [ 0 (zero) não herda / 1 (um) herda ] | S |
| CprNHerPis | NÚMERO | Indicativo para herdar o código da situação tributária de PIS [ 0 (zero) não herda / 1 (um) herda ] | S |
| CprNHerCof | NÚMERO | Indicativo para herdar o código da situação tributária de COFINS [ 0 (zero) não herda / 1 (um) herda ] | S |

Atenção

Caso o parâmetro global LisVarReg esteja habilitado, a variável ListaVariaveis estará disponível em todos os identificadores de regras do sistema. O conteúdo desta variável lista os campos disponibilizados no identificador de regras em questão.

Não é aconselhada a ativação desse parâmetro global para o uso cotidiano. Esse recurso de listagem dos campos de identificadores auxilia a construção de regras e o Suporte para, por exemplo, depuração ou quando não houver acesso à documentação dos identificadores de regras.

## Páginas relacionadas

* [LisVarReg](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#LisVarReg)
