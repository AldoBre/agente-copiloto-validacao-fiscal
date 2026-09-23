"""
Cliente da API pública do Zendesk Help Center.

A central de ajuda da Senior (``suporte.senior.com.br``) roda em Zendesk, que
expõe os artigos por API REST. Usar a API em vez de raspar HTML é melhor em
tudo o que importa aqui:

* **1 requisição por 100 artigos** em vez de 1 por artigo (6 mil artigos =
  ~64 chamadas, não 6 mil);
* o corpo vem limpo, sem menu, rodapé e banner de cookie;
* vêm junto o título, a seção, a URL pública e a data de atualização —
  metadados que o scraping teria de adivinhar.

Só artigos públicos são retornados; conteúdo restrito exigiria autenticação.
"""
from __future__ import annotations

import logging
import re
import time
from dataclasses import dataclass, field
from typing import Iterator

import httpx
from bs4 import BeautifulSoup
from markdownify import markdownify

from .imagens import normalizar_markdown

logger = logging.getLogger(__name__)

CABECALHOS = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
        "AgenteImplantacaoFiscal/1.0"
    ),
    "Accept": "application/json",
}

POR_PAGINA = 100
PAUSA_ENTRE_PAGINAS = 0.2  # gentileza com o servidor de quem nos cede o conteúdo

_RE_LINHAS_VAZIAS = re.compile(r"\n{3,}")
_RE_HOST = re.compile(r"^https?://([^/]+)")


@dataclass
class ArtigoZendesk:
    id: int
    titulo: str
    url: str
    secao_id: int
    secao_nome: str
    atualizado_em: str
    markdown: str
    rotulos: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return bool(self.markdown.strip())


def _base_api(url_central: str) -> str:
    """``https://suporte.senior.com.br/hc/pt-br/...`` → base da API."""
    encontrado = _RE_HOST.match(url_central)
    if not encontrado:
        raise ValueError(f"URL inválida: {url_central}")
    host = encontrado.group(1)
    idioma = "pt-br"
    if "/hc/" in url_central:
        partes = url_central.split("/hc/", 1)[1].split("/")
        if partes and partes[0]:
            idioma = partes[0]
    return f"https://{host}/api/v2/help_center/{idioma}"


def extrair_id(url: str) -> int | None:
    """Pega o id numérico de uma URL de categoria/seção do Help Center."""
    encontrado = re.search(r"/(?:categories|sections)/(\d+)", url)
    return int(encontrado.group(1)) if encontrado else None


def _html_para_markdown(html: str, base: str = "") -> str:
    if not html:
        return ""
    sopa = BeautifulSoup(html, "lxml")
    for tag in sopa.find_all(["script", "style", "iframe", "noscript"]):
        tag.decompose()
    texto = markdownify(str(sopa), heading_style="ATX", strip=["a"])
    texto = _RE_LINHAS_VAZIAS.sub("\n\n", texto).strip()
    # Anexos do Zendesk vêm como '/attachments/token/…' — fora do site, quebram.
    texto, _, _ = normalizar_markdown(texto, base)
    return texto


class ClienteZendesk:
    def __init__(self, url_central: str, *, timeout: float = 60.0):
        self.base = _base_api(url_central)
        self._cliente = httpx.Client(
            headers=CABECALHOS, timeout=timeout, follow_redirects=True
        )
        self._secoes: dict[int, str] = {}

    def __enter__(self):
        return self

    def __exit__(self, *_):
        self._cliente.close()

    # ------------------------------------------------------------- páginas --
    def _paginar(self, caminho: str, chave: str) -> Iterator[dict]:
        pagina = 1
        while True:
            resposta = self._cliente.get(
                f"{self.base}/{caminho}", params={"per_page": POR_PAGINA, "page": pagina}
            )
            resposta.raise_for_status()
            dados = resposta.json()
            for item in dados.get(chave, []):
                yield item
            if not dados.get("next_page"):
                break
            pagina += 1
            time.sleep(PAUSA_ENTRE_PAGINAS)

    # ------------------------------------------------------------- catálogo --
    def secoes_da_categoria(self, categoria_id: int) -> list[dict]:
        secoes = list(self._paginar(f"categories/{categoria_id}/sections.json", "sections"))
        self._secoes.update({s["id"]: s["name"] for s in secoes})
        return secoes

    def contar(self, caminho: str) -> int:
        resposta = self._cliente.get(f"{self.base}/{caminho}", params={"per_page": 1})
        resposta.raise_for_status()
        return resposta.json().get("count", 0)

    def contar_categoria(self, categoria_id: int) -> int:
        return self.contar(f"categories/{categoria_id}/articles.json")

    def contar_secao(self, secao_id: int) -> int:
        return self.contar(f"sections/{secao_id}/articles.json")

    # -------------------------------------------------------------- artigos --
    def artigos(
        self,
        *,
        categoria_id: int | None = None,
        secao_id: int | None = None,
        filtro_titulo: re.Pattern | None = None,
        limite: int | None = None,
    ) -> Iterator[ArtigoZendesk]:
        """
        Itera os artigos de uma categoria ou seção.

        ``filtro_titulo`` é aplicado **antes** de converter o corpo, então
        descartar um artigo não custa processamento.
        """
        if secao_id is not None:
            caminho = f"sections/{secao_id}/articles.json"
        elif categoria_id is not None:
            caminho = f"categories/{categoria_id}/articles.json"
        else:
            raise ValueError("Informe categoria_id ou secao_id.")

        entregues = 0
        for bruto in self._paginar(caminho, "articles"):
            if bruto.get("draft"):
                continue
            titulo = (bruto.get("title") or "").strip()
            if filtro_titulo and not filtro_titulo.search(titulo):
                continue

            markdown = _html_para_markdown(bruto.get("body") or "", bruto.get("html_url") or "")
            if not markdown:
                continue

            sid = bruto.get("section_id") or 0
            yield ArtigoZendesk(
                id=bruto.get("id", 0),
                titulo=titulo[:390],
                url=bruto.get("html_url", ""),
                secao_id=sid,
                secao_nome=self._secoes.get(sid, ""),
                atualizado_em=bruto.get("updated_at", ""),
                markdown=markdown,
                rotulos=bruto.get("label_names") or [],
            )

            entregues += 1
            if limite and entregues >= limite:
                return
