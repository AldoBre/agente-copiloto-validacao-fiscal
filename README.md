# Agente Copiloto de Validação Fiscal

Comparador de XML fiscal para a virada de ERP: confronta as notas que o cliente
emitia no sistema atual com as que o ERP Senior emite, lista as divergências de
imposto campo a campo e usa IA só para explicar onde corrigir a parametrização.

Sprint de IA do Grupo Assemble · StartSe × Senior · Canal Sancon, implantação.

> **Comece pelo [ANEXO_TECNICO.md](ANEXO_TECNICO.md)** (também em PDF): o que
> roda por trás, a fronteira entre código e IA, como rodar, como usar e o porquê
> de cada escolha de tecnologia.


## Tecnologias

| Camada | O quê |
|---|---|
| Linguagem | Python 3.12 |
| Web | Django 5.2, Django REST Framework, FastAPI (sub-app em `/api/ia`) |
| Servidor | Uvicorn (ASGI), WhiteNoise para estáticos |
| Banco | PostgreSQL 18 com pgvector (SQLite como alternativa sem infraestrutura) |
| IA / Agentes | LangChain, LangGraph |
| Provedores de IA | Anthropic, OpenAI, Google Gemini e Azure AI Foundry |
| Leitura de XML | lxml |
| Scraping da documentação | httpx, BeautifulSoup, markdownify |
| RAG | numpy, tiktoken |
| Segurança | cryptography (Fernet, para as chaves de API) |
| Front-end | Templates Django, Tailwind via CDN, JavaScript sem framework |

Dependências completas em [requirements.txt](requirements.txt). Os conectores de
provedores de IA são importados sob demanda — instale só os que for usar.

---

## Estrutura de pastas

```
config/                 Configuração do Django e roteamento ASGI
apps/
  core/                 As telas: painel do comparador e configurações
  comparador/           Motor determinístico de comparação (sem IA)
    services/
      parser_nfe.py       Lê NF-e/NFC-e 4.00 e NFS-e nacional
      mapa_campos.py      Categoria, severidade e pista de cada campo
      comparador.py       Pareamento de itens + comparação campo a campo
      relatorio.py        Compila o resultado de uma nota
      arquivos.py         Extração segura de ZIP
      pareador.py         Pareamento de notas entre os dois conjuntos
      relatorio_lote.py   Agrega N notas em causas recorrentes
  fiscal/               Tabelas oficiais (NCM, TIPI, CEST, CFOP, FCP) que o agente consulta
  provedores/           Cadastro multi-IA + criptografia das chaves
  conhecimento/         Scraping, chunking, embeddings e busca
  agente/               Agente de IA (LangGraph) e API FastAPI
base_conhecimento/      Documentação da Senior exportada em markdown
templates/  static/     Front-end
exemplos/               XMLs e ZIPs gerados para teste
```

---

## Como rodar localmente

Requisitos: Python 3.12 e Docker.

```bash
cd agente_implantacao

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

cp .env.example .env      # ajuste se quiser
docker compose up -d      # PostgreSQL 18 em 127.0.0.1:5435
./run.sh
```

Abra <http://127.0.0.1:8000>.

O `run.sh` aplica as migrações, semeia as regras de parametrização e sobe o
servidor. Para escolher host e porta: `./run.sh 0.0.0.0 8080`.

---

## Deploy

A aplicação roda como um container ([Dockerfile](Dockerfile)) que aplica as
migrações e sobe o servidor ASGI; basta um PostgreSQL com a extensão pgvector
ao lado e as variáveis do `.env.example` no ambiente. A infraestrutura como
código e os pipelines usados em produção ficaram fora desta cópia.

### Banco de dados

**PostgreSQL 18** é o banco do projeto. O `docker-compose.yml` sobe só o banco;
a aplicação roda no host.

O padrão é PostgreSQL mesmo sem `DB_ENGINE` no `.env`. Para rodar sem
infraestrutura nenhuma, defina `DB_ENGINE=sqlite` (usa `db.sqlite3`; só para
desenvolvimento, não para uso real).

### Testar sem arquivos reais

```bash
python manage.py gerar_lote_exemplo --quantidade 100   # dois ZIPs, comparação em massa
python manage.py gerar_exemplos                        # dois XMLs, nota a nota
```

Os arquivos vão para `exemplos/`, com divergências plantadas.

### Configurar a IA

O chat exige um provedor de IA cadastrado em **Configurações → Provedores de IA**.
A chave é criptografada antes de ir para o banco. Um provedor de **chat** é
obrigatório; um de **embeddings** é opcional — sem ele, a busca na base de
conhecimento usa correspondência textual em vez de busca semântica.
