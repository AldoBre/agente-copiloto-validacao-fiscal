"""
Exporta uma página da documentação como **um arquivo markdown por tópico**, mais
um ``mapa.json`` com telas, identificadores de regras e campos do XML de cada um.

    python manage.py exportar_markdown \
        "https://documentacao.senior.com.br/gestaoempresarialerp/5.10.4/geral/impostos-icms.htm" \
        --destino base_conhecimento/senior/5.10.4/impostos-icms

Por que arquivo, e não ingestão direta: a documentação da Senior é genérica e a
parametrização real varia por implantação. Em arquivo, a equipe revisa, corrige e
anota antes de virar embedding — e o resultado fica versionado, então dá para ver
o que mudou quando a Senior atualiza a página.

Depois de revisar, ingira normalmente pela URL (``ingerir_url``) ou colando o
conteúdo revisado como fonte do tipo "texto".

O corte é por tópico porque a página da Senior é uma sanfona só: "Rotinas de ICMS"
tem 25 tópicos e ~70 KB num único documento. Ingerida inteira, ela vira um
documento gigante cujos trechos competem entre si na recuperação.
"""
from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path
from urllib.parse import urljoin

import httpx
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand, CommandError
from markdownify import markdownify

from apps.conhecimento.services.imagens import normalizar_markdown
from apps.conhecimento.services.scraper import (
    CABECALHOS,
    SELETORES_CONTEUDO,
    TAGS_RUIDO,
    resolver_url,
)

#: ``F001TVE`` / ``E440NFC`` — código de tela ou tabela do Senior.
RE_TELA = re.compile(r"\b([A-Z]\d{3}[A-Z]{3})\b")
#: ``VEN-000ALICM01`` / ``CPR-440ALDFA01`` — identificador de regras.
RE_REGRA = re.compile(r"\b([A-Z]{3}-\d{3}[A-Z]{3,8}\d{2})\b")
#: ``Cadastros > Empresas > Cadastro (F070EMP)``
RE_CAMINHO = re.compile(r"^(.*>.*)\(([A-Z]\d{3}[A-Z]{3})\)\s*$", re.MULTILINE)


def _slug(texto: str) -> str:
    texto = unicodedata.normalize("NFKD", texto)
    texto = "".join(c for c in texto if not unicodedata.combining(c))
    texto = re.sub(r"[^a-zA-Z0-9]+", "-", texto).strip("-").lower()
    return re.sub(r"-{2,}", "-", texto)[:60]


def _campos_xml_conhecidos() -> set[str]:
    """Campos que o comparador sabe reportar — a ponte entre divergência e doc."""
    from apps.comparador.services import mapa_campos as M

    campos = set(M.CAMPOS_CRITICOS) | set(M.CAMPOS_FISCAIS_DO_PRODUTO)
    campos |= set(M.ALIQUOTAS_COM_PREFIXO_V)
    campos |= {chave.rsplit(".", 1)[-1] for chave in M.PISTAS}
    return {c for c in campos if len(c) >= 3}


def _coletar_links(corpo, url_base: str) -> list[dict[str, str]]:
    """Links de documentação do tópico — capturados antes de o markdownify os descartar."""
    vistos: dict[str, str] = {}
    for ancora in corpo.find_all("a", href=True):
        href = ancora["href"].strip()
        if not href or href.lower().startswith(("javascript:", "mailto:", "#")):
            continue
        texto = ancora.get_text(" ", strip=True)
        if texto:
            vistos.setdefault(urljoin(url_base, href), texto)
    return [{"texto": t, "url": u} for u, t in vistos.items()]


def _corpo_para_markdown(corpo, url_base: str) -> str:
    for tag in corpo.find_all(TAGS_RUIDO):
        tag.decompose()

    # Subtópico aninhado vira ## / ### relativo ao tópico, que é o # do arquivo.
    for cabecalho in corpo.select(".MCDropDownHead"):
        titulo = cabecalho.get_text(" ", strip=True)
        if not titulo:
            continue
        profundidade = len(cabecalho.find_parents(class_="MCDropDown"))
        novo = corpo.new_tag(f"h{min(max(profundidade, 2), 6)}")
        novo.string = titulo
        cabecalho.replace_with(novo)

    md = markdownify(str(corpo), heading_style="ATX", strip=["a"])
    md, _, _ = normalizar_markdown(re.sub(r"\n{3,}", "\n\n", md).strip(), url_base)
    return md.strip()


class Command(BaseCommand):
    help = "Exporta uma página da documentação como um markdown por tópico + mapa.json."

    def add_arguments(self, parser):
        parser.add_argument("url")
        parser.add_argument("--destino", required=True, help="Diretório de saída.")
        parser.add_argument("--versao", default="", help="Versão do produto, para o cabeçalho.")
        parser.add_argument(
            "--limpar",
            action="store_true",
            help="Apaga os .md do destino antes de gerar (remove tópicos que sumiram da página).",
        )

    def handle(self, *args, **opcoes):
        url = resolver_url(opcoes["url"])
        destino = Path(opcoes["destino"])

        try:
            resposta = httpx.get(url, headers=CABECALHOS, timeout=30.0, follow_redirects=True)
            resposta.raise_for_status()
        except Exception as exc:  # noqa: BLE001
            raise CommandError(f"Falha ao baixar {url}: {exc}") from exc

        sopa = BeautifulSoup(resposta.text, "lxml")

        # O portal responde 200 para página inexistente e devolve a casca de erro.
        # Sem esta checagem, o "404 - Página não encontrada" entraria na base como
        # se fosse documentação.
        titulo_html = sopa.title.get_text(strip=True) if sopa.title else ""
        if "404" in titulo_html or "não encontrada" in titulo_html.lower():
            raise CommandError(f"Página inexistente (o portal devolve 200 com {titulo_html!r}).")

        titulo_pagina = (
            sopa.select_one("h1").get_text(strip=True) if sopa.select_one("h1") else url
        )
        trilha = " > ".join(
            e.get_text(strip=True)
            for e in sopa.select(".MCBreadcrumbsSelf, .MCBreadcrumbsLink")
        )

        topicos_html = [
            d for d in sopa.select(".MCDropDown") if not d.find_parent(class_="MCDropDown")
        ]
        # Nem toda página é sanfona. Sem tópico recolhível, a página inteira vira um
        # arquivo só — continua valendo a pena pelo cabeçalho de procedência e pelo
        # mapa de telas/campos, que é o que liga a doc ao comparador.
        pagina_unica = not topicos_html
        if pagina_unica:
            for seletor in SELETORES_CONTEUDO:
                bloco = sopa.select_one(seletor)
                if bloco and len(bloco.get_text(strip=True)) > 200:
                    break
            else:
                bloco = sopa.body
            if bloco is None or len(bloco.get_text(strip=True)) < 200:
                raise CommandError("Página sem conteúdo aproveitável.")
            topicos_html = [bloco]

        destino.mkdir(parents=True, exist_ok=True)
        if opcoes["limpar"]:
            for antigo in destino.glob("*.md"):
                antigo.unlink()

        campos_xml = _campos_xml_conhecidos()
        versao = opcoes["versao"] or next(
            (p for p in url.split("/") if re.fullmatch(r"\d+(\.\d+)+", p)), ""
        )

        self.stdout.write(f"{titulo_pagina} — {len(topicos_html)} tópico(s)\n")
        mapa: list[dict] = []

        for indice, bloco in enumerate(topicos_html, start=1):
            if pagina_unica:
                titulo, ancora, corpo = titulo_pagina, "", bloco
                url_topico = url
                # O arquivo já abre com "# <título>"; o h1 do corpo repetiria.
                h1 = corpo.select_one("h1")
                if h1 and h1.get_text(strip=True) == titulo_pagina:
                    h1.decompose()
            else:
                cabecalho = bloco.select_one(".MCDropDownHead")
                titulo = cabecalho.get_text(" ", strip=True)
                ancora_tag = cabecalho.find("a", attrs={"name": True})
                ancora = ancora_tag["name"] if ancora_tag else ""
                url_topico = f"{url}#{ancora}" if ancora else url
                corpo = bloco.select_one(".MCDropDownBody")
                if corpo is None:
                    continue

            subtopicos = [
                h.get_text(" ", strip=True)
                for h in corpo.select(".MCDropDownHead")
                if h.get_text(strip=True)
            ]
            links = _coletar_links(corpo, url)
            md = _corpo_para_markdown(corpo, url_topico)

            telas = sorted(set(RE_TELA.findall(md)) | set(RE_TELA.findall(titulo)))
            regras = sorted(set(RE_REGRA.findall(md)))
            caminhos = sorted({f"{c.strip()} ({t})" for c, t in RE_CAMINHO.findall(md)})
            campos = sorted(c for c in campos_xml if re.search(rf"\b{re.escape(c)}\b", md))

            nome = f"{indice:02d}-{_slug(titulo)}.md"
            cabecalho_md = "\n".join(
                [
                    f"# {titulo}",
                    "",
                    f"> **Fonte:** {titulo_pagina}"
                    + (f" — versão {versao}" if versao else "") + "  ",
                    f"> **URL:** {url_topico}  ",
                    f"> **Trilha:** {trilha}  ",
                    f"> **Telas citadas:** {', '.join(telas) if telas else '—'}  ",
                    f"> **Identificadores de regras:** {', '.join(regras) if regras else '—'}",
                    "",
                    "---",
                    "",
                ]
            )
            rodape = (
                "\n\n## Páginas relacionadas\n\n"
                + "\n".join(f"* [{x['texto']}]({x['url']})" for x in links)
                if links
                else ""
            )
            (destino / nome).write_text(cabecalho_md + md + rodape + "\n", encoding="utf-8")

            mapa.append(
                {
                    "ordem": indice,
                    "titulo": titulo,
                    "slug": _slug(titulo),
                    "arquivo": nome,
                    "ancora": ancora,
                    "url": url_topico,
                    "subtopicos": subtopicos,
                    "telas": telas,
                    "caminhos_menu": caminhos,
                    "identificadores_regras": regras,
                    "campos_xml_citados": campos,
                    "links_documentacao": links,
                    "caracteres": len(md),
                }
            )
            self.stdout.write(
                f"  {indice:02d}. {titulo[:52]:<52} {len(md):>6} chars  "
                f"telas={len(telas):>2} regras={len(regras)} campos={len(campos)}"
            )

        indice_telas: dict[str, list[str]] = {}
        for item in mapa:
            for tela in item["telas"]:
                indice_telas.setdefault(tela, []).append(item["slug"])

        (destino / "mapa.json").write_text(
            json.dumps(
                {
                    "fonte": {
                        "pagina": titulo_pagina,
                        "versao": versao,
                        "url": url,
                        "trilha": trilha,
                    },
                    "total_topicos": len(mapa),
                    "topicos": mapa,
                    "indice_telas": {t: sorted(set(s)) for t, s in sorted(indice_telas.items())},
                    # Fila do próximo passo: as páginas para as quais esta aponta.
                    "paginas_relacionadas": sorted(
                        {x["url"] for t in mapa for x in t["links_documentacao"]}
                    ),
                },
                ensure_ascii=False,
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )

        linhas = [
            f"# {titulo_pagina} — índice",
            "",
            f"Fonte: {url}" + (f" (versão {versao})" if versao else ""),
            "",
            f"{len(mapa)} tópicos, um arquivo por tópico. O mapa estruturado (telas, "
            "identificadores de regras, campos do XML e links) está em `mapa.json`.",
            "",
            "| # | Tópico | Arquivo | Telas | Identificadores |",
            "|---|---|---|---|---|",
        ]
        linhas += [
            f"| {i['ordem']:02d} | {i['titulo']} | [`{i['arquivo']}`]({i['arquivo']}) "
            f"| {len(i['telas'])} | {len(i['identificadores_regras'])} |"
            for i in mapa
        ]
        (destino / "00-indice.md").write_text("\n".join(linhas) + "\n", encoding="utf-8")

        self.stdout.write("")
        self.stdout.write(
            self.style.SUCCESS(
                f"{len(mapa)} arquivo(s) em {destino}/ — {len(indice_telas)} tela(s) distinta(s), "
                f"{len({x['url'] for t in mapa for x in t['links_documentacao']})} página(s) "
                "relacionada(s) na fila."
            )
        )
