"""
Tabelas oficiais de referência fiscal — o que o agente consultor usa para
afirmar, e não para supor.

Estas tabelas vêm de fonte oficial e são consultadas por SQL, nunca pelo RAG:
"este NCM existe em 12/03/2025?" é pergunta de índice, não de busca semântica.
Um modelo de linguagem responde isso com um palpite plausível; a tabela
responde com o ato legal que criou o código.

## Por que cada tabela guarda a sua versão

Toda consulta precisa poder dizer *de quando* é o dado que usou. Sem isso o
agente afirma "a alíquota de IPI é 5%" sem que ninguém saiba se a TIPI usada é
de hoje ou de dois anos atrás — e num consultor fiscal essa diferença é a
diferença entre orientar e enganar. Ver :class:`VersaoTabela`.
"""
from __future__ import annotations

from django.db import models


class VersaoTabela(models.Model):
    """
    Carimbo de origem de cada tabela importada.

    A API do NCM só descreve o presente (todo ``Data_Fim`` vem 31/12/9999) e a
    URL da TIPI é fixa com conteúdo mutável. Sem registrar quando cada arquivo
    foi capturado, daqui a um ano ninguém consegue auditar uma nota antiga —
    e esse histórico é impossível de reconstruir depois.
    """

    tabela = models.CharField(max_length=40, unique=True)
    origem = models.URLField(max_length=500, blank=True, default="")
    #: O que a própria fonte diz sobre sua vigência ("Vigente em 12/08/2026",
    #: "Decreto 11.158/2022"). Texto livre porque cada órgão publica do seu jeito.
    referencia = models.CharField(max_length=300, blank=True, default="")
    #: SHA-256 do arquivo: é o que detecta troca de conteúdo numa URL fixa.
    hash_arquivo = models.CharField(max_length=64, blank=True, default="")
    registros = models.PositiveIntegerField(default=0)
    capturado_em = models.DateTimeField()
    importado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "versão de tabela fiscal"
        verbose_name_plural = "versões de tabelas fiscais"
        ordering = ["tabela"]

    def __str__(self) -> str:
        return f"{self.tabela} — {self.registros} registros ({self.referencia})"


class Ncm(models.Model):
    """
    Nomenclatura Comum do Mercosul, da API pública do Portal Único Siscomex.

    Guardamos todos os níveis (capítulo, posição, subposição, item, subitem) e
    não só as folhas de 8 dígitos, porque a descrição de um subitem raramente
    se sustenta sozinha: "Outros" aparece 2.027 vezes. O texto útil é a cadeia
    de ancestrais, montada em ``descricao_hierarquica``.
    """

    #: Só dígitos, sem pontuação. O comprimento define o nível: 8 é subitem
    #: (NCM completo da nota); 2, 4, 5, 6 e 7 são agrupadores.
    codigo = models.CharField(max_length=8, unique=True)
    descricao = models.TextField()
    #: Cadeia completa "Capítulo > Posição > … > este". É o que dá sentido a
    #: uma descrição como "Outros".
    descricao_hierarquica = models.TextField(blank=True, default="")

    inicio_vigencia = models.DateField(null=True, blank=True)
    #: Nulo quando vigente. A fonte usa a sentinela 31/12/9999, que traduzimos
    #: para NULL — comparar data com sentinela é fonte de erro sutil.
    fim_vigencia = models.DateField(null=True, blank=True)
    ato = models.CharField(max_length=120, blank=True, default="")

    class Meta:
        verbose_name = "NCM"
        verbose_name_plural = "NCM"
        ordering = ["codigo"]
        indexes = [models.Index(fields=["codigo"], name="ncm_codigo_idx")]

    def __str__(self) -> str:
        return f"{self.codigo} — {self.descricao[:60]}"

    @property
    def e_subitem(self) -> bool:
        """Só o código de 8 dígitos pode aparecer no campo NCM de um item."""
        return len(self.codigo) == 8

    def vigente_em(self, data) -> bool:
        if self.inicio_vigencia and data < self.inicio_vigencia:
            return False
        if self.fim_vigencia and data > self.fim_vigencia:
            return False
        return True


class TipiAliquota(models.Model):
    """
    Alíquota de IPI por NCM — a única tabela oficial "código → alíquota" que
    existe no Brasil.
    """

    ncm = models.CharField(max_length=8, db_index=True)
    #: Ex-tarifário. Zero é a linha base (sem Ex) — e não NULL de propósito:
    #: no Postgres, UNIQUE com NULL não impede duplicata, porque NULL ≠ NULL.
    ex = models.PositiveSmallIntegerField(default=0)
    descricao = models.TextField(blank=True, default="")

    #: Percentual. Nulo quando "NT" ou quando a fonte não trouxe valor.
    aliquota = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    #: "NT" na TIPI significa **fora do campo de incidência** — não é zero.
    #: Tratar como 0% faria o agente cobrar IPI de quem não deve.
    nao_tributado = models.BooleanField(default=False)

    class Meta:
        verbose_name = "alíquota da TIPI"
        verbose_name_plural = "alíquotas da TIPI"
        ordering = ["ncm", "ex"]
        constraints = [
            models.UniqueConstraint(fields=["ncm", "ex"], name="tipi_ncm_ex_unico")
        ]

    def __str__(self) -> str:
        alvo = f"{self.ncm}" + (f" Ex {self.ex:02d}" if self.ex else "")
        return f"{alvo} — {'NT' if self.nao_tributado else self.aliquota}"


class Cest(models.Model):
    """
    Código Especificador da Substituição Tributária (Convênio ICMS 142/2018).

    Define o universo nacional de mercadorias sujeitas a ST. Um CEST casa com
    vários NCM, e o casamento é **por prefixo**: a tabela traz desde posição de
    4 dígitos até subitem de 8.
    """

    codigo = models.CharField(max_length=9, db_index=True)   # 01.001.00
    #: Prefixo de NCM em dígitos puros, de 2 a 8 caracteres.
    ncm_prefixo = models.CharField(max_length=8, db_index=True)
    anexo = models.CharField(max_length=10, blank=True, default="")
    segmento = models.CharField(max_length=120, blank=True, default="")
    descricao = models.TextField(blank=True, default="")

    class Meta:
        verbose_name = "CEST"
        verbose_name_plural = "CEST"
        ordering = ["codigo", "ncm_prefixo"]

    def __str__(self) -> str:
        return f"{self.codigo} ↔ {self.ncm_prefixo}"


class Cfop(models.Model):
    """
    CFOP válido para NF-e, da tabela do Portal Nacional.

    A tabela oficial é de **validação**, não dicionário: ela diz quais códigos
    a SEFAZ aceita e em que contexto, mas não traz a descrição textual. Por
    isso ``descricao`` fica em branco até virmos de outra fonte.
    """

    codigo = models.CharField(max_length=4, unique=True)
    descricao = models.CharField(max_length=300, blank=True, default="")
    valido_nfe = models.BooleanField(default=True)
    inicio_vigencia = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = "CFOP"
        verbose_name_plural = "CFOP"
        ordering = ["codigo"]

    def __str__(self) -> str:
        return self.codigo

    @property
    def entrada(self) -> bool:
        return self.codigo[0] in "123"

    @property
    def interestadual(self) -> bool:
        """2xxx e 6xxx são operações interestaduais; 1/5 internas; 3/7 exterior."""
        return self.codigo[0] in "26"


class FcpUf(models.Model):
    """
    Fundo de Combate à Pobreza por UF — a única tabela nacional oficial de
    alíquota estadual que existe.

    Alguns estados fixam o percentual e outros definem apenas um teto; por isso
    ``tipo``. Conferir um FCP "fixo" é afirmação; conferir um "máximo" só
    permite apontar quando passou do teto.
    """

    class Tipo(models.TextChoices):
        FIXO = "fixo", "Percentual fixo"
        MAXIMO = "maximo", "Percentual máximo"

    uf = models.CharField(max_length=2, unique=True)
    nome_uf = models.CharField(max_length=60, blank=True, default="")
    tipo = models.CharField(max_length=8, choices=Tipo.choices, default=Tipo.FIXO)
    aliquota = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    #: Segunda faixa, quando a UF publica mais de uma (caso de AL e SE).
    aliquota_alternativa = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )
    observacao = models.TextField(blank=True, default="")

    class Meta:
        verbose_name = "FCP por UF"
        verbose_name_plural = "FCP por UF"
        ordering = ["uf"]

    def __str__(self) -> str:
        return f"{self.uf} — {self.get_tipo_display()} {self.aliquota}%"
