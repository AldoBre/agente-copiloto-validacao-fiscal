"""
Identidade da versão que produziu cada resposta.

## O problema que isto resolve

O agente coleta 👍/👎 e guarda um retrato do que gerou a resposta — pergunta,
resposta, modelo, fontes, lote. Faltava a peça que dá validade ao dado meses
depois: **qual versão do comportamento produziu aquela resposta**.

Sem isso, um voto negativo de hoje pode estar avaliando um prompt que já foi
corrigido, e não há como saber olhando só o voto. O valor do carimbo é
retroativo a zero: voto coletado antes dele existir é voto que ninguém vai
conseguir interpretar depois.

## O que entra no hash, e por que não só o prompt

A recomendação natural é hashear ``prompts.SISTEMA``. Não basta, e isto ficou
provado no mesmo dia em que as ferramentas entraram: as **docstrings das
ferramentas são prompt** — o modelo lê e decide com base nelas, e somam ~1.480
tokens. Um hash só do SISTEMA diria "mesma versão" depois de uma mudança que
alterou o comportamento.

Então o hash cobre o *contrato de comportamento* inteiro:

* ``SISTEMA`` e os blocos de contexto que o envolvem;
* nome, descrição e schema de cada ferramenta oferecida;
* os parâmetros que mudam **o que o modelo vê** (quantos trechos, que janela de
  histórico, quantas rodadas de ferramenta, se a semântica está ligada).

O último item é de propósito: o mesmo código com `AGENTE_BUSCA_SEMANTICA=on`
produz respostas diferentes, e isso é outra versão para efeito de avaliação.

## Por que também guardar o SHA do commit

O hash é exato e automático, mas opaco: daqui a seis meses você tem
``a3f9c2d1`` e nada com que comparar. O SHA do commit resolve o hash —
``git show <sha>:apps/agente/prompts.py`` devolve o texto exato. Um identifica,
o outro explica; por isso os dois.

O SHA chega por variável de ambiente, injetada no build (ver o Dockerfile). Em
desenvolvimento ele simplesmente não existe, e o hash sozinho continua servindo.
"""
from __future__ import annotations

import hashlib
import json
import os

from django.conf import settings

#: Injetado no build da imagem a partir de ``github.sha``. Vazio fora do CI.
ENV_GIT_SHA = "GIT_SHA"

#: Parâmetros que mudam o que o modelo vê. Mudou aqui, é outra versão — mesmo
#: sem nenhuma linha de código diferente.
_CHAVES_RELEVANTES = (
    "TOP_K_CONTEXTO",
    "JANELA_HISTORICO",
    "MAX_DIVERGENCIAS_PROMPT",
    "MAX_PASSOS_FERRAMENTA",
    "FERRAMENTAS",
    "BUSCA_SEMANTICA",
)

#: Tamanho do hash exibido. 12 hex são 48 bits: colisão é irrelevante para
#: dezenas de versões, e cabe numa coluna de planilha.
_DIGITOS = 12

_cache: dict[str, str] = {}


def _contrato() -> str:
    """Texto canônico do que determina o comportamento do agente."""
    from . import prompts
    from .ferramentas import FERRAMENTAS

    partes: list[str] = [
        prompts.SISTEMA,
        prompts.CONTEXTO_RELATORIO,
        prompts.CONTEXTO_BASE,
        prompts.CONTEXTO_REGRAS,
        prompts.SEM_COMPARACAO,
    ]

    # Ordenado por nome: a ordem da lista em ferramentas.py é estética e não
    # deve mudar a versão. Já a descrição e o schema, sim — são o que o modelo
    # lê para decidir se chama.
    if settings.AGENTE.get("FERRAMENTAS", True):
        for ferramenta in sorted(FERRAMENTAS, key=lambda f: f.name):
            schema = getattr(ferramenta, "args", {})
            partes.append(
                f"{ferramenta.name}\n{ferramenta.description}\n"
                + json.dumps(schema, sort_keys=True, ensure_ascii=False, default=str)
            )

    for chave in _CHAVES_RELEVANTES:
        partes.append(f"{chave}={settings.AGENTE.get(chave)!r}")

    return "\n\x00\n".join(partes)


def hash_prompt() -> str:
    """
    Identificador curto e determinístico do contrato de comportamento.

    Memorizado pelos parâmetros de runtime: o texto do prompt não muda dentro do
    processo, mas `override_settings` em teste muda, e um cache cego devolveria
    a versão errada.
    """
    chave = "|".join(f"{c}={settings.AGENTE.get(c)!r}" for c in _CHAVES_RELEVANTES)
    if chave not in _cache:
        digest = hashlib.sha256(_contrato().encode("utf-8")).hexdigest()
        _cache[chave] = digest[:_DIGITOS]
    return _cache[chave]


def git_sha() -> str:
    """SHA do commit que gerou a imagem, quando o build o injetou."""
    return (os.getenv(ENV_GIT_SHA) or "").strip()[:40]


def carimbo() -> dict[str, str]:
    """
    O que vai em ``Mensagem.metadados`` no momento em que a resposta é gravada.

    **Na criação da mensagem, não no voto.** É a diferença entre saber e supor:
    reconstruir a versão depois, por aproximação de data, erra sempre que houve
    deploy no meio do dia — e é exatamente nos dias de deploy que a informação
    importa.
    """
    dados = {"versao_prompt": hash_prompt()}
    sha = git_sha()
    if sha:
        dados["git_sha"] = sha
    return dados
