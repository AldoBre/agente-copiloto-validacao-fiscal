# Botões

> **Fonte:** F000INE - Via Recebimento de Documento Eletrônico — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f000ine.htm  
> **Trilha:** Ajuda por telas > Suprimentos > Gestão de Recebimento > Notas Fiscais de Entrada  
> **Telas citadas:** E000IPC, E000ISC, F000IDE, F000INE, F000SDV, F017SEL  
> **Identificadores de regras:** —

---
Seleção  
Exibe a tela F000SDV para seleção de informações. Este botão é desabilitado para o usuário logado caso esteja marcado na tela F017SEL.

Processar 

Processa os registros selecionados na tela, ou seja, registros marcados a partir do campo Selecionado existente na guia de Notas Fiscais de Entrada.

Observação

* Antes de processar um registro, é possível alterar alguns campos presentes na guia de Produto e Serviço para que estes dados alterados sejam gravados nas tabelas de notas fiscais. No entanto, somente alguns campos das tabelas-clone E000IPC e E000ISC (tabelas referentes aos campos da tela F000INE) serão atualizados automaticamente, conforme abaixo. Demais campos serão atualizados nas tabelas-clone somente ao utilizar o botão Alterar
  + Produto: Tabelas - Recebimento de Documentos Eletrônicos - Notas Fiscais de Entrada - Itens de Produto (E000IPC):
    - CodPro, CodDer, CodFam, CodDep, CgcOcp, NumOcp, SeqIpo, LauTec, UsuLau, DatLau, HorLau, CgcFab
  + Serviço: Tabelas - Recebimento de Documentos Eletrônicos - Notas Fiscais de Entrada - Itens de Serviço (E000ISC):
    - CodSer, CgcOcp, NumOcp, SeqIso
* No recebimento de uma Nota Fiscal de Compra (NFC) que contém dois itens no XML para o atendimento do mesmo item da Ordem de Compra (OC) e cada linha do XML possuir a quantidade total da ordem, as consistências da tela não serão executadas, uma vez que essas são executadas linha a linha

Alterar

Altera o valor dos campos nas tabelas-clone, como campos referente ao produto (E000IPC) e ao serviço (E000ISC). Desta forma, após a alteração do valor de um campo presente nas guias da tela, para os registros que estiverem selecionados e utilizado este botão, caso seja carregado novamente os documentos em tela, serão carregados os campos com os valores alterados e não com os valores originais que foram obtidos através do XML na importação do documento a partir do web service com.senior.g5.co.int.eletronicos.documentos, porta Receber.

Após clicar em Alterar ou Processar, alguns campos como a transação do item de produto e serviço, não serão mais sugeridos novamente nas próximas vezes que a nota for carregada.

Observação

Após a execução do botão Alterar, o campo UM Fiscal (XML) receberá o mesmo conteúdo do campo UM Nota (ERP).

Importar

Abre a tela de Importação de Documentos Eletrônicos (F000IDE), permitindo selecionar os arquivos XML de NF-e emitidas para serem importados para a grade de notas fiscais de entrada/saída.

## Páginas relacionadas

* [F000SDV](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f000sdv.htm)
* [com.senior.g5.co.int.eletronicos.documentos](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/webservices/com_senior_g5_co_int_eletronicos_documentos.htm)
* [Importação de Documentos Eletrônicos (F000IDE)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f000ide.htm)
