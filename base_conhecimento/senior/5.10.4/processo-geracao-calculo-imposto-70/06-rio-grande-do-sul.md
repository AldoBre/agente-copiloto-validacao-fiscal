# Rio Grande do Sul

> **Fonte:** Cálculo do imposto 70 - ICMS ST Complementar — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/processo-geracao-calculo-imposto-70.htm  
> **Trilha:** Ajuda por telas > Controladoria > Gestão de Tributos > Operações e Cálculos Fiscais > Cálculos > Apuração > F661IA5  
> **Telas citadas:** E051IMP, E660RES, E661RES, F051IMP, F669EFD  
> **Identificadores de regras:** —

---
## GIA-RS (SPED Fiscal)

**Importante**

As informações apuradas no imposto 70 possuem impacto nos registros do SPED Fiscal (F669EFD). Para mais informações, consulte o leiaute de geração da GIA-RS (SPED Fiscal) e a página Adequação aos leiautes 14 e 15 do SPED Fiscal. Lembrando que, para o estado do RS, é necessário fazer a atualização das médias antes de calcular o imposto 70.

![](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/resources/images/restituicao-e-complemento-icms-st/imposto-70-rs_thumb_0_48.png)

## Conceito

Com a publicação da apuração do ICMS ST complementar para o estado do RS, o valor apurado deve ser apresentado no registro E210 como **Outros Débitos** através do código de acerto **RS101921**, que é o resultado da apuração do imposto 70.

A orientação do Fisco é o transporte desse imposto para os registros da apuração do ICMS ST no SPED Fiscal, por isso ele estará embutido no valor do ICMS ST interno. Porém, o recolhimento do ICMS ST interno ocorre pelo código de recolhimento 0270 com data de vencimento até o dia 12 do mês subsequente, enquanto o recolhimento do valor do ICMS ST complementar ocorre através do código de recolhimento 1224 com data de vencimento até o dia 20 do mês subsequente.

Dessa forma, além da geração de títulos a pagar distintos, o registro E250 deve ser gerado com cada um dos títulos separadamente. Para isso, será utilizada a própria apuração do imposto 70 para gerar a guia de recolhimento e integrá-lo ao imposto 34 no SPED Fiscal, sem a necessidade de transportar o valor para a apuração do imposto 34, pois ele será somado no registro E210, E220 e E250 a partir do imposto 70. Além disso, no registro 1920 será feito o estorno do valor a recolher.

**Processo:**

* na tela F051IMP, cadastre no imposto 34 um vínculo com o imposto 70 (relacionado através do campo **E051IMP.ImpDie**);
  + **Saldo Credor:** a transferência acontecerá de maneira automática, restando vincular o dispositivo. O saldo credor é resultado da seguinte conta: (E661RES.TotCre - E660RES.TotDeb), desde que seja maior que **zero**;
  + **Saldo Devedor:** o saldo devedor da apuração do imposto 70 não deve ser lançado na apuração do imposto 34, pois na apuração do 70 é gerada uma guia de recolhimento;
* na apuração, os dispositivos fiscais cujos códigos de ajuste são iguais a **RS041921** (saldo devedor) ou **RS101921** (saldo credor) devem ser informados como **Dispositivo Fiscal de Saldo Credor** ou **Devedor**.
* na tela Tributos SPED Fiscal (EFD), configure o campo Gerar informações para a GIA/RS? como S-Sim e gere o arquivo. No primeiro envio das informações do ICMS ST, deve-se configurar e gerar o Bloco H, possibilitando a geração do registro H020 com os valores do ICMS ST.

## Páginas relacionadas

* [F669EFD](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f669efd.htm)
* [leiaute de geração da GIA-RS (SPED Fiscal)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/sped/fiscal-icms-ipi/gia-rs.htm)
* [Adequação aos leiautes 14 e 15 do SPED Fiscal](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/sped/fiscal-icms-ipi/adequacoes-leiautes.htm)
* [atualização das médias](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/sped/fiscal-icms-ipi/adequacoes-leiautes.htm#medias)
* [F051IMP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f051imp.htm)
* [Tributos SPED Fiscal (EFD)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f669efd.htm#menu_controladoria/f669efd.htm)
