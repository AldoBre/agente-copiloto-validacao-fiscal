"""Endpoints da base de conhecimento (fontes, ingestão, reindexação, regras)."""
from __future__ import annotations

import logging

from django.db.models import Count, Q
from django.utils import timezone
from rest_framework import status, viewsets
from rest_framework.decorators import action, api_view
from rest_framework.response import Response

from apps.provedores.models import ProvedorIA, TipoModelo

from .models import (
    Documento,
    FonteConhecimento,
    RegraParametrizacao,
    TarefaIndexacao,
    TipoFonte,
    Trecho,
)
from .serializers import (
    DocumentoSerializer,
    FonteConhecimentoSerializer,
    RegraParametrizacaoSerializer,
)
from .services.indexador import documentos_pendentes, indexar_documento
from .services.tarefas import iniciar_reindexacao, tarefa_ativa
from .services.extrator_links import extrair_de_texto
from .services.scraper import raspar_url, resolver_url

logger = logging.getLogger(__name__)


def _ingerir_conteudo(fonte: FonteConhecimento, titulo: str, url: str, markdown: str) -> dict:
    hash_conteudo = Documento.calcular_hash(markdown)
    documento, criado = Documento.objects.update_or_create(
        fonte=fonte,
        hash_conteudo=hash_conteudo,
        defaults={"titulo": titulo[:400], "url": url[:1000], "conteudo": markdown},
    )
    resultado = indexar_documento(documento)
    resultado["documento_id"] = documento.pk
    resultado["titulo"] = documento.titulo
    resultado["novo"] = criado
    return resultado


class FonteConhecimentoViewSet(viewsets.ModelViewSet):
    queryset = FonteConhecimento.objects.all()
    serializer_class = FonteConhecimentoSerializer

    @action(detail=True, methods=["post"])
    def ingerir(self, request, pk=None):
        """
        Dispara a ingestão da fonte.

        * tipo ``url``   → faz scraping (opcionalmente seguindo links internos)
        * tipo ``texto`` → espera ``{"titulo": ..., "conteudo": ...}`` no corpo
        """
        fonte = self.get_object()
        detalhes: list[dict] = []
        erros: list[str] = []

        if fonte.tipo == TipoFonte.LISTA:
            urls = [resolver_url(u) for u in (fonte.urls or []) if u]
            if not urls:
                return Response(
                    {"erro": "A fonte não possui nenhuma URL na lista."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            for url in urls:
                paginas = raspar_url(url)
                pagina = paginas[0] if paginas else None
                if pagina is None or not pagina.ok:
                    erros.append(
                        f"{url}: {(pagina.erro if pagina else '') or 'conteúdo vazio'}"
                    )
                    continue
                detalhes.append(
                    _ingerir_conteudo(fonte, pagina.titulo, pagina.url, pagina.markdown)
                )

        elif fonte.tipo == TipoFonte.URL:
            if not fonte.url:
                return Response(
                    {"erro": "A fonte não possui URL cadastrada."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            paginas = raspar_url(
                fonte.url,
                seguir_links=fonte.seguir_links,
                profundidade_max=fonte.profundidade_max,
            )
            for pagina in paginas:
                if not pagina.ok:
                    erros.append(f"{pagina.url}: {pagina.erro or 'conteúdo vazio'}")
                    continue
                detalhes.append(
                    _ingerir_conteudo(fonte, pagina.titulo, pagina.url, pagina.markdown)
                )
        else:
            conteudo = (request.data.get("conteudo") or "").strip()
            titulo = (request.data.get("titulo") or fonte.nome).strip()
            if not conteudo:
                return Response(
                    {"erro": "Envie 'conteudo' com o texto a ser indexado."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            detalhes.append(_ingerir_conteudo(fonte, titulo, fonte.url, conteudo))

        total_trechos = sum(d.get("trechos", 0) for d in detalhes)
        avisos = sorted({d["aviso"] for d in detalhes if d.get("aviso")})

        fonte.ultima_ingestao_em = timezone.now()
        fonte.ultima_ingestao_ok = bool(detalhes) and not erros
        fonte.ultima_ingestao_detalhe = (
            f"{len(detalhes)} documento(s), {total_trechos} trecho(s)."
            + (f" Erros: {'; '.join(erros[:5])}" if erros else "")
        )
        fonte.save(
            update_fields=["ultima_ingestao_em", "ultima_ingestao_ok", "ultima_ingestao_detalhe"]
        )

        return Response(
            {
                "documentos_processados": len(detalhes),
                "trechos": total_trechos,
                "detalhes": detalhes,
                "erros": erros,
                "avisos": avisos,
                "fonte": self.get_serializer(fonte).data,
            }
        )


class DocumentoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Documento.objects.select_related("fonte").all()
    serializer_class = DocumentoSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        fonte = self.request.query_params.get("fonte")
        if fonte:
            qs = qs.filter(fonte_id=fonte)
        return qs


class RegraParametrizacaoViewSet(viewsets.ModelViewSet):
    queryset = RegraParametrizacao.objects.all()
    serializer_class = RegraParametrizacaoSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        busca = self.request.query_params.get("q")
        if busca:
            qs = qs.filter(
                Q(campo__icontains=busca)
                | Q(area__icontains=busca)
                | Q(orientacao__icontains=busca)
            )
        return qs


@api_view(["GET"])
def status_base(request):
    """Resumo do estado da base — alimenta os cards da tela de configurações."""
    total_trechos = Trecho.objects.count()
    com_embedding = Trecho.objects.filter(embedding__isnull=False).count()
    provedor_embedding = ProvedorIA.obter_padrao(TipoModelo.EMBEDDING)
    provedor_chat = ProvedorIA.obter_padrao(TipoModelo.CHAT)

    return Response(
        {
            "fontes": FonteConhecimento.objects.count(),
            "fontes_ativas": FonteConhecimento.objects.filter(ativo=True).count(),
            "documentos": Documento.objects.count(),
            "trechos": total_trechos,
            "trechos_com_embedding": com_embedding,
            "regras": RegraParametrizacao.objects.count(),
            "busca_semantica_ativa": bool(provedor_embedding and com_embedding),
            "provedor_embedding": provedor_embedding.nome if provedor_embedding else None,
            "provedor_chat": provedor_chat.nome if provedor_chat else None,
            "por_fonte": list(
                FonteConhecimento.objects.annotate(qtd=Count("documentos")).values(
                    "id", "nome", "qtd"
                )
            ),
        }
    )


@api_view(["POST"])
def reindexar(request):
    """
    ``POST /api/conhecimento/reindexar/`` — abre a reindexação em SEGUNDO PLANO
    e responde na hora com o estado da tarefa.

    Milhares de trechos não cabem nos 230s de uma requisição do App Service: a
    versão síncrona devolvia 504 enquanto o servidor seguia trabalhando às
    cegas. Acompanhe por ``GET /api/conhecimento/reindexar/``.

    Se já houver tarefa rodando, devolve a existente (202) em vez de abrir
    outra — duas em paralelo brigariam pelos mesmos documentos e comprariam os
    embeddings duas vezes.
    """
    try:
        tarefa, criada = iniciar_reindexacao()
    except Exception as exc:  # noqa: BLE001
        logger.exception("Falha ao iniciar a reindexação")
        return Response(
            {"erro": f"{type(exc).__name__}: {exc}"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    dados = tarefa.para_dicionario()
    dados["ja_estava_rodando"] = not criada
    return Response(dados, status=status.HTTP_202_ACCEPTED)


@api_view(["GET"])
def progresso_reindexacao(request):
    """``GET /api/conhecimento/reindexar/`` — estado da reindexação mais recente."""
    tarefa = TarefaIndexacao.objects.order_by("-criado_em").first()
    if tarefa is None:
        return Response({"estado": "nenhuma", "pendentes": documentos_pendentes().count()})

    dados = tarefa.para_dicionario()
    # Tarefa "rodando" sem batida de coração é tarefa cujo worker morreu (deploy,
    # reciclagem do container). Reportar como interrompida em vez de deixar a
    # barra girando para sempre.
    if tarefa.estado == TarefaIndexacao.Estado.RODANDO and tarefa_ativa() is None:
        dados["estado"] = "interrompida"
    return Response(dados)


@api_view(["POST"])
def buscar(request):
    """Busca manual na base — útil para o consultor validar a qualidade do RAG."""
    from .services.retriever import buscar_contexto

    consulta = (request.data.get("consulta") or "").strip()
    if not consulta:
        return Response({"erro": "Informe 'consulta'."}, status=status.HTTP_400_BAD_REQUEST)
    top_k = min(int(request.data.get("top_k", 6)), 20)
    resultados = buscar_contexto(consulta, top_k=top_k)
    return Response({"resultados": [r.para_dicionario() for r in resultados]})
