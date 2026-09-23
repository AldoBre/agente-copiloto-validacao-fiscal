"""
Anonimização do que sai para o provedor de IA.

**Por que existe.** O prompt do agente proíbe reproduzir dado pessoal, mas
prompt não é controle de segurança: um modelo pode desobedecer, um filtro no
código não. Aqui é a última fronteira antes do texto atravessar para um serviço
de terceiros — o que passar daqui saiu do nosso controle.

**Onde é aplicado.** Só no relatório que vai para o modelo (``no_preparar``).
O relatório que o consultor lê na tela e baixa em PDF continua com os dados
reais: ele é o operador legítimo daquela informação. Mascarar ali só atrapalharia
o trabalho dele.

**Por que importa mesmo com o escopo fiscal.** Hoje o comparador roda em
``ESCOPO=impostos``, que não emite CPF/CNPJ — auditado. Mas
``COMPARADOR_ESCOPO=completo`` existe, é uma variável de ambiente, e nesse modo
o relatório inclui destinatário e emitente. Um filtro que depende do escopo
configurado é um filtro que falha no dia em que alguém mudar o escopo.

**O mascaramento preserva correlação.** Trocamos o identificador por uma forma
estável (mesmo documento → mesma máscara), então o modelo continua conseguindo
dizer "as duas notas são do mesmo destinatário" sem nunca ver quem ele é.
"""
from __future__ import annotations

import re

# A ordem das substituições importa: a chave de acesso tem 44 dígitos e contém
# um CNPJ embutido. Se o CNPJ rodasse primeiro, ele picotaria a chave no meio.
_RE_CHAVE = re.compile(r"\b\d{44}\b")
_RE_CNPJ_FORMATADO = re.compile(r"\b\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}\b")
_RE_CNPJ_CRU = re.compile(r"(?<!\d)\d{14}(?!\d)")
_RE_CPF_FORMATADO = re.compile(r"\b\d{3}\.\d{3}\.\d{3}-\d{2}\b")
_RE_CPF_CRU = re.compile(r"(?<!\d)\d{11}(?!\d)")
_RE_EMAIL = re.compile(r"\b[\w.+-]+@[\w-]+\.[\w.-]{2,}\b")
_RE_IE = re.compile(r"(?i)\b(inscri[çc][ãa]o estadual|\bIE\b)\s*[:=]\s*([\d.\-/]{6,20})")

_APENAS_DIGITOS = re.compile(r"\D")


def _mascarar_cnpj(encontrado: re.Match) -> str:
    """Preserva filial e dígito verificador; some com a raiz, que é quem identifica."""
    digitos = _APENAS_DIGITOS.sub("", encontrado.group(0))
    return f"**.***.***/{digitos[8:12]}-{digitos[12:]}"


def _mascarar_cpf(encontrado: re.Match) -> str:
    digitos = _APENAS_DIGITOS.sub("", encontrado.group(0))
    return f"***.***.***-{digitos[9:]}"


def _mascarar_chave(encontrado: re.Match) -> str:
    """Mantém os 6 últimos: dá para casar duas menções à mesma nota, e só."""
    return f"{'*' * 38}{encontrado.group(0)[38:]}"


def _mascarar_email(encontrado: re.Match) -> str:
    dominio = encontrado.group(0).split("@", 1)[1]
    return f"***@{dominio}"


def mascarar(texto: str) -> str:
    """
    Remove identificadores pessoais/empresariais de um texto.

    Trata CPF, CNPJ (com e sem formatação), chave de acesso da NF-e, e-mail e
    inscrição estadual. Nome e razão social **não** são detectáveis por regex —
    o controle contra eles é o escopo do comparador, que não os coleta.
    """
    if not texto:
        return texto

    texto = _RE_CHAVE.sub(_mascarar_chave, texto)
    texto = _RE_CNPJ_FORMATADO.sub(_mascarar_cnpj, texto)
    texto = _RE_CNPJ_CRU.sub(_mascarar_cnpj, texto)
    texto = _RE_CPF_FORMATADO.sub(_mascarar_cpf, texto)
    texto = _RE_CPF_CRU.sub(_mascarar_cpf, texto)
    texto = _RE_EMAIL.sub(_mascarar_email, texto)
    texto = _RE_IE.sub(lambda m: f"{m.group(1)}: ***", texto)
    return texto


def encontrar_dados_pessoais(texto: str) -> list[str]:
    """
    Devolve os identificadores achados no texto. Só para auditoria e teste —
    o fluxo normal usa :func:`mascarar`.
    """
    achados: list[str] = []
    for regex in (
        _RE_CHAVE,
        _RE_CNPJ_FORMATADO,
        _RE_CNPJ_CRU,
        _RE_CPF_FORMATADO,
        _RE_CPF_CRU,
        _RE_EMAIL,
    ):
        achados.extend(regex.findall(texto or ""))
    return achados
