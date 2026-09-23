# Tag CNPJ do fabricante (CNPJFab)

> **Fonte:** F000INE - Via Recebimento de Documento Eletrônico — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_suprimentos/f000ine.htm  
> **Trilha:** Ajuda por telas > Suprimentos > Gestão de Recebimento > Notas Fiscais de Entrada  
> **Telas citadas:** E000NFC, F076FAB  
> **Identificadores de regras:** CPR-000INECM02

---
* A consistência **O Produto possui indicativo de produção em escala não relevante e o fabricante não foi informado. Informe o código do fabricante** será executada quando: no XML houver um CNPJ de fabricante (tag CNPJFab) informado, a tag indEscala estiver definida como “N” e, no Cadastro de Fabricantes (F076FAB), não for encontrado um fabricante com o mesmo CNPJ constante no XML.
* Caso seja necessário que a consistência não seja executada, pode-se utilizar o identificador de regras CPR-000INECM02. Nesse caso, pode-se alterar o campo E000NFC.INDESC para "S" e, desta forma, a consistência não será executada para os itens alterados.
* O campo Produção em Escala Relevante presente da derivação do produto somente será considerado quando: no XML houver CNPJ do fabricante (tag CNPJFab ) informado, não houver a tag indEscala informada e o CNPJ do fabricante do XML estiver parametrizado no ERP (F076FAB).

## Páginas relacionadas

* [F076FAB](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f076fab.htm)
* [CPR-000INECM02](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/cpr_000inecm02.htm)
