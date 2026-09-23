# Formato

> **Fonte:** Adequação aos leiautes do SPED Fiscal — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/sped/fiscal-icms-ipi/adequacoes-leiautes.htm  
> **Trilha:** Segmentos > Compliance > Escriturações Fiscais Digitais (SPED) > SPED Fiscal (EFD ICMS/IPI)  
> **Telas citadas:** E660RRZ, E660RSC, E660RSV  
> **Identificadores de regras:** IMP-661CALIM05

---
A partir da competência 01/2021 a apuração do imposto 70 seguirá o formato abaixo. Lembrando que não é necessário cadastrar um novo imposto:

* É preciso ter inicializado e atualizado as médias, pois a apuração vai se basear nos códigos da Tabela 5.7:
  1. Caso as médias não tenham sido atualizadas para a competência, não será apresentada nenhuma mensagem ao usuário, porém a apuração **não trará valores**. O usuário deve se certificar de que as médias estejam atualizadas **antes** de realizar a apuração.
* Leiaute da tela de apuração (F661IA5):  

  ![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/images/sped-fiscal/f661ia5_thumb_0_48.png)  

  ![](../../../resources/images/sped-fiscal/f661ia5 (2)_thumb_0_48.png)

## Guia Restituição/Complementação

* **Restituição:** lista o valor do ICMS ST Complementar (E660RSV.VlrIsc + E660RRZ.VlrIsc) mais o Valor do FCP Complementar (E660RSV.VlrFcc + E660RRZ.VlrFcc) do Controle de Entrada e Saída de Produtos quando o Código da Tabela 5.7 (E660RSV.Ctab57 ou E660RRZ.Ctab57) for igual a "UF 1 XX".;
* **Estorno Complementação:** lista o valor do ICMS ST Complementar (E660RSV.VlrIsc + E660RRZ.VlrIsc) mais o Valor do FCP Complementar (E660RSV.VlrFcc + E660RRZ.VlrFcc) do Controle de Entrada e Saída de Produtos quando o Código da Tabela 5.7 (E660RSV.Ctab57 ou E660RRZ.Ctab57) for igual a "UF 8 XX";
* **Estorno Complementação:** lista o valor do ICMS ST Complementar (E660RSV.VlrIsc + E660RRZ.VlrIsc) mais o Valor do FCP Complementar (E660RSV.VlrFcc + E660RRZ.VlrFcc) do Controle de Entrada e Saída de Produtos quando o Código da Tabela 5.7 (E660RSV.Ctab57 ou E660RRZ.Ctab57) for igual a "UF 8 XX";
* **Estorno Restituição:** lista o valor do ICMS ST Complementar (E660RSV.VlrIsc + E660RRZ.VlrIsc) mais o Valor do FCP Complementar (E660RSV.VlrFcc + E660RRZ.VlrFcc) do Controle de Entrada e Saída de Produtos quando o Código da Tabela 5.7 (E660RSV.Ctab57 ou E660RRZ.Ctab57) for igual a "UF 6 XX";
* **Complemento:** lista o valor do ICMS ST Complementar (E660RSV.VlrIsc + E660RRZ.VlrIsc) mais o Valor do FCP Complementar (E660RSV.VlrFcc + E660RRZ.VlrFcc) do Controle de Entrada e Saída de Produtos quando o Código da Tabela 5.7 (E660RSV.Ctab57 ou E660RRZ.Ctab57) for igual a "UF 3 XX";
* **Total Créditos**: lista o total das colunas Restituição + Estorno Complementação;
* **Total Débitos:** lista o total das colunas Complemento + Estorno Restituição;
* **Saldo a restituir:** lista a diferença positiva entre Total Créditos - Total Débitos.
  + Via botão **Parâmetros**, o código de ajuste do Saldo Restituir que poderá ser lançado na apuração do ICMS Próprio ou ICMS ST deve ser justificado.
* **Saldo Complementar:** lista a diferença positiva entre Total Débitos - Total Créditos.
  + Via botão **Parâmetros**, o código de ajuste do Saldo Complementar que deverá ser lançado na apuração do ICMS ST deve ser justificado.

## Guia Ressarcimento

* **Ressarcimento:** lista o valor do ICMS ST Ressarcir (E660RSV.VlrIcs) mais o Valor do FCP Ressarcir (E660RSV.VlrFcp) do Controle de Entrada e Saída de Produtos quando o Código da Tabela 5.7 (E660RSV.Ctab57 ou E660RRZ.Ctab57) for igual a "UF 2 XX";
* **Estorno Ressarcimento:** lista o valor do ICMS ST Ressarcir (E660RSV.VlrIcs) mais o Valor do FCP Ressarcir (E660RSV.VlrFcp) do Controle de Entrada e Saída de Produtos quando o Código da Tabela 5.7 (E660RSV.Ctab57 ou E660RRZ.Ctab57) for igual a "UF 7 XX";
* **Estorno Ressarcimento:** lista o valor do ICMS ST Ressarcir (E660RSV.VlrIcs) mais o Valor do FCP Ressarcir (E660RSV.VlrFcp) do Controle de Entrada e Saída de Produtos quando o Código da Tabela 5.7 (E660RSV.Ctab57 ou E660RRZ.Ctab57) for igual a "UF 7 XX";
* **Saldo:** lista a diferença entre Ressarcimento e Estorno Ressarcimento (podendo ficar negativo para atender RICMS/RS, Livro II, art. 25, IV).

Através do botão **Origens** é possível visualizar os registros das tabelas E660RSC e E660RSV para cada um dos campos:  

![](../../../resources/images/sped-fiscal/f661ia5 (3)_thumb_0_48.png)  

![](../../../resources/images/sped-fiscal/f661ia5 (4)_thumb_0_48.png)  

As colunas abaixo exibem a média do ICMS ST considerando a quantidade comercializada:  

![](../../../resources/images/sped-fiscal/f661ia5 (5)_thumb_0_48.png)

## Identificador de regra IMP-661CALIM05 utilizado na apuração

O identificador de regra IMP-661CALIM05 funcionará conforme o exemplo abaixo para a apuração do imposto 70 com data inicial igual ou superior a 01/01/2021:

```
@ Restituição/Complementação do ICMS ST @  
VCreV01 = 1000; @ Restituição @  
VCreV02 = 500;  @ Estorno Complementação @  
VTotCre = 1500; @ Total Créditos @  
VCreV04 = 0;    @ Saldo Restituir @  
EDisC04 = 1;    @ Dispositivo Fiscal Restituição @  
VDebV01 = 2000; @ Estorno Ressarcimento @  
VDebV02 = 1000; @ Complementação @  
VTotDeb = 3000; @ Total Débitos @  
VDebV04 = 0;    @ Saldo Complementar @  
EDisD04 = 2;    @ Dispositivo Fiscal Complementação @  

@ Ressarcimento do ICMS ST @  
VCreV05 = 1000; @ Ressarcimento @  
VDebV05 = 500;  @ Estorno Ressarcimento @  
VCreV06 = 0;    @ Saldo Ressarcimento @  
EDisD06 = 3;    @ Dispositivo Fiscal Ressarcimento @
```

* Apuração do imposto ICMS:
  1. Se na apuração do imposto 70 foi vinculado um dispositivo fiscal **RS021255** ao saldo a restituir, esse valor será transportado automaticamente para a apuração do ICMS no campo de **Outros Créditos** com o mesmo dispositivo ou ICMS ST (RS121255).
* Apuração do imposto ICMS ST:
  1. se na apuração do imposto 70 foi vinculado um dispositivo fiscal **RS121255** ao saldo a restituir, esse valor será transportado automaticamente para a apuração do ICMS no campo de **Restituição ICMS ST** com o mesmo dispositivo.
     Caso a apuração do imposto 70 tenha resultado em um valor a complementar, esse saldo **não** será transportado na apuração, já que foi recolhido pela outra.

**Observação**

Na apuração do imposto 70 (Ressarcimento/Restituição/Complementação do ICMS ST), o sistema considera o cálculo da restituição/complementação dos documentos fiscais utilizando **6 casas decimais**, conforme previsto no guia prático do SPED Fiscal. No final do processo, o total do imposto é arredondado para **2 casas decimais**.

## Páginas relacionadas

* [F661IA5](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f661ia5.htm)
* [IMP-661CALIM05](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/imp_661calim05.htm)
