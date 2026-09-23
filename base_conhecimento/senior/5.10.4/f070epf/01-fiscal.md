# Fiscal

> **Fonte:** F070EPF - Cadastro de Parâmetros Fiscais — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070epf.htm  
> **Trilha:** Ajuda por telas > Cadastros > Empresas  
> **Telas citadas:** E000INT, E070EPF, E070INT, E075DER, E075PRO, E078ULT, E080SER, F055HFI, F070EPF, F075PRO, F081GTP  
> **Identificadores de regras:** —

---
Código Fiscal Produto

Informar o código fiscal do produto. O processo do campo Código Fiscal Produto
será gerado a partir de:

1. Gera o código do produto (E075PRO.CODPRO).
   * Se a proprietária NÃO conter ERP Varejo e possuir derivação, gera o código
     do produto (E075PRO.CODPRO) mais o código de derivação (E075DER.CODDER)
     separados por hífen.
   * Se a proprietária NÃO conter ERP Varejo e NÃO possuir derivação, gera o código
     do produto (E075PRO.CODPRO).
   * Se a proprietária CONTER ERP Varejo, gera o código do produto
     (E075PRO.CODPRO) mais o código de derivação (E075DER.CODDER).
2. Gera o código de barras EAN13 (E075DER.CODBAR).
3. Gera o código de barras livre (E075DER.CODBA2).
4. Gera o código do PDV da derivação (E075DER.CODPDV) ou o código do PDV do
   produto (E075PRO.CODPDV) caso não exista na derivação.
5. Gera um código sequencial localizando a chave "Item Fiscal" na tabela
   E078ULT e atualiza a sequência nesta tabela.
6. Gera um código sequencial.
7. Gera o código do produto do operador logístico.

Descrição Fiscal Produto

Informar o descrição fiscal do produto.

Se a opção Utiliza código fiscal estiver marcada como “Sim” na tela Cadastro de Parâmetros Fiscais (F070EPF), então:

* O campo Descrição Fiscal do cadastro do produto será preenchido automaticamente com base no valor informado em Descrição código fiscal da tela Cadastro de Parâmetros Fiscais (F070EPF).

Caso essa opção esteja marcada como "Não", então:

* O campo Descrição Fiscal do cadastro do produto será composto pela junção do próximo número sequencial de código fiscal gerado pelo sistema, mais o texto informado no campo Descrição para Nota Fiscal do cadastro do produto.

O processo do campo será gerado a
partir de:

Se o campo Descrição Fiscal Produto (E070EPF.PARDPR) for:

1. Gera a descrição para nota fiscal (E075PRO.DESNFV)
2. Gera a descrição do produto (E075PRO.DESPRO)
3. Gera a descrição da derivação (E075DER.DESDER)
4. Gera a descrição do produto (E075PRO.DESPRO) mais a descrição da derivação
   (E075DER.DESDER), separados por um espaço.
5. Gera a descrição do produto (E075PRO.DESPRO) mais o complemento da descrição
   do produto (E075PRO.CPLPRO), separados por um espaço.
6. Gera a descrição da derivação (E075DER.DESDER) mais o complemento da
   descrição da derivação (E075DER.DESCPL), separados por um espaço.

Código Fiscal Serviço

Informar o código fiscal de serviço. O processo do campo será gerado a partir
de:

1. Gera o código do serviço (E080SER.CODSER)
2. Gera o código do PDV (E080SER.CODPDV)
3. Gera um código sequencial localizando a chave "Item Fiscal" na tabela
   E078ULT e atualiza a sequência nesta tabela.

Descrição Fiscal Serviço

Informe a descrição fiscal do serviço.
O processo do campo será gerado a partir de:

1. Gera a descrição do serviço (E080SER.DESSER)
2. Gera a descrição para nota fiscal (E080SER.DESNFV)
3. Gera a descrição do serviço (E080SER.DESSER) mais o complemento da descrição do serviço (E080SER.CPLSER)

Duplicar Código Fiscal

Campo Duplicar Código Fiscal (DUPFIS) estiver como
S (Sim), e for alterado para N (Não), será realizada uma consulta nas
tabelas de derivação (E075DER) e serviço (E080SER) identificando a existência de
duplicidade de códigos sobre o campo Código Fiscal do Item (ITEFIS). Caso
estes existam, serão apresentados em uma mensagem que bloqueará a alteração do
campo, e retornará seu valor para S (Sim).

Observação

Esse campo é bloqueado para edição quando houver integração com Varejo (Integração Tabelas Intermediárias [E000INT], Integração WebServices [E070INT] e Integração Varejo EM).

**Alterar Código/Descrição Fiscal**

Permite definir a alteração do código ou descrição fiscal manualmente. Por padrão, é definido como **Não**. Nesse caso, os campos Código Fiscal e Descrição Fiscal da guia Derivações da tela Cadastro de Produto (F075PRO) não serão editáveis. Ou seja, o sistema sugere e grava o código e descrição fiscal com base nas informações definidas na tela de Cadastro de Parâmetros Fiscais.

Quando estiver como **Sim**, os web servicescom.senior.g5.co.ger.cad.servico e com.senior.g5.co.ger.cad.produto importarão as informações de Item fiscal e Descrição do item fiscal através da porta Cadastrar. Os campos Código Fiscal e Descrição Fiscal permanecerão editáveis na guia Derivações da tela F075PRO e não serão alterados pelo sistema, com objetivo de manter informações inseridas de forma manual pelo usuário.

Observação

O campo é bloqueado para edição quando houver integração com Varejo (Integração Tabelas Intermediárias [E000INT], Integração web services [E070INT] e Integração Varejo EM). Após gravar o **Código Fiscal**, o campo não deve mais ser alterado quando houver integração com Varejo, independentemente do conteúdo do campo Alterar Código/Descrição Fiscal.

Utiliza Código Fiscal

Uma vez utilizado o código fiscal, todas as integrações e processos do sistema passam a utilizar essa estrutura. Alterar essa parametrização novamente pode impactar todas essas integrações e processos, podendo até paralisar a operação do sistema. Por esse motivo, o campo será bloqueado quando selecionada a opção "S – Sim".

Além disso, nesse caso, os web services com.senior.g5.co.ger.cad.servico e com.senior.g5.co.ger.cad.produto importarão as informações de Item Fiscal e Descrição do Item Fiscal por meio da porta Cadastrar. Se a empresa estiver configurada com a proprietária do ERP Varejo, os campos Duplicar Código Fiscal e Alterar Código/Descrição Fiscal serão definidos como "N – Não" e ficarão bloqueados.

Comp. alterações prod./serv. por filial

Informe a competência para controle das alterações dos produto ou serviço por filial. Este controle é exibido na tela F055HFI. Após informar a competência, é necessário reiniciar o Gestão Empresarial | ERP para que a tela F055HFI seja exibida.

Bloquear Edição Alíquota Preço por Estado

Indica se o campo ICMS Saí. Contr. da guia ICMS Estado da tela Tabela de Preço de Venda (F081GTP) é bloqueado para edição.

Tipo cálculo IRRF
/PIS/COFINS
 Forn. Exterior

Indica qual o regime a ser utilizado para fins de cálculo de IRRF, PIS e COFINS. As opções disponíveis são: 0 - Nenhum ou 2 - Caixa (cálculo destes tributos).

**Gerar participante único para SPED**

Determina o controle da forma de exportação do participante no SPED Fiscal e Contribuições.

Configurar

É utilizado para cadastro das informações no momento da implantação da rotina.

## Páginas relacionadas

* [com.senior.g5.co.ger.cad.servico](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/webservices/com_senior_g5_co_cad_servicos.htm)
* [com.senior.g5.co.ger.cad.produto](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/webservices/com_senior_g5_co_cad_produtos.htm)
* [F055HFI](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f055hfi.htm)
* [Tabela de Preço de Venda (F081GTP)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f081gtp.htm)
* [Fiscal](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/sped/fiscal-icms-ipi/bloco-0.htm#0150)
* [Contribuições](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/sped/contribuicoes-pis-cofins/bloco-0.htm#0150)
