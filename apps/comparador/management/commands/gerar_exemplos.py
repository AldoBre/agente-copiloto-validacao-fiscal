"""
Gera dois XMLs de NF-e fictícios com divergências propositais, para testar o
comparador sem depender de arquivos reais do cliente.

    python manage.py gerar_exemplos

Cria ``exemplos/nfe_sistema_atual.xml`` e ``exemplos/nfe_senior.xml``.

Divergências plantadas:
  * item 1 — CST de ICMS 00 x 20 + redução de base só na Senior (regra diferente)
  * item 1 — alíquota de ICMS 18% x 12%
  * item 2 — NCM divergente e CFOP 5102 x 6102
  * item 2 — CST de PIS/COFINS 01 x 49
  * item 3 — existe só no XML do cliente (produto não migrado)
  * totais — vNF divergente por consequência
"""
from __future__ import annotations

from pathlib import Path

from django.core.management.base import BaseCommand

CABECALHO = """<?xml version="1.0" encoding="UTF-8"?>
<nfeProc xmlns="http://www.portalfiscal.inf.br/nfe" versao="4.00">
  <NFe>
    <infNFe Id="NFe{chave}" versao="4.00">
      <ide>
        <cUF>42</cUF><cNF>{cnf}</cNF>
        <natOp>{natop}</natOp>
        <mod>55</mod><serie>1</serie><nNF>{nnf}</nNF>
        <dhEmi>2026-07-20T09:00:00-03:00</dhEmi>
        <tpNF>1</tpNF><idDest>{iddest}</idDest><cMunFG>4204202</cMunFG>
        <tpImp>1</tpImp><tpEmis>1</tpEmis><cDV>0</cDV><tpAmb>2</tpAmb>
        <finNFe>1</finNFe><indFinal>{indfinal}</indFinal><indPres>1</indPres>
        <procEmi>0</procEmi><verProc>{verproc}</verProc>
      </ide>
      <emit>
        <CNPJ>03600477000104</CNPJ>
        <xNome>INDUSTRIA EXEMPLO LTDA</xNome>
        <enderEmit><UF>SC</UF><cMun>4204202</cMun><xMun>Concordia</xMun></enderEmit>
        <IE>255123456</IE><CRT>3</CRT>
      </emit>
      <dest>
        <CNPJ>11222333000181</CNPJ>
        <xNome>COMERCIO CLIENTE LTDA</xNome>
        <enderDest><UF>{ufdest}</UF><cMun>4106902</cMun><xMun>Curitiba</xMun></enderDest>
        <indIEDest>{indiedest}</indIEDest><IE>9012345678</IE>
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
          <NCM>{ncm}</NCM><CEST>{cest}</CEST><CFOP>{cfop}</CFOP>
          <uCom>UN</uCom><qCom>{qcom}</qCom><vUnCom>{vuncom}</vUnCom>
          <vProd>{vprod}</vProd>
          <cEANTrib>SEM GTIN</cEANTrib><uTrib>UN</uTrib>
          <qTrib>{qcom}</qTrib><vUnTrib>{vuncom}</vUnTrib>
          <indTot>1</indTot>
        </prod>
        <imposto>
          <vTotTrib>{vtottrib}</vTotTrib>
          <ICMS>{icms}</ICMS>
          <IPI>
            <cEnq>999</cEnq>
            <IPITrib><CST>50</CST><vBC>{vprod}</vBC><pIPI>{pipi}</pIPI><vIPI>{vipi}</vIPI></IPITrib>
          </IPI>
          <PIS>
            <PISAliq><CST>{cstpis}</CST><vBC>{vprod}</vBC><pPIS>1.65</pPIS><vPIS>{vpis}</vPIS></PISAliq>
          </PIS>
          <COFINS>
            <COFINSAliq><CST>{cstcofins}</CST><vBC>{vprod}</vBC><pCOFINS>7.60</pCOFINS><vCOFINS>{vcofins}</vCOFINS></COFINSAliq>
          </COFINS>
        </imposto>
      </det>
"""

ICMS_00 = (
    "<ICMS00><orig>0</orig><CST>00</CST><modBC>3</modBC>"
    "<vBC>{vbc}</vBC><pICMS>{picms}</pICMS><vICMS>{vicms}</vICMS></ICMS00>"
)
ICMS_20 = (
    "<ICMS20><orig>0</orig><CST>20</CST><modBC>3</modBC><pRedBC>{pred}</pRedBC>"
    "<vBC>{vbc}</vBC><pICMS>{picms}</pICMS><vICMS>{vicms}</vICMS></ICMS20>"
)


class Command(BaseCommand):
    help = "Gera dois XMLs de NF-e de exemplo com divergências fiscais propositais."

    def add_arguments(self, parser):
        parser.add_argument(
            "--destino", default="exemplos", help="Pasta de saída (padrão: ./exemplos)"
        )

    def handle(self, *args, **opcoes):
        destino = Path(opcoes["destino"])
        destino.mkdir(parents=True, exist_ok=True)

        # ---------------------------------------------------------- CLIENTE --
        itens_cliente = [
            ITEM.format(
                n=1,
                cprod="PRD-001",
                xprod="CHAPA DE ACO GALVANIZADO 2MM",
                ncm="72104900",
                cest="",
                cfop="6102",
                qcom="10.0000",
                vuncom="150.0000",
                vprod="1500.00",
                vtottrib="420.00",
                icms=ICMS_00.format(vbc="1500.00", picms="12.00", vicms="180.00"),
                pipi="5.00",
                vipi="75.00",
                cstpis="01",
                vpis="24.75",
                cstcofins="01",
                vcofins="114.00",
            ),
            ITEM.format(
                n=2,
                cprod="PRD-002",
                xprod="PARAFUSO SEXTAVADO M8",
                ncm="73181500",
                cest="",
                cfop="6102",
                qcom="500.0000",
                vuncom="1.2000",
                vprod="600.00",
                vtottrib="168.00",
                icms=ICMS_00.format(vbc="600.00", picms="12.00", vicms="72.00"),
                pipi="5.00",
                vipi="30.00",
                cstpis="01",
                vpis="9.90",
                cstcofins="01",
                vcofins="45.60",
            ),
            ITEM.format(
                n=3,
                cprod="PRD-003",
                xprod="ARRUELA LISA 8MM",
                ncm="73182200",
                cest="",
                cfop="6102",
                qcom="200.0000",
                vuncom="0.5000",
                vprod="100.00",
                vtottrib="28.00",
                icms=ICMS_00.format(vbc="100.00", picms="12.00", vicms="12.00"),
                pipi="5.00",
                vipi="5.00",
                cstpis="01",
                vpis="1.65",
                cstcofins="01",
                vcofins="7.60",
            ),
        ]
        xml_cliente = (
            CABECALHO.format(
                chave="42260703600477000104550010000012341000012349",
                cnf="00001234",
                nnf="1234",
                natop="VENDA DE PRODUCAO DO ESTABELECIMENTO",
                iddest="2",
                indfinal="0",
                verproc="SistemaAtual 9.2",
                ufdest="PR",
                indiedest="1",
            )
            + "".join(itens_cliente)
            + RODAPE.format(
                vbc="2200.00",
                vicms="264.00",
                vprod="2200.00",
                vipi="110.00",
                vpis="36.30",
                vcofins="167.20",
                vnf="2310.00",
                vtottrib="616.00",
            )
        )

        # ----------------------------------------------------------- SENIOR --
        itens_senior = [
            ITEM.format(
                n=1,
                cprod="PRD-001",
                xprod="CHAPA DE ACO GALVANIZADO 2MM",
                ncm="72104900",
                cest="",
                cfop="6102",
                qcom="10.0000",
                vuncom="150.0000",
                vprod="1500.00",
                vtottrib="420.00",
                # DIVERGÊNCIA: regra ICMS20 (redução de base) + alíquota 18%
                icms=ICMS_20.format(
                    pred="33.33", vbc="1000.05", picms="18.00", vicms="180.01"
                ),
                pipi="5.00",
                vipi="75.00",
                cstpis="01",
                vpis="24.75",
                cstcofins="01",
                vcofins="114.00",
            ),
            ITEM.format(
                n=2,
                cprod="PRD-002",
                xprod="PARAFUSO SEXTAVADO M8",
                # DIVERGÊNCIA: NCM e CFOP
                ncm="73181900",
                cest="",
                cfop="5102",
                qcom="500.0000",
                vuncom="1.2000",
                vprod="600.00",
                vtottrib="168.00",
                icms=ICMS_00.format(vbc="600.00", picms="12.00", vicms="72.00"),
                pipi="5.00",
                vipi="30.00",
                # DIVERGÊNCIA: CST de PIS/COFINS
                cstpis="49",
                vpis="0.00",
                cstcofins="49",
                vcofins="0.00",
            ),
            # DIVERGÊNCIA: item 3 (PRD-003) não existe na Senior.
        ]
        xml_senior = (
            CABECALHO.format(
                chave="42260703600477000104550010000056781000056789",
                cnf="00005678",
                nnf="5678",
                natop="VENDA DE PRODUCAO DO ESTABELECIMENTO",
                iddest="2",
                indfinal="0",
                verproc="Senior ERP",
                ufdest="PR",
                indiedest="1",
            )
            + "".join(itens_senior)
            + RODAPE.format(
                vbc="1600.05",
                vicms="252.01",
                vprod="2100.00",
                vipi="105.00",
                vpis="24.75",
                vcofins="114.00",
                vnf="2205.00",
                vtottrib="588.00",
            )
        )

        caminho_cliente = destino / "nfe_sistema_atual.xml"
        caminho_senior = destino / "nfe_senior.xml"
        caminho_cliente.write_text(xml_cliente, encoding="utf-8")
        caminho_senior.write_text(xml_senior, encoding="utf-8")

        self.stdout.write(self.style.SUCCESS(f"Gerado: {caminho_cliente}"))
        self.stdout.write(self.style.SUCCESS(f"Gerado: {caminho_senior}"))
        self.stdout.write(
            "\nSuba os dois na tela inicial e clique em 'Comparar XMLs'.\n"
            "Divergências plantadas: regra e alíquota de ICMS (item 1), NCM/CFOP e "
            "CST de PIS/COFINS (item 2), item PRD-003 ausente na Senior, e os totais."
        )
