#!/usr/bin/env bash
# ============================================================================
#  Sobe o sistema em modo ASGI (Django + FastAPI), que é o necessário para o
#  streaming do chat funcionar.
#
#      ./run.sh              # http://127.0.0.1:8000
#      ./run.sh 0.0.0.0 8080
# ============================================================================
set -euo pipefail

cd "$(dirname "$0")"

HOST="${1:-127.0.0.1}"
PORTA="${2:-8000}"

# Os caminhos Scripts/ são o venv no Windows (Git Bash / WSL montando o disco):
# sem eles o script cai no python3 do sistema, que não tem as dependências.
if [ -x "venv/bin/python" ]; then
  PY="venv/bin/python"
elif [ -x ".venv/bin/python" ]; then
  PY=".venv/bin/python"
elif [ -x ".venv/Scripts/python.exe" ]; then
  PY=".venv/Scripts/python.exe"
elif [ -x "venv/Scripts/python.exe" ]; then
  PY="venv/Scripts/python.exe"
else
  PY="python3"
fi

if [ ! -f ".env" ]; then
  echo "→ .env não encontrado; copiando de .env.example"
  cp .env.example .env
fi

echo "→ Aplicando migrações…"
"$PY" manage.py migrate --noinput

echo "→ Semeando regras de parametrização (se necessário)…"
"$PY" manage.py seed_regras >/dev/null

echo "→ Importando base de conhecimento versionada (se necessário)…"
"$PY" manage.py importar_markdown --sem-embeddings

echo ""
echo "  Painel .......... http://${HOST}:${PORTA}/"
echo "  Configurações ... http://${HOST}:${PORTA}/configuracoes/"
echo "  Admin ........... http://${HOST}:${PORTA}/admin/"
echo "  API da IA ....... http://${HOST}:${PORTA}/api/ia/docs"
echo ""

exec "$PY" -m uvicorn config.asgi:application \
  --host "$HOST" --port "$PORTA" --reload --log-level info
