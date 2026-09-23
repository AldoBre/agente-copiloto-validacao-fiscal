"""Endpoints do comparador (upload dos dois XMLs + consulta do resultado)."""
from __future__ import annotations

import logging

from django.conf import settings
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response

from .models import Comparacao, DivergenciaRegistrada
from .services import comparar_documentos, montar_relatorio_markdown, montar_resumo, parse_documento
from .services.mapa_campos import ALTA, CRITICA
from .services.parser_nfe import ErroDeParse

logger = logging.getLogger(__name__)


def _limite_bytes() -> int:
    return int(settings.COMPARADOR.get("TAMANHO_MAXIMO_XML_MB", 10)) * 1024 * 1024


def _ler_upload(arquivo, rotulo: str) -> bytes:
    if arquivo is None:
        raise ValueError(f"Envie o arquivo '{rotulo}'.")
    if arquivo.size > _limite_bytes():
        raise ValueError(
            f"O arquivo '{arquivo.name}' tem {arquivo.size / 1_048_576:.1f} MB e excede o "
            f"limite de {settings.COMPARADOR.get('TAMANHO_MAXIMO_XML_MB', 10)} MB."
        )
    return arquivo.read()


@api_view(["POST"])
@parser_classes([MultiPartParser, FormParser])
def comparar(request):
    """
    ``POST /api/comparador/comparar/``

    Campos (multipart): ``xml_cliente`` e ``xml_senior``.
    Devolve o resultado completo e persiste a comparação.
    """
    try:
        bytes_cliente = _ler_upload(request.FILES.get("xml_cliente"), "xml_cliente")
        bytes_senior = _ler_upload(request.FILES.get("xml_senior"), "xml_senior")
    except ValueError as exc:
        return Response({"erro": str(exc)}, status=status.HTTP_400_BAD_REQUEST)

    nome_cliente = request.FILES["xml_cliente"].name
    nome_senior = request.FILES["xml_senior"].name

    try:
        doc_cliente = parse_documento(bytes_cliente, origem="cliente", nome_arquivo=nome_cliente)
    except ErroDeParse as exc:
        return Response(
            {"erro": f"XML do sistema atual ({nome_cliente}): {exc}"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        doc_senior = parse_documento(bytes_senior, origem="senior", nome_arquivo=nome_senior)
    except ErroDeParse as exc:
        return Response(
            {"erro": f"XML da Senior ({nome_senior}): {exc}"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        resultado = comparar_documentos(
            doc_cliente,
            doc_senior,
            # Ver comparar_documentos: desligado, o item que o Senior não emitiu
            # deixa de virar divergência crítica.
            analisar_itens_nao_simulados=(
                request.data.get("itens_nao_simulados", "true") not in ("false", False, "0")
            ),
        )
    except Exception as exc:  # noqa: BLE001
        logger.exception("Falha ao comparar documentos")
        return Response(
            {"erro": f"Falha inesperada na comparação: {type(exc).__name__}: {exc}"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    dados = resultado.para_dicionario()
    resumo = montar_resumo(dados)
    markdown = montar_relatorio_markdown(
        dados,
        max_causas=int(settings.AGENTE.get("MAX_DIVERGENCIAS_PROMPT", 60)),
    )

    por_severidade = resumo.get("por_severidade", {})
    comparacao = Comparacao.objects.create(
        arquivo_cliente=nome_cliente,
        arquivo_senior=nome_senior,
        chave_cliente=doc_cliente.chave,
        chave_senior=doc_senior.chave,
        resumo=resumo,
        resultado=dados,
        relatorio_markdown=markdown,
        total_divergencias=resumo.get("total_divergencias", 0),
        total_criticas=por_severidade.get(CRITICA, 0),
        total_altas=por_severidade.get(ALTA, 0),
    )

    DivergenciaRegistrada.objects.bulk_create(
        [
            DivergenciaRegistrada(
                comparacao=comparacao,
                categoria=d.get("categoria", "")[:40],
                grupo=d.get("grupo", "")[:40],
                campo=d.get("campo", "")[:120],
                caminho=d.get("caminho", "")[:255],
                escopo=d.get("escopo", "item")[:20],
                tipo=d.get("tipo", "")[:40],
                severidade=d.get("severidade", "")[:10],
                valor_cliente=d.get("valor_cliente", ""),
                valor_senior=d.get("valor_senior", ""),
                diferenca=d.get("diferenca", "")[:80],
                item_numero=d.get("item_numero"),
                item_codigo=(d.get("item_codigo") or "")[:80],
                item_descricao=(d.get("item_descricao") or "")[:255],
                pista=d.get("pista", ""),
            )
            for d in dados.get("divergencias", [])
        ],
        batch_size=500,
    )

    return Response(
        {
            "comparacao_id": str(comparacao.id),
            "criado_em": comparacao.criado_em.isoformat(),
            "resumo": resumo,
            "divergencias": dados["divergencias"],
            "pareamento": dados["pareamento"],
            "avisos": dados["avisos"],
            "relatorio_markdown": markdown,
        }
    )


@api_view(["GET"])
def detalhe(request, comparacao_id):
    """``GET /api/comparador/<uuid>/`` — recupera uma comparação já feita."""
    try:
        comparacao = Comparacao.objects.get(pk=comparacao_id)
    except (Comparacao.DoesNotExist, ValueError, TypeError):
        return Response({"erro": "Comparação não encontrada."}, status=status.HTTP_404_NOT_FOUND)

    return Response(
        {
            "comparacao_id": str(comparacao.id),
            "criado_em": comparacao.criado_em.isoformat(),
            "resumo": comparacao.resumo,
            "divergencias": comparacao.resultado.get("divergencias", []),
            "pareamento": comparacao.resultado.get("pareamento", []),
            "avisos": comparacao.resultado.get("avisos", []),
            "relatorio_markdown": comparacao.relatorio_markdown,
        }
    )


@api_view(["GET"])
def historico(request):
    """``GET /api/comparador/historico/`` — últimas comparações."""
    limite = min(int(request.query_params.get("limite", 20)), 100)
    itens = Comparacao.objects.all()[:limite]
    return Response(
        [
            {
                "comparacao_id": str(c.id),
                "criado_em": c.criado_em.isoformat(),
                "arquivo_cliente": c.arquivo_cliente,
                "arquivo_senior": c.arquivo_senior,
                "total_divergencias": c.total_divergencias,
                "total_criticas": c.total_criticas,
                "total_altas": c.total_altas,
            }
            for c in itens
        ]
    )
