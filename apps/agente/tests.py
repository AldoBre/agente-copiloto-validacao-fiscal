"""
Testes das ferramentas do agente e do ciclo que as executa.

O foco não é cobertura: é travar os invariantes que já custaram caro em
produção. Dois deles, especificamente:

1. **Tabela vazia nunca vira acusação.** Em 12/08/2026 o `openpyxl` faltou no
   container, a tabela de CFOP ficou vazia e a conferência passou a acusar CFOPs
   válidos de não existirem. Numa ferramenta o risco é o mesmo, e pior: o
   resultado vai direto para o texto que o consultor lê.
2. **O ciclo de ferramentas termina.** Um modelo que pede consulta
   indefinidamente não pode prender o turno — e a parada não pode depender de
   ele decidir encerrar.
"""
from __future__ import annotations

from asgiref.sync import async_to_sync
from django.test import TestCase, override_settings
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import AIMessageChunk, HumanMessage, ToolMessage
from langchain_core.messages.tool import tool_call_chunk
from langchain_core.outputs import ChatGenerationChunk

from apps.fiscal.models import Cest, Cfop, FcpUf, Ncm, TipiAliquota, VersaoTabela

from . import ferramentas as F


def chamar(ferramenta, **argumentos) -> str:
    return async_to_sync(ferramenta.ainvoke)(argumentos)


def carimbar(tabela: str) -> None:
    """Sem VersaoTabela a tabela é considerada não carregada, mesmo com linhas."""
    from django.utils import timezone

    VersaoTabela.objects.create(
        tabela=tabela, referencia=f"fonte de teste de {tabela}", capturado_em=timezone.now()
    )


class TabelaVaziaNaoAcusa(TestCase):
    """
    Sem tabela, toda ferramenta responde "não sei" — nunca "não existe".

    A diferença entre `NAO_VERIFICADO` e `NAO_CONSTA` é a diferença entre o
    agente dizer "não consegui conferir" e o agente dizer "esse código é
    inválido". A segunda, dita sem base, é o erro mais caro que este produto
    comete.
    """

    def test_todas_as_consultas_de_tabela(self):
        casos = [
            (F.consultar_ncm, {"codigo": "84713012"}),
            (F.consultar_ipi, {"ncm": "84713012"}),
            (F.consultar_cest, {"ncm": "84713012"}),
            (F.consultar_cfop, {"codigo": "5102"}),
            (F.consultar_fcp, {"uf": "RJ"}),
        ]
        for ferramenta, argumentos in casos:
            with self.subTest(ferramenta=ferramenta.name):
                saida = chamar(ferramenta, **argumentos)
                self.assertTrue(
                    saida.startswith("NAO_VERIFICADO"),
                    f"{ferramenta.name} devolveu {saida[:60]!r} com a tabela vazia",
                )
                self.assertNotIn("NAO_CONSTA", saida)

    def test_linhas_sem_versao_ainda_contam_como_nao_carregada(self):
        # Carga pela metade (linhas gravadas, versão não) é indistinguível de
        # carga corrompida. Na dúvida, "não sei".
        Cfop.objects.create(codigo="5102")
        self.assertTrue(chamar(F.consultar_cfop, codigo="5102").startswith("NAO_VERIFICADO"))


class ConsultasComTabelaCarregada(TestCase):
    @classmethod
    def setUpTestData(cls):
        for tabela in ("ncm", "tipi", "cest", "cfop", "fcp"):
            carimbar(tabela)

        Ncm.objects.create(codigo="847130", descricao="Portáteis", descricao_hierarquica="… > Portáteis")
        Ncm.objects.create(codigo="84713012", descricao="De peso inferior a 3,5 kg")
        TipiAliquota.objects.create(ncm="84713012", ex=0, aliquota="15.00")
        TipiAliquota.objects.create(ncm="01012100", ex=0, nao_tributado=True)
        Cest.objects.create(codigo="21.028.00", ncm_prefixo="847130", anexo="T19", descricao="Portáteis")
        Cest.objects.create(codigo="28.061.00", ncm_prefixo="84", anexo="T25", descricao="Artigos de casa")
        Cfop.objects.create(codigo="5102")
        FcpUf.objects.create(uf="RJ", nome_uf="RIO DE JANEIRO", tipo=FcpUf.Tipo.MAXIMO, aliquota="4.00")
        FcpUf.objects.create(uf="MG", nome_uf="MINAS GERAIS", tipo=FcpUf.Tipo.FIXO, aliquota="2.00")

    def test_ncm_inexistente_aponta_o_agrupador_que_existe(self):
        saida = chamar(F.consultar_ncm, codigo="8471.30.99")
        self.assertTrue(saida.startswith("NAO_CONSTA"))
        self.assertIn("847130", saida)

    def test_nt_nao_e_zero(self):
        """NT é fora do campo de incidência. Tratar como 0% faz cobrar de quem não deve."""
        saida = chamar(F.consultar_ipi, ncm="01012100")
        self.assertIn("NT", saida)
        self.assertIn("não é 0%", saida)

    def test_ex_inexistente_e_avisado_sem_esconder_a_linha_base(self):
        saida = chamar(F.consultar_ipi, ncm="84713012", ex=42)
        self.assertIn("NÃO existe", saida)
        self.assertIn("15%", saida)

    def test_cest_por_capitulo_nao_se_mistura_com_casamento_especifico(self):
        """
        Um casamento de 2 dígitos vem de célula "Capítulos 39, 40, …, 84": é o
        capítulo inteiro, não a mercadoria. Listado junto de um casamento de 6
        dígitos, faz dois candidatos desiguais parecerem equivalentes — e sugere
        ST onde só houve coincidência de capítulo.
        """
        saida = chamar(F.consultar_cest, ncm="84713012")
        especifico, _, amplo = saida.partition("CAPÍTULO")
        self.assertIn("21.028.00", especifico)
        self.assertNotIn("28.061.00", especifico)
        self.assertIn("28.061.00", amplo)
        self.assertIn("NÃO identificam a mercadoria", amplo)

    def test_cfop_valido_nao_ganha_descricao_inventada(self):
        """A tabela oficial não traz o texto do CFOP — e o modelo tende a completar."""
        saida = chamar(F.consultar_cfop, codigo="5102")
        self.assertTrue(saida.startswith("ENCONTRADO"))
        self.assertIn("NÃO descreva", saida)

    def test_fcp_distingue_teto_de_percentual_fixo(self):
        self.assertIn("TETO", chamar(F.consultar_fcp, uf="rj"))
        self.assertIn("FIXO", chamar(F.consultar_fcp, uf="MG"))

    def test_aliquota_interestadual_cobre_as_tres_regras(self):
        casos = [
            ({"uf_origem": "SP", "uf_destino": "PR", "origem_mercadoria": "0"}, "12%"),
            ({"uf_origem": "SP", "uf_destino": "BA", "origem_mercadoria": "0"}, "7%"),
            ({"uf_origem": "SP", "uf_destino": "BA", "origem_mercadoria": "1"}, "4%"),
        ]
        for argumentos, esperado in casos:
            with self.subTest(**argumentos):
                self.assertIn(f"**{esperado}**", chamar(F.aliquota_icms_interestadual, **argumentos))

    def test_operacao_interna_nao_inventa_aliquota(self):
        saida = chamar(F.aliquota_icms_interestadual, uf_origem="SP", uf_destino="SP")
        self.assertIn("NAO_VERIFICADO", saida)


# --------------------------------------------------------------------------- #
#  O ciclo
# --------------------------------------------------------------------------- #
PLACAR: list[int] = []


class ModeloTeimoso(BaseChatModel):
    """Pede consulta enquanto houver ferramenta ligada. Nunca desiste sozinho."""

    tem_ferramentas: bool = False

    @property
    def _llm_type(self) -> str:
        return "teimoso"

    def bind_tools(self, ferramentas, **kwargs):
        return type(self)(tem_ferramentas=True)

    def _generate(self, messages, stop=None, run_manager=None, **kwargs):
        raise NotImplementedError("dublê só de streaming")

    async def _astream(self, messages, stop=None, run_manager=None, **kwargs):
        PLACAR.append(1)
        if not self.tem_ferramentas:
            yield ChatGenerationChunk(message=AIMessageChunk(content="Resposta final."))
            return
        # Argumentos fatiados: é assim que o provedor manda (input_json_delta),
        # e só a soma dos chunks remonta a chamada.
        yield ChatGenerationChunk(
            message=AIMessageChunk(
                content="",
                tool_call_chunks=[
                    tool_call_chunk(name="consultar_cfop", args='{"codi', id="c1", index=0)
                ],
            )
        )
        yield ChatGenerationChunk(
            message=AIMessageChunk(
                content="",
                tool_call_chunks=[tool_call_chunk(name=None, args='go": "5102"}', id=None, index=0)],
            )
        )


class CicloDeFerramentas(TestCase):
    def setUp(self):
        from . import graph

        self.graph = graph
        PLACAR.clear()
        self._provedor_original = graph._obter_provedor
        self._chat_original = graph.construir_chat
        self._compilado = graph._grafo_compilado

        class ProvedorFalso:
            nome, provedor, modelo = "falso", "anthropic", "teste"

        async def _obter(_id):
            return ProvedorFalso()

        graph._obter_provedor = _obter
        graph._grafo_compilado = None

    def tearDown(self):
        self.graph._obter_provedor = self._provedor_original
        self.graph.construir_chat = self._chat_original
        self.graph._grafo_compilado = self._compilado

    def _rodar(self, modelo):
        self.graph.construir_chat = lambda provedor, streaming=True: modelo
        self.graph._grafo_compilado = None
        return async_to_sync(self.graph.construir_grafo().ainvoke)(
            {"pergunta": "teste", "conversa_id": "x"}
        )

    @override_settings(AGENTE={"MAX_PASSOS_FERRAMENTA": 2, "FERRAMENTAS": True, "TOP_K_CONTEXTO": 6})
    def test_para_no_teto_e_ainda_assim_responde(self):
        final = self._rodar(ModeloTeimoso())

        self.assertEqual(final["passos_ferramenta"], 2)
        # 2 rodadas com ferramenta + 1 passada final sem: é a passada sem
        # ferramenta que garante uma resposta em vez de um turno vazio.
        self.assertEqual(len(PLACAR), 3)
        self.assertTrue(final["resposta"].endswith("Resposta final."))

    @override_settings(AGENTE={"MAX_PASSOS_FERRAMENTA": 1, "FERRAMENTAS": True, "TOP_K_CONTEXTO": 6})
    def test_toda_chamada_recebe_uma_resposta(self):
        """Chamada sem ToolMessage correspondente faz o provedor rejeitar a rodada."""
        final = self._rodar(ModeloTeimoso())

        pedidos = [
            c["id"]
            for m in final["mensagens"]
            for c in (getattr(m, "tool_calls", None) or [])
        ]
        respondidos = [
            m.tool_call_id for m in final["mensagens"] if isinstance(m, ToolMessage)
        ]
        self.assertEqual(sorted(pedidos), sorted(respondidos))

    @override_settings(AGENTE={"FERRAMENTAS": False, "TOP_K_CONTEXTO": 6})
    def test_desligado_volta_ao_fluxo_de_uma_passada(self):
        final = self._rodar(ModeloTeimoso())

        self.assertEqual(len(PLACAR), 1)
        self.assertEqual(final["resposta"], "Resposta final.")

    @override_settings(AGENTE={"MAX_PASSOS_FERRAMENTA": 2, "FERRAMENTAS": True, "TOP_K_CONTEXTO": 6})
    def test_provedor_sem_tool_calling_degrada_em_vez_de_derrubar(self):
        class SemBind(ModeloTeimoso):
            def bind_tools(self, ferramentas, **kwargs):
                raise NotImplementedError("provedor sem tool calling")

        final = self._rodar(SemBind())

        self.assertEqual(final["resposta"], "Resposta final.")
        self.assertFalse(final.get("erro"))

    @override_settings(AGENTE={"MAX_PASSOS_FERRAMENTA": 1, "FERRAMENTAS": True, "TOP_K_CONTEXTO": 6})
    def test_ferramenta_que_estoura_vira_nao_verificado(self):
        def explodir(*_a, **_k):
            raise RuntimeError("banco fora do ar")

        original = F.POR_NOME["consultar_cfop"].coroutine
        F.POR_NOME["consultar_cfop"].coroutine = explodir
        try:
            final = self._rodar(ModeloTeimoso())
        finally:
            F.POR_NOME["consultar_cfop"].coroutine = original

        resultado = next(m for m in final["mensagens"] if isinstance(m, ToolMessage))
        self.assertIn("NAO_VERIFICADO", resultado.content)
        self.assertTrue(final["resposta"].endswith("Resposta final."))


# --------------------------------------------------------------------------- #
#  Resposta interrompida e carimbo de versão
# --------------------------------------------------------------------------- #
class ModeloQueRecusaParametro(BaseChatModel):
    """Devolve HTTP 400 citando o parametro, como o Azure faz numa api-version antiga."""

    recusa: bool = False
    erro: str = "Error code: 400 - Unrecognized request argument supplied: reasoning_effort"

    @property
    def _llm_type(self) -> str:
        return "recusa-parametro"

    def bind_tools(self, ferramentas, **kwargs):
        return self

    def _generate(self, messages, stop=None, run_manager=None, **kwargs):
        raise NotImplementedError("duble so de streaming")

    async def _astream(self, messages, stop=None, run_manager=None, **kwargs):
        PLACAR.append(1)
        if self.recusa:
            raise RuntimeError(self.erro)
        yield ChatGenerationChunk(message=AIMessageChunk(content="Resposta sem o parametro."))


class RecuoDeParametroRecusado(TestCase):
    """
    O catalogo manda `reasoning_effort` para o gpt-5.5 do Foundry sem saber se a
    api-version aceita. Se nao aceitar, o consultor nao pode ver erro: o agente
    tira o parametro e responde. E o que torna seguro publicar a aposta.
    """

    def setUp(self):
        from apps.provedores import factory

        from . import graph

        self.graph, self.factory = graph, factory
        PLACAR.clear()
        factory._EXTRAS_RECUSADOS.clear()
        self._provedor_original = graph._obter_provedor
        self._chat_original = graph.construir_chat

        class ProvedorFalso:
            nome, provedor, modelo = "Foundry", "azure", "gpt-5.5"

        async def _obter(_id):
            return ProvedorFalso()

        graph._obter_provedor = _obter

    def tearDown(self):
        self.graph._obter_provedor = self._provedor_original
        self.graph.construir_chat = self._chat_original
        self.factory._EXTRAS_RECUSADOS.clear()

    def _responder(self, erro=None):
        def construir(provedor, streaming=True):
            extras = self.factory.extras_do_catalogo(provedor)
            argumentos = {"recusa": bool(extras) or erro is not None}
            if erro is not None:
                argumentos["erro"] = erro
            return ModeloQueRecusaParametro(**argumentos)

        self.graph.construir_chat = construir
        return async_to_sync(self.graph.no_responder)({"mensagens": [HumanMessage(content="x")]})

    def test_recusa_vira_resposta_e_nao_erro(self):
        final = self._responder()

        self.assertEqual(final["erro"], "")
        self.assertEqual(final["resposta"], "Resposta sem o parametro.")
        self.assertEqual(len(PLACAR), 2)  # a recusada + a que valeu

    def test_a_recusa_e_lembrada_e_a_proxima_pergunta_nao_paga_de_novo(self):
        self._responder()
        PLACAR.clear()

        final = self._responder()

        self.assertEqual(final["resposta"], "Resposta sem o parametro.")
        self.assertEqual(len(PLACAR), 1)

    def test_erro_sem_relacao_aparece_e_nao_e_repetido(self):
        final = self._responder(erro="Error code: 429 - Too Many Requests")

        self.assertIn("Foundry", final["erro"])
        self.assertEqual(len(PLACAR), 1)


class HistoricoDeRespostaInterrompida(TestCase):
    """
    Uma resposta que morreu no meio do streaming volta ao modelo no turno
    seguinte. Sem marcação, ela volta como fala completa e correta dele mesmo —
    o consultor vê o aviso de erro na tela, o modelo não via nada.
    """

    def _conversa_com(self, conteudo: str, erro: str):
        from apps.agente.models import Conversa, Mensagem

        conversa = Conversa.objects.create(titulo="t")
        Mensagem.objects.create(
            conversa=conversa, papel=Mensagem.Papel.USUARIO, conteudo="e o CFOP?"
        )
        Mensagem.objects.create(
            conversa=conversa, papel=Mensagem.Papel.AGENTE, conteudo=conteudo, erro=erro
        )
        return list(conversa.mensagens.order_by("criado_em", "id"))

    def test_resposta_cortada_volta_marcada(self):
        from apps.agente.graph import historico_para_mensagens

        msgs = historico_para_mensagens(
            self._conversa_com("| # | Ajuste | Onde no Sen", "Timeout")
        )

        self.assertEqual(len(msgs), 2)
        self.assertIn("INTERROMPIDA", msgs[-1].content)
        # O texto parcial CONTINUA lá: o consultor viu aquilo na tela, e some-lo
        # deixaria modelo e consultor conversando sobre coisas diferentes.
        self.assertIn("| # | Ajuste | Onde no Sen", msgs[-1].content)

    def test_resposta_boa_nao_ganha_marcador(self):
        from apps.agente.graph import historico_para_mensagens

        msgs = historico_para_mensagens(self._conversa_com("Resposta inteira.", ""))

        self.assertEqual(msgs[-1].content, "Resposta inteira.")

    def test_falha_sem_texto_nenhum_nao_entra(self):
        from apps.agente.graph import historico_para_mensagens

        msgs = historico_para_mensagens(self._conversa_com("", "Provedor indisponível"))

        self.assertEqual(len(msgs), 1)  # só a pergunta do consultor


class CarimboDeVersao(TestCase):
    """
    O carimbo é gravado na CRIAÇÃO da mensagem. Recalcular no voto daria a
    versão de hoje, não a que gerou a resposta votada.
    """

    def test_a_resposta_nasce_carimbada(self):
        from apps.agente.models import Conversa
        from apps.agente.services import salvar_resposta
        from apps.agente.versao import hash_prompt

        conversa = Conversa.objects.create(titulo="t")
        resposta = salvar_resposta(conversa_id=conversa.pk, conteudo="oi")

        self.assertEqual(resposta.metadados["versao_prompt"], hash_prompt())
        self.assertEqual(len(resposta.metadados["versao_prompt"]), 12)

    def test_mudar_o_prompt_muda_a_versao(self):
        from apps.agente import prompts
        from apps.agente.versao import _cache, hash_prompt

        antes = hash_prompt()
        original = prompts.SISTEMA
        prompts.SISTEMA = original + "\numa regra nova"
        _cache.clear()
        try:
            depois = hash_prompt()
        finally:
            prompts.SISTEMA = original
            _cache.clear()

        self.assertNotEqual(antes, depois)

    def test_mudar_a_descricao_de_uma_ferramenta_muda_a_versao(self):
        """
        As docstrings das ferramentas SÃO prompt: o modelo lê e decide com base
        nelas. Um hash só do SISTEMA diria "mesma versão" depois disto.
        """
        from apps.agente.ferramentas import POR_NOME
        from apps.agente.versao import _cache, hash_prompt

        antes = hash_prompt()
        ferramenta = POR_NOME["consultar_cfop"]
        original = ferramenta.description
        ferramenta.description = original + " Agora também confere o CEST."
        _cache.clear()
        try:
            depois = hash_prompt()
        finally:
            ferramenta.description = original
            _cache.clear()

        self.assertNotEqual(antes, depois)

    @override_settings(
        AGENTE={"FERRAMENTAS": True, "TOP_K_CONTEXTO": 6, "MAX_PASSOS_FERRAMENTA": 3}
    )
    def test_parametro_de_runtime_conta_como_versao(self):
        """O mesmo código com outro teto de trechos responde diferente."""
        from apps.agente.versao import hash_prompt

        com_6 = hash_prompt()
        with override_settings(
            AGENTE={"FERRAMENTAS": True, "TOP_K_CONTEXTO": 18, "MAX_PASSOS_FERRAMENTA": 3}
        ):
            com_18 = hash_prompt()

        self.assertNotEqual(com_6, com_18)

    def test_o_voto_copia_o_carimbo_da_mensagem_em_vez_de_recalcular(self):
        from apps.agente.models import Conversa, Mensagem
        from apps.agente.views import _montar_contexto

        conversa = Conversa.objects.create(titulo="t")
        Mensagem.objects.create(
            conversa=conversa, papel=Mensagem.Papel.USUARIO, conteudo="pergunta"
        )
        resposta = Mensagem.objects.create(
            conversa=conversa,
            papel=Mensagem.Papel.AGENTE,
            conteudo="resposta",
            metadados={"versao_prompt": "abc123def456", "git_sha": "0" * 40},
        )

        contexto = _montar_contexto(resposta)

        # A versão ANTIGA, não a de agora — é o ponto inteiro do campo.
        self.assertEqual(contexto["versao_prompt"], "abc123def456")
        self.assertEqual(contexto["git_sha"], "0" * 40)

    def test_sem_GIT_SHA_no_ambiente_o_carimbo_sai_so_com_o_hash(self):
        import os

        from apps.agente.versao import ENV_GIT_SHA, carimbo

        antes = os.environ.pop(ENV_GIT_SHA, None)
        try:
            self.assertEqual(set(carimbo()), {"versao_prompt"})
        finally:
            if antes is not None:
                os.environ[ENV_GIT_SHA] = antes


class RecuperacaoSensivelAoTurno(TestCase):
    """
    Pergunta digitada não deve refazer a busca das 8 divergências: elas custam
    ~5.200 tokens e respondem a outra coisa. O relatório continua no prompt.
    """

    ESTADO = {
        "causas": [
            {"grupo": "ICMS", "campo": "CST", "tipo": "valor_diferente"},
            {"grupo": "IPI", "campo": "pIPI", "tipo": "valor_diferente"},
        ],
        "campos_divergentes": ["ICMS.CST", "IPI.pIPI"],
    }

    def test_mensagem_de_botao_busca_as_causas(self):
        from apps.agente.graph import _analise_do_lote

        self.assertTrue(
            _analise_do_lote({**self.ESTADO, "rotulo": "Analise as divergências"})
        )

    def test_pergunta_digitada_nao_busca_as_causas(self):
        from apps.agente.graph import _analise_do_lote

        self.assertFalse(_analise_do_lote({**self.ESTADO, "rotulo": ""}))

    def test_o_sinal_e_o_rotulo_e_nao_a_existencia_de_historico(self):
        """
        O consultor pode apertar o botão no décimo turno — e aí as causas DEVEM
        mandar. E pode digitar uma pergunta na primeira mensagem.
        """
        from apps.agente.graph import _analise_do_lote

        botao_tarde = {**self.ESTADO, "rotulo": "Analise as divergências", "historico": [1, 2]}
        digitada_cedo = {**self.ESTADO, "rotulo": "", "historico": []}

        self.assertTrue(_analise_do_lote(botao_tarde))
        self.assertFalse(_analise_do_lote(digitada_cedo))

    def test_pergunta_digitada_leva_o_orcamento_inteiro(self):
        """A pergunta sai de 1 trecho (cota) para o teto próprio dela."""
        from asgiref.sync import async_to_sync

        from apps.agente.graph import no_recuperar

        chamadas = {}

        async def espiar(consultas, pergunta, campos, teto):
            chamadas.update(consultas=consultas, pergunta=pergunta, teto=teto)
            return {"contexto": [], "regras": []}

        from apps.agente import graph as g

        original = g._buscar_conhecimento
        g._buscar_conhecimento = espiar
        try:
            async_to_sync(no_recuperar)(
                {**self.ESTADO, "rotulo": "", "pergunta": "e o IPI na devolução?"}
            )
        finally:
            g._buscar_conhecimento = original

        # Nenhuma consulta de causa: só a pergunta, e sem cota (limites só
        # existe quando há causas, ver _buscar_conhecimento).
        self.assertEqual(chamadas["consultas"], [])
        self.assertEqual(chamadas["pergunta"], "e o IPI na devolução?")

    def test_botao_continua_buscando_todas_as_causas(self):
        from asgiref.sync import async_to_sync

        from apps.agente import graph as g
        from apps.agente.graph import no_recuperar

        chamadas = {}

        async def espiar(consultas, pergunta, campos, teto):
            chamadas.update(consultas=consultas, teto=teto)
            return {"contexto": [], "regras": []}

        original = g._buscar_conhecimento
        g._buscar_conhecimento = espiar
        try:
            async_to_sync(no_recuperar)(
                {**self.ESTADO, "rotulo": "Analise as divergências", "pergunta": "Analise…"}
            )
        finally:
            g._buscar_conhecimento = original

        self.assertEqual(len(chamadas["consultas"]), 2)  # uma por causa
