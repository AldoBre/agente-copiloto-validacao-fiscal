# Grupo I03 - Produtos e Serviços / Grupo de Exportação

> **Fonte:** Leiautes NF-e e NFC-e — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/leiaute-nf-e-nfc-e.htm  
> **Trilha:** Segmentos > Compliance > Documentos Eletrônicos > NF-e | NFC-e (Nota Fiscal Eletrônica) > Nota Fiscal Eletrônica 4.0  
> **Telas citadas:** F140GNF  
> **Identificadores de regras:** —

---
Abaixo serão apresentadas informações pontuais acerca da geração das tags do grupo <detExport> com base em informações manuais preenchidas na geração da nota fiscal pela tela Notas Fiscais de Saída (F140GNF).

Consulte a documentação completa da geração do grupo <detExport> clicando aqui.

| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação | Origem |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 128.20 | I50 | detExport | Grupo de informações de exportação para o item | G | I01 |  | 0-500 |  | Informar apenas no Drawback e nas exportações | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 128.21 | I51 | nDraw | Número do ato concessório de Drawback | E | I50 | N | 0-1 | 0, 9 ou 11 | O número do Ato Concessório de Suspensão deve ser preenchido com 11 dígitos (AAAANNNNNND) e o número do Ato Concessório de Drawback Isenção deve ser preenchido com 9 dígitos (AANNNNNND). (Observação incluída na NT 2013/005 v. 1.10) | Gera a tag conforme informação do campo Número do Drawback da tela F140GNF, guia Produtos. |
| 128.22 | I52 | exportInd | Grupo sobre exportação indireta | G | I50 |  | 0-1 |  |  | Gerado conforme o padrão do leiaute da SEFAZ. |
| 128.23 | I53 | nRE | Número do Registro de Exportação | E | I52 | N | 1-1 | 12 |  | Gera a tag conforme informação do campo Núm. Reg. Exportação da tela F140GNF, guia Produtos. |
| 128.24 | I54 | chNFe | Chave de Acesso da NF-e recebida para exportação | E | I52 | N | 1-1 | 44 | NF-e recebida com fim específico de exportação Observação: No caso de operação com CFOP 3.503, informar a chave de acesso da NF-e que efetivou a exportação | Gera a tag conforme informação do campo Chave Eletrônica Exp da tela F140GNF, guia Produtos. |
| 128.25 | I55 | qExport | Quantidade do item realmente exportado | E | I52 | N | 1-1 | 11v4 | A unidade de medida desta quantidade é a unidade de comercialização deste item. No caso de operação com CFOP 3.503, informar a quantidade de mercadoria devolvida | Gera a tag conforme informação do campo Qtde. U.M. Venda da tela F140GNF, guia Produtos. |

## Páginas relacionadas

* [F140GNF](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f140gnf.htm)
* [aqui.](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/referenciacao_nf_entrada_processo_exportacao.htm)
