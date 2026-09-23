# Processos

> **Fonte:** F075PRO - Cadastro de Produtos — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f075pro.htm  
> **Trilha:** Ajuda por telas > Cadastros > Produtos e Serviços > Produtos  
> **Telas citadas:** E075VDR, E075VPR, F070ECN  
> **Identificadores de regras:** GER-000ICECO01

---
* Número de Dias de Precedência
* Rotina de múltiplos volumes
* Duplicação automática de produto/serviço para outras empresas
* Curso online
* Geração automática do DUN-14

Somente no cadastro de Produtos Agrupados é possível gerar codificação com
sequenciador de código automático.

Codificação do produto utilizando dígito verificador: durante o cadastro de novos códigos, não é permitido informar caracteres especiais, como aspas (). O sistema considera como caracteres válidos os números de 0 (zero) a 9 (nove) e o alfabeto de A a Z. Somente será permitido o cadastro de ponto (.) e hífen (-). Esses serão exceção de cadastro de caracteres especiais, porém, não é recomendável o uso dos mesmos.

Caso seja informado algum caractere inválido, a mensagem A utilização de caracteres especiais (vírgula, aspas, espaço, hífen, etc) não é recomendada na codificação, pois pode causar problemas em campos do tipo abrangência e/ou consultas ao banco de dados. Verifique o código e, se possível, remova os caracteres especiais! será apresentada.

Quando o identificador de regras GER-000ICECO01 estiver ativo, a mensagem não será apresentada, pois essa é a função do identificador. Porém, não será possível sair do campo até que seja informado um código válido.

O cadastro de produtos é por Empresa, ou seja, o produto somente estará disponível na Empresa ativa. Consistência entre produto e derivações:

1. Ao ligar uma derivação ao produto se ela for adicionada como Ativa o produto caso esteja inativo será ativado automaticamente;
2. Ao desligar/excluir todas as derivações do produto ele será inativado automaticamente;
3. Ao inativar todas as derivações ligadas ao produto o mesmo será inativado automaticamente;
4. Ao ativar uma derivação caso o produto esteja inativo será necessário ativá-lo manualmente;
5. Ao inativar um produto, todas as derivações ficarão inativas;
6. Todas as alterações feitas no produto ou derivação serão respectivamente gravadas nas tabelas E075VPR (Cadastros - Produtos - Alteração de Produtos) ao
   alterar um produto e E075VDR (Cadastros - Produtos - Alteração de Derivações) ao alterar uma derivação;
7. Ao ativar um produto, todas as derivações ficarão ativas.

**Observação**

Se o sistema estiver parametrizado para a geração do Bloco K, algumas consistências e bloqueios podem ser realizadas nessa tela para garantir a geração correta das informações do arquivo. Confira essas consistências na tela Parâmetros e consistências da empresa (F070ECN).

## Páginas relacionadas

* [Número de Dias de Precedência](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_manufatura/conceito_dias_precedencias.htm)
* [Rotina de múltiplos volumes](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_mercado/mulvol.htm)
* [Duplicação automática de produto/serviço para outras empresas](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/manuais_processos/mercado/duplicacao-automatica.htm)
* [Curso online](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/curonl.htm)
* [Geração automática do DUN-14](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_manufatura/dun-14.htm)
* [sequenciador de código automático](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f084mpr.htm)
* [Codificação do produto utilizando dígito verificador](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/conceito_digitoverifproduto.htm)
* [GER-000ICECO01](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/identificadores_regras/ger_000iceco01.htm)
* [parametrizado](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_controladoria/processo-bloco-k.htm#ParametrizacoesIniciais)
* [(F070ECN)](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070ecn.htm)
