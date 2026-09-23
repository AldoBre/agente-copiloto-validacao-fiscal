"""
Importa a base de conhecimento versionada (``base_conhecimento/``) para o banco.

Cada pasta com ``mapa.json`` vira uma fonte do tipo "arquivo" e cada ``NN-*.md``
listado no mapa vira um documento — o mesmo upsert por hash da ingestão via API,
então rodar de novo só regrava o que mudou. Documentos que saíram do repo (ou
cujo conteúdo mudou) são removidos da fonte, para a base espelhar o repositório
em vez de acumular versões velhas.

    python manage.py importar_markdown                   # embeddings junto (se houver provedor)
    python manage.py importar_markdown --sem-embeddings  # boot: não depende do provedor de IA

Roda no boot do container (docker-entrypoint.sh), depois do ``seed_regras``, e é
idempotente e tolerante a corrida pelos mesmos motivos: o hash do conteúdo é a
chave do upsert, então instâncias concorrentes convergem para o mesmo estado.
Sem embeddings a busca cai no modo textual; ``POST /api/conhecimento/reindexar/``
completa os vetores depois, com o provedor de embeddings ativo.
"""
from __future__ import annotations

import json
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand
from django.utils import timezone

from apps.conhecimento.models import Documento, FonteConhecimento, TipoFonte
from apps.conhecimento.services.indexador import indexar_documento


class Command(BaseCommand):
    help = "Importa os markdowns de base_conhecimento/ como fontes + documentos (upsert por hash)."

    def add_arguments(self, parser):
        parser.add_argument(
            "--raiz",
            default=str(Path(settings.BASE_DIR) / "base_conhecimento"),
            help="Diretório com as pastas exportadas (uma por página, cada uma com mapa.json).",
        )
        parser.add_argument("--sem-embeddings", action="store_true")

    def handle(self, *args, **opcoes):
        raiz = Path(opcoes["raiz"])
        if not raiz.is_dir():
            self.stdout.write(self.style.WARNING(f"{raiz} não existe; nada a importar."))
            return

        mapas = sorted(raiz.glob("**/mapa.json"))
        if not mapas:
            self.stdout.write(self.style.WARNING(f"Nenhum mapa.json em {raiz}; nada a importar."))
            return

        total_docs = novos = removidos = com_embedding = 0

        for caminho_mapa in mapas:
            pasta = caminho_mapa.parent
            try:
                mapa = json.loads(caminho_mapa.read_text(encoding="utf-8"))
            except (OSError, ValueError) as exc:
                self.stderr.write(f"✗ {caminho_mapa}: mapa ilegível ({exc}); pasta ignorada.")
                continue

            info = mapa.get("fonte") or {}
            url = (info.get("url") or "")[:1000]
            relativa = pasta.relative_to(raiz).as_posix()

            # A chave é a URL, não o título: 25 páginas de regra se chamam
            # "Identificador de Regra". Agrupá-las por nome fazia a limpeza
            # abaixo apagar os documentos da pasta anterior a cada colisão —
            # sobrava só a última, e o resto sumia da base a cada boot.
            titulo = (info.get("pagina") or pasta.name)[:160]
            nome = f"{titulo} ({pasta.name})" if titulo != pasta.name else titulo
            if url:
                fonte, _ = FonteConhecimento.objects.get_or_create(
                    url=url,
                    tipo=TipoFonte.ARQUIVO,
                    defaults={"nome": nome[:200], "descricao": f"Importada do repositório ({relativa})"},
                )
            else:
                fonte, _ = FonteConhecimento.objects.get_or_create(
                    nome=nome[:200],
                    tipo=TipoFonte.ARQUIVO,
                    defaults={"url": "", "descricao": f"Importada do repositório ({relativa})"},
                )

            hashes_do_repo: set[str] = set()
            detalhes: list[str] = []
            for topico in mapa.get("topicos", []):
                arquivo = pasta / topico.get("arquivo", "")
                if not arquivo.is_file():
                    detalhes.append(f"{topico.get('arquivo')}: ausente no repo")
                    continue
                markdown = arquivo.read_text(encoding="utf-8")
                hash_conteudo = Documento.calcular_hash(markdown)
                hashes_do_repo.add(hash_conteudo)

                documento, criado = Documento.objects.update_or_create(
                    fonte=fonte,
                    hash_conteudo=hash_conteudo,
                    defaults={
                        "titulo": (topico.get("titulo") or arquivo.stem)[:400],
                        "url": (topico.get("url") or "")[:1000],
                        "conteudo": markdown,
                    },
                )
                total_docs += 1
                if criado:
                    novos += 1
                    resultado = indexar_documento(
                        documento, calcular_embeddings=not opcoes["sem_embeddings"]
                    )
                    com_embedding += resultado.get("com_embedding", 0)

            # A fonte espelha o repo: o que saiu de lá (ou mudou de hash) sai do banco.
            apagados, _ = fonte.documentos.exclude(hash_conteudo__in=hashes_do_repo).delete()
            removidos += apagados

            fonte.ultima_ingestao_em = timezone.now()
            fonte.ultima_ingestao_ok = True
            fonte.ultima_ingestao_detalhe = (
                f"importar_markdown: {len(hashes_do_repo)} documento(s)"
                + (f"; avisos: {'; '.join(detalhes)}" if detalhes else "")
            )
            fonte.save(
                update_fields=[
                    "ultima_ingestao_em", "ultima_ingestao_ok", "ultima_ingestao_detalhe"
                ]
            )

        resumo = (
            f"{len(mapas)} fonte(s), {total_docs} documento(s) no repo — "
            f"{novos} novo(s), {removidos} removido(s), {com_embedding} trecho(s) com embedding."
        )
        if opcoes["sem_embeddings"] and novos:
            resumo += " Embeddings pendentes: POST /api/conhecimento/reindexar/."
        self.stdout.write(self.style.SUCCESS(resumo))
