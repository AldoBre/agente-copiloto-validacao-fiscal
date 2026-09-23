"""Views das telas do sistema: painel do comparador e configurações."""
from django.http import JsonResponse
from django.shortcuts import render


def health(request):
    """
    Liveness: o processo está de pé. NÃO toca no banco de propósito — uma
    oscilação do PostgreSQL não deve fazer o App Service reciclar o container.
    """
    return JsonResponse({"status": "ok"})


def pronto(request):
    """
    Readiness: o processo está de pé **e consegue servir**.

    É este que o pipeline de deploy consulta, e a diferença importa. O
    ``/health`` responde 200 mesmo com o banco fora ou com o schema
    incompatível com o código — foi assim que um rollback de imagem passaria
    verde deixando a base de conhecimento em 500: o código anterior à coluna
    `vector` consulta o embedding como JSON e quebra no operador.

    A consulta abaixo é a que fecha essa brecha: toca a tabela que o agente
    depende e exercita a coluna do jeito que o código atual espera. Barata —
    um count com filtro, milissegundos.
    """
    from apps.conhecimento.models import Trecho

    try:
        com_vetor = Trecho.objects.filter(embedding__isnull=False).count()
    except Exception as exc:  # noqa: BLE001
        return JsonResponse(
            {"status": "indisponivel", "motivo": f"{type(exc).__name__}: {exc}"[:200]},
            status=503,
        )
    return JsonResponse({"status": "ok", "trechos_com_vetor": com_vetor})


def painel(request):
    """Tela 1 — chat com o agente (esquerda) + comparador de XMLs (direita)."""
    return render(request, "core/painel.html", {"pagina": "painel"})


def configuracoes(request):
    """Tela 2 — provedores de IA, modelos, credenciais e base de conhecimento."""
    return render(request, "core/configuracoes.html", {"pagina": "configuracoes"})
