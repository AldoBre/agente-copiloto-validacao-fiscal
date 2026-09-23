# 6. Como configurar o valor para o dispositivo fiscal previsto na Ato Diat nº 79/2022?

> **Fonte:** Configuração de Dispositivo e Benefício Fiscais — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/integracoes/nf-e/geracao-beneficio-fiscal.htm  
> **Trilha:** Segmentos > Compliance > Documentos Eletrônicos > NF-e | NFC-e (Nota Fiscal Eletrônica) > Nota Fiscal Eletrônica 4.0  
> **Telas citadas:** —  
> **Identificadores de regras:** GER-051DISPN01

---
O dispositivo fiscal deve ser gerado conforme cada código do cBenef, a qual está vinculado a uma fundamentação legal conforme a própria tabela publicada pelo estado de SC. Com isso, conforme o CST aplicado na operação com este dispositivo fiscal o valor associado a ele para ser encaminhado para o registro E115 deve ser:

* **CST 51 (Diferimento)**: Deve ser apresentado o valor do ICMS Diferido, onde o tipo de ajuste documento fiscal deve ser igual a "1 – ICMS Diferido".
* **CST 30 (Isenta ou não tributada com cobrança do ICMS por ST) e 40 (Isenta)**: Deve ser apresentado o valor do ICMS Desonerado, onde o tipo de ajuste documento fiscal deve ser igual a "J – ICMS Desonerado".
* **CST 41 (Não tributada)**: Deve ser apresentado valor zero, logo o tipo de ajuste documento fiscal deve ficar em branco.

**Observação**

Sendo necessária a sugestão automática do dispositivo fiscal parametrizado para CST 041, é possível utilizar o Parâmetro Global SugDisCst. A sugestão também pode ser feita por meio do Identificador de Regras GER-051DISPN01.

* **CST 20 (com redução base de cálculo) e 70 (Com redução de base de cálculo e cobrança do ICMS por ST)**: Deve ser apresentado o valor do ICMS Desonerado, onde o tipo de ajuste documento fiscal deve ser igual a "J – ICMS Desonerado".
* **CST 50 (suspensão)**: Deve ser apresentado o valor do ICMS Desonerado, onde o tipo de ajuste documento fiscal deve ser igual a "J – ICMS Desonerado".
