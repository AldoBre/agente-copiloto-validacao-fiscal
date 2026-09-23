"""
Tradução de erro de provedor para uma frase que o consultor consegue agir.

O SDK de cada provedor levanta a exceção com o corpo HTTP inteiro embutido na
mensagem. O consultor recebe algo assim:

    BadRequestError: Error code: 400 - {'type': 'error', 'error': {'type':
    'invalid_request_error', 'message': 'You have reached your specified API
    usage limits. You will regain access on 2026-08-01 at 00:00 UTC.'},
    'request_id': 'req_011CdN1NjaRncYj8p61xpVeS'}

A informação que importa — *a conta bateu o limite de gasto e volta dia 1º* —
está lá, mas ninguém lê. Pior: o formato é o mesmo de "chave inválida" e de
"modelo inexistente", que exigem ações completamente diferentes.

Aqui a exceção vira: causa provável, o que fazer, e o texto original preservado
no fim para quem for investigar.
"""
from __future__ import annotations

import re

#: A frase útil do provedor, quando ela vem embutida num dicionário serializado.
_RE_MENSAGEM = re.compile(r"['\"]message['\"]\s*:\s*['\"](.+?)['\"](?=[,}])", re.DOTALL)
_RE_STATUS = re.compile(r"\b(4\d\d|5\d\d)\b")

#: (termo no texto do erro, diagnóstico, o que fazer).
#: A ordem importa: o primeiro que casar vence, então o mais específico vem antes.
_PADROES: list[tuple[str, str, str]] = [
    # --- Azure AI Foundry ---------------------------------------------------
    # Vêm primeiro porque são os mais específicos, e porque o texto cru do Azure
    # não diz o que fazer: "DeploymentNotFound" com HTTP 404 leva o consultor a
    # achar que o modelo saiu do ar, quando o nome do deployment é que está
    # errado (no Azure o que se chama é o deployment, não o modelo).
    (
        "deploymentnotfound",
        "O deployment não existe nesta conta do Foundry.",
        "No Azure quem é chamado é o DEPLOYMENT, não o modelo. Confira o nome em "
        "Configurações → Deployment, ou liste os existentes com: "
        "az cognitiveservices account deployment list -g <rg> -n <conta> -o table",
    ),
    (
        "api deployment for this resource does not exist",
        "O deployment não existe nesta conta do Foundry.",
        "Confira o nome em Configurações → Deployment. Ele é escolhido por quem fez "
        "o deploy e não precisa ser igual ao id do modelo.",
    ),
    (
        "unsupported api version",
        "A versão da API não atende este modelo.",
        "Modelos gpt-5.x exigem api-version de 2025 em diante; 2024-10-21 só serve "
        "para a família gpt-4.x. Ajuste em Configurações → Versão da API.",
    ),
    (
        "invalid api version",
        "A versão da API é inválida para esta conta.",
        "Use uma api-version publicada pelo Azure (ex.: 2024-10-21). Ajuste em "
        "Configurações → Versão da API.",
    ),
    (
        "usage limit",
        "A chave é válida, mas a conta atingiu o limite de uso configurado.",
        "Ajuste o limite no console do provedor (na Anthropic: Settings → Limits) "
        "ou aguarde a data de liberação informada abaixo.",
    ),
    (
        "credit balance is too low",
        "A conta está sem créditos.",
        "Adicione créditos no console do provedor.",
    ),
    (
        "insufficient_quota",
        "A conta está sem cota disponível.",
        "Verifique o faturamento no console do provedor.",
    ),
    (
        "rate limit",
        "Limite de requisições por minuto atingido.",
        "Espere alguns segundos e tente de novo. Se for constante, o plano do "
        "provedor precisa ser elevado.",
    ),
    (
        "authentication",
        "A chave foi recusada.",
        "Confira se ela foi copiada inteira e se ainda está ativa no console do "
        "provedor. Use 'Trocar chave' para cadastrar outra.",
    ),
    (
        "invalid x-api-key",
        "A chave foi recusada.",
        "Confira se ela foi copiada inteira e se ainda está ativa no console do "
        "provedor. Use 'Trocar chave' para cadastrar outra.",
    ),
    (
        "incorrect api key",
        "A chave foi recusada.",
        "Confira se ela foi copiada inteira e se ainda está ativa no console do "
        "provedor. Use 'Trocar chave' para cadastrar outra.",
    ),
    (
        "permission",
        "A chave não tem permissão para este modelo.",
        "Verifique no console do provedor se o modelo está liberado para essa chave.",
    ),
    (
        "not_found",
        "O provedor não reconheceu o modelo.",
        "O identificador pode ter mudado do lado do provedor — avise quem mantém "
        "o catálogo de modelos.",
    ),
    (
        "temperature",
        "Este modelo não aceita o parâmetro de temperatura.",
        "Marque 'aceita_temperatura': False para ele no catálogo de modelos.",
    ),
    (
        "max_tokens",
        "O teto de tokens enviado não é aceito por este modelo.",
        "Ajuste 'max_tokens' desse modelo no catálogo.",
    ),
    (
        "overloaded",
        "O provedor está sobrecarregado no momento.",
        "É temporário — tente de novo em alguns instantes.",
    ),
    (
        "timeout",
        "O provedor não respondeu dentro do tempo limite.",
        "Tente de novo; se persistir, pode ser instabilidade do provedor.",
    ),
    (
        "connection",
        "Não foi possível alcançar o provedor.",
        "Confira a conexão de rede e se há proxy ou firewall bloqueando a saída.",
    ),
]


def mensagem_do_provedor(exc: BaseException) -> str:
    """Extrai a frase que o provedor escreveu, sem o invólucro do SDK."""
    bruto = str(exc)
    encontrado = _RE_MENSAGEM.search(bruto)
    return (encontrado.group(1) if encontrado else bruto).strip()


def explicar(exc: BaseException) -> str:
    """
    Devolve o erro em português, com o que fazer a respeito.

    Erro não catalogado volta com a frase do provedor em vez do dump — pior que
    um diagnóstico, melhor que JSON cru.
    """
    detalhe = mensagem_do_provedor(exc)
    procurado = f"{type(exc).__name__} {str(exc)}".lower()

    for termo, diagnostico, acao in _PADROES:
        if termo in procurado:
            return f"{diagnostico} {acao}\n\nProvedor: “{detalhe}”"

    status = _RE_STATUS.search(str(exc))
    prefixo = f"O provedor recusou a chamada (HTTP {status.group(1)})." if status else (
        "Falha ao falar com o provedor."
    )
    return f"{prefixo}\n\nProvedor: “{detalhe}”"
