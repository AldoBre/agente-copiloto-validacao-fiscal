from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("fontes", views.FonteConhecimentoViewSet, basename="fonte")
router.register("documentos", views.DocumentoViewSet, basename="documento")
router.register("regras", views.RegraParametrizacaoViewSet, basename="regra")

urlpatterns = [
    path("status/", views.status_base, name="conhecimento-status"),
    path("reindexar/", views.reindexar, name="conhecimento-reindexar"),
    path(
        "reindexar/progresso/",
        views.progresso_reindexacao,
        name="conhecimento-reindexar-progresso",
    ),
    path("buscar/", views.buscar, name="conhecimento-buscar"),
    path("", include(router.urls)),
]
