"""
Grafo do agente fiscal (LangGraph).

    preparar → recuperar → montar_prompt → responder ⇄ ferramentas
                                                ↓
                                               END

* **preparar** carrega o relatório da comparação anexada e extrai os campos
  divergentes (usados para buscar as regras certas).
* **recuperar** faz a busca híbrida na base de conhecimento + regras cadastradas.
* **montar_prompt** costura sistema + contexto + histórico + pergunta.
* **responder** chama o modelo em modo streaming.
* **ferramentas** executa as consultas que o modelo pediu e devolve a ele.

A camada HTTP consome ``astream_events`` para transmitir os tokens em tempo real
e as fontes assim que o nó de recuperação termina.

## Por que o ciclo responder ⇄ ferramentas termina

A recuperação de ``recuperar`` acontece **antes** de o modelo ler a pergunta,
com consultas derivadas das divergências. Isso resolve o primeiro turno e falha
no segundo: perguntado sobre outro assunto, o modelo não tem como ir buscar. O
ciclo com ferramentas resolve — desde que pare.

Ele para por construção, sem depender do bom senso do modelo: as ferramentas só
são oferecidas enquanto ``passos_ferramenta < MAX_PASSOS_FERRAMENTA``. No passo
do teto, ``responder`` roda **sem** ferramentas ligadas; sem elas o modelo não
tem como pedir mais nada e só lhe resta responder. Nenhuma aresta condicional
depende de o modelo "decidir encerrar".
"""
from __future__ import annotations

import logging
from typing import Any, TypedDict

from asgiref.sync import sync_to_async
from django.conf import settings
from langchain_core.messages import (
    AIMessage,
    BaseMessage,
    HumanMessage,
    SystemMessage,
    ToolMessage,
)
from langgraph.graph import END, START, StateGraph

from apps.provedores.factory import (
    ProvedorIndisponivel,
    construir_chat,
    recusar_extra_citado_no_erro,
)
from apps.provedores.models import ProvedorIA, TipoModelo

from . import ferramentas as ferr
from . import prompts
from .privacidade import mascarar

logger = logging.getLogger(__name__)

NOME_NO_RECUPERAR = "recuperar"
NOME_NO_RESPONDER = "responder"
NOME_NO_FERRAMENTAS = "ferramentas"


class EstadoAgente(TypedDict, total=False):
    # entrada
    pergunta: str
    conversa_id: str
    comparacao_id: str | None
    lote_id: str | None
    provedor_id: int | None
    historico: list[BaseMessage]
    #: Frase do botão que originou a mensagem, vazia quando o consultor digitou.
    #: É o que separa "analise o lote" de uma pergunta — ver `_analise_do_lote`.
    rotulo: str
    # derivado
    #
    # ⚠️ Toda chave que trafega entre nós precisa estar declarada AQUI. O
    # StateGraph só propaga os canais que conhece e **descarta o resto sem
    # erro nenhum** — 'causas' ficou de fora numa primeira versão e o nó de
    # recuperação recebia lista vazia, caía na pergunta genérica e devolvia
    # "não localizado na documentação" para quase tudo. Testar os nós soltos
    # não pega: só o grafo compilado filtra.
    relatorio: str
    campos_divergentes: list[str]
    causas: list[dict[str, str]]
    resumo_comparacao: dict[str, Any]
    contexto: list[dict[str, Any]]
    regras: list[dict[str, Any]]
    imagens: dict[str, str]
    mensagens: list[BaseMessage]
    #: Quantas rodadas de ferramentas já rodaram neste turno. É o que garante a
    #: parada do ciclo — ver o cabeçalho do módulo.
    passos_ferramenta: int
    #: Fontes descobertas pela busca documental durante o ciclo, para a UI somar
    #: às da recuperação inicial. Separado de `contexto` de propósito: `contexto`
    #: é o que foi para o prompt, e `montar_prompt` não roda de novo no ciclo.
    fontes_extras: list[dict[str, Any]]
    # saída
    resposta: str
    modelo_usado: str
    erro: str


# --------------------------------------------------------------------------- #
#  Acesso ao banco (sync → async)
# --------------------------------------------------------------------------- #
@sync_to_async
def _carregar_contexto_fiscal(
    comparacao_id: str | None, lote_id: str | None
) -> dict[str, Any]:
    """
    Carrega o relatório que serve de contexto — de um **lote** (comparação em
    massa) ou de uma **comparação** nota a nota. O lote tem prioridade: é o
    contexto mais informativo quando existe.
    """
    from apps.comparador.models import Comparacao, DivergenciaRegistrada, Lote

    if lote_id:
        try:
            lote = Lote.objects.get(pk=lote_id)
        except (Lote.DoesNotExist, ValueError, TypeError):
            lote = None

        if lote is not None and lote.relatorio_markdown:
            causas = list(
                DivergenciaRegistrada.objects.filter(comparacao__lote_id=lote.pk)
                .exclude(severidade="baixa")
                .values_list("grupo", "campo", "tipo")
                .distinct()[:80]
            )
            return {
                "relatorio": lote.relatorio_markdown,
                "campos_divergentes": [
                    f"{g}.{c}" if g else c for g, c, _ in causas
                ],
                "causas": [{"grupo": g, "campo": c, "tipo": t} for g, c, t in causas],
                "resumo_comparacao": lote.resumo or {},
            }

    if not comparacao_id:
        return {}

    try:
        comparacao = Comparacao.objects.get(pk=comparacao_id)
    except (Comparacao.DoesNotExist, ValueError, TypeError):
        return {}

    divergencias = comparacao.resultado.get("divergencias", [])
    campos: list[str] = []
    causas: list[dict[str, str]] = []
    for d in divergencias:
        grupo = d.get("grupo") or ""
        campo = d.get("campo") or ""
        chave = f"{grupo}.{campo}" if grupo else campo
        if chave and chave not in campos:
            campos.append(chave)
            causas.append({"grupo": grupo, "campo": campo, "tipo": d.get("tipo") or ""})

    return {
        "relatorio": comparacao.relatorio_markdown,
        "campos_divergentes": campos,
        "causas": causas,
        "resumo_comparacao": comparacao.resumo or {},
    }


@sync_to_async
def _buscar_conhecimento(
    consultas: list[str], pergunta: str, campos: list[str], teto: int
) -> dict[str, Any]:
    """
    Recupera a documentação de **cada causa separadamente**.

    ``consultas`` já vem em frase nominal (ver ``consulta_de_parametrizacao``),
    uma por causa; o resultado carrega o assunto de cada trecho para que o prompt
    consiga dizer "esta documentação responde a esta divergência".

    ``pergunta`` entra como consulta extra, mas **com uma vaga só** quando há
    causas: frases de gatilho ("Analise as divergências", "como arrumo isso?")
    não têm termo fiscal nenhum e recuperam ruído — medido, comiam 3 das 16
    vagas com artigos de SPED Contábil e casas decimais. Sem causas, ela é a
    única pista que existe e leva o orçamento inteiro.
    """
    from apps.conhecimento.services.imagens import trocar_por_marcadores
    from apps.conhecimento.services.retriever import buscar_por_consultas, buscar_regras

    todas = [*consultas, pergunta] if pergunta else list(consultas)
    # A cota da pergunta é aplicada DENTRO do rodízio: aparar depois deixaria
    # trechos reservados e descartados, bloqueados para as causas.
    limites = {pergunta: 1} if pergunta and consultas else {}
    por_consulta = buscar_por_consultas(todas, por_consulta=3, teto=teto, limites=limites)

    contexto: list[dict[str, Any]] = []
    imagens: dict[str, str] = {}
    for consulta, trechos in por_consulta.items():
        for trecho in trechos:
            dados = trecho.para_dicionario()
            # Os prints viram marcadores curtos ([[print:3]]) antes de irem ao
            # modelo — copiar URL de 90 caracteres é algo que ele simplesmente
            # não faz. Ver trocar_por_marcadores.
            dados["texto"], _ = trocar_por_marcadores(trecho.texto, imagens)
            dados["responde_a"] = "" if consulta == pergunta else consulta
            contexto.append(dados)

    return {
        "contexto": contexto,
        "regras": buscar_regras(campos),
        "imagens": imagens,
    }


@sync_to_async
def _obter_provedor(provedor_id: int | None) -> ProvedorIA | None:
    if provedor_id:
        provedor = ProvedorIA.objects.filter(pk=provedor_id, ativo=True).first()
        if provedor:
            return provedor
    return ProvedorIA.obter_padrao(TipoModelo.CHAT)


# --------------------------------------------------------------------------- #
#  Nós
# --------------------------------------------------------------------------- #
async def no_preparar(estado: EstadoAgente) -> dict[str, Any]:
    dados = await _carregar_contexto_fiscal(
        estado.get("comparacao_id"), estado.get("lote_id")
    )
    # Fronteira de saída: a partir daqui o texto vai para um provedor externo.
    # O relatório que o consultor lê na tela continua intacto — ver privacidade.py.
    return {
        "relatorio": mascarar(dados.get("relatorio", "")),
        "campos_divergentes": dados.get("campos_divergentes", []),
        "causas": dados.get("causas", []),
        "resumo_comparacao": dados.get("resumo_comparacao", {}),
    }


#: Teto de causas que viram consulta. Acima disso o prompt fica grande demais e
#: as causas da cauda longa costumam ser variações das primeiras.
MAX_CONSULTAS = 8


def _analise_do_lote(estado: EstadoAgente) -> bool:
    """
    Esta mensagem é o pedido de análise geral, ou uma pergunta do consultor?

    Quem responde é o ``rotulo``: ele só vem preenchido quando a mensagem partiu
    de um botão ("Analise as divergências"), e nesse caso o texto que chega como
    pergunta é a instrução longa que o front monta, não uma dúvida. Aí as causas
    do relatório são de fato a melhor fonte de busca que existe.

    **Por que não usar "tem histórico?" como sinal.** Erra nos dois sentidos: o
    consultor pode apertar o botão no décimo turno (e aí as causas DEVEM mandar),
    e pode digitar uma pergunta específica já na primeira mensagem.

    Numa pergunta digitada, buscar as 8 causas de novo custa caro e serve pouco.
    Medido na base real de 4.365 trechos: o bloco de documentação cai de 6.215
    para 977 tokens (-84%) e a busca de 259 ms para 26 ms, enquanto a pergunta
    do consultor sobe de 1 trecho para 3. Ele não fica sem o contexto do lote —
    **o relatório inteiro continua no prompt**, com todas as divergências; o que
    deixa de vir é a documentação pré-buscada de cada uma. Se o modelo precisar
    dela, chama `buscar_documentacao`, que traz 4 trechos sob demanda.
    """
    return bool((estado.get("rotulo") or "").strip())


async def no_recuperar(estado: EstadoAgente) -> dict[str, Any]:
    from apps.comparador.services.mapa_campos import consulta_de_parametrizacao

    teto = int(settings.AGENTE.get("TOP_K_CONTEXTO", 6))
    pergunta = (estado.get("pergunta") or "").strip()

    # Uma consulta POR CAUSA. Concatenar as causas num texto só produz um vetor
    # que não se parece com nenhum documento — medido: a busca junta devolvia
    # artigos de apuração e crítica de integração, e o agente respondia
    # "parâmetro não localizado" para todas as divergências.
    consultas: list[str] = []
    if _analise_do_lote(estado):
        for causa in estado.get("causas", [])[:MAX_CONSULTAS]:
            consulta = consulta_de_parametrizacao(
                causa.get("grupo", ""), causa.get("campo", ""), causa.get("tipo", "")
            )
            if consulta not in consultas:
                consultas.append(consulta)

    if not consultas and not pergunta:
        return {"contexto": [], "regras": []}

    # O teto de trechos cresce com o número de causas — 6 trechos não cobrem 8
    # causas —, mas com folga, não proporcionalmente.
    teto_efetivo = min(max(teto, len(consultas) * 2), 18)

    try:
        dados = await _buscar_conhecimento(
            consultas, pergunta, estado.get("campos_divergentes", [])[:25], teto_efetivo
        )
    except Exception as exc:  # noqa: BLE001
        logger.warning("Falha na recuperação de contexto: %s", exc)
        return {"contexto": [], "regras": []}
    return dados


async def no_montar_prompt(estado: EstadoAgente) -> dict[str, Any]:
    blocos: list[str] = []

    relatorio = estado.get("relatorio") or ""
    if relatorio:
        blocos.append(prompts.CONTEXTO_RELATORIO.format(relatorio=relatorio))
    else:
        blocos.append(prompts.SEM_COMPARACAO)

    regras_txt = prompts.formatar_regras(estado.get("regras", []))
    if regras_txt:
        blocos.append(prompts.CONTEXTO_REGRAS.format(regras=regras_txt))

    blocos.append(
        prompts.CONTEXTO_BASE.format(trechos=prompts.formatar_trechos(estado.get("contexto", [])))
    )

    mensagens: list[BaseMessage] = [
        SystemMessage(content=prompts.SISTEMA),
        SystemMessage(content="\n\n".join(blocos)),
    ]

    janela = int(settings.AGENTE.get("JANELA_HISTORICO", 12))
    mensagens.extend(estado.get("historico", [])[-janela:])
    mensagens.append(HumanMessage(content=estado.get("pergunta", "")))

    return {"mensagens": mensagens}


def _texto_de(conteudo: Any) -> str:
    """Texto puro de um conteúdo que pode vir como string ou blocos."""
    if isinstance(conteudo, list):  # blocos (Anthropic e afins)
        return "".join(b.get("text", "") for b in conteudo if isinstance(b, dict))
    return str(conteudo or "")


def _max_passos() -> int:
    return int(settings.AGENTE.get("MAX_PASSOS_FERRAMENTA", 4))


def _ferramentas_disponiveis(estado: EstadoAgente) -> list:
    """
    As ferramentas oferecidas nesta passada — vazio no passo do teto.

    Devolver vazio é o freio do ciclo: sem ferramenta ligada o modelo não tem
    como pedir mais consulta, e a passada seguinte é obrigatoriamente a resposta.
    """
    if not settings.AGENTE.get("FERRAMENTAS", True):
        return []
    if estado.get("passos_ferramenta", 0) >= _max_passos():
        return []
    return ferr.FERRAMENTAS


def _modelo_com_ferramentas(provedor: ProvedorIA, estado: EstadoAgente) -> Any:
    """O modelo de chat do provedor, já com as ferramentas desta passada ligadas."""
    modelo = construir_chat(provedor, streaming=True)
    disponiveis = _ferramentas_disponiveis(estado)
    if disponiveis:
        try:
            modelo = modelo.bind_tools(disponiveis)
        except (AttributeError, NotImplementedError, TypeError) as exc:
            # Nem todo provedor cadastrado suporta ferramentas. Perder a consulta
            # é aceitável; derrubar o chat de quem está no meio de uma
            # implantação não é.
            logger.warning(
                "O provedor %s não aceitou bind_tools (%s) — seguindo sem ferramentas.",
                provedor.nome,
                exc,
            )
    return modelo


async def no_responder(estado: EstadoAgente) -> dict[str, Any]:
    provedor = await _obter_provedor(estado.get("provedor_id"))
    if provedor is None:
        return {
            "erro": (
                "Nenhum provedor de IA ativo. Cadastre um modelo em **Configurações** "
                "e marque-o como padrão."
            ),
            "resposta": "",
        }

    try:
        modelo = _modelo_com_ferramentas(provedor, estado)
    except ProvedorIndisponivel as exc:
        return {"erro": str(exc), "resposta": ""}

    mensagens = list(estado.get("mensagens") or [])
    # O texto já emitido em passadas anteriores deste mesmo turno. O modelo pode
    # escrever antes de chamar a ferramenta, e esse pedaço já foi para a tela.
    anterior = estado.get("resposta") or ""

    acumulado = None
    for tentativa in (1, 2):
        acumulado = None
        try:
            async for pedaco in modelo.astream(mensagens):
                # A soma de chunks é o que reconstrói os `tool_calls`: eles chegam
                # fatiados em `tool_call_chunks` (JSON parcial) e só viram chamada
                # completa depois de somados.
                acumulado = pedaco if acumulado is None else acumulado + pedaco
            break
        except Exception as exc:  # noqa: BLE001
            # O provedor recusou um parâmetro que o CATÁLOGO mandou (ex.:
            # `reasoning_effort` numa api-version antiga do Azure)? Recusa de
            # parâmetro é HTTP 400 antes do primeiro byte — nada foi para a tela,
            # então repetir não duplica texto. Só uma vez, e só nesse caso.
            recusado = (
                recusar_extra_citado_no_erro(provedor, exc)
                if tentativa == 1 and acumulado is None
                else None
            )
            if recusado:
                logger.warning(
                    "%s recusou '%s' — seguindo sem ele até o processo reiniciar. "
                    "Tire do catálogo se for definitivo.",
                    provedor.nome,
                    recusado,
                )
                try:
                    modelo = _modelo_com_ferramentas(provedor, estado)
                    continue
                except ProvedorIndisponivel:
                    pass

            logger.exception("Falha ao chamar o modelo %s", provedor.nome)
            from apps.provedores.erros import explicar

            return {
                "erro": f"**{provedor.nome}** — {explicar(exc)}",
                "resposta": anterior + _texto_de(getattr(acumulado, "content", "")),
                "modelo_usado": f"{provedor.provedor}:{provedor.modelo}",
            }

    if acumulado is None:
        return {
            "resposta": anterior,
            "modelo_usado": f"{provedor.provedor}:{provedor.modelo}",
            "erro": "",
        }

    return {
        "mensagens": [*mensagens, acumulado],
        "resposta": anterior + _texto_de(acumulado.content),
        "modelo_usado": f"{provedor.provedor}:{provedor.modelo}",
        "erro": "",
    }


async def no_ferramentas(estado: EstadoAgente) -> dict[str, Any]:
    """
    Executa o lote de consultas que o modelo pediu e devolve o resultado a ele.

    Uma ferramenta que estoura vira ``ToolMessage`` de erro, não exceção: o
    modelo precisa receber **alguma** resposta para cada ``tool_call_id`` que
    emitiu — a API do provedor rejeita a rodada seguinte se sobrar chamada sem
    resposta —, e o texto do erro é instruído a ser tratado como "não sei", que
    é a única leitura honesta de uma consulta que não completou.
    """
    mensagens = list(estado.get("mensagens") or [])
    ultima = mensagens[-1] if mensagens else None
    chamadas = list(getattr(ultima, "tool_calls", None) or [])

    # A coleta precisa abrir aqui, na mesma task que executa as ferramentas, e
    # já com o registro de prints do turno — ver ferramentas.abrir_coleta.
    imagens = dict(estado.get("imagens") or {})
    coleta = ferr.abrir_coleta(imagens)

    respostas: list[BaseMessage] = []
    for chamada in chamadas:
        nome = chamada.get("name") or ""
        ferramenta = ferr.POR_NOME.get(nome)
        if ferramenta is None:
            conteudo = (
                f"A ferramenta '{nome}' não existe. Ferramentas disponíveis: "
                f"{', '.join(ferr.POR_NOME)}."
            )
        else:
            try:
                conteudo = str(await ferramenta.ainvoke(chamada.get("args") or {}))
            except Exception as exc:  # noqa: BLE001
                logger.exception("Falha ao executar a ferramenta %s", nome)
                conteudo = (
                    f"NAO_VERIFICADO — a consulta '{nome}' falhou "
                    f"({type(exc).__name__}). Trate como 'não foi possível conferir' "
                    f"e diga isso ao consultor; não conclua nada sobre este ponto."
                )
        respostas.append(
            ToolMessage(content=conteudo, tool_call_id=chamada.get("id") or "", name=nome)
        )

    return {
        "mensagens": [*mensagens, *respostas],
        "passos_ferramenta": estado.get("passos_ferramenta", 0) + 1,
        "imagens": imagens,
        "fontes_extras": [*(estado.get("fontes_extras") or []), *coleta["fontes"]],
    }


def _apos_responder(estado: EstadoAgente) -> str:
    """Tem consulta pendente? Vai executar. Senão, acabou."""
    mensagens = estado.get("mensagens") or []
    ultima = mensagens[-1] if mensagens else None
    return NOME_NO_FERRAMENTAS if getattr(ultima, "tool_calls", None) else END


# --------------------------------------------------------------------------- #
#  Compilação
# --------------------------------------------------------------------------- #
_grafo_compilado = None


def construir_grafo():
    """Compila (uma vez) e devolve o grafo do agente."""
    global _grafo_compilado
    if _grafo_compilado is not None:
        return _grafo_compilado

    grafo = StateGraph(EstadoAgente)
    grafo.add_node("preparar", no_preparar)
    grafo.add_node(NOME_NO_RECUPERAR, no_recuperar)
    grafo.add_node("montar_prompt", no_montar_prompt)
    grafo.add_node(NOME_NO_RESPONDER, no_responder)
    grafo.add_node(NOME_NO_FERRAMENTAS, no_ferramentas)

    grafo.add_edge(START, "preparar")
    grafo.add_edge("preparar", NOME_NO_RECUPERAR)
    grafo.add_edge(NOME_NO_RECUPERAR, "montar_prompt")
    grafo.add_edge("montar_prompt", NOME_NO_RESPONDER)
    grafo.add_conditional_edges(
        NOME_NO_RESPONDER,
        _apos_responder,
        {NOME_NO_FERRAMENTAS: NOME_NO_FERRAMENTAS, END: END},
    )
    grafo.add_edge(NOME_NO_FERRAMENTAS, NOME_NO_RESPONDER)

    _grafo_compilado = grafo.compile()
    return _grafo_compilado


#: Colado no fim de uma resposta que não terminou, antes de ela voltar ao
#: modelo no turno seguinte.
MARCA_INTERROMPIDA = (
    "\n\n[Nota do sistema: esta resposta foi INTERROMPIDA por uma falha antes de "
    "terminar. O texto acima pode estar cortado no meio. O consultor viu esta "
    "mesma versão incompleta, com um aviso de erro. Não trate o corte como uma "
    "escolha sua nem repita o que já está escrito — continue de onde parou se o "
    "consultor pedir.]"
)


def historico_para_mensagens(mensagens_db) -> list[BaseMessage]:
    """
    Converte ``Mensagem`` do Django em mensagens do LangChain.

    Uma resposta que morreu no meio do streaming é gravada com o texto parcial
    em ``conteudo`` e a falha em ``erro``. Sem tratar isso, ela voltava ao modelo
    no turno seguinte como fala completa e correta dele mesmo — uma tabela
    cortada no meio de uma linha vira "foi assim que eu respondi". O consultor vê
    o aviso de interrupção na tela; o modelo não via nada.

    **Por que marcar em vez de descartar.** A recomendação óbvia é filtrar por
    ``not m.erro``, e ela troca um desalinhamento por outro: `erro` também é
    gravado quando a falha aconteceu DEPOIS do texto ter saído inteiro, e nesses
    casos descartar joga fora resposta boa. Pior, o consultor viu aquele texto na
    tela — tirá-lo do histórico deixa modelo e consultor conversando sobre coisas
    diferentes, e o modelo tende a repetir o que já foi dito. Marcar custa o
    mesmo e diz a verdade: o texto existe, e foi cortado.
    """
    saida: list[BaseMessage] = []
    for m in mensagens_db:
        if m.papel == "usuario":
            saida.append(HumanMessage(content=m.conteudo))
        elif m.papel == "agente" and m.conteudo:
            conteudo = m.conteudo + MARCA_INTERROMPIDA if m.erro else m.conteudo
            saida.append(AIMessage(content=conteudo))
    return saida
