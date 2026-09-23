"""
Compilação do resultado da comparação.

Duas saídas:
  * :func:`montar_resumo` — dict enxuto para os cards da tela.
  * :func:`montar_relatorio_markdown` — o texto que é enviado ao agente de IA.

O relatório para a IA é agrupado por *causa provável* (grupo de imposto + campo)
em vez de item a item: 40 itens com a mesma CST errada viram uma linha só, com
a lista de itens afetados. Isso reduz drasticamente o tamanho do prompt e faz o
modelo responder sobre a parametrização, não sobre cada nota.
"""
from __future__ import annotations

from typing import Any

from .mapa_campos import ALTA, BAIXA, CRITICA, MEDIA, ORDEM_SEVERIDADE, ROTULO_SEVERIDADE


def montar_resumo(resultado: dict[str, Any]) -> dict[str, Any]:
    """Resumo compacto usado pelos cards da interface."""
    resumo = dict(resultado.get("resumo", {}))
    docs = resultado.get("documentos", {})
    resumo["documento_cliente"] = {
        "identificacao": docs.get("cliente", {}).get("identificacao", ""),
        "chave": docs.get("cliente", {}).get("chave", ""),
        "itens": docs.get("cliente", {}).get("quantidade_itens", 0),
        "arquivo": docs.get("cliente", {}).get("nome_arquivo", ""),
    }
    resumo["documento_senior"] = {
        "identificacao": docs.get("senior", {}).get("identificacao", ""),
        "chave": docs.get("senior", {}).get("chave", ""),
        "itens": docs.get("senior", {}).get("quantidade_itens", 0),
        "arquivo": docs.get("senior", {}).get("nome_arquivo", ""),
    }
    return resumo


def _agrupar_por_causa(divergencias: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Agrupa divergências idênticas (mesmo grupo/campo/valores) entre itens."""
    grupos: dict[tuple, dict[str, Any]] = {}

    for d in divergencias:
        chave = (
            d.get("grupo", ""),
            d.get("campo", ""),
            d.get("tipo", ""),
            d.get("valor_cliente", ""),
            d.get("valor_senior", ""),
        )
        entrada = grupos.get(chave)
        if entrada is None:
            entrada = {
                "categoria": d.get("categoria", ""),
                "grupo": d.get("grupo", ""),
                "campo": d.get("campo", ""),
                "caminho": d.get("caminho", ""),
                "escopo": d.get("escopo", ""),
                "tipo": d.get("tipo", ""),
                "tipo_rotulo": d.get("tipo_rotulo", d.get("tipo", "")),
                "severidade": d.get("severidade", MEDIA),
                "valor_cliente": d.get("valor_cliente", ""),
                "valor_senior": d.get("valor_senior", ""),
                "diferenca": d.get("diferenca", ""),
                "pista": d.get("pista", ""),
                "itens": [],
                "ocorrencias": 0,
            }
            grupos[chave] = entrada

        entrada["ocorrencias"] += 1
        if d.get("item_numero") is not None:
            rotulo = f"{d['item_numero']}"
            if d.get("item_codigo"):
                rotulo += f" ({d['item_codigo']})"
            if rotulo not in entrada["itens"]:
                entrada["itens"].append(rotulo)

    lista = list(grupos.values())
    lista.sort(
        key=lambda g: (
            ORDEM_SEVERIDADE.get(g["severidade"], 9),
            -g["ocorrencias"],
            g["categoria"],
            g["campo"],
        )
    )
    return lista


def montar_relatorio_markdown(
    resultado: dict[str, Any], *, max_causas: int = 60, incluir_baixa: bool = False
) -> str:
    """
    Monta o texto compilado que vai para o agente de IA.

    ``incluir_baixa=False`` corta divergências de severidade baixa (descrição,
    EAN, texto livre) — elas poluem o prompt e não são problema de parametrização.
    """
    docs = resultado.get("documentos", {})
    cliente = docs.get("cliente", {})
    senior = docs.get("senior", {})
    resumo = resultado.get("resumo", {})
    divergencias = resultado.get("divergencias", [])

    if not incluir_baixa:
        divergencias = [d for d in divergencias if d.get("severidade") != BAIXA]

    causas = _agrupar_por_causa(divergencias)
    total_causas = len(causas)
    causas_exibidas = causas[:max_causas]

    linhas: list[str] = []
    add = linhas.append

    add("# Relatório de comparação fiscal")
    add("")
    add("## Documentos")
    add("")
    add("| | XML do sistema atual (cliente) | XML gerado pelo ERP Senior |")
    add("|---|---|---|")
    add(
        f"| Arquivo | {cliente.get('nome_arquivo', '—')} | {senior.get('nome_arquivo', '—')} |"
    )
    add(f"| Tipo | {cliente.get('tipo', '—')} | {senior.get('tipo', '—')} |")
    add(
        f"| Identificação | {cliente.get('identificacao', '—')} | "
        f"{senior.get('identificacao', '—')} |"
    )
    add(
        f"| Qtde. de itens | {cliente.get('quantidade_itens', 0)} | "
        f"{senior.get('quantidade_itens', 0)} |"
    )
    emit_cliente = cliente.get("emitente", {}) or {}
    emit_senior = senior.get("emitente", {}) or {}
    add(f"| CRT do emitente | {emit_cliente.get('CRT', '—')} | {emit_senior.get('CRT', '—')} |")
    add("")

    por_sev = resumo.get("por_severidade", {})
    add("## Placar")
    add("")
    add(f"- Total de divergências: **{resumo.get('total_divergencias', 0)}**")
    add(
        f"- Críticas: **{por_sev.get(CRITICA, 0)}** · Altas: **{por_sev.get(ALTA, 0)}** · "
        f"Médias: **{por_sev.get(MEDIA, 0)}** · Baixas: **{por_sev.get(BAIXA, 0)}**"
    )
    add(f"- Itens pareados: {resumo.get('itens_pareados', 0)}")
    if resumo.get("itens_somente_cliente"):
        add(f"- Itens só no XML do cliente: {len(resumo['itens_somente_cliente'])}")
    if resumo.get("itens_somente_senior"):
        add(f"- Itens só no XML da Senior: {len(resumo['itens_somente_senior'])}")
    por_cat = resumo.get("por_categoria", {})
    if por_cat:
        add("- Por categoria: " + ", ".join(f"{k} ({v})" for k, v in por_cat.items()))
    add("")

    if not causas_exibidas:
        add("## Divergências")
        add("")
        add(
            "Nenhuma divergência relevante encontrada nos campos de imposto "
            "(considerando as tolerâncias configuradas)."
        )
        return "\n".join(linhas)

    add("## Divergências agrupadas por causa provável")
    add("")
    add(
        "Cada linha é um campo divergente; a coluna *Itens* lista os itens afetados "
        "(nº e código do produto)."
    )
    add("")

    severidade_atual = None
    for causa in causas_exibidas:
        if causa["severidade"] != severidade_atual:
            severidade_atual = causa["severidade"]
            add("")
            add(f"### Severidade: {ROTULO_SEVERIDADE.get(severidade_atual, severidade_atual)}")
            add("")

        cabecalho = f"**{causa['categoria']} · `{causa['campo']}`**"
        if causa["ocorrencias"] > 1:
            cabecalho += f" — {causa['ocorrencias']} ocorrências"
        add(cabecalho)
        add("")
        add(f"- Situação: {causa['tipo_rotulo']}")
        add(f"- Cliente: `{causa['valor_cliente'] or '(ausente)'}`")
        add(f"- Senior: `{causa['valor_senior'] or '(ausente)'}`")
        if causa["diferenca"]:
            add(f"- Diferença: `{causa['diferenca']}`")
        if causa["itens"]:
            itens_txt = ", ".join(causa["itens"][:15])
            if len(causa["itens"]) > 15:
                itens_txt += f" … (+{len(causa['itens']) - 15})"
            add(f"- Itens: {itens_txt}")
        if causa["caminho"]:
            add(f"- Caminho no XML: `{causa['caminho']}`")
        if causa["pista"]:
            add(f"- Pista de parametrização: {causa['pista']}")
        add("")

    if total_causas > max_causas:
        add(
            f"> _Foram omitidas {total_causas - max_causas} causas de menor severidade "
            "para caber no contexto. Peça o detalhamento se necessário._"
        )
        add("")

    avisos = resultado.get("avisos") or []
    if avisos:
        add("## Avisos do parser")
        add("")
        for aviso in avisos:
            add(f"- {aviso}")
        add("")

    return "\n".join(linhas)
