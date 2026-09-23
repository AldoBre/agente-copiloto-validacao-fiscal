# Exemplo

> **Fonte:** Detalhamento dos Impostos — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/impostos_nos_documentos_fiscais.htm  
> **Trilha:** Segmentos > Compliance > Configurações para cálculos fiscais > Impostos  
> **Telas citadas:** F001TVE, F075PPC, F085CAD  
> **Identificadores de regras:** —

---
1º) Ligação Cliente x Produto (F075PPC)

Consumidor Final = S, calcula os impostos;

Consumidor Final = N, não calcular os impostos;

Consumidor Final = '' ver 3° item

2º) Cliente (F085CAD)

Consumidor Final = S, calcula os impostos;

Consumidor Final = N, não calcular os impostos;

Consumidor Final = '' ver 3° item

3º) Transação (F001TVE)

Aplicação da Operação = S (Consumo Próprio) ou V (Serviço), calcula os impostos;

Caso contrário não calcula os impostos.
