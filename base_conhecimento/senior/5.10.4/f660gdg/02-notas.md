# Notas

> **Fonte:** F660GDG - Geração de detalhes das Notas Fiscais — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/f660gdg.htm  
> **Trilha:** Ajuda por telas > Controladoria > Gestão de Tributos > Escrituração > Lançamentos  
> **Telas citadas:** E001TNC, E001TNS, E008CEP, E070FIL, E085CLI, E095FOR, E440IPC, E440ISC, E660INC, E660INV, E660NFC, E660NFV, F001TCP, F001TVE, F660NFC, F660NFV  
> **Identificadores de regras:** —

---
Atualizar NF de Entrada

Assinalar esta opção para a geração no botão
Detalhes.

Atualizar NF de Saída

Assinalar esta opção para a geração no botão
Detalhes.

Ligação entre Notas Fiscais

Assinalar esta opção para a geração no botão
Detalhes.

Parcelas das Nota Fiscal

Assinalar esta opção para a geração no botão Detalhes.

Entrada, Vcto., Lote e Série

Assinalar esta opção para a geração no botão
Detalhes.

Nota Fiscal de Devolução

Assinalar esta opção para a geração no botão
Detalhes.

Notas Fiscais Complementares/Acerto

Assinalar esta opção para a geração no botão
Detalhes.

Peso Líquido/Peso bruto

Assinalar esta opção para a geração no botão Detalhes.

Preço unitário do Item

Assinalar esta opção para gerar o valor do preço unitário do item das notas fiscais de entrada e saída que
já estão integradas para a Gestão de Tributos.

Valor da Mercadoria

É imprescindível que os usuários da
Gestão de Tributos executem o processo de "Valor de Mercadoria" para
notas fiscais de entrada e notas fiscais de saída, ele irá gerar o valor
da mercadoria do item das notas fiscais de entrada e saída que já estão
integradas para a Gestão de Tributos. Este valor é gerado com base na
multiplicação da "Quantidade" (E660INC/E660INV.QTDENT) pelo "Preço
Unitário" (E660INC/E660INV.PREUNI). Caso este processo não seja
realizado, as obrigações acessórias ficaram **inválidas.**

Isso é necessário devido à remoção da chave "660VMITE01" do atualizador,
esta chave realizava a inicialização do campo Valor da Mercadoria (VlrMrc)
dos "Itens de Notas Fiscais de Venda" (E660INV) e "Itens de Notas
Fiscais de Compra" (E660INC), o mesmo tratamento ocorrerá ao executar
este processo.

Inicializar valores de ICMS e IPI efetivamente creditados

Tem a finalidade de inicializar os valores dos campos de ICMS e IPI efetivamente
creditados nas tabelas "E440ISC e E440IPC". Este preenchimento se dará com base
nos valores de ICMS e IPI presentes no próprio item da nota fiscal, se a nota
fiscal configurar recuperação destes impostos.

Base de Cálculo do Crédito

Tem a finalidade de inicializar o campo BASCRE das tabelas "E440IPC, E440ISC e
E660INC", buscando o mesmo campo da tabela "E001TNC", este tratamento é aplicado
apenas às notas fiscais de entrada e respeita os filtros de empresa e filial
logada e o período informado na tela.

Iniciar Valores de IPI e ICMS Creditados Efetivamente em Suprimentos

Essa opção inicializará o IPI Efetivamente Creditado das notas copiando os dados de IPI normal para o IPI Efetivamente Creditado (caso IPI Efetivamente Creditado tenha valor '0' (zero); caso já possua valor, nada será copiado. Não são feitos cálculos ou recálculos, apenas copiando os dados de um para o outro).

Carregar o Valor de Importação

Tem a finalidade de alterar os campos Valor Importado e Coeficiente
FCI de notas fiscais de entrada da gestão de Suprimentos em que o
fornecedor seja do exterior (Tipo mercado igual a E), conforme:

1. Quando a origem da mercadoria (E440IPC.ORIMER) for igual a 1, o valor
   de importação (E440IPC.VLRIMP) será preenchido pelo valor bruto do item
   mais o valor do frete importação   
    mais o valor do seguro importação (E440IPC.VLRBRU + E440IPC.VLRFEI +
   E440IPC.VLRSEI) e o Coeficiente do FCI será 100%.
2. Quando a origem da mercadoria (E440IPC.ORIMER) for igual a 2, 3, 5 e
   8, o valor de importação (E440IPC.VLRIMP) será preenchido pelo valor
   bruto do item menos o valor do ICMS   
    (E440IPC.VLRBRU – E440IPC.VLRICM).

2.1 Para a origem da mercadoria com o código 2 ou 8 será gerado o
Coeficiente do FCI com 100%.

2.2 Para a origem da mercadoria com o código 3 será gerado o
Coeficiente do FCI com 50%.

2.3 Para a origem da mercadoria com o código 5 será gerado o
Coeficiente do FCI com 0%.

Número do Contador de Ordem de Operação nos
Totalizadores - COO Redução Z

Tem a finalidade de inicializar o campo Número do Contador de Ordem de
Operação do Último Documento Emitido no Dia (COO da Redução Z) em todos
os totalizadores do período informado, gravando neste o número do último
cupom fiscal lançado para em cada data e equipamento fiscal.

Integração do Rateio com projeto da NF Entrada

Integra o valor do rateio com a nota fiscal de entrada que possui projeto informado.

Integração do Rateio com projeto da NF Saída

Integra o valor do rateio com a nota fiscal de saída que possui projeto informado.

Atualizar CFPS

Esta opção deve ser utilizada por usuários do Distrito Federal que atualizarem para esta versão e que possuem notas fiscais do módulo de Tributos que ainda não foram processadas no LFPD. Ela atualiza os documentos lançados na mesma empresa e filial, fornecidos como parâmetros para a tela e a data de emissão esteja compreendida no intervalo fornecido pelo usuário. A atualização ocorre da seguinte forma:

As notas fiscais de entrada que tenham transação configurada como serviço são atualizadas. O campo "E660NFC.NopOpe" (Natureza da Operação da tela F660NFC) é regravado com o campo E001TNS.COMNAT (Nova Natureza Operação - CFOP da tela F001TCP), e o campo E001TNS.COMNOP (Natureza de Operação - CFOP para Natureza de Operação - CFOP/CFPS da tela F001TCP) é regravado conforme abaixo:

| Valor a ser gravado | Regra de quando aplicar |
| --- | --- |
| 9104 | Fornecedor da nota é do exterior (E095FOR.SIGUFS = “EX”) |
| 8006 | Fornecedor da nota é do mercado interno (E095FOR.SigUfs <> “EX”) |

As notas fiscais de saída que tenham transação configurada como serviço são atualizadas. O campo "E660NFV.NopOpe" (Natureza da Operação da tela F660NFV) é regravado com o campo E001TNS.COMNAT (Nova Natureza Operação - CFOP da tela F001TVE), e o campo E001TNS.COMNOP (Natureza de Operação - CFOP para Natureza de Operação - CFOP/CFPS da tela F001TVE) é regravado:

| Valor a ser gravado | Regra de quando aplicar |
| --- | --- |
| 9101 | Prestação de serviço no mesmo município (E008CEP.CodIbg da filial igual ao da nota, isto é, igual ao E660NFV.CODRAI. Se E660NFV.CodRai for zero, buscar CODIBG do CEP do cliente (E085CLI.CEPINI) para comparação com o da filial) |
| 9102 | Prestação de serviço fora do município mas no mesmo estado da filial (E070FIL.SIGUFS = E085CLI.SIGUFS e E008CEP.CodIbd da filial diferente da nota) |
| 9404 | Prestação de serviço no exterior (E085CLI.SIGUFS = “EX”) |
| 9103 | Prestação de serviço em outro estado (E070FIL.SIGUFS <> E085CLI.SIGUFS) mas no Brasil |
| 0000 | Nota não se encaixar em nenhuma das anteriores |

Inicializar o campo ICMS Cobrado Importação nas notas fiscais de entrada e devolução de importação

O sistema inicializa os campos de ICMS Cobrado na Importação das notas fiscais de Entrada ou Devolução, conforme lançado na Gestão de Suprimentos/Mercado.

Inicializar o campo ICMS Diferido nas notas fiscais de entrada

O sistema inicializa os campos de ICMS Diferido nas notas fiscais de Entrada, conforme lançado na Gestão de Suprimentos.
