# Campos que representam valores monetários, quantidade e percentual e estão declarados como String

> **Fonte:** Web service Com.senior.g5.co.mct.imp.exclusaocalculo — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/webservices/com_senior_g5_co_mct_imp_exclusaocalculo.htm  
> **Trilha:** Integrações com outros sistemas > Web services > Web services disponíveis no Gestão Empresarial  
> **Telas citadas:** —  
> **Identificadores de regras:** —

---
* Envio no formato ZZZZ,ZZ
* É fundamental não enviar os campos numéricos com separador de milhar, pois ocorrerá erro ao executar a requisição
* Obrigatória a utilização do separador decimal com vírgula, e não com ponto
* Obrigatória a utilização do zero a direita. Por exemplo, se o valor for 350,20, a requisição deve ser enviada com este exato valor. Se o valor enviado for enviado como 350,2, o sistema não irá interpretar a requisição adequadamente

## Exemplo:

number(005,2) = 350,20 - o sistema espera que o número digitado contenha até 3 casas antes da vírgula e obrigatoriamente duas após;

number(015,2): 35000,20 - o sistema espera que o número digitado contenha até 13 casas antes da vírgula e obrigatoriamente duas após;

number(008,4) = 3200,2074 - o sistema espera que o número digitado contenha até 4 casas antes da vírgula e obrigatoriamente duas após.
