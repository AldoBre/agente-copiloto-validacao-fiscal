"""
Extração segura dos XMLs enviados pelo consultor.

Aceita um ZIP ou vários .xml soltos. Protege contra:
  * *zip slip* — nomes com ``../`` ou caminho absoluto (só o basename é usado);
  * *zip bomb* — limite de arquivos e de bytes descompactados;
  * colisão de nome entre subpastas diferentes dentro do mesmo ZIP.
"""
from __future__ import annotations

import logging
import shutil
import zipfile
from dataclasses import dataclass
from pathlib import Path

logger = logging.getLogger(__name__)

LIMITE_ARQUIVOS = 1000
LIMITE_BYTES_TOTAL = 300 * 1024 * 1024  # 300 MB descompactados
LIMITE_BYTES_ARQUIVO = 20 * 1024 * 1024  # 20 MB por XML


class ErroDeExtracao(ValueError):
    pass


@dataclass
class ArquivoExtraido:
    nome: str
    caminho: Path
    tamanho: int


def _nome_unico(destino: Path, nome: str, usados: set[str]) -> str:
    base = Path(nome).name or "arquivo.xml"
    if base not in usados:
        return base
    caule, sufixo = (base.rsplit(".", 1) + [""])[:2]
    contador = 2
    while True:
        candidato = f"{caule}_{contador}.{sufixo}" if sufixo else f"{caule}_{contador}"
        if candidato not in usados:
            return candidato
        contador += 1


def extrair_zip(arquivo, destino: Path) -> list[ArquivoExtraido]:
    """Extrai apenas os .xml do ZIP para ``destino`` (achatando subpastas)."""
    destino.mkdir(parents=True, exist_ok=True)
    extraidos: list[ArquivoExtraido] = []
    usados: set[str] = set()

    try:
        with zipfile.ZipFile(arquivo) as pacote:
            entradas = [
                info
                for info in pacote.infolist()
                if not info.is_dir() and info.filename.lower().endswith(".xml")
            ]

            if not entradas:
                raise ErroDeExtracao("O ZIP não contém nenhum arquivo .xml.")
            if len(entradas) > LIMITE_ARQUIVOS:
                raise ErroDeExtracao(
                    f"O ZIP contém {len(entradas)} XMLs; o limite é {LIMITE_ARQUIVOS}."
                )

            total = sum(info.file_size for info in entradas)
            if total > LIMITE_BYTES_TOTAL:
                raise ErroDeExtracao(
                    f"Conteúdo descompactado de {total / 1_048_576:.0f} MB excede o limite "
                    f"de {LIMITE_BYTES_TOTAL // 1_048_576} MB."
                )

            for info in entradas:
                if info.file_size > LIMITE_BYTES_ARQUIVO:
                    logger.warning("Ignorando %s (%s bytes)", info.filename, info.file_size)
                    continue
                nome = _nome_unico(destino, info.filename, usados)
                usados.add(nome)
                caminho = destino / nome
                with pacote.open(info) as origem, open(caminho, "wb") as saida:
                    shutil.copyfileobj(origem, saida, length=64 * 1024)
                extraidos.append(ArquivoExtraido(nome=nome, caminho=caminho, tamanho=info.file_size))
    except zipfile.BadZipFile as exc:
        raise ErroDeExtracao(f"Arquivo ZIP inválido ou corrompido: {exc}") from exc

    return extraidos


def salvar_xmls(arquivos, destino: Path) -> list[ArquivoExtraido]:
    """Salva uma lista de uploads .xml (sem ZIP) em ``destino``."""
    destino.mkdir(parents=True, exist_ok=True)
    salvos: list[ArquivoExtraido] = []
    usados: set[str] = set()

    for enviado in arquivos:
        if not enviado.name.lower().endswith(".xml"):
            continue
        if enviado.size > LIMITE_BYTES_ARQUIVO:
            continue
        nome = _nome_unico(destino, enviado.name, usados)
        usados.add(nome)
        caminho = destino / nome
        with open(caminho, "wb") as saida:
            for pedaco in enviado.chunks():
                saida.write(pedaco)
        salvos.append(ArquivoExtraido(nome=nome, caminho=caminho, tamanho=enviado.size))

    if not salvos:
        raise ErroDeExtracao("Nenhum arquivo .xml válido foi enviado.")
    if len(salvos) > LIMITE_ARQUIVOS:
        raise ErroDeExtracao(f"{len(salvos)} XMLs enviados; o limite é {LIMITE_ARQUIVOS}.")
    return salvos


def receber_conjunto(upload_zip, uploads_xml, destino: Path) -> list[ArquivoExtraido]:
    """
    Aceita as duas formas de envio.

    ``upload_zip`` tem prioridade; se ausente, usa a lista ``uploads_xml``.
    """
    if upload_zip is not None:
        nome = (upload_zip.name or "").lower()
        if nome.endswith(".zip"):
            return extrair_zip(upload_zip, destino)
        if nome.endswith(".xml"):
            return salvar_xmls([upload_zip], destino)
        raise ErroDeExtracao(f"Formato não suportado: {upload_zip.name}. Envie .zip ou .xml.")
    if uploads_xml:
        return salvar_xmls(uploads_xml, destino)
    raise ErroDeExtracao("Nenhum arquivo recebido.")
