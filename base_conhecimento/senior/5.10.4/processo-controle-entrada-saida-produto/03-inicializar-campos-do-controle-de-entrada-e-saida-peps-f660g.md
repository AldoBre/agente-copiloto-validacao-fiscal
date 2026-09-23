# Inicializar campos do Controle de Entrada e Saída (PEPS) (F660GDG)

> **Fonte:** Processo para Controle de Entrada e Saída de Produtos (PEPS/FIFO) — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/processo-controle-entrada-saida-produto.htm  
> **Trilha:** Segmentos > Compliance  
> **Telas citadas:** F075CEP, F660GDG  
> **Identificadores de regras:** —

---
Para atender o leiaute 14 do SPED Fiscal, estão disponíveis campos no Controle de Entrada e Saída:

* **Controle de Entrada:** Alíquota FCP, Base FCP, Valor FCP;
* **Controle de Saída:** Base FCP Complementar, Valor FCP Complementar, CFOP, CST ICMS, Valor Total do Item, Unidade de medida.

Para inserir esses campos nos registros já presentes nas tabelas do Controle, basta processar a rotina.

Com o Controle ativado para a empresa e os produtos configurados para terem o seu estoque controlado pelo PEPS, basta inicialize o Controle do consumo do estoque. A forma de inicializar o Controle do PEPS de um produto é por meio da tela F075CEP. Com isso, o produto indicado anteriormente para ter o Controle por PEPS terá todo o seu histórico inicializado com base no período informado, fazendo as ligações entre os documentos fiscais de entrada e seus respectivos documentos fiscais de saída.

A rotina atende **apenas** os campos citados acima, não interferindo nos já existentes no Controle.

**Importante**

E ao processar a tela Controle de Entrada de Produtos (F075CEP), caso não tenha sido feita essa inicialização será apresentada a mensagem: "É necessário fazer a inicialização dos campos do Controle de Entrada e Saída através da tela F660GDG para a empresa". Uma vez feito esse procedimento, não será mais necessário realizá-lo novamente para a Empresa/Filial/Período.

## Páginas relacionadas

* [F075CEP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075cep.htm)
