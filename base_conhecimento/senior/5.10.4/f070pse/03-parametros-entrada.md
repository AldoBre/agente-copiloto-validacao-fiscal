# Parâmetros Entrada

> **Fonte:** F070PSE - Parâmetros Fiscais de produtos e serviços por filial e estado — versão 5.10.4  
> **URL:** https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070pse.htm  
> **Trilha:** Ajuda por telas > Cadastros > Mercado e Suprimentos > Parâmetros Fiscais  
> **Telas citadas:** F070FCP  
> **Identificadores de regras:** —

---
Filial

Código da filial em que a definição será aplicada.

Inicio da vigência

Data em que as definições serão aplicadas.

Estado

Estado em que a definição será aplicada.

Produto

Código do produto da parametrização do DIFAL.

% ICMS UF filial

Percentual de ICMS interno especial para o estado da filial.

% Redução Base ICMS

Percentual de redução da base de ICMS na UF.

Tributa ICMS DIFAL

Indica se o produto tributa ICMS na UF de destino.   
Através da configuração deste campo para a UF da respectiva Filial, é possível definir se a operação deve calcular a parte do DIFAL relacionada a UF de Origem.

% FCP

Porcentagem da alíquota para o fundo de combate a pobreza. Indica se o FCP deve ser calculado nas operações de importação. Quando configurado como Sim e a nota fiscal de entrada ou ordem de compra for de importação (quando o tipo de mercado do fornecedor for E - Exterior), o cálculo do FCP é realizado.

O cálculo do FCP Normal nas operações de entrada depende das seguintes condições:

1. Operação interna;
2. Operação Interestadual / Externa
   * Importação: tipo de mercado do fornecedor for **Exterior**;
   * Ativo Imobilizado / Uso e consumo: aplicação da natureza na transação for **I - Imobilizado** ou **S - Consumo próprio**.

Para todas as situações, a alíquota de FCP deve ser configurada na UF da Filial.

%Efet. ICMS UF destino   
Este campo será utilizado nos processos de compra de imobilizado e indica que o estado de destino de uma operação de aquisição de ativo imobilizado está enquadrado no Convênio ICMS 52/91.

Tipo Base Calc. Difal Imobil.

Este campo será utilizado nos processos de compra de imobilizado e indica qual o tipo da base de cálculo do diferencial de alíquota do ICMS para compra de ativo imobilizado, quando o cálculo estiver enquadrado no Convênio ICMS 52/91. Poderá receber os valores:

* "2 - Simples";

* "9- Dupla com Aliq. Interna por dentro".

% Red. Base DIFAL

Percentual de redução da base do DIFAL. Esse campo é utilizado para os cálculos de DIFAL do tipo "12 - Dupla c/ aplicação da diferença de alíq. c/ redução de base de cálculo". Para verificar a utilização desse valor no cálculo do DIFAL acesse a documentação da tela F070FCP.

## Páginas relacionadas

* [Convênio ICMS 52/91](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/impostos-icms.htm#convenio-icms-52/91)
* [F070FCP](https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/menu_cadastros/f070fcp.htm)
