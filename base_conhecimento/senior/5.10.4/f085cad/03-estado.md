# Estado

> **Fonte:** F085CAD - Cadastro de Clientes — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f085cad.htm  
> **Trilha:** Ajuda por telas > Cadastros > Clientes e Fornecedores > Clientes  
> **Telas citadas:** E085CLI, E085INE  
> **Identificadores de regras:** —

---
Guia destinada ao cadastramento da sigla do estado e inscrição estadual de cada cliente.

Estado

Nesta tela, o campo Estado existe na guia Cadastro e na guia Estado para que seja possível cadastrar dois estados diferentes em um único cliente. O estado cadastrado no cliente através da guia:

* Cadastro: será gravado na Tabela em Cadastros - Clientes (E085CLI);
* Estado: será gravado na Tabela em Cadastros - Clientes - Inscrição Estadual (E085INE).

Observação

O sistema não permitirá cadastrar um estado na guia Estado que seja o mesmo já parametrizado na guia Cadastro. Caso haja a tentativa, uma mensagem será exibida consistindo que o respectivo estado já está informado.

Inscrição Estadual   
Nesta tela, o campo Inscrição Estadual existe na guia Cadastro e na guia Estado para que seja possível cadastrar duas inscrições estaduais diferentes em um único cliente. A Inscrição Estadual cadastrada no cliente através da guia:

* Cadastro: será gravado na Tabela em Cadastros - Clientes (E085CLI);
* Estado: será gravado na Tabela em Cadastros - Clientes - Inscrição Estadual (E085INE).

Importante

* A biblioteca de validação da Inscrição Estadual (arquivo dllie32.dll) é carregada sempre a partir do local de instalação do produto Gestão Empresarial | ERP dentro do diretório Sapiens;
* Em caso de execução a partir da DLL de integração do produto Gestão Empresarial (ISapiensDll.dll) com o produto Gestão de Pessoas | HCM, a carga dessa biblioteca é feita a partir do caminho de compartilhamento de rede da instalação do produto Gestão Empresarial no formato UNC (Uniform Naming Convention), que apresenta a seguinte convenção para acesso a um caminho de rede compartilhado:
  + Nome do computador\nome do compartilhamento\diretório.
* A instalação do produto Gestão Empresarial | ERP é uma instalação parte estação, ou seja, o arquivo DLL será obtido localmente. Caso seja utilizado somente um atalho para o Sapiens.exe apontando para um caminho de rede \\servidor\senior\sapiens\sapiens.exe, é necessário copiar a DLL para a unidade local da máquina. Do contrário, haverá problemas no cadastro dos Clientes e Fornecedores.
* A orientação referente à DLLIE32.DLL descrita acima se aplica para esta tela ou para qualquer outra rotina que faça utilização da DLL.
