"""
Ranking pelo full-text search nativo do PostgreSQL.

Usa a coluna gerada ``busca`` (tsvector, migração 0004): título da seção com
peso A, corpo com peso B, ambos SEM acento via ``translate`` — ``unaccent`` é
extensão e exigiria o mesmo admin que bloqueia o pgvector; ``translate`` é
built-in e imutável, então serve para coluna gerada. O lado da consulta usa os
mesmos tokens sem acento (``tokenizar_superficie``), mantendo os dois lados
consistentes.

Os termos entram no ``to_tsquery`` unidos por ``|`` (OU): as consultas
dirigidas são frases nominais longas e exigir todos os termos (como o
``websearch_to_tsquery`` faz) devolveria vazio. O ranking OU do ``ts_rank``
não tem IDF — por isso o FTS NÃO substitui o BM25: os dois são fundidos por
RRF no retriever, cada um puxando o que o outro não vê (o FTS traz o stemming
oficial do português e escala pelo índice GIN conforme a base cresce).

Título do DOCUMENTO fica de fora da coluna gerada (não pode referenciar outra
tabela); quem o cobre é o BM25 em memória — mais um motivo para a fusão.
"""
from __future__ import annotations

import logging

from django.db import connection

from .sinonimos import SINONIMOS_SUPERFICIE
from .texto import tokenizar_superficie

logger = logging.getLogger(__name__)


def ranking_fts(consulta: str, posicao_por_id: dict[int, int], limite: int) -> list[tuple[int, float]]:
    """Devolve [(posição no índice, score)] — vazio fora do Postgres ou em erro."""
    if connection.vendor != "postgresql":
        return []

    termos = tokenizar_superficie(consulta)
    if not termos:
        return []

    # Sinônimos entram no OU; tokens são [a-z0-9_]+ (sem acento), então não há
    # como injetar operador de tsquery.
    expandidos = list(
        dict.fromkeys(
            [*termos, *(e for t in termos for e in SINONIMOS_SUPERFICIE.get(t, ()))]
        )
    )

    try:
        with connection.cursor() as cur:
            cur.execute(
                """
                SELECT id, ts_rank(busca, q, 1) AS pontuacao
                  FROM conhecimento_trecho, to_tsquery('portuguese', %s) AS q
                 WHERE busca @@ q
                 ORDER BY pontuacao DESC, id
                 LIMIT %s
                """,
                [" | ".join(expandidos), limite],
            )
            linhas = cur.fetchall()
    except Exception as exc:  # noqa: BLE001 — ex.: migração 0004 ainda não aplicada
        logger.warning("FTS indisponível (%s: %s). Seguindo sem ele.", type(exc).__name__, exc)
        return []

    return [
        (posicao_por_id[id_], float(pontuacao))
        for id_, pontuacao in linhas
        if id_ in posicao_por_id
    ]
