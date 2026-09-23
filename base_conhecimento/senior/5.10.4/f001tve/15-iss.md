# ISS

> **Fonte:** F001TVE - Transações de Vendas — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f001tve.htm  
> **Trilha:** Ajuda por telas > Cadastros > Transações > Parâmetros por Gestão  
> **Telas citadas:** F070FVE  
> **Identificadores de regras:** —

---
Arredondamento Base ISS

Indicativo se o valor do arredondamento será considerado na base de ISS.

Importante

O parâmetro Utiliza regra arredondamento ABNT da tela Parâmetros da Filial para Vendas (F070FVE) também interfere no arredondamento. Para mais detalhes, consulte a documentação acerca da regra de arredondamento da ABNT.

Por padrão, o sistema realiza o arredondamento matemático:

* Se o algarismo a ser conservado for seguido de um algarismo maior ou igual a "5", soma-se uma unidade ao algarismo a ser conservado.
* Se o algarismo a ser conservado for seguido de um algarismo menor que "5", o algarismo a ser conservado é mantido sem alteração.

O arredondamento matemático não contempla apenas o último tópico da regra de arredondamento da ABNT, sendo então necessário ativar o parâmetro Utiliza regra arredondamento ABNT para aplicar o arredondamento conforme essa norma, quando for necessário.

Outras Base ISS

Indicativo se o valor de outras despesas será considerado na base de ISS.

Encargos Base ISS

Indicativo se o valor de encargos será considerado na base de ISS.

Outras Destacadas Base ISS

Indicativo se o valor de outras despesas destacadas será considerado na base de ISS.

ISS na NF Saída

Indica como o valor do ISS é considerado no valor líquido da nota fiscal,
adicionado, subtraído ou não influirá.

Valor Mínimo ISS

Valor mínimo de ISS considerado na nota fiscal.

Código de Tributação do ISSQN

Código de tributação do ISS. É consistido com o campo ISS
NFS da seguinte forma ao gravar as alterações:

* Se ISS NFS = "-", somente a opção "R - Retida";
* Se ISS NFS = "+", somente a opção "N-Normal".

Observação

O sistema não usa o valor desse campo em nenhum cálculo ou processo, somente envia o que está configurado na transação para a tag **imposto - ISSQN - cSitTrib** do .XML da nota fiscal de saída de itens de serviço.

Descontar dedução da base ISS

Indica se o valor de dedução será descontado da base de cálculo do ISS.

Exigibilidade ISS

Indicativo de exigibilidade de ISS. Este campo pode ser preenchido com as opções 1 - Exigível, 2 - Não incidência, 3 - Isenção, 4 - Exportação, 5 - Imunidade, 6 - Exigibilidade Suspensa por Decisão Judicial e 7 - Exigibilidade Suspensa por Processo Administrativo.

Importante

Este campo deve ser informado obrigatoriamente nas transações ao utilizar o padrão ABRASF 2.0 de NFS-e.

**Ind. Ded. Bas. Calc. ISS Arq. Fis:**   
Indicativo de como será lançado a dedução base de cálculo do ISS nos Arq. Fisc.

* Dedução de base de cálculo;
* Material fornecido por terceiros.

## Páginas relacionadas

* [F070FVE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070fve.htm)
* [regra de arredondamento da ABNT](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/regra_funcoes/arredonda-abnt.htm)
