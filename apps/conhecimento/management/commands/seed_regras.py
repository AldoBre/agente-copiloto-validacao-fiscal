"""
Semeia ``RegraParametrizacao`` com o mapa estático de pistas do comparador.

    python manage.py seed_regras            # só cria o que falta
    python manage.py seed_regras --forcar   # sobrescreve orientações editadas

Depois disso, o consultor refina cada linha no /admin (ou pela API) com os
nomes de rotina/tela da versão do Senior que está sendo implantada. O agente
lê primeiro daqui e só depois cai no mapa estático do código.
"""
from django.core.management.base import BaseCommand

from apps.comparador.services.mapa_campos import categoria_do_grupo, todas_as_pistas
from apps.conhecimento.models import RegraParametrizacao


class Command(BaseCommand):
    help = "Cria/atualiza as regras de parametrização a partir do mapa de campos."

    def add_arguments(self, parser):
        parser.add_argument(
            "--forcar",
            action="store_true",
            help="Sobrescreve a orientação de regras já existentes.",
        )

    def handle(self, *args, **opcoes):
        criadas = 0
        atualizadas = 0

        for chave, orientacao in todas_as_pistas().items():
            grupo = chave.split(".", 1)[0] if "." in chave else ""
            categoria = categoria_do_grupo(grupo) if grupo else ""

            # get_or_create: duas instâncias semeando ao mesmo tempo (deploy com
            # scale-out) não podem estourar o unique de `campo`.
            regra, criada = RegraParametrizacao.objects.get_or_create(
                campo=chave,
                defaults={"categoria": categoria, "orientacao": orientacao},
            )
            if criada:
                criadas += 1
            elif opcoes["forcar"]:
                regra.categoria = categoria
                regra.orientacao = orientacao
                regra.save(update_fields=["categoria", "orientacao"])
                atualizadas += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"{criadas} regra(s) criada(s), {atualizadas} atualizada(s). "
                f"Total na base: {RegraParametrizacao.objects.count()}."
            )
        )
