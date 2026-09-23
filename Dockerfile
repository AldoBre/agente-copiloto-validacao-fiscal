# ============================================================================
#  Imagem de produção — Django + FastAPI em ASGI (uvicorn), porta 8000.
#
#  Roda como container atrás do proxy reverso da plataforma de hospedagem;
#  o entrypoint aplica migrações e semeia as regras antes de subir o servidor.
# ============================================================================
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# SHA do commit que gerou esta imagem. É o que torna legível o `versao_prompt`
# carimbado em cada resposta: com ele, `git show <sha>:apps/agente/prompts.py`
# devolve o prompt exato que produziu aquela resposta. Vem por --build-arg no
# workflow; vazio em build local, e aí o hash sozinho ainda identifica.
# Fica aqui, e não no topo: um ARG declarado antes do `pip install` invalida
# aquela camada a cada commit e faria todo build reinstalar as dependências.
ARG GIT_SHA=""
ENV GIT_SHA=$GIT_SHA

# collectstatic não toca no banco (DB_ENGINE=sqlite garante zero dependência
# de rede no build); a SECRET_KEY de build não vaza para runtime.
RUN DJANGO_SECRET_KEY=apenas-para-o-collectstatic DJANGO_DEBUG=False DB_ENGINE=sqlite \
    python manage.py collectstatic --noinput

RUN useradd --create-home appuser \
    && chown -R appuser:appuser /app
USER appuser

EXPOSE 8000

ENTRYPOINT ["./docker-entrypoint.sh"]
