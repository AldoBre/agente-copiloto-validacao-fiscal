# Serviços

> **Fonte:** F440GNE - Nota Fiscal de Entrada Agrupada — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f440gne.htm  
> **Trilha:** Ajuda por telas > Suprimentos > Gestão de Recebimento > Notas Fiscais de Entrada  
> **Telas citadas:** F000INE, F001TCP, F001TNC, F070EMP, F080SER, F080TXM  
> **Identificadores de regras:** —

---
Informação dos dados referentes aos serviços da nota fiscal. Permite no máximo 990 itens. Para que o campo Classificação Fiscal seja herdado do cadastro do serviço para a nota fiscal de entrada o campo Possui Serviços c/ ICMS/IPI (Indicativo se possui serviços com tributação de ICMS/IPI para entradas e saídas), da tela F070EMP, deve estar preenchido com o valor S.

% Desconto

Percentual de desconto que será aplicado sobre a nota fiscal. Permite a inserção de até cinco dígitos, de forma que, as notas ficais possam geradas com até 100,00% de desconto.

Mod. ICMS

Este campo será preenchido automaticamente com a modalidade do serviço obedecendo à seguinte ordem:

1. Busca a modalidade da tela F001TCP;
2. Se não estiver preenchida, sugere a modalidade do cadastro de serviço, da tela F080SER;

Se não houver nenhuma destas 3, o campo fica em branco.

% Diferimento

Percentual que será utilizado para o cálculo do valor do ICMS Diferido em cotações, contratos, ordens de compras, pedidos, pré-faturas e notas fiscais de entrada e saída.

Observação

* Esse campo estará disponível somente quando o código da situação tributária finalizar em 51 (Diferimento). Para mais informações sobre o ICMS Diferido, consulte o processo
* Para que o percentual de diferimento seja sugerido/preenchido para os serviços, é necessário que o parâmetro Possui serviços c/ ICMS/IPI (F070EMP) esteja preenchido com "S - Sim"

Base ICMS Diferido, % ICMS Diferido e Valor ICMS Diferido

Esses campo serão calculado automaticamente quando houver percentual de diferimento informado. Estes campos são habilitados apenas quando o código da situação tributária do ICMS finalizar em 51.

Valor Dedução Base

Define qual será o valor de dedução do ISS. Ao digitar notas fiscais de serviço (NFS-e), o valor definido nesse campo não pode ser maior que a definição do % Limite Ded. (percentual limite de dedução) da tela Ligação Tipo de Serviço x Município (F080TXM).

* caso o valor informado seja inferior ao limite do município, será mantido o valor informado pelo usuário;
* caso o valor informado seja superior ao limite do município, será substituído pelo valor do limite.

% Redução ISS

Neste campo é exibido o percentual de redução do imposto sobre serviço. Para detalhes acesse a documentação do processo Redução de ISS.

A tela de configuração da guia é acessada através do caractere C, em azul no canto superior esquerdo da própria guia. As opções habilitadas para esta guia são a alteração do tamanho das colunas e o reposicionamento do campo complemento.

Personalizar(5)

Acesso a tela de campos personalizados de usuário.

Cálculos(X)

Acesso a tela de cálculos.

Seleção(Z)

Acesso a tela de configuração de campos da guia.

Serviço(K)

Acesso a tela de pesquisa de registros do item.

Requisição(3)

Acesso a tela de pesquisa de registros das requisições ligadas a nota fiscal.

Os botões acima referem-se ao registro posicionado na guia.

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

O complemento é buscado do cadastro do serviço, não é editável e será formado da seguinte maneira: Descrição do Serviço + Descrição Complementar do Serviço.  
Com a **ordem de compra informada**, o complemento será formado: Descrição do Serviço + Descrição Complementar do Serviço + Complemento da Ordem de Compra.

Base Cálc. Créd

A sugestão do valor desse campo segue a seguinte ordem:

1. Se for informado um código de serviço, é verificado o valor do campo Base Cálculo Crédito do cadastro do serviço e atribuído no item;
2. Se no cadastro do serviço o campo Base Cálculo Crédito estiver zerado, então nesse caso verifica o valor do campo Base Cálculo Crédito dos dados complementares da transação, informação parametrizada na tela F001TNC. Se o valor do campo for diferente de zero, retorna esse valor para o item. Se o valor for zero, então é retornado o valor zero;
3. Se no item não for informado um código de serviço (apenas um complemento), busca por padrão o valor do campo Base Cálculo Crédito da tela F001TNC. Se o valor for zero, então é retornado o valor zero.

Sit. Trib. Ori.  
Este campo pode ser alterado pelo usuário e serve para armazenar a CST original do documento. A Situação Tributária do ICMS receberá a CST da operação sob o enfoque do adquirente.

Ind. Devolução  
Campo opcional e que serve para indicar que o serviço é uma dedução. Quando o item tiver esta coluna igual a "S - Sim" os impostos referentes a ele serão negativados, deduzindo do valor total da nota.

Código item cClass  
Campo com a classificação do item para NFCom e NF3e (cClass). Informação vem diretamente do cadastro (F080SER), campo Código item cClass, não sendo possível realizar a alteração através da grade.

**Observação**

Para que o item tenha o seu valor deduzido, o cClass deve ser do grupo 560 ou 590.

## Páginas relacionadas

* [F001TCP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f001tcp.htm)
* [F080SER](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f080ser.htm)
* [processo](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/impostos-icms.htm)
* [F070EMP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070emp.htm)
* [F080TXM](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f080txm.htm)
* [Redução de ISS](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/manuais_processos/suprimentos/cadastro-reducao-iss.htm)
* [F000INE](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f000ine.htm)
* [C170 - Itens do documento](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/sped/fiscal-icms-ipi/bloco-c.htm#C170)
