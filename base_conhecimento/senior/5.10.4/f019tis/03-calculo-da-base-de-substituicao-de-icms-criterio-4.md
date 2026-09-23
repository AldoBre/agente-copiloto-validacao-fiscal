# Cálculo da Base de Substituição de ICMS |
Critério 4

> **Fonte:** F019TIS - Tipos Substituições Impostos / Modalidade Base Cálculo / Antecipação - Por Estado — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f019tis.htm  
> **Trilha:** Ajuda por telas > Cadastros > Mercado e Suprimentos > Parâmetros Fiscais > Substituições Impostos/Modalidade Base Cálculo/Antecipação  
> **Telas citadas:** F009PPE, F019TIS, F075PRO  
> **Identificadores de regras:** —

---
Cálculo da Base de Substituição de ICMS quando o
critério de cálculo é "4 - Pela carga tributária média":

Processo de cálculo:

1. VALOR TOTAL DAS OPERAÇÕES: Valor bruto menos descontos da Nota Fiscal, Somado valor de IPI ((Bruto - Descontos) + IPI);
2. VALOR DO ICMS OPERAÇÃO PRÓPRIA: Valor do ICMS da nota fiscal;
3. ALÍQUOTA INTERNA DE ICMS DO PRODUTO: Percentual informado na tela F019TIS, campo % Imposto;
4. PERCENTUAL DE CARGA TRIBUTÁRIA MÉDIA: Percentual informado na tela F019TIS, campo % Carga Trib. Média;
5. VALOR DO ICMS-ST ( A x D ): (VALOR TOTAL DAS OPERAÇÕES \* PERCENTUAL DE CARGA TRIBUTÁRIA MÉDIA);
6. BASE DE CALCULO IMPOSTO SUBSTITUIÇÃO [(B + E) / C]: [(VALOR DO ICMS OPERAÇÃO PRÓPRIA + VALOR DO ICMS-ST) / ALÍQUOTA INTERNA DE ICMS DO PRODUTO].

Desta equação são extraídas a base de ICMS ST ("E") e o valor do ICMS ST ("F"). Segue exemplo com valores:

* Produto , configurado para 10% de IPI (Tela F075PRO);
* Cliente do estado RS, com % ICMS saída contribuinte configurado para 7% (Tela F009PPE);
* Nota fiscal com 100 unidades do produto com preço de R$ 10,00 cada.

Nesta situação teremos os seguintes valores:

1. VALOR TOTAL DAS OPERAÇÕES: R$ 1000,00 + R$ 100 = R$ 1100,00 ((Bruto - Descontos) + IPI);
2. VALOR DO ICMS OPERAÇÃO PRÓPRIA: R$ 70,00 (7% aplicado sobre a base de R$ 1000,00);
3. ALÍQUOTA INTERNA DE ICMS DO PRODUTO: 17%;
4. PERCENTUAL DE CARGA TRIBUTÁRIA MÉDIA: 15%;
5. VALOR DO ICMS-ST ( A x D ): (R$ 1100,00 \* (15/100)) = R$ 165,00
6. BASE DE CALCULO IMPOSTO SUBSTITUIÇÃO [(B + E) / C]: [(R$ 70,00 + R$ 165,00) / (17/100)] = R$ 1382,35

Processo de cálculo ESTIMATIVA SIMPLIFICADO:

1. VALOR TOTAL DAS OPERAÇÕES: Valor bruto menos descontos da Nota Fiscal, somado
   valor de IPI. ((Bruto - Descontos) + IPI);
2. ALÍQUOTA INTERNA DE ICMS DO PRODUTO: Percentual informado na tela F019TIS,
   campo % Imposto.
3. VALOR DO ICMS OPERAÇÃO PRÓPRIA: Valor do ICMS da nota fiscal.
4. MARGEM DE LUCRO (ANEXO XI): Percentual informado na tela F019TIS, campo %Margem/base;
5. VALOR AGREGADO (A x D);
6. PERCENTUAL DE CARGA TRIBUTÁRIA MÉDIA: Percentual informado na tela F019TIS,
   campo % Carga Trib. Média
7. VALOR DO ICMS-ST - ESTIMATIVA SIMPLIFICADO (E x F): (VALOR TOTAL DAS OPERAÇÕES \* PERCENTUAL DE CARGA
   TRIBUTÁRIA MÉDIA)
8. BASE DE CALCULO IMPOSTO SUBSTITUIÇÃO [(C + G) / B]: [(VALOR DO ICMS OPERAÇÃO
   PRÓPRIA + VALOR DO ICMS-ST) / ALÍQUOTA INTERNA DE ICMS DO PRODUTO]

Nesta
situação teremos os seguintes valores:

1. VALOR TOTAL DAS OPERAÇÕES: R$ 1000,00;
2. ALÍQUOTA INTERNA DE ICMS DO PRODUTO: 17% (Tela F019TIS, campo % Imposto);
3. VALOR DO ICMS OPERAÇÃO PRÓPRIA: R$ R$ 161,90 (valor total dos produtos x B);
4. MARGEM DE LUCRO (ANEXO XI): 38%;
5. VALOR AGREGADO (A x D): 380,00
6. PERCENTUAL DE CARGA TRIBUTÁRIA MÉDIA: 16% (Tela F019TIS, campo % Carga Trib.
   Média);
7. VALOR DO ICMS-ST - ESTIMATIVA SIMPLIFICADO (E x F): R$ 60,80
8. BASE DE CALCULO IMPOSTO SUBSTITUIÇÃO [(C + G) / B]: R$ 1310,35
