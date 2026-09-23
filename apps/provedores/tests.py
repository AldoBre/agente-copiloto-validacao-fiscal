"""
Azure AI Foundry — os invariantes que impedem o pior desfecho.

O pior desfecho aqui não é "não funciona": é **funcionar pelo caminho errado**.
Com uma ``OPENAI_API_KEY`` presente no ambiente, um Foundry mal configurado que
caísse para a OpenAI pública responderia normalmente — e mandaria nota fiscal de
cliente para fora do nosso tenant sem ninguém notar. É por isso que boa parte
dos testes abaixo verifica que algo **falha**.
"""
from __future__ import annotations

import os

from django.core.exceptions import ValidationError
from django.test import TestCase
from rest_framework.test import APIClient

from . import foundry
from .factory import ProvedorIndisponivel, construir_chat, construir_embeddings
from .models import Provedor, ProvedorIA, TipoModelo

ENDPOINT = "https://oai-exemplo-teste.cognitiveservices.azure.com"

COMPLETO = {
    foundry.ENV_ENDPOINT: ENDPOINT,
    foundry.ENV_API_KEY: "chave-secreta-do-key-vault",
    foundry.ENV_DEPLOYMENT: "gpt41-implantacao",
    foundry.ENV_DEPLOYMENT_EMBEDDINGS: "emb3-large",
}


class ambiente:
    """Define as variáveis do Foundry e restaura tudo no fim, dê no que der."""

    def __init__(self, **variaveis):
        self.variaveis = variaveis

    def __enter__(self):
        todas = {
            foundry.ENV_ENDPOINT: None,
            foundry.ENV_API_KEY: None,
            foundry.ENV_DEPLOYMENT: None,
            foundry.ENV_DEPLOYMENT_EMBEDDINGS: None,
            foundry.ENV_VERSAO_API: None,
            **self.variaveis,
        }
        self.antes = {chave: os.environ.get(chave) for chave in todas}
        for chave, valor in todas.items():
            if valor is None:
                os.environ.pop(chave, None)
            else:
                os.environ[chave] = valor
        return self

    def __exit__(self, *_):
        for chave, valor in self.antes.items():
            if valor is None:
                os.environ.pop(chave, None)
            else:
                os.environ[chave] = valor
        return False


def registro(modelo: str = "gpt-5.5") -> ProvedorIA:
    """O registro do Foundry: só diz QUAL modelo usar. Nada de credencial."""
    provedor = ProvedorIA(nome="Foundry", provedor=Provedor.AZURE, modelo=modelo)
    provedor.aplicar_catalogo()
    return provedor


class ConfiguracaoVemDoAmbiente(TestCase):
    def test_barra_no_fim_e_aparada(self):
        """
        O Azure devolve o endpoint COM barra e o SDK monta
        ``{endpoint}/openai/deployments/...`` — sem aparar vira ``//openai``.
        """
        with ambiente(**{**COMPLETO, foundry.ENV_ENDPOINT: ENDPOINT + "/"}):
            cfg = foundry.resolver()

        self.assertEqual(cfg.endpoint, ENDPOINT)
        self.assertEqual(cfg.url_deployment, ENDPOINT + "/openai/deployments/gpt41-implantacao")

    def test_chat_e_embeddings_sao_deployments_diferentes(self):
        with ambiente(**COMPLETO):
            self.assertEqual(foundry.resolver().deployment, "gpt41-implantacao")
            self.assertEqual(foundry.resolver(para_embeddings=True).deployment, "emb3-large")

    def test_versao_api_tem_padrao_e_pode_ser_sobreposta(self):
        with ambiente(**COMPLETO):
            self.assertEqual(foundry.resolver().versao_api, foundry.VERSAO_API_PADRAO)
        with ambiente(**COMPLETO, **{foundry.ENV_VERSAO_API: "2025-04-01"}):
            self.assertEqual(foundry.resolver().versao_api, "2025-04-01")

    def test_dominio_antigo_e_recusado_com_a_dica_certa(self):
        """
        Contas kind=AIServices não respondem em ``.openai.azure.com``. Sem esta
        checagem o sintoma é um 404 opaco vindo de dentro do SDK.
        """
        with ambiente(**{**COMPLETO, foundry.ENV_ENDPOINT: "https://x.openai.azure.com"}):
            with self.assertRaises(foundry.ConfiguracaoFoundryIncompleta) as caso:
                foundry.resolver()

        self.assertIn("cognitiveservices.azure.com", str(caso.exception))

    def test_embeddings_podem_estar_ativos_sem_o_chat_e_vice_versa(self):
        """São deployments independentes: um pode existir sem o outro."""
        sem_embeddings = {k: v for k, v in COMPLETO.items() if k != foundry.ENV_DEPLOYMENT_EMBEDDINGS}
        with ambiente(**sem_embeddings):
            self.assertTrue(foundry.configurado())
            self.assertFalse(foundry.configurado(para_embeddings=True))


class NuncaCaiNaOpenAIPublica(TestCase):
    """
    Configuração incompleta precisa ESTOURAR. É o teste mais importante do
    arquivo: o fallback silencioso responderia certo e vazaria o dado.
    """

    def test_cada_peca_faltando_e_nomeada_no_erro(self):
        for ausente in (foundry.ENV_ENDPOINT, foundry.ENV_API_KEY, foundry.ENV_DEPLOYMENT):
            with self.subTest(ausente=ausente):
                parcial = {k: v for k, v in COMPLETO.items() if k != ausente}
                with ambiente(**parcial):
                    with self.assertRaises(ProvedorIndisponivel) as caso:
                        construir_chat(registro())
                self.assertIn(ausente, str(caso.exception))

    def test_a_mensagem_diz_por_que_nao_caiu_na_openai(self):
        with ambiente():
            with self.assertRaises(ProvedorIndisponivel) as caso:
                construir_chat(registro())

        texto = str(caso.exception)
        self.assertIn("OpenAI pública", texto)
        self.assertIn("variáveis de ambiente", texto)


class ConstrucaoDoModelo(TestCase):
    def test_chat_aponta_para_o_deployment_do_ambiente(self):
        with ambiente(**COMPLETO):
            modelo = construir_chat(registro(), streaming=True)

        self.assertEqual(modelo.deployment_name, "gpt41-implantacao")
        self.assertTrue(str(modelo.azure_endpoint).startswith(ENDPOINT))
        self.assertEqual(modelo.openai_api_version, foundry.VERSAO_API_PADRAO)

    def test_chat_suporta_ferramentas(self):
        """Sem isto o agente perderia o tool-use ao trocar para o Foundry."""
        from apps.agente.ferramentas import FERRAMENTAS

        with ambiente(**COMPLETO):
            ligado = construir_chat(registro()).bind_tools(FERRAMENTAS)

        self.assertTrue(hasattr(ligado, "invoke"))

    def test_embeddings_usam_o_deployment_de_embeddings(self):
        provedor = registro("text-embedding-3-large")
        provedor.tipo = TipoModelo.EMBEDDING

        with ambiente(**COMPLETO):
            self.assertEqual(construir_embeddings(provedor).deployment, "emb3-large")


class ReferenciaDeKeyVaultNaoResolvida(TestCase):
    """
    Quando o App Service nao resolve uma referencia de Key Vault, ele entrega a
    aplicacao o TEXTO da referencia — nao vazio. Sem tratar, o texto vira a
    "chave" mandada ao Azure e volta um 401, escondendo que o problema real e
    permissao da managed identity no cofre.
    """

    REFERENCIA = "@Microsoft.KeyVault(VaultName=kv-exemplo;SecretName=azure-openai-api-key)"

    def test_referencia_crua_conta_como_ausente(self):
        with ambiente(**{**COMPLETO, foundry.ENV_API_KEY: self.REFERENCIA}):
            self.assertEqual(foundry.api_key(), "")
            self.assertFalse(foundry.configurado())

    def test_o_erro_aponta_para_permissao_e_nao_para_configuracao(self):
        with ambiente(**{**COMPLETO, foundry.ENV_API_KEY: self.REFERENCIA}):
            with self.assertRaises(ProvedorIndisponivel) as caso:
                construir_chat(registro())

        texto = str(caso.exception)
        self.assertIn("Key Vault Secrets User", texto)
        self.assertIn(foundry.ENV_API_KEY, texto)
        # E nao a mensagem generica de "nao configurado", que mandaria o time
        # procurar no lugar errado.
        self.assertNotIn("nao esta configurado", texto)


class ParametrosQueOModeloAceita(TestCase):
    """
    Medido contra o deployment real em 19/08/2026: o gpt-5.5 devolve HTTP 400
    para `temperature` ("Only the default (1) value is supported"), igual aos
    Claude 4.7+. O catalogo e quem decide se o parametro vai — com o valor
    errado ali, TODA chamada de chat falha.
    """

    def test_gpt55_nao_recebe_temperature(self):
        from .catalogo import buscar_modelo

        self.assertFalse(buscar_modelo("azure", "gpt-5.5")["aceita_temperatura"])

        with ambiente(**COMPLETO):
            modelo = construir_chat(registro("gpt-5.5"))

        self.assertIsNone(getattr(modelo, "temperature", None))

    def test_o_catalogo_azure_so_oferece_o_que_esta_deployado(self):
        """
        O modelo escolhido na tela nao escolhe o deployment — ele so define teto
        de tokens e suporte a temperature. Oferecer um modelo que nao esta
        deployado faz o app mandar parametro incompativel para o deployment que
        existe, e o operador recebe HTTP 400 tendo clicado justamente na opcao
        marcada como recomendada.
        """
        from .catalogo import CATALOGO

        chats = [m["id"] for m in CATALOGO["azure"]["modelos"] if m["tipo"] == "chat"]

        self.assertEqual(chats, ["gpt-5.5"])


class FamiliaGpt56NaOpenAIPublica(TestCase):
    """
    GPT-5.6 (Terra, Luna, Sol) e GPT-6 Astra entraram no catalogo em 20/09/2026
    para o caminho da OpenAI publica. Sao modelos de raciocinio: `temperature`
    fora do padrao derruba a chamada, e o `reasoning_effort` padrao da API
    (medium) foi o que deixou a analise de duas NFS-e em ~2 min.
    """

    NOVOS = ["gpt-5.6-terra", "gpt-5.6-luna", "gpt-5.6-sol", "gpt-6-astra"]

    def _openai(self, modelo: str, **extras) -> ProvedorIA:
        provedor = ProvedorIA(
            nome="OpenAI", provedor=Provedor.OPENAI, modelo=modelo, parametros_extras=extras
        )
        provedor.api_key = "sk-teste-nao-e-usada-em-chamada"
        provedor.aplicar_catalogo()
        return provedor

    def test_os_quatro_estao_no_dropdown(self):
        from .catalogo import para_frontend

        openai = next(p for p in para_frontend() if p["valor"] == "openai")
        ids = [m["id"] for m in openai["modelos"]]

        for modelo in self.NOVOS:
            self.assertIn(modelo, ids)

    def test_so_um_modelo_de_chat_e_o_recomendado(self):
        """Dois 'recomendado' no mesmo select nao recomendam nada."""
        from .catalogo import CATALOGO

        recomendados = [
            m["id"]
            for m in CATALOGO["openai"]["modelos"]
            if m["tipo"] == "chat" and m.get("recomendado")
        ]

        self.assertEqual(recomendados, ["gpt-5.6-terra"])

    def test_nenhum_recebe_temperature(self):
        for nome in self.NOVOS:
            modelo = construir_chat(self._openai(nome))
            self.assertIsNone(getattr(modelo, "temperature", None), nome)

    def test_reasoning_effort_vem_do_catalogo(self):
        for nome in self.NOVOS:
            modelo = construir_chat(self._openai(nome))
            self.assertEqual(modelo.reasoning_effort, "low", nome)

    def test_o_registro_do_provedor_vence_o_catalogo(self):
        """Ajuste pontual (ex.: caso dificil pede mais raciocinio) sem editar o catalogo."""
        modelo = construir_chat(self._openai("gpt-5.6-sol", reasoning_effort="high"))

        self.assertEqual(modelo.reasoning_effort, "high")

    def test_trocar_de_modelo_nao_deixa_reasoning_effort_orfao(self):
        """
        O extra mora no catalogo, nao no banco. Se fosse gravado no registro,
        trocar gpt-5.6-luna por gpt-4.1 levaria `reasoning_effort` junto, e o
        gpt-4.1 responde HTTP 400 para parametro que nao conhece.
        """
        provedor = self._openai("gpt-5.6-luna")
        construir_chat(provedor)

        provedor.modelo = "gpt-4.1"
        provedor.aplicar_catalogo()
        modelo = construir_chat(provedor)

        self.assertEqual(provedor.parametros_extras, {})
        self.assertIsNone(getattr(modelo, "reasoning_effort", None))


class RecuoQuandoOProvedorRecusaUmExtra(TestCase):
    """
    `reasoning_effort` no gpt-5.5 do Foundry e uma aposta: o Azure aceita ou
    recusa conforme a api-version, e isso so se descobre chamando. A aposta nao
    pode custar o chat de quem esta no meio de uma implantacao.
    """

    def setUp(self):
        from . import factory

        factory._EXTRAS_RECUSADOS.clear()
        self.addCleanup(factory._EXTRAS_RECUSADOS.clear)

    def test_o_gpt55_do_foundry_pede_raciocinio_curto(self):
        with ambiente(**COMPLETO):
            modelo = construir_chat(registro("gpt-5.5"))

        self.assertEqual(modelo.reasoning_effort, "low")

    def test_erro_que_cita_o_extra_desliga_o_extra(self):
        from .factory import extras_do_catalogo, recusar_extra_citado_no_erro

        provedor = registro("gpt-5.5")
        erro = RuntimeError("Error code: 400 - Unrecognized request argument supplied: reasoning_effort")

        self.assertEqual(recusar_extra_citado_no_erro(provedor, erro), "reasoning_effort")
        self.assertEqual(extras_do_catalogo(provedor), {})

        with ambiente(**COMPLETO):
            modelo = construir_chat(provedor)
        self.assertIsNone(getattr(modelo, "reasoning_effort", None))

    def test_erro_sem_relacao_nao_desliga_nada(self):
        """Cota estourada, timeout, chave errada: nada disso e culpa do extra."""
        from .factory import extras_do_catalogo, recusar_extra_citado_no_erro

        provedor = registro("gpt-5.5")

        self.assertIsNone(recusar_extra_citado_no_erro(provedor, RuntimeError("429 Too Many Requests")))
        self.assertEqual(extras_do_catalogo(provedor), {"reasoning_effort": "low"})

    def test_extra_gravado_pelo_operador_nao_e_escondido(self):
        """So o catalogo recua. Cadastro errado do operador tem que aparecer como erro."""
        from .factory import recusar_extra_citado_no_erro

        provedor = ProvedorIA(
            nome="OpenAI", provedor=Provedor.OPENAI, modelo="gpt-4.1",
            parametros_extras={"parametro_inventado": 1},
        )
        provedor.aplicar_catalogo()

        self.assertIsNone(
            recusar_extra_citado_no_erro(provedor, RuntimeError("unknown: parametro_inventado"))
        )


class CadastroPelaTela(TestCase):
    def test_registro_do_foundry_nao_exige_chave(self):
        """A chave vem do Key Vault; pedir para colar duplicaria o segredo."""
        registro().full_clean()  # não pode levantar

    def test_os_outros_provedores_continuam_exigindo_chave(self):
        outro = ProvedorIA(nome="OpenAI", provedor=Provedor.OPENAI, modelo="gpt-4.1")
        outro.aplicar_catalogo()

        with self.assertRaises(ValidationError) as caso:
            outro.full_clean()

        self.assertIn("api_key", caso.exception.message_dict)

    def test_modelo_fora_do_catalogo_e_recusado(self):
        with self.assertRaises(ValidationError):
            registro("gpt-inexistente").full_clean()


class RotaPlatformSettings(TestCase):
    """
    ``GET /api/platform-settings/`` devolve o bloco ``azure``.
    """

    def test_contrato_da_rota(self):
        with ambiente(**COMPLETO):
            resposta = APIClient().get("/api/platform-settings/")

        self.assertEqual(resposta.status_code, 200)
        azure = resposta.json()["azure"]
        self.assertEqual(
            set(azure),
            {
                "configured",
                "embeddingsActive",
                "endpoint",
                "deployment",
                "embeddingDeployment",
                "apiVersion",
                "key",
            },
        )
        self.assertTrue(azure["configured"])
        self.assertTrue(azure["embeddingsActive"])
        self.assertEqual(azure["deployment"], "gpt41-implantacao")
        self.assertEqual(azure["embeddingDeployment"], "emb3-large")

    def test_a_chave_nunca_sai_inteira(self):
        with ambiente(**COMPLETO):
            azure = APIClient().get("/api/platform-settings/").json()["azure"]

        self.assertTrue(azure["key"]["configured"])
        self.assertNotIn(COMPLETO[foundry.ENV_API_KEY], str(azure))
        # Sempre da infra, nunca do banco — é o que o rótulo da tela promete.
        self.assertFalse(azure["key"]["fromDatabase"])

    def test_sem_configuracao_a_tela_sabe_avisar(self):
        with ambiente():
            azure = APIClient().get("/api/platform-settings/").json()["azure"]

        self.assertFalse(azure["configured"])
        self.assertFalse(azure["embeddingsActive"])
        self.assertFalse(azure["key"]["configured"])

    def test_nao_existe_escrita(self):
        """Editar aqui criaria uma segunda verdade, que diverge da infra."""
        with ambiente(**COMPLETO):
            resposta = APIClient().put("/api/platform-settings/", {}, format="json")

        self.assertEqual(resposta.status_code, 405)
