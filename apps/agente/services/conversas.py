"""
Persistência da conversa — o pedaço que os dois caminhos do chat compartilham.

O chat tem duas implementações: o SSE (``apps/agente/api.py``, FastAPI) e o
``chat_sincrono`` (``apps/agente/views.py``, plano B em WSGI). A lógica de abrir
a conversa e gravar a resposta vivia duplicada nos dois, e já tinha divergido: só
o SSE carimbava ``atualizado_em``, então conversa mantida pelo fallback afundava
numa lista ordenada por esse campo — exatamente o que o histórico exibe.

As funções são **síncronas**: o FastAPI as envolve com ``sync_to_async`` e o
Django as chama direto.
"""
from __future__ import annotations

from typing import Any

from django.core.exceptions import ValidationError

from apps.agente.graph import historico_para_mensagens
from apps.agente.models import Conversa, Mensagem


def preparar_conversa(
    *,
    mensagem: str,
    conversa_id: str | None = None,
    comparacao_id: str | None = None,
    lote_id: str | None = None,
    chave_sessao: str = "",
    rotulo: str = "",
) -> dict[str, Any]:
    """
    Abre (ou reaproveita) a conversa e grava a pergunta do consultor.

    ``rotulo`` é o que o consultor viu na tela quando a pergunta partiu de um
    botão ("Analise as divergências"): o ``mensagem`` nesse caso é o prompt
    longo que vai ao modelo. Guardar os dois deixa o histórico reexibir a frase
    curta em vez da instrução interna.

    Devolve o contexto que os dois caminhos do chat precisam para montar o
    estado inicial do grafo.
    """
    conversa = None
    if conversa_id:
        try:
            conversa = Conversa.objects.filter(pk=conversa_id).first()
        except (ValidationError, ValueError, TypeError):
            # A PK é UUID: um id inválido levantaria ValidationError e viraria
            # 500 no chat. Tratar como "conversa nova" é o comportamento útil.
            conversa = None

    if conversa is None:
        conversa = Conversa.objects.create(
            titulo=((rotulo or mensagem)[:80] or "Nova conversa"),
            comparacao_id=comparacao_id or None,
            lote_id=lote_id or None,
            chave_sessao=chave_sessao or "",
        )
    else:
        campos: list[str] = []
        if comparacao_id and str(conversa.comparacao_id or "") != str(comparacao_id):
            conversa.comparacao_id = comparacao_id
            campos.append("comparacao")
        if lote_id and str(conversa.lote_id or "") != str(lote_id):
            conversa.lote_id = lote_id
            campos.append("lote")
        # Conversa criada antes do escopo por sessão existir adota a primeira
        # sessão que voltar a falar nela.
        if chave_sessao and not conversa.chave_sessao:
            conversa.chave_sessao = chave_sessao
            campos.append("chave_sessao")
        if campos:
            conversa.save(update_fields=campos)

    # O histórico é lido ANTES de gravar a pergunta atual: ela vai para o grafo
    # pelo campo `pergunta`, e apareceria duplicada se entrasse aqui também.
    historico_db = list(conversa.mensagens.order_by("criado_em", "id"))

    mensagem_usuario = Mensagem.objects.create(
        conversa=conversa,
        papel=Mensagem.Papel.USUARIO,
        conteudo=mensagem,
        metadados={"rotulo": rotulo[:200]} if rotulo else {},
    )

    return {
        "conversa_id": str(conversa.pk),
        "mensagem_usuario_id": mensagem_usuario.pk,
        "historico": historico_para_mensagens(historico_db),
        "comparacao_id": comparacao_id
        or (str(conversa.comparacao_id) if conversa.comparacao_id else None),
        "lote_id": lote_id or (str(conversa.lote_id) if conversa.lote_id else None),
    }


def salvar_resposta(
    *,
    conversa_id: str,
    conteudo: str,
    fontes: list[dict[str, Any]] | None = None,
    prints: dict[str, str] | None = None,
    modelo: str = "",
    erro: str = "",
    provedor_id: int | None = None,
) -> Mensagem:
    """
    Grava a resposta do agente e carimba a conversa.

    ``prints`` é o mapa ``{"3": "https://…"}`` dos marcadores citados. Sem ele
    persistido, reabrir a conversa mostraria o texto sem as imagens.

    ``metadados`` carrega o carimbo da versão que produziu a resposta — aqui, na
    criação, e não no momento do voto: reconstruir depois por aproximação de
    data erra em todo dia que teve deploy. Ver ``apps/agente/versao.py``.
    """
    from apps.agente.versao import carimbo

    resposta = Mensagem.objects.create(
        conversa_id=conversa_id,
        papel=Mensagem.Papel.AGENTE,
        conteudo=conteudo,
        modelo=modelo,
        fontes=fontes or [],
        prints=prints or {},
        metadados=carimbo(),
        erro=erro,
        provedor_id=provedor_id or None,
    )
    # update() em vez de save(): auto_now sobrescreveria com o horário do save,
    # e queremos o horário da resposta.
    Conversa.objects.filter(pk=conversa_id).update(atualizado_em=resposta.criado_em)
    return resposta
