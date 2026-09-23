# Fórmulas para os tipos de cálculo DIFAL

> **Fonte:** F009PPE - Parâmetros por Estado — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f009ppe.htm  
> **Trilha:** Ajuda por telas > Cadastros > Mercado e Suprimentos > Parâmetros Fiscais > Parâmetros por Estado  
> **Telas citadas:** F070PSE  
> **Identificadores de regras:** —

---
**1 - Dupla Dif. Alíquota e 3 - Dupla Dif. Valor:**

Valor Base do DIFAL = Valor Base do ICMS \* Percentual de ICMS interna no estado de destino;  
Arredonda(Valor Base do DIFAL, 2);  
Valor Base do ICMS = Valor Base do ICMS - Valor Base do DIFAL - Valor do ICMS para fundo de combate à pobreza na UF de destino;  
Arredonda(Valor Base do ICMS , 2);  
Valor do ICMS = Valor Base do ICMS \* Percentual de ICMS da operação;  
Arredonda(Valor do ICMS , 2);  
Valor do DIFAL = Valor Base do DIFAL- Valor do ICMS;  
Arredonda(Valor do DIFAL, 2).

**2 - Simples:**

Verifica se há diferença entre o Percentual de ICMS do estado de destino e do Percentual de ICMS da operação. Se houver, calcula o DIFAL pela diferença (caso as bases de ICMS origem e destino sejam iguais) ou pela diferença de valor (caso as bases de ICMS origem e destino sejam diferentes).

**5 - Simples com desconto do valor do ICMS:**

Valor Base do DIFAL = Valor Base do ICMS;  
Valor do DIFAL = (Valor Base do DIFAL \* Percentual de ICMS interna no estado de destino) / 100;  
Arredonda(Valor do DIFAL, 2);  
Valor do DIFAL = Valor do DIFAL - Valor do ICMS;  
Arredonda(Valor do DIFAL, 2).

**6 - Simples com aplicação da diferença de alíquota:**

Valor Base do DIFAL = Valor Base do ICMS;  
Diferença de alíquota = (Percentual de ICMS interna no estado de destino - Percentual de ICMS da operação) / 100;  
Valor do DIFAL = Valor Base do DIFAL \* Diferença de alíquota;  
Arredonda(Valor do DIFAL, 2).

**7 - Dupla com diferença de alíquota por dentro:**

Diferença de alíquota = (Percentual de ICMS interna no estado de destino - Percentual de ICMS da operação) / 100;  
Valor Base do DIFAL = Valor Base do ICMS / (1 - Diferença de alíquota);  
Arredonda(Valor Base do DIFAL, 2);  
Valor do DIFAL = Valor Base do DIFAL \* Diferença de alíquota;  
Arredonda(Valor do DIFAL, 2).

**8 - Dupla com desconto do ICMS e alíquota interna por dentro com desconto do valor do ICMS:**

Valor Base do DIFAL = Valor Base do ICMS - Valor do ICMS;  
Valor Base do DIFAL = Valor Base do DIFAL / (1 - (Percentual de ICMS interna no estado de destino / 100));  
Arredonda(Valor Base do DIFAL, 2);  
Valor do DIFAL = (Valor Base do DIFAL \* Percentual de ICMS interna no estado de destino) / 100;  
Arredonda(Valor do DIFAL, 2);  
Valor do DIFAL = Valor do DIFAL - Valor do ICMS.

**9 - Dupla com alíquota interna por dentro:**

Valor Base do DIFAL = Valor Base do ICMS / (1 - (Percentual de ICMS interna no estado de destino / 100));  
Arredonda(Valor Base do DIFAL, 2);  
Diferença de alíquota = (Percentual de ICMS interna no estado de destino - Percentual de ICMS da operação) / 100;  
Valor do DIFAL = Valor Base do DIFAL \* Diferença de alíquota;  
Arredonda(Valor do DIFAL, 2).

**10 - Dupla com desconto do ICMS e alíquota interna por dentro com aplicação da diferença de alíquota:**

Valor Base do DIFAL = Valor Base do ICMS - Valor do ICMS;  
Valor Base do DIFAL = Valor Base do DIFAL / (1 - (Percentual de ICMS interna no estado de destino / 100));  
Arredonda(Valor Base do DIFAL, 2);  
Diferença de alíquota = (Percentual de ICMS interna no estado de destino - Percentual de ICMS da operação) / 100;  
Valor do DIFAL = Valor Base do DIFAL \* Diferença de alíquota;  
Arredonda(Valor do DIFAL, 2).

**11 - Dupla com desconto do ICMS e alíquota interna (ICMS + FCP) por dentro com desconto do valor do ICMS:**

Valor Base do DIFAL = Valor Base do ICMS - Valor do ICMS;  
Valor Base do DIFAL = Valor Base do DIFAL / (1 - ((Percentual de ICMS interna no estado de destino + Percentual do ICMS para fundo de combate à pobreza no estado de destino) / 100));  
Arredonda(Valor Base do DIFAL, 2);  
Valor do DIFAL = (Valor Base do DIFAL \* Percentual de ICMS interna no estado de destino) / 100;  
Arredonda(Valor do DIFAL, 2);  
Valor do DIFAL = Valor do DIFAL - Valor do ICMS.

**12 - Dupla c/ aplicação da diferença de alíq. c/ redução de base de cálculo**

Percentual de Redução de Base de Cálculo é parametrizado na tela F070PSE.  
Valor Base do DIFAL = (Valor Base do ICMS sem redução - Valor do ICMS) / ( 1 - Percentual de ICMS interna no estado de destino)  
Valor Base do DIFAL = Valor Base do DIFAL \* (Percentual de Redução de Base de Cálculo/100)  
Arredonda(Valor Base do DIFAL, 2);  
Valor do DIFAL = Valor Base do DIFAL \* Percentual de ICMS interna no estado de destino  
Arredonda(Valor do DIFAL, 2);  
Valor do DIFAL = Valor do DIFAL - Valor ICMS

## Páginas relacionadas

* [F070PSE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070pse.htm)
