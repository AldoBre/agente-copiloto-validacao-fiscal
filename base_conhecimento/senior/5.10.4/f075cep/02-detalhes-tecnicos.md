# Detalhes técnicos

> **Fonte:** F075CEP - Controle de Entrada de Produtos — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075cep.htm  
> **Trilha:** Ajuda por telas > Cadastros > Produtos e Serviços > Produtos  
> **Telas citadas:** E660NFV, E660RRZ, E660RSC, E660RSM, E660RSV  
> **Identificadores de regras:** —

---
Gravação das médias do dia:

* **Entradas e devoluções de venda:** recupera todos os registros na tabela E660RSC que atendem os parâmetros da classe;
* **Saídas:** recupera todos os registros na tabela E660RSV/E660RRZ que atendem os parâmetros da classe, excluindo as notas de devolução (E660NFV.TipNfe = 2);
* **Devolução de compra:** recupera os itens de saída do Controle (E660RSV) das notas fiscais de saída em devolução (E660NFV.TipNfe = 2) ligando com a entrada que está sendo devolvida no Controle (E660RSC). Sempre que houver ligação com essa origem de dados, o campo irá apresentar "¹" desse ponto em diante. O valor das entradas será negativo e reduzido do saldo do dia anterior para que a média seja recalculada;
* **Médias do período anterior:** recupera o registro na tabela E660RSM ligando o item que está sendo processado e retornando o registro com data anterior (DatMed) ao que está sendo processado.

Os valores são gravados, conforme abaixo:

| Campo | Valor |
| --- | --- |
| QtdEnt | Soma do campo E660RSC.QtdEnt - Soma do campo E660RSV.QtdSai¹ quando TipNfs = 2 |
| VlrBic | Soma do campo E660RSC.VlrBic - Soma (E660RSC.VlrBic¹ / E660RSC.QtdEnt¹) \* E660RSV.QtdSai¹) |
| VlrIcm | Soma do campo E660RSC.VlrIcm - Soma (E660RSC.VlrIcm¹ / E660RSC.QtdEnt¹) \* E660RSV.QtdSai¹) |
| VlrBsi | Soma do campo E660RSC.VlrBsi - Soma (E660RSC.VlrBsi¹ / E660RSC.QtdEnt¹) \* E660RSV.QtdSai¹) |
| VlrIcs | Soma do campo E660RSC.VlrIcs - Soma (E660RSC.VlrIcs¹ / E660RSC.QtdEnt¹) \* E660RSV.QtdSai¹) |
| BasFcp | Soma do campo E660RSC.BasFcp - Soma (E660RSC.BasFcp¹ / E660RSC.QtdEnt¹) \* E660RSV.QtdSai¹) |
| VlrFcp | Soma do campo E660RSC.VlrFcp - Soma (E660RSC.VlrFcp¹ / E660RSC.QtdEnt¹) \* E660RSV.QtdSai¹) |
| QtdSai | Soma do campo E660RSV.QtdFat + E660RRZ.QtdFat |
| QtdSal | MEDIAANT.QtdSal + QtdEnt - QtdSai |
| BicMed | ((MEDIAANT.BicMed \* MEDIAANT.QtdSal) + VlrBic) / (MEDIAANT.QtdSal + QtdEnt) |
| IcmMed | ((MEDIAANT.IcmMed \* MEDIAANT.QtdSal) + VlrIcm) / (MEDIAANT.QtdSal + QtdEnt) |
| BsiMed | ((MEDIAANT.BsiMed \* MEDIAANT.QtdSal) + VlrBsi) / (MEDIAANT.QtdSal + QtdEnt) |
| IcsMed | ((MEDIAANT.IcsMed \* MEDIAANT.QtdSal) + VlrIcs) / (MEDIAANT.QtdSal + QtdEnt) |
| BfcMed | ((MEDIAANT.BfcMed \* MEDIAANT.QtdSal) + BasFcp) / (MEDIAANT.QtdSal + QtdEnt) |
| FcpMed | ((MEDIAANT.FcpMed \* MEDIAANT.QtdSal) + VlrFcp) / (MEDIAANT.QtdSal + QtdEnt) |
