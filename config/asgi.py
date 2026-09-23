"""
ASGI do projeto.

O Django atende tudo, EXCETO o prefixo ``/api/ia`` — que é roteado para um
sub-app FastAPI responsável pelo streaming (SSE) do chat com o agente.

Rodar com:

    uvicorn config.asgi:application --reload

`python manage.py runserver` sobe apenas o WSGI: as telas funcionam, mas o
streaming em /api/ia/* responde 404. Use o ./run.sh.
"""
from __future__ import annotations

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

# Precisa acontecer ANTES de importar qualquer coisa que toque em models.
django_app = get_asgi_application()

from apps.agente.api import api_app  # noqa: E402

PREFIXO_IA = "/api/ia"


def _aquecer_indice() -> None:
    """
    Constrói o índice de busca no start, e não na primeira pergunta.

    O índice é montado sob demanda e fica em cache no processo. O problema é
    quem paga a construção: medido em produção, a primeira pergunta esperava
    **56 segundos** só pela recuperação — carregar 4.365 trechos do Postgres do
    Azure e tokenizá-los com stemming num worker compartilhado. Localmente o
    mesmo trabalho leva menos de um segundo, o que escondeu o problema até o
    primeiro uso real.

    Roda numa thread daemon para não atrasar o start, e cada worker aquece o
    seu (o cache é por processo). Falha aqui é irrelevante: se não aquecer, a
    primeira pergunta reconstrói como antes.
    """
    import logging
    import threading
    import time

    logger = logging.getLogger(__name__)

    def _trabalho() -> None:
        from django.db import close_old_connections

        try:
            from apps.conhecimento.services.retriever import obter_indice

            inicio = time.perf_counter()
            indice = obter_indice()
            logger.info(
                "Índice de busca aquecido no start: %s trechos em %.1fs",
                indice.total,
                time.perf_counter() - inicio,
            )
        except Exception as exc:  # noqa: BLE001
            logger.warning("Não foi possível aquecer o índice: %s", exc)
        finally:
            # A thread tem conexão própria; sem fechar, ela vaza.
            close_old_connections()

    threading.Thread(target=_trabalho, name="aquecer-indice", daemon=True).start()


_aquecer_indice()


async def application(scope, receive, send):
    if scope["type"] == "lifespan":
        # O FastAPI cuida do ciclo de vida; o Django não usa lifespan.
        await api_app(scope, receive, send)
        return

    caminho = scope.get("path", "")
    if caminho.startswith(PREFIXO_IA):
        await api_app(scope, receive, send)
        return

    await django_app(scope, receive, send)
