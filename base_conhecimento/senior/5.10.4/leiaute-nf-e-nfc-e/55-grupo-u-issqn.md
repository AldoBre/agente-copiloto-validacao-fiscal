# Grupo U - ISSQN

> **Fonte:** Leiautes NF-e e NFC-e — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/leiaute-nf-e-nfc-e.htm  
> **Trilha:** Segmentos > Compliance > Documentos Eletrônicos > NF-e | NFC-e (Nota Fiscal Eletrônica) > Nota Fiscal Eletrônica 4.0  
> **Telas citadas:** —  
> **Identificadores de regras:** VEN-140ISRET01, VEN-140NEITE01

---
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação | Origem |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 319 | U01 | ISSQN | Grupo ISSQN | CG | M01 |  | 0-1 |  | Campos para cálculo do ISSQN na NF-e conjugada, onde há a prestação de serviços sujeitos ao ISSQN e fornecimento de pelas sujeitas ao ICMS | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 320 | U02 | vBC | Valor da Base de Cálculo do ISSQN | E | U01 | N | 1-1 | 13v2 |  | Tag gerada via identificador de regra VEN-140ISRET01 através da variável VenNVlrBis. |
| 321 | U03 | vAliq | Alíquota do ISSQN | E | U01 | N | 1-1 | 3v2-4 |  | Tag gerada via identificador de regra VEN-140ISRET01 através da variável VenNPerIss. |
| 322 | U04 | vISSQN | Valor do ISSQN | E | U01 | N | 1-1 | 13v2 |  | Gera o valor, conforme consta no campo E140Isv.VlrIss. |
| 323 | U05 | cMunFG | Código do município de ocorrência do fato gerador do ISSQN | E | U01 | N | 1-1 | 7 | Informar o município de ocorrência do fato gerador do ISSQN. Utilizar a Tabela do IBGE (Seção 8.2 do MOC - Visão Geral, Tabela de UF, Município e País)  Nota 1: Não vincular com o município do fato gerador de ICMS (id:B12), ou com o município do emitente (id:C10) ou do destinatário (id:E10)  Nota 2: Pode ser informado 99999999 se a prestação de serviço for no Exterior | Tag gerada via identificador de regra VEN-140NEITE01 através da variável VSIntIssCmu. |
| 324 | U06 | cListServ | Item da Lista de Serviços | E | U01 | C | 1-1 | 5 | Informar o Item da lista de serviços em que se classifica o serviço no padrão ABRASF (Formato: NN.NN) | Gera o valor, conforme consta no campo E075Der.IteFis. |
| 324a | U07 | vDeducao | Valor da dedução para redução da Base de Cálculo | E | U01 | N | 0-1 | 13v2 |  | Caso não tenha valor de dedução, não deve ser adicionado essa tag ao XML.  Se tiver valor de dedução, a tag é gerada do identificador de regra VEN-140ISRET01 através da variável VenNVlrDed. |
| 324b | U08 | vOutro | Valor outras retenções | E | U01 | N | 0-1 | 13v2 | Valor declaratório | Gera o valor, conforme consta no campo E140Ipv.VlrOur. |
| 324c | U09 | vDescIncond | Valor desconto incondicionado | E | U01 | N | 0-1 | 13v2 |  | Gera o valor, conforme consta no campo E140Ipv.VlrDsc , VlrDs1, VlrDs2, VlrDs3, VlrDs4, VlrDs5. |
| 324d | U10 | vDescCond | Valor desconto condicionado | E | U01 | N | 0-1 | 13v2 |  | Essa tag não é gerada pelo ERP. |
| 324f | U11 | vISSRet | Valor retenção ISS | E | U01 | N | 0-1 | 13v2 | Valor declaratório | Tag gerada via identificador de regra VEN-140NEITE01 através da variável VenNVlrRet. |
| 324g | U12 | indISS | Indicador da exigibilidade do ISS | E | U01 | N | 1-1 | 2 | 1. Exigível 2. Não Incidência 3. Isenção 4. Exportação 5. Imunidade 6. Exigibilidade Suspensa por Decisão Judicial 7. Exigibilidade Suspensa por Processo Administrativo | Gera o valor, conforme consta no campo E001Tve.ExiIss. |
| 324h | U13 | cServico | Código do serviço prestado dentro do município | E | U01 | C | 0-1 | 1 - 20 |  | Gera o valor, conforme consta no campo E080Ser.CodSer. |
| 324i | U14 | cMun | Código do Município de incidência do imposto | E | U01 | N | 0-1 | 7 | Tabela do IBGE. Informar "9999999" para serviço fora do País. | Gera o valor, conforme consta no campo E085Cli.CepCli. |
| 324j | U15 | cPais | Código do País onde o serviço foi prestado | E | U01 | N | 0-1 | 4 | Tabela do BACEN. Informar somente se o município da prestação do serviço for "9999999" | Gera o valor, conforme consta no campo E085Cli.CodPai. |
| 324k | U16 | nProcesso | Número do processo judicial ou administrativo de suspensão da exigibilidade | E | U01 | C | 0-1 | 1 - 30 | Informar somente quando declarada a suspensão da exigibilidade do ISSQN | Essa tag não é gerada pelo ERP. |
| 324l | U17 | indIncentivo | Indicador de incentivo Fiscal | E | U01 | N | 1-1 | 1 | 1 = Sim; 2 = Não | Gera por padrão o indicador de incentivo com o valor igual a 2. |

## Páginas relacionadas

* [VEN-140ISRET01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_140isret01.htm)
* [VEN-140NEITE01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_140neite01.htm)
