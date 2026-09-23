from django.contrib import admin

from .models import Cest, Cfop, FcpUf, Ncm, TipiAliquota, VersaoTabela


@admin.register(VersaoTabela)
class VersaoTabelaAdmin(admin.ModelAdmin):
    """A primeira coisa a olhar quando o agente afirmar algo estranho: de quando é o dado."""

    list_display = ("tabela", "registros", "referencia", "capturado_em", "importado_em")
    readonly_fields = ("hash_arquivo",)


@admin.register(Ncm)
class NcmAdmin(admin.ModelAdmin):
    list_display = ("codigo", "descricao", "inicio_vigencia", "fim_vigencia")
    search_fields = ("codigo", "descricao")
    list_filter = ("fim_vigencia",)


@admin.register(TipiAliquota)
class TipiAliquotaAdmin(admin.ModelAdmin):
    list_display = ("ncm", "ex", "aliquota", "nao_tributado")
    search_fields = ("ncm", "descricao")
    list_filter = ("nao_tributado",)


@admin.register(Cest)
class CestAdmin(admin.ModelAdmin):
    list_display = ("codigo", "ncm_prefixo", "anexo", "segmento")
    search_fields = ("codigo", "ncm_prefixo", "descricao")


@admin.register(Cfop)
class CfopAdmin(admin.ModelAdmin):
    list_display = ("codigo", "valido_nfe", "inicio_vigencia")
    list_filter = ("valido_nfe",)
    search_fields = ("codigo",)


@admin.register(FcpUf)
class FcpUfAdmin(admin.ModelAdmin):
    list_display = ("uf", "nome_uf", "tipo", "aliquota", "aliquota_alternativa")
    list_filter = ("tipo",)
