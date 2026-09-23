# Produtos

> **Fonte:** F440GNE - Nota Fiscal de Entrada Agrupada — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f440gne.htm  
> **Trilha:** Ajuda por telas > Suprimentos > Gestão de Recebimento > Notas Fiscais de Entrada  
> **Telas citadas:** E000PCD, E075PRO, E440IPC, E440PCD, F000DLS, F000INE, F001TCP, F001TNC, F070EMP, F075PRO, F085SEL, F095CAD, F099UCP, F205DEP, F403FPR, F440DIS  
> **Identificadores de regras:** —

---
Informação dos dados referentes aos produtos da nota fiscal. Permite no máximo 990 itens.

Preço Estoque (E440IPC.PREEST)   
Tem como objetivo armazenar o preço do item conforme unidade de medida de estoque, lembrando que a unidade de medida do item no estoque pode ser diferente da unidade de medida do item na nota fiscal de entrada.

Quando a unidade de medida da nota é diferente da unidade de medida no estoque o cálculo para buscar o E440IPC.PREEST é: (E440IPC.QtdRec X E440IPC.PreUni) / E440IPC.QtdEst. O valor bruto do item da nota fiscal de entrada é calculado com base no E440IPC.PREEST.

Para o produto ser inserido na nota fiscal o campo Pode ser comprado do cadastro de produtos (E075PRO.INDCPR) deve estar igual a Sim, com exceção às notas de entrada do tipo 4 - Retorno(Industrialização), 5 - Retorno(Outros) ou 11 - Transferência entre Empresas/Filiais.

Quando o Gestão Empresarial | ERP está integrado com o WMS WIS e o depósito está configurado como Integra com WMS igual a Sim (em F205DEP - Depósitos), o sistema exige que o produto tenha código de barras configurado.

Observação

Na devolução de uma nota fiscal, quando o campo Tipo Cálculo Devolução estiver parametrizado como **P - Cálculo Proporcional** na tela Transações de Compra (F001TCP), e a Unidade de medida do fornecedor for diferente da unidade utilizada na emissão da nota, a Quantidade do fornecedor será convertida para a unidade utilizada na devolução e o Preço Unitário será ajustado conforme a conversão da unidade de medida.

Mod. ICMS

Este campo será preenchido automaticamente com a modalidade do produto obedecendo à seguinte ordem:

1. Busca a modalidade da tela F001TCP;
2. Se não estiver preenchida, sugere a modalidade da ligação entre  fornecedor e produto, da tela F403FPR, caso o campo Usa Produto X Fornecedor, da tela F075PRO, estiver preenchido com Sim;
3. Se não estiver cadastrada, busca a modalidade da tela F075PRO. Caso o parâmetro Usa Produto X Fornecedor estiver preenchido com Não;  
   Se não houver nenhuma destas 3, o campo fica em branco.

% Funrural

O percentual do Funrural é buscado do cadastro do fornecedor (F095CAD, campo % Funrural/INSS). Ele pode ser alterado se o usuário possuir permissão na tela F099UCP, campo Alterar Funrural OC/NF.

Observação

* O % Funrural já considera o valor do Gilrat em sua porcentagem
* O% Funrural não pode ser inferior ao % GILRAT
* Dentro do cálculo do IPI presumido será realizada uma verificação no Cadastro do Fornecedor (F095CAD), para analisar se o campo É Indústria está igual a "N - Não". Nesse momento, se o percentual de Funrural, informado no campo % Funrural dessa tela, for diferente do que está no Cadastro do Fornecedor, o sistema buscará a informação existente no campo % Funrural/INSS, da tela F095CAD, e modificará a informação desse campo

% GILRAT

Percentual de Gilrat que compõe a alíquota de Funrural.

% Senar

O percentual do Senar é buscado do cadastro do fornecedor F095CAD e F085SEL (guia Cadastro) , campo % SENAR/SENAR). Ele pode ser alterado se o usuário possuir permissão na tela F099UCP, campo Alterar Senar OC/NF. É possível também incluir os campos **Base Senar** e **Vlr. Senar**, pelo botão C.

Número do ato concessório de Drawback

Esse número fica associado ao documento fiscal e é apresentado em obrigações acessórias, relatórios e consultas. Pode ser alterado independentemente do tipo de mercado do fornecedor.

A tela de configuração da guia é acessada por meio do caractere C em azul no canto superior esquerdo da guia. As opções habilitadas para ela incluem alteração do tamanho das colunas e o reposicionamento do campo Complemento.

Personalizar(5)

Abre a tela de campos personalizados de usuário.

Cálculos(X)

Abre a tela de cálculos do item.

Laudo(Y)

Abre a tela de laudo técnico.

Seleção(Z)

Abre a tela de configuração de campos da guia.

Produto(K)

Abre a tela de consulta de produtos/derivações.

Estoque

Abre a tela de consulta de posição de estoques.

Lote(G)

Abre a tela de consulta de montagem do lote.

Dist. Série(H)

Abre a tela F000DLS.

Dist. Lote(J)

Abre a tela F000DLS.

Série(H)

Abre a tela de distribuição por séries.

Lote(J)

Abre a tela de distribuição por lotes.

For.X Pro.(2)

Abre a tela de pesquisa de registros da ligação Produto X Fornecedor.

Observação

As notas dos tipos 2 - Devolução (NF do Cliente), 3 - Devolução (NF de Saída), 4 - Retorno (Industrialização), 5 - Retorno (Outros) e 11 - Transferência entre Empresas/Filiais não exigem a ligação do produto com o fornecedor.  
As demais notas exigem que o campo Bloqueia Produto s/Ligação Fornecedor, da tela Cadastro de Empresas (F070EMP), esteja marcado como "S - Sim" para permitir a consistência da ligação do produto com o fornecedor, exibindo a mensagem "Fornecedor X não possui ligação com o produto X. Deseja liga-lo?". Esse campo serve para bloquear a compra de produtos que não estejam ligados ao fornecedor.

Requisição(3)

Abre a tela de pesquisa de registros das requisições ligadas a nota fiscal.

Proced.Reserva

Abre a tela de consulta de procedência da reserva.

Dispos. Fiscais 

Abre a tela F440DIS para o cadastro de dispositivo fiscal. Os botões acima referem-se ao registro posicionado na guia.

Vlr. AFRMM

Valor adicional ao frete para renovação da marinha mercante. Sempre que o campo Vlr. AFRMM da guia Dados Gerais for alterado, o valor será rateado entre os itens desta guia, sendo (qtde. recebida, o valor bruto, o valor líquido ou o peso líquido do produto).

% Diferimento

Percentual que será utilizado para o cálculo do valor do ICMS Diferido em notas fiscais de entrada. Este campo estará disponível somente quando o código da situação tributária finalizar em 51 (Diferimento). Para mais informações sobre o ICMS Diferido, consulte o processo.

Base ICMS Diferido, % ICMS Diferido e Valor ICMS Diferido

Esses campos serão calculado automaticamente quando houver percentual de diferimento informado. Estes campos são habilitados apenas quando o código da situação tributária do ICMS finalizar em 51.

Prod. Esc. Relevante

Informe se o produto é produzido em escala relevante ou não.

Os produtos produzidos em escala não relevante cuja NCM esteja relacionada no Anexo XXVII do Convênio 52/2017 devem ser preenchidas com o valor **N - Produzido em Escala Não Relevante**.

O valor do campo Prod. Esc. Relevante será sugerido conforme cadastrado a Ligação de Produto X Fabricante ou na guia Derivação da tela Cadastro de Produto. Para mais informações, consulte a documentação do Indicador de Escala Relevante.

Vlr do ICMS-ST desonerado

Valor do ICMS-ST desonerado.

Mot. deson. ICMS-ST

Motivo da desoneração do ICMS-ST.

Descrição (Mot. deson. ICMS-ST)

Descrição do motivo da desoneração do ICMS-ST.

Per. do dif. de ICMS FCP

Percentual diferido de ICMS FCP. Através desse percentual, é efetuado o cálculo dos valores de ICMS FCP diferido e ICMS FCP efetivo.

Sequencial Impressão da Nota Fiscal

Campo para identificar o sequencial de impressão do item da nota fiscal, conforme DANFE. Sendo que não existe automatismo para preenchimento do campo, exceto quando a nota fiscal for importada via tela F000INE.

Observação

* Quando preenchido, fica por conta do usuário garantir que todos os itens tiveram o sequencial preenchido (produto e serviço) e sem repetição
* Qualquer alteração nesse campo irá impactar na geração do registro C170 - Itens do documento do SPED ICMS/IPI

Complemento

Este campo recebe a descrição da tag **<prod|xProd>** do .XML, sendo que o seu conteúdo será listado no registro C170 - Itens do documento do SPED ICMS/IPI.

Compl. (ERP)

O complemento é buscado do cadastro do produto/derivação, não é editável e será formado da seguinte maneira: Descrição do Produto + Descrição Complementar do Produto + Descrição da Derivação + Descrição Complementar da Derivação.  
Com a **ordem de compra informada**, o complemento será formado: Descrição do Produto + Descrição Complementar do Produto + Descrição da Derivação + Descrição Complementar da Derivação + Complemento da Ordem de Compra.

Base Cálc. Créd

A sugestão do valor desse campo segue a seguinte ordem:

1. Se for informado um código de produto, é verificado o valor do campo Base Cálculo Crédito do cadastro do produto e atribuído no item;
2. Se no cadastro do produto o campo Base Cálculo Crédito estiver zerado, então nesse caso verifica o valor do campo Base Cálculo Crédito dos dados complementares da transação, informação parametrizada na tela F001TNC. Se o valor do campo for diferente de zero, retorna esse valor para o item. Se o valor for zero, então é retornado o valor zero;
3. Se no item não for informado um código de produto (apenas um complemento), busca por padrão o valor do campo Base Cálculo Crédito da tela F001TNC. Se o valor for zero, então é retornado o valor zero.

Sit. Trib. Ori.

Esse campo (E440PCD.StrOri) é editável. Ele será preenchido automaticamente somente quando o campo Sit. Trib. Ori. (E000PCD.StrOri) estiver informado na tela Via de Recebimento Eletrônico (F000INE).

Ind. Devolução

Campo opcional e que serve para indicar que o produto é uma dedução. Quando o item tiver esta coluna igual a "S - Sim" os impostos referentes a ele serão negativados, deduzindo do valor total da nota.

Código item cClass

 Campo com a classificação do item para NFCom e NF3e (cClass). Informação vem diretamente do cadastro (F075PRO), guia Inf. Complementares no campo Código item cClass, não sendo possível realizar a alteração através da grade.

**Observação**

Para que o item tenha o seu valor deduzido, o cClass deve ser do grupo 560 ou 590.

Código do Bem

Código do bem vinculado ao item. Campo meramente informativo, não permite edição, sendo apresentado com o valor originado do campo Código do Bem Principal informado na Solicitação de Compras.

Observação

O preenchimento deste campo ocorre ao emitir a nota fiscal vinculada à Ordem de Compra oriunda dessa Solicitação de Compras, desde que seja utilizada uma transação com o campo Aplicação Operação definido como **I - Imobilizado**.

## Páginas relacionadas

* [F205DEP - Depósitos](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f205dep.htm)
* [F001TCP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f001tcp.htm)
* [F403FPR](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f403fpr.htm)
* [F075PRO](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075pro.htm)
* [F095CAD](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f095cad.htm)
* [F099UCP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f099ucp.htm)
* [F085SEL](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f085sel.htm)
* [F000DLS](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f000dls.htm)
* [F070EMP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070emp.htm)
* [F440DIS](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f440dis.htm)
* [processo](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/impostos-icms.htm)
* [Indicador de Escala Relevante](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/manuais_processos/mercado/nf-e/regras-e-sugestoes-valores.htm#indicador_de_escala_relevante)
* [F000INE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f000ine.htm)
* [C170 - Itens do documento](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/sped/fiscal-icms-ipi/bloco-c.htm#C170)
