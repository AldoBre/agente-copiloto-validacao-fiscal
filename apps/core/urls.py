from django.urls import path

from . import views

urlpatterns = [
    path("health", views.health, name="health"),
    # Readiness: usado pelo pipeline. Ver a docstring de `pronto`.
    path("health/pronto", views.pronto, name="health-pronto"),
    path("", views.painel, name="painel"),
    path("configuracoes/", views.configuracoes, name="configuracoes"),
]
