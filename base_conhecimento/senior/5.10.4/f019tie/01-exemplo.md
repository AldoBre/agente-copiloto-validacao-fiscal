# Exemplo

> **Fonte:** F019TIE - ICMS Especial - Por Estado — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f019tie.htm  
> **Trilha:** Ajuda por telas > Cadastros > Mercado e Suprimentos > Parâmetros Fiscais > ICMS especiais  
> **Telas citadas:** —  
> **Identificadores de regras:** —

---
É útil em casos em que a parametrização é igual para todas as filiais, mas também pode ser utilizado como parametrização alternativa para filiais que tem algum cadastro especifico.

Exemplo 1

A empresa possui duas filiais ("A" e "B") em SC, ambas com o mesmo padrão de ICMS especial, então é utilizada a opção Cadastro padrão para filiais, e cadastrar os ICMS especiais.

Porém, a filial "B" tem uma exceção para o estado de Mato Grosso, com isso, é possível cadastrar (Inserir) o ICMS especial informando a filial "B", com estado destino "MT".

Assim, sempre que calcular o imposto para a filial "B", com destino à Mato Grosso, buscará esse cadastro "exclusivo" feito para a filial "B". Os demais estados de destino serão buscados da parametrização feita com a opção Cadastro padrão para filiais.
