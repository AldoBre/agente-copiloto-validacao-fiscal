# Tela Moedas - Cadastro (F031AIM)

> **Fonte:** F440GNE - Nota Fiscal de Entrada Agrupada — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f440gne.htm  
> **Trilha:** Ajuda por telas > Suprimentos > Gestão de Recebimento > Notas Fiscais de Entrada  
> **Telas citadas:** F031AIM, F051IMP  
> **Identificadores de regras:** —

---
Na tela Moedas - Cadastro, é configurado o índice da moeda usada para o cálculo do imposto (configurado na tela Cadastro de Imposto (F051IMP)). Caso o Tipo de período informado na configuração de imposto seja N - Nenhum, o processo de busca irá seguir o padrão adotado pelo ERP. Caso seja diferente, a busca pelo índice irá seguir as seguintes regras:

## Exemplo

Como exemplo, para simplificar, vamos usar uma Nota Fiscal de Entrada com a data de entrada sendo 15/01/2023:

* N - Nenhum:
  + Data para busca do índice: 15/01/2023;
  + Essa busca leva em consideração os índices gerados em um intervalo de dois anos (padrão atual do ERP).

* M - Mensal:
  + Data para busca do índice: 01/01/2023;
  + A data é convertida para o primeiro dia do mês da data de parâmetro;
  + O índice será localizado apenas se o mesmo estivar cadastrado na data correta: 01/01/2023.

* S - Semestral:
  + Data para busca do índice: 01/01/2023;
  + Caso o mês da data corrente seja menor ou igual a **6**, assume-se o primeiro dia do primeiro semestre do ano;
  + Caso o mês da data corrente seja superior a **7**, assume-se o primeiro dia do segundo semestre do ano (01/07/XXXX);
  + O índice será localizado apenas se o mesmo estivar cadastrado na data correta: 01/01/2023 ou 01/07/XXXX.

* A - Anual:
  + Data para busca do índice: 01/01/2023;
  + A data é convertida para o primeiro dia do ano da data de parâmetro;
  + O índice será localizado apenas se o mesmo estivar cadastrado na data correta: 01/01/2023.

## Páginas relacionadas

* [Moedas - Cadastro](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f031aim.htm)
