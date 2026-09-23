from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("", views.ProvedorIAViewSet, basename="provedor")

urlpatterns = [
    path("catalogo/", views.catalogo, name="provedores-catalogo"),
    path("", include(router.urls)),
]
