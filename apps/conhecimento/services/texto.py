"""
Tokenização canônica da busca textual: normalização, stopwords e stemming.

O pipeline por token é::

    casefold → sem acento → stopword? fora → reparo de sufixo → stem → sem acento

O **reparo de sufixo** existe porque o consultor digita sem acento e o Snowball
português depende dos sufixos acentuados: ``stem("operacao") = "operaca"`` mas
``stem("operação") = "oper"``. Recolocando só as terminações inequívocas
(``cao → ção``, ``coes → ções``…), "operacao", "operação" e "operações" caem
todas no mesmo stem — e pares derivacionais do vocabulário fiscal
("tributação"/"tributária", "parametrizar"/"parametrização") unificam sem
dicionário. Medido em 02/08/2026 com snowballstemmer 3.x; os testes
(``TextoTests``) cravam o comportamento.

``tokenizar`` é o pipeline completo (índice BM25 e consulta usam o MESMO).
``tokenizar_superficie`` para antes do stem — é o insumo do FTS nativo do
Postgres, que faz o próprio stemming no ``to_tsvector('portuguese', ...)``.
"""
from __future__ import annotations

import re
import unicodedata

try:
    import snowballstemmer

    _STEMMER = snowballstemmer.stemmer("portuguese")
except Exception:  # noqa: BLE001 — sem o pacote a busca segue, só sem stemming
    _STEMMER = None

_RE_TOKEN = re.compile(r"[a-z0-9á-úçãõâêô_]+", re.IGNORECASE)

#: Terminações que o unaccent destrói e o stemmer precisa de volta. Só as
#: inequívocas: em português, palavra terminada em "cao" é sempre "ção".
_REPAROS = (("coes", "ções"), ("cao", "ção"), ("soes", "sões"), ("ssao", "ssão"))

PALAVRAS_VAZIAS = {
    "a", "o", "as", "os", "de", "da", "do", "das", "dos", "e", "em", "no", "na",
    "nos", "nas", "um", "uma", "para", "por", "com", "que", "se", "ao", "a",
    "aos", "as", "ou", "the", "of", "is", "nao", "sim", "como", "qual", "quais",
    "onde", "ser", "esta", "estao", "esse", "essa", "isso", "meu", "minha",
}


def sem_acento(texto: str) -> str:
    texto = unicodedata.normalize("NFKD", texto or "")
    return "".join(c for c in texto if not unicodedata.combining(c))


def _reparar_sufixo(token: str) -> str:
    if len(token) <= 4:
        return token
    for cru, reparado in _REPAROS:
        if token.endswith(cru):
            return token[: -len(cru)] + reparado
    return token


def _stem(token: str) -> str:
    if _STEMMER is None:
        return token
    return sem_acento(_STEMMER.stemWord(_reparar_sufixo(token)))


def tokenizar_superficie(texto: str) -> list[str]:
    """Tokens normalizados (minúsculos, sem acento, sem stopword), SEM stem."""
    return [
        t
        for t in (sem_acento(bruto.casefold()) for bruto in _RE_TOKEN.findall(texto or ""))
        if len(t) > 1 and t not in PALAVRAS_VAZIAS
    ]


def tokenizar(texto: str) -> list[str]:
    """Pipeline completo — a forma canônica usada pelo índice BM25 e pela consulta."""
    return [_stem(t) for t in tokenizar_superficie(texto)]
