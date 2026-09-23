"""
Gera dois ZIPs com N notas cada, para testar a comparação em massa.

    python manage.py gerar_lote_exemplo --quantidade 100

Cria ``exemplos/lote_sistema_atual.zip`` e ``exemplos/lote_senior.zip``.

As divergências são **sistemáticas**, como numa implantação real — é isso que o
relatório consolidado precisa evidenciar:

  * todo produto de NCM 7210xxxx sai com CST 20 + redução de base no Senior
    (no cliente é CST 00) e alíquota 18% em vez de 12%;
  * o produto PRD-005 está com NCM errado no cadastro do Senior;
  * ~15% das notas saem com CST de PIS/COFINS 49 em vez de 01;
  * algumas notas perdem um item (produto não migrado);
  * algumas notas existem só de um lado (operação não emitida no Senior e
    vice-versa).
"""
from __future__ import annotations

import random
import zipfile
from pathlib import Path

from django.core.management.base import BaseCommand

CLIENTES = [
    ("11222333000181", "COMERCIO ALFA LTDA", "PR", "4106902", "1"),
    ("22333444000172", "DISTRIBUIDORA BETA SA", "SP", "3550308", "1"),
    ("33444555000163", "MERCADO GAMA EIRELI", "RS", "4314902", "1"),
    ("44555666000154", "ATACADO DELTA LTDA", "SC", "4205407", "1"),
    ("55666777000145", "VAREJO EPSILON ME", "MG", "3106200", "2"),
]

# (código, descrição, NCM, unidade, valor unitário, alíquota IPI)
PRODUTOS = [
    ("PRD-001", "CHAPA DE ACO GALVANIZADO 2MM", "72104900", 150.00, "5.00"),
    ("PRD-002", "PARAFUSO SEXTAVADO M8", "73181500", 1.20, "5.00"),
    ("PRD-003", "ARRUELA LISA 8MM", "73182200", 0.50, "5.00"),
    ("PRD-004", "BOBINA DE ACO LAMINADO", "72104100", 890.00, "5.00"),
    ("PRD-005", "PORCA SEXTAVADA M8", "73181600", 0.80, "5.00"),
    ("PRD-006", "CANTONEIRA DE ACO 50X50", "72169100", 42.00, "5.00"),
    ("PRD-007", "TUBO DE ACO CARBONO 1POL", "73063000", 68.00, "5.00"),
    ("PRD-008", "GRAMPO DE FIXACAO", "73269090", 3.40, "5.00"),
]

# NCM errado no cadastro do Senior para o PRD-005
NCM_ERRADO_SENIOR = {"PRD-005": "73181900"}

CABECALHO = """<?xml version="1.0" encoding="UTF-8"?>
<nfeProc xmlns="http://www.portalfiscal.inf.br/nfe" versao="4.00">
  <NFe>
    <infNFe Id="NFe{chave}" versao="4.00">
      <ide>
        <cUF>42</cUF><cNF>{cnf}</cNF>
        <natOp>VENDA DE PRODUCAO DO ESTABELECIMENTO</natOp>
        <mod>55</mod><serie>{serie}</serie><nNF>{nnf}</nNF>
        <dhEmi>{data}T09:00:00-03:00</dhEmi>
        <tpNF>1</tpNF><idDest>2</idDest><cMunFG>4204202</cMunFG>
        <tpImp>1</tpImp><tpEmis>1</tpEmis><cDV>0</cDV><tpAmb>2</tpAmb>
        <finNFe>1</finNFe><indFinal>0</indFinal><indPres>1</indPres>
        <procEmi>0</procEmi><verProc>{verproc}</verProc>
      </ide>
      <emit>
        <CNPJ>03600477000104</CNPJ>
        <xNome>INDUSTRIA EXEMPLO LTDA</xNome>
        <enderEmit><UF>SC</UF><cMun>4204202</cMun><xMun>Concordia</xMun></enderEmit>
        <IE>255123456</IE><CRT>3</CRT>
      </emit>
      <dest>
        <CNPJ>{dest_cnpj}</CNPJ>
        <xNome>{dest_nome}</xNome>
        <enderDest><UF>{dest_uf}</UF><cMun>{dest_mun}</cMun><xMun>Cidade</xMun></enderDest>
        <indIEDest>{dest_ie}</indIEDest><IE>9012345678</IE>
      </dest>
"""

RODAPE = """      <total>
        <ICMSTot>
          <vBC>{vbc}</vBC><vICMS>{vicms}</vICMS><vICMSDeson>0.00</vICMSDeson>
          <vFCP>0.00</vFCP><vBCST>0.00</vBCST><vST>0.00</vST><vFCPST>0.00</vFCPST>
          <vProd>{vprod}</vProd><vFrete>0.00</vFrete><vSeg>0.00</vSeg><vDesc>0.00</vDesc>
          <vII>0.00</vII><vIPI>{vipi}</vIPI><vIPIDevol>0.00</vIPIDevol>
          <vPIS>{vpis}</vPIS><vCOFINS>{vcofins}</vCOFINS><vOutro>0.00</vOutro>
          <vNF>{vnf}</vNF><vTotTrib>{vtottrib}</vTotTrib>
        </ICMSTot>
      </total>
      <transp><modFrete>9</modFrete></transp>
    </infNFe>
  </NFe>
</nfeProc>
"""

ITEM = """      <det nItem="{n}">
        <prod>
          <cProd>{cprod}</cProd><cEAN>SEM GTIN</cEAN>
          <xProd>{xprod}</xProd>
          <NCM>{ncm}</NCM><CFOP>{cfop}</CFOP>
          <uCom>UN</uCom><qCom>{qcom}.0000</qCom><vUnCom>{vuncom:.4f}</vUnCom>
          <vProd>{vprod:.2f}</vProd>
          <cEANTrib>SEM GTIN</cEANTrib><uTrib>UN</uTrib>
          <qTrib>{qcom}.0000</qTrib><vUnTrib>{vuncom:.4f}</vUnTrib>
          <indTot>1</indTot>
        </prod>
        <imposto>
          <ICMS>{icms}</ICMS>
          <IPI>
            <cEnq>999</cEnq>
            <IPITrib><CST>50</CST><vBC>{vprod:.2f}</vBC><pIPI>{pipi}</pIPI><vIPI>{vipi:.2f}</vIPI></IPITrib>
          </IPI>
          <PIS>
            <PISAliq><CST>{cstpis}</CST><vBC>{vprod:.2f}</vBC><pPIS>1.65</pPIS><vPIS>{vpis:.2f}</vPIS></PISAliq>
          </PIS>
          <COFINS>
            <COFINSAliq><CST>{cstcofins}</CST><vBC>{vprod:.2f}</vBC><pCOFINS>7.60</pCOFINS><vCOFINS>{vcofins:.2f}</vCOFINS></COFINSAliq>
          </COFINS>
        </imposto>
      </det>
"""

ICMS_00 = (
    "<ICMS00><orig>0</orig><CST>00</CST><modBC>3</modBC>"
    "<vBC>{vbc:.2f}</vBC><pICMS>{picms}</pICMS><vICMS>{vicms:.2f}</vICMS></ICMS00>"
)
ICMS_20 = (
    "<ICMS20><orig>0</orig><CST>20</CST><modBC>3</modBC><pRedBC>33.33</pRedBC>"
    "<vBC>{vbc:.2f}</vBC><pICMS>{picms}</pICMS><vICMS>{vicms:.2f}</vICMS></ICMS20>"
)


def _montar_nota(nota, *, lado: str) -> str:
    """``lado`` = 'cliente' ou 'senior'."""
    partes = []
    tot = dict(vbc=0.0, vicms=0.0, vprod=0.0, vipi=0.0, vpis=0.0, vcofins=0.0)

    itens = nota["itens"]
    if lado == "senior" and nota["item_faltando"] and len(itens) > 1:
        itens = itens[:-1]  # produto não migrado

    for posicao, item in enumerate(itens, start=1):
        codigo, descricao, ncm, valor_unitario, pipi = item["produto"]
        quantidade = item["quantidade"]
        valor_produto = round(valor_unitario * quantidade, 2)

        if lado == "senior":
            ncm = NCM_ERRADO_SENIOR.get(codigo, ncm)

        # Divergência sistemática: NCM 7210* → o Senior aplica redução de base.
        aplica_reducao = lado == "senior" and ncm.startswith("7210")
        if aplica_reducao:
            base = round(valor_produto * (1 - 0.3333), 2)
            aliquota, corpo_icms = "18.00", ICMS_20
        else:
            base = valor_produto
            aliquota, corpo_icms = "12.00", ICMS_00
        valor_icms = round(base * float(aliquota) / 100, 2)

        # Divergência sistemática: PIS/COFINS zerados em parte das notas.
        if lado == "senior" and nota["pis_cofins_errado"]:
            cst_pis = cst_cofins = "49"
            valor_pis = valor_cofins = 0.0
        else:
            cst_pis = cst_cofins = "01"
            valor_pis = round(valor_produto * 0.0165, 2)
            valor_cofins = round(valor_produto * 0.076, 2)

        valor_ipi = round(valor_produto * float(pipi) / 100, 2)

        partes.append(
            ITEM.format(
                n=posicao,
                cprod=codigo,
                xprod=descricao,
                ncm=ncm,
                cfop=nota["cfop"],
                qcom=quantidade,
                vuncom=valor_unitario,
                vprod=valor_produto,
                icms=corpo_icms.format(vbc=base, picms=aliquota, vicms=valor_icms),
                pipi=pipi,
                vipi=valor_ipi,
                cstpis=cst_pis,
                vpis=valor_pis,
                cstcofins=cst_cofins,
                vcofins=valor_cofins,
            )
        )

        tot["vbc"] += base
        tot["vicms"] += valor_icms
        tot["vprod"] += valor_produto
        tot["vipi"] += valor_ipi
        tot["vpis"] += valor_pis
        tot["vcofins"] += valor_cofins

    valor_nf = tot["vprod"] + tot["vipi"]
    cnpj, nome, uf, municipio, indicador_ie = nota["cliente"]

    if lado == "cliente":
        numero, serie, versao = nota["numero_cliente"], "1", "SistemaAtual 9.2"
    else:
        numero, serie, versao = nota["numero_senior"], "2", "Senior ERP"

    chave = f"4226070360047700010455{serie.zfill(3)}{str(numero).zfill(9)}1{str(numero).zfill(8)}"[:44]

    return (
        CABECALHO.format(
            chave=chave,
            cnf=str(numero).zfill(8),
            serie=serie,
            nnf=numero,
            data=nota["data"],
            verproc=versao,
            dest_cnpj=cnpj,
            dest_nome=nome,
            dest_uf=uf,
            dest_mun=municipio,
            dest_ie=indicador_ie,
        )
        + "".join(partes)
        + RODAPE.format(
            vbc=f"{tot['vbc']:.2f}",
            vicms=f"{tot['vicms']:.2f}",
            vprod=f"{tot['vprod']:.2f}",
            vipi=f"{tot['vipi']:.2f}",
            vpis=f"{tot['vpis']:.2f}",
            vcofins=f"{tot['vcofins']:.2f}",
            vnf=f"{valor_nf:.2f}",
            vtottrib=f"{tot['vprod'] * 0.28:.2f}",
        )
    )


class Command(BaseCommand):
    help = "Gera dois ZIPs com N notas cada para testar a comparação em massa."

    def add_arguments(self, parser):
        parser.add_argument("--quantidade", type=int, default=100)
        parser.add_argument("--destino", default="exemplos")
        parser.add_argument("--semente", type=int, default=42)

    def handle(self, *args, **opcoes):
        aleatorio = random.Random(opcoes["semente"])
        quantidade = opcoes["quantidade"]
        destino = Path(opcoes["destino"])
        destino.mkdir(parents=True, exist_ok=True)

        notas = []
        for indice in range(quantidade):
            quantidade_itens = aleatorio.choice([1, 2, 2, 3, 3, 4])
            produtos = aleatorio.sample(PRODUTOS, quantidade_itens)
            notas.append(
                {
                    "numero_cliente": 1000 + indice,
                    "numero_senior": 5000 + indice,
                    "data": f"2026-07-{(indice % 28) + 1:02d}",
                    "cliente": aleatorio.choice(CLIENTES),
                    "cfop": "6102",
                    "itens": [
                        {"produto": p, "quantidade": aleatorio.choice([1, 2, 5, 10, 20, 50])}
                        for p in produtos
                    ],
                    "pis_cofins_errado": aleatorio.random() < 0.15,
                    "item_faltando": aleatorio.random() < 0.05,
                }
            )

        # Notas que existem só de um lado.
        somente_cliente = max(1, quantidade // 50)
        somente_senior = max(1, quantidade // 50)

        caminho_cliente = destino / "lote_sistema_atual.zip"
        caminho_senior = destino / "lote_senior.zip"

        with zipfile.ZipFile(caminho_cliente, "w", zipfile.ZIP_DEFLATED) as pacote:
            for indice, nota in enumerate(notas):
                if indice >= quantidade - somente_senior:
                    continue  # essas só existirão no Senior
                pacote.writestr(
                    f"NFe_{nota['numero_cliente']}.xml", _montar_nota(nota, lado="cliente")
                )

        with zipfile.ZipFile(caminho_senior, "w", zipfile.ZIP_DEFLATED) as pacote:
            for indice, nota in enumerate(notas):
                if indice < somente_cliente:
                    continue  # essas só existem no cliente
                pacote.writestr(
                    f"{nota['numero_senior']}-nfe.xml", _montar_nota(nota, lado="senior")
                )

        self.stdout.write(self.style.SUCCESS(f"Gerado: {caminho_cliente}"))
        self.stdout.write(self.style.SUCCESS(f"Gerado: {caminho_senior}"))
        self.stdout.write(
            f"\n{quantidade - somente_senior} nota(s) no ZIP do cliente, "
            f"{quantidade - somente_cliente} no ZIP do Senior.\n"
            f"{somente_cliente} nota(s) só no cliente e {somente_senior} só no Senior "
            "(para testar o tratamento de notas sem par).\n\n"
            "Suba os dois na aba 'Em massa' do painel."
        )
