"""
Consolidação de um lote (N notas × N notas).

Com 100 notas, mandar 100 relatórios para a IA é inútil e caro. O que interessa
ao consultor é o **padrão**: se `ICMS.CST` diverge `00 → 20` em 87 das 100
notas, isso é *um* ajuste de parametrização, não 87 problemas.

Este módulo transforma N resultados individuais em um ranking de causas
recorrentes, ordenado por severidade e por número de notas afetadas.
"""
from __future__ import annotations

from collections import Counter
from typing import Any, Iterable

from .mapa_campos import ALTA, BAIXA, CRITICA, MEDIA, ORDEM_SEVERIDADE, ROTULO_SEVERIDADE

#: Quantas variações de valor detalhar por causa.
MAX_VARIACOES = 5
#: Quantos produtos citar por causa.
MAX_PRODUTOS = 6
#: Quantas causas entram no relatório enviado à IA.
MAX_CAUSAS_PROMPT = 40


def agregar_lote(
    resultados: Iterable[dict[str, Any]],
    *,
    incluir_baixa: bool = False,
) -> dict[str, Any]:
    """
    ``resultados`` é uma sequência de dicts, um por par comparado:

        {"arquivo_cliente": ..., "arquivo_senior": ...,
         "identificacao": ..., "divergencias": [...]}

    Devolve a estrutura consolidada consumida pela tela e pelo relatório.
    """
    causas: dict[tuple[str, str], dict[str, Any]] = {}
    notas: list[dict[str, Any]] = []

    total_divergencias = 0
    por_severidade = {CRITICA: 0, ALTA: 0, MEDIA: 0, BAIXA: 0}
    notas_conformes = 0

    for resultado in resultados:
        # Rótulo do PAR — é isso que o consultor procura: "Nota Original 63 ↔
        # Nota Senior 65". Nomear os dois lados importa: "NF 63" sozinho não
        # dizia de qual sistema era. Cai para o nome do arquivo se a nota não
        # trouxer numeração.
        rotulo_nota = resultado.get("rotulo") or resultado.get("arquivo_cliente", "")
        divergencias = resultado.get("divergencias", []) or []
        if not incluir_baixa:
            divergencias = [d for d in divergencias if d.get("severidade") != BAIXA]

        contagem_nota = {CRITICA: 0, ALTA: 0, MEDIA: 0, BAIXA: 0}
        for d in divergencias:
            severidade = d.get("severidade", MEDIA)
            contagem_nota[severidade] = contagem_nota.get(severidade, 0) + 1
            por_severidade[severidade] = por_severidade.get(severidade, 0) + 1
            total_divergencias += 1

            chave = (d.get("grupo", ""), d.get("campo", ""), d.get("tipo", ""))
            causa = causas.get(chave)
            if causa is None:
                causa = {
                    "titulo": d.get("titulo", ""),
                    "categoria": d.get("categoria", ""),
                    "grupo": d.get("grupo", ""),
                    "campo": d.get("campo", ""),
                    "tipo": d.get("tipo", ""),
                    "severidade": severidade,
                    "pista": d.get("pista", ""),
                    "tipo_rotulo": d.get("tipo_rotulo", d.get("tipo", "")),
                    "notas": [],
                    "ocorrencias": 0,
                    "variacoes": {},
                    "produtos": Counter(),
                    "exemplo_caminho": d.get("caminho", ""),
                }
                causas[chave] = causa

            # A causa herda a severidade mais grave que apareceu nela.
            if ORDEM_SEVERIDADE.get(severidade, 9) < ORDEM_SEVERIDADE.get(causa["severidade"], 9):
                causa["severidade"] = severidade

            if rotulo_nota not in causa["notas"]:
                causa["notas"].append(rotulo_nota)
            causa["ocorrencias"] += 1
            if d.get("item_codigo"):
                causa["produtos"][d["item_codigo"]] += 1

            # Item ausente: agrupa por PRODUTO, não por número do item. Cinco
            # linhas "item 2 → ausente … item 6 → ausente" viram
            # "5 itens do produto 00001".
            if d.get("campo") == "_item":
                chave_variacao = (d.get("item_codigo") or "(sem código)", "")
            else:
                chave_variacao = (d.get("valor_cliente", ""), d.get("valor_senior", ""))

            variacao = causa["variacoes"].setdefault(
                chave_variacao, {"ocorrencias": 0, "notas": []}
            )
            variacao["ocorrencias"] += 1
            if rotulo_nota not in variacao["notas"]:
                variacao["notas"].append(rotulo_nota)

        conforme = not (contagem_nota[CRITICA] or contagem_nota[ALTA])
        if conforme:
            notas_conformes += 1

        titulos_da_nota = sorted(
            {
                d.get("titulo") or f"{d.get('categoria', '')} · {d.get('campo', '')}"
                for d in divergencias
            }
        )

        notas.append(
            {
                "rotulo": rotulo_nota,
                "titulos": titulos_da_nota,
                "arquivo_cliente": resultado.get("arquivo_cliente", ""),
                "arquivo_senior": resultado.get("arquivo_senior", ""),
                "identificacao": resultado.get("identificacao", ""),
                "comparacao_id": resultado.get("comparacao_id"),
                "total": sum(contagem_nota.values()),
                "criticas": contagem_nota[CRITICA],
                "altas": contagem_nota[ALTA],
                "conforme": conforme,
            }
        )

    total_notas = len(notas)

    lista_causas = []
    for causa in causas.values():
        quantidade_notas = len(causa["notas"])

        ordenadas = sorted(
            causa["variacoes"].items(), key=lambda kv: -kv[1]["ocorrencias"]
        )[:MAX_VARIACOES]

        lista_causas.append(
            {
                "titulo": causa["titulo"],
                "categoria": causa["categoria"],
                "grupo": causa["grupo"],
                "campo": causa["campo"],
                "tipo": causa["tipo"],
                "severidade": causa["severidade"],
                "severidade_rotulo": ROTULO_SEVERIDADE.get(
                    causa["severidade"], causa["severidade"]
                ),
                "tipo_rotulo": causa["tipo_rotulo"],
                "pista": causa["pista"],
                "caminho": causa["exemplo_caminho"],
                "notas": causa["notas"][:20],
                "total_notas_listadas": len(causa["notas"]),
                "notas_afetadas": quantidade_notas,
                "percentual_notas": round(quantidade_notas / total_notas * 100) if total_notas else 0,
                "ocorrencias": causa["ocorrencias"],
                "variacoes": [
                    {
                        "cliente": cliente,
                        "senior": senior,
                        "ocorrencias": dados["ocorrencias"],
                        "notas": dados["notas"][:6],
                        "total_notas": len(dados["notas"]),
                    }
                    for (cliente, senior), dados in ordenadas
                ],
                "total_variacoes": len(causa["variacoes"]),
                "produtos": [
                    {"codigo": codigo, "ocorrencias": qtd}
                    for codigo, qtd in causa["produtos"].most_common(MAX_PRODUTOS)
                ],
                "total_produtos": len(causa["produtos"]),
            }
        )

    lista_causas.sort(
        key=lambda c: (
            ORDEM_SEVERIDADE.get(c["severidade"], 9),
            -c["notas_afetadas"],
            -c["ocorrencias"],
            c["campo"],
        )
    )

    notas.sort(key=lambda n: (-n["criticas"], -n["altas"], n["arquivo_cliente"]))

    perfis = _agrupar_perfis(notas)

    placar = {
        "notas_comparadas": total_notas,
        "notas_conformes": notas_conformes,
        "notas_com_divergencia": total_notas - notas_conformes,
        "total_divergencias": total_divergencias,
        "por_severidade": por_severidade,
        "total_causas": len(lista_causas),
    }

    return {
        "placar": placar,
        "causas": lista_causas,
        "notas": notas,
        "perfis": perfis,
        "narrativa": montar_narrativa(placar, perfis),
    }


# --------------------------------------------------------------------------- #
#  Resumo em linguagem natural
# --------------------------------------------------------------------------- #
#: Quantos perfis distintos são narrados antes de agrupar o resto em "outras".
MAX_PERFIS_NARRADOS = 6


def _agrupar_perfis(notas: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """
    Agrupa as notas pelo **conjunto** de problemas que elas têm.

    É assim que o consultor pensa: "40 notas têm exatamente os mesmos três
    problemas" vale mais que "56 notas têm o problema X e 32 têm o Y", porque
    cada grupo tende a corresponder a um cenário de parametrização (um CFOP, um
    perfil de cliente, uma família de produtos).
    """
    agrupados: dict[tuple[str, ...], dict[str, Any]] = {}

    for nota in notas:
        chave = tuple(nota.get("titulos") or ())
        perfil = agrupados.setdefault(
            chave,
            {"causas": list(chave), "notas": 0, "exemplos": [], "conforme": not chave},
        )
        perfil["notas"] += 1
        if len(perfil["exemplos"]) < 5:
            perfil["exemplos"].append(nota.get("rotulo") or nota.get("arquivo_cliente", ""))

    total = len(notas) or 1
    lista = list(agrupados.values())
    for perfil in lista:
        perfil["percentual"] = round(perfil["notas"] / total * 100)

    # Notas conformes por último; o resto por volume.
    lista.sort(key=lambda p: (p["conforme"], -p["notas"]))
    return lista


def _lista_em_texto(itens: list[str]) -> str:
    """``["a", "b", "c"]`` → ``"a, b e c"``."""
    itens = [i for i in itens if i]
    if not itens:
        return ""
    if len(itens) == 1:
        return itens[0]
    return f"{', '.join(itens[:-1])} e {itens[-1]}"


def _para_lista(titulo: str) -> str:
    """
    Ajusta o título da causa para caber numa enumeração corrida.

    "Alíquota de ICMS divergente" → "alíquota de ICMS"
    "CST de ICMS divergente"      → "CST de ICMS"      (sigla mantém a caixa)
    "Item não emitido na nota do Senior" → "item não emitido na nota do Senior"
    """
    texto = titulo.replace(" divergente", "").strip()
    if not texto:
        return texto
    primeira_palavra = texto.split(" ", 1)[0]
    if primeira_palavra.isupper():  # CST, CFOP, NCM, CEST, MVA…
        return texto
    return texto[0].lower() + texto[1:]


def montar_narrativa(placar: dict[str, Any], perfis: list[dict[str, Any]]) -> dict[str, Any]:
    """
    Resumo em português para o consultor ler antes de olhar a lista de causas.

    Devolve ``{"abertura": str, "linhas": [str], "fechamento": str}`` — separado
    para a tela poder formatar cada parte de um jeito.
    """
    total = placar.get("notas_comparadas", 0)
    com_divergencia = placar.get("notas_com_divergencia", 0)
    conformes = placar.get("notas_conformes", 0)

    if total == 0:
        return {"abertura": "Nenhuma nota foi comparada.", "linhas": [], "fechamento": ""}

    if com_divergencia == 0:
        return {
            "abertura": (
                f"Comparamos {total} nota{'s' if total > 1 else ''} e "
                f"nenhuma apresentou divergência fiscal. A parametrização do Senior está "
                "reproduzindo a tributação do sistema atual nas operações testadas."
            ),
            "linhas": [],
            "fechamento": "",
        }

    plural_total = "s" if total > 1 else ""
    verbo = "apresentaram" if com_divergencia > 1 else "apresentou"

    abertura = (
        f"Das {total} nota{plural_total} comparada{plural_total}, "
        f"**{com_divergencia}** {verbo} divergência fiscal"
    )
    if conformes:
        saiu = "saíram iguais" if conformes > 1 else "saiu igual"
        abertura += f" e **{conformes}** {saiu}."
    else:
        abertura += "."

    linhas: list[str] = []
    com_problema = [p for p in perfis if not p["conforme"]]
    narrados = com_problema[:MAX_PERFIS_NARRADOS]
    restantes = com_problema[MAX_PERFIS_NARRADOS:]

    for perfil in narrados:
        quantidade = perfil["notas"]
        rotulo = f"**{quantidade} nota{'s' if quantidade > 1 else ''}** ({perfil['percentual']}%)"
        causas = _lista_em_texto([_para_lista(c) for c in perfil["causas"]])
        linhas.append(f"{rotulo} — diferenças em {causas}.")

    if restantes:
        soma = sum(p["notas"] for p in restantes)
        linhas.append(
            f"**{soma} nota{'s' if soma > 1 else ''}** em outras {len(restantes)} "
            "combinações de divergência."
        )

    fechamento = ""
    if conformes:
        fechamento = (
            f"{'As' if conformes > 1 else 'A'} {conformes} "
            f"nota{'s' if conformes > 1 else ''} sem divergência "
            f"{'mostram' if conformes > 1 else 'mostra'} que a parametrização já está correta "
            f"para o perfil de operação {'delas' if conformes > 1 else 'dela'} — compare com as "
            "demais para achar o que muda."
        )

    return {"abertura": abertura, "linhas": linhas, "fechamento": fechamento}


def montar_relatorio_lote_markdown(
    agregado: dict[str, Any],
    *,
    escopo: dict[str, Any] | None = None,
    max_causas: int = MAX_CAUSAS_PROMPT,
) -> str:
    """Relatório consolidado do lote — é isto que vai para o agente de IA."""
    placar = agregado.get("placar", {})
    causas = agregado.get("causas", [])
    notas = agregado.get("notas", [])
    escopo = escopo or {}

    linhas: list[str] = []
    add = linhas.append

    add("# Relatório consolidado — comparação em massa")
    add("")
    add(
        "Este relatório agrega a comparação de **várias notas** emitidas nos dois "
        "sistemas para as mesmas operações. As divergências estão agrupadas por "
        "causa provável, com o número de notas afetadas por cada uma."
    )
    add("")

    # ---------------------------------------------------------------- escopo
    add("## Escopo")
    add("")
    add(f"- Notas do sistema atual do cliente: **{escopo.get('total_cliente', '—')}**")
    add(f"- Notas geradas pelo ERP Senior: **{escopo.get('total_senior', '—')}**")
    add(f"- Pares comparados: **{placar.get('notas_comparadas', 0)}**")
    sem_par_cliente = escopo.get("sem_par_cliente", 0)
    sem_par_senior = escopo.get("sem_par_senior", 0)
    if sem_par_cliente or sem_par_senior:
        add(
            f"- Sem par: **{sem_par_cliente}** do cliente e **{sem_par_senior}** do Senior "
            "(operações que não foram encontradas do outro lado)"
        )
    add("")

    # ---------------------------------------------------------------- placar
    sev = placar.get("por_severidade", {})
    add("## Placar")
    add("")
    add(
        f"- Notas **sem** divergência relevante: **{placar.get('notas_conformes', 0)}** "
        f"de {placar.get('notas_comparadas', 0)}"
    )
    add(f"- Notas **com** divergência: **{placar.get('notas_com_divergencia', 0)}**")
    add(f"- Total de divergências: **{placar.get('total_divergencias', 0)}**")
    add(
        f"- Críticas: **{sev.get(CRITICA, 0)}** · Altas: **{sev.get(ALTA, 0)}** · "
        f"Médias: **{sev.get(MEDIA, 0)}**"
    )
    add(f"- Causas distintas identificadas: **{placar.get('total_causas', 0)}**")
    add("")

    narrativa = agregado.get("narrativa") or {}
    if narrativa.get("abertura"):
        add("## Resumo")
        add("")
        add(narrativa["abertura"])
        add("")
        for linha in narrativa.get("linhas", []):
            add(f"- {linha}")
        if narrativa.get("linhas"):
            add("")
        if narrativa.get("fechamento"):
            add(narrativa["fechamento"])
            add("")

    if not causas:
        add("## Resultado")
        add("")
        add(
            "Nenhuma divergência relevante encontrada nos campos de imposto, "
            "considerando as tolerâncias configuradas."
        )
        return "\n".join(linhas)

    # ---------------------------------------------------------------- causas
    add("## Causas recorrentes")
    add("")
    add(
        "Ordenadas por severidade e por número de notas afetadas. **Corrigir uma causa "
        "corrige todas as notas listadas nela** — trate cada bloco como um único ajuste "
        "de parametrização. `NF X ↔ NF Y` identifica o par: nota X no sistema atual do "
        "cliente, nota Y equivalente no Senior."
    )
    add("")

    severidade_atual = None
    for posicao, causa in enumerate(causas[:max_causas], start=1):
        if causa["severidade"] != severidade_atual:
            severidade_atual = causa["severidade"]
            add("")
            add(f"### Severidade {ROTULO_SEVERIDADE.get(severidade_atual, severidade_atual)}")
            add("")

        titulo = causa.get("titulo") or f"{causa['categoria']} · {causa['campo']}"
        add(
            f"**{posicao}. {titulo} — {causa['notas_afetadas']} nota(s) "
            f"({causa['percentual_notas']}%)**"
        )
        add("")
        add(f"- Campo no XML: `{causa['campo']}` ({causa['categoria']})")

        e_item_ausente = causa.get("campo") == "_item"
        for variacao in causa["variacoes"]:
            notas_da_variacao = ", ".join(variacao["notas"])
            if variacao["total_notas"] > len(variacao["notas"]):
                notas_da_variacao += f" (+{variacao['total_notas'] - len(variacao['notas'])})"

            if e_item_ausente:
                add(
                    f"- Produto `{variacao['cliente']}`: {variacao['ocorrencias']} item(ns) "
                    f"não emitido(s) — {notas_da_variacao}"
                )
            else:
                cliente = variacao["cliente"] or "(ausente)"
                senior = variacao["senior"] or "(ausente)"
                add(f"- **`{cliente}` no cliente → `{senior}` no Senior** — {notas_da_variacao}")

        if causa["total_variacoes"] > len(causa["variacoes"]):
            add(f"- … e mais {causa['total_variacoes'] - len(causa['variacoes'])} variação(ões)")

        if causa["produtos"] and not e_item_ausente:
            produtos = ", ".join(
                f"{p['codigo']} ({p['ocorrencias']})" for p in causa["produtos"]
            )
            extra = (
                f" … e mais {causa['total_produtos'] - len(causa['produtos'])} produto(s)"
                if causa["total_produtos"] > len(causa["produtos"])
                else ""
            )
            add(f"- Produtos afetados: {produtos}{extra}")

        if causa["pista"]:
            add(f"- **O que ajustar:** {causa['pista']}")
        add("")

    if len(causas) > max_causas:
        add(
            f"> _Foram omitidas {len(causas) - max_causas} causas de menor severidade/frequência. "
            "Peça o detalhamento se necessário._"
        )
        add("")

    # ------------------------------------------------------- notas críticas
    piores = [n for n in notas if n["criticas"]][:15]
    if piores:
        add("## Notas com mais divergências")
        add("")
        add("| Par de notas | Divergências | Arquivos |")
        add("|---|---:|---|")
        for nota in piores:
            add(
                f"| {nota.get('rotulo') or nota['arquivo_cliente']} | {nota['total']} | "
                f"{nota['arquivo_cliente']} ↔ {nota['arquivo_senior']} |"
            )
        add("")

    conformes = [n for n in notas if n["conforme"]]
    if conformes:
        add(
            f"_{len(conformes)} nota(s) saíram sem divergência crítica ou alta — "
            "a parametrização já está correta para o perfil dessas operações._"
        )
        add("")

    return "\n".join(linhas)
