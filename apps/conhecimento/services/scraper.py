"""
Scraping da documentação de parametrização fiscal da Senior.

Recebe uma URL, baixa o HTML, remove navegação/scripts e devolve markdown.
Opcionalmente segue links internos do mesmo domínio (útil para índices de
documentação, onde a página inicial só lista os tópicos).

Nada aqui é específico da Senior: qualquer portal de documentação funciona.
Se no futuro a documentação vier por um MCP, basta trocar esta camada — a
interface com o resto do sistema é ``raspar_url() -> [ResultadoScraping]``.
"""
from __future__ import annotations

import logging
import re
from dataclasses import dataclass, field
from urllib.parse import unquote, urldefrag, urljoin, urlparse

import httpx
from bs4 import BeautifulSoup
from markdownify import markdownify

from .imagens import normalizar_markdown

logger = logging.getLogger(__name__)


# --------------------------------------------------------------------------- #
#  Resolução de URL de portais de ajuda
# --------------------------------------------------------------------------- #
def resolver_url(url: str) -> str:
    """
    Converte a URL de navegação de um portal de ajuda na URL do **conteúdo**.

    Portais gerados por MadCap Flare & cia. — o da Senior entre eles — servem
    uma casca SPA e põem a página real depois do ``#``:

        .../5.10.4/#geral/impostos-icms.htm?TocPath=Segmentos|Compliance|…
        .../5.10.4/geral/impostos-icms.htm                     ← conteúdo real

    Como o navegador nunca envia o fragmento ao servidor, baixar a URL original
    devolve só o esqueleto de navegação. O sintoma é traiçoeiro: HTTP 200,
    algum HTML e um texto minúsculo de placeholder — o scraper "funciona" e a
    base fica cheia de menu.

    Também remove o ``TocPath`` (posição na árvore, não afeta o conteúdo) e a
    âncora interna (a página inteira é indexada de qualquer forma).
    """
    if "#" not in url:
        return url

    base, fragmento = url.split("#", 1)
    fragmento = unquote(fragmento).split("?", 1)[0].split("#", 1)[0].strip()

    # Fragmento que não aponta para um documento é âncora comum — mantém a URL.
    if not fragmento or not re.search(r"\.(html?|aspx?|php)$", fragmento, re.IGNORECASE):
        return base or url

    return urljoin(base, fragmento.lstrip("/"))

TAGS_RUIDO = (
    "script",
    "style",
    "noscript",
    "nav",
    "header",
    "footer",
    "aside",
    "form",
    "iframe",
    "svg",
    "button",
)

SELETORES_CONTEUDO = (
    "#mc-main-content",   # MadCap Flare (portal da Senior)
    "main",
    "article",
    "[role=main]",
    ".content",
    "#content",
    ".documentation",
    ".markdown-body",
    ".article-body",
    ".doc-content",
)

CABECALHOS = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
        "AgenteImplantacaoFiscal/1.0"
    ),
    "Accept-Language": "pt-BR,pt;q=0.9",
}

_RE_LINHAS_VAZIAS = re.compile(r"\n{3,}")

#: Abaixo disso a página quase certamente é casca de SPA, não conteúdo.
TAMANHO_MINIMO_SUSPEITO = 400


@dataclass
class ResultadoScraping:
    url: str
    titulo: str
    markdown: str
    links_internos: list[str] = field(default_factory=list)
    erro: str = ""

    @property
    def ok(self) -> bool:
        return not self.erro and bool(self.markdown.strip())


def _extrair_titulo(sopa: BeautifulSoup, url: str) -> str:
    for seletor in ("h1", "title"):
        elemento = sopa.select_one(seletor)
        if elemento and elemento.get_text(strip=True):
            return elemento.get_text(strip=True)[:390]
    return urlparse(url).path.strip("/").replace("/", " › ") or url


def _bloco_principal(sopa: BeautifulSoup):
    for seletor in SELETORES_CONTEUDO:
        bloco = sopa.select_one(seletor)
        if bloco and len(bloco.get_text(strip=True)) > 200:
            return bloco
    return sopa.body or sopa


def _promover_dropdowns(sopa: BeautifulSoup) -> int:
    """
    Converte tópico recolhível do MadCap Flare em cabeçalho markdown real.

    O portal da Senior monta cada tópico como ``<span class="MCDropDownHead">``
    seguido de ``<div class="MCDropDownBody">`` — visualmente é um título, mas no
    HTML não é ``<h2>``. Sem esta conversão o título vira um parágrafo solto no
    markdown e o efeito aparece só lá na frente, no RAG: a página de ICMS tem 25
    tópicos e ~70 KB, mas gera só 17 seções. O chunker então corta por tamanho no
    meio do assunto e o trecho chega ao modelo sem dizer de qual tópico veio —
    "Antecipação de ICMS" e "ICMS Diferido" acabam no mesmo trecho.

    O nível do cabeçalho vem do aninhamento: tópico → subtópico → exemplo.
    """
    promovidos = 0
    for cabecalho in sopa.select(".MCDropDownHead"):
        titulo = cabecalho.get_text(" ", strip=True)
        if not titulo:
            continue
        # O próprio .MCDropDown do cabeçalho conta, então o topo já vale 1 → h2.
        profundidade = len(cabecalho.find_parents(class_="MCDropDown"))
        novo = sopa.new_tag(f"h{min(max(profundidade, 1) + 1, 6)}")
        novo.string = titulo
        cabecalho.replace_with(novo)
        promovidos += 1
    return promovidos


def _links_internos(sopa: BeautifulSoup, url_base: str) -> list[str]:
    dominio = urlparse(url_base).netloc
    vistos: list[str] = []
    for ancora in sopa.find_all("a", href=True):
        destino = urljoin(url_base, ancora["href"])
        destino, _ = urldefrag(destino)
        if urlparse(destino).netloc != dominio:
            continue
        if destino.lower().endswith((".pdf", ".zip", ".png", ".jpg", ".jpeg", ".gif", ".svg")):
            continue
        if destino not in vistos:
            vistos.append(destino)
    return vistos


def _html_para_markdown(html: str, url: str) -> ResultadoScraping:
    sopa = BeautifulSoup(html, "lxml")
    titulo = _extrair_titulo(sopa, url)
    links = _links_internos(sopa, url)
    _promover_dropdowns(sopa)

    for tag in sopa.find_all(TAGS_RUIDO):
        tag.decompose()

    bloco = _bloco_principal(sopa)
    markdown = markdownify(str(bloco), heading_style="ATX", strip=["a"])
    markdown = _RE_LINHAS_VAZIAS.sub("\n\n", markdown).strip()
    # A documentação oficial (MadCap Flare) referencia print por caminho relativo
    # ao arquivo e enche o texto de ícone do próprio tema — ver imagens.py.
    markdown, _, _ = normalizar_markdown(markdown, url)

    return ResultadoScraping(url=url, titulo=titulo, markdown=markdown, links_internos=links)


def raspar_url(
    url: str,
    *,
    seguir_links: bool = False,
    profundidade_max: int = 1,
    limite_paginas: int = 40,
    timeout: float = 30.0,
) -> list[ResultadoScraping]:
    """
    Baixa a URL (e opcionalmente seus links internos) e devolve os conteúdos.

    Erros de rede não levantam exceção: viram um :class:`ResultadoScraping` com
    ``erro`` preenchido, para a tela mostrar o que falhou.
    """
    resultados: list[ResultadoScraping] = []
    visitadas: set[str] = set()
    fila: list[tuple[str, int]] = [(resolver_url(url), 0)]

    with httpx.Client(
        headers=CABECALHOS, timeout=timeout, follow_redirects=True, http2=False
    ) as cliente:
        while fila and len(resultados) < limite_paginas:
            atual, profundidade = fila.pop(0)
            atual, _ = urldefrag(resolver_url(atual))
            if atual in visitadas:
                continue
            visitadas.add(atual)

            try:
                resposta = cliente.get(atual)
                resposta.raise_for_status()
            except Exception as exc:  # noqa: BLE001
                logger.warning("Falha ao baixar %s: %s", atual, exc)
                resultados.append(
                    ResultadoScraping(url=atual, titulo=atual, markdown="", erro=str(exc))
                )
                continue

            tipo = resposta.headers.get("content-type", "")
            if "html" not in tipo and "xml" not in tipo:
                resultados.append(
                    ResultadoScraping(
                        url=atual,
                        titulo=atual,
                        markdown="",
                        erro=f"Content-Type não suportado: {tipo}",
                    )
                )
                continue

            resultado = _html_para_markdown(resposta.text, atual)
            if resultado.ok and len(resultado.markdown) < TAMANHO_MINIMO_SUSPEITO:
                resultado.erro = (
                    f"Conteúdo muito curto ({len(resultado.markdown)} caracteres). "
                    "Provável casca de página renderizada por JavaScript — o conteúdo "
                    "real não veio no HTML."
                )
            resultados.append(resultado)

            if seguir_links and profundidade < profundidade_max:
                for link in resultado.links_internos:
                    destino = resolver_url(link)
                    if destino not in visitadas:
                        fila.append((destino, profundidade + 1))

    return resultados
