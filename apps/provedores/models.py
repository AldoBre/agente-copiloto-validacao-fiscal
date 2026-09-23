"""
Cadastro de provedores/modelos de IA.

A tela /configuracoes/ escreve aqui. Nenhum modelo ou chave fica no código-fonte:
para testar outro provedor basta cadastrar e marcar como padrão.
"""
from __future__ import annotations

from django.core.exceptions import ValidationError
from django.db import models, transaction

from .crypto import criptografar, descriptografar, mascarar


class Provedor(models.TextChoices):
    ANTHROPIC = "anthropic", "Anthropic (Claude)"
    OPENAI = "openai", "OpenAI (GPT)"
    GOOGLE = "google", "Google (Gemini)"
    #: OpenAI hospedado na nossa assinatura Azure (contas kind=AIServices).
    #: Mesmos modelos da OpenAI pública, mas o dado não sai do nosso tenant —
    #: que é o motivo de existir, num produto que lê nota fiscal de cliente.
    AZURE = "azure", "Azure AI Foundry"


class TipoModelo(models.TextChoices):
    CHAT = "chat", "Chat / raciocínio"
    EMBEDDING = "embedding", "Embeddings (busca semântica)"


#: Todos os provedores suportados exigem API key.
PROVEDORES_SEM_CHAVE: set[str] = set()


class ProvedorIA(models.Model):
    """Uma combinação provedor + modelo + credencial, testável isoladamente."""

    nome = models.CharField(
        "Apelido",
        max_length=80,
        unique=True,
        help_text="Como este provedor aparece no seletor do chat. Ex.: 'Claude — produção'.",
    )
    provedor = models.CharField("Provedor", max_length=32, choices=Provedor.choices)
    tipo = models.CharField(
        "Tipo", max_length=16, choices=TipoModelo.choices, default=TipoModelo.CHAT
    )
    modelo = models.CharField(
        "Modelo",
        max_length=120,
        help_text="ID exato do modelo no provedor. Ex.: claude-opus-5, gpt-4o, gemini-2.0-flash.",
    )

    api_key_cripto = models.TextField("API key (criptografada)", blank=True, default="")
    base_url = models.URLField(
        "Base URL", blank=True, default="", help_text="Só para Ollama / Azure / compatíveis."
    )
    versao_api = models.CharField(
        "Versão da API", max_length=40, blank=True, default="",
        help_text="Usado pelo Azure OpenAI (api-version).",
    )

    temperatura = models.FloatField("Temperatura", default=0.2)
    max_tokens = models.PositiveIntegerField("Máx. tokens de saída", default=4096)
    timeout_segundos = models.PositiveIntegerField("Timeout (s)", default=120)

    parametros_extras = models.JSONField(
        "Parâmetros extras",
        default=dict,
        blank=True,
        help_text="Repassados direto ao construtor do modelo (JSON).",
    )

    ativo = models.BooleanField("Ativo", default=True)
    padrao = models.BooleanField(
        "Padrão", default=False, help_text="Usado quando o chat não especifica um provedor."
    )

    ultimo_teste_em = models.DateTimeField("Último teste", null=True, blank=True)
    ultimo_teste_ok = models.BooleanField("Último teste OK", null=True, blank=True)
    ultimo_teste_detalhe = models.TextField("Detalhe do teste", blank=True, default="")

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "provedor de IA"
        verbose_name_plural = "provedores de IA"
        ordering = ["tipo", "-padrao", "nome"]

    def __str__(self) -> str:
        return f"{self.nome} ({self.get_provedor_display()} · {self.modelo})"

    # ------------------------------------------------------------------ chave
    @property
    def api_key(self) -> str:
        return descriptografar(self.api_key_cripto)

    @api_key.setter
    def api_key(self, valor: str) -> None:
        self.api_key_cripto = criptografar(valor or "")

    @property
    def api_key_mascarada(self) -> str:
        return mascarar(self.api_key)

    @property
    def tem_chave(self) -> bool:
        return bool(self.api_key_cripto)

    # -------------------------------------------------------------- Azure ---
    @property
    def e_azure(self) -> bool:
        """
        O Foundry não guarda credencial nem endpoint aqui.

        Endpoint, deployments e chave são **fatos do deploy**: chegam pelas
        variáveis de ambiente do servidor. Não são editáveis por ninguém
        na tela, então não fazem sentido no banco — o registro existe só para o
        Foundry poder ser escolhido como o modelo em uso. Ver ``foundry.py``.
        """
        return self.provedor == Provedor.AZURE

    # ----------------------------------------------------------- validações --
    def clean(self):
        from .catalogo import buscar_modelo

        # O Foundry é a exceção: a chave vem do ambiente do servidor, e pedir
        # que alguém a cole aqui seria duplicar em texto um segredo que o deploy
        # já entrega.
        if not self.api_key_cripto and not self.e_azure:
            raise ValidationError({"api_key": "Informe a API key do provedor."})
        if buscar_modelo(self.provedor, self.modelo) is None:
            raise ValidationError(
                {"modelo": f"Modelo '{self.modelo}' não está no catálogo de {self.provedor}."}
            )
        if not isinstance(self.parametros_extras, dict):
            raise ValidationError({"parametros_extras": "Deve ser um objeto JSON."})

    # -------------------------------------------------------------- salvar ---
    def aplicar_catalogo(self) -> None:
        """
        Preenche tipo, teto de tokens, temperatura e timeout a partir do
        catálogo. Esses valores **não** são escolha do usuário: temperatura
        variável faz o modelo oscilar e teto errado trunca a resposta.
        """
        from .catalogo import TEMPERATURA, TIMEOUT_SEGUNDOS, buscar_modelo

        entrada = buscar_modelo(self.provedor, self.modelo)
        if entrada is None:
            return
        self.tipo = entrada["tipo"]
        self.max_tokens = entrada["max_tokens"] or 1024
        self.temperatura = TEMPERATURA if entrada["aceita_temperatura"] else 0.0
        self.timeout_segundos = TIMEOUT_SEGUNDOS

    @transaction.atomic
    def save(self, *args, **kwargs):
        self.aplicar_catalogo()
        super().save(*args, **kwargs)
        if self.padrao:
            # Só um padrão por tipo (um chat padrão + um embedding padrão).
            ProvedorIA.objects.filter(tipo=self.tipo).exclude(pk=self.pk).update(padrao=False)

    # ------------------------------------------------------------ consultas --
    @classmethod
    def obter_padrao(cls, tipo: str = TipoModelo.CHAT) -> "ProvedorIA | None":
        qs = cls.objects.filter(ativo=True, tipo=tipo)
        return qs.filter(padrao=True).first() or qs.first()

    def para_dicionario(self) -> dict:
        return {
            "id": self.pk,
            "nome": self.nome,
            "provedor": self.provedor,
            "provedor_label": self.get_provedor_display(),
            "tipo": self.tipo,
            "modelo": self.modelo,
            "base_url": self.base_url,
            "versao_api": self.versao_api,
            "temperatura": self.temperatura,
            "max_tokens": self.max_tokens,
            "timeout_segundos": self.timeout_segundos,
            "parametros_extras": self.parametros_extras,
            "ativo": self.ativo,
            "padrao": self.padrao,
            "tem_chave": self.tem_chave,
            "api_key_mascarada": self.api_key_mascarada,
            "ultimo_teste_em": self.ultimo_teste_em.isoformat() if self.ultimo_teste_em else None,
            "ultimo_teste_ok": self.ultimo_teste_ok,
            "ultimo_teste_detalhe": self.ultimo_teste_detalhe,
        }
