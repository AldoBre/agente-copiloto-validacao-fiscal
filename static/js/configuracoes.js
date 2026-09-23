/* ==========================================================================
   Tela 2 — Configurações
   Abas: Provedores de IA · Base de conhecimento
   ========================================================================== */
(function () {
  'use strict';

  const { API, toast, escaparHtml, formatarData } = window.App;

  const $ = (sel) => document.querySelector(sel);
  const $$ = (sel) => Array.from(document.querySelectorAll(sel));

  const estado = {
    catalogo: null,
    provedores: [],
    fontes: [],
    // Paginação da lista de fontes: com 138 fontes importadas do repositório,
    // renderizar todas de uma vez dava uma página de rolagem interminável.
    paginaFontes: 1,
    buscaFonte: '',
    pollReindex: null,
  };

  const FONTES_POR_PAGINA = 15;

  /* ====================================================================== */
  /*  ABAS                                                                  */
  /* ====================================================================== */
  function configurarAbas() {
    $$('.aba').forEach((botao) => {
      botao.addEventListener('click', () => {
        $$('.aba').forEach((b) => {
          const ativo = b === botao;
          b.className =
            'aba border-b-2 px-4 py-2 text-sm font-medium ' +
            (ativo
              ? 'border-navy-500 text-navy-700'
              : 'border-transparent text-aco-500 hover:text-aco-700');
        });
        $$('.painel-aba').forEach((painel) =>
          painel.classList.toggle('hidden', painel.dataset.aba !== botao.dataset.aba)
        );

        if (botao.dataset.aba === 'conhecimento') {
          carregarStatus();
          carregarFontes();
        }
      });
    });
  }

  /* ====================================================================== */
  /*  PROVEDORES                                                            */
  /* ====================================================================== */
  async function carregarCatalogo() {
    estado.catalogo = await API.get('/api/provedores/catalogo/');

    const selProvedor = $('#form-provedor [name=provedor]');
    selProvedor.innerHTML = estado.catalogo.provedores
      .map((p) => `<option value="${p.valor}">${escaparHtml(p.rotulo)}</option>`)
      .join('');

    selProvedor.addEventListener('change', () => {
      preencherModelos();
      alternarCamposAzure();
    });
    $('#form-provedor [name=modelo]').addEventListener('change', mostrarDescricaoModelo);
    preencherModelos();
  }

  /** Modelos do provedor escolhido, agrupados por finalidade. */
  function preencherModelos(selecionado) {
    if (!estado.catalogo) return;
    const provedor = $('#form-provedor [name=provedor]').value;
    const meta = estado.catalogo.provedores.find((p) => p.valor === provedor);
    const selModelo = $('#form-provedor [name=modelo]');
    if (!meta) { selModelo.innerHTML = ''; return; }

    const grupo = (titulo, tipo) => {
      const itens = meta.modelos.filter((m) => m.tipo === tipo);
      if (!itens.length) return '';
      return (
        `<optgroup label="${titulo}">` +
        itens
          .map(
            (m) =>
              `<option value="${escaparHtml(m.id)}">${escaparHtml(m.rotulo)}${
                m.recomendado ? ' — recomendado' : ''
              }</option>`
          )
          .join('') +
        '</optgroup>'
      );
    };

    selModelo.innerHTML =
      grupo('Chat — análise das divergências', 'chat') +
      grupo('Embeddings — busca na base de conhecimento', 'embedding');

    if (selecionado) selModelo.value = selecionado;
    $('#ajuda-chave').textContent = meta.ajuda_chave || '';
    alternarCamposAzure();
    mostrarDescricaoModelo();
  }

  /**
   * No Foundry a chave vem do ambiente do servidor, não da tela. Deixar o campo visível
   * convidaria a colar em texto um segredo que o deploy já entrega — e o valor
   * colado seria ignorado, porque a configuração é lida do ambiente.
   */
  function alternarCamposAzure() {
    const azure = $('#form-provedor [name=provedor]').value === 'azure';
    $('#grupo-chave').classList.toggle('hidden', azure);
  }

  function mostrarDescricaoModelo() {
    if (!estado.catalogo) return;
    const provedor = $('#form-provedor [name=provedor]').value;
    const modeloId = $('#form-provedor [name=modelo]').value;
    const meta = estado.catalogo.provedores.find((p) => p.valor === provedor);
    const modelo = meta && meta.modelos.find((m) => m.id === modeloId);
    $('#descricao-modelo').textContent = modelo ? modelo.descricao || '' : '';

    // O atalho de embeddings só faz sentido ao cadastrar um modelo de CHAT de
    // um provedor que tenha modelo de embeddings próprio.
    const grupo = $('#grupo-embeddings');
    const cabe = modelo && modelo.tipo === 'chat' && meta && meta.embedding_padrao;
    grupo.classList.toggle('hidden', !cabe);
    grupo.classList.toggle('flex', !!cabe);
    if (cabe) {
      const emb = meta.modelos.find((m) => m.id === meta.embedding_padrao);
      $('#nome-embedding').textContent = emb ? emb.rotulo : meta.embedding_padrao;
    }
  }

  /* ====================================================================== */
  /*  AZURE AI FOUNDRY — somente leitura                                    */
  /* ====================================================================== */
  /**
   * Cartão somente leitura, alimentado por GET /api/platform-settings/.
   *
   * Não há formulário de propósito: endpoint, deployments e chave são fatos do
   * deploy — vêm das variáveis de ambiente do servidor. Um campo editável aqui
   * criaria uma segunda verdade, e o valor digitado seria simplesmente ignorado.
   */
  async function carregarFoundry() {
    const selos = $('#selos-foundry');
    const corpo = $('#corpo-foundry');

    let azure;
    try {
      azure = (await API.get('/api/platform-settings/')).azure;
    } catch (erro) {
      corpo.innerHTML =
        '<p class="text-xs text-aco-400">Não consegui ler a configuração da infra.</p>';
      return;
    }

    const emUso = (estado.provedores || []).some(
      (p) => p.provedor === 'azure' && p.ativo && p.padrao
    );
    const selo = (texto, classes) =>
      `<span class="rounded-full px-2 py-0.5 text-[10px] font-medium ${classes}">${texto}</span>`;

    selos.innerHTML =
      (azure.embeddingsActive ? selo('Embeddings ativos', 'bg-navy-50 text-navy-700') : '') +
      (emUso ? selo('Em uso', 'bg-acao/20 text-oliva') : '');

    if (!azure.configured) {
      corpo.innerHTML = `
        <div class="rounded-md border border-atencao/40 bg-atencao/10 p-2.5 text-[11px] leading-relaxed text-aco-700">
          <strong>Foundry não configurado nesta instância</strong> — escolher este
          provedor fará o chat falhar. Os valores vêm das variáveis de ambiente do
          servidor (AZURE_OPENAI_*); configure-as para provisionar.
        </div>`;
      return;
    }

    // Sem isto o deploy fica verde e nada muda: as app settings sozinhas não
    // ligam o Foundry — é preciso um registro de provedor marcado como padrão,
    // e a troca do modelo em uso tem de ser um ato humano explícito, não um
    // efeito colateral silencioso de subir a infra.
    const acao = emUso
      ? ''
      : `<button id="btn-usar-foundry"
                 class="mt-3 w-full rounded-md bg-acao px-3 py-2 text-xs font-semibold text-oliva transition hover:bg-acao-escuro">
           Usar o Foundry no chat
         </button>`;

    const linhas = [
      ['Endpoint', azure.endpoint],
      ['Deployment (chat)', azure.deployment],
      ['Deployment (embeddings)', azure.embeddingDeployment],
      ['api-version', azure.apiVersion],
      ['Chave (ambiente)', azure.key.configured ? azure.key.preview : 'não configurada'],
    ];

    corpo.innerHTML =
      `<p class="mb-2 text-[11px] leading-relaxed text-aco-400">
         Somente leitura: estes valores vêm das variáveis de ambiente do servidor.
         Para trocar o modelo ou a capacidade, mude o ambiente — não aqui.
       </p>` +
      linhas
        .map(
          ([rotulo, valor]) => `
            <div class="flex items-baseline justify-between gap-3 border-b border-aco-100 py-1.5 last:border-b-0">
              <span class="flex-none text-[11px] text-aco-500">${rotulo}</span>
              <code class="min-w-0 truncate text-right font-mono text-[11px] text-aco-800">${escaparHtml(
                valor || '—'
              )}</code>
            </div>`
        )
        .join('') +
      acao;

    const botao = $('#btn-usar-foundry');
    if (botao) botao.addEventListener('click', () => usarFoundry(botao));
  }

  /** Cadastra (ou reativa) o provedor Azure e o marca como o modelo do chat. */
  async function usarFoundry(botao) {
    const meta = (estado.catalogo?.provedores || []).find((p) => p.valor === 'azure');
    const chat = (meta?.modelos || []).find((m) => m.tipo === 'chat');
    if (!chat) {
      toast('O catálogo não tem modelo de chat para o Foundry.', 'erro');
      return;
    }

    botao.disabled = true;
    botao.textContent = 'Configurando…';
    try {
      // Sem api_key de propósito: no Foundry ela vem do ambiente do servidor.
      const existente = (estado.provedores || []).find(
        (p) => p.provedor === 'azure' && p.modelo === chat.id
      );
      const carga = { provedor: 'azure', modelo: chat.id, ativo: true, padrao: true };
      if (existente) await API.put(`/api/provedores/${existente.id}/`, carga);
      else await API.post('/api/provedores/', carga);

      toast(`${chat.rotulo} passou a ser o modelo do chat.`, 'sucesso');
      carregarProvedores();
    } catch (erro) {
      toast(erro.message || 'Não consegui ativar o Foundry.', 'erro');
      botao.disabled = false;
      botao.textContent = 'Usar o Foundry no chat';
    }
  }

  async function carregarProvedores() {
    estado.provedores = await API.get('/api/provedores/');
    const area = $('#lista-provedores');

    if (!estado.provedores.length) {
      area.innerHTML = `
        <div class="rounded-lg border border-dashed border-aco-300 bg-white p-8 text-center">
          <p class="text-sm font-medium text-aco-700">Nenhum provedor cadastrado</p>
          <p class="mt-1 text-xs text-aco-500">
            Cadastre pelo menos um modelo de <strong>chat</strong> para o agente funcionar.<br>
            Um provedor de <strong>embeddings</strong> é opcional (melhora a busca na base).
          </p>
        </div>`;
      return;
    }

    area.innerHTML = estado.provedores
      .map((p) => {
        const teste =
          p.ultimo_teste_ok === null || p.ultimo_teste_ok === undefined
            ? '<span class="rounded-full bg-aco-100 px-2 py-0.5 text-[10px] text-aco-500">não testado</span>'
            : p.ultimo_teste_ok
            ? '<span class="rounded-full bg-navy-50 px-2 py-0.5 text-[10px] font-medium text-navy-700">✓ conectado</span>'
            : '<span class="rounded-full bg-erro/10 px-2 py-0.5 text-[10px] font-medium text-erro">✗ falhou</span>';

        const emUso = p.ativo && p.padrao;

        return `
        <div class="rounded-lg border ${emUso ? 'border-navy-300 bg-navy-50/40' : 'border-aco-200 bg-white'} p-3.5">
          <div class="flex flex-wrap items-center gap-2">
            <span class="text-sm font-semibold text-aco-900">${escaparHtml(p.modelo_label)}</span>
            ${emUso ? '<span class="rounded-full bg-sucesso px-2 py-0.5 text-[10px] font-semibold text-white">em uso</span>' : ''}
            ${!p.ativo ? '<span class="rounded-full bg-aco-200 px-2 py-0.5 text-[10px] text-aco-600">inativo</span>' : ''}
            ${teste}
          </div>

          <div class="mt-1 text-xs text-aco-500">
            ${escaparHtml(p.provedor_label)} · ${escaparHtml(p.tipo_label)}
            ${p.tem_chave ? ` · chave <code class="font-mono">${escaparHtml(p.api_key_mascarada)}</code>` : ''}
          </div>

          ${p.ultimo_teste_detalhe
            ? `<div class="mt-1.5 rounded bg-aco-50 p-1.5 font-mono text-[10px] text-aco-500">${escaparHtml(p.ultimo_teste_detalhe)}</div>`
            : ''}

          <div class="mt-2.5 flex flex-wrap gap-1.5">
            <button data-acao="testar" data-id="${p.id}"
                    class="rounded border border-aco-200 px-2.5 py-1 text-[11px] text-aco-600 transition hover:bg-aco-50">Testar conexão</button>
            <button data-acao="editar" data-id="${p.id}"
                    class="rounded border border-aco-200 px-2.5 py-1 text-[11px] text-aco-600 transition hover:bg-aco-50">Trocar chave</button>
            ${!emUso ? `<button data-acao="padrao" data-id="${p.id}"
                    class="rounded border border-navy-200 bg-navy-50 px-2.5 py-1 text-[11px] text-navy-700 transition hover:bg-navy-100">Usar este</button>` : ''}
            <button data-acao="excluir" data-id="${p.id}"
                    class="ml-auto rounded border border-erro/40 px-2.5 py-1 text-[11px] text-erro transition hover:bg-erro/10">Excluir</button>
          </div>
        </div>`;
      })
      .join('');

    area.querySelectorAll('button[data-acao]').forEach((botao) =>
      botao.addEventListener('click', () => acaoProvedor(botao.dataset.acao, botao.dataset.id, botao))
    );

    // Aqui e não no início: o selo "Em uso" do cartão depende de saber quem é o
    // padrão, e todo caminho que troca o padrão já recarrega esta lista.
    carregarFoundry();
  }

  async function acaoProvedor(acao, id, botao) {
    const provedor = estado.provedores.find((p) => String(p.id) === String(id));

    if (acao === 'editar') {
      preencherFormularioProvedor(provedor);
      return;
    }

    if (acao === 'excluir') {
      if (!confirm(`Excluir "${provedor.modelo_label}"?`)) return;
      try {
        await API.delete(`/api/provedores/${id}/`);
        toast('Modelo excluído.', 'sucesso');
        carregarProvedores();
      } catch (erro) {
        toast(erro.message, 'erro');
      }
      return;
    }

    if (acao === 'padrao') {
      try {
        await API.post(`/api/provedores/${id}/definir-padrao/`);
        toast('Modelo em uso alterado.', 'sucesso');
        carregarProvedores();
      } catch (erro) {
        toast(erro.message, 'erro');
      }
      return;
    }

    if (acao === 'testar') {
      const original = botao.textContent;
      botao.textContent = 'Testando…';
      botao.disabled = true;
      try {
        const resultado = await API.post(`/api/provedores/${id}/testar/`);
        toast(resultado.detalhe, resultado.ok ? 'sucesso' : 'erro', 10000);
      } catch (erro) {
        toast((erro.dados && erro.dados.detalhe) || erro.message, 'erro', 12000);
      } finally {
        botao.textContent = original;
        botao.disabled = false;
        carregarProvedores();
      }
    }
  }

  function preencherFormularioProvedor(provedor) {
    const form = $('#form-provedor');
    form.reset();
    $('#titulo-form-provedor').textContent = provedor
      ? `Editar: ${provedor.modelo_label}`
      : 'Adicionar modelo';

    if (!provedor) {
      form.elements.id.value = '';
      form.elements.ativo.checked = true;
      form.elements.api_key.placeholder = 'cole a chave aqui';
      preencherModelos();
      alternarCamposAzure();
      return;
    }

    form.elements.id.value = provedor.id;
    form.elements.provedor.value = provedor.provedor;
    preencherModelos(provedor.modelo);
    form.elements.ativo.checked = provedor.ativo && provedor.padrao;
    form.elements.api_key.value = '';
    form.elements.api_key.placeholder = provedor.tem_chave
      ? 'deixe em branco para manter a chave atual'
      : 'cole a chave aqui';
    alternarCamposAzure();

    form.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  }

  async function salvarProvedor(evento) {
    evento.preventDefault();
    const form = evento.target;
    const id = form.elements.id.value;
    const emUso = form.elements.ativo.checked;

    const grupoEmb = $('#grupo-embeddings');
    const carga = {
      provedor: form.elements.provedor.value,
      modelo: form.elements.modelo.value,
      // "Usar este modelo" liga as duas coisas: fica ativo e vira o escolhido.
      ativo: emUso,
      padrao: emUso,
      tambem_embeddings:
        !grupoEmb.classList.contains('hidden') && form.elements.tambem_embeddings.checked,
    };
    const chave = form.elements.api_key.value.trim();
    if (chave) carga.api_key = chave;

    // O Foundry é a exceção: a chave vem do ambiente, e o campo nem aparece.
    if (!id && !chave && carga.provedor !== 'azure') {
      toast('Informe a API key do provedor.', 'aviso');
      return;
    }

    try {
      const salvo = id
        ? await API.put(`/api/provedores/${id}/`, carga)
        : await API.post('/api/provedores/', carga);

      toast(id ? 'Modelo atualizado.' : 'Modelo cadastrado.', 'sucesso');
      if (salvo && salvo.embedding_criado) {
        toast(
          `Busca semântica configurada com ${salvo.embedding_criado}. ` +
            'Clique em "Reindexar tudo" na aba Base de conhecimento para gerar os vetores.',
          'aviso',
          15000
        );
      }
      preencherFormularioProvedor(null);
      carregarProvedores();
    } catch (erro) {
      toast(erro.message, 'erro', 10000);
    }
  }

  /* ====================================================================== */
  /*  BASE DE CONHECIMENTO                                                  */
  /* ====================================================================== */
  async function carregarStatus() {
    try {
      const s = await API.get('/api/conhecimento/status/');
      const cards = [
        ['Fontes', s.fontes],
        ['Documentos', s.documentos],
        ['Trechos', s.trechos],
        ['Com embedding', s.trechos_com_embedding],
      ];
      $('#cards-status').innerHTML =
        cards
          .map(
            ([rotulo, valor]) => `
          <div class="rounded-lg border border-aco-200 bg-white p-3">
            <div class="text-[10px] font-medium uppercase tracking-wide text-aco-400">${rotulo}</div>
            <div class="mt-0.5 text-xl font-bold text-aco-800">${valor}</div>
          </div>`
          )
          .join('') +
        // A faixa só aparece quando há algo a resolver. Com tudo configurado
        // ela apenas repetia o que a aba de provedores já mostra.
        (s.busca_semantica_ativa
          ? ''
          : `<div class="col-span-2 rounded-lg border border-atencao/30 bg-atencao/10 p-3 text-xs text-aco-800 sm:col-span-4">
               Busca semântica <strong>inativa</strong> — o sistema usa só correspondência textual.
               Cadastre um provedor do tipo <em>Embeddings</em> e clique em "Reindexar tudo".
             </div>`);
    } catch (erro) {
      toast(erro.message, 'erro');
    }
  }

  async function carregarFontes() {
    estado.fontes = await API.get('/api/conhecimento/fontes/');
    renderizarFontes();
  }

  /* ------------------------------------------- reindexação em segundo plano */
  /**
   * A indexação roda no servidor; aqui só perguntamos como vai.
   *
   * O polling é retomado no carregamento da página (ver DOMContentLoaded):
   * como o estado está no banco, dar F5 ou voltar depois continua mostrando o
   * progresso — o navegador não é dono da tarefa.
   */
  function acompanharReindexacao() {
    const botao = $('#btn-reindexar');
    if (estado.pollReindex) clearInterval(estado.pollReindex);

    const consultar = async () => {
      let t;
      try {
        t = await API.get('/api/conhecimento/reindexar/progresso/');
      } catch (_) {
        return; // falha de rede pontual não cancela o acompanhamento
      }

      if (t.estado === 'rodando') {
        botao.disabled = true;
        botao.textContent = `Indexando… ${t.percentual}%`;
        return;
      }

      clearInterval(estado.pollReindex);
      estado.pollReindex = null;
      botao.disabled = false;
      botao.textContent = 'Reindexar tudo';

      if (t.estado === 'concluida') {
        toast(
          `Indexação concluída — ${t.processados} documento(s), ${t.com_embedding} trecho(s) com embedding.`,
          'sucesso',
          8000
        );
        if (t.mensagem) toast(t.mensagem, 'aviso', 12000);
        carregarStatus();
        carregarFontes();
      } else if (t.estado === 'erro') {
        toast(t.mensagem || 'A indexação falhou.', 'erro', 12000);
      } else if (t.estado === 'interrompida') {
        toast(
          'A indexação foi interrompida (o servidor reiniciou). Clique de novo — ela continua de onde parou.',
          'aviso',
          12000
        );
      }
    };

    consultar();
    estado.pollReindex = setInterval(consultar, 2500);
  }

  function fontesFiltradas() {
    const busca = estado.buscaFonte.trim().toLowerCase();
    if (!busca) return estado.fontes;
    return estado.fontes.filter((f) =>
      `${f.nome} ${f.url || ''}`.toLowerCase().includes(busca)
    );
  }

  function renderizarPaginacao(total, paginas) {
    const area = $('#paginacao-fontes');
    if (paginas <= 1) { area.innerHTML = ''; return; }

    const inicio = (estado.paginaFontes - 1) * FONTES_POR_PAGINA + 1;
    const fim = Math.min(estado.paginaFontes * FONTES_POR_PAGINA, total);
    const botao = (rotulo, pagina, ativo) =>
      `<button class="pagina-fonte rounded border px-2 py-1 text-[11px] transition ${
        ativo
          ? 'border-aco-200 bg-white text-aco-600 hover:bg-aco-50'
          : 'cursor-not-allowed border-aco-100 text-aco-300'
      }" data-pagina="${pagina}" ${ativo ? '' : 'disabled'}>${rotulo}</button>`;

    area.innerHTML =
      `<span class="text-[11px] text-aco-400">${inicio}–${fim} de ${total}</span>` +
      `<span class="flex items-center gap-1">
         ${botao('Anterior', estado.paginaFontes - 1, estado.paginaFontes > 1)}
         <span class="px-1 text-[11px] text-aco-500">${estado.paginaFontes}/${paginas}</span>
         ${botao('Próxima', estado.paginaFontes + 1, estado.paginaFontes < paginas)}
       </span>`;

    area.querySelectorAll('.pagina-fonte').forEach((b) =>
      b.addEventListener('click', () => {
        estado.paginaFontes = Number(b.dataset.pagina);
        renderizarFontes();
        $('#lista-fontes').scrollIntoView({ block: 'nearest' });
      })
    );
  }

  function renderizarFontes() {
    const area = $('#lista-fontes');
    const lista = fontesFiltradas();
    const total = lista.length;
    const paginas = Math.max(Math.ceil(total / FONTES_POR_PAGINA), 1);

    // Filtrar (ou excluir a última fonte de uma página) pode deixar a página
    // atual fora do intervalo — sem isto a lista apareceria vazia.
    if (estado.paginaFontes > paginas) estado.paginaFontes = paginas;

    $('#contador-fontes').textContent = estado.fontes.length
      ? `(${total}${total !== estado.fontes.length ? ` de ${estado.fontes.length}` : ''})`
      : '';

    if (!estado.fontes.length) {
      area.innerHTML =
        '<div class="rounded-lg border border-dashed border-aco-300 bg-white p-8 text-center text-xs text-aco-400">' +
        'Nenhuma fonte cadastrada. Adicione a URL da documentação de parametrização fiscal ao lado.</div>';
      $('#paginacao-fontes').innerHTML = '';
      return;
    }

    if (!total) {
      area.innerHTML =
        '<div class="rounded-lg border border-dashed border-aco-300 bg-white p-8 text-center text-xs text-aco-400">' +
        'Nenhuma fonte com esse filtro.</div>';
      $('#paginacao-fontes').innerHTML = '';
      return;
    }

    const inicio = (estado.paginaFontes - 1) * FONTES_POR_PAGINA;
    area.innerHTML = lista
      .slice(inicio, inicio + FONTES_POR_PAGINA)
      .map(
        (f) => `
      <div class="rounded-lg border border-aco-200 bg-white p-3.5">
        <div class="flex flex-wrap items-center gap-2">
          <span class="text-sm font-semibold text-aco-900">${escaparHtml(f.nome)}</span>
          <span class="rounded bg-aco-100 px-2 py-0.5 text-[10px] text-aco-600">${escaparHtml(f.tipo_label)}</span>
          ${!f.ativo ? '<span class="rounded-full bg-aco-200 px-2 py-0.5 text-[10px] text-aco-600">inativa</span>' : ''}
          <span class="ml-auto text-[10px] text-aco-400">
            ${f.total_documentos} doc(s) · ${f.total_trechos} trecho(s)
          </span>
        </div>
        ${f.url ? `<div class="mt-1 truncate text-[11px] text-aco-500">${escaparHtml(f.url)}</div>` : ''}
        ${f.ultima_ingestao_em
          ? `<div class="mt-1 text-[10px] ${f.ultima_ingestao_ok ? 'text-navy-600' : 'text-erro'}">
               Última ingestão: ${formatarData(f.ultima_ingestao_em)} — ${escaparHtml(f.ultima_ingestao_detalhe || '')}
             </div>`
          : '<div class="mt-1 text-[10px] text-aco-400">Nunca ingerida.</div>'}
        <div class="mt-2.5 flex flex-wrap gap-1.5">
          <button data-acao="ingerir" data-id="${f.id}"
                  class="rounded bg-acao px-2.5 py-1 text-[11px] font-medium text-oliva transition hover:bg-acao-escuro">Ingerir agora</button>
          <button data-acao="excluir-fonte" data-id="${f.id}"
                  class="ml-auto rounded border border-erro/40 px-2.5 py-1 text-[11px] text-erro transition hover:bg-erro/10">Excluir</button>
        </div>
      </div>`
      )
      .join('');

    area.querySelectorAll('button[data-acao]').forEach((botao) =>
      botao.addEventListener('click', () => acaoFonte(botao.dataset.acao, botao.dataset.id, botao))
    );

    renderizarPaginacao(total, paginas);
  }

  async function acaoFonte(acao, id, botao) {
    if (acao === 'excluir-fonte') {
      if (!confirm('Excluir a fonte e todos os seus documentos indexados?')) return;
      await API.delete(`/api/conhecimento/fontes/${id}/`);
      toast('Fonte excluída.', 'sucesso');
      carregarFontes();
      carregarStatus();
      return;
    }

    if (acao === 'ingerir') {
      const original = botao.textContent;
      botao.textContent = 'Ingerindo…';
      botao.disabled = true;
      try {
        const resultado = await API.post(`/api/conhecimento/fontes/${id}/ingerir/`, {});
        toast(
          `${resultado.documentos_processados} documento(s), ${resultado.trechos} trecho(s).`,
          resultado.erros.length ? 'aviso' : 'sucesso',
          8000
        );
        (resultado.avisos || []).forEach((a) => toast(a, 'aviso', 12000));
        (resultado.erros || []).slice(0, 3).forEach((e) => toast(e, 'erro', 12000));
        carregarFontes();
        carregarStatus();
      } catch (erro) {
        toast(erro.message, 'erro', 12000);
      } finally {
        botao.textContent = original;
        botao.disabled = false;
      }
    }
  }

  async function salvarFonte(evento) {
    evento.preventDefault();
    const form = evento.target;
    const tipo = form.elements.tipo.value;

    const urls = (form.elements.lista_urls.value || '')
      .split(/[\r\n\s]+/)
      .map((u) => u.trim())
      .filter((u) => /^https?:\/\//i.test(u));

    if (tipo === 'lista' && !urls.length) {
      toast('Cole ao menos um link (um por linha).', 'aviso');
      return;
    }

    const carga = {
      nome: form.elements.nome.value.trim(),
      tipo,
      url: form.elements.url.value.trim(),
      urls,
      descricao: form.elements.descricao.value.trim(),
      seguir_links: form.elements.seguir_links.checked,
      profundidade_max: parseInt(form.elements.profundidade_max.value, 10) || 1,
    };

    try {
      const fonte = await API.post('/api/conhecimento/fontes/', carga);
      const corpo =
        tipo === 'texto'
          ? { conteudo: form.elements.conteudo.value, titulo: carga.nome }
          : {};
      const resultado = await API.post(`/api/conhecimento/fontes/${fonte.id}/ingerir/`, corpo);

      toast(
        `Fonte criada — ${resultado.documentos_processados} página(s), ${resultado.trechos} trecho(s).`,
        resultado.erros && resultado.erros.length ? 'aviso' : 'sucesso',
        8000
      );
      (resultado.erros || []).slice(0, 3).forEach((e) => toast(e, 'erro', 12000));
      (resultado.avisos || []).forEach((a) => toast(a, 'aviso', 12000));
      form.reset();
      alternarCamposFonte();
      carregarFontes();
      carregarStatus();
    } catch (erro) {
      toast(erro.message, 'erro', 12000);
    }
  }

  function alternarCamposFonte() {
    const tipo = $('#form-fonte [name=tipo]').value;
    $('#grupo-lista-fonte').classList.toggle('hidden', tipo !== 'lista');
    $('#grupo-url-fonte').classList.toggle('hidden', tipo !== 'url');
    $('#grupo-texto-fonte').classList.toggle('hidden', tipo !== 'texto');
  }

  /* ====================================================================== */
  /*  INÍCIO                                                                */
  /* ====================================================================== */
  document.addEventListener('DOMContentLoaded', async () => {
    configurarAbas();

    try {
      await carregarCatalogo();
      await carregarProvedores();
    } catch (erro) {
      toast(erro.message, 'erro');
    }

    $('#form-provedor').addEventListener('submit', salvarProvedor);
    $('#btn-novo-provedor').addEventListener('click', () => preencherFormularioProvedor(null));
    $('#btn-cancelar-provedor').addEventListener('click', () => preencherFormularioProvedor(null));

    $('#form-fonte').addEventListener('submit', salvarFonte);
    $('#form-fonte [name=tipo]').addEventListener('change', alternarCamposFonte);
    $('#btn-cancelar-fonte').addEventListener('click', () => {
      $('#form-fonte').reset();
      alternarCamposFonte();
    });

    $('#busca-fonte').addEventListener('input', (e) => {
      estado.buscaFonte = e.target.value;
      estado.paginaFontes = 1; // filtrar sempre volta para a primeira página
      renderizarFontes();
    });

    $('#btn-reindexar').addEventListener('click', async () => {
      try {
        const tarefa = await API.post('/api/conhecimento/reindexar/', {});
        if (tarefa.ja_estava_rodando) {
          toast('Já existe uma indexação em andamento.', 'aviso');
        }
        acompanharReindexacao();
      } catch (erro) {
        toast(erro.message, 'erro', 12000);
      }
    });

    // Uma indexação pode ter sido disparada antes deste F5 (ou por outra
    // pessoa): a tarefa é do servidor, então retomamos o acompanhamento.
    try {
      const t = await API.get('/api/conhecimento/reindexar/progresso/');
      if (t.estado === 'rodando') acompanharReindexacao();
    } catch (_) { /* silencioso */ }
  });
})();
