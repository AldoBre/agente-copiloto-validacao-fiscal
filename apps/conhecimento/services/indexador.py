"""
Indexação: transforma o markdown de um documento em trechos e, quando houver um
provedor de embeddings cadastrado, calcula os vetores.

Sem provedor de embeddings o sistema continua funcionando: a recuperação cai
para busca textual (BM25 simplificado) — pior, mas suficiente para começar.
"""
from __future__ import annotations

import logging

from django.db import transaction

from apps.provedores.factory import ProvedorIndisponivel, construir_embeddings
from apps.provedores.models import ProvedorIA, TipoModelo

from ..models import Documento, Trecho
from .chunker import dividir_em_trechos

logger = logging.getLogger(__name__)

TAMANHO_LOTE_EMBEDDING = 64


def obter_provedor_embedding() -> ProvedorIA | None:
    return ProvedorIA.obter_padrao(TipoModelo.EMBEDDING)


def _calcular_embeddings(textos: list[str], provedor: ProvedorIA) -> list[list[float]]:
    modelo = construir_embeddings(provedor)
    vetores: list[list[float]] = []
    for inicio in range(0, len(textos), TAMANHO_LOTE_EMBEDDING):
        lote = textos[inicio : inicio + TAMANHO_LOTE_EMBEDDING]
        vetores.extend(modelo.embed_documents(lote))
    return vetores


@transaction.atomic
def indexar_documento(documento: Documento, *, calcular_embeddings: bool = True) -> dict:
    """
    (Re)cria os trechos de um documento.

    Devolve ``{"trechos": n, "com_embedding": n, "aviso": str}``.
    """
    documento.trechos.all().delete()

    brutos = dividir_em_trechos(documento.conteudo)
    if not brutos:
        return {"trechos": 0, "com_embedding": 0, "aviso": "Documento sem conteúdo aproveitável."}

    trechos = [
        Trecho(
            documento=documento,
            ordem=b.ordem,
            titulo_secao=b.titulo_secao[:400],
            texto=b.texto,
        )
        for b in brutos
    ]

    aviso = ""
    com_embedding = 0

    if calcular_embeddings:
        provedor = obter_provedor_embedding()
        if provedor is None:
            aviso = (
                "Nenhum provedor de embeddings ativo. Os trechos foram salvos e a busca "
                "usará correspondência textual. Cadastre um provedor do tipo 'Embeddings' "
                "em Configurações para habilitar a busca semântica."
            )
        else:
            try:
                vetores = _calcular_embeddings([t.texto for t in trechos], provedor)
                for trecho, vetor in zip(trechos, vetores):
                    trecho.embedding = list(vetor)
                    trecho.modelo_embedding = f"{provedor.provedor}:{provedor.modelo}"
                com_embedding = len(vetores)
            except ProvedorIndisponivel as exc:
                aviso = f"Embeddings não calculados: {exc}"
            except Exception as exc:  # noqa: BLE001
                logger.exception("Falha ao calcular embeddings")
                aviso = f"Embeddings não calculados ({type(exc).__name__}: {exc})."

    Trecho.objects.bulk_create(trechos, batch_size=200)
    return {"trechos": len(trechos), "com_embedding": com_embedding, "aviso": aviso}


def documentos_pendentes():
    """
    Documentos que precisam de (re)indexação: sem trecho, sem vetor, ou com
    vetor de outro modelo.

    O último caso é o que torna a troca de modelo de embeddings retomável —
    vetores de modelos diferentes não são comparáveis, então todos precisam ser
    refeitos, e com milhares de trechos isso não cabe numa requisição só.
    """
    sem_trecho = Documento.objects.filter(trechos__isnull=True).values_list("id", flat=True)
    sem_vetor = Trecho.objects.filter(embedding__isnull=True).values_list(
        "documento_id", flat=True
    )

    ids = set(sem_trecho) | set(sem_vetor)

    provedor = obter_provedor_embedding()
    if provedor is not None:
        atual = f"{provedor.provedor}:{provedor.modelo}"
        ids |= set(
            Trecho.objects.filter(embedding__isnull=False)
            .exclude(modelo_embedding=atual)
            .values_list("documento_id", flat=True)
        )

    return Documento.objects.filter(id__in=ids)


def reindexar_tudo(
    *,
    calcular_embeddings: bool = True,
    apenas_pendentes: bool = False,
    limite: int | None = None,
) -> dict:
    """
    Reprocessa documentos. Usado após trocar o modelo de embeddings.

    ``apenas_pendentes`` pula quem já tem vetor — é o modo para completar uma
    importação. Sem ele, reprocessar uma base de milhares de trechos estoura o
    tempo de resposta do App Service (230s) e ainda recompra embeddings que já
    estavam pagos. ``limite`` fecha a conta: cada chamada faz um lote e volta,
    e o chamador repete até ``pendentes`` zerar.
    """
    consulta = documentos_pendentes() if apenas_pendentes else Documento.objects.all()
    if limite:
        consulta = consulta.order_by("id")[:limite]

    total_trechos = 0
    total_embeddings = 0
    processados = 0
    avisos: list[str] = []

    for documento in consulta.iterator():
        resultado = indexar_documento(documento, calcular_embeddings=calcular_embeddings)
        total_trechos += resultado["trechos"]
        total_embeddings += resultado["com_embedding"]
        processados += 1
        if resultado["aviso"] and resultado["aviso"] not in avisos:
            avisos.append(resultado["aviso"])

    return {
        "documentos": Documento.objects.count(),
        "processados": processados,
        "trechos": total_trechos,
        "com_embedding": total_embeddings,
        "pendentes": documentos_pendentes().count(),
        "avisos": avisos,
    }
