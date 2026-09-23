# E210, E220 e E250 com guia de recolhimento

> **Fonte:** Adequação aos leiautes do SPED Fiscal — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/sped/fiscal-icms-ipi/adequacoes-leiautes.htm  
> **Trilha:** Segmentos > Compliance > Escriturações Fiscais Digitais (SPED) > SPED Fiscal (EFD ICMS/IPI)  
> **Telas citadas:** —  
> **Identificadores de regras:** —

---
Quando a apuração do ICMS ST a Restituir/Complementar resultar em Saldo Devedor e houver guia de recolhimento:

* Nesse cenário, a apuração do imposto 34 - ICMS ST não será impactada, pois o recolhimento do ICMS ST a Restituir/Complementar foi feito em uma guia especifica;
* No registro E210 o sistema lança o total do **Saldo Devedor** da apuração do ICMS ST a Restituir/Complementar no campo **9 - VL\_OUT\_DEB\_ST**;
* No registro E250 o sistema gera uma guia de recolhimento com base na apuração do imposto tipo 34 - ICMS ST (quando a apuração resultar em **Saldo Devedor**) e outra guia com base no **Saldo Devedor** do ICMS ST Complementar.
