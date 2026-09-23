# Base de conhecimento — arquivos-fonte

Documentação da Senior exportada em markdown, **um arquivo por tópico**, para ser
revisada pela equipe antes de virar embedding.

```
base_conhecimento/<fornecedor>/<versão>/<página>/
  00-indice.md      tabela dos tópicos
  NN-<slug>.md      um tópico, com cabeçalho de procedência
  mapa.json         mapa estruturado (ver abaixo)
```

## Por que arquivo, e não ingestão direta da URL

Três motivos, em ordem de importância:

1. **A documentação é genérica; a implantação, não.** O texto da Senior descreve o
   comportamento padrão do produto. O que vale para o cliente é o que foi
   parametrizado nele. Em arquivo a equipe corrige e anota antes de indexar —
   direto da URL, o que entra na base é só o texto de fábrica.
2. **Versionado, dá para ver o que mudou.** Quando a Senior atualiza a página, o
   `git diff` mostra exatamente o que saiu e o que entrou.
3. **O corte por tópico melhora a recuperação.** "Rotinas de ICMS" é uma sanfona
   só: 25 tópicos e ~70 KB num único documento. Ingerida inteira, vira um
   documento gigante cujos trechos competem entre si — e um trecho sobre
   "Antecipação de ICMS" pode chegar ao modelo colado em "ICMS Diferido".

## Como gerar

```bash
python manage.py exportar_markdown \
    "https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/impostos-icms.htm" \
    --destino base_conhecimento/senior/5.10.4/impostos-icms --limpar
```

O comando só funciona em página montada como sanfona (MadCap Flare, que é o
formato do portal da Senior). Página comum vai direto pelo `ingerir_url`.

## Como indexar depois de revisar

Os arquivos **ainda não estão na base** — não há provedor de embeddings
cadastrado. Depois de configurar um em **Configurações → Provedores de IA**:

```bash
# a partir da URL original (o scraper já preserva os títulos dos tópicos)
python manage.py ingerir_url "https://.../impostos-icms.htm" --nome "Senior — ICMS 5.10.4"
```

Para indexar o conteúdo **revisado** em vez do original, cole cada arquivo como
fonte do tipo "Texto colado" em **Configurações → Base de conhecimento**.

## O que tem no `mapa.json`

Por tópico:

| Campo | Para que serve |
|---|---|
| `telas` | Códigos de tela/tabela citados (`F001TVE`, `E440NFC`) |
| `caminhos_menu` | Caminho completo quando a página informa (`Cadastros > … (F070EMP)`) |
| `identificadores_regras` | `VEN-000ALICM01` e afins |
| `campos_xml_citados` | Campos que **o comparador sabe reportar** e que aparecem no tópico |
| `links_documentacao` | Páginas para as quais o tópico aponta |
| `ancora` / `url` | Link direto para o tópico na documentação |

`campos_xml_citados` é a ponte entre as duas metades do sistema: liga a
divergência que o comparador aponta (`vICMSDeson`, `motDesICMS`, `CST`) ao tópico
da documentação que explica onde aquilo é parametrizado. É o insumo natural para
refinar as `RegraParametrizacao` do `/admin` com nomes de rotina reais, em vez das
orientações por conceito que o `seed_regras` traz.

`paginas_relacionadas`, no fim do arquivo, é a fila do próximo passo: as páginas
que esta referencia e que ainda não foram exportadas.
