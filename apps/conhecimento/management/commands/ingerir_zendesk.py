"""
Ingere artigos da central de ajuda (Zendesk) da Senior.

    # 1) ver o que existe antes de baixar
    python manage.py ingerir_zendesk <url-da-categoria> --listar

    # 2) ingerir só as seções que interessam, filtrando por assunto fiscal
    python manage.py ingerir_zendesk <url-da-categoria> \
        --secoes 4404559239956 360014006852 4404566641812 \
        --fiscal --nome "Suporte Senior — Fiscal"

    # 3) sem filtro (cuidado: milhares de artigos)
    python manage.py ingerir_zendesk <url-da-categoria> --tudo

O filtro ``--fiscal`` casa o título com termos de imposto/obrigação acessória.
É o corte recomendado: a categoria inteira tem folha de pagamento, manufatura,
qualidade e outros assuntos que só diluem a busca do agente.
"""
from __future__ import annotations

import re

from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone

from apps.conhecimento.models import Documento, FonteConhecimento, TipoFonte
from apps.conhecimento.services.indexador import indexar_documento
from apps.conhecimento.services.retriever import invalidar_indice
from apps.conhecimento.services.zendesk import ClienteZendesk, extrair_id

#: Termos que identificam um artigo de interesse fiscal pelo título.
PADRAO_FISCAL = re.compile(
    r"icms|ipi|\bpis\b|cofins|\biss\b|tribut|fiscal|sped|efd|reinf|difal|"
    r"substitui|imposto|\bcfop\b|\bncm\b|\bcest\b|\bcst\b|csosn|nota fiscal|"
    r"nf-?e|nfc-?e|nfs-?e|danfe|simples nacional|retenç|aliquot|alíquot|"
    r"monofás|monofas|desonera|benefício fiscal|beneficio fiscal|apuraç",
    re.IGNORECASE,
)


class Command(BaseCommand):
    help = "Ingere artigos de uma central de ajuda Zendesk (ex.: suporte.senior.com.br)."

    def add_arguments(self, parser):
        parser.add_argument("url", help="URL da categoria ou seção do Help Center.")
        parser.add_argument("--nome", default="", help="Nome da fonte na base.")
        parser.add_argument(
            "--secoes", nargs="*", type=int, default=[], help="IDs das seções a ingerir."
        )
        parser.add_argument(
            "--fiscal",
            action="store_true",
            help="Só artigos cujo título mencione assunto fiscal (recomendado).",
        )
        parser.add_argument("--filtro", default="", help="Regex própria sobre o título.")
        parser.add_argument(
            "--tudo", action="store_true", help="Sem filtro de assunto (pode ser enorme)."
        )
        parser.add_argument("--limite", type=int, default=0, help="Máx. de artigos por seção.")
        parser.add_argument(
            "--listar", action="store_true", help="Só mostra seções e contagens."
        )
        parser.add_argument("--sem-embeddings", action="store_true")

    def handle(self, *args, **opcoes):
        url = opcoes["url"]
        identificador = extrair_id(url)
        if identificador is None:
            raise CommandError(
                "Não encontrei o id na URL. Use o link de uma categoria "
                "(/hc/pt-br/categories/<id>-...) ou de uma seção (/sections/<id>-...)."
            )
        e_secao = "/sections/" in url

        if opcoes["filtro"]:
            filtro = re.compile(opcoes["filtro"], re.IGNORECASE)
        elif opcoes["tudo"]:
            filtro = None
        else:
            filtro = PADRAO_FISCAL
            if not opcoes["fiscal"]:
                self.stdout.write(
                    self.style.WARNING(
                        "Aplicando o filtro fiscal por padrão. Use --tudo para ingerir "
                        "a categoria inteira.\n"
                    )
                )

        with ClienteZendesk(url) as cliente:
            # ------------------------------------------------------ listagem --
            if opcoes["listar"]:
                if e_secao:
                    self.stdout.write(
                        f"Seção {identificador}: {cliente.contar_secao(identificador)} artigo(s)"
                    )
                    return
                total = cliente.contar_categoria(identificador)
                self.stdout.write(f"Categoria {identificador}: {total} artigo(s)\n")
                self.stdout.write("Seções:")
                for secao in cliente.secoes_da_categoria(identificador):
                    quantidade = cliente.contar_secao(secao["id"])
                    self.stdout.write(f"  {secao['id']:>16}  {quantidade:>5}  {secao['name']}")
                self.stdout.write(
                    "\nUse --secoes <id> <id> ... para escolher, e --fiscal para filtrar "
                    "por assunto."
                )
                return

            # ------------------------------------------------------ ingestão --
            if not e_secao:
                cliente.secoes_da_categoria(identificador)

            alvos: list[tuple[str, dict]]
            if e_secao:
                alvos = [(f"seção {identificador}", {"secao_id": identificador})]
            elif opcoes["secoes"]:
                alvos = [(f"seção {s}", {"secao_id": s}) for s in opcoes["secoes"]]
            else:
                alvos = [("categoria inteira", {"categoria_id": identificador})]

            nome = opcoes["nome"] or "Central de ajuda Senior"
            fonte, _ = FonteConhecimento.objects.get_or_create(
                nome=nome, defaults={"tipo": TipoFonte.URL, "url": url[:1000]}
            )
            fonte.url = url[:1000]
            fonte.descricao = (
                f"Zendesk — {'seções ' + ', '.join(map(str, opcoes['secoes'])) if opcoes['secoes'] else 'categoria'} "
                f"{identificador}{' · filtro fiscal' if filtro else ''}"
            )
            fonte.save()

            total_artigos = 0
            total_trechos = 0
            avisos: set[str] = set()

            for rotulo, parametros in alvos:
                self.stdout.write(f"\n→ {rotulo}")
                for artigo in cliente.artigos(
                    filtro_titulo=filtro,
                    limite=opcoes["limite"] or None,
                    **parametros,
                ):
                    documento, _ = Documento.objects.update_or_create(
                        fonte=fonte,
                        hash_conteudo=Documento.calcular_hash(artigo.markdown),
                        defaults={
                            "titulo": artigo.titulo,
                            "url": artigo.url[:1000],
                            "conteudo": artigo.markdown,
                        },
                    )
                    resultado = indexar_documento(
                        documento, calcular_embeddings=not opcoes["sem_embeddings"]
                    )
                    total_artigos += 1
                    total_trechos += resultado["trechos"]
                    if resultado["aviso"]:
                        avisos.add(resultado["aviso"])

                    if total_artigos % 25 == 0:
                        self.stdout.write(
                            f"   {total_artigos} artigo(s), {total_trechos} trecho(s)…"
                        )

            fonte.ultima_ingestao_em = timezone.now()
            fonte.ultima_ingestao_ok = True
            fonte.ultima_ingestao_detalhe = (
                f"{total_artigos} artigo(s), {total_trechos} trecho(s)."
            )
            fonte.save()

        invalidar_indice()

        self.stdout.write("")
        self.stdout.write(
            self.style.SUCCESS(
                f"{total_artigos} artigo(s) indexado(s), {total_trechos} trecho(s) "
                f"na fonte '{fonte.nome}'."
            )
        )
        for aviso in avisos:
            self.stdout.write(self.style.WARNING(f"  ! {aviso}"))
