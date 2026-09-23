# Regra:

> **Fonte:** Identificador de Regra — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/com_000alstr01.htm#Regra  
> **Trilha:**   
> **Telas citadas:** —  
> **Identificadores de regras:** —

---
Definir Alfa VsCodStr;  
Definir Alfa VenACodStrSeqIte;  
Definir Alfa VenAWebSer;  
Definir Alfa VsOrigem;

Inicio

Se ((VsOrigem="PED") ou (VsOrigem="NFS"))

Se ((VenAWebSer="GRAVARNOTAFISCALSAIDA") ou (VenAWebSer="SIMULARPEDIDOS") ou (VenAWebSer="GRAVARPEDIDOS"))

VsCodStr=VenACodStrSeqIte; @Se a regra foi chamada dos webservices acima, a variável VenACodStrSeqIte conterá o valor informado na requisição@

Fim
