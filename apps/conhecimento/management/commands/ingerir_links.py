"""
Ingere de uma vez todas as páginas de uma lista de links.

    # a partir do Word que a equipe montou
    python manage.py ingerir_links --arquivo "Links de documentações Senior.docx" \
        --nome "Documentação Senior — Fiscal"

    # ou passando as URLs direto
    python manage.py ingerir_links https://... https://... --nome "Fiscal"

Links de portal de ajuda (``.../#pagina.htm?TocPath=...``) são resolvidos para a
URL do conteúdo automaticamente — sem isso, o download traz só a casca de
navegação.
"""
from __future__ import annotations

from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone

from apps.conhecimento.models import Documento, FonteConhecimento, TipoFonte
from apps.conhecimento.services.extrator_links import extrair_de_arquivo
from apps.conhecimento.services.indexador import indexar_documento
from apps.conhecimento.services.scraper import raspar_url, resolver_url


class Command(BaseCommand):
    help = "Ingere várias páginas de documentação de uma lista de links."

    def add_arguments(self, parser):
        parser.add_argument("urls", nargs="*", help="URLs a ingerir.")
        parser.add_argument(
            "--arquivo", default="", help="Arquivo .docx/.txt/.md de onde extrair os links."
        )
        parser.add_argument("--nome", default="", help="Nome da fonte na base.")
        parser.add_argument(
            "--sem-embeddings",
            action="store_true",
            help="Só cria os trechos, sem chamar o provedor de embeddings.",
        )
        parser.add_argument(
            "--listar",
            action="store_true",
            help="Só mostra os links resolvidos, sem baixar nada.",
        )

    def handle(self, *args, **opcoes):
        urls = list(opcoes["urls"])
        if opcoes["arquivo"]:
            try:
                urls += extrair_de_arquivo(opcoes["arquivo"])
            except (FileNotFoundError, ValueError) as exc:
                raise CommandError(str(exc)) from exc

        # dedup preservando a ordem, já resolvendo o fragmento
        vistas: set[str] = set()
        resolvidas: list[str] = []
        for bruta in urls:
            destino = resolver_url(bruta)
            if destino not in vistas:
                vistas.add(destino)
                resolvidas.append(destino)

        if not resolvidas:
            raise CommandError("Nenhuma URL encontrada. Use --arquivo ou passe as URLs.")

        if opcoes["listar"]:
            self.stdout.write(f"{len(resolvidas)} URL(s):")
            for u in resolvidas:
                self.stdout.write(f"  {u}")
            return

        nome = opcoes["nome"] or (
            opcoes["arquivo"].rsplit("/", 1)[-1].rsplit(".", 1)[0]
            if opcoes["arquivo"]
            else resolvidas[0].split("//")[-1].split("/")[0]
        )

        fonte, _ = FonteConhecimento.objects.get_or_create(
            nome=nome, defaults={"tipo": TipoFonte.LISTA}
        )
        fonte.tipo = TipoFonte.LISTA
        fonte.urls = resolvidas
        fonte.save()

        self.stdout.write(f"Fonte '{fonte.nome}' — {len(resolvidas)} página(s) a ingerir.\n")

        total_trechos = 0
        erros: list[str] = []
        avisos: set[str] = set()

        for indice, url in enumerate(resolvidas, start=1):
            self.stdout.write(f"[{indice}/{len(resolvidas)}] {url}")
            paginas = raspar_url(url)
            if not paginas:
                erros.append(f"{url}: sem resposta")
                continue

            pagina = paginas[0]
            if not pagina.ok:
                erros.append(f"{url}: {pagina.erro or 'conteúdo vazio'}")
                self.stdout.write(self.style.WARNING(f"    ✗ {pagina.erro}"))
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
            if resultado["aviso"]:
                avisos.add(resultado["aviso"])

            self.stdout.write(
                self.style.SUCCESS(
                    f"    ✓ {pagina.titulo[:60]} — {len(pagina.markdown)} chars, "
                    f"{resultado['trechos']} trecho(s)"
                )
            )

        fonte.ultima_ingestao_em = timezone.now()
        fonte.ultima_ingestao_ok = not erros
        fonte.ultima_ingestao_detalhe = (
            f"{len(resolvidas) - len(erros)}/{len(resolvidas)} página(s), {total_trechos} trecho(s)."
        )
        fonte.save()

        self.stdout.write("")
        self.stdout.write(
            self.style.SUCCESS(
                f"{len(resolvidas) - len(erros)} página(s) indexada(s), "
                f"{total_trechos} trecho(s), {len(erros)} erro(s)."
            )
        )
        for aviso in avisos:
            self.stdout.write(self.style.WARNING(f"  ! {aviso}"))
        for erro in erros:
            self.stdout.write(self.style.ERROR(f"  ✗ {erro}"))
