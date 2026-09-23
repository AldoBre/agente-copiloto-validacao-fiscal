from django.contrib import admin

from .models import Documento, FonteConhecimento, RegraParametrizacao, Trecho


@admin.register(FonteConhecimento)
class FonteConhecimentoAdmin(admin.ModelAdmin):
    list_display = ("nome", "tipo", "url", "ativo", "ultima_ingestao_em", "ultima_ingestao_ok")
    list_filter = ("tipo", "ativo")
    search_fields = ("nome", "url")


class TrechoInline(admin.TabularInline):
    model = Trecho
    extra = 0
    fields = ("ordem", "titulo_secao", "texto")
    readonly_fields = fields
    can_delete = False
    max_num = 0


@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "fonte", "url", "criado_em")
    list_filter = ("fonte",)
    search_fields = ("titulo", "url", "conteudo")
    inlines = [TrechoInline]


@admin.register(RegraParametrizacao)
class RegraParametrizacaoAdmin(admin.ModelAdmin):
    list_display = ("campo", "categoria", "area", "atualizado_em")
    list_filter = ("categoria",)
    search_fields = ("campo", "area", "orientacao")
