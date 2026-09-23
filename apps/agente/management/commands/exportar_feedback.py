"""
Exporta as avaliações 👍/👎 como JSONL — a fundação para fine-tuning futuro.

    python manage.py exportar_feedback --saida feedback.jsonl
    python manage.py exportar_feedback --valor 1        # só os aprovados
    python manage.py exportar_feedback --formato revisao  # para ler os negativos

Dois formatos:

* ``chat`` (padrão) — ``{"messages": [{system}, {user}, {assistant}]}``, o
  formato que OpenAI e afins esperam para fine-tuning. Só faz sentido com os
  positivos (``--valor 1``): um dataset de treino não deve conter as respostas
  que o consultor reprovou.
* ``revisao`` — registro completo (pergunta, resposta, fontes, motivo,
  comentário) para leitura humana. É o que serve HOJE: ler os negativos e
  corrigir ``prompts.py`` ou as ``RegraParametrizacao``.

Por que não fine-tunar agora: a qualidade da resposta depende quase toda do
contexto recuperado pelo RAG, não do peso do modelo — um modelo ajustado
receberia o mesmo contexto e erraria igual. Além disso o provedor é trocável em
runtime, e fine-tuning amarra o produto a um. Este comando existe para que o
dado esteja pronto quando (e se) o volume justificar.
"""
from __future__ import annotations

import json
from pathlib import Path

from django.core.management.base import BaseCommand

from apps.agente.models import AvaliacaoMensagem

#: Resumo curto do papel do agente, usado como `system` no formato de
#: fine-tuning.
#:
#: **Não é o prompt real** — o SISTEMA de produção passa de 4 mil tokens e muda
#: com o tempo. Treinar com este resumo e servir com aquele produziria um modelo
#: ajustado para outra tarefa. Por isso cada registro carrega `versao_prompt`:
#: é o que permite ir buscar o prompt exato daquele momento
#: (`git show <sha>:apps/agente/prompts.py`) em vez de supor.
INSTRUCAO = (
    "Você é o agente fiscal de implantação do ERP Senior. A partir do relatório "
    "de divergências entre a nota do cliente e a do Senior, diga o que ajustar "
    "na parametrização, citando a tela do Senior e a documentação."
)


class Command(BaseCommand):
    help = "Exporta as avaliações das respostas do agente em JSONL."

    def add_arguments(self, parser):
        parser.add_argument("--saida", default="feedback.jsonl", help="Arquivo de saída.")
        parser.add_argument(
            "--valor",
            type=int,
            choices=[1, -1],
            help="Filtra por 1 (gostei) ou -1 (não gostei). Sem isto, exporta tudo.",
        )
        parser.add_argument(
            "--formato",
            choices=["chat", "revisao"],
            default="chat",
            help="'chat' para fine-tuning; 'revisao' para leitura humana.",
        )

    def handle(self, *args, **opcoes):
        consulta = AvaliacaoMensagem.objects.all().order_by("criado_em")
        if opcoes["valor"]:
            consulta = consulta.filter(valor=opcoes["valor"])

        destino = Path(opcoes["saida"])
        formato = opcoes["formato"]
        escritos = 0
        sem_pergunta = 0

        with destino.open("w", encoding="utf-8") as arquivo:
            for avaliacao in consulta:
                ctx = avaliacao.contexto or {}
                pergunta = (ctx.get("pergunta") or "").strip()
                resposta = (ctx.get("resposta") or "").strip()

                if formato == "chat":
                    # Par incompleto não treina nada — e polui o dataset.
                    if not pergunta or not resposta:
                        sem_pergunta += 1
                        continue
                    registro = {
                        "messages": [
                            {"role": "system", "content": INSTRUCAO},
                            {"role": "user", "content": pergunta},
                            {"role": "assistant", "content": resposta},
                        ],
                        "avaliacao": avaliacao.valor,
                        # Sem isto, um registro de hoje e um de seis meses atrás
                        # são indistinguíveis no arquivo — e o prompt mudou no
                        # meio. Ver apps/agente/versao.py.
                        "versao_prompt": ctx.get("versao_prompt", ""),
                    }
                else:
                    registro = {
                        "avaliacao": avaliacao.valor,
                        "motivo": avaliacao.motivo,
                        "comentario": avaliacao.comentario,
                        "pergunta": pergunta,
                        "resposta": resposta,
                        "fontes": ctx.get("fontes") or [],
                        "modelo": ctx.get("modelo") or "",
                        "versao_prompt": ctx.get("versao_prompt", ""),
                        "git_sha": ctx.get("git_sha", ""),
                        "lote_id": ctx.get("lote_id"),
                        "conversa_id": ctx.get("conversa_id"),
                        "criado_em": avaliacao.criado_em.isoformat(),
                    }

                arquivo.write(json.dumps(registro, ensure_ascii=False) + "\n")
                escritos += 1

        resumo = f"{escritos} registro(s) em {destino} (formato {formato})."
        if sem_pergunta:
            resumo += f" {sem_pergunta} descartado(s) por não ter par pergunta/resposta."
        if formato == "chat" and not opcoes["valor"]:
            resumo += " Atenção: sem --valor 1 o arquivo mistura respostas reprovadas."
        self.stdout.write(self.style.SUCCESS(resumo))
