# Informações de transporte

> **Fonte:** F135FCP - Formação de Cargas (via Pedidos) — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/f135fcp.htm  
> **Trilha:** Ajuda por telas > Mercado > Gestão de Distribuição > Cargas > Formação  
> **Telas citadas:** —  
> **Identificadores de regras:** —

---
Transp./placa

Transportadora e placa do veículo. É obrigatório informar uma transportadora. Ao clique do botão Processar, se este campo não possuir informação será exibida mensagem ao usuário. Pode-se informá-la no cabeçalho e pelo botão Veículos. Uma vez informada, a rotina busca o peso e o volume máximo que está no cadastro da transportadora e mostra no cabeçalho da tela.A rotina também verifica se a capacidade de peso e volume da transportadora atendem ao peso e volume total da carga. Caso não atenda será
exibida uma mensagem de aviso e permitirá ao usuário, selecionar outra transportadora, cancelar o processo ou continuar com a mesma transportadora. O campo Controla Veículos dos parâmetros para vendas da filial define se o campo Placa terá um campo de pesquisa de registros associado.

Transp./Motorista

Código da transportadora e motorista que farão parte da carga.

Transp. Redespacho

Código da transportadora de redespacho para a carga.

Utilizar Memória de Carga

Terá por finalidade sugerir a última transportadora, placa e motorista utilizados na rota informada através da tela associada ao botão Seleção para a formação da carga. Esta informação será sugerida da tabela de notas fiscais. Esta opção, quando marcada, exibida ao lado do campo Considerar faturamento dos últimos [nn] dias para a busca da sugestão dos valores para a transportadora, placa e motorista. Ao clicar no botão Mostrar será efetuada a busca da memória da carga, sendo carregados para o cabeçalho da tela os valores sugeridos para os campos mencionados.  

Caso nenhum valor seja retornado o sistema irá exibir mensagem de aviso: Não há memória de carga para a rota selecionada: xxxx. Os dados da transportadora/placa/veículo deverão ser informados manualmente.. As consistências referentes a Tipo de Veículo X Clientes e Tipo de Veículo X Agrupamento de Estoques continuarão sendo feitas no processamento da carga. As opções Utilizar Memória de Carga e Considerar faturamento dos últimos [nn] dias] serão gravadas por usuário, ou seja, na próxima vez que a tela for acessada pelo mesmo usuário as opções virão pré-definidas conforme o acesso anterior.

Peso Máximo

Será visualizado o peso máximo que a transportadora ou o veículo poderá conter. Na seguinte situação, se nos parâmetros para vendas da filial, possuir a indicação no campo Controla Veículos igual N, será exibida a informação do peso máximo cadastrado na transportadora, caso contrario, a informação exibida será o peso máximo cadastrado no veículo (Cadastro>Transportadora>Veículos>Cadastros).

Volume Máximo

Será visualizado o volume máximo que a transportadora ou o veículo poderá conter. Na seguinte situação, se nos parâmetros para vendas da filial, possuir a indicação no campo Controla Veículos igual N, será exibida a informação do volume máximo cadastrado na transportadora, caso contrario, a informação exibida será o volume máximo cadastrado no veículo (Cadastro>Transportadora>Veículos>Cadastros).

Diferença

Localizado abaixo dos campos Peso Máximo e Volume Máximo. Estes campos apresentam a diferença entre o peso máximo da transportadora ou veículo (conforme os parâmetros para vendas da filial, campo controla veículos) do peso bruto dos pedidos selecionados, bem como a diferença entre o volume máximo e o volume dos pedidos selecionados.
