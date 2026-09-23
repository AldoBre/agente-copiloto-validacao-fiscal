# 2. Como ocorre a sugestão do Dispositivo Fiscal?

> **Fonte:** Configuração de Dispositivo e Benefício Fiscais — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/geracao-beneficio-fiscal.htm  
> **Trilha:** Segmentos > Compliance > Documentos Eletrônicos > NF-e | NFC-e (Nota Fiscal Eletrônica) > Nota Fiscal Eletrônica 4.0  
> **Telas citadas:** E009PPE, E051DIS, E140IPV, E140ISV, E440IPC, E440PCD, E660INC, E660INV, E660IRZ, E660RSC, E660RSV, F000INE, F140DIS, F660DIS, F660NFC, F660NFV  
> **Identificadores de regras:** GER-051DISPN02

---
Após configurar o campo Código Dispositivo Fiscal em alguma das rotinas acima, a sugestão acontecerá automaticamente durante o lançamento da nota fiscal.

**Consulta do dispositivo sugerido:**

* Dispositivos fiscais do item da nota fiscal de entrada, saída e cupom fiscal (F660DIS)
* Dispositivos Fiscais do item da Nota Fiscal de Saída (F140DIS)

## 2.1 Funcionamento no módulo de Tributos

A sugestão dos Dispositivos ocorre apenas no lançamento manual de um item na nota fiscal (F660NFC e F660NFV). Os Dispositivos sugeridos tem como origem o Dispositivo Fiscal informado nos cadastros do tópico 1.

**Importante**

É possível utilizar o identificador de regra GER-051SUGDISP para incluir um comando SQL na busca dos Dispositivos Fiscais para a sugestão.

Com base nos Dispositivo Fiscais localizados, o sistema verificará qual o tipo de ajuste informado e fará a sugestão conforme as opções abaixo:

### I - ICMS ou ICMS ST

Se E051DIS.Rec197 igual a:

* "1 - ICMS" ou "2 - Outros"
  + Se percentual do ajuste (E051DIS.PERAJS) for maior que zero:
    - Base: Base do ICMS (E660IRZ/E660INC/E660INV.VLRBIC);
    - Percentual: Percentual do ajuste (E051DIS.PERAJS);
    - Valor: Base do ICMS (E660IRZ/E660INC/E660INV.VLRBIC) \* Percentual do ajuste (E051DIS.PERAJS) / 100.
  + Se percentual do ajuste (E051DIS.PERAJS) for igual a zero:
    - Base: Base do ICMS (E660IRZ/E660INC/E660INV.VLRBIC);
    - Percentual: Percentual do ICMS (E660IRZ/E660INC/E660INV.PERICM);
    - Valor: Valor do ICMS (E660IRZ/E660INC/E660INV.VLRICM).
* "3 - Ambos (preferencialmente Imposto)"
  + Percentual: Percentual do ajuste (E051DIS.PERAJS) preenchido. Do contrário E660IRZ/E660INC/E660INV.PERICM;
  + Base: Base do ICMS (E660IRZ/E660INC/E660INV.VLRBIC)
  + Valor: Se E051DIS.PERAJS maior que zero, campo recebe Base \* E051DIS.PERAJS. Senão E660IRZ/E660INC/E660INV.VLRICM;
  + Outros: 0.
* "4 - Ambos (preferencialmente Outros)"
  + Percentual: Percentual do ajuste (E051DIS.PERAJS) preenchido. Do contrário E660IRZ/E660INC/E660INV.PERICM;
  + Base: 0;
  + Valor: 0;
  + Outros: Se E051DIS.PERAJS maior que zero, campo recebe Base ICMS (E660IRZ/E660INC/E660INV.VLRBIC) \* E051DIS.PERAJS. Senão E660IRZ/E660INC/E660INV.VLRICM.

### S - ICMS ST

Se E051DIS.Rec197 igual a:

* "1 - ICMS" ou "2 - Outros"
  + Se percentual do ajuste (E051DIS.PERAJS) for maior que zero:
    - Base: Base ICMS Substituído (E660IRZ/E660INC/E660INV.VLRBSI);
    - Percentual: Percentual do ajuste (E051DIS.PERAJS);
    - Valor: Base ICMS Substituído (E660IRZ/E660INC/E660INV.VLRBSI) \* Percentual do ajuste (E051DIS.PERAJS) / 100.
  + Se percentual do ajuste (E051DIS.PERAJS) for igual a zero:
    - Base: Base ICMS Substituído (E660IRZ/E660INC/E660INV.VLRBSI);
    - Percentual: Se a Base ICMS Substituído (E660IRZ/E660INC/E660INV.VLRBSI) for maior que zero, recebe Valor ICMS Substituído (E660IRZ/E660INC/E660INV.VLRSIC) / Base ICMS Substituído (E660IRZ/E660INC/E660INV.VLRBSI) \* 100;
    - Valor: Valor ICMS Substituído (E660IRZ/E660INC/E660INV.VLRSIC).
* "3 - Ambos (preferencialmente Imposto)"
  + Percentual: E051DIS.PerAjs quando preenchido do contrário o campo é preenchido com Valor dividido por Base de Cálculo;
  + Base: Base ICMS ST (E660IRZ/E660INC/E660INV.VlrBsi);
  + Valor: ICMS ST (E660IRZ/E660INC/E660INV.VlrSic) quando E051DIS.PerAjs não estiver preenchido, do contrário faz E051DIS.PerAjs vezes Base;
  + Outros: 0.
* "4 - Ambos (preferencialmente Outros)"
  + Percentual: E051DIS.PerAjs quando preenchido do contrário o campo é preenchido com ICMS ST (E660IRZ/E660INC/E660INV.VlrSic) dividido por Base ICMS ST (E660IRZ/E660INC/E660INV.VlrBsi);
  + Base: 0;
  + Valor: 0;
  + Outros: ICMS ST (E660IRZ/E660INC/E660INV.VlrSic) quando E051DIS.PerAjs não estiver preenchido, do contrário faz E051DIS.PerAjs vezes Base ICMS ST (E660IRZ/E660INC/E660INV.VlrBsi).

### T - ICMS ST destacado

Se E051DIS.Rec197 igual a:

* "1 - ICMS" ou "2 - Outros"
  + Se percentual do ajuste (E051DIS.PERAJS) for maior que zero:
    - Base: Base do ICMS Substituído Destacado (E660INC/E660INV.VLRBSD);
    - Percentual: Percentual do ajuste (E051DIS.PERAJS);
    - Valor: Base do ICMS Substituído Destacado (E660INC/E660INV.VLRBSD) \* Percentual do ajuste (E051DIS.PERAJS) / 100.
  + Se percentual do ajuste (E051DIS.PERAJS) for igual a zero:
    - Base: Base do ICMS Substituído Destacado (E660INC/E660INV.VLRBSD);
    - Percentual: Se a Base do ICMS Substituído Destacado (E660INC/E660INV.VLRBSD) for maior que zero, recebe Valor ICMS Substituído Destacado (E660INC/E660INV.VLRISD) / Base do ICMS Substituído Destacado (E660INC/E660INV.VLRBSD) \* 100;
    - Valor: Valor ICMS Substituído Destacado (E660INC/E660INV.VLRISD).
* "3 - Ambos (preferencialmente Imposto)"
  + Percentual: E051DIS.PERAJS quando preenchido do contrário ICMS ST Destacado (E660INV/E660INC.VlrIsd) dividido por Base ICMS ST Destacado (E660INC/E660INV.VlrBsd);
  + Base: Base ICMS ST Destacado (E660INC/E660INV.VlrBsd);
  + Valor: Se E051DIS.PerAjs preenchido recebe E051DIS.PerAjs vezes Base ICMS ST Destacado (E660INC/E660INV.VlrBsd) do contrário ICMS ST Destacado (E660INV/E660INC.VlrIsd);
  + Outros: 0.
* "4 - Ambos (preferencialmente Outros)"
  + Percentual: E051DIS.PERAJS quando preenchido do contrário ICMS ST Destacado (E660INV/E660INC.VlrIsd) dividido por Base ICMS ST Destacado (E660INC/E660INV.VlrBsd);
  + Base: 0;
  + Valor: 0;
  + Outros: Se E051DIS.PerAjs preenchido recebe E051DIS.PerAjs vezes Base ICMS ST Destacado (E660INC/E660INV.VlrBsd) do contrário ICMS ST Destacado (E660INV/E660INC.VlrIsd).

### D - Diferencial de alíquota

Se E051DIS.Rec197 igual a:

* "1 - ICMS" ou "2 - Outros"
  + Base: Fixo 0;
  + Percentual: Fixo 0;
  + Valor: Valor diferencial alíquota interestadual (E660INC/E660INV.VLRDAI).
* "3 - Ambos (preferencialmente Imposto)"
  + Percentual: 0;
  + Base: Base 0;
  + Valor: E660INC/E660INV.VlrDai;
  + Outros: 0.
* "4 - Ambos (preferencialmente Outros)"
  + Percentual: 0;
  + Base: 0;
  + Valor: 0;
  + Outros: E660INC/E660INV.VlrDai.

### M - DIFAL do estado de origem

Se E051DIS.Rec197 igual a:

* "1 - ICMS" ou "2 - Outros"
  + Se percentual do ajuste (E051DIS.PERAJS) for maior que zero:
    - Base: Base do ICMS (E660INC/E660INV.VLRBIC);
    - Percentual: Percentual do ajuste (E051DIS.PERAJS);
    - Valor: Base do ICMS (E660INC/E660INV.VLRBIC) \* Percentual do ajuste (E051DIS.PERAJS) / 100.
  + Se percentual do ajuste (E051DIS.PERAJS) for igual a zero:
    - Base: Base do ICMS (E660INC/E660INV.VLRBIC);
    - Percentual: Fixo 0;
    - Valor: Valor de ICMS partilhado com o estado remetente (E660INC/E660INV.ICMVOR).
* "3 - Ambos (preferencialmente Imposto)"
  + Percentual: E051DIS.PerAjs quando preenchido do contrário 0;
  + Base: Base ICMS (E660INC/E660INV.VlrBic);
  + Valor: Se E051DIS.PerAjs maior que zero campo recebe Base vezes E051DIS.PerAjs senão E660INC/E660INV.IcmVor;
  + Outros: 0.
* "4 - Ambos (preferencialmente Outros)"
  + Percentual: E051DIS.PerAjs quando preenchido do contrário 0;
  + Base: 0;
  + Valor: 0;
  + Outros: Se E051DIS.PerAjs maior que zero campo recebe Base ICMS (E660INC/E660INV.VlrBic) vezes E051DIS.PerAjs senão campo recebe E660INC/E660INV.IcmVor.

### E - DIFAL do estado de destino

Se E051DIS.Rec197 igual a:

* "1 - ICMS" ou "2 - Outros"
  + Se percentual do ajuste (E051DIS.PERAJS) for maior que zero:
    - Base: Base ICMS partilha para estado destino (E660INC/E660INV.ICMBDE);
    - Percentual: Percentual do ajuste (E051DIS.PERAJS);
    - Valor: Base ICMS partilha para estado destino (E660INC/E660INV.ICMBDE) \* Percentual do ajuste (E051DIS.PERAJS) / 100.
  + Se percentual do ajuste (E051DIS.PERAJS) for igual a zero:
    - Base: Base ICMS partilha para estado destino (E660INC/E660INV.ICMBDE);
    - Percentual: Fixo 0;
    - Valor: Valor ICMS partilhado UF destinatário (E660INC/E660INV.ICMVDE).
* "3 - Ambos (preferencialmente Imposto)"
  + Percentual: E051DIS.PerAjs quando preenchido do contrário 0;
  + Base: Base ICMS (E660INC/E660INV.IcmBde);
  + Valor: Se E051DIS.PerAjs maior que zero campo recebe Base ICMS (E660INC/E660INV.IcmBde) vezes E051DIS.PerAjs senão DIFAL do estado destino (E660INC/E660INV.IcmVde);
  + Outros: 0.
* "4 - Ambos (preferencialmente Outros)"
  + Percentual: E051DIS.PerAjs quando preenchido do contrário 0;
  + Base: 0;
  + Valor: 0;
  + Outros: Se E051DIS.PerAjs maior que zero campo recebe Base ICMS (E660INC/E660INV.IcmBde) vezes E051DIS.PerAjs senão DIFAL do estado destino (E660INC/E660INV.IcmVde).

### F - Fundo de combate à pobreza

Se E051DIS.Rec197 igual a:

* "1 - ICMS" ou "2 - Outros"

+ Se percentual do ajuste (E051DIS.PERAJS) for maior que zero:
  - Base: Base ICMS partilha para estado destino (E660INC/E660INV.ICMBDE);
  - Percentual: Percentual do ajuste (E051DIS.PERAJS);
  - Valor: Base ICMS partilha para estado destino (E660INC/E660INV.ICMBDE) \* Percentual do ajuste (E051DIS.PERAJS) / 100.
+ Se percentual do ajuste (E051DIS.PERAJS) for igual a zero:
  - Base: Base ICMS partilha para estado destino (E660INC/E660INV.ICMBDE);
  - Percentual: Fixo 0;
  - Valor: Valor do ICMS para fundo de combate a pobreza (E660INC/E660INV.ICMVFC).

* "3 - Ambos (preferencialmente Imposto)"
  + Percentual: E051DIS.PerAjs quando preenchido do contrário 0;
  + Base: Base ICMS (E660INC/E660INV.IcmBfc);
  + Valor: Se E051DIS.PerAjs maior que zero campo recebe Base ICMS (E660INC/E660INV.IcmBde) vezes E051DIS.PerAjs senão DIFAL do estado destino (E660INC/E660INV.IcmVfc);
  + Outros: 0.
* "4 - Ambos (preferencialmente Outros)"
  + Percentual: E051DIS.PerAjs quando preenchido do contrário 0;
  + Base: 0;
  + Valor: 0;
  + Outros: Se E051DIS.PerAjs maior que zero campo recebe Base ICMS (E660INC/E660INV.IcmBde) vezes E051DIS.PerAjs senão DIFAL do estado destino (E660INC/E660INV.IcmVfc).

### B - Isentas e Outras

Se E051DIS.Rec197 igual a:

* "1 - ICMS" ou "2 - Outros"
  + Base: Valor Isento ICMS (E660IRZ/E660INC/E660INV.VLRIIC) + Valor outros ICMS (E660IRZ/E660INC/E660INV.VLROIC);
  + Percentual: Percentual do ajuste (E051DIS.PERAJS);
  + Valor: (Valor Isento ICMS (E660IRZ/E660INC/E660INV.VLRIIC) + Valor outros ICMS (E660IRZ/E660INC/E660INV.VLROIC)) \* Percentual do ajuste (E051DIS.PERAJS) / 100.
* "3 - Ambos (preferencialmente Imposto)"
  + Percentual: E051DIS.PerAjs;
  + Base: Valor Isento ICMS (E660IRZ.VLRIIC/E660INV.VLRIIC/E660INC.VLRIIC) + Valor outros ICMS (E660IRZ.VLROIC/E660INV.VLROIC/E660INC.VLROIC);
  + Valor: (Valor Isento ICMS (E660IRZ.VLRIIC/E660INV.VLRIIC/E660INC.VLRIIC) + Valor outros ICMS (E660IRZ.VLROIC/E660INV.VLROIC/E660INC.VLROIC)) \* Percentual do ajuste (E051DIS.PERAJS) / 100;
  + Outros: 0.
* "4 - Ambos (preferencialmente Outros)"
  + Percentual: E051DIS.PerAjs;
  + Base: 0;
  + Valor: 0;
  + Outros: (Valor Isento ICMS (E660IRZ.VLRIIC/E660INV.VLRIIC/E660INC.VLRIIC) + Valor outros ICMS (E660IRZ.VLROIC/E660INV.VLROIC/E660INC.VLROIC)) \* Percentual do ajuste (E051DIS.PERAJS) / 100.

### N - Isentas ICMS

Se E051DIS.Rec197 igual a:

* "1 - ICMS" ou "2 - Outros"
  + Base: Valor Isento ICMS (E660IRZ/E660INC/E660INV.VLRIIC);
  + Percentual: Percentual do ajuste (E051DIS.PERAJS);
  + Valor: Valor Isento ICMS (E660IRZ/E660INC/E660INV.VLRIIC) \* Percentual do ajuste (E051DIS.PERAJS) / 100.
* "3 - Ambos (preferencialmente Imposto)"
  + Percentual: E051DIS.PerAjs;
  + Base: Valor Isento ICMS (E660IRZ.VLRIIC/E660INV.VLRIIC/E660INC.VLRIIC);
  + Valor: Valor Isento ICMS (E660IRZ.VLRIIC/E660INV.VLRIIC/E660INC.VLRIIC) \* Percentual do ajuste (E051DIS.PERAJS) / 100;
  + Outros: 0.
* "4 - Ambos (preferencialmente Outros)"
  + Percentual: E051DIS.PerAjs;
  + Base: 0;
  + Valor: 0;
  + Outros: Valor Isento ICMS (E660IRZ.VLRIIC/E660INV.VLRIIC/E660INC.VLRIIC) \* Percentual do ajuste (E051DIS.PERAJS) / 100.

### A - Outras ICMS

Se E051DIS.Rec197 igual a:

* "1 - ICMS" ou "2 - Outros"
  + Base: Valor outros ICMS (E660IRZ/E660INC/E660INV.VLROIC);
  + Percentual: Percentual do ajuste (E051DIS.PERAJS);
  + Valor: Valor outros ICMS (E660IRZ/E660INC/E660INV.VLROIC) \* Percentual: Percentual do ajuste (E051DIS.PERAJS) / 100.
* "3 - Ambos (preferencialmente Imposto)"
  + Percentual: E051DIS.PerAjs;
  + Base: Valor Isento ICMS (E660IRZ.VLROIC/E660INV.VLROIC/E660INC.VLROIC);
  + Valor: Valor Isento ICMS (E660IRZ.VLROIC/E660INV.VLROIC/E660INC.VLROIC) \* Percentual do ajuste (E051DIS.PERAJS) / 100;
  + Outros: 0.
* "4 - Ambos (preferencialmente Outros)"
  + Percentual: E051DIS.PerAjs;
  + Base: 0;
  + Valor: 0;
  + Outros: Valor Isento ICMS (E660IRZ.VLROIC/E660INV.VLROIC/E660INC.VLROIC) \* Percentual do ajuste (E051DIS.PERAJS) / 100.

### C - Valor Líquido

Se E051DIS.Rec197 igual a:

* "1 - ICMS" ou "2 - Outros"
  + Base: Valor contábil (E660IRZ/E660INC/E660INV.VLRCTB);
  + Percentual: Percentual do ajuste (E051DIS.PERAJS);
  + Valor: Valor contábil (E660IRZ/E660INC/E660INV.VLRCTB) \* Percentual do ajuste (E051DIS.PERAJS) / 100.
* "3 - Ambos (preferencialmente Imposto)"
  + Percentual: E051DIS.PerAjs;
  + Base: Valor Contábil (E660IRZ.VlrCtb/E660INC.VlrCtb/E660INV.VlrCtb);
  + Valor: Valor Contábil (E660IRZ.VlrCtb/E660INC.VlrCtb/E660INV.VlrCtb) \* Percentual do ajuste (E051DIS.PERAJS) / 100;
  + Outros: 0.
* "4 - Ambos (preferencialmente Outros)"
  + Percentual: E051DIS.PerAjs;
  + Base: 0;
  + Valor: 0;
  + Outros: Valor Contábil (E660IRZ.VlrCtb/E660INC.VlrCtb/E660INV.VlrCtb) \* Percentual do ajuste (E051DIS.PERAJS) / 100.

### O - Outros Valores

Se E051DIS.Rec197 igual a:

* "1 - ICMS" ou "2 - Outros"
  + Base: Fixo 0;
  + Percentual: Fixo 0;
  + Valor: Fixo 0.
* "3 - Ambos (preferencialmente Imposto)"
  + Percentual: 0;
  + Base: 0;
  + Valor: 0;
  + Outros: 0.
* "4 - Ambos (preferencialmente Outros)"
  + Percentual: 0;
  + Base: 0;
  + Valor: 0;
  + Outros: 0.

### X - Valor Frete

Se E051DIS.Rec197 igual a:

* "1 - ICMS" ou "2 - Outros"
  + Base: Fixo 0;
  + Percentual: Fixo 0;
  + Valor: Valor do frete (E660INC/E660INV.VLRFRE).
* "3 - Ambos (preferencialmente Imposto)"
  + Percentual: 0;
  + Base: 0;
  + Valor: E660INC.VlrFre/E660INV.VlrFre;
  + Outros: 0.
* "4 - Ambos (preferencialmente Outros)"
  + Percentual: 0;
  + Base: 0;
  + Valor: 0;
  + Outros: E660INC.VlrFre/E660INV.VlrFre.

### Z - Valor Bruto

Se E051DIS.Rec197 igual a:

* "1 - ICMS" ou "2 - Outros"
  + Base: Valor da Mercadoria (E660INC/E660INV.VLRMRC);
  + Percentual: Percentual do Ajuste (E051DIS.PERAJS);
  + Valor: Valor da Mercadoria (E660INC/E660INV.VLRMRC) \* Percentual: Percentual do Ajuste (E051DIS.PERAJS) / 100.
* "3 - Ambos (preferencialmente Imposto)"
  + Percentual: E051DIS.PerAjs;
  + Base: Valor da Mercadoria (E660INC.VlrMrc/E660INV.VlrMrc);
  + Valor: Valor da Mercadoria (E660INC.VlrMrc/E660INV.VlrMrc) \* Percentual: Percentual do Ajuste (E051DIS.PERAJS) / 100;
  + Outros: 0.
* "4 - Ambos (preferencialmente Outros)"
  + Percentual: E051DIS.PerAjs;
  + Base: 0;
  + Valor: 0;
  + Outros: Valor da Mercadoria (E660INC.VlrMrc/E660INV.VlrMrc) \* Percentual: Percentual do Ajuste (E051DIS.PERAJS) / 100.

### R - Ressarcimento do ICMS ST

Se E051DIS.Rec197 igual a:

* "1 - ICMS" ou "2 - Outros"
  + Entrada - somente devoluções:
    - Base: Busca a soma do valor da base do ICMS substituido por unidade (E660RSC.BSIUNI) equivalente a quantidade faturada (E660RSV.QTDFAT) da nota fiscal de venda;
    - Percentual: Percentual do ajuste (E051DIS.PERAJS);
    - Valor: Busca a soma do valor ICMS substituido por unidade (E660RSC.ICSUNI) equivalente a quantidade faturada (E660RSV.QTDFAT) da nota fiscal de venda.
  + Saída:
    - Base: Busca a soma do valor da base do ICMS substituido por unidade (E660RSC.BSIUNI) equivalente a quantidade faturada (E660RSV.QTDFAT);
    - Percentual: Percentual do ajuste (E051DIS.PERAJS);
    - Valor: Busca a soma do valor ICMS substituido por unidade (E660RSC.ICSUNI) equivalente a quantidade faturada (E660RSV.QTDFAT).
* "3 - Ambos (preferencialmente Imposto)"
  + Percentual: E051DIS.PerAjs;
  + Base: Quando relativo a uma devolução busca a soma do valor da base do ICMS substituído por unidade (E660RSC.BSIUNI) equivalente a quantidade faturada (E660RSV.QTDFAT) da nota fiscal de venda ou quando relativo a uma venda busca a soma do valor da base do ICMS substituído por unidade (E660RSC.BSIUNI) equivalente a quantidade faturada (E660RSV.QTDFAT);
  + Valor: Quando relativo a uma devolução busca a soma do valor ICMS substituido por unidade (E660RSC.ICSUNI) equivalente a quantidade faturada (E660RSV.QTDFAT) da nota fiscal de venda ou quando relativo a uma venda busca a soma do valor ICMS substituido por unidade (E660RSC.ICSUNI) equivalente a quantidade faturada (E660RSV.QTDFAT);
  + Outros: 0.
* "4 - Ambos (preferencialmente Outros)"
  + Percentual: E051DIS.PerAjs;
  + Base: 0;
  + Valor: 0;
  + Outros: Quando relativo a uma devolução busca a soma do valor ICMS substituido por unidade (E660RSC.ICSUNI) equivalente a quantidade faturada (E660RSV.QTDFAT) da nota fiscal de venda ou quando relativo a uma venda busca a soma do valor ICMS substituido por unidade (E660RSC.ICSUNI) equivalente a quantidade faturada (E660RSV.QTDFAT).

### G - Ressarcimento do crédito de ICMS

Se E051DIS.Rec197 igual a:

* "1 - ICMS" ou "2 - Outros"
  + Entrada - somente devoluções:
    - Base: Busca a soma do valor da base do ICMS substituído por unidade (E660RSC.BSIUNI) equivalente a quantidade faturada (E660RSV.QTDFAT) da nota fiscal de venda;
    - Percentual: Percentual do ajuste (E051DIS.PERAJS);
    - Valor: Busca a soma do valor ICMS substituído por unidade (E660RSC.ICSUNI) equivalente a quantidade faturada (E660RSV.QTDFAT) da nota fiscal de venda.
  + Saída:
    - Base: Busca a soma da base do ICMS (E660RSC.VLRBIC) equivalente a quantidade faturada (E660RSV.QTDFAT);
    - Percentual: Percentual do ajuste (E051DIS.PERAJS);
    - Valor: Busca a soma do valor ICMS (E660RSC.VLRICM) equivalente a quantidade faturada (E660RSV.QTDFAT).
* "3 - Ambos (preferencialmente Imposto)"
  + Percentual: E051DIS.PerAjs;
  + Base: Busca a soma do valor da base do ICMS substituído por unidade (E660RSC.BSIUNI) equivalente a quantidade faturada (E660RSV.QTDFAT) da nota fiscal de venda;
  + Valor: Quando relativo a uma devolução busca a soma do valor ICMS substituido por unidade (E660RSC.ICSUNI) equivalente a quantidade faturada (E660RSV.QTDFAT) da nota fiscal de venda já quando relativo a uma venda busca a soma do valor ICMS substituído por unidade (E660RSC.ICSUNI) equivalente a quantidade faturada (E660RSV.QTDFAT) da nota fiscal de venda;
  + Outros: 0.
* "4 - Ambos (preferencialmente Outros)"
  + Percentual: E051DIS.PerAjs;
  + Base: 0;
  + Valor: 0;
  + Outros: Quando relativo a uma devolução busca a soma do valor ICMS substituido por unidade (E660RSC.ICSUNI) equivalente a quantidade faturada (E660RSV.QTDFAT) da nota fiscal de venda já quando relativo a uma venda busca a soma do valor ICMS substituído por unidade (E660RSC.ICSUNI) equivalente a quantidade faturada (E660RSV.QTDFAT) da nota fiscal de venda.

### V - Valor da antecipação do ICMS

Se E051DIS.Rec197 igual a:

* "1 - ICMS" ou "2 - Outros"
  + Base: Valor contábil (E660INC/E660INV.VLRCTB);
  + Percentual: Percentual do Ajuste (E051DIS.PERAJS);
  + Valor: Valor contábil (E660INC/E660INV.VLRCTB) \* Percentual do Ajuste (E051DIS.PERAJS) / 100 - Valor do ICMS (E660INC/E660INV.VLRICM).
* "3 - Ambos (preferencialmente Imposto)"
  + Percentual: E051DIS.PerAjs;
  + Base: Valor contábil (E660INC.VLRCTB/E660INV.VlrCtb);
  + Valor: Valor contábil (E660INC.VLRCTB/E660INV.VlrCtb) \* Percentual do Ajuste (E051DIS.PERAJS) / 100 - Valor do ICMS (E660INC.VLRICM/E660INV.VlrIcm);
  + Outros.
* "4 - Ambos (preferencialmente Outros)"
  + Percentual: E051DIS.PerAjs;
  + Base:
  + Valor:
  + Outros: Valor contábil (E660INC.VLRCTB/E660INV.VlrCtb) \* Percentual do Ajuste (E051DIS.PERAJS) / 100 - Valor do ICMS (E660INC.VLRICM/E660INV.VlrIcm)

### P - Valor original de PIS anterior à decisão judicial - Identificador de Regra GER-051DISPCSU

Se E051DIS.Rec197 igual a:

* "1 - ICMS" ou "2 - Outros"
  + Base: Variável GERNBASAJS do identificador de regras;
  + Percentual: Variável GERNPERAJS do identificador de regras;
  + Valor: Variável GERNVLRAJS do identificador de regras.
* "3 - Ambos (preferencialmente Imposto)"
  + Percentual: GERNPERAJS;
  + Base: GERNBASAJS;
  + Valor: GERNVLRAJS;
  + Outros: 0.
* "4 - Ambos (preferencialmente Outros)"
  + Percentual: GERNPERAJS;
  + Base: 0;
  + Valor: 0;
  + Outros: GERNVLROUT.

### H - Valor original de COFINS anterior à decisão judicial - Identificador de Regra GER-051DISPCSU

Se E051DIS.Rec197 igual a:

* "1 - ICMS" ou "2 - Outros"
  + Base: Variável GERNBASAJS do identificador de regras;
  + Percentual: Variável GERNPERAJS do identificador de regras;
  + Valor: Variável GERNVLRAJS do identificador de regras.
* "3 - Ambos (preferencialmente Imposto)"
  + Percentual: GERNPERAJS;
  + Base: GERNBASAJS;
  + Valor: GERNVLRAJS;
  + Outros: 0.
* "4 - Ambos (preferencialmente Outros)"
  + Percentual: GERNPERAJS;
  + Base: 0;
  + Valor: 0;
  + Outros: GERNVLROUT.

### J - ICMS Desonerado

Se E051DIS.Rec197 igual a:

* "1 - ICMS" ou "2 - Outros"
  + Base: Fixo 0;
  + Percentual: Fixo 0;
  + Entrada: Valor: Valor do ICMS substituído destacado (E660INC.VLRICD). Saída: Valor: ICMS Desonerado (E660INV.VLRICD).
* "3 - Ambos (preferencialmente Imposto)"
  + Percentual: 0;
  + Base: 0;
  + Valor: Valor do ICMS substituído destacado (E660INC.VLRICD/E660INV.VlrIcd);
  + Outros.
* "4 - Ambos (preferencialmente Outros)"
  + Percentual:0
  + Base:0
  + Valor:0
  + Outros:Valor do ICMS substituído destacado (E660INC.VLRICD/E660INV.VlrIcd).

### K - Valor do FCP Retido Ant. por Subst. Trib.

Se E051DIS.Rec197 igual a:

* "1 - ICMS" ou "2 - Outros" ou "3 - Ambos (preferencialmente Imposto)"
  + Percentual: E660INC/E660INV.AreFcp;
  + Base: Base ICMS (E660INC/E660INV.BreFcp);
  + Valor: E660INC/E660INV.VreFcp;
  + Outros: 0.
* "4 - Ambos (preferencialmente Outros)"
  + Percentual: E660INC/E660INV.AreFcp;
  + Base: 0;
  + Valor: 0;
  + Outros: E660INC/E660INV.VreFcp.

### L - Valor do FCP Retido por Substituição Tributária

Se E051DIS.Rec197 igual a:

* "1 - ICMS" ou "2 - Outros" ou "3 - Ambos (preferencialmente Imposto)"
  + Percentual: E660INC/E660INV.AstFcp;
  + Base: Base ICMS (E660INC/E660INV.BstFcp);
  + Valor: E660INC/E660INV.VstFcp;
  + Outros: 0.

* "4 - Ambos (preferencialmente Outros)"
  + Percentual: E660INC/E660INV.AstFcp;
  + Base: 0;
  + Valor: 0;
  + Outros: E660INC/E660INV.VstFcp.

### Q - Valor Retenção ICMS Substituto

Se E051DIS.Rec197 igual a:

* "1 - ICMS" ou "2 - Outros" ou "3 - Ambos (preferencialmente Imposto)"
  + Percentual: 0;
  + Base: Base ICMS 0;
  + Valor: E660INC/E660INV.VlrRis;
  + Outros: 0.

* "4 - Ambos (preferencialmente Outros)"
  + Percentual: 0;
  + Base: 0;
  + Valor: 0;
  + Outros: E660INC/E660INV.VlrRis.

### Y - Via regra

Independente de onde o valor do ajuste deve ser lançado, essa possibilidade permite lançar via regra, valores para as colunas a partir do identificador de regra: GER-051DISPN02.

### W - Memória de Cálculo do Diferencial de Alíquota

* Convênio 52/91 - Disponível apenas para a gestão de suprimentos e sempre que Base do ICMS for diferente da Base do diferencial de alíquotas:
  + Base: Base do diferencial de alíquotas calculado na nota fiscal;
  + Imposto: E440IPC.VlrDfa;
  + Percentual: E440IPC.PerIcm;
  + Outros: E440IPC.VlrIcm / (E440IPC.VlrIic + E440IPC.VlrOic) \* 100.
* Demais casos
  + Base: E660INC.VlrIic + E660INC.VlrOic;
  + Imposto: E660INC.VlrDai;
  + Outros: E009PPE.IcmInd (com base no estado da filial);
  + Percentual: Outros - (Imposto / Base).

Observação

Para que o sistema preencha a coluna Outros com uma alíquota, é necessário que em Tabelas - Impostos - Dispositivos Fiscais (E051DIS), o campo Local onde o valor do ajuste será lançado no documento fiscal (Imposto / Outros) esteja preenchido igual a "3 - Ambos (preferencialmente Imposto)".

### U - Total do imposto antecipado, pelo controle de entradas e saídas

* Base: E660RSC.VlrBsi;
* Imposto: E660RSC.VlrIcm + E660RSC.VlrIcs;
* Outros: E660RSC.PerMva;
* Percentual: E660RSC.PerIcs.

Observações

* Para que o sistema preencha a coluna Outros com uma alíquota, é necessário que em Tabelas - Impostos - Dispositivos Fiscais (E051DIS), o campo Local onde o valor do ajuste será lançado no documento fiscal (Imposto / Outros) esteja preenchido igual a "3 - Ambos (preferencialmente Imposto)".
* Para utilizar esse tipo de ajuste fiscal, é necessário configurar a empresa para trabalhar com o Processo para Controle de Entrada e Saída de Produtos (PEPS/FIFO).

### 1 - ICMS Diferido

Para notas fiscais de saída:

* Base: E140IPV.BasIdf / E140ISV.BasIdf
* Imposto: E140IPV.VlrIdf / E140ISV.VlrIdf
* Outros: 0;
* Percentual: 0.

Para notas fiscais de entrada:

* Base: E440Ipc.BasIdf / E440Isc.BasIdf
* Imposto: E440Ipc.VlrIdf / E440Isc.VlrIdf
* Outros: 0;
* Percentual: 0.

**Nota**

Mais informações sobre o ICMS diferido podem ser encontradas em Rotinas de ICMS.

### 2 - ICMS Monofásico cobrado anteriormente

A partir deste tipo é possível informar em conta gráfica este crédito na apuração do ICMS Monofásico cobrado anteriormente.

* Base: Base do ICMS (E440PCD.QtmBid);
* Percentual: Percentual do ajuste (E440PCD.AliImd);
* Valor: Base do ICMS (E440PCD.VmoIcd).

### 4 - Redução linear de incentivos e benefícios - LC nº 224/2025

Esta opção visa permitir os ajustes automáticos referente à NT 012/2026. Para esta opção será sugerido no ajuste os campos conforme abaixo:

* Base: Base de Cálculo da Cofins (VlrBcf / VlrBsc / VlrBcr / BcoImp)
* Imposto: Fixo 0
* Outros: Fixo 0
* Percentual: E051DIS.PerAjs
  Comment

## 2.2 Sugestão dos valores do ICMS Simples Nacional

**Módulo Suprimentos:**

* No campo Cód. Dis. Fis da tela F000INE, guia Itens, quando o **Tipo de Ajuste** do Dispositivo cadastrado estiver configurado como **I - ICMS**, e a nota fiscal tiver os valores de **Base**, **Valor** e **Percentual** de ICMS do Simples Nacional, o sistema irá sugerir o valor no Dispositivo.

**Módulo Tributos:**

* Quando o Dispositivo for parametrizado para o ICMS e o fornecedor for do Simples Nacional, será apresentado automaticamente na sugestão do Dispositivo o valor do ICMS Simples Nacional.

## Páginas relacionadas

* [Dispositivos fiscais do item da nota fiscal de entrada, saída e cupom fiscal (F660DIS)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f660dis.htm)
* [Dispositivos Fiscais do item da Nota Fiscal de Saída (F140DIS)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f140dis.htm)
* [GER-051SUGDISP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ger_051sugdisp.htm)
* [GER-051DISPN02](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ger_051dispn02.htm)
* [Processo para Controle de Entrada e Saída de Produtos (PEPS/FIFO)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/processo-controle-entrada-saida-produto.htm)
* [Rotinas de ICMS](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/impostos-icms.htm)
* [NT 012/2026](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f661i12.htm#NT012/2026)
