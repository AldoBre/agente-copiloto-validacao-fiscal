"""
Azure AI Foundry — configuração, e por que ela não fica no banco.

Cada detalhe abaixo custou uma sessão de depuração.

## Só ambiente, de propósito

Diferente dos outros provedores, o Foundry **não tem campos no banco**.
Endpoint, deployments e chave são *fatos do deploy* — chegam pelas variáveis de
ambiente do servidor. Nada disso é editável por alguém na
tela de Configurações, então guardar no banco só criaria uma segunda verdade,
que diverge da primeira no dia em que a infra mudar.

Na tela isto aparece como um cartão **somente leitura**: mostra o que está
configurado e o que falta, sem campo para editar.

## Os nomes das variáveis são canônicos do SDK

``AZURE_OPENAI_ENDPOINT``, ``AZURE_OPENAI_API_KEY`` e afins são exatamente os
nomes que o ``langchain-openai`` reconhece. NÃO renomeie (ex.: para
``AZURE_OPENAI_DEPLOYMENT``): um nome fora desta lista faz a configuração
parecer presente e não ser.

## As três armadilhas

1. **O domínio é ``.cognitiveservices.azure.com``**, não ``.openai.azure.com``.
   Contas ``kind=AIServices`` — que é o que o Foundry cria — só respondem no
   primeiro. Pegue o valor exato com::

       az cognitiveservices account show -g <rg> -n <conta> \\
          --query properties.endpoint -o tsv

2. **Barra no fim quebra a URL.** O Azure devolve o endpoint com barra e o SDK
   monta ``{endpoint}/openai/deployments/{deployment}`` — sem aparar vira
   ``//openai/...``.

3. **O que se chama é o DEPLOYMENT, não o modelo.** O nome é escolhido por quem
   fez o deploy, e chat e embeddings são deployments diferentes na mesma conta —
   por isso as duas variáveis.

## Por que falhar alto

Configuração incompleta levanta :class:`ConfiguracaoFoundryIncompleta` em vez de
cair para a OpenAI pública. Com uma ``OPENAI_API_KEY`` no ambiente, o fallback
silencioso *funcionaria* — e mandaria nota fiscal de cliente para fora do nosso
tenant sem ninguém perceber. É o bug caro que este módulo existe para impedir.
"""
from __future__ import annotations

import os
from dataclasses import dataclass

#: Versão da API. Medido contra o deployment real em 19/08/2026: ``2024-10-21``
#: atende tanto gpt-4o-mini quanto gpt-5.5 — a crença de que gpt-5.x exigiria
#: uma versão de 2025 não se confirmou nesta conta. Já ``2026-01-01-preview``
#: devolve 404. Mudar isto sem medir é trocar um valor que funciona por um
#: palpite; o teste é uma chamada ao deployment.
VERSAO_API_PADRAO = "2024-10-21"

#: Nomes canônicos do SDK. Renomear aqui desliga a integração em silêncio.
ENV_ENDPOINT = "AZURE_OPENAI_ENDPOINT"
ENV_API_KEY = "AZURE_OPENAI_API_KEY"
ENV_DEPLOYMENT = "AZURE_OPENAI_API_DEPLOYMENT_NAME"
ENV_DEPLOYMENT_EMBEDDINGS = "AZURE_OPENAI_API_EMBEDDINGS_DEPLOYMENT_NAME"
ENV_VERSAO_API = "AZURE_OPENAI_API_VERSION"


class ConfiguracaoFoundryIncompleta(RuntimeError):
    """Falta endpoint, chave ou deployment — e não vamos adivinhar."""


@dataclass(frozen=True)
class ConfigFoundry:
    endpoint: str
    api_key: str
    deployment: str
    versao_api: str

    @property
    def url_deployment(self) -> str:
        """A URL que o SDK vai montar. Só para log e diagnóstico."""
        return f"{self.endpoint}/openai/deployments/{self.deployment}"


#: Uma referência de Key Vault que o App Service NÃO conseguiu resolver é
#: entregue à aplicação como o PRÓPRIO TEXTO da referência, não como vazio
#: ("If a reference isn't resolved properly, the reference string is used
#: instead" — doc do App Service). Sem tratar isso, o texto passa por qualquer
#: checagem de "está preenchido?", vai como chave para o Azure e volta um 401
#: opaco — escondendo o que realmente aconteceu, que é falta de permissão da
#: managed identity no vault. Todo erro de RBAC se disfarçaria de chave errada.
_PREFIXO_REFERENCIA_NAO_RESOLVIDA = "@Microsoft.KeyVault"


def _env(nome: str) -> str:
    valor = (os.getenv(nome) or "").strip()
    return "" if valor.startswith(_PREFIXO_REFERENCIA_NAO_RESOLVIDA) else valor


def referencias_nao_resolvidas() -> list[str]:
    """Variáveis que chegaram como referência de Key Vault crua."""
    return [
        nome
        for nome in (ENV_ENDPOINT, ENV_API_KEY, ENV_DEPLOYMENT, ENV_DEPLOYMENT_EMBEDDINGS)
        if (os.getenv(nome) or "").strip().startswith(_PREFIXO_REFERENCIA_NAO_RESOLVIDA)
    ]


def endpoint() -> str:
    """Endpoint sem a barra final — ver armadilha 2."""
    return _env(ENV_ENDPOINT).rstrip("/")


def api_key() -> str:
    return _env(ENV_API_KEY)


def deployment(*, para_embeddings: bool = False) -> str:
    return _env(ENV_DEPLOYMENT_EMBEDDINGS if para_embeddings else ENV_DEPLOYMENT)


def versao_api() -> str:
    return _env(ENV_VERSAO_API) or VERSAO_API_PADRAO


def resolver(*, para_embeddings: bool = False) -> ConfigFoundry:
    """
    Monta a configuração, ou explica o que falta.

    ``para_embeddings`` troca a variável do deployment: chat e embeddings são
    deployments diferentes na mesma conta.
    """
    alvo_endpoint = endpoint()
    alvo_chave = api_key()
    alvo_deployment = deployment(para_embeddings=para_embeddings)

    faltando = [
        rotulo
        for valor, rotulo in (
            (alvo_endpoint, ENV_ENDPOINT),
            (alvo_chave, ENV_API_KEY),
            (alvo_deployment, ENV_DEPLOYMENT_EMBEDDINGS if para_embeddings else ENV_DEPLOYMENT),
        )
        if not valor
    ]
    if faltando:
        nao_resolvidas = referencias_nao_resolvidas()
        if nao_resolvidas:
            raise ConfiguracaoFoundryIncompleta(
                "O App Service não conseguiu resolver a referência de Key Vault de: "
                + ", ".join(nao_resolvidas)
                + ". Isso é permissão, não configuração: a managed identity do app "
                "precisa da role 'Key Vault Secrets User' no segredo. Diagnostique com: "
                "az webapp config appsettings list -g <rg> -n <app> e "
                "az rest --method get --url '<appId>/config/configreferences/appsettings"
                "?api-version=2022-03-01' — o status vem em 'Resolved' ou com o motivo."
            )
        raise ConfiguracaoFoundryIncompleta(
            "Azure AI Foundry não está configurado nesta instância — faltando: "
            + ", ".join(faltando)
            + ". Estes valores vêm das variáveis de ambiente do servidor, não da "
            "tela. A chamada NÃO foi redirecionada para a OpenAI "
            "pública de propósito: mandar nota fiscal para fora do nosso tenant por "
            "engano é pior que falhar."
        )

    if ".openai.azure.com" in alvo_endpoint:
        # Erro clássico, e o sintoma é um 404 opaco vindo de dentro do SDK.
        raise ConfiguracaoFoundryIncompleta(
            f"O endpoint '{alvo_endpoint}' usa o domínio antigo .openai.azure.com. As "
            "contas do Foundry (kind=AIServices) respondem em "
            ".cognitiveservices.azure.com. Confira com: az cognitiveservices account "
            "show -g <rg> -n <conta> --query properties.endpoint -o tsv"
        )

    return ConfigFoundry(
        endpoint=alvo_endpoint,
        api_key=alvo_chave,
        deployment=alvo_deployment,
        versao_api=versao_api(),
    )


def configurado(*, para_embeddings: bool = False) -> bool:
    try:
        resolver(para_embeddings=para_embeddings)
        return True
    except ConfiguracaoFoundryIncompleta:
        return False


def _mascarar(chave: str) -> str:
    """Prévia da chave — nunca a chave. Mesma ideia do ``mascarar`` do crypto."""
    if not chave:
        return ""
    return f"{chave[:4]}…{chave[-4:]}" if len(chave) > 12 else "…"


def para_frontend() -> dict:
    """
    O que a tela mostra no cartão do Foundry.

    Tudo somente leitura: ``fromDatabase`` é sempre ``False`` porque a chave vem
    do ambiente, nunca do banco.
    """
    return {
        # endpoint + chave + deployment de chat → dá para usar o Foundry.
        "configured": configurado(),
        # Embeddings dependem do deployment próprio, e são independentes do chat.
        "embeddingsActive": configurado(para_embeddings=True),
        "endpoint": endpoint(),
        "deployment": deployment(),
        "embeddingDeployment": deployment(para_embeddings=True),
        "apiVersion": versao_api(),
        "key": {
            "configured": bool(api_key()),
            "fromDatabase": False,
            "preview": _mascarar(api_key()),
        },
    }
