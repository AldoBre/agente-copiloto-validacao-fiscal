# F024MSG - Mensagens de Notas Fiscais

> **Fonte:** F024MSG - Mensagens de Notas Fiscais — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f024msg.htm  
> **Trilha:** Ajuda por telas > Cadastros > Mercado e Suprimentos > Parâmetros Fiscais  
> **Telas citadas:** E012FAM, E075DER, E075PRO, E140IPV, F024MSD, F024MSG  
> **Identificadores de regras:** —

---
Ajuda por telas > Cadastros > Mercado e Suprimentos > Parâmetros Fiscais > Mensagens NF

Tela destinada ao cadastramento de mensagens, fiscais ou não, para uso em notas fiscais.

## Campos

Código Mensagem

Código da mensagem para nota fiscal.

Descrição Mensagem

Descrição da mensagem para a nota fiscal. A descrição informada neste campo é utilizada na nota fiscal apenas se não houver mensagem dinâmica cadastrada na tela F024MSD.

Situação Tributária Federal

Código da situação tributária federal para impostos.

Rotina de Aplicação da Mensagem

Rotina em que será aplicada a mensagem especial.

0. Nota Fiscal (Mensagem Fiscal);
1. Contrato (somente para contratos do tipo "08 - Comercial Licitação", informado na página "Mensagens por
   Agrupamento");
2. Mensagem de Aviso em Tela.

Observação

As mensagens fiscais de aplicação "0 - Nota Fiscal" podem ser configuradas para sugestão nas notas fiscais de saída. Para mais informações, consulte a documentação.

Usuário

Código do usuário responsável pela geração da mensagem.

Data Geração

Data da geração da mensagem.

Hora Geração

Hora da geração da mensagem.

Mensagem Fiscal

Indicativo se a mensagem é ou não fiscal.

Processo/Ato Concessório

Número do processo concessório.

Orig.Proc./Ato Concessório

Origem do processo ou ato concessório:

* "0 - Sefaz";
* "1 - Justiça Federal";
* "2 - Justiça Estadual";
* "3 - Secex/RFB";
* "4 - CONFAZ";
* "9 - Outros".

Documento Referenciado

Documento referenciado.

* 1 - Documento de Arrecadação;
* 2 - NF Devolução;
* 3 - NF Retorno;
* 4 - NF Transferência;
* 5 - NF Cobrança Serviços Via Remessa Produto;
* 6 - NF Cobrança Via Remessa;
* 7 - NF Remessa Via Cobrança;
* 8 - NF Retorno de Componentes;
* 9 - NF Complementar;
* 10 - Cupom Fiscal;
* 11 - Coleta e Entrega;
* 12 - NF Produtor;
* 13 - Substituição de NF cancelada;
* 14 - NF Pagamento;
* 15 - NF Referenciada;
* 98 - Listar dados da guia recolhimento do ICMS ST associada à nota fiscal entrada;
* 99 - Listar observação da nota fiscal no SPED.

Interesse Mensagem

Indicativo para especificar o interessado da mensagem:

* "F - Fisco": Quando esta opção estiver selecionada, a mensagem é considerada no grupo infAdFisco (Informações Adicionais de Interesse do Fisco) do arquivo XML. Somente mensagens de aplicação **Nota Fiscal (Mensagem Fiscal)** e que possuírem indicativo de Mensagem Fiscal = "S" podem receber o indicativo "F";
* "C - Contribuinte": Quando esta opção estiver selecionada, a mensagem é considerada no grupo infCpl (Informações Complementares de interesse do Contribuinte) do arquivo XML. Somente mensagens de aplicação **Nota Fiscal (Mensagem Fiscal)** e que possuírem indicativo de Mensagem Fiscal = "N" podem receber o indicativo "C";
* "N - Nenhum": Somente mensagens com aplicação diferente de **Nota Fiscal (Mensagem Fiscal)** podem receber o indicativo "N";
* "P - Produto (Inf. Adic.)": Indica as informações adicionais relativas ao item da nota fiscal na tag de produtos (tag infAdProd);
* "O - Produto (Obs. Cont.)": Indica as observações de uso livre do contribuinte relativas ao item da nota fiscal na tag do item (tag obsCont).
* "I - Produto (Obs. Fisco)": Indica as observações de uso livre do fisco relativas ao item da nota fiscal na tag do item (tag obsFisco).

As tags obsCont e obsFisco possuem duas tags, sendo xCampo (identificação do campo) e xTexto (conteúdo do campo). Para que seja gerada corretamente no XML da Nota Fiscal, o campo Descrição Mensagem deverá ser por um sinal de igual, onde do lado esquerdo fica o valor de xCampo e do lado direito o valor de xTexto. Também será possível retornar o valor de xTexto de forma dinâmica, utilizando o valor informado na mensagem dinâmica que é acessada a partir do botão Mensagem e o valor de xCampo será a o valor de Descrição Mensagem.

Para que as mensagens sejam carregadas na observação dos itens da nota, o campo Mensagem Fiscal deve ser parametrizado igual a "S - Sim" e o campo Interesse Mensag. deve conter selecionada a opção "P - Produto (Inf. Adic.)". Além disso, o cadastro da transação de produtos utilizada na nota fiscal deve ter o código da mensagem desejada no campo "Mensagem - 1", "Mensagem - 2", "Mensagem - 3" ou "Mensagem - 4".

Tp. Ato Concessório

Esse campo é de preenchimento obrigatório, caso a opção definida a partir do campo Orig. Proc./Ato Concessório seja igual a "O - Sefaz". Os tipos são:

* "08 - Termo de Acordo";
* "10 - Regime Especial";
* "12 - "Autorização específica".

Observações

* Os campos que serão exibidos na mensagem (vBCFCP, pFCP...) serão os selecionados pelo usuário na mensagem dinâmica pelo botão Mensagem desta tela. Exemplo:
  + Supondo que esta foi a mensagem dinâmica cadastrada: **Filial: [campo:20], Valor FCP: [campo:21]**;
  + A mensagem de saída seria: **Filial: 1, Valor FCP: 18,00**.
* As opções "O - Produto (Obs. Cont.)" e "I - Produto (Obs. Fisco.)" do campo Interesse Mensagem, além do campo Tp. Ato Concessório foram adicionados, conforme previstos na exigência legal da Nota Técnica de NF-e/NFC-e 2021.004 - Regras de Validação e Novos Campos, que entra em vigor no ambiente de homologação em 14/03/2022 e de produção em 08/08/2022. Desta forma, recomendamos não utilizar estes parâmetros antes das datas mencionadas, já que poderá gerar erro de autorização na nota fiscal.
* É possível utilizar campos de usuário da entidade (tabela) principal a qual a mensagem dinâmica estiver relacionada. Por exemplo, se a entidade principal for Mercado - Item de produto nota fiscal de saída (E140IPV), então será possível utilizar campos de usuário desta tabela. Não é aconselhável utilizar campos de usuário de uma tabela relacionada com a entidade principal. Por exemplo, se a entidade principal for Mercado - Item de produto nota fiscal de saída (E140IPV), então será possível utilizar todos os campos das tabelas relacionadas a essa tabela, como por exemplo: tabela de produto (E075PRO), tabela de derivação (E075DER), tabela de família (E012FAM), entre outras. No entanto, utilizar campos de usuário das tabelas relacionadas com a tabela principal é algo que não deve ser feito, pois podem ocorrer erros na geração da mensagem.

## Botão

Mensagem

Exibe a tela F024MSD para o cadastro de mensagens dinâmicas. Esta tela é exibida apenas quando um registro é inserido ou alterado.

## Páginas relacionadas

* [Ajuda por telas](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/ajuda-telas.htm)
* [F024MSD](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f024msd.htm)
* [documentação](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/manuais_processos/mercado/nf-e/regras-e-sugestoes-valores.htm#mensagens-fiscais)
