from __future__ import annotations

import uuid

from django.db import models

from apps.comparador.models import Comparacao, Lote
from apps.provedores.models import ProvedorIA


class Conversa(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    titulo = models.CharField(max_length=200, blank=True, default="Nova conversa")
    comparacao = models.ForeignKey(
        Comparacao,
        null=True,
        blank=True,
        related_name="conversas",
        on_delete=models.SET_NULL,
        help_text="Comparação nota a nota que serve de contexto para esta conversa.",
    )
    lote = models.ForeignKey(
        Lote,
        null=True,
        blank=True,
        related_name="conversas",
        on_delete=models.SET_NULL,
        help_text="Lote (comparação em massa) que serve de contexto para esta conversa.",
    )
    #: Identificador do navegador (localStorage), para o histórico listar as
    #: conversas daquele consultor. NÃO é autenticação: a API é AllowAny e
    #: qualquer um consegue ver tudo. Login é pré-requisito antes de expor o
    #: app fora da rede interna.
    chave_sessao = models.CharField(max_length=64, blank=True, default="", db_index=True)

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "conversa"
        verbose_name_plural = "conversas"
        ordering = ["-atualizado_em"]
        indexes = [models.Index(fields=["-atualizado_em"], name="conversa_recentes_idx")]

    def __str__(self) -> str:
        return self.titulo or str(self.id)


class Mensagem(models.Model):
    class Papel(models.TextChoices):
        USUARIO = "usuario", "Consultor"
        AGENTE = "agente", "Agente"
        SISTEMA = "sistema", "Sistema"

    conversa = models.ForeignKey(Conversa, related_name="mensagens", on_delete=models.CASCADE)
    papel = models.CharField(max_length=10, choices=Papel.choices)
    conteudo = models.TextField()

    provedor = models.ForeignKey(
        ProvedorIA, null=True, blank=True, on_delete=models.SET_NULL, related_name="mensagens"
    )
    modelo = models.CharField(max_length=120, blank=True, default="")

    #: Trechos da base de conhecimento usados na resposta.
    fontes = models.JSONField(default=list, blank=True)
    #: Mapa dos marcadores ``[[print:N]]`` citados: ``{"3": "https://…"}``.
    #: Sem isto persistido, reabrir a conversa mostraria o texto sem as imagens.
    prints = models.JSONField(default=dict, blank=True)
    #: Tokens/latência quando o provedor devolver.
    metadados = models.JSONField(default=dict, blank=True)

    erro = models.TextField(blank=True, default="")
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "mensagem"
        verbose_name_plural = "mensagens"
        ordering = ["criado_em", "id"]
        indexes = [models.Index(fields=["conversa", "criado_em"], name="mensagem_conversa_idx")]

    def __str__(self) -> str:
        return f"[{self.papel}] {self.conteudo[:60]}"

    def para_dicionario(self) -> dict:
        # Serializer único: usado pelo detalhe da conversa e pela resposta do
        # chat síncrono. Campo novo aqui aparece nos dois de graça.
        avaliacao = getattr(self, "avaliacao", None)
        return {
            "id": self.pk,
            "papel": self.papel,
            "conteudo": self.conteudo,
            "modelo": self.modelo,
            "fontes": self.fontes,
            "prints": self.prints,
            # O que o consultor viu na tela quando a pergunta veio de um botão.
            "rotulo": (self.metadados or {}).get("rotulo", ""),
            "erro": self.erro,
            "avaliacao": avaliacao.valor if avaliacao else None,
            "criado_em": self.criado_em.isoformat(),
        }


class AvaliacaoMensagem(models.Model):
    """
    👍/👎 do consultor numa resposta do agente.

    O ``contexto`` guarda um retrato do que produziu aquela resposta (pergunta,
    fontes, lote). É ele que dá valor ao dado meses depois: as FKs são SET_NULL
    e o lote pode ser apagado — sem o retrato, o registro vira um voto órfão,
    inútil tanto para revisão quanto para exportar dataset.

    O sinal serve para **revisão humana** e dataset. Nunca para alterar prompt
    em runtime: o endpoint é público e o id da mensagem é sequencial.
    """

    class Valor(models.IntegerChoices):
        NEGATIVO = -1, "Não gostei"
        POSITIVO = 1, "Gostei"

    class Motivo(models.TextChoices):
        TELA_ERRADA = "tela_errada", "Apontou a tela errada"
        SEM_FUNDAMENTO = "sem_fundamento", "Resposta sem fundamento na documentação"
        INCOMPLETA = "incompleta", "Faltou tratar divergências"
        FORMATO = "formato", "Formato/organização ruim"
        OUTRO = "outro", "Outro"

    mensagem = models.OneToOneField(
        Mensagem, related_name="avaliacao", on_delete=models.CASCADE
    )
    valor = models.SmallIntegerField(choices=Valor.choices)
    motivo = models.CharField(max_length=20, choices=Motivo.choices, blank=True, default="")
    comentario = models.TextField(blank=True, default="")

    #: Retrato do contexto no momento do voto (pergunta, fontes, lote, modelo).
    contexto = models.JSONField(default=dict, blank=True)
    chave_sessao = models.CharField(max_length=64, blank=True, default="")

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "avaliação de mensagem"
        verbose_name_plural = "avaliações de mensagens"
        ordering = ["-criado_em"]

    def __str__(self) -> str:
        return f"{self.get_valor_display()} — mensagem {self.mensagem_id}"
