"""
Normaliza as URLs de imagem do conteúdo já ingerido, **sem recalcular embeddings**.

    python manage.py corrigir_imagens --simular   # só relatório, não grava
    python manage.py corrigir_imagens

Por que não usar ``reindexar``: ele reprocessa tudo e refaz os 3.934 embeddings,
o que custa dinheiro e ~1h. Uma URL de imagem não muda o significado semântico do
trecho — trocar ``/attachments/token/x`` por ``https://host/attachments/token/x``
não move o vetor para lugar nenhum de útil. Então dá para reescrever o texto no
lugar e manter o vetor que já existe.
"""
from __future__ import annotations

from django.core.management.base import BaseCommand
from django.db import transaction

from apps.conhecimento.models import Documento, Trecho
from apps.conhecimento.services.imagens import normalizar_markdown
from apps.conhecimento.services.retriever import invalidar_indice


class Command(BaseCommand):
    help = "Converte URLs de imagem para absolutas e remove imagens decorativas."

    def add_arguments(self, parser):
        parser.add_argument(
            "--simular", action="store_true", help="Mostra o que mudaria, sem gravar."
        )

    def handle(self, *args, **opcoes):
        simular = opcoes["simular"]
        docs_tocados = trechos_tocados = 0
        total_norm = total_desc = 0

        for documento in Documento.objects.all().iterator():
            base = documento.url or ""
            conteudo, norm_doc, desc_doc = normalizar_markdown(documento.conteudo, base)

            mudou_trecho = False
            trechos_novos = []
            for trecho in documento.trechos.all():
                texto, n, d = normalizar_markdown(trecho.texto, base)
                total_norm += n
                total_desc += d
                if texto != trecho.texto:
                    trecho.texto = texto
                    trechos_novos.append(trecho)
                    mudou_trecho = True

            if conteudo == documento.conteudo and not mudou_trecho:
                continue

            docs_tocados += 1
            trechos_tocados += len(trechos_novos)

            if not simular:
                with transaction.atomic():
                    if conteudo != documento.conteudo:
                        documento.conteudo = conteudo
                        documento.save(update_fields=["conteudo"])
                    if trechos_novos:
                        # Só o texto: 'embedding' e 'modelo_embedding' ficam como
                        # estão, de propósito — ver o docstring do módulo.
                        Trecho.objects.bulk_update(trechos_novos, ["texto"], batch_size=200)

        if not simular:
            invalidar_indice()

        prefixo = "[simulação] " if simular else ""
        self.stdout.write(
            self.style.SUCCESS(
                f"{prefixo}{docs_tocados} documento(s) e {trechos_tocados} trecho(s) "
                f"ajustados · {total_norm} URL(s) normalizada(s) · "
                f"{total_desc} imagem(ns) decorativa(s) removida(s)."
            )
        )
        if simular:
            self.stdout.write("Rode sem --simular para aplicar.")
