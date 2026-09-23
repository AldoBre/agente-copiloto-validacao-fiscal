from django.utils import timezone
from rest_framework import status, viewsets
from rest_framework.decorators import action, api_view
from rest_framework.response import Response

from . import foundry
from .catalogo import TIMEOUT_SEGUNDOS, para_frontend
from .factory import testar
from .models import ProvedorIA
from .serializers import ProvedorIASerializer


class ProvedorIAViewSet(viewsets.ModelViewSet):
    """CRUD dos provedores + ações de teste e definição de padrão."""

    queryset = ProvedorIA.objects.all()
    serializer_class = ProvedorIASerializer

    def get_queryset(self):
        qs = super().get_queryset()
        tipo = self.request.query_params.get("tipo")
        if tipo:
            qs = qs.filter(tipo=tipo)
        if self.request.query_params.get("ativo") == "1":
            qs = qs.filter(ativo=True)
        return qs

    @action(detail=True, methods=["post"])
    def testar(self, request, pk=None):
        provedor = self.get_object()
        ok, detalhe = testar(provedor)
        provedor.ultimo_teste_em = timezone.now()
        provedor.ultimo_teste_ok = ok
        provedor.ultimo_teste_detalhe = detalhe
        provedor.save(update_fields=["ultimo_teste_em", "ultimo_teste_ok", "ultimo_teste_detalhe"])
        return Response(
            {"ok": ok, "detalhe": detalhe, "provedor": self.get_serializer(provedor).data},
            status=status.HTTP_200_OK if ok else status.HTTP_502_BAD_GATEWAY,
        )

    @action(detail=True, methods=["post"], url_path="definir-padrao")
    def definir_padrao(self, request, pk=None):
        provedor = self.get_object()
        provedor.padrao = True
        provedor.ativo = True
        provedor.save()
        return Response(self.get_serializer(provedor).data)


@api_view(["GET"])
def platform_settings(request):
    """
    ``GET /api/platform-settings/`` — configuração vinda da infra.

    Só leitura: não existe PUT porque endpoint, deployments e chave do Foundry
    vêm das variáveis de ambiente do servidor — mudar aqui seria criar uma
    segunda verdade, que diverge do ambiente no dia em que ele mudar.
    """
    return Response({"azure": foundry.para_frontend()})


@api_view(["GET"])
def catalogo(request):
    """Catálogo estático de provedores e modelos que a tela usa nos selects."""
    return Response({"provedores": para_frontend(), "timeout_segundos": TIMEOUT_SEGUNDOS})
