from django.urls import path

from . import views, views_lote

urlpatterns = [
    # --- comparação nota a nota ---------------------------------------------
    path("comparar/", views.comparar, name="comparador-comparar"),
    path("historico/", views.historico, name="comparador-historico"),
    # --- comparação em massa (lotes) ----------------------------------------
    path("lotes/", views_lote.historico_lotes, name="comparador-lotes"),
    path("lotes/parear/", views_lote.parear_lote, name="comparador-lote-parear"),
    path("lotes/<uuid:lote_id>/", views_lote.detalhe_lote, name="comparador-lote-detalhe"),
    path(
        "lotes/<uuid:lote_id>/repartear/",
        views_lote.repartear_lote,
        name="comparador-lote-repartear",
    ),
    path(
        "lotes/<uuid:lote_id>/comparar/",
        views_lote.comparar_lote,
        name="comparador-lote-comparar",
    ),
    path(
        "lotes/<uuid:lote_id>/relatorio/",
        views_lote.relatorio_detalhado,
        name="comparador-lote-relatorio",
    ),
    path(
        "lotes/<uuid:lote_id>/consolidar/",
        views_lote.consolidar_lote,
        name="comparador-lote-consolidar",
    ),
    path(
        "lotes/<uuid:lote_id>/xml/<str:lado>/<path:nome_arquivo>",
        views_lote.xml_do_lote,
        name="comparador-lote-xml",
    ),
    # --- detalhe de uma comparação (deve ficar por último) ------------------
    path(
        "<uuid:comparacao_id>/relatorio/",
        views_lote.relatorio_comparacao,
        name="comparador-comparacao-relatorio",
    ),
    path("<uuid:comparacao_id>/", views.detalhe, name="comparador-detalhe"),
]
