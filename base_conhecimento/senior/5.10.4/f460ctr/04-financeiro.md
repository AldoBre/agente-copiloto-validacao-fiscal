# Financeiro

> **Fonte:** F460CTR - Contrato de Compra (Comercial/Financeiro/Eventos) — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f460ctr.htm  
> **Trilha:** Ajuda por telas > Suprimentos > Gestão de Compras > Contratos  
> **Telas citadas:** E001TNS, E002TPT, E020SNF, F000PGS, F460EVE  
> **Identificadores de regras:** —

---
Dia Fixo

Campo que define um dia específico do mês para vencimento das parcelas geradas a partir do contrato. Exemplo: se configurado como "30", o sistema tentará gerar vencimentos no dia 30 de cada mês.

**Comportamento em meses com menos dias:** Quando o dia fixo configurado não existe no mês (como o dia 30 ou 31 em fevereiro), o sistema posterga o vencimento para o primeiro dia do mês seguinte, independentemente da configuração de critério de vencimento do cliente (dias corridos, dias úteis, antecipação, etc.).

**Critério de Vencimento do Cliente:** Configuração global que define como o sistema deve tratar datas de vencimento em situações especiais (antecipação em dias corridos, ajuste para dias úteis, etc.). Este critério é consultado para a maioria dos cenários de cálculo, com exceção do caso descrito acima.

## Exemplo:

| Configuração | Valor |
| --- | --- |
| Dia Fixo de Vencimento no Contrato | 30 |
| Data de Emissão da Nota | 01/02/2026 |
| Critério de Vencimento do Cliente | Dias Corridos (Antecipa) |
| Mês | Fevereiro (28 dias) |

**Resultado esperado:**

* O sistema identifica que o dia 30 não existe em fevereiro
* O vencimento é postergado para 01/03/2026 (primeiro dia do mês seguinte)
* O critério de antecipação do cliente não é aplicado neste caso

Contratos dos tipo 3 - Financeiro Normal e 4 - Financeiro Adicional

Para contratos dos tipos **3 - Financeiro/Arrendamento Mercantil** e **4 - Financeiro Adicional** é possível gerar títulos no Contas a Pagar para mais de um fornecedor. Para isso, defina um rateio por fornecedor na aba Fornecedor, sendo que os títulos serão gerados com base nos fornecedores informados e no seu respectivo percentual sobre o valor base da parcela.

Valor Total

Valor total do contrato.

Tipo do Título

Tipo do título. Registros gravados na tabela E002TPT e cadastrados em Tabelas > Financeiro > Tipos de Títulos.

Número do Título

Número do título.

Origem Parcelas

Série origem das parcelas. Registros gravados na tabela E020SNF e cadastrados em Tabelas > Comercial > Fiscais > Séries Notas Fiscais.

Transação Titulo

Transação dos títulos a serem gerados pelo contrato. Registros gravados na tabela E001TNS e cadastrados em Tabelas > Transações > Cadastro > Contas a Pagar. . A sugestão padrão é efetuada a partir de Cadastros > Filiais > Contas a Pagar.

Vigência do contrato

Datas de vigência inicial e final do contrato.

Saldo do Contrato

Saldo do contrato. Para contratos de tipo 10 (Financeiro com Saldo). Este campo será atualizado a cada nota fiscal gerada referenciando o contrato.

**Código Favorecido**

Ver Norma IFRS-16. Após selecionar a conta para o favorecido os campos abaixo serão preenchidos:

* Banco Fav.
* Tipo de conta
* Descrição
* Agência
* Conta corrente

Se informado um **Código Favorecido**, a **Conta corrente** é obrigatória.

O preenchimento do código ocorre da seguinte forma:

1. **Parâmetro global DetsugFav = N na tela F000PGS:** preenche os dados de favorecido conforme a grade de rateio
2. **Parâmetro global DetsugFav = S na tela F000PGS:**
   abre uma tela para que o usuário informe o favorecido, isso quando na grade de rateio o **Código Favorecido** não for informado. O sistema utiliza os dados da grade de rateio se os campos estiverem preenchidos

**Seq. Banco**

Conforme acima.

Contratos do tipo 10 - Financeiro com Saldo

* No contrato tipo 10, os campos Tipo do Título, N° do Título, Origem Parcelas e Transação Título são desabilitados. Para este tipo de contrato ficaram habilitados somente os campos Valor total, Saldo do Contrato, Vigência do Contrato, Forn dif Ctr, Herdar bem e Condição de Pagamento.
* A guia Serviços é habilitada para gravar um item de serviço, bem como seus rateios. É possível informar apenas um item de serviço, caso tente informar mais de um item o processo é bloqueado. Embora esta grade tenha sido liberada, não existe a obrigatoriedade de informar um item de serviço, o objetivo desta informação é apenas para que possam ser definidos os rateios, que serão herdados para os itens da nota fiscal de entrada ao utilizar um contrato tipo 10
* É obrigatório informar o valor total, e o mesmo tem que coincidir com o valor do item de serviço do contrato (quando informado um item de serviço), a consistência ocorre no processamento. O cálculo para esta consistência é: Quantidade do item \* Preço Unitário (excluindo o valor de outras despesas). Caso não houver esta coerência de valores o processo será bloqueado com uma mensagem.

  Será possível efetuar alterações no contrato tipo 10 somente quando o mesmo ainda não tenha sido utilizado, ou seja, o Valor Total ainda estiver igual ao Saldo. Quando o saldo do contrato já foi utilizado pelo vínculo em alguma nota fiscal, as alterações não disponíveis no contrato são: alteração do fornecedor nos dados gerais e alteração dos dados na guia complemento e na guia Serviços
* Para contrato tipo 10 é obrigatório informar um período de Vigência
* O campo Vigência do Contrato é desabilitado caso o contrato tenha sido utilizado em alguma nota fiscal
* Ao digitar o complemento é atribuído **A - Ativo** para a situação do contrato, visto que este não gera títulos e para outros tipos de contrato este campo é inicializado como **I - Inativo** e é alterado para **A - Ativo** apenas na geração de títulos. Sendo assim, caso for um contrato tipo 10, este terá o campo situação alterado para ativo, evitando assim que o usuário precise alterar a situação manualmente para **A - Ativo** a cada contrato tipo 10 digitado

Contratos do tipo 11 - Por Eventos

Esse é idêntico ao contrato tipo 10, possui também o vínculo com a NF-e , tendo o abatimento de saldo do contrato e também o abatimento do saldo do evento.

Além de ser semelhante ao contrato financeiro com saldo, o contrato por eventos possui algumas funcionalidades adicionais, que são:

O cadastramento dos eventos do contrato e suas posteriores liberações, feitas apenas por usuários cadastrados para tal permissão. Na guia Eventos são mostrados todos os eventos ligados ao contrato, não é possível fazer alteração nos eventos a partir desta grade, sendo que nesta tela é possível apenas liberar o referido evento ou cancelar a liberação do mesmo. A liberação e cancelamento da liberação do evento pode ser feita apenas por usuários cadastrados, para isso são utilizados os botões Liberar e Canc. Liber. No rodapé da guia estão disponíveis os botões:

Cad. Eventos

Acessar a tela de cadastro de eventos.

NFE Evento

Consulta as ligações do mesmo com itens de NFEs

Gravar Obs.

Confirma a observação digitada no momento da liberação de um evento.

Uma vez liberado o evento, sua situação pode ser alterada somente por um usuário com
permissão cadastrado na tela Eventos de Contrato de Compra (F460EVE) e se ainda não foram geradas notas ligadas ao evento (mesmo que só digitadas,ou seja, somente se o saldo do evento for igual ao valor do evento).

Observação

O tratamento do saldo do evento é semelhante ao tratamento do saldo do contrato. Na gravação de um contrato tipo 11 que ainda não foram cadastrados eventos, é questionado ao usuário sobre o cadastramento dos eventos. Caso deseje cadastrar, é exibida a tela F460EVE. Se o usuário optar por não cadastrar, futuramente poderá acessar a guia Eventos. Nela só acessam os botões Liberar e Canc. Liber. os usuários cadastrados na tela F460EVE (a habilitação ou não dos referidos botões é feita de acordo com a situação na grade), ou seja, só poderá liberar evento se o usuário tiver permissão para o mesmo, e só pode cancelar liberação de um evento se o usuário tiver permissão para o mesmo e se ainda não foram processadas notas ligadas ao evento, ou seja:

O cancelamento da liberação somente será permitido se:

* Valor do evento for igual ao saldo (evento não foi usado em nenhuma nota)
* O evento não estiver ligado a algum item de nota (mesmo que a nota não esteja fechada, só foi digitada, não será permitido cancelar liberação)

Na exclusão de um contrato são excluídos seus eventos e os usuários liberadores dos eventos. Não é permitida a exclusão de um contrato caso o mesmo já estiver vinculado a uma nota fiscal de entrada. Na duplicação de um contrato o usuário tem a opção de escolher se deseja duplicar também os eventos, e conseqüentemente os usuários liberadores destes eventos.

## Páginas relacionadas

* [Tabelas > Financeiro > Tipos de Títulos](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f002tpt.htm)
* [Tabelas > Comercial > Fiscais > Séries Notas Fiscais](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f020snf.htm)
* [Tabelas > Transações > Cadastro > Contas a Pagar.](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f001tpa.htm)
* [Cadastros > Filiais > Contas a Pagar](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070fpa.htm)
* [Norma IFRS-16](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/manuais_processos/controladoria-tributos/ifrs-16.htm)
* [Eventos de Contrato de Compra (F460EVE)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f460eve.htm)
