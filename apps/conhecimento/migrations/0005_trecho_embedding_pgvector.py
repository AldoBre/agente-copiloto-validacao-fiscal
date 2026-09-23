"""
Embedding sai do JSONField e vira coluna nativa ``vector`` (pgvector).

A similaridade passa a ser calculada no PostgreSQL, onde o dado já está, em vez
de carregar a base inteira na RAM de cada worker e comparar com numpy. Medido na
escala de produção (4.365 trechos × 3.072 dimensões): o pico de ~466 MB ao montar
o índice foi o que empurrou o plano compartilhado para swap e cravou a CPU em
100% em 31/07/2026.

## Por que esta migração NÃO cria a extensão

A primeira versão disto (commit dcf5cc8, revertido) rodava
``CREATE EXTENSION IF NOT EXISTS vector`` apostando que, com a extensão já
presente, o comando viraria um NOTICE inofensivo para o usuário comum.

**No Azure isso é falso, e foi verificado contra o servidor real em 20/08/2026:**
a checagem de privilégio acontece ANTES do ``IF NOT EXISTS``, então o comando
estoura com ``InsufficientPrivilege`` mesmo quando não teria nada a fazer::

    Because vector isn't a trusted extension, only members of
    "azure_pg_admin" are allowed to use CREATE EXTENSION vector

Como o ``migrate`` roda no boot do container, isso derrubaria a aplicação — que
é exatamente o incidente que causou a reversão em 02/08.

Então aqui a extensão é **conferida, não criada**. Se faltar, a migração para com
uma mensagem que diz o comando exato e quem precisa rodá-lo, em vez de despejar
um erro de Postgres. Em desenvolvimento, onde o dono do banco é superusuário, ela
ainda cria — só tenta quando sabe que precisa.

## Como voltar atrás — leia antes de reverter a imagem

**Reverter só o container NÃO funciona, e o pior é que fica verde.** O código
anterior a este consulta o embedding como JSON (``exclude(embedding=[])``), e
contra uma coluna ``vector`` isso é ``operator does not exist: vector = jsonb``.
O ``/health`` de então não toca no banco, então o pipeline aprova o rollback
enquanto a base de conhecimento devolve 500 em toda consulta — falha pior que a
original, porque não aparece em monitor nenhum.

O rollback correto tem DOIS passos, nesta ordem:

1. desfazer o schema, com acesso ao banco de produção::

       python manage.py migrate conhecimento 0004

   O ``_restaurar_json`` devolve os vetores para a coluna JSON antes de dropar
   a coluna ``vector``: nada do que foi pago em embeddings se perde.

2. só então voltar a imagem.

Se o objetivo for apenas parar de usar a busca semântica — que é o motivo mais
provável —, **não reverta nada**: ``buscaSemantica: "off"`` em
``infra/parameters/prod.parameters.json``, ou a app setting
``AGENTE_BUSCA_SEMANTICA=off`` para efeito imediato. A coluna ``vector`` fica, e
não atrapalha.

## Espaço em disco depois da conversão

A tabela cresce (~165 MB → ~232 MB medidos em produção) e **não encolhe
sozinha**: ``DROP COLUMN`` no PostgreSQL é operação de metadado, e os chunks
TOAST do JSON continuam referenciados pelas tuplas vivas. ``VACUUM`` comum não
devolve nada — só ``VACUUM FULL``, que trava a tabela. Não há urgência (o
servidor tem folga), mas quem rodar o VACUUM comum esperando recuperar espaço
vai achar que resolveu.

## A cópia dos dados

Um único ``UPDATE`` com cast ``jsonb → text → vector``, resolvido no servidor:
nada de ``RunPython`` trazendo 13 milhões de floats para o Python. É idempotente
e leva menos de um segundo na base atual.
"""
from django.db import migrations

import pgvector.django

#: Ação para quem esbarrar no pré-requisito. Fica aqui, e não num README, porque
#: é aqui que a pessoa vai estar quando o deploy parar.
COMO_CRIAR = """
A extensão 'vector' não existe neste banco, e a aplicação não tem privilégio
para criá-la (no Azure, só membros de azure_pg_admin conseguem).

Peça a um administrador do PostgreSQL para rodar UMA vez, conectado ao MESMO
banco desta aplicação — extensão é objeto por banco, e rodar no 'postgres'
responde com sucesso sem resolver nada:

    CREATE EXTENSION IF NOT EXISTS vector;

Em Azure PostgreSQL Flexible Server, 'vector' também precisa estar na lista do
parâmetro azure.extensions do servidor (conferir com
`az postgres flexible-server parameter show ... -n azure.extensions`).
"""


def _exigir_extensao(apps, schema_editor):
    """Confere; só tenta criar quando falta e há privilégio para isso."""
    if schema_editor.connection.vendor != "postgresql":
        return

    with schema_editor.connection.cursor() as cursor:
        cursor.execute("SELECT 1 FROM pg_extension WHERE extname = 'vector'")
        if cursor.fetchone():
            return

    # Só chega aqui se realmente faltar. A tentativa vem depois da checagem de
    # propósito: no Postgres, um comando que falha aborta a transação inteira, e
    # a migração roda dentro de uma — tentar primeiro e perguntar depois deixaria
    # o resto da migração inalcançável.
    try:
        schema_editor.execute("CREATE EXTENSION IF NOT EXISTS vector")
    except Exception as exc:  # noqa: BLE001
        raise RuntimeError(COMO_CRIAR) from exc


def _copiar_vetores(apps, schema_editor):
    """JSON → vector num único UPDATE, resolvido no servidor."""
    if schema_editor.connection.vendor != "postgresql":
        return
    schema_editor.execute(
        """
        UPDATE conhecimento_trecho
           SET embedding_vec = embedding::text::vector
         WHERE embedding_vec IS NULL
           AND embedding IS NOT NULL
           AND embedding::text NOT IN ('[]', 'null')
        """
    )


def _restaurar_json(apps, schema_editor):
    """Volta o vetor para JSON, para o downgrade não perder o que foi pago."""
    if schema_editor.connection.vendor != "postgresql":
        return
    schema_editor.execute(
        """
        UPDATE conhecimento_trecho
           SET embedding = embedding_vec::text::jsonb
         WHERE embedding_vec IS NOT NULL
        """
    )


class Migration(migrations.Migration):

    dependencies = [
        ("conhecimento", "0004_trecho_busca_fts"),
    ]

    operations = [
        migrations.RunPython(_exigir_extensao, migrations.RunPython.noop),
        migrations.AddField(
            model_name="trecho",
            name="embedding_vec",
            field=pgvector.django.VectorField(blank=True, null=True),
        ),
        migrations.RunPython(_copiar_vetores, _restaurar_json),
        migrations.RemoveField(model_name="trecho", name="embedding"),
        migrations.RenameField(
            model_name="trecho", old_name="embedding_vec", new_name="embedding"
        ),
    ]
