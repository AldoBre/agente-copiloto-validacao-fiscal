"""
Normalização das imagens do conteúdo ingerido.

As capturas de tela da documentação valem mais que qualquer descrição — mostrar
o print da tela F009PPE com o campo destacado é melhor do que descrever onde ele
fica. Mas, do jeito que saem da conversão HTML → markdown, elas não servem:

* **Zendesk** referencia anexos por caminho absoluto do site
  (``/attachments/token/…``): fora do site, quebram. São **1.723** na base.
* **MadCap Flare** (a documentação oficial) usa caminhos relativos ao arquivo
  (``../resources/images/icms/monofasico/…``), que dependem da URL de origem.
* O mesmo Flare enfia **227** ``transparent.gif`` do próprio tema — são os
  ícones de sanfona ("Closed"), não têm conteúdo nenhum e virariam quadradinhos
  quebrados no chat.
* Seis URLs saíram com o host duplicado (``https://host/https://host/…``),
  resíduo da resolução de caminho na ingestão.

Aqui tudo isso é resolvido para URL absoluta, e o que é decoração é descartado.
"""
from __future__ import annotations

import re
from urllib.parse import urljoin, urlparse

#: ``![alt](url)`` — captura alt e url separadamente para poder reescrever a url.
RE_IMAGEM = re.compile(r"!\[([^\]]*)\]\(([^)\s]+)(\s+\"[^\"]*\")?\)")

#: Host repetido no começo da URL: ``https://a/https://a/x`` → ``https://a/x``.
_RE_HOST_DUPLICADO = re.compile(r"^https?://[^/]+/(https?://)")

#: Imagens que são tema/ícone da ferramenta de documentação, não conteúdo.
_RE_DECORATIVA = re.compile(
    r"(Skins/[^)]*|transparent\.gif|spacer\.gif|/blank\.(gif|png))$", re.IGNORECASE
)


def e_decorativa(url: str) -> bool:
    return bool(_RE_DECORATIVA.search(url.split("?")[0]))


def normalizar_url(url: str, base: str) -> str:
    """URL de imagem → absoluta, resolvida contra a página de origem."""
    url = (url or "").strip()
    if not url or url.startswith("data:"):
        return url

    duplicado = _RE_HOST_DUPLICADO.match(url)
    if duplicado:
        url = url[duplicado.start(1) :]

    if url.startswith(("http://", "https://")):
        return url

    if not base:
        return url

    if url.startswith("//"):
        return f"{urlparse(base).scheme or 'https'}:{url}"

    # urljoin resolve tanto '/attachments/…' (raiz do host) quanto '../resources/…'
    # (relativo ao arquivo), que é exatamente a diferença entre Zendesk e Flare.
    return urljoin(base, url)


def normalizar_markdown(texto: str, base: str) -> tuple[str, int, int]:
    """
    Reescreve as imagens de um markdown.

    Devolve ``(texto, normalizadas, descartadas)``.
    """
    if not texto:
        return texto, 0, 0

    normalizadas = descartadas = 0

    def trocar(encontrado: re.Match) -> str:
        nonlocal normalizadas, descartadas
        alt, url, titulo = encontrado.group(1), encontrado.group(2), encontrado.group(3) or ""
        if e_decorativa(url):
            descartadas += 1
            return ""
        nova = normalizar_url(url, base)
        if nova != url:
            normalizadas += 1
        return f"![{alt}]({nova}{titulo})"

    saida = RE_IMAGEM.sub(trocar, texto)
    # A remoção de decorativas deixa linhas só com espaço — o chunker as trataria
    # como conteúdo.
    saida = re.sub(r"\n[ \t]+\n", "\n\n", saida)
    saida = re.sub(r"\n{3,}", "\n\n", saida)
    return saida, normalizadas, descartadas


def urls_de_imagem(texto: str) -> list[str]:
    """URLs de imagem reais (não decorativas) presentes num texto."""
    return [
        u for _alt, u, _t in RE_IMAGEM.findall(texto or "")
        if u.startswith(("http://", "https://")) and not e_decorativa(u)
    ]


#: Como o print aparece no contexto do modelo e na resposta dele.
RE_MARCADOR = re.compile(r"\[\[print:(\d+)\]\]")


def trocar_por_marcadores(texto: str, registro: dict[str, str]) -> tuple[str, list[str]]:
    """
    Troca ``![alt](url)`` por ``[[print:N]]`` e registra ``N → url``.

    **Por que não mandar a URL para o modelo copiar.** Foi a primeira tentativa
    e falhou duas vezes seguidas com o GPT-4o: instruído a colar a marcação
    exata, ele simplesmente não colava — havia 8 prints disponíveis nos trechos
    e a resposta saiu sem nenhum. Transcrever 90 caracteres opacos
    (``.../attachments/token/5wSArl9yWpEcpNqtHuO7fa5C5/?name=…``) é caro em
    tokens de saída e frágil: um caractere errado e a imagem quebra.

    Com marcador o custo vira ~4 tokens, e a integridade deixa de depender do
    modelo: ``[[print:3]]`` só vira ``<img>`` se o 3 existir no registro que o
    servidor montou. Marcador inventado não renderiza nada — não há URL a
    forjar.

    ``registro`` é mutado de propósito: a numeração é **global à resposta**, não
    por trecho, senão dois trechos teriam ambos um ``print:1``.
    """
    if not texto:
        return texto, []

    usados: list[str] = []

    def trocar(encontrado: re.Match) -> str:
        url = encontrado.group(2)
        if not url.startswith(("http://", "https://")) or e_decorativa(url):
            return ""
        chave = next((k for k, v in registro.items() if v == url), None)
        if chave is None:
            chave = str(len(registro) + 1)
            registro[chave] = url
        usados.append(chave)
        return f"[[print:{chave}]]"

    return RE_IMAGEM.sub(trocar, texto), usados
