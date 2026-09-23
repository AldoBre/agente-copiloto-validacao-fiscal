# Geração de logs de títulos do contas a receber em notas fiscais de saída

> **Fonte:** F140GNF - Notas Fiscais de Saída — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f140gnf.htm  
> **Trilha:** Ajuda por telas > Mercado > Gestão de Faturamento e Outras Saídas > Notas Fiscais de Saída  
> **Telas citadas:** F000PGS, F000PPD, F098REG  
> **Identificadores de regras:** VEN-140CNFEC01, VEN-140CNFEC02, VEN-140CNFEC03

---
Para utilização da rotina de geração de logs de títulos do contas a receber em notas de saída são necessárias algumas configurações no sistema:

1. Na tela F000PGS, marcar o parâmetro global LogNfsTit, como "S";
2. Na tela F000PPD, definir os parâmetros dinâmicos LOG.NFS.TIT.CRE.140CNFEC01, LOG.NFS.TIT.CRE.140CNFEC02, LOG.NFS.TIT.CRE.140CNFEC03, LOG.NFS.TIT.CRE.EMISSAO e LOG.NFS.TIT.CRE.GERAR, configurados como "S";
3. Na tela F098REG, ativar os identificadores VEN-140CNFEC01, VEN-140CNFEC02 e VEN-140CNFEC03 com uma regra vinculada (a regra pode estar em branco);
4. Gravar a tabela de usuário no banco de dados para gravação dos logs. A tabela de usuário deve ser criada através do CBDS e deve estar exatamente compatível com os campos necessários para a utilização da rotina, conforme orientações abaixo:

   ## Orientações

   * O nome da tabela de usuário deve ser “USU\_T140LOGTIT”;
   * Para adicionar os campos da tabela, basta clicar com o botão direito em cima da pasta Colunas e selecionar Nova Coluna;
   * Após informar os valores de cada coluna clique no botão Salvar;
   * Após criar todos os campos, clique no botão com desenho de raio (Confirmar personalização no banco) para confirmar as alterações.

   Campos necessários:

   | Nome do campo | Máscara | Tipo | Tamanho |
   | --- | --- | --- | --- |
   | USU\_SEQUENCIAL | Z[11]9 | Number | 12 |
   | USU\_DATA | DD/MM/YYYY | Date | 0 |
   | USU\_HORA | hh:mm:ss | Time | 0 |
   | USU\_CODEMP | ZZZ9 | Number | 4 |
   | USU\_CODFIL | ZZZZ9 | Number | 5 |
   | USU\_CODSNF | U[3] | String | 3 |
   | USU\_NUMNFV | ZZZ.ZZZ.ZZ9 | Number | 9 |
   | USU\_USUARIO | Z[9]9 | Number | 10 |
   | USU\_ORIGEM | A[10] | String | 10 |
   | USU\_OPERACAO | A[50] | String | 50 |
   | USU\_ERRO | A[5] | String | 5 |
   | USU\_OK | A[3] | String | 3 |
   | USU\_NUMTIT | U[15] | String | 15 |
   | USU\_CODTPT | U[3] | String | 3 |
   | USU\_CODTNS | A[5] | String | 5 |

## Páginas relacionadas

* [F000PGS](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm)
* [LogNfsTit](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#LogNfsTit)
* [F000PPD](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000ppd.htm)
* [LOG.NFS.TIT.CRE.140CNFEC01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000ppd.htm#LOG.NFS.TIT.CRE.140CNFEC01)
* [LOG.NFS.TIT.CRE.140CNFEC02](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000ppd.htm#LOG.NFS.TIT.CRE.140CNFEC02)
* [LOG.NFS.TIT.CRE.140CNFEC03](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000ppd.htm#LOG.NFS.TIT.CRE.140CNFEC03)
* [LOG.NFS.TIT.CRE.EMISSAO](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000ppd.htm#LOG.NFS.TIT.CRE.EMISSAO)
* [LOG.NFS.TIT.CRE.GERAR](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000ppd.htm#LOG.NFS.TIT.CRE.GERAR)
* [F098REG](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f098reg.htm)
* [VEN-140CNFEC01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_140cnfec01.htm)
* [VEN-140CNFEC02](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_140cnfec02.htm)
* [VEN-140CNFEC03](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_140cnfec03.htm)
