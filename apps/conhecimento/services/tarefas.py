"""
Reindexação em segundo plano.

Uma base com milhares de trechos não cabe nos 230s que o App Service dá para
uma requisição: a chamada direta devolvia 504 enquanto o servidor seguia
trabalhando às cegas. Aqui a requisição só **abre** a tarefa e volta na hora; o
progresso é gravado no banco a cada lote e o front acompanha por polling.

Thread em vez de fila (Celery/RQ): não há broker na infra, e o trabalho é
raro — reindexar é operação de manutenção, não caminho de request. A tarefa é
retomável, então o pior caso de um container reciclado no meio é ter que
disparar de novo.
"""
from __future__ import annotations

import logging
import threading

from django.db import close_old_connections
from django.utils import timezone

from apps.conhecimento.models import TarefaIndexacao

logger = logging.getLogger(__name__)

#: Documentos por lote. Pequeno o bastante para o progresso andar visivelmente.
TAMANHO_LOTE = 25
#: Sem batida de coração por este tempo, a tarefa é considerada morta.
SEGUNDOS_ATE_ORFA = 180


def tarefa_ativa() -> TarefaIndexacao | None:
    """Tarefa rodando de verdade — ignora as que ficaram órfãs."""
    limite = timezone.now() - timezone.timedelta(seconds=SEGUNDOS_ATE_ORFA)
    return (
        TarefaIndexacao.objects.filter(
            estado=TarefaIndexacao.Estado.RODANDO, atualizado_em__gte=limite
        )
        .order_by("-criado_em")
        .first()
    )


def _executar(tarefa_id: int) -> None:
    from .indexador import documentos_pendentes, indexar_documento

    try:
        tarefa = TarefaIndexacao.objects.get(pk=tarefa_id)
    except TarefaIndexacao.DoesNotExist:
        return

    avisos: list[str] = []
    try:
        while True:
            lote = list(documentos_pendentes().order_by("id")[:TAMANHO_LOTE])
            if not lote:
                break

            for documento in lote:
                resultado = indexar_documento(documento)
                tarefa.processados += 1
                tarefa.trechos += resultado["trechos"]
                tarefa.com_embedding += resultado["com_embedding"]
                if resultado["aviso"] and resultado["aviso"] not in avisos:
                    avisos.append(resultado["aviso"])

            tarefa.pendentes = documentos_pendentes().count()
            tarefa.mensagem = " · ".join(avisos)
            tarefa.save(
                update_fields=[
                    "processados", "trechos", "com_embedding", "pendentes",
                    "mensagem", "atualizado_em",
                ]
            )

            # Sem provedor de embeddings, o laço continuaria eternamente: os
            # documentos seguem "pendentes" porque nunca ganham vetor.
            if avisos and tarefa.com_embedding == 0:
                break

        tarefa.estado = TarefaIndexacao.Estado.CONCLUIDA
        tarefa.pendentes = documentos_pendentes().count()
        tarefa.save(update_fields=["estado", "pendentes", "atualizado_em"])

    except Exception as exc:  # noqa: BLE001
        logger.exception("Falha na reindexação em segundo plano")
        tarefa.estado = TarefaIndexacao.Estado.ERRO
        tarefa.mensagem = f"{type(exc).__name__}: {exc}"
        tarefa.save(update_fields=["estado", "mensagem", "atualizado_em"])
    finally:
        # A thread tem sua própria conexão; sem isto ela vaza a cada execução.
        close_old_connections()


def iniciar_reindexacao() -> tuple[TarefaIndexacao, bool]:
    """
    Abre a tarefa e devolve ``(tarefa, criada)``.

    Se já houver uma rodando, devolve a existente em vez de começar outra —
    duas reindexações concorrentes brigariam pelos mesmos documentos e
    comprariam os embeddings duas vezes.
    """
    from .indexador import documentos_pendentes

    existente = tarefa_ativa()
    if existente is not None:
        return existente, False

    tarefa = TarefaIndexacao.objects.create(total_inicial=documentos_pendentes().count())
    threading.Thread(target=_executar, args=(tarefa.pk,), daemon=True).start()
    return tarefa, True
