# E210, E220 e E250 sem guia de recolhimento

> **Fonte:** Adequação aos leiautes do SPED Fiscal — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/sped/fiscal-icms-ipi/adequacoes-leiautes.htm  
> **Trilha:** Segmentos > Compliance > Escriturações Fiscais Digitais (SPED) > SPED Fiscal (EFD ICMS/IPI)  
> **Telas citadas:** —  
> **Identificadores de regras:** —

---
Quando a apuração do ICMS ST a Restituir/Complementar resultar em Saldo Devedor e não houver guia de recolhimento:

* Nesse cenário o sistema carrega automaticamente o **Saldo Devedor** da apuração do ICMS ST a Restituir/Complementar na apuração do imposto 34 - ICMS ST, sendo que o ajuste em questão deve ser justificado utilizando um dispositivos fiscal com código de ajuste igual a RS101255;
* No registro E210 o sistema lança o total do **Saldo Devedor** da apuração do ICMS ST a Restituir/Complementar no campo **9 - VL\_OUT\_DEB\_ST**;
* No registro E250 o sistema gera uma guia de recolhimento com base na apuração do imposto tipo 34 - ICMS ST (quando a apuração resultar em **Saldo Devedor**).
