"""
Sub-aplicação FastAPI responsável pelo streaming do chat (SSE).

Montada em ``/api/ia`` pelo ``config/asgi.py``. O Django continua atendendo todo
o resto — usamos o FastAPI aqui porque ele lida melhor com respostas assíncronas
de longa duração (o token-a-token do modelo).

Eventos SSE emitidos (um JSON por linha ``data:``):

    {"tipo": "inicio",     "conversa_id": "...", "mensagem_id": 12}
    {"tipo": "fontes",     "fontes": [...], "prints": {...}}
    {"tipo": "ferramenta", "chamadas": [{"nome": "consultar_ipi", "resumo": "NCM 8471…"}]}
    {"tipo": "token",      "texto": "..."}
    {"tipo": "fim",        "mensagem_id": 13, "modelo": "anthropic:claude-opus-5"}
    {"tipo": "erro",       "mensagem": "..."}

``ferramenta`` existe por causa da espera: uma rodada de consulta são duas idas
ao provedor antes do primeiro token, e sem sinal nenhum a tela fica em
"carregando" por vários segundos — foi a reclamação registrada em 12/08/2026.
"""
from __future__ import annotations

import json
import logging
from typing import Any, AsyncIterator

from asgiref.sync import sync_to_async
from fastapi import FastAPI
from fastapi.responses import JSONResponse, StreamingResponse
from pydantic import BaseModel, Field

from .cronometro import Cronometro
from .graph import NOME_NO_FERRAMENTAS, NOME_NO_RECUPERAR, construir_grafo
from .services import preparar_conversa, salvar_resposta

logger = logging.getLogger(__name__)

#: Como cada consulta aparece na tela enquanto roda.
_ROTULO_FERRAMENTA = {
    "buscar_documentacao": "documentação Senior",
    "consultar_ncm": "tabela NCM",
    "consultar_ipi": "TIPI (IPI por NCM)",
    "consultar_cest": "tabela CEST",
    "consultar_cfop": "tabela CFOP",
    "consultar_fcp": "FCP por UF",
    "aliquota_icms_interestadual": "alíquota interestadual",
}


def _resumir_chamada(chamada: dict[str, Any]) -> dict[str, str]:
    """Nome legível + os argumentos, curtos, para a pastilha de atividade."""
    nome = chamada.get("name") or ""
    argumentos = chamada.get("args") or {}
    valores = ", ".join(str(v) for v in argumentos.values() if v not in (None, "", 0))
    return {
        "nome": _ROTULO_FERRAMENTA.get(nome, nome),
        "detalhe": valores[:80],
    }

api_app = FastAPI(
    title="Agente de Implantação Fiscal — API de IA",
    docs_url="/api/ia/docs",
    openapi_url="/api/ia/openapi.json",
    redoc_url=None,
)


class EntradaChat(BaseModel):
    mensagem: str = Field(..., min_length=1)
    conversa_id: str | None = None
    comparacao_id: str | None = None
    lote_id: str | None = None
    provedor_id: int | None = None
    #: Escopo de UI do histórico. Viaja no corpo porque o SSE não passa pelo
    #: middleware do Django (o fetch do front é cru, sem o wrapper `requisicao`).
    sessao: str | None = None
    #: Frase curta exibida na tela quando a pergunta parte de um botão.
    rotulo: str | None = None


# --------------------------------------------------------------------------- #
#  Acesso ao banco — a lógica mora em services/conversas.py, compartilhada com
#  o chat síncrono de views.py. Aqui só o embrulho assíncrono.
# --------------------------------------------------------------------------- #
_preparar_conversa = sync_to_async(preparar_conversa)
_salvar_resposta = sync_to_async(salvar_resposta)


# --------------------------------------------------------------------------- #
#  Streaming
# --------------------------------------------------------------------------- #
def _sse(dados: dict[str, Any]) -> str:
    return f"data: {json.dumps(dados, ensure_ascii=False)}\n\n"


async def _stream_resposta(entrada: EntradaChat) -> AsyncIterator[str]:
    try:
        contexto = await _preparar_conversa(
            mensagem=entrada.mensagem,
            conversa_id=entrada.conversa_id,
            comparacao_id=entrada.comparacao_id,
            lote_id=entrada.lote_id,
            chave_sessao=(entrada.sessao or "")[:64],
            rotulo=(entrada.rotulo or "")[:200],
        )
    except Exception as exc:  # noqa: BLE001
        logger.exception("Falha ao preparar a conversa")
        yield _sse({"tipo": "erro", "mensagem": f"Falha ao iniciar a conversa: {exc}"})
        return

    conversa_id = contexto["conversa_id"]
    yield _sse(
        {
            "tipo": "inicio",
            "conversa_id": conversa_id,
            "mensagem_id": contexto["mensagem_usuario_id"],
        }
    )

    estado_inicial = {
        "pergunta": entrada.mensagem,
        "conversa_id": conversa_id,
        "comparacao_id": contexto["comparacao_id"],
        "lote_id": contexto["lote_id"],
        "provedor_id": entrada.provedor_id,
        "historico": contexto["historico"],
        "rotulo": entrada.rotulo or "",
    }

    grafo = construir_grafo()
    partes: list[str] = []
    fontes: list[dict[str, Any]] = []
    prints: dict[str, str] = {}
    modelo_usado = ""
    erro = ""
    cronometro = Cronometro()

    try:
        async for evento in grafo.astream_events(estado_inicial, version="v2"):
            cronometro.observar(evento)
            tipo = evento.get("event")

            if tipo == "on_chat_model_stream":
                pedaco = evento["data"].get("chunk")
                texto = getattr(pedaco, "content", "") if pedaco is not None else ""
                if isinstance(texto, list):
                    texto = "".join(
                        b.get("text", "") for b in texto if isinstance(b, dict)
                    )
                if texto:
                    cronometro.token_visivel()
                    partes.append(str(texto))
                    yield _sse({"tipo": "token", "texto": str(texto)})

            elif tipo == "on_chat_model_end":
                # O modelo decidiu consultar. Avisar AGORA, e não depois de
                # executar: entre este ponto e o primeiro token da resposta final
                # há uma execução mais uma ida inteira ao provedor.
                saida = evento["data"].get("output")
                chamadas = list(getattr(saida, "tool_calls", None) or [])
                if chamadas:
                    yield _sse(
                        {
                            "tipo": "ferramenta",
                            "chamadas": [_resumir_chamada(c) for c in chamadas],
                        }
                    )

            elif tipo == "on_chain_end" and evento.get("name") == NOME_NO_FERRAMENTAS:
                # A busca documental achou trechos novos: a lista de fontes e o
                # mapa de prints crescem no meio do turno. Reemitimos a UNIÃO —
                # o front substitui a caixa de fontes, então mandar só as novas
                # apagaria as da recuperação inicial.
                saida = evento["data"].get("output") or {}
                extras = saida.get("fontes_extras") or []
                prints = saida.get("imagens") or prints
                if extras:
                    conhecidas = {f.get("trecho_id") for f in fontes}
                    for t in extras:
                        if t.get("trecho_id") not in conhecidas:
                            conhecidas.add(t.get("trecho_id"))
                            fontes.append({k: v for k, v in t.items() if k != "texto"})
                    yield _sse({"tipo": "fontes", "fontes": fontes, "prints": prints})

            elif tipo == "on_chain_end" and evento.get("name") == NOME_NO_RECUPERAR:
                saida = evento["data"].get("output") or {}
                trechos = saida.get("contexto") or []
                fontes = [
                    {k: v for k, v in t.items() if k != "texto"} for t in trechos
                ]
                # Mapa dos prints ({"3": "https://…"}). Capturado fora do `if`
                # das fontes porque ele também precisa ser PERSISTIDO — sem isso
                # reabrir a conversa no histórico mostra o texto sem as imagens.
                prints = saida.get("imagens") or {}
                # Vai junto das fontes — ou seja, chega ANTES do primeiro token —,
                # então o front já resolve [[print:3]] desde o começo do
                # streaming. Marcador que não estiver aqui não vira imagem: é o
                # que impede o modelo de forjar uma referência.
                if fontes:
                    yield _sse({"tipo": "fontes", "fontes": fontes, "prints": prints})

            elif tipo == "on_chain_end" and evento.get("name") == "LangGraph":
                saida = evento["data"].get("output") or {}
                modelo_usado = saida.get("modelo_usado", "") or modelo_usado
                erro = saida.get("erro", "") or erro
                if not partes and saida.get("resposta"):
                    partes.append(saida["resposta"])
    except Exception as exc:  # noqa: BLE001
        logger.exception("Falha durante o streaming do agente")
        erro = f"{type(exc).__name__}: {exc}"

    conteudo = "".join(partes)
    tempos = cronometro.fechar()

    if erro:
        yield _sse({"tipo": "erro", "mensagem": erro})

    try:
        resposta = await _salvar_resposta(
            conversa_id=conversa_id,
            conteudo=conteudo,
            fontes=fontes,
            prints=prints,
            modelo=modelo_usado,
            erro=erro,
            provedor_id=entrada.provedor_id,
        )
        mensagem_id = resposta.pk
    except Exception as exc:  # noqa: BLE001
        logger.exception("Falha ao salvar a resposta")
        mensagem_id = 0

    yield _sse(
        {
            "tipo": "fim",
            "conversa_id": conversa_id,
            "mensagem_id": mensagem_id,
            "modelo": modelo_usado,
            "tem_erro": bool(erro),
            # Aditivo: o front atual ignora; serve para olhar no DevTools
            # (aba Network → EventStream) sem precisar do log do servidor.
            "tempos": tempos,
        }
    )


# --------------------------------------------------------------------------- #
#  Rotas
# --------------------------------------------------------------------------- #
@api_app.post("/api/ia/chat")
async def chat(entrada: EntradaChat):
    """Conversa com o agente, com resposta em streaming (SSE)."""
    return StreamingResponse(
        _stream_resposta(entrada),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache, no-transform",
            "X-Accel-Buffering": "no",
            "Connection": "keep-alive",
        },
    )


@api_app.get("/api/ia/saude")
async def saude():
    """Checagem simples usada pelo front para saber se o ASGI está ativo."""
    return JSONResponse({"ok": True, "servico": "agente-ia"})
