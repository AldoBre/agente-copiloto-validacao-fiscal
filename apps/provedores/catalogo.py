"""
Catálogo estático de provedores e modelos.

Por que estático: o consultor não deve escolher temperatura, teto de tokens nem
timeout — errar qualquer um deles degrada a resposta sem aviso. O que ele
escolhe é **o modelo**; o resto vem daqui.

Cada modelo declara suas próprias capacidades porque elas diferem de verdade:

* ``aceita_temperatura`` — os modelos Claude 4.7+ **rejeitam** ``temperature``
  com HTTP 400. Mandar o campo "só por garantia" quebra a chamada.
* ``max_tokens`` — teto de saída do modelo. Não é meta, é limite; sobra é
  gratuita e falta trunca a resposta no meio.
* ``parametros_extras`` (opcional) — parâmetros que só aquele modelo entende,
  como ``reasoning_effort``. Ficam aqui, e não no registro do provedor, porque
  são atributo do MODELO: gravados no banco, sobreviveriam à troca de modelo e
  um ``reasoning_effort`` herdado faz o gpt-4.1 devolver HTTP 400. A fábrica
  lê daqui a cada chamada (``factory.construir_chat``).

Para acrescentar um modelo novo, basta uma linha aqui — nada de migração nem
mudança de tela.
"""
from __future__ import annotations

from typing import Any

CHAT = "chat"
EMBEDDING = "embedding"

#: Timeout único para todos: análise fiscal com raciocínio estendido é lenta,
#: e o custo de esperar é sempre menor que o de perder a resposta pronta.
TIMEOUT_SEGUNDOS = 600

#: Temperatura fixa. O agente lê um relatório determinístico e responde sobre
#: parametrização — variação criativa aqui é defeito, não recurso.
TEMPERATURA = 0.0


CATALOGO: dict[str, dict[str, Any]] = {
    "anthropic": {
        "rotulo": "Anthropic (Claude)",
        "ajuda_chave": "Chave em console.anthropic.com → API Keys (começa com sk-ant-).",
        # A Anthropic não publica modelo de embeddings próprio.
        "embedding_padrao": None,
        "modelos": [
            {
                "id": "claude-opus-5",
                "rotulo": "Claude Opus 5",
                "tipo": CHAT,
                "max_tokens": 64000,
                "aceita_temperatura": False,
                "descricao": "O mais capaz. Recomendado para análise fiscal.",
                "recomendado": True,
            },
            {
                "id": "claude-sonnet-5",
                "rotulo": "Claude Sonnet 5",
                "tipo": CHAT,
                "max_tokens": 64000,
                "aceita_temperatura": False,
                "descricao": "Equilíbrio entre qualidade e custo.",
            },
            {
                "id": "claude-opus-4-8",
                "rotulo": "Claude Opus 4.8",
                "tipo": CHAT,
                "max_tokens": 64000,
                "aceita_temperatura": False,
                "descricao": "Geração anterior do Opus.",
            },
            {
                "id": "claude-haiku-4-5",
                "rotulo": "Claude Haiku 4.5",
                "tipo": CHAT,
                "max_tokens": 32000,
                "aceita_temperatura": True,
                "descricao": "Mais rápido e barato; respostas mais simples.",
            },
        ],
    },
    "openai": {
        "rotulo": "OpenAI (GPT)",
        "ajuda_chave": "Chave em platform.openai.com → API Keys (começa com sk-).",
        # A mesma chave atende chat e embeddings.
        "embedding_padrao": "text-embedding-3-large",
        # Família GPT-5.6 e GPT-6 — conferido em developers.openai.com/api/docs/models
        # em 20/09/2026: contexto de 1,05M, saída de até 128k, todos de raciocínio.
        #
        # * ``aceita_temperatura: False`` — é o mesmo comportamento medido no
        #   gpt-5.5 (HTTP 400 para qualquer valor fora do padrão). A documentação
        #   não confirma nem nega para a 5.6; False é o lado seguro, porque a
        #   fábrica simplesmente não manda o campo.
        # * ``reasoning_effort: low`` — o padrão da API é ``medium``, e foi o
        #   raciocínio longo somado às até 4 idas ao provedor que levou uma
        #   análise de duas NFS-e a ~2 min. Valores aceitos: none, low, medium,
        #   high, xhigh, max. Subir aqui é trocar velocidade por profundidade.
        # * ``max_tokens: 16384`` — em modelo de raciocínio o teto inclui os
        #   tokens de raciocínio; mesmo valor que já funciona no gpt-5.5.
        "modelos": [
            {
                "id": "gpt-5.6-terra",
                "rotulo": "GPT-5.6 Terra",
                "tipo": CHAT,
                "max_tokens": 16384,
                "aceita_temperatura": False,
                "parametros_extras": {"reasoning_effort": "low"},
                "descricao": "Equilíbrio entre qualidade e custo. Qualidade do GPT-5.5 pela metade do preço.",
                "recomendado": True,
            },
            {
                "id": "gpt-5.6-luna",
                "rotulo": "GPT-5.6 Luna",
                "tipo": CHAT,
                "max_tokens": 16384,
                "aceita_temperatura": False,
                "parametros_extras": {"reasoning_effort": "low"},
                "descricao": "O mais rápido e barato da família 5.6.",
            },
            {
                "id": "gpt-5.6-sol",
                "rotulo": "GPT-5.6 Sol",
                "tipo": CHAT,
                "max_tokens": 16384,
                "aceita_temperatura": False,
                "parametros_extras": {"reasoning_effort": "low"},
                "descricao": "Topo da família 5.6, para análise complexa. Mais lento e mais caro.",
            },
            {
                "id": "gpt-6-astra",
                "rotulo": "GPT-6 Astra",
                "tipo": CHAT,
                "max_tokens": 16384,
                "aceita_temperatura": False,
                "parametros_extras": {"reasoning_effort": "low"},
                "descricao": "O mais capaz da OpenAI. Reserve para o caso difícil: é o mais caro e o mais lento.",
            },
            {
                "id": "gpt-4.1",
                "rotulo": "GPT-4.1",
                "tipo": CHAT,
                "max_tokens": 32768,
                "aceita_temperatura": True,
                "descricao": "Geração anterior, sem raciocínio estendido. Resposta direta e rápida.",
            },
            {
                "id": "gpt-4o",
                "rotulo": "GPT-4o",
                "tipo": CHAT,
                "max_tokens": 16384,
                "aceita_temperatura": True,
                "descricao": "Bom equilíbrio entre qualidade e custo.",
            },
            {
                "id": "gpt-4.1-mini",
                "rotulo": "GPT-4.1 mini",
                "tipo": CHAT,
                "max_tokens": 32768,
                "aceita_temperatura": True,
                "descricao": "Mais rápido e barato.",
            },
            {
                "id": "text-embedding-3-large",
                "rotulo": "Embeddings 3 large",
                "tipo": EMBEDDING,
                "max_tokens": 0,
                "aceita_temperatura": False,
                "descricao": "Busca semântica na base de conhecimento.",
                "recomendado": True,
            },
            {
                "id": "text-embedding-3-small",
                "rotulo": "Embeddings 3 small",
                "tipo": EMBEDDING,
                "max_tokens": 0,
                "aceita_temperatura": False,
                "descricao": "Busca semântica mais barata.",
            },
        ],
    },
    "google": {
        "rotulo": "Google (Gemini)",
        "ajuda_chave": "Chave em aistudio.google.com → Get API key.",
        "embedding_padrao": "models/text-embedding-004",
        "modelos": [
            {
                "id": "gemini-2.0-pro",
                "rotulo": "Gemini 2.0 Pro",
                "tipo": CHAT,
                "max_tokens": 8192,
                "aceita_temperatura": True,
                "descricao": "Recomendado para análise fiscal.",
                "recomendado": True,
            },
            {
                "id": "gemini-2.0-flash",
                "rotulo": "Gemini 2.0 Flash",
                "tipo": CHAT,
                "max_tokens": 8192,
                "aceita_temperatura": True,
                "descricao": "Mais rápido e barato.",
            },
            {
                "id": "models/text-embedding-004",
                "rotulo": "Text Embedding 004",
                "tipo": EMBEDDING,
                "max_tokens": 0,
                "aceita_temperatura": False,
                "descricao": "Busca semântica na base de conhecimento.",
            },
        ],
    },
    "azure": {
        "rotulo": "Azure AI Foundry",
        "ajuda_chave": (
            "Não precisa de chave aqui: ela vem do ambiente do servidor. Endpoint e "
            "deployment também — ver o cartão do Foundry ao lado."
        ),
        # Mesma conta atende chat e embeddings; o que muda é o deployment.
        "embedding_padrao": "text-embedding-3-large",
        # ATENÇÃO — esta lista é curta de propósito, e precisa espelhar os
        # DEPLOYMENTS que existem de verdade na conta.
        #
        # No Azure quem é chamado é o deployment (vem de
        # AZURE_OPENAI_API_DEPLOYMENT_NAME), e o modelo escolhido aqui só serve
        # para tirar daqui o teto de tokens e se o modelo aceita `temperature`.
        # Os dois são atributos do MODELO POR TRÁS do deployment: oferecer aqui
        # um modelo que não está deployado faz o app mandar parâmetro
        # incompatível e receber HTTP 400 — com o agravante de o operador ter
        # escolhido justamente a opção que a tela marcava como recomendada.
        #
        # Ao criar um deployment novo na conta, acrescente a linha dele aqui.
        # Conferir com:
        #   az cognitiveservices account deployment list -g <rg> -n <conta> -o table
        "modelos": [
            {
                "id": "gpt-5.5",
                "rotulo": "GPT-5.5 (Foundry)",
                "tipo": CHAT,
                "max_tokens": 16384,
                # Medido contra o deployment real em 19/08/2026: mandar
                # temperature=0 devolve HTTP 400 "does not support 0 with this
                # model. Only the default (1) value is supported" — mesma
                # situação dos Claude 4.7+. Com True aqui, TODA chamada falha.
                "aceita_temperatura": False,
                # Medido em 20/09/2026 pelo log de produção: numa análise de
                # lote, a última ida ao modelo levou 47,7 s até o PRIMEIRO byte
                # — raciocínio invisível, com a tela parada. O padrão da API é
                # `medium`. Se este deployment/api-version recusar o parâmetro,
                # o agente recua sozinho e segue sem ele (graph.no_responder);
                # o chat não cai por causa disto.
                "parametros_extras": {"reasoning_effort": "low"},
                "descricao": "Modelo do deployment dedicado deste projeto.",
                "recomendado": True,
            },
            {
                "id": "text-embedding-3-large",
                "rotulo": "Embeddings 3 large (Foundry)",
                "tipo": EMBEDDING,
                "max_tokens": 0,
                "aceita_temperatura": False,
                # 3.072 dimensões, igual ao corpus já gravado pela OpenAI
                # pública — por isso `dimensions` NÃO é passado em factory.py.
                "descricao": "Busca semântica na base de conhecimento.",
            },
        ],
    },
}


def provedores_suportados() -> list[str]:
    return list(CATALOGO)


def buscar_modelo(provedor: str, modelo_id: str) -> dict[str, Any] | None:
    for modelo in CATALOGO.get(provedor, {}).get("modelos", []):
        if modelo["id"] == modelo_id:
            return modelo
    return None


def rotulo_do_modelo(provedor: str, modelo_id: str) -> str:
    modelo = buscar_modelo(provedor, modelo_id)
    return modelo["rotulo"] if modelo else modelo_id


def rotulo_do_provedor(provedor: str) -> str:
    return CATALOGO.get(provedor, {}).get("rotulo", provedor)


def embedding_padrao(provedor: str) -> str | None:
    """
    Modelo de embeddings recomendado do provedor, ou ``None`` se ele não tiver.

    Serve para o atalho "usar a mesma chave para a busca semântica": nenhum
    modelo de chat gera embeddings — são endpoints diferentes — mas a
    credencial é a mesma, então dá para cadastrar os dois de uma vez.
    """
    return CATALOGO.get(provedor, {}).get("embedding_padrao")


def para_frontend() -> list[dict[str, Any]]:
    """Estrutura consumida pelos selects da tela de configurações."""
    return [
        {
            "valor": chave,
            "rotulo": dados["rotulo"],
            "ajuda_chave": dados["ajuda_chave"],
            "embedding_padrao": dados.get("embedding_padrao"),
            "modelos": [
                {
                    "id": m["id"],
                    "rotulo": m["rotulo"],
                    "tipo": m["tipo"],
                    "descricao": m.get("descricao", ""),
                    "recomendado": m.get("recomendado", False),
                }
                for m in dados["modelos"]
            ],
        }
        for chave, dados in CATALOGO.items()
    ]
