"""
Fábrica de modelos LangChain a partir de um :class:`ProvedorIA`.

Os pacotes de cada provedor são importados sob demanda: se o `langchain-groq`
não estiver instalado, só quebra quem tentar usar o Groq — os demais seguem
funcionando.
"""
from __future__ import annotations

import logging
from typing import Any

from .catalogo import buscar_modelo
from .models import Provedor, ProvedorIA, TipoModelo

logger = logging.getLogger(__name__)


class ProvedorIndisponivel(RuntimeError):
    """Provedor não instalado, mal configurado ou sem credencial."""


def _config_foundry(*, para_embeddings: bool = False):
    """
    Resolve a configuração do Foundry (só ambiente — ver ``foundry.py``),
    convertendo a falha no erro que a camada de cima já sabe exibir.
    """
    from .foundry import ConfiguracaoFoundryIncompleta, resolver

    try:
        return resolver(para_embeddings=para_embeddings)
    except ConfiguracaoFoundryIncompleta as exc:
        raise ProvedorIndisponivel(str(exc)) from exc


def _erro_import(provedor: str, pacote: str, exc: Exception) -> ProvedorIndisponivel:
    return ProvedorIndisponivel(
        f"O provedor '{provedor}' exige o pacote '{pacote}', que não está instalado "
        f"neste ambiente. Rode: pip install {pacote}  ({exc})"
    )


# --------------------------------------------------------------------------- #
#  Extras do catálogo — e o recuo quando o provedor recusa um deles
# --------------------------------------------------------------------------- #
#: (provedor, modelo, parâmetro) que o provedor RECUSOU neste processo. Um
#: extra do catálogo é uma aposta sobre o que o deployment aceita; no Azure a
#: resposta depende da api-version, que não se descobre sem chamar. Em vez de
#: derrubar o chat, quem chama marca a recusa aqui e reconstrói o modelo sem o
#: parâmetro. Vale pela vida do processo: a recusa não muda entre chamadas.
_EXTRAS_RECUSADOS: set[tuple[str, str, str]] = set()


def extras_do_catalogo(provedor: ProvedorIA) -> dict[str, Any]:
    """Os ``parametros_extras`` do modelo no catálogo, menos os já recusados."""
    entrada = buscar_modelo(provedor.provedor, provedor.modelo) or {}
    return {
        nome: valor
        for nome, valor in (entrada.get("parametros_extras") or {}).items()
        if (provedor.provedor, provedor.modelo, nome) not in _EXTRAS_RECUSADOS
    }


def recusar_extra_citado_no_erro(provedor: ProvedorIA, erro: BaseException) -> str | None:
    """
    Se o erro do provedor cita um extra do catálogo, marca-o como recusado.

    Devolve o nome do parâmetro (para o log) ou ``None`` quando o erro não tem
    relação com extras — caso em que quem chamou deve tratar o erro normalmente.
    Só olha extras do CATÁLOGO: o que o operador gravou no registro do provedor
    é escolha dele, e esconder a recusa disso mascararia um cadastro errado.
    """
    texto = str(erro)
    for nome in extras_do_catalogo(provedor):
        if nome in texto:
            _EXTRAS_RECUSADOS.add((provedor.provedor, provedor.modelo, nome))
            return nome
    return None


# --------------------------------------------------------------------------- #
#  Modelos de chat
# --------------------------------------------------------------------------- #
def construir_chat(provedor: ProvedorIA, *, streaming: bool = True) -> Any:
    """Devolve um ``BaseChatModel`` do LangChain configurado."""
    if provedor.tipo != TipoModelo.CHAT:
        raise ProvedorIndisponivel(
            f"'{provedor.nome}' está cadastrado como {provedor.get_tipo_display()}, "
            "não pode ser usado no chat."
        )

    entrada = buscar_modelo(provedor.provedor, provedor.modelo)

    # Os extras do catálogo (ex.: `reasoning_effort`) são atributo do modelo e
    # entram a cada chamada, sem passar pelo banco — assim trocar de modelo
    # não deixa parâmetro órfão para trás. O que estiver no registro do
    # provedor vence, para permitir ajuste pontual sem mexer no catálogo.
    comuns: dict[str, Any] = {
        **extras_do_catalogo(provedor),
        **(provedor.parametros_extras or {}),
    }

    # Claude 4.7+ REJEITA `temperature` com HTTP 400 — mandar "por garantia"
    # quebra a chamada. Quem decide é o catálogo, modelo a modelo.
    aceita_temperatura = entrada["aceita_temperatura"] if entrada else True
    if aceita_temperatura:
        comuns.setdefault("temperature", provedor.temperatura)

    p = provedor.provedor

    if p == Provedor.ANTHROPIC:
        try:
            from langchain_anthropic import ChatAnthropic
        except ImportError as exc:
            raise _erro_import(p, "langchain-anthropic", exc) from exc
        return ChatAnthropic(
            model=provedor.modelo,
            api_key=provedor.api_key,
            max_tokens=provedor.max_tokens,
            streaming=streaming,
            timeout=provedor.timeout_segundos,
            **comuns,
        )

    if p == Provedor.OPENAI:
        try:
            from langchain_openai import ChatOpenAI
        except ImportError as exc:
            raise _erro_import(p, "langchain-openai", exc) from exc
        return ChatOpenAI(
            model=provedor.modelo,
            api_key=provedor.api_key,
            max_tokens=provedor.max_tokens,
            streaming=streaming,
            timeout=provedor.timeout_segundos,
            **comuns,
        )

    if p == Provedor.AZURE:
        try:
            from langchain_openai import AzureChatOpenAI
        except ImportError as exc:
            raise _erro_import(p, "langchain-openai", exc) from exc

        cfg = _config_foundry()
        logger.info("Foundry (chat): %s · api-version %s", cfg.url_deployment, cfg.versao_api)
        # Os nomes abaixo são os públicos do SDK. NÃO troque por `model=` ou
        # `deployment_name=`: o AzureChatOpenAI ignora o que não reconhece, e o
        # sintoma é um 404 ou uma chamada para o deployment errado.
        return AzureChatOpenAI(
            azure_endpoint=cfg.endpoint,
            azure_deployment=cfg.deployment,
            api_key=cfg.api_key,
            api_version=cfg.versao_api,
            max_tokens=provedor.max_tokens,
            streaming=streaming,
            timeout=provedor.timeout_segundos,
            **comuns,
        )

    if p == Provedor.GOOGLE:
        try:
            from langchain_google_genai import ChatGoogleGenerativeAI
        except ImportError as exc:
            raise _erro_import(p, "langchain-google-genai", exc) from exc
        return ChatGoogleGenerativeAI(
            model=provedor.modelo,
            google_api_key=provedor.api_key,
            max_output_tokens=provedor.max_tokens,
            **comuns,
        )

    raise ProvedorIndisponivel(f"Provedor desconhecido: {p}")


# --------------------------------------------------------------------------- #
#  Modelos de embedding
# --------------------------------------------------------------------------- #
def construir_embeddings(provedor: ProvedorIA) -> Any:
    """Devolve um ``Embeddings`` do LangChain configurado."""
    if provedor.tipo != TipoModelo.EMBEDDING:
        raise ProvedorIndisponivel(
            f"'{provedor.nome}' não está cadastrado como provedor de embeddings."
        )

    extras: dict[str, Any] = dict(provedor.parametros_extras or {})
    p = provedor.provedor

    if p == Provedor.OPENAI:
        try:
            from langchain_openai import OpenAIEmbeddings
        except ImportError as exc:
            raise _erro_import(p, "langchain-openai", exc) from exc
        return OpenAIEmbeddings(model=provedor.modelo, api_key=provedor.api_key, **extras)

    if p == Provedor.AZURE:
        try:
            from langchain_openai import AzureOpenAIEmbeddings
        except ImportError as exc:
            raise _erro_import(p, "langchain-openai", exc) from exc

        # Deployment DIFERENTE do chat, na mesma conta — por isso a variável de
        # ambiente própria (AZURE_OPENAI_API_EMBEDDINGS_DEPLOYMENT_NAME).
        cfg = _config_foundry(para_embeddings=True)
        logger.info("Foundry (embeddings): %s", cfg.url_deployment)
        return AzureOpenAIEmbeddings(
            azure_endpoint=cfg.endpoint,
            azure_deployment=cfg.deployment,
            api_key=cfg.api_key,
            api_version=cfg.versao_api,
            **extras,
        )

    if p == Provedor.GOOGLE:
        try:
            from langchain_google_genai import GoogleGenerativeAIEmbeddings
        except ImportError as exc:
            raise _erro_import(p, "langchain-google-genai", exc) from exc
        return GoogleGenerativeAIEmbeddings(
            model=provedor.modelo, google_api_key=provedor.api_key, **extras
        )

    raise ProvedorIndisponivel(
        f"O provedor '{p}' não oferece modelo de embeddings. Use OpenAI, Google ou "
        "Azure AI Foundry para habilitar a busca semântica na base de conhecimento."
    )


# --------------------------------------------------------------------------- #
#  Teste de conectividade (usado pelo botão "Testar" da tela de configurações)
# --------------------------------------------------------------------------- #
def testar(provedor: ProvedorIA) -> tuple[bool, str]:
    """Faz uma chamada mínima e devolve ``(ok, mensagem)``."""
    try:
        if provedor.tipo == TipoModelo.EMBEDDING:
            emb = construir_embeddings(provedor)
            vetor = emb.embed_query("teste de conectividade")
            return True, f"OK — embedding com {len(vetor)} dimensões."

        chat = construir_chat(provedor, streaming=False)
        resposta = chat.invoke("Responda apenas com a palavra: OK")
        texto = getattr(resposta, "content", str(resposta))
        if isinstance(texto, list):  # alguns provedores devolvem blocos
            texto = " ".join(
                bloco.get("text", "") for bloco in texto if isinstance(bloco, dict)
            )
        return True, f"OK — resposta: {str(texto).strip()[:120]}"
    except ProvedorIndisponivel as exc:
        return False, str(exc)
    except Exception as exc:  # noqa: BLE001 — qualquer falha do provedor vira texto
        logger.warning("Teste do provedor %s falhou: %s", provedor.nome, exc)
        from .erros import explicar

        return False, explicar(exc)
