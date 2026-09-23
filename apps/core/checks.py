"""
Verificações de implantação — rodam em ``python manage.py check --deploy``.
"""
from __future__ import annotations

from django.conf import settings
from django.core.checks import Tags, Warning as Aviso, register


@register(Tags.security, deploy=True)
def banco_exige_tls(app_configs, **kwargs):
    """
    ``sslmode=prefer`` contra um banco remoto é uma armadilha silenciosa.

    O nome sugere preferência, mas o comportamento é *degradar sem avisar*: se o
    servidor não oferecer TLS, o libpq conecta em texto claro e nada no log
    denuncia. Contra um PostgreSQL gerenciado isso normalmente não passa
    (o serviço recusa conexão sem TLS), mas basta um proxy, um túnel ou um
    servidor intermediário mal configurado para a senha do banco e as notas
    fiscais dos clientes trafegarem abertas.

    O check só falha em ``--deploy``: em dev, contra o Postgres em container
    local sem certificado, ``prefer`` é o valor certo.
    """
    config = settings.DATABASES.get("default", {})
    if "postgresql" not in config.get("ENGINE", ""):
        return []

    modo = (config.get("OPTIONS") or {}).get("sslmode", "")
    if modo in ("require", "verify-ca", "verify-full"):
        return []

    return [
        Aviso(
            f"A conexão com o PostgreSQL está com sslmode={modo!r}, que aceita "
            "conexão sem criptografia.",
            hint=(
                "Defina DB_SSLMODE=require no .env (mínimo fora da máquina local). Para "
                "também validar o certificado do servidor, use "
                "DB_SSLMODE=verify-full com DB_SSLROOTCERT apontando para o CA."
            ),
            id="core.W001",
        )
    ]
