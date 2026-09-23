"""
Configuração do projeto "Agente de Implantação Fiscal — Senior ERP".
"""
from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")


def _bool(nome: str, padrao: bool = False) -> bool:
    return str(os.getenv(nome, str(padrao))).strip().lower() in ("1", "true", "yes", "on", "sim")


# ---------------------------------------------------------------- segurança --
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "dev-insecure-troque-esta-chave")
DEBUG = _bool("DJANGO_DEBUG", True)
ALLOWED_HOSTS = [h.strip() for h in os.getenv("DJANGO_ALLOWED_HOSTS", "*").split(",") if h.strip()]
CSRF_TRUSTED_ORIGINS = [
    o.strip() for o in os.getenv("DJANGO_CSRF_TRUSTED_ORIGINS", "").split(",") if o.strip()
]

# Chave de criptografia das credenciais de IA (ver apps/provedores/crypto.py).
APP_ENCRYPTION_KEY = os.getenv("APP_ENCRYPTION_KEY", "").strip()

# ------------------------------------------------------------------- apps ---
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # terceiros
    "rest_framework",
    "corsheaders",
    # projeto
    "apps.core",
    "apps.provedores",
    "apps.comparador",
    "apps.conhecimento",
    "apps.agente",
    "apps.fiscal",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"
ASGI_APPLICATION = "config.asgi.application"

# --------------------------------------------------------------- database ---
#: Modo TLS da conexão. Bancos PostgreSQL gerenciados normalmente **exigem**
#: TLS: com ``prefer`` a conexão até sobe, mas ``require`` é o mínimo aceitável
#: fora da máquina local, e ``verify-full`` (que também valida o certificado do
#: servidor, evitando man-in-the-middle) precisa de ``DB_SSLROOTCERT``.
DB_SSLMODE = os.getenv("DB_SSLMODE", "prefer").strip()

# PostgreSQL é o padrão mesmo sem DB_ENGINE; SQLite só com DB_ENGINE=sqlite
# explícito (desenvolvimento sem infraestrutura).
if os.getenv("DB_ENGINE", "postgres").lower().startswith("post"):
    _opcoes_db = {
        "sslmode": DB_SSLMODE,
        "connect_timeout": int(os.getenv("DB_CONNECT_TIMEOUT", "10")),
    }
    if os.getenv("DB_SSLROOTCERT"):
        _opcoes_db["sslrootcert"] = os.getenv("DB_SSLROOTCERT")

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.getenv("DB_NAME", "agente_implantacao"),
            "USER": os.getenv("DB_USER", "postgres"),
            "PASSWORD": os.getenv("DB_PASSWORD", ""),
            "HOST": os.getenv("DB_HOST", "127.0.0.1"),
            "PORT": os.getenv("DB_PORT", "5432"),
            "OPTIONS": _opcoes_db,
            # Com o banco fora da máquina, abrir conexão a cada request custa um
            # handshake TLS inteiro. Mas conexão persistente tem contrapartida em
            # banco gerenciado: o plano limita conexões (um plano de entrada
            # permite ~50), e o limite é consumido por worker, não por instância —
            # CONN_MAX_AGE alto com muitos workers esgota o servidor.
            "CONN_MAX_AGE": int(os.getenv("DB_CONN_MAX_AGE", "60")),
            # Sem isto, a conexão reaproveitada que o servidor já derrubou (ou
            # que o balanceador do provedor expirou por ociosidade) só é descoberta
            # quando a query falha, e o erro aparece no usuário.
            "CONN_HEALTH_CHECKS": True,
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
            "OPTIONS": {"timeout": 20},
        }
    }

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ------------------------------------------------------------------- i18n ---
LANGUAGE_CODE = "pt-br"
TIME_ZONE = "America/Sao_Paulo"
USE_I18N = True
USE_TZ = True

# ---------------------------------------------------------------- estáticos --
STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
STORAGES = {
    "default": {"BACKEND": "django.core.files.storage.FileSystemStorage"},
    "staticfiles": {"BACKEND": "whitenoise.storage.CompressedStaticFilesStorage"},
}

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

# ------------------------------------------------------------------- DRF ----
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.AllowAny"],
    "DEFAULT_AUTHENTICATION_CLASSES": [],
    "DEFAULT_RENDERER_CLASSES": ["rest_framework.renderers.JSONRenderer"],
    "UNAUTHENTICATED_USER": None,
}

# Sem login por enquanto (requisito do MVP) → CORS liberado em dev.
CORS_ALLOW_ALL_ORIGINS = DEBUG

# --------------------------------------------------------- app: comparador ---
COMPARADOR = {
    "TOLERANCIA_MONETARIA": float(os.getenv("COMPARADOR_TOLERANCIA_MONETARIA", "0.01")),
    "TOLERANCIA_PERCENTUAL": float(os.getenv("COMPARADOR_TOLERANCIA_PERCENTUAL", "0.01")),
    "TAMANHO_MAXIMO_XML_MB": int(os.getenv("COMPARADOR_TAMANHO_MAXIMO_XML_MB", "10")),
    # "impostos" (padrão): compara só os grupos de imposto e a classificação
    #   fiscal do item (CFOP, NCM, CEST, cBenef). Cadastro, documento e dado
    #   comercial servem apenas para parear as notas.
    # "completo": inclui cabeçalho, totalizadores e campos comerciais.
    "ESCOPO": os.getenv("COMPARADOR_ESCOPO", "impostos"),
}

# ------------------------------------------------------------- app: agente ---
AGENTE = {
    # TEMPORÁRIO — a busca semântica fica DESLIGADA por padrão até o pgvector
    # ser habilitado no banco (CREATE EXTENSION exige admin). A versão em RAM
    # derrubou o plano compartilhado em 31/07/2026. Ligue localmente com
    # AGENTE_BUSCA_SEMANTICA=on.
    "BUSCA_SEMANTICA": _bool("AGENTE_BUSCA_SEMANTICA", False),
    # Quantos trechos da base de conhecimento entram no contexto do modelo.
    "TOP_K_CONTEXTO": int(os.getenv("AGENTE_TOP_K_CONTEXTO", "6")),
    # Quantas mensagens anteriores da conversa são reenviadas.
    "JANELA_HISTORICO": int(os.getenv("AGENTE_JANELA_HISTORICO", "12")),
    # Limite de divergências enviadas em detalhe no prompt (o resto vira resumo).
    "MAX_DIVERGENCIAS_PROMPT": int(os.getenv("AGENTE_MAX_DIVERGENCIAS_PROMPT", "60")),
    # Deixa o modelo consultar as tabelas oficiais e a documentação durante a
    # resposta (apps/agente/ferramentas.py). Desligue para voltar ao fluxo de
    # uma passada só — é a chave de reversão se algum provedor der problema.
    "FERRAMENTAS": _bool("AGENTE_FERRAMENTAS", True),
    # Rodadas de consulta por pergunta — RODADAS, não consultas: numa rodada o
    # modelo pode pedir várias de uma vez. Na última ele responde sem
    # ferramentas ligadas, o que encerra o ciclo por construção.
    #
    # Duas porque o custo é real: as definições das ferramentas somam ~1.480
    # tokens em toda pergunta (medido), e cada rodada reenvia o prompt inteiro
    # mais os resultados acumulados. Com 2, o pior caso são 3 idas ao provedor.
    #
    # Era 3 até 20/09/2026. Medido em produção com o gpt-5.5: a análise de uma
    # NFS-e usou as 3 rodadas (2+2+1 buscas na documentação), e cada rodada
    # custou de 6 a 10 s entre o modelo decidir e a busca voltar. A terceira
    # trazia uma busca só, de retorno marginal.
    "MAX_PASSOS_FERRAMENTA": int(os.getenv("AGENTE_MAX_PASSOS_FERRAMENTA", "2")),
}

# --------------------------------------------------------------- logging ----
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simples": {"format": "[{levelname}] {asctime} {name}: {message}", "style": "{"},
    },
    "handlers": {
        "console": {"class": "logging.StreamHandler", "formatter": "simples"},
    },
    "root": {"handlers": ["console"], "level": "INFO"},
    "loggers": {
        "apps": {"handlers": ["console"], "level": "DEBUG" if DEBUG else "INFO", "propagate": False},
        "httpx": {"level": "WARNING"},
    },
}
