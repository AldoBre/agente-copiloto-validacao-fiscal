"""
Sinônimos do vocabulário fiscal para expansão de consulta.

O consultor escreve sigla ("ST", "difal", "NF-e"); a documentação da Senior
escreve por extenso ("substituição tributária", "nota fiscal eletrônica") — e
vice-versa ("ICMS-ST" tokeniza como ``icms st``). A expansão é SÓ do lado da
consulta (expandir o documento inflaria o índice e distorceria o IDF) e entra
com peso menor que o termo digitado — ver ``PESO_SINONIMO`` no retriever.

O dicionário é escrito em forma legível (acentuada); as formas canônicas que a
busca usa são derivadas aqui mesmo, no import:

- ``SINONIMOS_CANONICOS`` — chaves e expansões passadas pelo ``tokenizar``
  (com stemming), para o BM25 em memória;
- ``SINONIMOS_SUPERFICIE`` — sem stemming, para montar o ``to_tsquery`` do FTS
  nativo do Postgres (que stemiza sozinho).

Pares morfológicos que o stemming já unifica ("tributação"/"tributária",
"parametrizar"/"parametrização") NÃO pertencem a este dicionário.
"""
from .texto import tokenizar, tokenizar_superficie

#: forma legível: token digitado → termos adicionais a pontuar.
_SINONIMOS = {
    # siglas → por extenso
    "st": ("substituição", "tributária"),
    "difal": ("diferencial", "alíquota", "partilha"),
    "cst": ("situação", "tributária"),
    "csosn": ("situação", "tributária", "simples", "nacional"),
    "mva": ("margem", "valor", "agregado"),
    "bc": ("base", "cálculo"),
    "aliq": ("alíquota",),
    "nf": ("nota", "fiscal"),
    "nfe": ("nota", "fiscal", "eletrônica"),
    "nfce": ("nota", "fiscal", "consumidor"),
    "nfse": ("nota", "fiscal", "serviço"),
    "cest": ("especificador", "substituição", "tributária"),
    "cbenef": ("código", "benefício", "fiscal"),
    "ncm": ("nomenclatura", "classificação", "fiscal"),
    "issqn": ("iss", "serviço"),
    "iss": ("issqn", "serviço"),
    # por extenso → sigla (a documentação escreve "ICMS-ST", "DIFAL")
    "substituição": ("st",),
    "diferencial": ("difal",),
    # o Snowball não unifica este par ("fiscal" → fiscal, "fiscais" → fisc)
    "fiscal": ("fiscais",),
    "fiscais": ("fiscal",),
}


def _canonizar(fn) -> dict[str, tuple[str, ...]]:
    canonico: dict[str, tuple[str, ...]] = {}
    for chave, expansoes in _SINONIMOS.items():
        (chave_c,) = fn(chave)
        vistos: list[str] = []
        for termo in expansoes:
            for token in fn(termo):
                if token != chave_c and token not in vistos:
                    vistos.append(token)
        if vistos:
            canonico[chave_c] = tuple(vistos)
    return canonico


SINONIMOS_CANONICOS = _canonizar(tokenizar)
SINONIMOS_SUPERFICIE = _canonizar(tokenizar_superficie)
