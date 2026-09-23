# Grupo L - Detalhamento Específico de Armamentos

> **Fonte:** Leiautes NF-e e NFC-e — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/leiaute-nf-e-nfc-e.htm  
> **Trilha:** Segmentos > Compliance > Documentos Eletrônicos > NF-e | NFC-e (Nota Fiscal Eletrônica) > Nota Fiscal Eletrônica 4.0  
> **Telas citadas:** —  
> **Identificadores de regras:** —

---
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocor. | Tam. | Observação | Origem |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 158 | L01 | arma | Detalhamento de Armamento | CG | I90 |  | 1-500 |  | Informar apenas quando se tratar de armamento, permite ocorrências. | Tag de abertura do grupo. Gerado conforme o padrão do leiaute da SEFAZ. |
| 159 | L02 | tpArma | Indicador do tipo de arma de fogo | E | L01 | N | 1-1 | 1 | 0=Uso permitido; 1=Uso restrito. | Verifica se existe uma característica ligada ao produto com nome "GTU". Caso encontre, verifica se a característica é do tipo **P** ou **R**. Se **P**, envia o valor 0 e se for **R**, envia o valor 1. |
| 160 | L03 | nSerie | Número de série da arma | E | L01 | C | 1-1 | 1 - 15 |  | Gera a informação que consta no campo E140Dls.NumSep. |
| 161 | L04 | nCano | Número de série do cano | E | L01 | C | 1-1 | 1 - 15 |  | Gera o valor 0 ou 1, conforme o valor da tag tpArma. |
| 162 | L05 | descr | Descrição completa da arma, compreendendo: calibre, marca, capacidade, tipo de funcionamento, comprimento e demais elementos que permitam a sua perfeita identificação | E | L01 | C | 1-1 | 1 - 256 |  | Gera o valor, conforme o nome da característica. |
