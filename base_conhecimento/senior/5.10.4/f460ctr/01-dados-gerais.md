# Dados Gerais

> **Fonte:** F460CTR - Contrato de Compra (Comercial/Financeiro/Eventos) — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f460ctr.htm  
> **Trilha:** Ajuda por telas > Suprimentos > Gestão de Compras > Contratos  
> **Telas citadas:** E021MOT, E023CRP, E031MOE, E095FOR, E460APL, F023CRP, F070ENT, F070FCA, F070FCP, F099UCP, F461GNC  
> **Identificadores de regras:** CPR-460CONDG01

---
Situação

Para que esse fique disponível para edição, é necessário possuir o parâmetro Alterar situação do contrato de compra definido como "S - Sim" na tela Compras e Recebimento (F099UCP). Além disso, o contrato deve atender a uma das seguintes condições, dependendo do tipo de contrato:  

Para contratos dos tipos 1, 2, 5, 9, 10 e 11:

* Não deve possuir controle de aprovação; ou
* Possuir controle de aprovação e estar aprovado

Para contratos dos tipos 3 e 4:

* Não deve haver títulos de contas a pagar; ou
* Não deve possuir controle de aprovação; ou
* Possuir controle de aprovação e estar aprovado; ou
* Se houver títulos gerados, o parâmetro Permite Inativar Contrato financ. com títulos, da tela Parâmetros da Filial para Compras (F070FCP) deve estar definido como "S - Sim"

Quando o contrato estiver na situação "I - Inativo" na base, o campo Múltiplas Competências ficará habilitado para edição e permitirá alteração.

Importante

Um contrato inativado pode ser ativado novamente. Caso deseje bloquear a alteração do status de um contrato, utilize o identificador de regras CPR-460CONDG01. Neste, configure uma regra específica para impedir a mudança de status do contrato de "I - Inativo" para "A - Ativo".

Múltiplas Competências

O valor padrão será sim, para qualquer contrato. Este campo indica se o contrato permite que seja gerado mais de uma competência na notas fiscais via contrato comercial. O campo ficará desabilitado tanto na situação A (ativo) ou I (inativo) para contratos tipo 10 (financeiro com saldo) e 11 (por eventos).

**Data Cancelamento**

Esse campo é de preenchimento obrigatório ao alterar a situação do contrato de **Ativo** para **Inativo**. O bem e seus acréscimos (quando houver) serão baixados sempre que um contrato for inativado.

Fornecedor

Código do fornecedor. Registros gravados na tabela E095FOR e cadastrados na tela  Cadastros > Fornecedores >Cadastro .

Nº Contrato

Numero do contrato. Sugerido o mesmo número do contrato, permitindo ao usuário alterar ou informar qualquer dado alfa-numérico.

Objeto

Objeto do contrato.

Nº Interno Origem

Número interno do contrato de origem.

* Para contratos adicionais, tipos "2 - Comercial Adicional" ou "4 - Financeiro Adicional", deve-se informar o contrato original para estabelecer a ligação entre ambos;
* Para contratos gerados através de duplicação, esse campo sempre receberá o número do contrato base da duplicação.

Emissão

Data de emissão do contrato.

Entrada

Data de entrada do contrato.

Fornecedor Tit

Trata-se do fornecedor para geração título a pagar, neste campo é sugerido o mesmo fornecedor do contrato, porém pode ser alterado. O código do fornecedor preenchido aqui será considerado posteriormente na geração da nota fiscal na tela F461GNC.

Grupo Contas a Pagar

Código do grupo de contas a pagar. Registros gravados na tabela E023CRP e cadastrados a partir de F023CRP. A sugestão padrão é efetuada a partir das definições/histórico do fornecedor.

Código Fator de Correção

Código da moeda ou índice como fator de correção (financeiro). Registros gravados na tabela E031MOE e cadastrados a
partir de Tabelas > Financeiro > Moedas/Índices > Cadastro/Manutenção. A sugestão padrão é a moeda da empresa .

Data Fator de Correção

Data da cotação da moeda ou índice como fator de correção(financeiro).

Moeda

Código da moeda para conversão para a moeda da empresa na geração da nota fiscal. Registros gravados na tabela E031MOE e cadastrados a partir de Tabelas > Financeiro > Moedas/Índices > Cadastro/Manutenção. A sugestão padrão é a moeda da empresa.

Aplicação

Código da aplicação do contrato. Registros gravados na tabela E460APL e cadastrados a partir de Comercial > Compras > Contratos > Aplicações.

Considera no Fluxo de Caixa

Indicativo se o contrato deverá ser considerado no fluxo de caixa.

Motivo

Código do motivo da situação do contrato. Registros gravados na tabela E021MOT e cadastrados a
partir de Tabelas > Gerais > Motivo Sit/Obs.

Endereço entrega 

Sequência do endereço de entrega cadastrada na tela Endereço de Entrega (F070ENT). Caso este campo permaneça com zero, é considerado o endereço de entrega informado na tela Cadastro de Filiais (F070FCA).

Obs. Motivo

Observação do motivo da situação do contrato.

Usu. Últ. Alteração

Usuário que realizou última alteração no contrato. O campo é somente para consulta, portanto se mantém desabilitado.

Data Últ. Alteração

Data da última alteração realizada no contrato. O campo é somente para consulta, portanto se mantém desabilitado.

Hora Últ. Alteração

Hora da última alteração realizada no contrato. O campo é somente para consulta, portanto se mantém desabilitado.

Data Base Contábil

Serve para geração de títulos do contrato, podendo assumir os valores 0 (zero) - Nenhum, 1 - Entrada ou 2 - Vencimento.

Importante

* Para tipo de contrato comercial, o campo Data Base Contábil, receberá valor 0 - Nenhum e será ocultado da tela
* Para tipo de contrato financeiro, o campo Data Base Contábil, receberá como sugestão valor 1 - Entrada e o usuário poderá escolher entre as opções 1 - Entrada e 2 - Vencimento
* Ainda nessa opção (contrato financeiro), quando for feita a consulta do contrato e já tiver sido gerado título o campo Data Base Contábil ficará desabilitado

Botão Personalizar

Quando existir controle de Aprovação Multinível, é possível alterar os campos de usuário enquanto o contrato não estiver liberado. Após liberar o contrato para aprovação, os campos de usuário (acessados através do botão Personalizar) estarão disponíveis apenas para consulta.

Observação

A parametrização referente à forma de pagamento será herdada das definições de histórico do fornecedor, não existindo campo que permita edição de tal informação durante a geração/edição do contrato.

## Páginas relacionadas

* [F099UCP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f099ucp.htm)
* [F070FCP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070fcp.htm)
* [CPR-460CONDG01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/cpr_460condg01.htm)
* [Cadastros > Fornecedores >Cadastro](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f095cad.htm)
* [F461GNC](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f461gnc.htm)
* [F023CRP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f023crp.htm)
* [definições/histórico do fornecedor](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f095hfo.htm)
* [Tabelas > Financeiro > Moedas/Índices > Cadastro/Manutenção](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f031aim.htm)
* [F070ENT](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070ent.htm)
* [F070FCA](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070fca.htm)
