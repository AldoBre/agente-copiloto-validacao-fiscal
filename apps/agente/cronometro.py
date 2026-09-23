"""
Cronômetro de um turno do chat — para onde vai o tempo de uma resposta.

Existe por causa de uma pergunta concreta (20/09/2026): "por que a análise de
duas NFS-e leva 2 minutos?". O código permitia três respostas — raciocínio longo
do modelo, várias idas ao provedor no ciclo de ferramentas, ou cota estourada —
e cada uma pede uma correção diferente. Sem medir, qualquer ajuste é palpite.

Ele só observa os eventos que o ``astream_events`` já emite; não muda o fluxo.
Tudo aqui é defensivo de propósito: um log de tempo nunca pode derrubar o chat
de quem está no meio de uma implantação.

O que sai no log (nível INFO, logger ``apps.agente.cronometro``)::

    [tempo] no recuperar: 0.3s
    [tempo] ida 1 ao modelo: 31.2s · entrada 14210 tok · saida 1840 tok
            (raciocinio 1500) · pediu 3 consulta(s)
    [tempo] no ferramentas: 0.1s
    [tempo] ida 2 ao modelo: 48.7s · entrada 15102 tok · saida 3120 tok ...
    [tempo] TURNO: 80.9s · 2 ida(s) ao modelo = 79.9s (99%) · 1o token visivel
            aos 33.4s

Como ler: se quase tudo está nas idas ao modelo e ``raciocinio`` domina a saída,
o remédio é ``reasoning_effort``; se são muitas idas, é ``MAX_PASSOS_FERRAMENTA``;
se uma ida isolada demora muito com pouca saída, é cota (throttling) do provedor.
"""
from __future__ import annotations

import logging
import time
from typing import Any

logger = logging.getLogger(__name__)

#: Nós do grafo cujo tempo interessa separar do tempo de modelo.
_NOS = {"preparar", "recuperar", "montar_prompt", "ferramentas"}


class Cronometro:
    def __init__(self) -> None:
        self._t0 = time.perf_counter()
        self._inicio_no: dict[str, float] = {}
        self._inicio_ida: float | None = None
        self._idas: list[float] = []
        self._primeiro_token: float | None = None

    # ------------------------------------------------------------ eventos ---
    def observar(self, evento: dict[str, Any]) -> None:
        """Recebe cada evento do ``astream_events``. Nunca levanta."""
        try:
            self._observar(evento)
        except Exception:  # noqa: BLE001
            logger.debug("cronometro: evento ignorado", exc_info=True)

    def _observar(self, evento: dict[str, Any]) -> None:
        tipo = evento.get("event")
        nome = evento.get("name") or ""
        agora = time.perf_counter()

        if tipo == "on_chain_start" and nome in _NOS:
            self._inicio_no[nome] = agora

        elif tipo == "on_chain_end" and nome in _NOS and nome in self._inicio_no:
            logger.info("[tempo] no %s: %.1fs", nome, agora - self._inicio_no.pop(nome))

        elif tipo == "on_chat_model_start":
            self._inicio_ida = agora

        elif tipo == "on_chat_model_end" and self._inicio_ida is not None:
            duracao = agora - self._inicio_ida
            self._inicio_ida = None
            self._idas.append(duracao)
            saida = (evento.get("data") or {}).get("output")
            logger.info(
                "[tempo] ida %d ao modelo: %.1fs%s",
                len(self._idas),
                duracao,
                _resumo_de_uso(saida),
            )

    def token_visivel(self) -> None:
        """Chame quando o primeiro texto for para a tela."""
        if self._primeiro_token is None:
            self._primeiro_token = time.perf_counter() - self._t0

    # -------------------------------------------------------------- resumo ---
    def fechar(self) -> dict[str, Any]:
        """Loga o resumo do turno e devolve os números (vão no evento ``fim``)."""
        total = time.perf_counter() - self._t0
        no_modelo = sum(self._idas)
        resumo = {
            "total_s": round(total, 1),
            "idas_ao_modelo": len(self._idas),
            "tempo_no_modelo_s": round(no_modelo, 1),
            "primeiro_token_s": (
                round(self._primeiro_token, 1) if self._primeiro_token is not None else None
            ),
        }
        try:
            logger.info(
                "[tempo] TURNO: %.1fs · %d ida(s) ao modelo = %.1fs (%d%%) · 1o token visivel %s",
                total,
                len(self._idas),
                no_modelo,
                round(100 * no_modelo / total) if total else 0,
                f"aos {self._primeiro_token:.1f}s" if self._primeiro_token is not None else "nunca",
            )
        except Exception:  # noqa: BLE001
            pass
        return resumo


def _resumo_de_uso(saida: Any) -> str:
    """Tokens de entrada/saída/raciocínio e consultas pedidas, quando o provedor informa."""
    partes: list[str] = []
    uso = getattr(saida, "usage_metadata", None) or {}
    if uso.get("input_tokens") is not None:
        partes.append(f"entrada {uso['input_tokens']} tok")
    if uso.get("output_tokens") is not None:
        texto = f"saida {uso['output_tokens']} tok"
        raciocinio = (uso.get("output_token_details") or {}).get("reasoning")
        if raciocinio:
            texto += f" (raciocinio {raciocinio})"
        partes.append(texto)
    chamadas = getattr(saida, "tool_calls", None) or []
    if chamadas:
        partes.append(f"pediu {len(chamadas)} consulta(s)")
    return (" · " + " · ".join(partes)) if partes else ""
