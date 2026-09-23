# Processos

> **Fonte:** F075GFP - Cadastro de Produtos — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075gfp.htm  
> **Trilha:** Ajuda por telas > Cadastros > Produtos e Serviços > Produtos  
> **Telas citadas:** E075VDR, E075VPR, F070ECN, F070EMP, F075OPC  
> **Identificadores de regras:** GER-000ICECO01

---
* Duplicação automática de produto/serviço para outras empresas;
* Geração automática do DUN-14.

Na grade Derivações Possíveis existe o botão EAN 13
para efetuar-se o cadastro da numeração do código de barras (padrão EAN 13) para o
produto/derivação.  
Ver também codificação do produto utilizando dígito
verificador.

Durante o cadastro de novos códigos, não é permitido informar caracteres especiais, como aspas (). O sistema considera como caracteres válidos os números de 0 (zero) a 9 (nove) e o alfabeto de A a Z. Somente será permitido o cadastro de ponto (.) e hífen (-). Esses serão exceção de cadastro de caracteres especiais, porém, não é recomendável o uso dos mesmos.

Caso seja informado algum caractere inválido, a mensagem A utilização de caracteres especiais (vírgula, aspas, espaço, hífen, etc) não é recomendada na codificação, pois pode causar problemas em campos do tipo abrangência e/ou consultas ao banco de dados. Verifique o código e, se possível, remova os caracteres especiais! será apresentada.

Quando o identificador de regras GER-000ICECO01 estiver ativo, a mensagem não será apresentada, pois essa é a função do identificador. Porém, não será possível sair do campo até que seja informado um código válido.

Os caracteres acima citados, provocam erro de sintaxe nos
comandos internos executados no banco de dados, prejudicando
o funcionamento normal das rotinas.  
Ver botão Monta Código e botão Monta Desc.  
Todas as
alterações feitas no produto ou derivação serão respectivamente gravadas nas
tabelas E075VPR (Cadastros - Produtos - Alteração de Produtos) ao alterar um
produto e E075VDR (Cadastros - Produtos - Alteração de Derivações) ao alterar
uma derivação.

Quando a empresa fizer uso da gestão de contabilidade, conforme
indicação no cadastro da empresa (F070EMP),
será consistido o preenchimento das contas contábeis e financeiras
conforme segue:

* Será obrigatório informar a conta de receita quando produto tiver
  indicação que pode ser vendido.
* Será obrigatório informar a conta de despesa quando produto tiver
  indicação que pode ser comprado ou requisitado;
* Será obrigatório informar a conta de estoque/imobilizado quando
  produto tiver indicação que pode ser comprado ou requisitado;
* Será obrigatório informar a conta de custo direto quando produto tiver
  indicação que pode ser comprado ou requisitado;
* Será obrigatório informar a conta de custo indireto quando produto
  tiver indicação que pode ser comprado ou requisitado;
* Será obrigatório informar a conta financeira de receita padrão quando
  produto tiver indicação que pode ser vendido;
* Será obrigatório informar a conta financeira de despesa padrão quando
  produto tiver indicação que pode ser comprado ou requisitado.

Importante

* Se o sistema estiver parametrizado para a geração do bloco K, algumas consistências e bloqueios podem ser realizadas nessa tela, garantindo a correta geração de informações do arquivo, conforme guia prático. Confira estas consistências na tela Parâmetros e consistências da empresa (F070ECN).
* Quando um novo produto for cadastrado, a ligação automática com o depósito padrão somente ocorrerá quando a caixa de seleção **Ligar Automaticamente Produto ao Depósito Padrão** da tela F075OPC (botão Opções) estiver selecionado, a família do produto não possuir mascará de derivação e for Produzido ou Comprado.
* Quando um novo produto for cadastrado e a opção de seleção Visualizar Somente Derivações Cadastradas da tela F075OPC (botão Opções) estiver selecionada, a grade **Derivações Possíveis** não ficará ativa para alteração, pois não existe derivação cadastrada para mostrar. Para mostrar as derivações possíveis na grade, a opção Visualizar Somente Derivações Cadastradas, não deve estar assinalada.

## Páginas relacionadas

* [Duplicação automática de produto/serviço para outras empresas](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/manuais_processos/mercado/duplicacao-automatica.htm)
* [Geração automática do DUN-14](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_manufatura/dun-14.htm)
* [dígito
			verificador](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/conceito_digitoverifproduto.htm)
* [GER-000ICECO01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ger_000iceco01.htm)
* [Monta Código](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075mcp.htm)
* [Monta Desc.](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075mde.htm)
* [F070EMP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070emp.htm)
* [parametrizado](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/processo-bloco-k.htm#ParametrizacoesIniciais)
* [(F070ECN)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070ecn.htm)
* [F075OPC](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075opc.htm)
