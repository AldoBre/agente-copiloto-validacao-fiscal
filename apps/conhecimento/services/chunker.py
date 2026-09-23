"""
Divisão de documentos em trechos para RAG.

Estratégia: quebra primeiro por cabeçalho markdown (para não misturar assuntos),
depois por tamanho com sobreposição. Cada trecho carrega o título da seção — o
que melhora bastante a citação de fonte na resposta do agente.
"""
from __future__ import annotations

import re
from dataclasses import dataclass

TAMANHO_PADRAO = 1200
SOBREPOSICAO_PADRAO = 150

_RE_CABECALHO = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.MULTILINE)


@dataclass
class TrechoBruto:
    ordem: int
    titulo_secao: str
    texto: str


def _separar_por_secao(markdown: str) -> list[tuple[str, str]]:
    """Devolve ``[(titulo_secao, corpo), ...]`` preservando a ordem."""
    marcas = list(_RE_CABECALHO.finditer(markdown))
    if not marcas:
        return [("", markdown)]

    secoes: list[tuple[str, str]] = []
    preambulo = markdown[: marcas[0].start()].strip()
    if preambulo:
        secoes.append(("", preambulo))

    for indice, marca in enumerate(marcas):
        titulo = marca.group(2).strip()
        inicio = marca.end()
        fim = marcas[indice + 1].start() if indice + 1 < len(marcas) else len(markdown)
        corpo = markdown[inicio:fim].strip()
        if corpo:
            secoes.append((titulo, corpo))
    return secoes


def _quebrar_por_tamanho(texto: str, tamanho: int, sobreposicao: int) -> list[str]:
    if len(texto) <= tamanho:
        return [texto]

    partes: list[str] = []
    inicio = 0
    while inicio < len(texto):
        fim = min(inicio + tamanho, len(texto))
        if fim < len(texto):
            # Tenta cortar num limite natural (parágrafo → frase → espaço).
            for separador in ("\n\n", ". ", "\n", " "):
                corte = texto.rfind(separador, inicio + tamanho // 2, fim)
                if corte != -1:
                    fim = corte + len(separador)
                    break
        parte = texto[inicio:fim].strip()
        if parte:
            partes.append(parte)
        if fim >= len(texto):
            break
        inicio = max(fim - sobreposicao, inicio + 1)
    return partes


def dividir_em_trechos(
    markdown: str,
    *,
    tamanho: int = TAMANHO_PADRAO,
    sobreposicao: int = SOBREPOSICAO_PADRAO,
    minimo: int = 80,
) -> list[TrechoBruto]:
    """Divide o markdown em trechos prontos para virar :class:`Trecho`."""
    trechos: list[TrechoBruto] = []
    ordem = 0

    for titulo, corpo in _separar_por_secao(markdown or ""):
        for parte in _quebrar_por_tamanho(corpo, tamanho, sobreposicao):
            if len(parte.strip()) < minimo:
                continue
            texto = f"## {titulo}\n\n{parte}" if titulo else parte
            trechos.append(TrechoBruto(ordem=ordem, titulo_secao=titulo, texto=texto))
            ordem += 1

    return trechos
