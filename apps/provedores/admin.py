from django.contrib import admin

from .models import ProvedorIA


@admin.register(ProvedorIA)
class ProvedorIAAdmin(admin.ModelAdmin):
    list_display = ("nome", "provedor", "tipo", "modelo", "ativo", "padrao", "ultimo_teste_ok")
    list_filter = ("provedor", "tipo", "ativo", "padrao")
    search_fields = ("nome", "modelo")
    readonly_fields = ("api_key_mascarada", "ultimo_teste_em", "ultimo_teste_ok", "ultimo_teste_detalhe")
    exclude = ("api_key_cripto", "parametros_extras", "base_url", "versao_api", "deployment")
