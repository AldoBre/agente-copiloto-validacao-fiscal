from django.contrib import admin

from .models import AvaliacaoMensagem, Conversa, Mensagem


class MensagemInline(admin.TabularInline):
    model = Mensagem
    extra = 0
    fields = ("papel", "conteudo", "modelo", "erro", "criado_em")
    readonly_fields = fields
    can_delete = False
    max_num = 0


@admin.register(Conversa)
class ConversaAdmin(admin.ModelAdmin):
    list_display = ("id", "titulo", "comparacao", "lote", "atualizado_em")
    list_filter = ("atualizado_em",)
    search_fields = ("titulo",)
    inlines = [MensagemInline]


@admin.register(Mensagem)
class MensagemAdmin(admin.ModelAdmin):
    list_display = ("conversa", "papel", "modelo", "criado_em")
    list_filter = ("papel", "modelo")
    search_fields = ("conteudo",)


@admin.register(AvaliacaoMensagem)
class AvaliacaoMensagemAdmin(admin.ModelAdmin):
    """
    A tela de revisão do feedback. Filtrar por ``valor=-1`` e ler os negativos é
    o ritual quinzenal que transforma o sinal em mudança de prompt/regra — não
    construir tela custom antes de existir volume que justifique.
    """

    list_display = ("criado_em", "valor", "motivo", "resumo_pergunta", "modelo_usado")
    list_filter = ("valor", "motivo", "criado_em")
    search_fields = ("comentario", "mensagem__conteudo")
    readonly_fields = ("mensagem", "contexto", "chave_sessao", "criado_em", "atualizado_em")

    @admin.display(description="pergunta")
    def resumo_pergunta(self, obj: AvaliacaoMensagem) -> str:
        return ((obj.contexto or {}).get("pergunta") or "")[:80]

    @admin.display(description="modelo")
    def modelo_usado(self, obj: AvaliacaoMensagem) -> str:
        return (obj.contexto or {}).get("modelo") or ""
