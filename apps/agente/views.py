"""
Endpoints Django do agente: histórico de conversas, avaliação e um chat
**sem streaming**.

O caminho normal do chat é o SSE em ``/api/ia/chat`` (FastAPI). O endpoint
``chat_sincrono`` daqui existe como plano B: ele funciona mesmo rodando o
projeto com ``manage.py runserver`` (WSGI), onde o sub-app FastAPI não é
montado. O front detecta o 404 do SSE e cai para cá automaticamente.
"""
from __future__ import annotations

import logging

from asgiref.sync import async_to_sync
from django.db.models import Count
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.provedores.catalogo import rotulo_do_modelo, rotulo_do_provedor
from apps.provedores.models import ProvedorIA, TipoModelo

from .graph import construir_grafo
from .models import AvaliacaoMensagem, Conversa, Mensagem
from .services import preparar_conversa, salvar_resposta

logger = logging.getLogger(__name__)


def _sessao(request) -> str:
    """
    Escopo de UI vindo do header ``X-Sessao`` (localStorage do navegador).

    NÃO é autenticação — ver o comentário em ``Conversa.chave_sessao``.
    """
    return (request.headers.get("X-Sessao") or "").strip()[:64]


@api_view(["GET"])
def listar_conversas(request):
    """
    ``GET /api/agente/conversas/`` — histórico, mais recentes primeiro.

    Lista TODAS as conversas por padrão. O filtro por sessão existe em
    ``?minhas=1``, mas não é o comportamento padrão — e a razão é concreta:
    o escopo vem do localStorage, então trocar de navegador, abrir uma aba
    anônima ou limpar os dados do site fazia o histórico inteiro desaparecer,
    sem qualquer forma de recuperá-lo. Como não há autenticação, filtrar não
    protegia nada: só escondia o trabalho do próprio consultor.

    A ``chave_sessao`` continua sendo gravada — quando houver login, o escopo
    passa a ser por usuário de verdade e este endpoint volta a filtrar.
    """
    try:
        limite = min(max(int(request.query_params.get("limite", 30)), 1), 100)
    except (TypeError, ValueError):
        limite = 30  # ?limite=abc não é motivo para derrubar o histórico
    consulta = Conversa.objects.annotate(qtd_mensagens=Count("mensagens"))

    chave = _sessao(request)
    if chave and request.query_params.get("minhas") == "1":
        consulta = consulta.filter(chave_sessao=chave)

    return Response(
        [
            {
                "id": str(c.pk),
                "titulo": c.titulo,
                "comparacao_id": str(c.comparacao_id) if c.comparacao_id else None,
                "lote_id": str(c.lote_id) if c.lote_id else None,
                "tem_contexto": bool(c.comparacao_id or c.lote_id),
                "criado_em": c.criado_em.isoformat(),
                "atualizado_em": c.atualizado_em.isoformat(),
                "total_mensagens": c.qtd_mensagens,
            }
            for c in consulta[:limite]
        ]
    )


@api_view(["GET", "DELETE"])
def detalhe_conversa(request, conversa_id):
    try:
        conversa = Conversa.objects.get(pk=conversa_id)
    except (Conversa.DoesNotExist, ValueError, TypeError):
        return Response({"erro": "Conversa não encontrada."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        conversa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    mensagens = conversa.mensagens.select_related("avaliacao").all()
    return Response(
        {
            "id": str(conversa.pk),
            "titulo": conversa.titulo,
            "comparacao_id": str(conversa.comparacao_id) if conversa.comparacao_id else None,
            "lote_id": str(conversa.lote_id) if conversa.lote_id else None,
            # As FKs são SET_NULL: o lote pode ter sido apagado depois. Sem este
            # aviso o agente responderia sem contexto e o consultor não saberia.
            "contexto_ativo": bool(conversa.comparacao_id or conversa.lote_id),
            "criado_em": conversa.criado_em.isoformat(),
            "mensagens": [m.para_dicionario() for m in mensagens],
        }
    )


@api_view(["POST", "DELETE"])
def avaliar_mensagem(request, mensagem_id):
    """
    ``POST /api/agente/mensagens/<id>/avaliacao/`` — 👍/👎 numa resposta.

    Corpo: ``{"valor": 1 | -1, "motivo": "tela_errada", "comentario": "..."}``.
    ``DELETE`` desfaz o voto. Repetir o POST troca o voto (update_or_create).
    """
    try:
        mensagem = Mensagem.objects.select_related("conversa").get(pk=mensagem_id)
    except (Mensagem.DoesNotExist, ValueError, TypeError):
        return Response({"erro": "Mensagem não encontrada."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        AvaliacaoMensagem.objects.filter(mensagem=mensagem).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    if mensagem.papel != Mensagem.Papel.AGENTE:
        return Response(
            {"erro": "Só respostas do agente podem ser avaliadas."},
            status=status.HTTP_400_BAD_REQUEST,
        )
    # Resposta que falhou não diz nada sobre a qualidade do agente e sujaria o
    # dataset. O front já não oferece os botões nesses casos; aqui é a trava,
    # porque o endpoint é público e o id da mensagem é sequencial.
    if mensagem.erro or not mensagem.conteudo.strip():
        return Response(
            {"erro": "Esta resposta falhou e não pode ser avaliada."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        valor = int(request.data.get("valor"))
    except (TypeError, ValueError):
        valor = 0
    if valor not in (AvaliacaoMensagem.Valor.POSITIVO, AvaliacaoMensagem.Valor.NEGATIVO):
        return Response(
            {"erro": "Informe 'valor' igual a 1 (gostei) ou -1 (não gostei)."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    motivo = (request.data.get("motivo") or "").strip()
    if motivo and motivo not in AvaliacaoMensagem.Motivo.values:
        motivo = AvaliacaoMensagem.Motivo.OUTRO

    avaliacao, _ = AvaliacaoMensagem.objects.update_or_create(
        mensagem=mensagem,
        defaults={
            "valor": valor,
            "motivo": motivo,
            "comentario": (request.data.get("comentario") or "").strip()[:2000],
            "contexto": _montar_contexto(mensagem),
            "chave_sessao": _sessao(request),
        },
    )
    return Response({"valor": avaliacao.valor, "motivo": avaliacao.motivo})


def _montar_contexto(mensagem: Mensagem) -> dict:
    """
    Retrato do que gerou a resposta — montado no servidor, não confiando no
    cliente. É o que permite revisar (e exportar) o caso meses depois.
    """
    pergunta = (
        Mensagem.objects.filter(
            conversa_id=mensagem.conversa_id,
            papel=Mensagem.Papel.USUARIO,
            criado_em__lte=mensagem.criado_em,
        )
        .exclude(pk=mensagem.pk)
        .order_by("-criado_em", "-id")
        .first()
    )
    conversa = mensagem.conversa
    metadados = mensagem.metadados or {}
    return {
        "pergunta": pergunta.conteudo if pergunta else "",
        "resposta": mensagem.conteudo,
        "modelo": mensagem.modelo,
        # Copiado do que foi congelado quando a resposta nasceu. Recalcular aqui
        # daria a versão de HOJE, não a que gerou a resposta votada — que é
        # justamente o erro que este campo existe para evitar.
        "versao_prompt": metadados.get("versao_prompt", ""),
        "git_sha": metadados.get("git_sha", ""),
        "fontes": [
            {k: v for k, v in f.items() if k in ("documento", "fonte", "secao", "url")}
            for f in (mensagem.fontes or [])
        ],
        "conversa_id": str(conversa.pk),
        "lote_id": str(conversa.lote_id) if conversa.lote_id else None,
        "comparacao_id": str(conversa.comparacao_id) if conversa.comparacao_id else None,
        "respondido_em": mensagem.criado_em.isoformat(),
    }


@api_view(["GET"])
def provedores_disponiveis(request):
    """Lista compacta para o seletor de modelo no topo do chat."""
    padrao = ProvedorIA.obter_padrao(TipoModelo.CHAT)
    provedores = ProvedorIA.objects.filter(ativo=True, tipo=TipoModelo.CHAT)
    return Response(
        {
            "padrao_id": padrao.pk if padrao else None,
            "provedores": [
                {
                    "id": p.pk,
                    "nome": p.nome,
                    "provedor": p.provedor,
                    "provedor_label": rotulo_do_provedor(p.provedor),
                    "modelo": p.modelo,
                    "modelo_label": rotulo_do_modelo(p.provedor, p.modelo),
                    "padrao": p.padrao,
                }
                for p in provedores
            ],
        }
    )


@api_view(["POST"])
def chat_sincrono(request):
    """
    ``POST /api/agente/chat-sync/`` — mesma lógica do SSE, resposta de uma vez.

    Corpo: ``{"mensagem": ..., "conversa_id": ..., "comparacao_id": ..., "provedor_id": ...}``
    """
    mensagem = (request.data.get("mensagem") or "").strip()
    if not mensagem:
        return Response({"erro": "Informe 'mensagem'."}, status=status.HTTP_400_BAD_REQUEST)

    provedor_id = request.data.get("provedor_id")
    contexto = preparar_conversa(
        mensagem=mensagem,
        conversa_id=request.data.get("conversa_id"),
        comparacao_id=request.data.get("comparacao_id"),
        lote_id=request.data.get("lote_id"),
        chave_sessao=_sessao(request),
        rotulo=(request.data.get("rotulo") or "")[:200],
    )

    estado = {
        "pergunta": mensagem,
        "conversa_id": contexto["conversa_id"],
        "comparacao_id": contexto["comparacao_id"],
        "lote_id": contexto["lote_id"],
        "provedor_id": int(provedor_id) if provedor_id else None,
        "historico": contexto["historico"],
        "rotulo": (request.data.get("rotulo") or "").strip(),
    }

    try:
        final = async_to_sync(construir_grafo().ainvoke)(estado)
    except Exception as exc:  # noqa: BLE001
        logger.exception("Falha no chat síncrono")
        return Response(
            {"erro": f"{type(exc).__name__}: {exc}"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    # `fontes_extras` são as que a busca documental achou durante a resposta —
    # sem elas o caminho síncrono grava a resposta citando trechos que não
    # aparecem em lugar nenhum quando a conversa é reaberta.
    vistos: set = set()
    fontes = []
    for trecho in [*final.get("contexto", []), *final.get("fontes_extras", [])]:
        if trecho.get("trecho_id") in vistos:
            continue
        vistos.add(trecho.get("trecho_id"))
        fontes.append({k: v for k, v in trecho.items() if k != "texto"})
    resposta_agente = salvar_resposta(
        conversa_id=contexto["conversa_id"],
        conteudo=final.get("resposta", ""),
        fontes=fontes,
        prints=final.get("imagens") or {},
        modelo=final.get("modelo_usado", ""),
        erro=final.get("erro", ""),
        provedor_id=int(provedor_id) if provedor_id else None,
    )

    return Response(
        {
            "conversa_id": contexto["conversa_id"],
            "mensagem": resposta_agente.para_dicionario(),
            "erro": final.get("erro", ""),
        }
    )
