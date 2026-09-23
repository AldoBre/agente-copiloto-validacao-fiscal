"""
Leitura dos arquivos oficiais para as tabelas de referência.

Cada função aqui foi escrita contra o arquivo REAL, não contra a documentação
dele — e as armadilhas comentadas foram todas observadas na prática, não
supostas. Quando um comentário diz "5 linhas órfãs", são cinco linhas que
existem mesmo no arquivo de hoje.
"""
from __future__ import annotations

import hashlib
import json
import re
from datetime import date, datetime
from decimal import Decimal
from pathlib import Path

#: 31/12/9999 é a sentinela de "vigente" da API do NCM. Traduzimos para None
#: porque comparar data com sentinela é fonte silenciosa de erro.
SENTINELA_VIGENTE = "31/12/9999"

_RE_TAG = re.compile(r"<[^>]+>")
_RE_NCM8 = re.compile(r"^\d{4}\.\d{2}\.\d{2}$")


def hash_arquivo(caminho: Path) -> str:
    """SHA-256 — é o que detecta troca de conteúdo numa URL fixa (caso da TIPI)."""
    h = hashlib.sha256()
    with caminho.open("rb") as f:
        for bloco in iter(lambda: f.read(65536), b""):
            h.update(bloco)
    return h.hexdigest()


def _limpar(texto: str) -> str:
    """
    Normaliza texto vindo dos arquivos oficiais.

    Cuida de três sujeiras reais: NBSP disfarçado de espaço (1.397 no NCM),
    quebras de linha dentro de célula (175 na TIPI) e espaços duplicados.
    """
    if not texto:
        return ""
    return " ".join(str(texto).replace("\xa0", " ").split())


def _sem_html(texto: str) -> str:
    """
    Remove marcação das descrições do NCM.

    ``<sup>2</sup>`` vira "2" e não desaparece: apagar cegamente transformaria
    "cm2" em "cm" e mudaria o sentido técnico da descrição.
    """
    if not texto:
        return ""
    texto = texto.replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&")
    return _limpar(_RE_TAG.sub("", texto))


def _data_br(valor: str) -> date | None:
    if not valor or valor == SENTINELA_VIGENTE:
        return None
    try:
        return datetime.strptime(valor.strip(), "%d/%m/%Y").date()
    except (ValueError, AttributeError):
        return None


def so_digitos(codigo: str) -> str:
    """
    ``0101.21.00`` → ``01012100``.

    A posição do ponto muda conforme o nível (``01.01`` tem 4 dígitos e
    ``0102.21`` tem 6), então contar pontos ou usar split não funciona —
    o comprimento em dígitos é o único critério confiável.
    """
    return re.sub(r"\D", "", codigo or "")


# --------------------------------------------------------------------------- #
#  NCM
# --------------------------------------------------------------------------- #
def ler_ncm(caminho: Path) -> tuple[list[dict], str]:
    """
    Devolve ``(registros, referencia)`` a partir do JSON do Siscomex.

    A hierarquia é montada por PREFIXO de dígitos, e não por busca do código
    pai: 4.434 nós não têm pai declarado no arquivo (``0101.21.00`` existe mas
    ``0101.21`` não). Procurar o pai por chave perderia todos eles.
    """
    dados = json.loads(caminho.read_text(encoding="utf-8"))
    referencia = _limpar(dados.get("Data_Ultima_Atualizacao_NCM", ""))
    ato = _limpar(dados.get("Ato", ""))

    registros: list[dict] = []
    por_codigo: dict[str, str] = {}

    for item in dados.get("Nomenclaturas", []):
        codigo = so_digitos(item.get("Codigo", ""))
        if not codigo:
            continue
        descricao = _sem_html(item.get("Descricao", ""))
        # Os travessões marcam profundidade visual e atrapalham a busca.
        descricao_limpa = descricao.lstrip("- ").strip()
        por_codigo[codigo] = descricao_limpa
        registros.append(
            {
                "codigo": codigo,
                "descricao": descricao_limpa,
                "inicio_vigencia": _data_br(item.get("Data_Inicio", "")),
                # .get() e não acesso direto: um item do arquivo (3913.90.50)
                # traz três chaves a mais que todos os outros.
                "fim_vigencia": _data_br(item.get("Data_Fim", "")),
                "ato": ato,
            }
        )

    # Cadeia de ancestrais por prefixo. Sem isso, "Outros" — que aparece 2.027
    # vezes — é texto inútil para qualquer busca.
    niveis = (2, 4, 5, 6, 7)
    for registro in registros:
        codigo = registro["codigo"]
        cadeia = [
            por_codigo[codigo[:n]]
            for n in niveis
            if n < len(codigo) and codigo[:n] in por_codigo
        ]
        cadeia.append(registro["descricao"])
        registro["descricao_hierarquica"] = " > ".join(p for p in cadeia if p)

    return registros, referencia


# --------------------------------------------------------------------------- #
#  TIPI
# --------------------------------------------------------------------------- #
def ler_tipi(caminho: Path) -> tuple[list[dict], str]:
    """
    Lê a planilha da TIPI.

    Três detalhes que quebram um parser ingênuo: o cabeçalho está na linha 8
    (as sete primeiras são título e histórico de atualizações), 4.460 linhas
    são agrupadores sem alíquota, e cinco linhas de Ex-tarifário vêm com a
    coluna NCM vazia, herdando o código da linha anterior.
    """
    from openpyxl import load_workbook

    wb = load_workbook(caminho, data_only=True, read_only=True)
    ws = wb["Tabela Completa"]

    # A linha 3 lista, uma por linha, todas as atualizações desde 2022. A
    # versão vigente é a ÚLTIMA — as anteriores só interessam ao histórico, e
    # concatená-las produziria uma "fonte" de 500 caracteres na resposta.
    referencia = ""
    for linha in ws.iter_rows(min_row=3, max_row=3, max_col=1, values_only=True):
        atos = [
            _limpar(parte)
            for parte in str(linha[0] or "").split("\n")
            if re.search(r"(Decreto|Ato Declaratório Executivo)\s+n", parte or "")
        ]
        referencia = (atos[-1] if atos else _limpar(linha[0] or ""))[:200]

    registros: list[dict] = []
    ultimo_ncm = ""

    for a, b, c, d in ws.iter_rows(min_row=9, max_col=4, values_only=True):
        if a is None and b is None and c is None and d is None:
            continue

        codigo_bruto = str(a).strip() if a is not None else ""

        if _RE_NCM8.fullmatch(codigo_bruto):
            ultimo_ncm = so_digitos(codigo_bruto)
        elif a is None and b is not None and ultimo_ncm:
            pass  # Ex-tarifário órfão: herda o NCM da linha acima.
        else:
            continue  # agrupador (capítulo/posição/subposição/item)

        # EX vem como int (1..5) ou texto ("Ex 01", "01"). Zero = linha base.
        ex = 0
        if b is not None:
            achado = re.search(r"\d+", str(b))
            if achado:
                ex = int(achado.group())

        aliquota, nao_tributado = None, False
        if isinstance(d, str):
            texto = d.strip().upper()
            if texto == "NT":
                # "NT" é fora do campo de incidência — não é zero. Tratar como
                # 0% faria o agente cobrar IPI de quem não deve.
                nao_tributado = True
            elif texto:
                try:
                    aliquota = Decimal(texto.replace(",", "."))
                except Exception:  # noqa: BLE001
                    aliquota = None
        elif d is not None:
            aliquota = Decimal(str(round(float(d), 2)))  # mata 7.800000000000001

        registros.append(
            {
                "ncm": ultimo_ncm,
                "ex": ex,
                "descricao": _limpar(c or ""),
                "aliquota": aliquota,
                "nao_tributado": nao_tributado,
            }
        )

    wb.close()
    return registros, referencia


# --------------------------------------------------------------------------- #
#  CEST
# --------------------------------------------------------------------------- #
#: Tabelas 1..26 do HTML são os anexos II..XXVII. A 0 é o de-para de segmentos,
#: e as 27..30 são formulário, lista de contribuintes e a seção de retificação
#: — nenhuma delas é dado vigente.
_FAIXA_ANEXOS = range(1, 27)


def _revogada(tr) -> bool:
    """
    Redação antiga é marcada por classe CSS terminada em "verde", e a classe
    fica nos ``<p>``/``<td>`` internos — nunca na própria ``<tr>``.

    Não há ``<s>``/``<del>`` nem ``line-through`` no documento: a cor via
    classe é o único sinal. Raspar sem esse filtro importa 294 linhas de
    redação revogada como se fossem vigentes.
    """
    for elemento in tr.find_all(True):
        for classe in elemento.get("class") or []:
            if "verde" in classe.lower():
                return True
    return False


def ler_cest(caminho: Path) -> tuple[list[dict], str]:
    from bs4 import BeautifulSoup

    sopa = BeautifulSoup(caminho.read_text(encoding="utf-8", errors="replace"), "lxml")
    tabelas = sopa.find_all("table")

    registros: list[dict] = []
    for indice in _FAIXA_ANEXOS:
        if indice >= len(tabelas):
            break
        tabela = tabelas[indice]

        # O nome do segmento vem do texto anterior à tabela (título do anexo).
        titulo = ""
        anterior = tabela.find_previous(string=re.compile(r"ANEXO\s+[IVXLC]+", re.I))
        if anterior:
            titulo = _limpar(anterior)[:120]

        for tr in tabela.find_all("tr"):
            celulas = tr.find_all(["td", "th"])
            if len(celulas) <= 2:
                continue  # nota de remissão ou linha "REVOGADO"
            if _revogada(tr):
                continue

            textos = [_limpar(c.get_text(" ", strip=True)) for c in celulas]
            if textos[0].upper() == "ITEM" and textos[1].upper() == "CEST":
                continue  # o cabeçalho reaparece no meio de algumas tabelas
            if not any(textos):
                continue
            cest = textos[1]
            if not re.fullmatch(r"\d{2}\.\d{3}\.\d{2}", cest):
                continue  # inclusive as linhas com "REVOGADO" no lugar do código

            # A célula de NCM traz vários códigos, separados ora por <p>,
            # ora por espaço — às vezes os dois na mesma célula.
            bruto = celulas[2]
            partes = [p.get_text(" ", strip=True) for p in bruto.find_all("p")] or [
                bruto.get_text(" ", strip=True)
            ]
            descricao = _limpar(" ".join(textos[3:]))

            for parte in partes:
                for token in _limpar(parte).split():
                    prefixo = so_digitos(token.rstrip(",."))
                    if 2 <= len(prefixo) <= 8:
                        registros.append(
                            {
                                "codigo": cest,
                                "ncm_prefixo": prefixo,
                                "anexo": f"T{indice}",
                                "segmento": titulo,
                                "descricao": descricao,
                            }
                        )

    return registros, "Convênio ICMS 142/2018"


# --------------------------------------------------------------------------- #
#  CFOP e FCP
# --------------------------------------------------------------------------- #
def ler_cfop(caminho: Path) -> tuple[list[dict], str]:
    """
    A planilha tem 1.026 colunas fantasma de formatação; sem ``max_col`` o
    openpyxl devolve centenas de ``None`` por linha.
    """
    from openpyxl import load_workbook

    wb = load_workbook(caminho, data_only=True, read_only=True)
    ws = wb["CFOP"]

    registros = []
    for linha in ws.iter_rows(min_row=2, max_col=11, values_only=True):
        codigo = linha[0]
        if codigo is None:
            continue
        inicio = linha[1]
        registros.append(
            {
                "codigo": str(codigo).strip(),
                "valido_nfe": bool(linha[3]),
                "inicio_vigencia": inicio.date() if hasattr(inicio, "date") else None,
            }
        )
    wb.close()
    return registros, "Tabela CFOP — Portal Nacional da NF-e"


def ler_fcp(caminho: Path) -> tuple[list[dict], str]:
    """
    A alíquota vem como texto ``"Fixo:2.00"`` ou ``"Max:4.00"`` — a distinção
    importa: com teto só dá para apontar quando o valor passa dele.
    """
    from openpyxl import load_workbook

    wb = load_workbook(caminho, data_only=True, read_only=True)
    ws = wb["FCP"]

    def _faixa(valor) -> tuple[str, Decimal] | None:
        if not valor or ":" not in str(valor):
            return None
        rotulo, numero = str(valor).split(":", 1)
        try:
            return rotulo.strip().lower(), Decimal(numero.strip())
        except Exception:  # noqa: BLE001
            return None

    registros = []
    for linha in ws.iter_rows(min_row=2, max_col=8, values_only=True):
        # As linhas de nota no rodapé não têm código de UF numérico.
        if not isinstance(linha[0], int):
            continue
        principal = _faixa(linha[3])
        if principal is None:
            continue
        rotulo, valor = principal
        alternativa = _faixa(linha[4])
        registros.append(
            {
                "uf": _limpar(linha[1]),
                "nome_uf": _limpar(linha[2]),
                "tipo": "maximo" if rotulo.startswith("max") else "fixo",
                "aliquota": valor,
                "aliquota_alternativa": alternativa[1] if alternativa else None,
                "observacao": _limpar(linha[7] or ""),
            }
        )
    wb.close()
    return registros, "Tabela de alíquotas do FCP — Portal Nacional da NF-e"
