# Cadastro de financeiras (F032FIN)

> **Fonte:** F000PPD -  Configuração de parâmetros dinâmicos — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000ppd.htm  
> **Trilha:** Ajuda por telas > Cadastros  
> **Telas citadas:** F032FIN  
> **Identificadores de regras:** —

---
#### FINANCEIRA.CARNE.URLIMPRESSAO

URL, no formato texto, para geração do arquivo PDF do boleto.

Valor **Padrão**: https://printserver.losango.com.br/printwebserverv2/impressaocarne.aspx

#### FINANCEIRA.CD.URLIMPRESSAO

URL, no formato texto, para geração do arquivo PDF do comprovante de débito.

Valor **Padrão**: https://printserver.losango.com.br/printwebserverv2/impressaocd.aspx.

#### FINANCEIRA.INDENTIFICACAO.INTEGRACAO

Define qual a financeira a integrar.

| Valor (Lista) | Descrição |
| --- | --- |
| 1 | Losango |
| 2 | Omni |

#### Financeira.ParcelaProtegia.URLImpressão

URL, no formato texto, para geração do arquivo PDF do Seguro Parcela Protegida.

Valor **Padrão**: https://printserver.losango.com.br/printwebserverV2/impressaoSeguros.aspx.

#### FINANCEIRA.SENHAINTEGRACAO

Senha,no formato texto, para autenticação na Omni. Este valor deve estar convertido em BASE64 para não ficar exposto diretamente. Utilize o site BASE64 Deconde and Encode.

#### FINANCEIRA.USUARIOINTEGRACAO

Usuário, no formato texto, para integração com a financeira.

#### POS.BANDEIRASPERMITIDAS

Indica as bandeiras dos cartões que devem ser apresentados para seleção no caixa. Os códigos da BandeiraCartao devem ser separados por ponto e vírgula. Por exemplo: 1;2.

| Valor | Descrição |
| --- | --- |
| 1 | Visa |
| 2 | Mastercard |
| 3 | American Express |
| 4 | Sorocred |
| 5 | Diners Club |
| 6 | Elo |
| 7 | Hipercard |
| 8 | Aura |
| 9 | Cabal |
| 99 | Outros |
| (vazio) | Manter campo **Valor** vazio (valor **Padrão**) |

## Páginas relacionadas

* [BASE64 Deconde and Encode](http://www.base64encode.org/)
