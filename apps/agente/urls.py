from django.urls import path

from . import views

urlpatterns = [
    path("conversas/", views.listar_conversas, name="agente-conversas"),
    path("conversas/<uuid:conversa_id>/", views.detalhe_conversa, name="agente-conversa"),
    path(
        "mensagens/<int:mensagem_id>/avaliacao/",
        views.avaliar_mensagem,
        name="agente-avaliacao",
    ),
    path("provedores/", views.provedores_disponiveis, name="agente-provedores"),
    path("chat-sync/", views.chat_sincrono, name="agente-chat-sync"),
]
