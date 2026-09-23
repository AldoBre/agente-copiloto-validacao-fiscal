"""
Base de conhecimento das parametrizações fiscais da Senior.

Fluxo: Fonte (URL ou texto colado) → Documento (markdown limpo) →
Trecho (chunk + embedding opcional) → recuperado pelo agente no chat.
"""
from __future__ import annotations

import hashlib

from django.db import models
from pgvector.django import VectorField


class TipoFonte(models.TextChoices):
    URL = "url", "Página web (scraping)"
    LISTA = "lista", "Lista de páginas web"
    TEXTO = "texto", "Texto colado"
    ARQUIVO = "arquivo", "Arquivo enviado"


class FonteConhecimento(models.Model):
    nome = models.CharField(max_length=200)
    tipo = models.CharField(max_length=16, choices=TipoFonte.choices, default=TipoFonte.URL)
    url = models.URLField(max_length=1000, blank=True, default="")
    #: Para o tipo "lista": todas as páginas a ingerir de uma vez.
    urls = models.JSONField("URLs", default=list, blank=True)
    descricao = models.TextField(blank=True, default="")

    #: Quando ligado, ``ingerir_url`` segue links do mesmo domínio.
    seguir_links = models.BooleanField("Seguir links internos", default=False)
    profundidade_max = models.PositiveSmallIntegerField("Profundidade máxima", default=1)

    ativo = models.BooleanField(default=True)
    ultima_ingestao_em = models.DateTimeField(null=True, blank=True)
    ultima_ingestao_ok = models.BooleanField(null=True, blank=True)
    ultima_ingestao_detalhe = models.TextField(blank=True, default="")

    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "fonte de conhecimento"
        verbose_name_plural = "fontes de conhecimento"
        ordering = ["nome"]

    def __str__(self) -> str:
        return self.nome


class Documento(models.Model):
    fonte = models.ForeignKey(
        FonteConhecimento, related_name="documentos", on_delete=models.CASCADE
    )
    titulo = models.CharField(max_length=400)
    url = models.URLField(max_length=1000, blank=True, default="")
    conteudo = models.TextField()
    hash_conteudo = models.CharField(max_length=64, db_index=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "documento"
        verbose_name_plural = "documentos"
        ordering = ["titulo"]
        constraints = [
            models.UniqueConstraint(fields=["fonte", "hash_conteudo"], name="doc_unico_por_fonte")
        ]

    def __str__(self) -> str:
        return self.titulo

    @staticmethod
    def calcular_hash(conteudo: str) -> str:
        return hashlib.sha256(conteudo.encode("utf-8")).hexdigest()

    def save(self, *args, **kwargs):
        if not self.hash_conteudo:
            self.hash_conteudo = self.calcular_hash(self.conteudo)
        super().save(*args, **kwargs)


class Trecho(models.Model):
    documento = models.ForeignKey(Documento, related_name="trechos", on_delete=models.CASCADE)
    ordem = models.PositiveIntegerField(default=0)
    titulo_secao = models.CharField(max_length=400, blank=True, default="")
    texto = models.TextField()

    #: Vetor do trecho como coluna nativa `vector` (pgvector). Sem dimensão
    #: fixa de propósito: o modelo de embeddings é trocável em runtime e cada
    #: um tem a sua (1.536 no small, 3.072 no large). Ausência de vetor é NULL,
    #: nunca lista vazia.
    #:
    #: Não há índice HNSW: com a base atual a varredura exata roda em dezenas
    #: de milissegundos no banco, e exata é melhor que aproximada. Se um dia
    #: justificar, o índice para 3.072 dimensões exige o cast para halfvec —
    #: `vector` puro só indexa até 2.000 dimensões.
    embedding = VectorField(null=True, blank=True)
    modelo_embedding = models.CharField(max_length=120, blank=True, default="")

    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "trecho"
        verbose_name_plural = "trechos"
        ordering = ["documento_id", "ordem"]
        indexes = [models.Index(fields=["documento", "ordem"])]

    def __str__(self) -> str:
        return f"{self.documento.titulo} #{self.ordem}"

    @property
    def tem_embedding(self) -> bool:
        # `is not None` e não `bool()`: dependendo da versão do pgvector a
        # coluna volta como list ou como array numpy, e `bool()` de um array
        # levanta ValueError. Ausência de vetor é NULL, nunca lista vazia.
        return self.embedding is not None

    def referencia(self) -> dict:
        return {
            "trecho_id": self.pk,
            "documento": self.documento.titulo,
            "secao": self.titulo_secao,
            "url": self.documento.url,
            "fonte": self.documento.fonte.nome,
        }


class TarefaIndexacao(models.Model):
    """
    Reindexação rodando em segundo plano.

    O estado vive no banco, e não em memória, porque o processo sobe com dois
    workers (``docker-entrypoint.sh``): o navegador que pergunta "como está?"
    quase sempre cai no worker que **não** iniciou a tarefa. Também é o que faz
    a barra de progresso sobreviver a um F5.

    A tarefa é retomável — trabalha sobre ``documentos_pendentes()`` —, então
    um container reciclado no meio do caminho não corrompe nada: basta disparar
    de novo e ela continua de onde parou.
    """

    class Estado(models.TextChoices):
        RODANDO = "rodando", "Em andamento"
        CONCLUIDA = "concluida", "Concluída"
        ERRO = "erro", "Falhou"

    estado = models.CharField(max_length=12, choices=Estado.choices, default=Estado.RODANDO)
    total_inicial = models.PositiveIntegerField(default=0)
    processados = models.PositiveIntegerField(default=0)
    trechos = models.PositiveIntegerField(default=0)
    com_embedding = models.PositiveIntegerField(default=0)
    pendentes = models.PositiveIntegerField(default=0)
    mensagem = models.TextField(blank=True, default="")

    criado_em = models.DateTimeField(auto_now_add=True)
    #: Batida do coração: atualizado a cada lote. Tarefa "rodando" com este
    #: campo velho é tarefa cujo worker morreu.
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "tarefa de indexação"
        verbose_name_plural = "tarefas de indexação"
        ordering = ["-criado_em"]

    def __str__(self) -> str:
        return f"{self.get_estado_display()} — {self.processados}/{self.total_inicial}"

    def para_dicionario(self) -> dict:
        total = self.total_inicial or 1
        return {
            "id": self.pk,
            "estado": self.estado,
            "total_inicial": self.total_inicial,
            "processados": self.processados,
            "trechos": self.trechos,
            "com_embedding": self.com_embedding,
            "pendentes": self.pendentes,
            "percentual": min(round(self.processados / total * 100), 100),
            "mensagem": self.mensagem,
            "atualizado_em": self.atualizado_em.isoformat(),
        }


class RegraParametrizacao(models.Model):
    """
    Mapa editável "campo do XML → onde parametrizar no Senior".

    Semeado por ``python manage.py seed_regras`` a partir de
    ``comparador.services.mapa_campos``. O consultor pode refinar cada linha no
    /admin conforme a realidade do cliente — o agente lê daqui em primeiro lugar.
    """

    campo = models.CharField(
        max_length=120,
        unique=True,
        help_text="Chave 'GRUPO.campo' (ex.: ICMS.CST) ou só 'campo' como fallback.",
    )
    categoria = models.CharField(max_length=60, blank=True, default="")
    area = models.CharField(
        "Área / rotina no Senior",
        max_length=200,
        blank=True,
        default="",
        help_text="Ex.: 'Regras de tributação', 'Cadastro de produto'. Preencha conforme a versão do cliente.",
    )
    orientacao = models.TextField("Orientação ao consultor")
    referencia_url = models.URLField(max_length=1000, blank=True, default="")
    observacoes = models.TextField(blank=True, default="")
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "regra de parametrização"
        verbose_name_plural = "regras de parametrização"
        ordering = ["campo"]

    def __str__(self) -> str:
        return self.campo
