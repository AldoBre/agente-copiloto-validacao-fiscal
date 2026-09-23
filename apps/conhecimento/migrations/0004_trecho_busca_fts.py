"""
Coluna gerada ``busca`` (tsvector) + índice GIN para o FTS nativo.

Nada aqui exige extensão nem admin: ``to_tsvector``/``ts_rank`` são built-in e
o app (dono das próprias tabelas) pode criar coluna e índice. O acento é
removido com ``translate`` — built-in e IMUTÁVEL, requisito de coluna gerada —
porque ``unaccent`` é extensão e cairia no mesmo bloqueio do pgvector.

Só existe no PostgreSQL: no SQLite (dev sem infra) a coluna nem é criada e o
retriever detecta pelo vendor. A coluna fica fora do model Django de propósito
— só o SQL cru do ``services/fts.py`` a lê, e assim o SQLite não precisa de
uma coluna fantasma.

Ao reaplicar o commit do pgvector (dcf5cc8), renumerar aquela migração para
0005 e apontar a dependência para esta.
"""
from django.db import migrations

_ACENTOS = "áàâãäéèêëíìîïóòôõöúùûüç"
_PLANOS = "aaaaaeeeeiiiiooooouuuuc"

_CRIAR = f"""
ALTER TABLE conhecimento_trecho
  ADD COLUMN IF NOT EXISTS busca tsvector
  GENERATED ALWAYS AS (
    setweight(to_tsvector('portuguese',
        translate(lower(coalesce(titulo_secao, '')), '{_ACENTOS}', '{_PLANOS}')), 'A') ||
    setweight(to_tsvector('portuguese',
        translate(lower(texto), '{_ACENTOS}', '{_PLANOS}')), 'B')
  ) STORED;
CREATE INDEX IF NOT EXISTS conhecimento_trecho_busca_gin
    ON conhecimento_trecho USING gin (busca);
"""

_REVERTER = """
DROP INDEX IF EXISTS conhecimento_trecho_busca_gin;
ALTER TABLE conhecimento_trecho DROP COLUMN IF EXISTS busca;
"""


def _criar(apps, schema_editor):
    if schema_editor.connection.vendor == "postgresql":
        schema_editor.execute(_CRIAR)


def _reverter(apps, schema_editor):
    if schema_editor.connection.vendor == "postgresql":
        schema_editor.execute(_REVERTER)


class Migration(migrations.Migration):

    dependencies = [
        ("conhecimento", "0003_tarefaindexacao"),
    ]

    operations = [
        migrations.RunPython(_criar, _reverter),
    ]
