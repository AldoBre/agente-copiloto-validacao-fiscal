"""
Endpoints da comparação **em massa** (N notas × N notas).

Fluxo pensado para o consultor:

    1. envia os dois conjuntos (ZIP ou vários .xml)   → POST  lotes/parear/
    2. confere/ajusta o pareamento na tela            → POST  lotes/<id>/repartear/
    3. compara em blocos, com barra de progresso      → POST  lotes/<id>/comparar/
    4. consolida e manda para o agente                → POST  lotes/<id>/consolidar/

A comparação é fatiada em blocos porque 100 pares num único request travariam a
resposta e não dariam progresso. Cada bloco é independente: se um par falhar, o
erro fica registrado nele e o lote segue.
"""
from __future__ import annotations

import logging
import shutil
from pathlib import Path

from django.conf import settings
from django.http import HttpResponse
from django.db import transaction
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response

from .models import Comparacao, DivergenciaRegistrada, Lote, ParDocumentos
from .services.arquivos import ErroDeExtracao, receber_conjunto
from .services.comparador import comparar_documentos
from .services.mapa_campos import ALTA, CRITICA
from .services.pareador import montar_assinatura, parear
from .services.parser_nfe import ErroDeParse, parse_documento
from .services.relatorio_lote import agregar_lote, montar_relatorio_lote_markdown

logger = logging.getLogger(__name__)

TAMANHO_BLOCO_PADRAO = 5

MSG_LOTE_SUMIU = (
    "Lote não encontrado. Ele deixa de existir se o serviço foi reiniciado com um banco "
    "novo, se o lote foi apagado ou se a pasta de mídia foi limpa. Envie os arquivos "
    "novamente para criar um lote novo."
)


# --------------------------------------------------------------------------- #
#  Helpers
# --------------------------------------------------------------------------- #
def _raiz_lote(lote_id) -> Path:
    return Path(settings.MEDIA_ROOT) / "lotes" / str(lote_id)


def _caminho(lote_id, lado: str, nome_arquivo: str) -> Path:
    # ``nome_arquivo`` já foi normalizado para basename na extração; ainda assim
    # reaplicamos o basename para não confiar no que veio do cliente HTTP.
    return _raiz_lote(lote_id) / lado / Path(nome_arquivo).name


@api_view(["GET"])
def xml_do_lote(request, lote_id, lado: str, nome_arquivo: str):
    """
    ``GET /api/comparador/lotes/<id>/xml/<lado>/<arquivo>`` — o XML como veio.

    Existe para o pareamento manual: na lista de notas sem par, o que identifica
    o arquivo costuma ser a chave de acesso de 44 dígitos, e com dezenas de
    notas não dá para saber qual é qual. Abrir o XML resolve a dúvida sem sair
    da tela.

    Devolve o arquivo cru, sem reprocessar: quem abre quer ver o que o emissor
    gerou, não a nossa leitura dele.
    """
    if lado not in ("cliente", "senior"):
        return Response(
            {"erro": "Lado inválido. Use 'cliente' ou 'senior'."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    # `_caminho` reaplica o basename — o nome vem da URL e não é confiável.
    caminho = _caminho(lote_id, lado, nome_arquivo)
    if not caminho.is_file():
        return Response(
            {"erro": "Arquivo não encontrado neste lote."},
            status=status.HTTP_404_NOT_FOUND,
        )

    # `inline` para o navegador renderizar em vez de baixar; XML tem visualizador
    # nativo em Chrome e Firefox.
    resposta = HttpResponse(caminho.read_bytes(), content_type="application/xml")
    resposta["Content-Disposition"] = f'inline; filename="{caminho.name}"'
    return resposta


def _ler_documento(lote_id, lado: str, nome_arquivo: str, origem: str):
    caminho = _caminho(lote_id, lado, nome_arquivo)
    if not caminho.is_file():
        raise ErroDeParse(f"Arquivo '{nome_arquivo}' não encontrado no lote.")
    return parse_documento(caminho.read_bytes(), origem=origem, nome_arquivo=nome_arquivo)


def _estado_lote(lote: Lote) -> dict:
    documentos = lote.documentos or {}
    return {
        "lote_id": str(lote.id),
        "criado_em": lote.criado_em.isoformat(),
        "status": lote.status,
        "origem_cliente": lote.nome_origem_cliente,
        "origem_senior": lote.nome_origem_senior,
        "total_cliente": lote.total_cliente,
        "total_senior": lote.total_senior,
        "total_pares": lote.total_pares,
        "total_comparados": lote.total_comparados,
        "pares": [p.para_dicionario(documentos) for p in lote.pares.all()],
        "nao_pareados": lote.nao_pareados,
        "documentos": documentos,
        "resumo": lote.resumo,
        "avisos": lote.avisos,
    }


# --------------------------------------------------------------------------- #
#  1. Pareamento
# --------------------------------------------------------------------------- #
@api_view(["POST"])
@parser_classes([MultiPartParser, FormParser])
def parear_lote(request):
    """
    ``POST /api/comparador/lotes/parear/``

    Campos (multipart):
      * ``zip_cliente`` / ``zip_senior`` — um ZIP por lado, **ou**
      * ``xmls_cliente`` / ``xmls_senior`` — vários arquivos .xml por lado.
    """
    lote = Lote(
        nome_origem_cliente=(
            request.FILES["zip_cliente"].name if "zip_cliente" in request.FILES else "XMLs avulsos"
        ),
        nome_origem_senior=(
            request.FILES["zip_senior"].name if "zip_senior" in request.FILES else "XMLs avulsos"
        ),
    )
    raiz = _raiz_lote(lote.id)

    try:
        arquivos_cliente = receber_conjunto(
            request.FILES.get("zip_cliente"),
            request.FILES.getlist("xmls_cliente"),
            raiz / "cliente",
        )
        arquivos_senior = receber_conjunto(
            request.FILES.get("zip_senior"),
            request.FILES.getlist("xmls_senior"),
            raiz / "senior",
        )
    except ErroDeExtracao as exc:
        shutil.rmtree(raiz, ignore_errors=True)
        return Response({"erro": str(exc)}, status=status.HTTP_400_BAD_REQUEST)

    avisos: list[str] = []

    def _montar(arquivos, origem, lado):
        assinaturas = []
        for arquivo in arquivos:
            try:
                doc = parse_documento(
                    arquivo.caminho.read_bytes(), origem=origem, nome_arquivo=arquivo.nome
                )
            except ErroDeParse as exc:
                avisos.append(f"[{lado}] {arquivo.nome}: {exc}")
                continue
            assinaturas.append(montar_assinatura(doc))
        return assinaturas

    assinaturas_cliente = _montar(arquivos_cliente, "cliente", "cliente")
    assinaturas_senior = _montar(arquivos_senior, "senior", "Senior")

    if not assinaturas_cliente or not assinaturas_senior:
        shutil.rmtree(raiz, ignore_errors=True)
        return Response(
            {
                "erro": "Nenhum XML válido foi lido em um dos lados.",
                "avisos": avisos,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    pares, sem_par_cliente, sem_par_senior = parear(assinaturas_cliente, assinaturas_senior)

    lote.total_cliente = len(assinaturas_cliente)
    lote.total_senior = len(assinaturas_senior)
    lote.total_pares = len(pares)
    lote.documentos = {
        "cliente": [a.para_dicionario() for a in assinaturas_cliente],
        "senior": [a.para_dicionario() for a in assinaturas_senior],
    }
    lote.avisos = avisos
    lote.status = Lote.Status.PAREADO

    with transaction.atomic():
        lote.save()
        ParDocumentos.objects.bulk_create(
            [
                ParDocumentos(
                    lote=lote,
                    indice=indice,
                    arquivo_cliente=par.cliente.nome_arquivo,
                    arquivo_senior=par.senior.nome_arquivo,
                    score=par.score,
                    confianca=par.confianca,
                    motivos=par.motivos,
                )
                for indice, par in enumerate(pares)
            ]
        )

    if sem_par_cliente or sem_par_senior:
        avisos.append(
            f"{len(sem_par_cliente)} nota(s) do cliente e {len(sem_par_senior)} do Senior "
            "ficaram sem par. Elas podem ser vinculadas manualmente na tela."
        )
        lote.avisos = avisos
        lote.save(update_fields=["avisos"])

    return Response(_estado_lote(lote), status=status.HTTP_201_CREATED)


# --------------------------------------------------------------------------- #
#  2. Consulta / repareamento manual
# --------------------------------------------------------------------------- #
@api_view(["GET", "DELETE"])
def detalhe_lote(request, lote_id):
    try:
        lote = Lote.objects.prefetch_related("pares").get(pk=lote_id)
    except (Lote.DoesNotExist, ValueError, TypeError):
        return Response({"erro": MSG_LOTE_SUMIU}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        shutil.rmtree(_raiz_lote(lote.id), ignore_errors=True)
        lote.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    return Response(_estado_lote(lote))


@api_view(["POST"])
def repartear_lote(request, lote_id):
    """
    ``POST /api/comparador/lotes/<id>/repartear/``

    Corpo: ``{"pares": [{"cliente": "a.xml", "senior": "b.xml"}, ...]}``

    Substitui todo o pareamento pelo informado. Usado quando o consultor
    corrige um vínculo errado ou liga manualmente duas notas que ficaram sem par.
    """
    try:
        lote = Lote.objects.get(pk=lote_id)
    except (Lote.DoesNotExist, ValueError, TypeError):
        return Response({"erro": MSG_LOTE_SUMIU}, status=status.HTTP_404_NOT_FOUND)

    entrada = request.data.get("pares")
    if not isinstance(entrada, list):
        return Response(
            {"erro": "Envie 'pares' como lista de {cliente, senior}."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    documentos = lote.documentos or {}
    validos_cliente = {d["nome_arquivo"] for d in documentos.get("cliente", [])}
    validos_senior = {d["nome_arquivo"] for d in documentos.get("senior", [])}

    vistos_cliente: set[str] = set()
    vistos_senior: set[str] = set()
    novos: list[ParDocumentos] = []

    for indice, item in enumerate(entrada):
        cliente = (item or {}).get("cliente")
        senior = (item or {}).get("senior")
        if cliente not in validos_cliente or senior not in validos_senior:
            return Response(
                {"erro": f"Par inválido na posição {indice}: {cliente} ↔ {senior}."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if cliente in vistos_cliente or senior in vistos_senior:
            return Response(
                {"erro": f"A nota {cliente or senior} aparece em mais de um par."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        vistos_cliente.add(cliente)
        vistos_senior.add(senior)
        novos.append(
            ParDocumentos(
                lote=lote,
                indice=indice,
                arquivo_cliente=cliente,
                arquivo_senior=senior,
                score=0,
                confianca=ParDocumentos.Confianca.MANUAL,
                motivos=["vínculo definido manualmente pelo consultor"],
            )
        )

    with transaction.atomic():
        Comparacao.objects.filter(lote=lote).delete()
        lote.pares.all().delete()
        ParDocumentos.objects.bulk_create(novos)
        lote.total_pares = len(novos)
        lote.total_comparados = 0
        lote.status = Lote.Status.PAREADO
        lote.resumo = {}
        lote.relatorio_markdown = ""
        lote.save()

    lote.refresh_from_db()
    return Response(_estado_lote(lote))


# --------------------------------------------------------------------------- #
#  3. Comparação em blocos
# --------------------------------------------------------------------------- #
@api_view(["POST"])
def comparar_lote(request, lote_id):
    """
    ``POST /api/comparador/lotes/<id>/comparar/``

    Corpo: ``{"indices": [0, 1, 2, 3, 4]}`` (opcional — sem ele, compara os
    ``tamanho_bloco`` próximos pares ainda não comparados).

    A tela chama este endpoint em sequência para desenhar a barra de progresso.
    """
    try:
        lote = Lote.objects.get(pk=lote_id)
    except (Lote.DoesNotExist, ValueError, TypeError):
        return Response({"erro": MSG_LOTE_SUMIU}, status=status.HTTP_404_NOT_FOUND)

    indices = request.data.get("indices")
    if isinstance(indices, list) and indices:
        pares = list(lote.pares.filter(indice__in=indices))
    else:
        tamanho = int(request.data.get("tamanho_bloco") or TAMANHO_BLOCO_PADRAO)
        pares = list(lote.pares.filter(comparado=False)[:tamanho])

    if lote.status != Lote.Status.COMPARANDO:
        lote.status = Lote.Status.COMPARANDO
        lote.save(update_fields=["status"])

    # Numa validação de implantação é comum simular só parte dos itens. Os que
    # ficaram de fora aparecem como "item não emitido pelo Senior" e viram
    # dezenas de achados CRÍTICOS que afogam as divergências reais.
    itens_nao_simulados = request.data.get("itens_nao_simulados", True) is not False

    processados = []
    for par in pares:
        processados.append(
            _comparar_par(lote, par, itens_nao_simulados=itens_nao_simulados)
        )

    lote.total_comparados = lote.pares.filter(comparado=True).count()
    lote.save(update_fields=["total_comparados", "atualizado_em"])

    return Response(
        {
            "lote_id": str(lote.id),
            "processados": processados,
            "total_comparados": lote.total_comparados,
            "total_pares": lote.total_pares,
            "concluido": lote.total_comparados >= lote.total_pares,
        }
    )


def _comparar_par(lote: Lote, par: ParDocumentos, *, itens_nao_simulados: bool = True) -> dict:
    """Compara um par e persiste o resultado. Erros ficam no próprio par."""
    try:
        doc_cliente = _ler_documento(lote.id, "cliente", par.arquivo_cliente, "cliente")
        doc_senior = _ler_documento(lote.id, "senior", par.arquivo_senior, "senior")
        resultado = comparar_documentos(
            doc_cliente, doc_senior, analisar_itens_nao_simulados=itens_nao_simulados
        )
    except (ErroDeParse, Exception) as exc:  # noqa: BLE001
        logger.warning("Falha ao comparar par %s: %s", par.indice, exc)
        par.erro = f"{type(exc).__name__}: {exc}"
        par.comparado = True
        par.save(update_fields=["erro", "comparado"])
        return {"indice": par.indice, "erro": par.erro}

    dados = resultado.para_dicionario()
    sev = dados["resumo"].get("por_severidade", {})

    with transaction.atomic():
        if par.comparacao_id:
            Comparacao.objects.filter(pk=par.comparacao_id).delete()

        comparacao = Comparacao.objects.create(
            lote=lote,
            arquivo_cliente=par.arquivo_cliente,
            arquivo_senior=par.arquivo_senior,
            chave_cliente=doc_cliente.chave,
            chave_senior=doc_senior.chave,
            resumo=dados["resumo"],
            resultado=dados,
            relatorio_markdown="",  # no lote, o relatório é consolidado
            total_divergencias=dados["resumo"].get("total_divergencias", 0),
            total_criticas=sev.get(CRITICA, 0),
            total_altas=sev.get(ALTA, 0),
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

        par.comparacao = comparacao
        par.comparado = True
        par.erro = ""
        par.total_divergencias = comparacao.total_divergencias
        par.total_criticas = comparacao.total_criticas
        par.total_altas = comparacao.total_altas
        par.save(
            update_fields=[
                "comparacao",
                "comparado",
                "erro",
                "total_divergencias",
                "total_criticas",
                "total_altas",
            ]
        )

    return {
        "indice": par.indice,
        "arquivo_cliente": par.arquivo_cliente,
        "arquivo_senior": par.arquivo_senior,
        "total_divergencias": par.total_divergencias,
        "total_criticas": par.total_criticas,
        "total_altas": par.total_altas,
        "comparacao_id": str(comparacao.id),
        "erro": "",
    }


# --------------------------------------------------------------------------- #
#  4. Consolidação
# --------------------------------------------------------------------------- #
@api_view(["POST", "GET"])
def consolidar_lote(request, lote_id):
    """
    ``POST /api/comparador/lotes/<id>/consolidar/``

    Agrega todas as comparações do lote num ranking de causas recorrentes e
    monta o relatório que vai para o agente de IA.
    """
    try:
        lote = Lote.objects.prefetch_related("pares").get(pk=lote_id)
    except (Lote.DoesNotExist, ValueError, TypeError):
        return Response({"erro": MSG_LOTE_SUMIU}, status=status.HTTP_404_NOT_FOUND)

    comparacoes = {
        str(c.pk): c
        for c in Comparacao.objects.filter(lote=lote).only("id", "resultado")
    }

    # "Nota Original 63 ↔ Nota Senior 65" é como o consultor identifica o par —
    # muito mais útil que o nome do arquivo, que costuma ser a chave de acesso
    # de 44 dígitos. O par sempre nomeia os dois lados: "NF" sozinho não dizia
    # qual dos sistemas era qual.
    documentos = lote.documentos or {}
    numero_por_arquivo = {
        d["nome_arquivo"]: d.get("numero", "")
        for lado in ("cliente", "senior")
        for d in documentos.get(lado, [])
    }

    def _rotulo(par: ParDocumentos) -> str:
        numero_cliente = numero_por_arquivo.get(par.arquivo_cliente, "")
        numero_senior = numero_por_arquivo.get(par.arquivo_senior, "")
        if numero_cliente and numero_senior:
            return f"Nota Original {numero_cliente} ↔ Nota Senior {numero_senior}"
        return f"{par.arquivo_cliente} ↔ {par.arquivo_senior}"

    entradas = []
    for par in lote.pares.filter(comparado=True):
        comparacao = comparacoes.get(str(par.comparacao_id)) if par.comparacao_id else None
        if comparacao is None:
            continue
        resultado = comparacao.resultado or {}
        identificacao = (
            (resultado.get("documentos", {}).get("cliente", {}) or {}).get("identificacao", "")
        )
        entradas.append(
            {
                "arquivo_cliente": par.arquivo_cliente,
                "arquivo_senior": par.arquivo_senior,
                "rotulo": _rotulo(par),
                "identificacao": identificacao,
                "comparacao_id": str(comparacao.pk),
                "divergencias": resultado.get("divergencias", []),
            }
        )

    if not entradas:
        return Response(
            {"erro": "Nenhum par comparado ainda. Rode a comparação antes de consolidar."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    nao_pareados = lote.nao_pareados
    escopo = {
        "total_cliente": lote.total_cliente,
        "total_senior": lote.total_senior,
        "sem_par_cliente": len(nao_pareados["cliente"]),
        "sem_par_senior": len(nao_pareados["senior"]),
    }

    agregado = agregar_lote(entradas)
    markdown = montar_relatorio_lote_markdown(agregado, escopo=escopo)

    lote.resumo = {
        "escopo": escopo,
        **agregado["placar"],
        "narrativa": agregado["narrativa"],
        "perfis": agregado["perfis"],
    }
    lote.relatorio_markdown = markdown
    lote.status = Lote.Status.CONCLUIDO
    lote.total_comparados = len(entradas)
    lote.save(update_fields=["resumo", "relatorio_markdown", "status", "total_comparados"])

    return Response(
        {
            "lote_id": str(lote.id),
            "escopo": escopo,
            "placar": agregado["placar"],
            "narrativa": agregado["narrativa"],
            "perfis": agregado["perfis"],
            "causas": agregado["causas"],
            "notas": agregado["notas"],
            "nao_pareados": nao_pareados,
            "relatorio_markdown": markdown,
        }
    )


# --------------------------------------------------------------------------- #
#  5. Histórico
# --------------------------------------------------------------------------- #
@api_view(["GET"])
def historico_lotes(request):
    limite = min(int(request.query_params.get("limite", 20)), 100)
    return Response(
        [
            {
                "lote_id": str(l.id),
                "criado_em": l.criado_em.isoformat(),
                "origem_cliente": l.nome_origem_cliente,
                "origem_senior": l.nome_origem_senior,
                "status": l.status,
                "total_pares": l.total_pares,
                "total_comparados": l.total_comparados,
                "resumo": l.resumo,
            }
            for l in Lote.objects.all()[:limite]
        ]
    )


# --------------------------------------------------------------------------- #
#  6. Relatório detalhado (HTML imprimível, sem IA)
# --------------------------------------------------------------------------- #
def relatorio_detalhado(request, lote_id):
    """
    ``GET /api/comparador/lotes/<id>/relatorio/``

    Documento completo do lote: resumo, todas as causas, todas as divergências
    nota a nota e as notas sem par. Abre numa aba nova e imprime em PDF pelo
    próprio navegador (Ctrl+P).

    É gerado pelo comparador, **não pela IA** — o conteúdo é 100% determinístico
    e reproduzível a partir dos mesmos XMLs.
    """
    from django.http import Http404
    from django.shortcuts import render

    try:
        lote = Lote.objects.prefetch_related("pares").get(pk=lote_id)
    except (Lote.DoesNotExist, ValueError, TypeError):
        raise Http404(MSG_LOTE_SUMIU)

    comparacoes = {str(c.pk): c for c in Comparacao.objects.filter(lote=lote)}

    documentos = lote.documentos or {}
    numero_por_arquivo = {
        d["nome_arquivo"]: d.get("numero", "")
        for lado in ("cliente", "senior")
        for d in documentos.get(lado, [])
    }

    entradas = []
    notas_detalhadas = []
    for par in lote.pares.filter(comparado=True):
        comparacao = comparacoes.get(str(par.comparacao_id)) if par.comparacao_id else None
        if comparacao is None:
            continue
        numero_cliente = numero_por_arquivo.get(par.arquivo_cliente, "")
        numero_senior = numero_por_arquivo.get(par.arquivo_senior, "")
        rotulo = (
            f"Nota Original {numero_cliente} ↔ Nota Senior {numero_senior}"
            if numero_cliente and numero_senior
            else f"{par.arquivo_cliente} ↔ {par.arquivo_senior}"
        )
        divergencias = (comparacao.resultado or {}).get("divergencias", [])
        entradas.append(
            {
                "arquivo_cliente": par.arquivo_cliente,
                "arquivo_senior": par.arquivo_senior,
                "rotulo": rotulo,
                "divergencias": divergencias,
            }
        )
        notas_detalhadas.append(
            {
                "rotulo": rotulo,
                "par": par,
                "divergencias": divergencias,
                "total": len(divergencias),
            }
        )

    agregado = agregar_lote(entradas) if entradas else {"placar": {}, "causas": [], "notas": [], "perfis": [], "narrativa": {}}
    notas_detalhadas.sort(key=lambda n: (-n["total"], n["rotulo"]))

    nao_pareados = lote.nao_pareados

    return render(
        request,
        "comparador/relatorio_lote.html",
        {
            "lote": lote,
            "placar": agregado["placar"],
            "narrativa": agregado["narrativa"],
            "perfis": agregado["perfis"],
            "causas": agregado["causas"],
            "notas": notas_detalhadas,
            "nao_pareados": nao_pareados,
            "escopo": lote.resumo.get("escopo", {}) if isinstance(lote.resumo, dict) else {},
        },
    )


def relatorio_comparacao(request, comparacao_id):
    """
    ``GET /api/comparador/<uuid>/relatorio/``

    Mesmo documento do relatório de lote, para uma comparação avulsa (modo
    "nota a nota"). Também 100% determinístico.
    """
    from django.http import Http404
    from django.shortcuts import render

    try:
        comparacao = Comparacao.objects.get(pk=comparacao_id)
    except (Comparacao.DoesNotExist, ValueError, TypeError):
        raise Http404("Comparação não encontrada.")

    resultado = comparacao.resultado or {}
    documentos = resultado.get("documentos", {})
    rotulo = "{} ↔ {}".format(
        (documentos.get("cliente", {}) or {}).get("identificacao", comparacao.arquivo_cliente),
        (documentos.get("senior", {}) or {}).get("identificacao", comparacao.arquivo_senior),
    )
    divergencias = resultado.get("divergencias", [])

    agregado = agregar_lote(
        [
            {
                "arquivo_cliente": comparacao.arquivo_cliente,
                "arquivo_senior": comparacao.arquivo_senior,
                "rotulo": rotulo,
                "divergencias": divergencias,
            }
        ]
    )

    # O template espera um objeto com os mesmos atributos do lote/par.
    class _Falso:
        pass

    lote_falso = _Falso()
    lote_falso.id = comparacao.pk
    lote_falso.nome_origem_cliente = comparacao.arquivo_cliente
    lote_falso.nome_origem_senior = comparacao.arquivo_senior

    par_falso = _Falso()
    par_falso.arquivo_cliente = comparacao.arquivo_cliente
    par_falso.arquivo_senior = comparacao.arquivo_senior
    par_falso.score = 0
    par_falso.get_confianca_display = lambda: "comparação avulsa"

    return render(
        request,
        "comparador/relatorio_lote.html",
        {
            "lote": lote_falso,
            "placar": agregado["placar"],
            "narrativa": agregado["narrativa"],
            "perfis": agregado["perfis"],
            "causas": agregado["causas"],
            "notas": [
                {
                    "rotulo": rotulo,
                    "par": par_falso,
                    "divergencias": divergencias,
                    "total": len(divergencias),
                }
            ],
            "nao_pareados": {"cliente": [], "senior": []},
        },
    )
