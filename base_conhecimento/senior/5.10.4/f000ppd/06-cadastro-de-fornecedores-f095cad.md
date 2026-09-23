# Cadastro de fornecedores (F095CAD)

> **Fonte:** F000PPD -  Configuração de parâmetros dinâmicos — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000ppd.htm  
> **Trilha:** Ajuda por telas > Cadastros  
> **Telas citadas:** F095CAD, F690ILA  
> **Identificadores de regras:** —

---
#### FORNECEDOR.CPFPRODUTORRURAL

Indicar o CPF do produtor rural a ser exportado no registros "R-2055 - Aquisição de produção rural" do REINF quando no cadastro do fornecedor o tipo do mesmo for "PJ - Pessoa jurídica" e no campo CNPJ/CPF possuir um CNPJ informado.

Valor **Padrão**: 00000000000

#### FORNECEDOR.ISENCAOPRR

Indica se há isenção da contribuição previdenciária conforme o Programa de Regularização Tributária Rural (PRR) Lei 13.606/2018. Atende a geração do registro R-2055 (Aquisição de Produção Rural) da EFD-Reinf (F690ILA).

#### FORNECEDOR.MOTIVONAORETENCAO

Indica o Motivo de Não Retenção a ser gerado no registro tipo "R" - Notas Recebidas do relatório BHISS - Belo Horizonte (CIAM006).

#### FORNECEDOR.SUSPENSAO\_IPI

Indica se é necessário comunicar o fornecedor da suspensão do IPI conforme art. 29 lei 10.637/2002 e art. 7º da IN 948/2009. Utilizado para gerar o relatório Carta de suspensão de IPI a ser encaminhada aos fornecedores (CIOD033).

| Valor | Descrição |
| --- | --- |
| 0 | Não (valor **Padrão**) |
| 1 | Sim |

#### SEGUROFURTOROUBO.ATENDIMENTOONLINE

Endereço on-line (site/e-mail), no formato texto, para atendimento do cliente.

Valor **Padrão**: www.assurantsolutions.com/brasil/br-area-do-cliente.html e clique em “chat online”.

#### SEGUROFURTOROUBO.PROCESSOSUSEPCAP

Número do processo de capitalização SUSEP, no formato texto, que permite a venda do seguro.

Valor **Padrão**:15414.900871/2013-63.

#### SEGUROFURTOROUBO.TELEFONEDEFICIENTEAUDITIVO

Número de telefone, no formato texto, para atendimento de deficiente auditivo.

Valor **Padrão**: 0800 726 6363.

#### SEGUROFURTOROUBO.TELEFONEOUVIDORIA

Número de telefone da ouvidoria da seguradora, no formato texto.

Valor **Padrão**: 0800 771 7266.

#### SEGUROFURTOROUBO.TELEFONESAC

Número de telefone para o serviço de atendimento ao cliente, no formato texto.

Valor **Padrão**: 0800 700 0530.

#### SEGUROFURTOROUBO.TELEFONESINISTRO

Número de telefone, no formato texto, para aviso de sinistro nas demais localidades.

Valor **Padrão**: 0800 700 0520.

#### SEGUROFURTOROUBO.TELEFONESINISTROCAPITAIS

Número de telefone, no formato texto, para abertura do sinistro nas capitais.

Valor **Padrão**: 3004 0520.

## Páginas relacionadas

* [F690ILA](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f690ila.htm)
* [BHISS - Belo Horizonte (CIAM006)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/relatorios/arquivos-eletronicos-municipais/ciam006.htm)
* [Carta de suspensão de IPI a ser encaminhada aos fornecedores (CIOD033)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/relatorios/declaracoes/ciod033.htm)
