# Identificador de Regra

> **Fonte:** Identificador de Regra — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/cpr_000alicd01.htm  
> **Trilha:**   
> **Telas citadas:** E440IPC, E440ISC, F440GNE  
> **Identificadores de regras:** CPR-000ALICD01

---
## CPR-000ALICD01

**Módulo:** CPR - Compras.

**Finalidade:** Este identificador permite a alteração do valor de ICMS desonerado bem como o motivo da desoneração ao calcular o item de produto da nota fiscal de entrada.

**Características:** Todos os campos do item de produto da nota fiscal de entrada estão disponíveis na regra através da sintaxe E440IPC.[NomeCampo], por exemplo, E440IPC.CodPro.  

A chamada deste identificador ocorre antes do cálculo dos impostos, visto que a desoneração é convertida em desconto e irá afetar a base de cálculo dos demais impostos, e para os itens de serviço, permitindo assim, alterar o motivo de desoneração e o valor de ICMS desonerado do item de serviço. Para saber se o identificador está sendo chamado por produto ou serviço, deverá ser verificado na regra qual é a tabela enviada através da variável **VenATabela**. Se a tabela for "E440IPC" significa que a chamada está sendo feita por item de produto. Se for "E440ISC" significa que a chamada está sendo feita por item de serviço.

**Regra:**

Definir Alfa VenATabela;

Se (VenATabela = "E440IPC")  
Inicio  
   E440IPC.MotDes = 9;  
   E440IPC.VlrIcd = 100;  
Fim  
Senao  
Se (VenATabela = "E440ISC")  
Inicio  
   E440ISC.MotDes = 9;  
   E440ISC.VlrIcd = 300;  
Fim;

**Tela:** F440GNE.

**Transação:** Não se aplica.

**Variáveis Disponibilizadas:**

| Nome | Tipo | Observações | Retorna Valor |
| --- | --- | --- | --- |
| VenATabela | ALFA | Indica qual é a tabela utilizada | N |

Atenção

Caso o parâmetro global LisVarReg esteja habilitado, a variável ListaVariaveis estará disponível em todos os identificadores de regras do sistema. O conteúdo desta variável lista os campos disponibilizados no identificador de regras em questão.

Não é aconselhada a ativação desse parâmetro global para o uso cotidiano. Esse recurso de listagem dos campos de identificadores auxilia a construção de regras e o Suporte para, por exemplo, depuração ou quando não houver acesso à documentação dos identificadores de regras.

## Páginas relacionadas

* [LisVarReg](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f000pgs.htm#LisVarReg)
