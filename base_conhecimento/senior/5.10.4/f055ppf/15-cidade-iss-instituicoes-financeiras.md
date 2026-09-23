# Cidade ISS Instituições Financeiras

> **Fonte:** F055PPF - Configuração de Impostos para a Filial — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f055ppf.htm  
> **Trilha:** Ajuda por telas > Cadastros > Controladoria > Tributos  
> **Telas citadas:** —  
> **Identificadores de regras:** —

---
Habilitada sempre que o **Método Apuração** for **1** ou **2**.

#### Campos

**Data Base**

Informe uma data base.

**Cidade ISS**

O sistema lista o Código RAIS da filial informada na tela (não pode ser alterado).

**Filial Origem**

Informe uma filial que possua o mesmo Código RAIS da filial informada no topo da tela ou utilize o botão **Sugerir**.

**Tipo Compensação**

Selecione a forma como o saldo será utilizado na apuração dos impostos 65 e 72 (abater imposto a recolher ou processo administrativo).

**Parcelamento Crédito**

Parcelamento do saldo credor da apuração dos impostos 65 e 72.

Os campos acima têm preenchimento obrigatório para o imposto 72, sendo que, ao utilizar o **Tipo Compensação** **1 - Lançar o crédito diretamente no mês imediatamente posterior**, será sugerido no campo **Parcelamento Crédito** o valor **1**, bloqueando sua edição.

Para mais informações sobre os campos acima, confira a documentação sobre a apuração do ISSQN para instituições financeiras, especialmente o tópico 3.

#### Botões

**Sugerir**

Sugere as filiais que possuem o mesmo código RAIS da filial selecionada. A data sugerida será a última data de apuração se o campo **Data Base Cálculo** estiver selecionado com a opção **Última**. Se a opção selecionada para o campo for **Todas** ou não houver apuração, será sugerido o primeiro dia do mês vigente. Ou seja, pelo menos uma apuração precisa ser realizada para que o sistema possa sugerir uma data diferente da atual.

Importante

Disponível apenas para os impostos "65 - ISS Retido", "73 - ISS (LC 175/2020)" e "74 - ISS Retido (LC 175/2020)" e serve como facilitador para a parametrização das cidades que fazem parte da apuração.

Ao clicar em Sugerir, serão verificadas as notas fiscais emitidas desde a última apuração e, caso as cidades para cálculo do ISS não estiverem devidamente parametrizadas para o imposto selecionado, as mesmas serão inseridas na guia Cidade ISS com base nos parâmetros informados na guia Impostos.

**Excluir**

Verifica o campo **Data Base Cálculo** antes de realizar a exclusão. Portanto é possível excluir todos os registros da guia ou apenas o registro da última data base.

Lembrando que os registros da guia não podem ser alterados. Eles são modificados apenas no momento da inclusão, permitindo duas operações apenas: inclusão e exclusão de linhas da guia. Além da inserção manual, os dados podem ser inseridos a partir do botão **Sugerir**.

Para mais informações, confira a documentação sobre a apuração do ISSQN para instituições financeiras.

## Páginas relacionadas

* [apuração do ISSQN para instituições financeiras](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/issqn-if.htm)
