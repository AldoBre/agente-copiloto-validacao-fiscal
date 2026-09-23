from django.contrib import admin
from django.urls import include, path

from apps.provedores import views as provedores_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.core.urls")),
    path("api/provedores/", include("apps.provedores.urls")),
    # A configuração que vem do ambiente do servidor (hoje, só o Azure AI
    # Foundry). Fica fora de /api/provedores/ porque não é
    # um provedor cadastrado — é um fato do deploy.
    path("api/platform-settings/", provedores_views.platform_settings),
    path("api/comparador/", include("apps.comparador.urls")),
    path("api/conhecimento/", include("apps.conhecimento.urls")),
    path("api/agente/", include("apps.agente.urls")),
]
