#!/usr/bin/env sh
# ============================================================================
#  Entrypoint do container: migra, semeia e sobe o ASGI (Django + FastAPI).
#
#  --proxy-headers/--forwarded-allow-ips: atrás do proxy reverso da plataforma o
#  X-Forwarded-Proto é quem diz que a conexão é https — sem isso o Django
#  acha que é http e o CSRF rejeita todo POST.
# ============================================================================
set -e

echo "→ Aplicando migrações…"
python manage.py migrate --noinput

echo "→ Semeando regras de parametrização (se necessário)…"
# Tolerante a corrida: com 2+ instâncias subindo juntas, a que perder a
# disputa não pode derrubar o container (o seed é idempotente).
python manage.py seed_regras || echo "⚠ seed_regras falhou; seguindo — outra instância deve ter semeado"

echo "→ Carregando tabelas fiscais oficiais (se mudaram)…"
# Compara o hash de cada arquivo antes de reprocessar, então o custo em boot
# repetido é de milissegundos. Tolerante a falha: sem as tabelas o consultor
# ainda faz a conferência aritmética, e a tela diz o que não foi verificado.
python manage.py importar_tabelas_fiscais || echo "⚠ importar_tabelas_fiscais falhou; seguindo sem as tabelas"

echo "→ Importando base de conhecimento versionada (se necessário)…"
# --sem-embeddings: o boot não pode depender do provedor de IA nem demorar por
# causa dele; POST /api/conhecimento/reindexar/ completa os vetores depois.
python manage.py importar_markdown --sem-embeddings || echo "⚠ importar_markdown falhou; seguindo — a base pode ser ingerida pela interface"

exec python -m uvicorn config.asgi:application \
  --host 0.0.0.0 \
  --port "${PORT:-8000}" \
  --workers "${UVICORN_WORKERS:-2}" \
  --proxy-headers \
  --forwarded-allow-ips '*' \
  --log-level info
