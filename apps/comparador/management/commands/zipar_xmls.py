"""
Separa os XMLs de uma pasta em dois ZIPs (cliente × Senior) por padrão no nome.

    python manage.py zipar_xmls xml_example
    python manage.py zipar_xmls /caminho/dos/xmls --cliente Original --senior Simulada
    python manage.py zipar_xmls ./notas --cliente legado --senior senior --destino exemplos

Útil quando o consultor recebe tudo numa pasta só: em vez de separar na mão,
marca-se o padrão que identifica cada lado no nome do arquivo.
"""
from __future__ import annotations

import zipfile
from pathlib import Path

from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Separa os XMLs de uma pasta em dois ZIPs (sistema atual × ERP Senior)."

    def add_arguments(self, parser):
        parser.add_argument("pasta", help="Pasta com os arquivos .xml")
        parser.add_argument(
            "--cliente",
            default="Original",
            help="Trecho do nome que identifica o XML do sistema atual (padrão: Original).",
        )
        parser.add_argument(
            "--senior",
            default="Simulada",
            help="Trecho do nome que identifica o XML gerado pelo Senior (padrão: Simulada).",
        )
        parser.add_argument(
            "--destino", default="", help="Onde gravar os ZIPs (padrão: a própria pasta)."
        )
        parser.add_argument("--prefixo", default="", help="Prefixo dos arquivos ZIP gerados.")

    def handle(self, *args, **opcoes):
        pasta = Path(opcoes["pasta"]).expanduser()
        if not pasta.is_dir():
            raise CommandError(f"Pasta não encontrada: {pasta}")

        destino = Path(opcoes["destino"]).expanduser() if opcoes["destino"] else pasta
        destino.mkdir(parents=True, exist_ok=True)

        marca_cliente = opcoes["cliente"].casefold()
        marca_senior = opcoes["senior"].casefold()

        xmls = sorted(p for p in pasta.rglob("*.xml") if p.is_file())
        if not xmls:
            raise CommandError(f"Nenhum .xml encontrado em {pasta}")

        do_cliente: list[Path] = []
        do_senior: list[Path] = []
        indefinidos: list[Path] = []

        for arquivo in xmls:
            nome = arquivo.name.casefold()
            tem_cliente = marca_cliente in nome
            tem_senior = marca_senior in nome
            if tem_cliente and not tem_senior:
                do_cliente.append(arquivo)
            elif tem_senior and not tem_cliente:
                do_senior.append(arquivo)
            else:
                indefinidos.append(arquivo)

        if indefinidos:
            self.stdout.write(
                self.style.WARNING(
                    f"{len(indefinidos)} arquivo(s) não casaram com nenhum dos padrões "
                    "(ou casaram com os dois) e ficaram de fora:"
                )
            )
            for arquivo in indefinidos[:10]:
                self.stdout.write(f"    {arquivo.name}")
            if len(indefinidos) > 10:
                self.stdout.write(f"    … e mais {len(indefinidos) - 10}")

        if not do_cliente or not do_senior:
            raise CommandError(
                "Um dos lados ficou vazio "
                f"(cliente: {len(do_cliente)}, Senior: {len(do_senior)}). "
                "Ajuste --cliente / --senior para os padrões que aparecem nos nomes."
            )

        prefixo = opcoes["prefixo"]
        caminho_cliente = destino / f"{prefixo}sistema_atual.zip"
        caminho_senior = destino / f"{prefixo}senior.zip"

        for caminho, arquivos in ((caminho_cliente, do_cliente), (caminho_senior, do_senior)):
            with zipfile.ZipFile(caminho, "w", zipfile.ZIP_DEFLATED) as pacote:
                for arquivo in arquivos:
                    pacote.write(arquivo, arcname=arquivo.name)

        self.stdout.write(
            self.style.SUCCESS(f"\n{caminho_cliente}  —  {len(do_cliente)} XML(s) do sistema atual")
        )
        for arquivo in do_cliente[:5]:
            self.stdout.write(f"    {arquivo.name}")
        if len(do_cliente) > 5:
            self.stdout.write(f"    … e mais {len(do_cliente) - 5}")

        self.stdout.write(
            self.style.SUCCESS(f"\n{caminho_senior}  —  {len(do_senior)} XML(s) do ERP Senior")
        )
        for arquivo in do_senior[:5]:
            self.stdout.write(f"    {arquivo.name}")
        if len(do_senior) > 5:
            self.stdout.write(f"    … e mais {len(do_senior) - 5}")

        self.stdout.write("\nSuba os dois na aba 'Em massa' do painel.")
