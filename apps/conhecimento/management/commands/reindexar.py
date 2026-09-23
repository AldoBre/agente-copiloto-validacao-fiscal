"""
Recria trechos e embeddings de toda a base.

    python manage.py reindexar
    python manage.py reindexar --sem-embeddings

Rode sempre que trocar o modelo de embeddings — vetores de modelos diferentes
não são comparáveis entre si.
"""
from django.core.management.base import BaseCommand

from apps.conhecimento.services.indexador import reindexar_tudo


class Command(BaseCommand):
    help = "Reindexa todos os documentos da base de conhecimento."

    def add_arguments(self, parser):
        parser.add_argument("--sem-embeddings", action="store_true")
        parser.add_argument(
            "--apenas-pendentes",
            action="store_true",
            help="Só o que ainda não tem vetor — completa uma importação sem recomprar embeddings.",
        )
        parser.add_argument("--limite", type=int, default=0, help="Processa no máximo N documentos.")

    def handle(self, *args, **opcoes):
        resultado = reindexar_tudo(
            calcular_embeddings=not opcoes["sem_embeddings"],
            apenas_pendentes=opcoes["apenas_pendentes"],
            limite=opcoes["limite"] or None,
        )
        self.stdout.write(
            self.style.SUCCESS(
                f"{resultado['processados']} documento(s) processado(s) de "
                f"{resultado['documentos']} na base, {resultado['trechos']} trecho(s), "
                f"{resultado['com_embedding']} com embedding. "
                f"Pendentes: {resultado['pendentes']}."
            )
        )
        for aviso in resultado["avisos"]:
            self.stdout.write(self.style.WARNING(f"  ! {aviso}"))
