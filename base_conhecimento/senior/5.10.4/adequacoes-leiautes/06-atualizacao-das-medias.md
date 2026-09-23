# Atualização das médias

> **Fonte:** Adequação aos leiautes do SPED Fiscal — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/sped/fiscal-icms-ipi/adequacoes-leiautes.htm  
> **Trilha:** Segmentos > Compliance > Escriturações Fiscais Digitais (SPED) > SPED Fiscal (EFD ICMS/IPI)  
> **Telas citadas:** F075CEP, F660INT  
> **Identificadores de regras:** —

---
Mensalmente, é necessário realizar a atualização das médias a partir do campo **Atualização da Média Móvel Ponderada** da tela F075CEP.

* A rotina atualiza a média ponderada móvel para cada data em que houve movimentação para um determinado produto/derivação no Controle e atribui o código da Tabela 5.7 aos registros de saídas e devoluções.
  + As devoluções de saídas terão seus valores atualizados pela rotina, sendo que a entrada no Controle receberá os valores das bases de cálculo e impostos médios da data da venda de forma proporcional à quantidade devolvida. Esse processo ocorre durante a atualização das médias, portanto devoluções que foram integradas anteriormente pelo movimento de entradas **apresentarão outro valor no Controle** após a atualização das médias.
* Empresas que utilizam o Controle online ou com origem nos movimentos de Mercado e Suprimentos **devem executar essa rotina mensalmente** por meio da tela F075CEP, de forma manual. A integração online das notas de entradas e saídas **não atualiza** a média ponderada móvel. Para essas empresas, com os documentos do Comercial já integrados no Controle será preciso:
  + Integrar os documentos fiscais para tributos (tela F660INT);
  + Se necessário, fazer a integração das entradas e saídas com o módulo de origem **Comercial** (F075CEP);
  + Informar o período das médias a serem calculadas, preencher o módulo de origem como **Tributos** e processar a atualização das médias;
* A opção será selecionada automaticamente ao integrar entradas e saídas com o módulo de origem **Tributos** a partir de 01/01/2021;
* Não é possível calcular as médias de um período anterior a 01/01/2021.

## Páginas relacionadas

* [F075CEP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075cep.htm)
* [F660INT](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f660int.htm)
