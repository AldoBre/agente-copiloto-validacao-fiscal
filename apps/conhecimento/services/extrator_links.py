"""
Extração de URLs de um arquivo (.docx, .txt, .md, .html) ou de texto colado.

O consultor costuma receber a lista de documentação como um Word com os links
em hiperlink — onde o texto visível é o título da página e a URL só existe na
relação de relacionamentos do .docx. Ler só o texto perderia tudo.
"""
from __future__ import annotations

import re
import zipfile
from pathlib import Path

_RE_URL = re.compile(r"https?://[^\s<>\"'\)\]]+")
_RE_ALVO_DOCX = re.compile(r'Target="(https?://[^"]+)"')


def _limpar(url: str) -> str:
    return url.rstrip(".,;:)]}> ").strip()


def _ordenar_unicos(urls: list[str]) -> list[str]:
    vistos: set[str] = set()
    saida: list[str] = []
    for url in urls:
        url = _limpar(url)
        if url and url not in vistos:
            vistos.add(url)
            saida.append(url)
    return saida


def extrair_de_texto(texto: str) -> list[str]:
    return _ordenar_unicos(_RE_URL.findall(texto or ""))


def extrair_de_docx(caminho: str | Path) -> list[str]:
    """
    Lê os hiperlinks de um .docx.

    Um .docx é um ZIP: o texto fica em ``word/document.xml`` e o destino dos
    hiperlinks em ``word/_rels/document.xml.rels``. Pegamos os dois — links
    escritos como texto puro não aparecem no .rels.
    """
    caminho = Path(caminho)
    urls: list[str] = []

    with zipfile.ZipFile(caminho) as pacote:
        try:
            rels = pacote.read("word/_rels/document.xml.rels").decode("utf-8", "ignore")
            urls.extend(_RE_ALVO_DOCX.findall(rels))
        except KeyError:
            pass
        try:
            documento = pacote.read("word/document.xml").decode("utf-8", "ignore")
            texto = re.sub(r"<[^>]+>", " ", documento)
            urls.extend(_RE_URL.findall(texto))
        except KeyError:
            pass

    return _ordenar_unicos(urls)


def extrair_de_arquivo(caminho: str | Path) -> list[str]:
    """Detecta o formato pela extensão e extrai as URLs."""
    caminho = Path(caminho)
    if not caminho.is_file():
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")

    if caminho.suffix.lower() == ".docx":
        return extrair_de_docx(caminho)
    if caminho.suffix.lower() in (".txt", ".md", ".csv", ".html", ".htm", ".xml"):
        return extrair_de_texto(caminho.read_text(encoding="utf-8", errors="ignore"))

    raise ValueError(
        f"Formato não suportado: {caminho.suffix}. Use .docx, .txt, .md, .csv ou .html."
    )
