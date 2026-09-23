"""
Criptografia simétrica (Fernet) das credenciais de IA guardadas no banco.

A chave vem de ``APP_ENCRYPTION_KEY``. Se não estiver definida, é derivada
determinísticamente da ``SECRET_KEY`` — aceitável em desenvolvimento, mas em
produção defina ``APP_ENCRYPTION_KEY`` explicitamente: trocar a SECRET_KEY
tornaria todas as chaves salvas ilegíveis.
"""
from __future__ import annotations

import base64
import hashlib
import logging
from functools import lru_cache

from cryptography.fernet import Fernet, InvalidToken
from django.conf import settings

logger = logging.getLogger(__name__)


@lru_cache(maxsize=1)
def _fernet() -> Fernet:
    chave = (getattr(settings, "APP_ENCRYPTION_KEY", "") or "").strip()
    if chave:
        return Fernet(chave.encode())
    derivada = base64.urlsafe_b64encode(hashlib.sha256(settings.SECRET_KEY.encode()).digest())
    return Fernet(derivada)


def criptografar(texto: str) -> str:
    if not texto:
        return ""
    return _fernet().encrypt(texto.encode("utf-8")).decode("ascii")


def descriptografar(token: str) -> str:
    if not token:
        return ""
    try:
        return _fernet().decrypt(token.encode("ascii")).decode("utf-8")
    except (InvalidToken, ValueError):
        logger.error(
            "Falha ao descriptografar credencial. A APP_ENCRYPTION_KEY/SECRET_KEY "
            "provavelmente mudou — recadastre a chave do provedor."
        )
        return ""


def mascarar(segredo: str) -> str:
    """Devolve algo como ``sk-a…4f2c`` para exibir na tela sem vazar a chave."""
    if not segredo:
        return ""
    if len(segredo) <= 8:
        return "•" * len(segredo)
    return f"{segredo[:4]}…{segredo[-4:]}"
