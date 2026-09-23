"""
Testes do retriever — em especial o guard temporário da busca semântica.

Rode com:  DB_ENGINE=sqlite python manage.py test apps.conhecimento
"""
from django.conf import settings
from django.db import connection
from django.test import TestCase, override_settings
from unittest import skipUnless

#: `<=>` e `vector_dims` só existem no PostgreSQL. Fora dele estes testes não
#: podem simplesmente "passar": o de dimensão divergente recebia [] por erro de
#: sintaxe, não por filtro — falso verde guardando justamente o cenário de troca
#: de modelo de embeddings.
so_postgres = skipUnless(
    connection.vendor == "postgresql", "a perna semântica exige pgvector"
)

from apps.conhecimento.models import Documento, FonteConhecimento, Trecho
from apps.conhecimento.services import retriever


def _agente(**sobrescreve):
    return {**settings.AGENTE, **sobrescreve}


class RetrieverGuardSemanticaTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        fonte = FonteConhecimento.objects.create(nome="Senior Docs")
        doc = Documento.objects.create(
            fonte=fonte, titulo="Parametrização de ICMS", url="https://exemplo/icms"
        )
        cls.com_vetor = Trecho.objects.create(
            documento=doc,
            ordem=1,
            titulo_secao="Alíquota interna",
            texto="Como parametrizar a alíquota de ICMS na rotina de tributação.",
            embedding=[0.1, 0.2, 0.3],
        )
        cls.sem_vetor = Trecho.objects.create(
            documento=doc,
            ordem=2,
            titulo_secao="CFOP",
            texto="Validação de CFOP na natureza de operação.",
            embedding=None,  # sem vetor agora é NULL, não lista vazia
        )

    def setUp(self):
        # O índice é cacheado por (count, max id) — a flag NÃO entra na versão,
        # então cada cenário precisa começar sem cache.
        retriever.invalidar_indice()

    def test_o_indice_nunca_guarda_vetor(self):
        """
        O ponto do pgvector: o processo não carrega vetor nenhum, com a flag
        ligada ou desligada. Era a matriz em RAM que custava ~51 MB por worker
        e derrubou o plano compartilhado em 31/07/2026.
        """
        for ligada in (False, True):
            with self.subTest(semantica=ligada):
                with override_settings(AGENTE=_agente(BUSCA_SEMANTICA=ligada)):
                    retriever.invalidar_indice()
                    indice = retriever.obter_indice()

                    self.assertFalse(hasattr(indice, "matriz"))
                    self.assertFalse(hasattr(indice, "posicoes_com_vetor"))
        retriever.invalidar_indice()

    def test_tem_embedding_continua_fiel_sem_selecionar_a_coluna(self):
        """A UI mostra quantos trechos têm vetor; trazer a coluna custaria 12 KB cada."""
        indice = retriever.obter_indice()
        por_id = {t.id: t for t in indice.trechos}

        self.assertTrue(por_id[self.com_vetor.id].tem_embedding)
        self.assertFalse(por_id[self.sem_vetor.id].tem_embedding)

    def test_flag_desligada_busca_textual_funciona(self):
        resultados = retriever.buscar_contexto("parametrizar ICMS alíquota")

        self.assertTrue(resultados)
        self.assertEqual(resultados[0].trecho_id, self.com_vetor.id)
        # No Postgres o FTS também entra na fusão; o que NÃO pode haver é semântica.
        self.assertIn(resultados[0].origem_ranking, ("textual", "fts", "hibrido"))

    def test_flag_desligada_nao_chama_provedor_de_embeddings(self):
        self.assertIsNone(retriever._vetores_das_consultas(["qualquer consulta"]))

    @so_postgres
    def test_ranking_semantico_consulta_o_banco_e_devolve_posicoes(self):
        """
        O banco responde com id; o resto do pipeline trabalha por posição no
        índice textual. `posicao_por_id` é a ponte, e um id que saiu da base
        entre a montagem e a consulta precisa ser ignorado, não quebrar.
        """
        indice = retriever.obter_indice()

        posicoes = retriever._ranking_semantico_do_vetor([0.1, 0.2, 0.3], indice, 5)

        self.assertEqual(len(posicoes), 1)  # só um trecho tem vetor
        posicao, similaridade = posicoes[0]
        self.assertEqual(indice.trechos[posicao].id, self.com_vetor.id)
        self.assertAlmostEqual(similaridade, 1.0, places=4)  # vetor idêntico

    @so_postgres
    def test_vetor_de_outra_dimensao_e_ignorado_sem_quebrar(self):
        """
        Troca de modelo de embeddings no meio da base. Sem o filtro por
        vector_dims o Postgres levanta erro; com ele, a perna semântica
        simplesmente não contribui e a busca segue textual.
        """
        indice = retriever.obter_indice()

        self.assertEqual(
            retriever._ranking_semantico_do_vetor([0.1] * 1536, indice, 5), []
        )

    @so_postgres
    def test_vetor_numpy_e_serializado_em_formato_que_o_pgvector_aceita(self):
        """
        Regressão do NumPy 2: `str(list(array))` virou
        "[np.float32(0.1), …]", que o pgvector recusa — e a falha era
        silenciosa, só um warning e busca semântica vazia.
        """
        import numpy as np

        indice = retriever.obter_indice()
        vetor = np.array([0.1, 0.2, 0.3], dtype="float32")

        posicoes = retriever._ranking_semantico_do_vetor(vetor, indice, 5)

        self.assertEqual(len(posicoes), 1)


    def test_fora_do_postgres_a_perna_semantica_apenas_nao_contribui(self):
        """
        No SQLite o ranking semântico devolve vazio por GUARD, não por erro —
        a busca cai para as pernas lexicais e continua respondendo.
        """
        indice = retriever.obter_indice()

        with self.assertNoLogs("apps.conhecimento.services.retriever", level="WARNING"):
            posicoes = retriever._ranking_semantico_do_vetor([0.1, 0.2, 0.3], indice, 5)

        if connection.vendor != "postgresql":
            self.assertEqual(posicoes, [])
        else:
            self.assertEqual(len(posicoes), 1)


class RankingTextualTests(TestCase):
    """Boost de títulos e expansão por sinônimos no BM25."""

    @classmethod
    def setUpTestData(cls):
        fonte = FonteConhecimento.objects.create(nome="Senior Docs")
        doc_rotinas = Documento.objects.create(
            fonte=fonte,
            titulo="Rotinas de ICMS",
            url="https://exemplo/rotinas-icms",
            hash_conteudo="hash-rotinas",
        )
        doc_outro = Documento.objects.create(
            fonte=fonte,
            titulo="Cadastro de Produtos",
            url="https://exemplo/produtos",
            hash_conteudo="hash-produtos",
        )
        # O corpo NÃO repete o título: só acha via índice de títulos.
        cls.pelo_titulo = Trecho.objects.create(
            documento=doc_rotinas,
            ordem=1,
            titulo_secao="Visão geral",
            texto="Esta página descreve a parametrização de impostos estaduais.",
        )
        cls.pela_sigla = Trecho.objects.create(
            documento=doc_outro,
            ordem=1,
            titulo_secao="Impostos do item",
            texto="Como configurar a substituição tributária no cadastro do produto.",
        )

    def setUp(self):
        retriever.invalidar_indice()

    def test_titulo_do_documento_e_indexado(self):
        resultados = retriever.buscar_contexto("rotinas de ICMS")
        self.assertTrue(resultados)
        self.assertEqual(resultados[0].trecho_id, self.pelo_titulo.id)

    def test_sigla_encontra_texto_por_extenso(self):
        # "ST" não aparece em nenhum texto; só o sinônimo casa.
        resultados = retriever.buscar_contexto("parametrizar ST do produto")
        self.assertIn(self.pela_sigla.id, [r.trecho_id for r in resultados])

    def test_termo_digitado_pesa_mais_que_sinonimo(self):
        # Quem escreve "substituição tributária" por extenso deve ranquear o
        # trecho literal acima de qualquer casamento via expansão.
        resultados = retriever.buscar_contexto("substituição tributária")
        self.assertTrue(resultados)
        self.assertEqual(resultados[0].trecho_id, self.pela_sigla.id)


class SinonimosTests(TestCase):
    def test_toda_entrada_vira_exatamente_um_token(self):
        """Entrada multi-palavra ou stopword no dicionário nunca casaria — falha aqui."""
        from apps.conhecimento.services.sinonimos import _SINONIMOS
        from apps.conhecimento.services.texto import tokenizar_superficie

        for chave, expansoes in _SINONIMOS.items():
            for termo in (chave, *expansoes):
                self.assertEqual(
                    len(tokenizar_superficie(termo)),
                    1,
                    f"entrada {termo!r} não tokeniza para exatamente 1 termo",
                )

    def test_canonizacao_liga_sigla_ao_stem_do_extenso(self):
        from apps.conhecimento.services.sinonimos import SINONIMOS_CANONICOS

        (chave_st,) = retriever.tokenizar("ST")
        extenso = set(retriever.tokenizar("substituição tributária"))
        self.assertTrue(extenso.intersection(SINONIMOS_CANONICOS[chave_st]))


class TextoTests(TestCase):
    """Stemming com reparo de sufixo: acentuado e sem acento caem no mesmo stem."""

    def test_unifica_derivacoes_do_vocabulario_fiscal(self):
        pares = [
            ("parametrização", "parametrizar"),
            ("tributação", "tributária"),
            ("operações", "operacao"),
            ("alíquota", "aliquotas"),
            ("substituição", "substituicao"),
        ]
        for a, b in pares:
            self.assertEqual(
                retriever.tokenizar(a), retriever.tokenizar(b), f"{a!r} ≠ {b!r}"
            )

    def test_siglas_passam_intactas(self):
        for sigla in ("difal", "icms", "st", "cfop", "ncm"):
            self.assertEqual(retriever.tokenizar(sigla), [sigla])

    def test_stopwords_continuam_fora(self):
        self.assertEqual(retriever.tokenizar("como está a nota?"), retriever.tokenizar("nota"))


class FtsTests(TestCase):
    """FTS nativo — só roda no Postgres (a migração 0004 não cria nada no SQLite)."""

    @classmethod
    def setUpTestData(cls):
        fonte = FonteConhecimento.objects.create(nome="Senior Docs")
        doc = Documento.objects.create(
            fonte=fonte, titulo="Impostos", url="https://exemplo/impostos", hash_conteudo="h1"
        )
        cls.no_titulo = Trecho.objects.create(
            documento=doc,
            ordem=1,
            titulo_secao="Retenção de tributos federais",
            texto="Configuração aplicável às notas de serviço.",
        )
        cls.no_corpo = Trecho.objects.create(
            documento=doc,
            ordem=2,
            titulo_secao="Outros",
            texto="A retenção de tributos federais é definida por transação.",
        )

    def setUp(self):
        retriever.invalidar_indice()

    def _postgres(self) -> bool:
        from django.db import connection

        return connection.vendor == "postgresql"

    def test_ranking_fts_prioriza_titulo_e_stemiza(self):
        if not self._postgres():
            self.skipTest("FTS só existe no Postgres")
        from apps.conhecimento.services.fts import ranking_fts

        indice = retriever.obter_indice()
        # "retencoes tributarias" sem acento e flexionado: só o stemming casa.
        resultado = ranking_fts("retencoes tributarias federais", indice.posicao_por_id, 10)
        self.assertTrue(resultado)
        ids = [indice.trechos[pos].id for pos, _s in resultado]
        self.assertIn(self.no_titulo.id, ids)
        # peso A do título deve vencer o corpo
        self.assertEqual(ids[0], self.no_titulo.id)

    def test_fusao_marca_origem_hibrida(self):
        if not self._postgres():
            self.skipTest("FTS só existe no Postgres")
        resultados = retriever.buscar_contexto("retenção de tributos federais")
        self.assertTrue(resultados)
        self.assertEqual(resultados[0].origem_ranking, "hibrido")
