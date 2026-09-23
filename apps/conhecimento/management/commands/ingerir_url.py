"""
Ingestão de documentação por linha de comando.

    python manage.py ingerir_url https://.../parametrizacao-fiscal --nome "Docs Senior — Fiscal"
    python manage.py ingerir_url https://.../indice --seguir-links --profundidade 2
"""
from __future__ import annotations

from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone

from apps.conhecimento.models import Documento, FonteConhecimento, TipoFonte
from apps.conhecimento.services.indexador import indexar_documento
from apps.conhecimento.services.scraper import raspar_url


class Command(BaseCommand):
    help = "Baixa uma URL de documentação, converte em markdown e indexa na base."

    def add_arguments(self, parser):
        parser.add_argument("url")
        parser.add_argument("--nome", default="", help="Nome da fonte (padrão: domínio da URL).")
        parser.add_argument("--seguir-links", action="store_true")
        parser.add_argument("--profundidade", type=int, default=1)
        parser.add_argument("--limite", type=int, default=40, help="Máx. de páginas.")
        parser.add_argument(
            "--sem-embeddings",
            action="store_true",
            help="Só cria os trechos, sem chamar o provedor de embeddings.",
        )

    def handle(self, *args, **opcoes):
        url = opcoes["url"]
        nome = opcoes["nome"] or url.split("//")[-1].split("/")[0]

        fonte, _ = FonteConhecimento.objects.get_or_create(
            nome=nome,
            defaults={
                "tipo": TipoFonte.URL,
                "url": url,
                "seguir_links": opcoes["seguir_links"],
                "profundidade_max": opcoes["profundidade"],
            },
        )

        self.stdout.write(f"Baixando {url} …")
        paginas = raspar_url(
            url,
            seguir_links=opcoes["seguir_links"],
            profundidade_max=opcoes["profundidade"],
            limite_paginas=opcoes["limite"],
        )
        if not paginas:
            raise CommandError("Nenhuma página retornada.")

        total_trechos = 0
        erros = 0
        for pagina in paginas:
            if not pagina.ok:
                erros += 1
                self.stdout.write(self.style.WARNING(f"  ✗ {pagina.url} — {pagina.erro}"))
                continue

            documento, _ = Documento.objects.update_or_create(
                fonte=fonte,
                hash_conteudo=Documento.calcular_hash(pagina.markdown),
                defaults={
                    "titulo": pagina.titulo[:400],
                    "url": pagina.url[:1000],
                    "conteudo": pagina.markdown,
                },
            )
            resultado = indexar_documento(
                documento, calcular_embeddings=not opcoes["sem_embeddings"]
            )
            total_trechos += resultado["trechos"]
            self.stdout.write(
                f"  ✓ {pagina.titulo[:70]} — {resultado['trechos']} trecho(s)"
                + (f" | {resultado['aviso']}" if resultado["aviso"] else "")
            )

        fonte.ultima_ingestao_em = timezone.now()
        fonte.ultima_ingestao_ok = erros == 0
        fonte.ultima_ingestao_detalhe = f"{len(paginas) - erros} página(s), {total_trechos} trecho(s)"
        fonte.save()

        self.stdout.write(
            self.style.SUCCESS(
                f"\nFonte '{fonte.nome}': {len(paginas) - erros} página(s) indexada(s), "
                f"{total_trechos} trecho(s), {erros} erro(s)."
            )
        )
