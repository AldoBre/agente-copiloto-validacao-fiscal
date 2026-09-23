from django.contrib import admin

from .models import Comparacao, DivergenciaRegistrada, Lote, ParDocumentos


class ParInline(admin.TabularInline):
    model = ParDocumentos
    extra = 0
    fields = (
        "indice",
        "arquivo_cliente",
        "arquivo_senior",
        "score",
        "confianca",
        "comparado",
        "total_divergencias",
        "total_criticas",
    )
    readonly_fields = fields
    can_delete = False
    max_num = 0


@admin.register(Lote)
class LoteAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "criado_em",
        "status",
        "total_cliente",
        "total_senior",
        "total_pares",
        "total_comparados",
    )
    list_filter = ("status", "criado_em")
    readonly_fields = ("id", "criado_em", "resumo", "documentos", "relatorio_markdown", "avisos")
    inlines = [ParInline]


class DivergenciaInline(admin.TabularInline):
    model = DivergenciaRegistrada
    extra = 0
    fields = ("severidade", "categoria", "campo", "item_numero", "valor_cliente", "valor_senior")
    readonly_fields = fields
    can_delete = False
    max_num = 0


@admin.register(Comparacao)
class ComparacaoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "criado_em",
        "arquivo_cliente",
        "arquivo_senior",
        "total_divergencias",
        "total_criticas",
    )
    list_filter = ("criado_em", "status")
    search_fields = ("chave_cliente", "chave_senior", "arquivo_cliente", "arquivo_senior")
    readonly_fields = ("id", "criado_em", "resumo", "resultado", "relatorio_markdown")
    inlines = [DivergenciaInline]


@admin.register(DivergenciaRegistrada)
class DivergenciaRegistradaAdmin(admin.ModelAdmin):
    list_display = ("comparacao", "severidade", "categoria", "campo", "item_numero")
    list_filter = ("severidade", "categoria", "tipo")
    search_fields = ("campo", "item_codigo", "item_descricao")
