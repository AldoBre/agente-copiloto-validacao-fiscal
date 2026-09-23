"""
Conversa com o agente pelo terminal — sem abrir a UI, sem subir XML.

    # o que a base responde, sem gastar token de chat
    python manage.py perguntar "aliquota de ICMS por UF de destino" --so-busca

    # pergunta de verdade, com resposta em streaming
    python manage.py perguntar "Onde ajusto a aliquota de ICMS?"

    # com o contexto de um lote já comparado (é assim que a UI chama)
    python manage.py perguntar "Analise as divergencias" --lote <uuid>
    python manage.py perguntar "Analise as divergencias" --ultimo-lote

    # ver exatamente o que vai para o provedor, sem chamar o provedor
    python manage.py perguntar "Analise as divergencias" --ultimo-lote --so-prompt

Serve para iterar no prompt: ``--so-prompt`` mostra o payload final (já com os
dados pessoais mascarados) e ``--so-busca`` isola a recuperação, que é onde
mora a maior parte dos problemas de resposta ruim.
"""
from __future__ import annotations

import asyncio
import sys
import time

from django.core.management.base import BaseCommand, CommandError

from apps.agente.graph import no_montar_prompt, no_preparar, no_recuperar
from apps.agente.privacidade import encontrar_dados_pessoais
from apps.provedores.factory import ProvedorIndisponivel, construir_chat
from apps.provedores.models import ProvedorIA, TipoModelo


class Command(BaseCommand):
    help = "Faz uma pergunta ao agente fiscal pelo terminal."

    def add_arguments(self, parser):
        parser.add_argument("pergunta", help="A pergunta.")
        parser.add_argument("--lote", default="", help="UUID de um lote comparado.")
        parser.add_argument("--comparacao", default="", help="UUID de uma comparação.")
        parser.add_argument(
            "--ultimo-lote",
            action="store_true",
            help="Usa o lote comparado mais recente como contexto.",
        )
        parser.add_argument("--top-k", type=int, default=6, help="Trechos recuperados.")
        parser.add_argument(
            "--so-busca", action="store_true", help="Só a recuperação; não chama o modelo."
        )
        parser.add_argument(
            "--so-prompt",
            action="store_true",
            help="Mostra o payload que iria para o provedor; não chama o modelo.",
        )

    # ------------------------------------------------------------------ #
    def handle(self, *args, **opcoes):
        lote_id = opcoes["lote"]
        if opcoes["ultimo_lote"]:
            from apps.comparador.models import Lote

            lote = (
                Lote.objects.exclude(relatorio_markdown="").order_by("-criado_em").first()
            )
            if lote is None:
                raise CommandError(
                    "Nenhum lote comparado no banco. Suba os ZIPs na tela e rode a "
                    "comparação, ou use sem --ultimo-lote para perguntar só sobre a base."
                )
            lote_id = str(lote.pk)
            self.stdout.write(self.style.NOTICE(f"Contexto: lote {lote_id}"))

        estado = {
            "pergunta": opcoes["pergunta"],
            "lote_id": lote_id or None,
            "comparacao_id": opcoes["comparacao"] or None,
        }

        # --------------------------------------------------------- preparar --
        estado |= asyncio.run(no_preparar(estado))
        relatorio = estado.get("relatorio") or ""
        if relatorio:
            residuo = encontrar_dados_pessoais(relatorio)
            marca = self.style.SUCCESS("limpo") if not residuo else self.style.ERROR(residuo)
            self.stdout.write(f"Relatório: {len(relatorio)} chars · dado pessoal: {marca}")
        else:
            self.stdout.write(
                self.style.WARNING("Sem comparação anexada — respondendo só com a base.")
            )

        # -------------------------------------------------------- recuperar --
        inicio = time.perf_counter()
        from django.conf import settings

        settings.AGENTE["TOP_K_CONTEXTO"] = opcoes["top_k"]
        estado |= asyncio.run(no_recuperar(estado))
        ms = (time.perf_counter() - inicio) * 1000

        contexto = estado.get("contexto", [])
        self.stdout.write(f"\nRecuperados {len(contexto)} trecho(s) em {ms:.0f} ms:")
        for i, t in enumerate(contexto, 1):
            self.stdout.write(
                f"  [{i}] {t.get('score', 0):.3f} {t.get('origem', ''):9} "
                f"{t.get('documento', '')[:72]}"
            )
        if regras := estado.get("regras", []):
            self.stdout.write(f"Regras da equipe: {[r['campo'] for r in regras]}")

        if opcoes["so_busca"]:
            return

        # ----------------------------------------------------- montar prompt --
        estado |= asyncio.run(no_montar_prompt(estado))
        mensagens = estado["mensagens"]
        total = sum(len(m.content) for m in mensagens)
        self.stdout.write(
            f"\nPayload: {len(mensagens)} mensagem(ns), {total} chars "
            f"(~{total // 4} tokens de entrada)"
        )

        if opcoes["so_prompt"]:
            for m in mensagens:
                self.stdout.write(self.style.NOTICE(f"\n===== {type(m).__name__} ====="))
                self.stdout.write(m.content)
            return

        # ---------------------------------------------------------- responder --
        provedor = ProvedorIA.obter_padrao(TipoModelo.CHAT)
        if provedor is None:
            raise CommandError(
                "Nenhum modelo de chat ativo. Cadastre um em Configurações e marque "
                "'Usar este'."
            )
        try:
            modelo = construir_chat(provedor, streaming=True)
        except ProvedorIndisponivel as exc:
            raise CommandError(str(exc)) from exc

        self.stdout.write(self.style.NOTICE(f"\n===== {provedor.nome} =====\n"))
        inicio = time.perf_counter()
        primeiro_token = None
        try:
            for pedaco in modelo.stream(mensagens):
                conteudo = pedaco.content
                if isinstance(conteudo, list):  # blocos (Anthropic e afins)
                    conteudo = "".join(
                        b.get("text", "") for b in conteudo if isinstance(b, dict)
                    )
                if conteudo:
                    if primeiro_token is None:
                        primeiro_token = time.perf_counter() - inicio
                    sys.stdout.write(str(conteudo))
                    sys.stdout.flush()
        except Exception as exc:  # noqa: BLE001 — mesma tradução que a UI mostra
            from apps.provedores.erros import explicar

            raise CommandError(explicar(exc)) from None

        total_s = time.perf_counter() - inicio
        self.stdout.write(
            self.style.SUCCESS(
                f"\n\n— 1º token em {(primeiro_token or 0):.1f}s · total {total_s:.1f}s"
            )
        )
