"""
Carrega as tabelas oficiais de ``dados_fiscais/`` para o banco.

    python manage.py importar_tabelas_fiscais
    python manage.py importar_tabelas_fiscais --tabela ncm --tabela tipi

Os arquivos são versionados no repositório de propósito: a API do NCM só
descreve o presente e a URL da TIPI é fixa com conteúdo mutável, então o
snapshot datado é a única forma de auditar uma nota antiga depois. Cada
importação registra hash e data de captura em :class:`VersaoTabela`.

Idempotente: reimportar não duplica nada e não derruba a tabela anterior
enquanto a nova não estiver pronta.
"""
from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import transaction

from apps.fiscal.models import Cest, Cfop, FcpUf, Ncm, TipiAliquota, VersaoTabela
from apps.fiscal.services import importadores

#: tabela → (arquivo, leitor, model, campos-chave para o update_or_create)
FONTES = {
    "ncm": ("ncm.json", importadores.ler_ncm, Ncm, ("codigo",)),
    "tipi": ("tipi.xlsx", importadores.ler_tipi, TipiAliquota, ("ncm", "ex")),
    "cest": ("cest_conv142.html", importadores.ler_cest, Cest, None),
    "cfop": ("cfop.xlsx", importadores.ler_cfop, Cfop, ("codigo",)),
    "fcp": ("fcp.xlsx", importadores.ler_fcp, FcpUf, ("uf",)),
}


class Command(BaseCommand):
    help = "Importa as tabelas fiscais oficiais para o banco."

    def add_arguments(self, parser):
        parser.add_argument(
            "--tabela",
            action="append",
            choices=sorted(FONTES),
            help="Importa só a(s) tabela(s) indicada(s). Sem isto, importa todas.",
        )
        parser.add_argument(
            "--dados",
            default=str(Path(settings.BASE_DIR) / "dados_fiscais"),
            help="Diretório com os arquivos oficiais baixados.",
        )
        parser.add_argument(
            "--forcar",
            action="store_true",
            help="Reimporta mesmo que o arquivo não tenha mudado desde a última carga.",
        )

    def handle(self, *args, **opcoes):
        raiz = Path(opcoes["dados"])
        alvos = opcoes["tabela"] or sorted(FONTES)

        for nome in alvos:
            arquivo, leitor, model, chaves = FONTES[nome]
            caminho = raiz / arquivo
            if not caminho.is_file():
                self.stderr.write(self.style.WARNING(f"✗ {nome}: {caminho} não existe."))
                continue

            # O comando roda a cada boot do container. Reprocessar 26 mil
            # registros quando nada mudou é desperdício puro — o hash do
            # arquivo diz em milissegundos se há trabalho a fazer.
            impressao = importadores.hash_arquivo(caminho)
            atual = VersaoTabela.objects.filter(tabela=nome).first()
            if atual and atual.hash_arquivo == impressao and not opcoes["forcar"]:
                self.stdout.write(
                    f"= {nome}: inalterado desde a última carga "
                    f"({atual.registros} registros)."
                )
                continue

            self.stdout.write(f"→ {nome}: lendo {arquivo}…")
            try:
                registros, referencia = leitor(caminho)
            except Exception as exc:  # noqa: BLE001
                self.stderr.write(self.style.ERROR(f"✗ {nome}: falha ao ler ({exc})"))
                continue

            if not registros:
                self.stderr.write(self.style.WARNING(f"✗ {nome}: nenhum registro lido."))
                continue

            with transaction.atomic():
                if chaves is None:
                    # CEST não tem chave natural (o mesmo código aparece em
                    # vários anexos e casa com vários NCM): recria a tabela.
                    model.objects.all().delete()
                    model.objects.bulk_create(
                        [model(**r) for r in registros], batch_size=1000
                    )
                else:
                    self._sincronizar(model, chaves, registros)

                VersaoTabela.objects.update_or_create(
                    tabela=nome,
                    defaults={
                        "referencia": referencia,
                        "hash_arquivo": impressao,
                        "registros": len(registros),
                        # Data do arquivo, não de agora: é quando a fonte foi
                        # de fato capturada.
                        "capturado_em": datetime.fromtimestamp(
                            caminho.stat().st_mtime, tz=timezone.utc
                        ),
                    },
                )

            self.stdout.write(
                self.style.SUCCESS(
                    f"  {len(registros)} registro(s) · {referencia[:70] or 'sem referência'}"
                )
            )

        self._resumo()

    def _sincronizar(self, model, chaves, registros) -> None:
        """
        Atualiza o que mudou, cria o que falta e apaga o que saiu da fonte.

        Recriar do zero seria mais simples, mas deixaria a tabela vazia por
        alguns segundos — e uma consulta nesse intervalo responderia "NCM não
        existe" para um código perfeitamente válido.
        """
        existentes = {
            tuple(getattr(obj, c) for c in chaves): obj for obj in model.objects.all()
        }
        vistos = set()
        criar, atualizar = [], []

        campos = [c for c in registros[0] if c not in chaves]
        for registro in registros:
            chave = tuple(registro[c] for c in chaves)
            if chave in vistos:
                continue  # a fonte pode repetir; a primeira ocorrência vence
            vistos.add(chave)

            atual = existentes.get(chave)
            if atual is None:
                criar.append(model(**registro))
                continue
            mudou = False
            for campo in campos:
                if getattr(atual, campo) != registro[campo]:
                    setattr(atual, campo, registro[campo])
                    mudou = True
            if mudou:
                atualizar.append(atual)

        if criar:
            model.objects.bulk_create(criar, batch_size=1000)
        if atualizar:
            model.objects.bulk_update(atualizar, campos, batch_size=500)

        saiu = [obj.pk for chave, obj in existentes.items() if chave not in vistos]
        if saiu:
            model.objects.filter(pk__in=saiu).delete()

    def _resumo(self) -> None:
        self.stdout.write("")
        self.stdout.write("Estado das tabelas:")
        for versao in VersaoTabela.objects.all():
            self.stdout.write(
                f"  {versao.tabela:6} {versao.registros:>7} registros  "
                f"capturado {versao.capturado_em:%d/%m/%Y}  {versao.referencia[:50]}"
            )
