# Grupo K - Detalhamento Específico de Medicamento e de matérias-primas farmacêuticas

> **Fonte:** Leiautes NF-e e NFC-e — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/leiaute-nf-e-nfc-e.htm  
> **Trilha:** Segmentos > Compliance > Documentos Eletrônicos > NF-e | NFC-e (Nota Fiscal Eletrônica) > Nota Fiscal Eletrônica 4.0  
> **Telas citadas:** —  
> **Identificadores de regras:** VEN-140NEMED02

---
Observação

A impressão desse grupo (Grupo K) pode ser evitada por meio do uso do identificador de regras VEN-140NEMED02. Para maiores informações consultar a documentação do IR: Identificador de Regra VEN-140NEMED02

| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação | Origem |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 152 | K01 | med | Detalhamento de Medicamentos e de matérias-primas farmacêuticas | CG | I90 |  | 0-1 |  | Informar apenas quando se tratar de medicamentos ou de matérias-primas farmacêuticas, permite ocorrências. | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 152a | K01a | cProdANVISA | Código de Produto da ANVISA | E | K01 | C | 1-1 | 6,11,13 | Utilizar o número do registro ANVISA ou preencher com o literal "ISENTO", no caso de medicamento isento de registro na ANVISA. (Incluído na NT2016.002. Atualizado na NT 2021.004) | Gera por padrão o valor do campo E075Der.RegAnv. Se necessário a alteração dessa informação, utilize a variável VSIntRegAnv do identificador de regra VEN-140NEMED02. |
| 152b | K01b | xMotivoIsencao | Motivo da isenção da ANVISA | E | K01 | C | 0-1 | 1-255 | Obs.: Para medicamento isento de registro na ANVISA, informar o número da decisão que o isenta, como por exemplo o número da Resolução da Diretoria Colegiada da ANVISA (RCD). (Criado na NT 2018.005) | Gera o valor de acordo com o campo E075Der.MotAnv. |
| 157 | K06 | vPMC | Preço máximo consumidor | E | K01 | N | 1-1 | 13v2 |  | Verifica se o produto se encontra em uma tabela de preço. Caso encontre, envia para tag o preço base da tabela. Caso contrário, envia o valor 0. |

## Páginas relacionadas

* [Identificador de Regra VEN-140NEMED02](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ven_140nemed02.htm)
