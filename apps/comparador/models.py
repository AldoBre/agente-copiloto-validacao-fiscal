from __future__ import annotations

import uuid

from django.db import models


class Lote(models.Model):
    """
    Comparação em massa: dois conjuntos de XMLs (normalmente dois ZIPs) que são
    pareados automaticamente e comparados par a par.
    """

    class Status(models.TextChoices):
        PAREADO = "pareado", "Pareado — aguardando comparação"
        COMPARANDO = "comparando", "Comparando"
        CONCLUIDO = "concluido", "Concluído"
        ERRO = "erro", "Erro"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    nome_origem_cliente = models.CharField(max_length=255, blank=True, default="")
    nome_origem_senior = models.CharField(max_length=255, blank=True, default="")

    status = models.CharField(max_length=12, choices=Status.choices, default=Status.PAREADO)

    total_cliente = models.PositiveIntegerField(default=0)
    total_senior = models.PositiveIntegerField(default=0)
    total_pares = models.PositiveIntegerField(default=0)
    total_comparados = models.PositiveIntegerField(default=0)

    #: Todos os documentos lidos, para permitir repareamento manual na tela.
    #: ``{"cliente": [{nome_arquivo, caminho, resumo...}], "senior": [...]}``
    documentos = models.JSONField(default=dict, blank=True)

    resumo = models.JSONField(default=dict, blank=True)
    relatorio_markdown = models.TextField(blank=True, default="")
    avisos = models.JSONField(default=list, blank=True)

    class Meta:
        verbose_name = "lote de comparação"
        verbose_name_plural = "lotes de comparação"
        ordering = ["-criado_em"]

    def __str__(self) -> str:
        return f"Lote {self.id} — {self.total_pares} par(es)"

    @property
    def nao_pareados(self) -> dict:
        pareados_cliente = set(self.pares.values_list("arquivo_cliente", flat=True))
        pareados_senior = set(self.pares.values_list("arquivo_senior", flat=True))
        docs = self.documentos or {}
        return {
            "cliente": [
                d for d in docs.get("cliente", []) if d["nome_arquivo"] not in pareados_cliente
            ],
            "senior": [
                d for d in docs.get("senior", []) if d["nome_arquivo"] not in pareados_senior
            ],
        }


class Comparacao(models.Model):
    """Uma execução do comparador: dois XMLs + o resultado compilado."""

    class Status(models.TextChoices):
        OK = "ok", "Concluída"
        ERRO = "erro", "Erro"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    criado_em = models.DateTimeField(auto_now_add=True)

    lote = models.ForeignKey(
        Lote,
        null=True,
        blank=True,
        related_name="comparacoes",
        on_delete=models.CASCADE,
        help_text="Preenchido quando a comparação faz parte de um lote.",
    )

    arquivo_cliente = models.CharField("Arquivo do cliente", max_length=255, blank=True, default="")
    arquivo_senior = models.CharField("Arquivo da Senior", max_length=255, blank=True, default="")
    chave_cliente = models.CharField(max_length=60, blank=True, default="")
    chave_senior = models.CharField(max_length=60, blank=True, default="")

    status = models.CharField(max_length=10, choices=Status.choices, default=Status.OK)
    mensagem_erro = models.TextField(blank=True, default="")

    resumo = models.JSONField(default=dict, blank=True)
    resultado = models.JSONField(default=dict, blank=True)
    relatorio_markdown = models.TextField(blank=True, default="")

    total_divergencias = models.PositiveIntegerField(default=0)
    total_criticas = models.PositiveIntegerField(default=0)
    total_altas = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "comparação"
        verbose_name_plural = "comparações"
        ordering = ["-criado_em"]

    def __str__(self) -> str:
        return f"Comparação {self.id} — {self.total_divergencias} divergência(s)"


class DivergenciaRegistrada(models.Model):
    """
    Divergência persistida (linha a linha).

    O JSON completo já está em ``Comparacao.resultado``; esta tabela existe para
    permitir consultas/relatórios cruzando várias comparações — por exemplo,
    "quais campos mais divergem nesta implantação".
    """

    comparacao = models.ForeignKey(
        Comparacao, related_name="divergencias", on_delete=models.CASCADE
    )
    categoria = models.CharField(max_length=40, db_index=True)
    grupo = models.CharField(max_length=40, blank=True, default="")
    campo = models.CharField(max_length=120, db_index=True)
    caminho = models.CharField(max_length=255, blank=True, default="")
    escopo = models.CharField(max_length=20, default="item")
    tipo = models.CharField(max_length=40)
    severidade = models.CharField(max_length=10, db_index=True)
    valor_cliente = models.TextField(blank=True, default="")
    valor_senior = models.TextField(blank=True, default="")
    diferenca = models.CharField(max_length=80, blank=True, default="")
    item_numero = models.IntegerField(null=True, blank=True)
    item_codigo = models.CharField(max_length=80, blank=True, default="")
    item_descricao = models.CharField(max_length=255, blank=True, default="")
    pista = models.TextField(blank=True, default="")

    class Meta:
        verbose_name = "divergência"
        verbose_name_plural = "divergências"
        ordering = ["severidade", "item_numero", "campo"]
        indexes = [models.Index(fields=["comparacao", "severidade"])]

    def __str__(self) -> str:
        return f"{self.categoria}.{self.campo} ({self.severidade})"


class ParDocumentos(models.Model):
    """
    Um par (nota do cliente ↔ nota do Senior) dentro de um lote.

    O pareamento é feito por assinatura fiscal (destinatário, valor, produtos,
    data), não por nome de arquivo — os dois sistemas nomeiam e numeram as notas
    de formas diferentes.
    """

    class Confianca(models.TextChoices):
        ALTA = "alta", "Alta"
        MEDIA = "media", "Média"
        BAIXA = "baixa", "Baixa"
        MANUAL = "manual", "Manual"

    lote = models.ForeignKey(Lote, related_name="pares", on_delete=models.CASCADE)
    indice = models.PositiveIntegerField(default=0)

    arquivo_cliente = models.CharField(max_length=255)
    arquivo_senior = models.CharField(max_length=255)

    score = models.FloatField(default=0)
    confianca = models.CharField(max_length=8, choices=Confianca.choices, default=Confianca.BAIXA)
    motivos = models.JSONField(default=list, blank=True)

    comparado = models.BooleanField(default=False)
    comparacao = models.OneToOneField(
        Comparacao, null=True, blank=True, related_name="par", on_delete=models.SET_NULL
    )

    total_divergencias = models.PositiveIntegerField(default=0)
    total_criticas = models.PositiveIntegerField(default=0)
    total_altas = models.PositiveIntegerField(default=0)
    erro = models.TextField(blank=True, default="")

    class Meta:
        verbose_name = "par de documentos"
        verbose_name_plural = "pares de documentos"
        ordering = ["lote_id", "indice"]
        indexes = [models.Index(fields=["lote", "indice"])]

    def __str__(self) -> str:
        return f"{self.arquivo_cliente} ↔ {self.arquivo_senior}"

    def para_dicionario(self, documentos: dict | None = None) -> dict:
        docs = documentos if documentos is not None else (self.lote.documentos or {})
        indice_cliente = {d["nome_arquivo"]: d for d in docs.get("cliente", [])}
        indice_senior = {d["nome_arquivo"]: d for d in docs.get("senior", [])}
        return {
            "indice": self.indice,
            "arquivo_cliente": self.arquivo_cliente,
            "arquivo_senior": self.arquivo_senior,
            "cliente": indice_cliente.get(self.arquivo_cliente, {}),
            "senior": indice_senior.get(self.arquivo_senior, {}),
            "score": round(self.score, 1),
            "confianca": self.confianca,
            "confianca_rotulo": self.get_confianca_display(),
            "motivos": self.motivos,
            "comparado": self.comparado,
            "comparacao_id": str(self.comparacao_id) if self.comparacao_id else None,
            "total_divergencias": self.total_divergencias,
            "total_criticas": self.total_criticas,
            "total_altas": self.total_altas,
            "erro": self.erro,
        }
