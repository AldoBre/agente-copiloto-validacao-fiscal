# Exemplo:

> **Fonte:** Identificador de Regra — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_000alicd01.htm  
> **Trilha:**   
> **Telas citadas:** E120IPD, E140IPV  
> **Identificadores de regras:** —

---
Definir Alfa VSOrigem;   
SE (VSOrigem="PEDIDO")  

Inicio  
E120IPD.Vlrlcd - 100;  
E120IPD.MotDes = 7;  
Fim

Senao

Inicio  
E140IPV.VlrIcd = 100;  
E140IPV.MotDes = 7;  
Fim;
