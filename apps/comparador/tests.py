"""
Pareamento automático das notas — o que decide se o consultor vai ter que
vincular na mão.

O foco aqui é o caso que motivou o EAN entrar no escore: numa migração o
**código interno do produto quase sempre muda** entre o sistema atual e o
Senior, porque o cadastro é recriado. O EAN/GTIN não muda — é do fabricante.
Sem ele, notas idênticas ficavam sem par por falta de sinal de produto.
"""
from __future__ import annotations

from decimal import Decimal

from django.test import SimpleTestCase

from apps.comparador.services.pareador import (
    LIMIAR_ALTA,
    LIMIAR_PADRAO,
    Assinatura,
    _ean_utilizavel,
    pontuar,
)


def assinatura(codigos=(), eans=(), **campos) -> Assinatura:
    base = dict(
        nome_arquivo="nota.xml",
        destinatario_doc="12345678000199",
        valor_total=Decimal("1000.00"),
        quantidade_itens=2,
        data="2026-06-29",
    )
    base.update(campos)
    return Assinatura(codigos_produto=set(codigos), eans=set(eans), **base)


class GtinUtilizavel(SimpleTestCase):
    """
    ``SEM GTIN`` é literal permitido pelo XSD da NF-e e MUITO comum. Aceitá-lo
    faria todo produto sem código de barras compartilhar o mesmo "EAN", e
    qualquer nota casaria com qualquer outra pelo produto.
    """

    def test_aceita_os_comprimentos_de_gtin(self):
        for valor in ("12345678", "123456789012", "7891234567895", "17891234567892"):
            with self.subTest(valor=valor):
                self.assertEqual(_ean_utilizavel(valor), valor)

    def test_limpa_pontuacao(self):
        self.assertEqual(_ean_utilizavel("789.1234.56789-5"), "7891234567895")

    def test_recusa_o_que_nao_identifica_produto(self):
        for valor in ("SEM GTIN", "", "   ", "123", "0000000000000", "abc"):
            with self.subTest(valor=valor):
                self.assertEqual(_ean_utilizavel(valor), "")


class ProdutoNoEscore(SimpleTestCase):
    def test_codigo_interno_diferente_mas_mesmo_ean_ainda_pareia(self):
        """O caso da migração: cadastro recriado, numeração nova, mesmo produto."""
        atual = assinatura({"PROD-001", "PROD-002"}, {"7891234567895", "7899876543210"})
        senior = assinatura({"1", "2"}, {"7891234567895", "7899876543210"})

        escore, motivos = pontuar(atual, senior)

        self.assertGreaterEqual(escore, LIMIAR_ALTA)
        self.assertIn("100% dos EAN/GTIN em comum", motivos)

    def test_quem_ja_casava_por_codigo_pontua_igual(self):
        """
        Código e EAN disputam os MESMOS 25 pontos. Somar os dois inflaria o
        escore e obrigaria a recalibrar os limiares.
        """
        codigos = {"PROD-001", "PROD-002"}
        so_codigo = pontuar(assinatura(codigos), assinatura(codigos))[0]
        com_ean = pontuar(
            assinatura(codigos, {"7891234567895"}),
            assinatura(codigos, {"7891234567895"}),
        )[0]

        self.assertEqual(so_codigo, com_ean)

    def test_sem_gtin_dos_dois_lados_nao_vira_sinal_de_produto(self):
        vazio = {g for g in [_ean_utilizavel("SEM GTIN")] if g}
        a = assinatura({"A"}, vazio)
        b = assinatura({"B"}, vazio)

        _, motivos = pontuar(a, b)

        self.assertFalse([m for m in motivos if "EAN" in m or "código" in m])

    def test_codigo_interno_e_ean_nao_se_misturam(self):
        """
        Conjuntos separados de propósito: juntando tudo num só, um código
        interno "7891234567895" casaria com o EAN de outro produto.
        """
        a = assinatura({"7891234567895"}, set())
        b = assinatura(set(), {"7891234567895"})

        _, motivos = pontuar(a, b)

        self.assertFalse([m for m in motivos if "EAN" in m or "código" in m])


class DestinatarioNoEscore(SimpleTestCase):
    """A primeira pergunta do pareamento é "é o mesmo cliente?"."""

    def test_mesmo_cnpj_soma(self):
        _, motivos = pontuar(
            assinatura({"A"}, destinatario_doc="12345678000199"),
            assinatura({"A"}, destinatario_doc="12345678000199"),
        )

        self.assertIn("mesmo destinatário (CNPJ/CPF)", motivos)

    def test_cnpj_diferente_derruba_o_par(self):
        """
        Sem a penalidade, duas notas que só compartilham o produto casariam —
        e o consultor compararia a nota de um cliente contra a de outro.
        """
        escore, motivos = pontuar(
            assinatura({"A", "B"}, destinatario_doc="12345678000199"),
            assinatura({"A", "B"}, destinatario_doc="98765432000188"),
        )

        self.assertIn("destinatários diferentes", motivos)
        self.assertLess(escore, LIMIAR_PADRAO + 30)


class ItensNaoSimulados(SimpleTestCase):
    """
    Numa validação de implantação é comum simular só PARTE dos itens no Senior.
    Os que ficaram de fora viram "item não emitido na nota do Senior" com
    severidade crítica — dezenas de achados que o consultor já sabe que não são
    erro, e que afogam as divergências reais de parametrização.
    """

    def _documentos(self):
        from apps.comparador.services.parser_nfe import DocumentoFiscal, ItemNota

        def item(numero, codigo):
            return ItemNota(
                numero=numero, codigo=codigo, descricao=f"Produto {codigo}",
                ncm="72085100", cfop="5102", valor_produto="100.00",
                impostos={"ICMS": {"CST": "00", "pICMS": "18.00"}},
            )

        cliente = DocumentoFiscal(origem="cliente", numero="1", itens=[item(1, "A"), item(2, "B")])
        # O Senior só simulou o primeiro item.
        senior = DocumentoFiscal(origem="senior", numero="1", itens=[item(1, "A")])
        return cliente, senior

    def _tipos(self, **opcoes):
        from apps.comparador.services.comparador import comparar_documentos

        cliente, senior = self._documentos()
        resultado = comparar_documentos(cliente, senior, **opcoes)
        return [d.tipo for d in resultado.divergencias], resultado

    def test_por_padrao_o_item_faltante_e_apontado(self):
        tipos, _ = self._tipos()

        self.assertIn("item_ausente_no_senior", tipos)

    def test_desligado_o_item_faltante_deixa_de_ser_divergencia(self):
        tipos, _ = self._tipos(analisar_itens_nao_simulados=False)

        self.assertNotIn("item_ausente_no_senior", tipos)

    def test_o_par_continua_registrado_mesmo_desligado(self):
        """
        O item não ter contraparte não deixa de ser verdade — só deixa de ser
        tratado como problema. Some do relatório de divergências, fica no
        pareamento.
        """
        _, resultado = self._tipos(analisar_itens_nao_simulados=False)

        somente_cliente = [p for p in resultado.pareamento if p["tipo"] == "somente_cliente"]

        self.assertEqual(len(somente_cliente), 1)
        self.assertEqual(somente_cliente[0]["cliente"]["codigo"], "B")

    def test_nao_mexe_no_item_a_mais_do_senior(self):
        """
        O inverso é outro caso: item que o Senior gerou e o cliente não tem
        (frete, brinde, composição de kit) continua sendo achado — não é
        "não simulado", é o Senior inventando linha.
        """
        from apps.comparador.services.comparador import comparar_documentos
        from apps.comparador.services.parser_nfe import DocumentoFiscal, ItemNota

        extra = ItemNota(numero=2, codigo="FRETE", descricao="Frete", valor_produto="50.00")
        cliente = DocumentoFiscal(origem="cliente", numero="1", itens=[])
        senior = DocumentoFiscal(origem="senior", numero="1", itens=[extra])

        resultado = comparar_documentos(cliente, senior, analisar_itens_nao_simulados=False)

        self.assertIn("item_ausente_no_cliente", [d.tipo for d in resultado.divergencias])
