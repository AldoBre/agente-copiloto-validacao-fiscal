/* ==========================================================================
   Tela 1 — Painel
   Esquerda: chat com o agente (streaming SSE).
   Direita : comparação EM MASSA (ZIP × ZIP) ou NOTA A NOTA.
   ========================================================================== */
(function () {
  'use strict';

  const { API, toast, escaparHtml, renderizarMarkdown, formatarData, moeda, configurarDivisor,
    SESSAO } = window.App;

  const $ = (sel) => document.querySelector(sel);
  const $$ = (sel) => Array.from(document.querySelectorAll(sel));

  const TAMANHO_BLOCO = 10;

  const estado = {
    //: Nota escolhida de cada lado no vínculo manual (nome do arquivo).
    semPar: { cliente: '', senior: '' },
    modo: 'massa',
    // --- chat -------------------------------------------------------------
    conversaId: null,
    enviando: false,
    usarStreaming: true,
    chatLiberado: false,
    // --- comparação nota a nota -------------------------------------------
    arquivos: { cliente: null, senior: null },
    comparacaoId: null,
    divergencias: [],
    relatorio: '',
    filtroSeveridade: 'todas',
    busca: '',
    // --- comparação em massa ----------------------------------------------
    lote: {
      envio: { cliente: null, senior: null },
      id: null,
      pares: [],
      naoPareados: { cliente: [], senior: [] },
      documentos: { cliente: [], senior: [] },
      totais: {},
      pareamentoAlterado: false,
      consolidado: null,
      relatorio: '',
      ordem: 'confianca',
    },
  };

  /* ====================================================================== */
  /*  ALTERNÂNCIA DE MODO                                                   */
  /* ====================================================================== */
  function configurarModos() {
    $$('.aba-modo').forEach((botao) => {
      botao.addEventListener('click', () => {
        estado.modo = botao.dataset.modo;
        $$('.aba-modo').forEach((b) => {
          const ativo = b === botao;
          b.className =
            'aba-modo border-b-2 px-3 py-2.5 text-sm font-medium ' +
            (ativo
              ? 'border-navy-500 text-navy-700'
              : 'border-transparent text-aco-500 hover:text-aco-700');
        });
        $$('.painel-modo').forEach((painel) =>
          painel.classList.toggle('hidden', painel.dataset.modo !== estado.modo)
        );
      });
    });
  }

  function mostrarEtapa(nome) {
    ['envio', 'pareamento', 'progresso', 'resultado'].forEach((etapa) =>
      $(`#etapa-${etapa}`).classList.toggle('hidden', etapa !== nome)
    );
  }

  /**
   * O chat só abre depois que existe um resultado de comparação — sem contexto
   * o agente responderia no vazio, que é justamente o que queremos evitar.
   */
  function liberarChat(rotuloContexto) {
    estado.chatLiberado = true;

    const entrada = $('#entrada-mensagem');
    entrada.disabled = false;
    entrada.placeholder = 'Pergunte ao agente… (Enter envia, Shift+Enter quebra linha)';
    $('#btn-enviar').disabled = false;
    $('#caixa-entrada').classList.remove('bg-aco-100', 'opacity-60');
    $('#caixa-entrada').classList.add('bg-white');
    $('#dica-rodape').textContent =
      'As respostas partem do relatório determinístico + base de conhecimento cadastrada.';

    if (rotuloContexto) {
      $('#badge-contexto').textContent = rotuloContexto;
      $('#badge-contexto').classList.remove('hidden');
    }

    const vazio = $('#estado-vazio-chat');
    if (vazio) {
      vazio.querySelector('h3').textContent = 'Chat liberado';
      vazio.querySelector('p').textContent =
        'O resultado da comparação já está no contexto. Clique em "Enviar divergências para ' +
        'o agente" ou pergunte diretamente aqui embaixo.';
    }
  }

  /* ====================================================================== */
  /*  DROPZONES                                                             */
  /* ====================================================================== */
  function configurarDropzones() {
    $$('.dropzone').forEach((zona) => {
      const alvo = zona.dataset.alvo;
      const input = zona.querySelector('input[type=file]');

      input.addEventListener('change', () => {
        if (input.files.length) definirArquivos(alvo, Array.from(input.files), zona);
      });

      ['dragenter', 'dragover'].forEach((evt) =>
        zona.addEventListener(evt, (e) => { e.preventDefault(); zona.classList.add('arrastando'); })
      );
      ['dragleave', 'drop'].forEach((evt) =>
        zona.addEventListener(evt, (e) => { e.preventDefault(); zona.classList.remove('arrastando'); })
      );
      zona.addEventListener('drop', (e) => {
        const arquivos = Array.from(e.dataTransfer.files || []);
        if (arquivos.length) definirArquivos(alvo, arquivos, zona);
      });
    });
  }

  function definirArquivos(alvo, arquivos, zona) {
    const rotulo = zona.querySelector('.nome-arquivo');

    if (alvo === 'cliente' || alvo === 'senior') {
      const arquivo = arquivos[0];
      if (!/\.xml$/i.test(arquivo.name)) { toast('Envie um arquivo .xml', 'aviso'); return; }
      estado.arquivos[alvo] = arquivo;
      rotulo.textContent = arquivo.name;
      zona.classList.add('carregado');
      $('#btn-comparar').disabled = !(estado.arquivos.cliente && estado.arquivos.senior);
      return;
    }

    const lado = alvo === 'lote-cliente' ? 'cliente' : 'senior';
    const zips = arquivos.filter((a) => /\.zip$/i.test(a.name));
    const xmls = arquivos.filter((a) => /\.xml$/i.test(a.name));

    if (!zips.length && !xmls.length) { toast('Envie um .zip ou arquivos .xml', 'aviso'); return; }

    estado.lote.envio[lado] = zips.length ? { zip: zips[0] } : { xmls };
    rotulo.textContent = zips.length
      ? zips[0].name
      : `${xmls.length} arquivo(s) .xml selecionado(s)`;
    zona.classList.add('carregado');
    $('#btn-parear').disabled = !(estado.lote.envio.cliente && estado.lote.envio.senior);
  }

  /* ====================================================================== */
  /*  ETAPA 1 → 2 : PAREAMENTO                                              */
  /* ====================================================================== */
  async function parearLote() {
    const botao = $('#btn-parear');
    const original = botao.textContent;
    botao.disabled = true;
    botao.textContent = 'Lendo e pareando as notas…';

    const dados = new FormData();
    ['cliente', 'senior'].forEach((lado) => {
      const envio = estado.lote.envio[lado];
      if (envio.zip) dados.append(`zip_${lado}`, envio.zip);
      else envio.xmls.forEach((arquivo) => dados.append(`xmls_${lado}`, arquivo));
    });

    try {
      const resposta = await API.post('/api/comparador/lotes/parear/', dados);
      aplicarEstadoLote(resposta);
      mostrarEtapa('pareamento');
      const naoAlta = estado.lote.pares.filter((p) => p.confianca !== 'alta').length;
      toast(
        `${resposta.total_pares} par(es) identificado(s) de ${resposta.total_cliente} × ${resposta.total_senior} notas.` +
          (naoAlta ? ` ${naoAlta} precisa(m) de conferência.` : ''),
        naoAlta ? 'aviso' : 'sucesso',
        8000
      );
      (resposta.avisos || []).slice(0, 4).forEach((a) => toast(a, 'aviso', 12000));
    } catch (erro) {
      toast(erro.message || 'Falha ao parear os arquivos.', 'erro', 12000);
    } finally {
      botao.disabled = false;
      botao.textContent = original;
    }
  }

  function aplicarEstadoLote(dados) {
    estado.lote.id = dados.lote_id;
    estado.lote.pares = dados.pares || [];
    estado.lote.naoPareados = dados.nao_pareados || { cliente: [], senior: [] };
    estado.lote.documentos = dados.documentos || { cliente: [], senior: [] };
    estado.lote.totais = {
      cliente: dados.total_cliente,
      senior: dados.total_senior,
      pares: dados.total_pares,
    };
    estado.lote.pareamentoAlterado = false;
    renderizarPareamento();
  }

  const CLASSE_CONFIANCA = {
    alta: 'border-navy-200 bg-navy-50 text-navy-700',
    media: 'border-atencao/40 bg-atencao/10 text-aco-800',
    baixa: 'border-orange-300 bg-orange-50 text-orange-700',
    manual: 'border-aco-300 bg-aco-100 text-aco-600',
  };

  function renderizarPareamento() {
    const pares = estado.lote.pares;
    const semPar = estado.lote.naoPareados;

    const contagem = { alta: 0, media: 0, baixa: 0, manual: 0 };
    pares.forEach((p) => { contagem[p.confianca] = (contagem[p.confianca] || 0) + 1; });

    $('#resumo-pareamento').innerHTML = [
      ['Pares', pares.length, 'text-aco-800'],
      ['Confiança alta', contagem.alta, 'text-navy-600'],
      ['Conferir', contagem.media + contagem.baixa + contagem.manual, 'text-aco-700'],
      ['Sem par', semPar.cliente.length + semPar.senior.length, 'text-orange-600'],
    ]
      .map(
        ([rotulo, valor, cor]) => `
        <div class="rounded-lg border border-aco-200 bg-white p-3">
          <div class="text-[10px] font-medium uppercase tracking-wide text-aco-400">${rotulo}</div>
          <div class="mt-0.5 text-xl font-bold ${cor}">${valor}</div>
        </div>`
      )
      .join('');

    const aConferir = contagem.media + contagem.baixa;
    const alerta = $('#alerta-confianca');
    if (aConferir) {
      alerta.innerHTML =
        `<strong>${aConferir} par(es) com confiança média ou baixa.</strong> ` +
        'O vínculo foi deduzido do conteúdo fiscal, não do nome do arquivo. ' +
        'Confira os primeiros da lista abaixo — um par errado gera divergências que não existem. ' +
        'Use o ✕ para desfazer e vincule manualmente em "Notas sem par".';
      alerta.classList.remove('hidden');
    } else {
      alerta.classList.add('hidden');
    }

    $('#cnt-sem-par').textContent = semPar.cliente.length + semPar.senior.length;
    $('#btn-comparar-lote').textContent = `Comparar ${pares.length} par(es)`;

    const ordem = { baixa: 0, media: 1, manual: 2, alta: 3 };
    const ordenados = [...pares].sort((a, b) =>
      estado.lote.ordem === 'arquivo'
        ? a.arquivo_cliente.localeCompare(b.arquivo_cliente)
        : (ordem[a.confianca] ?? 9) - (ordem[b.confianca] ?? 9) || a.score - b.score
    );

    $('#lista-pares').innerHTML = ordenados
      .map((par) => {
        const c = par.cliente || {};
        const s = par.senior || {};
        return `
        <div class="rounded-lg border border-aco-200 bg-white p-2.5">
          <div class="flex items-center gap-2">
            <span class="rounded-full border px-2 py-0.5 text-[10px] font-semibold ${CLASSE_CONFIANCA[par.confianca] || ''}">
              ${escaparHtml(par.confianca_rotulo)}${par.score ? ' · ' + par.score : ''}
            </span>
            <div class="min-w-0 flex-1 truncate text-[11px]">
              <span class="font-mono text-aco-700">${escaparHtml(par.arquivo_cliente)}</span>
              <span class="mx-1 text-aco-300">↔</span>
              <span class="font-mono text-navy-700">${escaparHtml(par.arquivo_senior)}</span>
            </div>
            <button data-desvincular="${par.indice}" title="Desfazer este vínculo"
                    class="flex-none rounded p-1 text-aco-300 transition hover:bg-erro/10 hover:text-erro">
              <svg class="h-3.5 w-3.5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12"/>
              </svg>
            </button>
          </div>
          <div class="mt-1 grid grid-cols-2 gap-2 text-[10px] text-aco-500">
            <div class="truncate">nº ${escaparHtml(c.numero || '?')} · ${escaparHtml(c.destinatario_nome || '')} · R$ ${escaparHtml(c.valor_total || '?')}</div>
            <div class="truncate">nº ${escaparHtml(s.numero || '?')} · ${escaparHtml(s.destinatario_nome || '')} · R$ ${escaparHtml(s.valor_total || '?')}</div>
          </div>
          ${par.motivos && par.motivos.length
            ? `<div class="mt-1 text-[10px] text-aco-400">${escaparHtml(par.motivos.join(' · '))}</div>`
            : ''}
        </div>`;
      })
      .join('');

    $$('#lista-pares [data-desvincular]').forEach((botao) =>
      botao.addEventListener('click', () => desvincular(Number(botao.dataset.desvincular)))
    );

    renderizarSemPar();
  }

  /**
   * Lista das notas sem par, uma ficha por nota.
   *
   * Era um <select> mostrando o nome do arquivo — que na prática é a chave de
   * acesso de 44 dígitos, porque é assim que a maioria dos emissores nomeia o
   * XML. Com dezenas de notas sem par, não dava para saber qual era qual sem
   * abrir arquivo por arquivo.
   *
   * A ficha mostra o que identifica a nota de verdade: número, data,
   * destinatário, valor e produtos. Nenhum dado novo foi buscado — tudo isso já
   * vinha na assinatura usada no pareamento automático. E quando a ficha não
   * basta, o link abre o XML cru numa aba.
   */
  function fichaSemPar(d, lado, selecionado) {
    const marcado = selecionado === d.nome_arquivo;
    const produtos = (d.produtos || []).slice(0, 3).join(', ');
    const xml = `/api/comparador/lotes/${encodeURIComponent(estado.lote.id)}/xml/${lado}/${encodeURIComponent(d.nome_arquivo)}`;

    return `
      <div class="ficha-sem-par cursor-pointer rounded border p-1.5 transition ${
        marcado ? 'border-navy-400 bg-navy-50' : 'border-aco-200 bg-white hover:border-navy-300'
      }" data-lado="${lado}" data-arquivo="${escaparHtml(d.nome_arquivo)}">
        <div class="flex items-baseline justify-between gap-2">
          <span class="text-[11px] font-semibold text-aco-800">
            nº ${escaparHtml(d.numero || '?')}${d.serie ? ' · série ' + escaparHtml(d.serie) : ''}
          </span>
          <span class="flex-none font-mono text-[11px] text-aco-700">${escaparHtml(moeda(d.valor_total))}</span>
        </div>
        <div class="truncate text-[10px] text-aco-500">
          ${escaparHtml(d.destinatario_nome || d.destinatario_doc || 'destinatário não informado')}
        </div>
        <div class="mt-0.5 flex flex-wrap items-center gap-x-2 gap-y-0.5 text-[10px] text-aco-400">
          ${d.data ? `<span>${escaparHtml(d.data.split('-').reverse().join('/'))}</span>` : ''}
          <span>${d.quantidade_itens || 0} item(ns)</span>
          ${produtos ? `<span class="truncate">· ${escaparHtml(produtos)}</span>` : ''}
        </div>
        <a href="${xml}" target="_blank" rel="noopener noreferrer"
           class="mt-1 inline-block text-[10px] text-navy-600 underline hover:text-navy-800">
          abrir XML
        </a>
      </div>`;
  }

  function renderizarSemPar() {
    const preencher = (seletor, itens, lado) => {
      const area = $(seletor);
      if (!itens.length) {
        area.innerHTML = '<p class="p-2 text-center text-[10px] text-aco-400">nenhuma nota sem par</p>';
        return;
      }
      area.innerHTML = itens.map((d) => fichaSemPar(d, lado, estado.semPar[lado])).join('');
    };
    preencher('#sel-sem-par-cliente', estado.lote.naoPareados.cliente, 'cliente');
    preencher('#sel-sem-par-senior', estado.lote.naoPareados.senior, 'senior');
  }

  /**
   * Seleção por clique na ficha. O link "abrir XML" é ignorado de propósito:
   * abrir o arquivo para conferir não deve mexer no que está escolhido.
   */
  function configurarSelecaoSemPar() {
    ['#sel-sem-par-cliente', '#sel-sem-par-senior'].forEach((seletor) =>
      $(seletor).addEventListener('click', (e) => {
        if (e.target.closest('a')) return;
        const ficha = e.target.closest('.ficha-sem-par');
        if (!ficha) return;
        const lado = ficha.dataset.lado;
        estado.semPar[lado] =
          estado.semPar[lado] === ficha.dataset.arquivo ? '' : ficha.dataset.arquivo;
        renderizarSemPar();
      })
    );
  }

  function desvincular(indice) {
    const par = estado.lote.pares.find((p) => p.indice === indice);
    if (!par) return;
    estado.lote.pares = estado.lote.pares.filter((p) => p.indice !== indice);
    if (par.cliente) estado.lote.naoPareados.cliente.push(par.cliente);
    if (par.senior) estado.lote.naoPareados.senior.push(par.senior);
    estado.lote.pareamentoAlterado = true;
    renderizarPareamento();
  }

  function vincularManual() {
    const cliente = estado.semPar.cliente;
    const senior = estado.semPar.senior;
    if (!cliente || !senior) { toast('Selecione uma nota de cada lado.', 'aviso'); return; }

    const docCliente = estado.lote.naoPareados.cliente.find((d) => d.nome_arquivo === cliente);
    const docSenior = estado.lote.naoPareados.senior.find((d) => d.nome_arquivo === senior);

    estado.lote.naoPareados.cliente = estado.lote.naoPareados.cliente.filter((d) => d.nome_arquivo !== cliente);
    estado.lote.naoPareados.senior = estado.lote.naoPareados.senior.filter((d) => d.nome_arquivo !== senior);
    // A nota saiu da lista: deixar a seleção apontando para ela faria o próximo
    // "Vincular" usar um arquivo que já tem par.
    estado.semPar = { cliente: '', senior: '' };

    const proximoIndice = estado.lote.pares.reduce((m, p) => Math.max(m, p.indice), -1) + 1;
    estado.lote.pares.push({
      indice: proximoIndice,
      arquivo_cliente: cliente,
      arquivo_senior: senior,
      cliente: docCliente,
      senior: docSenior,
      score: 0,
      confianca: 'manual',
      confianca_rotulo: 'Manual',
      motivos: ['vínculo definido manualmente'],
      comparado: false,
      total_divergencias: 0,
      total_criticas: 0,
      total_altas: 0,
    });
    estado.lote.pareamentoAlterado = true;
    renderizarPareamento();
    toast('Par vinculado.', 'sucesso', 2500);
  }

  /* ====================================================================== */
  /*  ETAPA 2 → 3 : COMPARAÇÃO COM PROGRESSO                                */
  /* ====================================================================== */
  /**
   * O lote vive no servidor (banco + XMLs em disco). Se ele sumir — servidor
   * reiniciado com banco novo, lote apagado, deploy no meio do caminho — a tela
   * precisa dizer isso com todas as letras e voltar para o envio, em vez de
   * deixar o consultor clicando num lote fantasma.
   */
  function loteExpirou() {
    estado.lote.id = null;
    estado.lote.pares = [];
    estado.lote.naoPareados = { cliente: [], senior: [] };
    estado.lote.consolidado = null;
    estado.lote.pareamentoAlterado = false;
    mostrarEtapa('envio');
    toast(
      'Este lote não existe mais no servidor (o serviço foi reiniciado ou o lote foi ' +
        'removido). Envie os arquivos novamente.',
      'erro',
      15000
    );
  }

  async function compararLote() {
    if (!estado.lote.id) { toast('Envie os arquivos e pareie antes de comparar.', 'aviso'); return; }
    if (!estado.lote.pares.length) { toast('Nenhum par para comparar.', 'aviso'); return; }

    mostrarEtapa('progresso');
    atualizarProgresso(0, estado.lote.pares.length, {});

    try {
      if (estado.lote.pareamentoAlterado) {
        $('#texto-progresso').textContent = 'salvando o pareamento ajustado…';
        const resposta = await API.post(`/api/comparador/lotes/${estado.lote.id}/repartear/`, {
          pares: estado.lote.pares.map((p) => ({
            cliente: p.arquivo_cliente,
            senior: p.arquivo_senior,
          })),
        });
        aplicarEstadoLote(resposta);
      }

      const total = estado.lote.pares.length;
      let comparados = 0;
      const acumulado = { divergencias: 0, criticas: 0, altas: 0 };

      // Lido UMA vez, antes do laço: se o consultor desmarcar no meio da
      // comparação, metade do lote sairia com um critério e metade com outro.
      const itensNaoSimulados = $('#chk-itens-nao-simulados').checked;

      while (comparados < total) {
        const resposta = await API.post(`/api/comparador/lotes/${estado.lote.id}/comparar/`, {
          tamanho_bloco: TAMANHO_BLOCO,
          itens_nao_simulados: itensNaoSimulados,
        });

        (resposta.processados || []).forEach((p) => {
          acumulado.divergencias += p.total_divergencias || 0;
          acumulado.criticas += p.total_criticas || 0;
          acumulado.altas += p.total_altas || 0;
        });

        comparados = resposta.total_comparados;
        atualizarProgresso(comparados, resposta.total_pares, acumulado);

        if (resposta.concluido) break;
        if (!resposta.processados || !resposta.processados.length) break; // trava de segurança
      }

      $('#texto-progresso').textContent = 'consolidando as divergências…';
      const consolidado = await API.post(`/api/comparador/lotes/${estado.lote.id}/consolidar/`);
      estado.lote.consolidado = consolidado;
      estado.lote.relatorio = consolidado.relatorio_markdown || '';
      renderizarConsolidado(consolidado);
      mostrarEtapa('resultado');
      liberarChat(`lote de ${consolidado.placar.notas_comparadas} notas`);

      toast(
        `${consolidado.placar.total_divergencias} divergência(s) em ${consolidado.placar.notas_com_divergencia} nota(s), ` +
          `agrupadas em ${consolidado.placar.total_causas} causa(s).`,
        consolidado.placar.por_severidade.critica ? 'aviso' : 'sucesso',
        9000
      );
    } catch (erro) {
      if (erro.status === 404) { loteExpirou(); return; }
      toast(erro.message || 'Falha ao comparar o lote.', 'erro', 12000);
      mostrarEtapa('pareamento');
    }
  }

  function atualizarProgresso(feitos, total, acumulado) {
    const percentual = total ? Math.round((feitos / total) * 100) : 0;
    $('#barra-progresso').style.width = `${percentual}%`;
    $('#texto-progresso').textContent = `comparando ${feitos} de ${total} notas (${percentual}%)`;
    $('#parciais-progresso').innerHTML = [
      ['Divergências', acumulado.divergencias || 0, 'text-aco-700'],
      ['Críticas', acumulado.criticas || 0, 'text-erro'],
      ['Altas', acumulado.altas || 0, 'text-orange-600'],
    ]
      .map(
        ([rotulo, valor, cor]) => `
        <div class="rounded border border-aco-200 bg-aco-50 p-2">
          <div class="text-[9px] font-medium uppercase tracking-wide text-aco-400">${rotulo}</div>
          <div class="text-base font-bold ${cor}">${valor}</div>
        </div>`
      )
      .join('');
  }

  /* ====================================================================== */
  /*  ETAPA 4 : RESULTADO CONSOLIDADO                                       */
  /* ====================================================================== */
  const CLASSE_SEV = { critica: 'sev-critica', alta: 'sev-alta', media: 'sev-media', baixa: 'sev-baixa' };

  /** Lista de notas afetadas, como chips "Nota Original 63 ↔ Nota Senior 65". */
  function chipsNotas(notas, total) {
    if (!notas || !notas.length) return '';
    const chips = notas
      .map(
        (n) =>
          `<span class="whitespace-nowrap rounded border border-aco-200 bg-white px-1.5 py-0.5 font-mono text-[10px] text-aco-600">${escaparHtml(n)}</span>`
      )
      .join('');
    const resto =
      total > notas.length
        ? `<span class="text-[10px] text-aco-400">+${total - notas.length}</span>`
        : '';
    return `<div class="mt-1 flex flex-wrap items-center gap-1">${chips}${resto}</div>`;
  }

  /**
   * Card de causa recorrente.
   *
   * Responde, nesta ordem: **o que** está errado (título em português),
   * **onde** (quais notas), **qual é a diferença** e **o que fazer**.
   * O nome do campo no XML fica como referência, não como manchete.
   */
  function cartaoCausa(causa, posicao) {
    const ehItemAusente = causa.campo === '_item';

    const variacoes = (causa.variacoes || [])
      .map((v) => {
        const notas = chipsNotas(v.notas, v.total_notas);
        if (ehItemAusente) {
          return `
            <div class="rounded border border-aco-200 bg-aco-50 p-2">
              <div class="text-[11px] text-aco-700">
                Produto <code class="font-mono font-semibold">${escaparHtml(v.cliente)}</code> —
                <strong>${v.ocorrencias}</strong> item(ns) não emitido(s) pelo Senior
              </div>
              ${notas}
            </div>`;
        }
        return `
          <div class="rounded border border-aco-200 bg-aco-50 p-2">
            <div class="flex flex-wrap items-center gap-2 text-[11px]">
              <span class="text-[10px] uppercase tracking-wide text-aco-400">XML Original</span>
              <code class="rounded bg-white px-1.5 py-0.5 font-mono font-semibold text-aco-800">${escaparHtml(v.cliente || '(ausente)')}</code>
              <span class="text-aco-300">→</span>
              <span class="text-[10px] uppercase tracking-wide text-navy-500">XML Senior</span>
              <code class="rounded bg-navy-50 px-1.5 py-0.5 font-mono font-semibold text-navy-800">${escaparHtml(v.senior || '(ausente)')}</code>
            </div>
            ${notas}
          </div>`;
      })
      .join('');

    const produtos =
      causa.produtos && causa.produtos.length && !ehItemAusente
        ? `<div class="mt-2 text-[10px] text-aco-500">Produtos: ${causa.produtos
            .map((x) => escaparHtml(x.codigo))
            .join(', ')}${
            causa.total_produtos > causa.produtos.length
              ? ` +${causa.total_produtos - causa.produtos.length}`
              : ''
          }</div>`
        : '';

    return `
      <div class="card-divergencia ${CLASSE_SEV[causa.severidade] || 'sev-baixa'} rounded-lg border border-aco-200 bg-white p-3.5">

        <div class="flex items-start gap-2.5">
          <span class="mt-0.5 flex h-5 w-5 flex-none items-center justify-center rounded bg-aco-100 text-[10px] font-bold text-aco-500">
            ${posicao}
          </span>
          <div class="min-w-0 flex-1">
            <h4 class="text-sm font-semibold leading-snug text-aco-900">
              ${escaparHtml(causa.titulo || causa.campo)}
            </h4>
            <div class="mt-0.5 flex flex-wrap items-center gap-1.5 text-[10px] text-aco-400">
              <span class="chip-sev rounded-full px-1.5 py-0.5 font-semibold">${escaparHtml(causa.severidade_rotulo)}</span>
              <span>${escaparHtml(causa.categoria)}</span>
              <span>·</span>
              <code class="font-mono">${escaparHtml(causa.campo)}</code>
            </div>
          </div>
          <span class="flex-none rounded-full bg-aco-800 px-2 py-0.5 text-[10px] font-semibold text-white">
            ${causa.notas_afetadas} nota${causa.notas_afetadas > 1 ? 's' : ''}
          </span>
        </div>

        <div class="mt-2.5 space-y-1.5">${variacoes}</div>
        ${causa.total_variacoes > causa.variacoes.length
          ? `<div class="mt-1 text-[10px] text-aco-400">… e mais ${causa.total_variacoes - causa.variacoes.length} variação(ões)</div>`
          : ''}
        ${produtos}

        ${causa.pista
          ? `<div class="mt-2.5 rounded border-l-2 border-navy-300 bg-navy-50 px-2.5 py-2">
               <div class="text-[9px] font-semibold uppercase tracking-wide text-navy-600">O que ajustar</div>
               <div class="mt-0.5 text-[11px] leading-relaxed text-aco-700">${escaparHtml(causa.pista)}</div>
             </div>`
          : ''}
      </div>`;
  }

  /** Negrito de markdown (**x**) → <strong>, com escape antes. */
  function negrito(texto) {
    return escaparHtml(texto).replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');
  }

  function renderizarNarrativa(narrativa, placar) {
    const area = $('#resumo-narrativo');
    if (!narrativa || !narrativa.abertura) {
      area.classList.add('hidden');
      return;
    }
    area.classList.remove('hidden');
    area.innerHTML = `
      <div class="flex items-start gap-2.5">
        <span class="mt-0.5 flex h-5 w-5 flex-none items-center justify-center rounded bg-navy-50 text-navy-600">
          <svg class="h-3 w-3" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
          </svg>
        </span>
        <div class="min-w-0 flex-1">
          <div class="text-sm leading-relaxed text-aco-800">${negrito(narrativa.abertura)}</div>
          ${narrativa.linhas && narrativa.linhas.length
            ? `<ul class="mt-2 space-y-1">${narrativa.linhas
                .map(
                  (l) =>
                    `<li class="flex gap-2 text-[13px] leading-relaxed text-aco-700">
                       <span class="mt-1.5 h-1 w-1 flex-none rounded-full bg-navy-400"></span>
                       <span>${negrito(l)}</span>
                     </li>`
                )
                .join('')}</ul>`
            : ''}
          ${narrativa.fechamento
            ? `<p class="mt-2 text-[11px] leading-relaxed text-aco-500">${escaparHtml(narrativa.fechamento)}</p>`
            : ''}
        </div>
      </div>`;
  }

  function renderizarConsolidado(dados) {
    const p = dados.placar;
    renderizarNarrativa(dados.narrativa, p);
    $('#placar-lote').innerHTML = [
      ['Notas comparadas', p.notas_comparadas, 'text-aco-800'],
      ['Com divergência', p.notas_com_divergencia, 'text-orange-600'],
      ['Sem divergência', p.notas_conformes, 'text-navy-600'],
      ['Causas distintas', p.total_causas, 'text-erro'],
    ]
      .map(
        ([rotulo, valor, cor]) => `
        <div class="rounded-lg border border-aco-200 bg-white p-3">
          <div class="text-[10px] font-medium uppercase tracking-wide text-aco-400">${rotulo}</div>
          <div class="mt-0.5 text-xl font-bold ${cor}">${valor}</div>
        </div>`
      )
      .join('');

    // ---- causas ----------------------------------------------------------
    $('#lista-causas').innerHTML = (dados.causas || [])
      .map((causa, posicao) => cartaoCausa(causa, posicao + 1))
      .join('');

    // ---- notas -----------------------------------------------------------
    $('#lista-notas-lote').innerHTML = (dados.notas || [])
      .map(
        (nota) => `
        <div class="flex items-center gap-2 rounded-lg border border-aco-200 bg-white px-3 py-2 text-[11px]">
          <span class="h-2 w-2 flex-none rounded-full ${nota.conforme ? 'bg-sucesso' : 'bg-erro/100'}"></span>
          <span class="flex-none font-mono font-semibold text-aco-800">${escaparHtml(nota.rotulo || nota.arquivo_cliente)}</span>
          <span class="min-w-0 flex-1 truncate text-[10px] text-aco-400">
            ${escaparHtml(nota.arquivo_cliente)} ↔ ${escaparHtml(nota.arquivo_senior)}
          </span>
          <span class="flex-none ${nota.conforme ? 'text-navy-600' : 'text-aco-600'}">
            ${nota.conforme ? 'sem divergência' : `${nota.total} divergência${nota.total > 1 ? 's' : ''}`}
          </span>
          ${nota.comparacao_id
            ? `<button data-nota="${nota.comparacao_id}" data-rotulo="${escaparHtml(nota.rotulo || nota.arquivo_cliente)}"
                       class="flex-none rounded border border-aco-200 px-2 py-0.5 text-[10px] text-aco-600 transition hover:bg-aco-50">ver</button>`
            : ''}
        </div>`
      )
      .join('');

    $$('#lista-notas-lote [data-nota]').forEach((botao) =>
      botao.addEventListener('click', () => abrirModalNota(botao.dataset.nota, botao.dataset.rotulo))
    );

    // ---- sem par ---------------------------------------------------------
    const semPar = dados.nao_pareados || { cliente: [], senior: [] };
    const linhas = [
      ...semPar.cliente.map((d) => ({ lado: 'Só no sistema atual', cor: 'text-aco-700', d })),
      ...semPar.senior.map((d) => ({ lado: 'Só no Senior', cor: 'text-navy-700', d })),
    ];
    $('#lista-sem-par-final').innerHTML = linhas.length
      ? linhas
          .map(
            ({ lado, cor, d }) => `
          <div class="rounded-lg border border-aco-200 bg-white px-3 py-2 text-[11px]">
            <div class="flex items-center gap-2">
              <span class="rounded bg-aco-100 px-2 py-0.5 text-[10px] font-medium ${cor}">${lado}</span>
              <span class="font-mono text-aco-700">${escaparHtml(d.nome_arquivo)}</span>
            </div>
            <div class="mt-0.5 text-[10px] text-aco-500">
              nº ${escaparHtml(d.numero || '?')} · ${escaparHtml(d.destinatario_nome || '')} ·
              R$ ${escaparHtml(d.valor_total || '?')} · ${d.quantidade_itens || 0} item(ns)
            </div>
          </div>`
          )
          .join('')
      : '<div class="rounded-lg border border-dashed border-aco-300 bg-white p-6 text-center text-xs text-aco-400">Todas as notas foram pareadas.</div>';
  }

  async function abrirModalNota(comparacaoId, rotulo) {
    const modal = $('#modal-nota');
    $('#titulo-modal-nota').textContent = `Divergências — ${rotulo}`;
    $('#conteudo-modal-nota').innerHTML = '<div class="text-xs text-aco-400">Carregando…</div>';
    modal.classList.remove('hidden');
    modal.classList.add('flex');

    try {
      const dados = await API.get(`/api/comparador/${comparacaoId}/`);
      const divergencias = dados.divergencias || [];
      $('#conteudo-modal-nota').innerHTML = divergencias.length
        ? divergencias.map(cartaoDivergencia).join('')
        : '<div class="text-xs text-aco-400">Nenhuma divergência nesta nota.</div>';
    } catch (erro) {
      $('#conteudo-modal-nota').innerHTML =
        `<div class="text-xs text-erro">${escaparHtml(erro.message)}</div>`;
    }
  }

  /* ====================================================================== */
  /*  COMPARAÇÃO NOTA A NOTA                                                */
  /* ====================================================================== */
  async function comparar() {
    const botao = $('#btn-comparar');
    const original = botao.textContent;
    botao.disabled = true;
    botao.textContent = 'Comparando…';

    const dados = new FormData();
    dados.append('xml_cliente', estado.arquivos.cliente);
    dados.append('xml_senior', estado.arquivos.senior);

    try {
      const resposta = await API.post('/api/comparador/comparar/', dados);
      estado.comparacaoId = resposta.comparacao_id;
      estado.divergencias = resposta.divergencias || [];
      estado.relatorio = resposta.relatorio_markdown || '';
      renderizarResultadoUnico(resposta);
      liberarChat('comparação anexada');
      const criticas = (resposta.resumo.por_severidade || {}).critica || 0;
      toast(
        `${resposta.resumo.total_divergencias} divergência(s)` + (criticas ? `, ${criticas} crítica(s).` : '.'),
        criticas ? 'aviso' : 'sucesso'
      );
    } catch (erro) {
      toast(erro.message || 'Falha ao comparar os XMLs.', 'erro', 9000);
    } finally {
      botao.disabled = false;
      botao.textContent = original;
    }
  }

  function renderizarResultadoUnico(resposta) {
    const resumo = resposta.resumo || {};
    const sev = resumo.por_severidade || {};
    $('#cnt-critica').textContent = sev.critica || 0;
    $('#cnt-alta').textContent = sev.alta || 0;
    $('#cnt-media').textContent = sev.media || 0;
    $('#cnt-baixa').textContent = sev.baixa || 0;

    $('#resumo-documentos').innerHTML = [
      ['Sistema atual', resumo.documento_cliente || {}],
      ['ERP Senior', resumo.documento_senior || {}],
    ]
      .map(
        ([rotulo, doc]) => `
        <div class="rounded-lg border border-aco-200 bg-white p-2.5">
          <div class="text-[10px] font-semibold uppercase tracking-wide text-aco-400">${rotulo}</div>
          <div class="mt-0.5 truncate font-medium text-aco-700">${escaparHtml(doc.arquivo || '—')}</div>
          <div class="text-aco-500">${escaparHtml(doc.identificacao || '')} · ${doc.itens || 0} item(ns)</div>
        </div>`
      )
      .join('');

    const avisos = resposta.avisos || [];
    const areaAvisos = $('#avisos');
    if (avisos.length) {
      areaAvisos.innerHTML =
        '<strong>Avisos:</strong><ul class="mt-1 list-disc pl-4">' +
        avisos.map((a) => `<li>${escaparHtml(a)}</li>`).join('') + '</ul>';
      areaAvisos.classList.remove('hidden');
    } else {
      areaAvisos.classList.add('hidden');
    }

    $('#painel-resultado').classList.remove('hidden');
    renderizarDivergencias();
  }

  function cartaoDivergencia(d) {
    const local =
      d.item_numero != null
        ? `item ${d.item_numero}${d.item_codigo ? ' · ' + escaparHtml(d.item_codigo) : ''}`
        : d.escopo === 'totais' ? 'totais da nota' : 'cabeçalho';

    return `
    <div class="card-divergencia ${CLASSE_SEV[d.severidade] || 'sev-baixa'} rounded-lg border border-aco-200 bg-white p-3">
      <div class="flex items-start gap-2">
        <div class="min-w-0 flex-1">
          <div class="text-xs font-semibold text-aco-900">${escaparHtml(d.titulo || d.campo)}</div>
          <div class="mt-0.5 flex flex-wrap items-center gap-1.5 text-[10px] text-aco-400">
            <span class="chip-sev rounded-full px-1.5 py-0.5 font-semibold">${escaparHtml(d.severidade_rotulo || d.severidade)}</span>
            <span>${escaparHtml(d.categoria)}</span>
            <span>·</span>
            <code class="font-mono">${escaparHtml(d.campo)}</code>
          </div>
        </div>
        <span class="flex-none text-[10px] text-aco-400">${local}</span>
      </div>
      <div class="mt-2 grid grid-cols-2 gap-2 text-[11px]">
        <div class="rounded border border-aco-200 bg-aco-50 p-1.5">
          <div class="text-[9px] font-semibold uppercase text-aco-400">XML Original</div>
          <div class="truncate font-mono text-aco-700">${escaparHtml(d.valor_cliente || '(ausente)')}</div>
        </div>
        <div class="rounded border border-navy-200 bg-navy-50 p-1.5">
          <div class="text-[9px] font-semibold uppercase text-navy-600">XML Senior</div>
          <div class="truncate font-mono text-navy-800">${escaparHtml(d.valor_senior || '(ausente)')}</div>
        </div>
      </div>
      ${d.diferenca ? `<div class="mt-1.5 text-[10px] text-aco-500">Diferença: <code class="font-mono">${escaparHtml(d.diferenca)}</code></div>` : ''}
      ${d.pista ? `<div class="mt-1.5 border-t border-aco-100 pt-1.5 text-[11px] leading-relaxed text-aco-600">${escaparHtml(d.pista)}</div>` : ''}
    </div>`;
  }

  function renderizarDivergencias() {
    const busca = estado.busca.trim().toLowerCase();
    const lista = estado.divergencias.filter((d) => {
      if (estado.filtroSeveridade !== 'todas' && d.severidade !== estado.filtroSeveridade) return false;
      if (!busca) return true;
      return [d.campo, d.categoria, d.item_codigo, d.item_descricao, d.valor_cliente, d.valor_senior]
        .join(' ').toLowerCase().includes(busca);
    });

    const area = $('#lista-divergencias');
    if (!lista.length) {
      area.innerHTML =
        '<div class="rounded-lg border border-dashed border-aco-300 bg-white p-6 text-center text-xs text-aco-400">Nenhuma divergência com os filtros atuais.</div>';
      return;
    }
    area.innerHTML = lista.slice(0, 400).map(cartaoDivergencia).join('');
    if (lista.length > 400) {
      area.innerHTML += `<div class="p-2 text-center text-[11px] text-aco-400">Exibindo 400 de ${lista.length}.</div>`;
    }
  }

  /* ====================================================================== */
  /*  CHAT                                                                  */
  /* ====================================================================== */
  function adicionarBolha(papel, conteudo, opcoes = {}) {
    const vazio = $('#estado-vazio-chat');
    if (vazio) vazio.remove();

    const area = $('#mensagens');
    const div = document.createElement('div');
    div.className = 'aparecer';

    if (papel === 'usuario') {
      div.innerHTML = `
        <div class="flex justify-end">
          <div class="max-w-[85%] rounded-lg rounded-br-sm bg-navy-500 px-3.5 py-2.5 text-sm text-white">
            ${escaparHtml(conteudo).replace(/\n/g, '<br>')}
          </div>
        </div>`;
    } else {
      div.innerHTML = `
        <div class="flex gap-2.5">
          <div class="mt-0.5 flex h-6 w-6 flex-none items-center justify-center rounded bg-navy-50 text-[10px] font-bold text-navy-600">S</div>
          <div class="min-w-0 flex-1">
            <div class="area-consultas mb-1.5 hidden flex-wrap gap-1"></div>
            <div class="md corpo-resposta rounded-lg rounded-tl-sm border border-aco-200 bg-white px-3.5 py-2.5">
              ${opcoes.html || renderizarMarkdown(conteudo)}
            </div>
            <div class="area-fontes mt-1.5 flex flex-wrap gap-1"></div>
            <div class="area-acoes mt-1.5 flex flex-wrap items-center gap-1"></div>
          </div>
        </div>`;
    }

    area.appendChild(div);
    area.scrollTop = area.scrollHeight;
    return div;
  }

  /**
   * Fontes ficam RECOLHIDAS por padrão.
   *
   * Com a busca dirigida por causa, um lote de 7 divergências recupera ~14
   * trechos — 14 pastilhas empilhadas embaixo de cada resposta empurravam o
   * conteúdo para fora da tela e competiam com o que importa. Vira uma linha
   * ("14 fontes consultadas") que só abre quando o consultor quiser conferir a
   * procedência.
   */
  function renderizarFontes(elemento, fontes) {
    if (!fontes || !fontes.length) return;
    const area = elemento.querySelector('.area-fontes');
    if (!area) return;

    const pastilhas = fontes
      .map((f) => {
        const rotulo = escaparHtml(f.documento || f.fonte || 'fonte');
        const titulo = escaparHtml(
          [f.fonte, f.secao, f.responde_a].filter(Boolean).join(' · ')
        );
        const corpo = `<span class="rounded-full border border-aco-200 bg-aco-50 px-2 py-0.5 text-[10px] text-aco-500" title="${titulo}">📄 ${rotulo}</span>`;
        return f.url
          ? `<a href="${escaparHtml(f.url)}" target="_blank" rel="noopener noreferrer">${corpo}</a>`
          : corpo;
      })
      .join('');

    const plural = fontes.length === 1 ? 'fonte consultada' : 'fontes consultadas';
    area.innerHTML =
      `<details class="w-full">
         <summary class="cursor-pointer select-none text-[10px] text-aco-400 hover:text-aco-600">
           ${fontes.length} ${plural}
         </summary>
         <div class="mt-1 flex flex-wrap gap-1">${pastilhas}</div>
       </details>`;
  }

  /**
   * Pastilhas do que o agente foi consultar antes de responder.
   *
   * Cada consulta são duas idas ao provedor antes do primeiro token da resposta
   * final — sem sinal nenhum a tela fica parada em "carregando" por vários
   * segundos, que foi a reclamação de 12/08/2026. As pastilhas ficam na bolha
   * depois de pronto, de propósito: saber que a alíquota saiu da TIPI, e não da
   * cabeça do modelo, é metade do valor da resposta.
   */
  function registrarConsultas(bolha, chamadas) {
    const area = bolha.querySelector('.area-consultas');
    if (!area || !chamadas || !chamadas.length) return;
    area.classList.remove('hidden');
    area.classList.add('flex');
    area.insertAdjacentHTML(
      'beforeend',
      chamadas
        .map((c) => {
          const detalhe = c.detalhe ? ` · ${escaparHtml(c.detalhe)}` : '';
          return `<span class="consulta-chip inline-flex items-center gap-1 rounded-full border border-navy-200 bg-navy-50 px-2 py-0.5 text-[10px] text-navy-700">
                    <span class="ponto-consulta h-1.5 w-1.5 flex-none rounded-full bg-navy-400"></span>
                    consultando ${escaparHtml(c.nome)}${detalhe}
                  </span>`;
        })
        .join('')
    );
  }

  /** Troca "consultando X" por "X" quando o turno acaba. */
  function encerrarConsultas(bolha) {
    bolha.querySelectorAll('.consulta-chip').forEach((chip) => {
      const ponto = chip.querySelector('.ponto-consulta');
      if (ponto) ponto.remove();
      chip.innerHTML = chip.innerHTML.replace('consultando ', '');
    });
  }

  async function enviarMensagem(texto, opcoes = {}) {
    if (estado.enviando) return;
    if (!estado.chatLiberado) {
      toast('Rode uma comparação antes de conversar com o agente.', 'aviso');
      return;
    }
    const mensagem = (texto || $('#entrada-mensagem').value).trim();
    if (!mensagem) return;

    estado.enviando = true;
    $('#btn-enviar').disabled = true;
    $('#entrada-mensagem').value = '';
    $('#entrada-mensagem').style.height = 'auto';

    adicionarBolha('usuario', opcoes.rotuloUsuario || mensagem);
    const bolha = adicionarBolha('agente', '', {
      html: '<span class="pontos"><span></span><span></span><span></span></span>',
    });
    const corpo = bolha.querySelector('.corpo-resposta');

    const carga = {
      mensagem,
      conversa_id: estado.conversaId,
      comparacao_id: estado.comparacaoId,
      lote_id: estado.lote.consolidado ? estado.lote.id : null,
      // O SSE não passa pelo wrapper `requisicao` (fetch cru), então a sessão
      // do histórico viaja no corpo.
      sessao: SESSAO,
      // Guardado junto da mensagem para o histórico reexibir o que apareceu na
      // tela, não o prompt longo que foi para o modelo.
      rotulo: opcoes.rotuloUsuario || '',
    };

    let acumulado = '';
    // Mapa DESTA resposta. A numeração dos prints recomeça a cada turno, então
    // um acumulado entre respostas faria [[print:2]] da resposta nova exibir a
    // captura da anterior — tela errada com cara de fonte legítima.
    const printsDaResposta = {};
    let houveErro = false;
    let mensagemErro = '';

    try {
      await enviarComStreaming(carga, (evento) => {
        if (evento.tipo === 'inicio') {
          estado.conversaId = evento.conversa_id;
        } else if (evento.tipo === 'token') {
          acumulado += evento.texto;
          corpo.innerHTML = renderizarMarkdown(acumulado, printsDaResposta);
          corpo.classList.add('cursor-digitando');
          $('#mensagens').scrollTop = $('#mensagens').scrollHeight;
        } else if (evento.tipo === 'fontes') {
          // Precisa vir ANTES do primeiro token: sem o mapa, o [[print:N]] que
          // chegar em seguida não teria como ser resolvido.
          Object.assign(printsDaResposta, evento.prints || {});
          renderizarFontes(bolha, evento.fontes);
          // A busca documental pode acrescentar fontes no meio do turno, depois
          // de o texto já ter começado. Sem redesenhar, o [[print:N]] que veio
          // dela ficaria como texto cru no que já está na tela.
          if (acumulado) corpo.innerHTML = renderizarMarkdown(acumulado, printsDaResposta);
        } else if (evento.tipo === 'ferramenta') {
          registrarConsultas(bolha, evento.chamadas);
        } else if (evento.tipo === 'erro') {
          houveErro = true;
          mensagemErro = evento.mensagem;
        } else if (evento.tipo === 'fim') {
          corpo.classList.remove('cursor-digitando');
          encerrarConsultas(bolha);
          if (acumulado) corpo.innerHTML = renderizarMarkdown(acumulado, printsDaResposta);
          // O erro é ANEXADO, nunca substitui: quando o modelo já tinha escrito
          // metade da análise, jogar o texto fora é pior que mostrá-lo com o
          // aviso de que a resposta foi interrompida.
          if (houveErro || evento.tem_erro) {
            corpo.innerHTML +=
              `<div class="mt-2 rounded border border-erro/40 bg-erro/10 p-2 text-xs text-erro">${escaparHtml(mensagemErro || 'A resposta foi interrompida antes de terminar.')}</div>`;
          }
          // mensagem_id só existe depois que a resposta foi gravada; é ele que
          // amarra o 👍/👎 a esta resposta. Vem 0 quando o salvamento falha.
          if (evento.mensagem_id && !houveErro && !evento.tem_erro) {
            renderizarAcoes(bolha, evento.mensagem_id, null);
          }
        }
      });
    } catch (erro) {
      corpo.innerHTML =
        `<div class="rounded border border-erro/40 bg-erro/10 p-2 text-xs text-erro">${escaparHtml(erro.message || 'Falha ao falar com o agente.')}</div>`;
    } finally {
      corpo.classList.remove('cursor-digitando');
      // Também aqui: se o turno morreu no meio, a pastilha não pode ficar
      // pulsando "consultando" para sempre.
      encerrarConsultas(bolha);
      estado.enviando = false;
      $('#btn-enviar').disabled = false;
      $('#mensagens').scrollTop = $('#mensagens').scrollHeight;
    }
  }

  async function enviarComStreaming(carga, aoEvento) {
    let resposta = null;
    if (estado.usarStreaming) {
      try {
        resposta = await fetch('/api/ia/chat', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(carga),
        });
      } catch (_) {
        resposta = null;
      }
    }

    if (!resposta || !resposta.ok || !resposta.body) {
      if (estado.usarStreaming) {
        estado.usarStreaming = false;
        toast('Streaming indisponível (use ./run.sh). Respondendo sem streaming.', 'aviso', 7000);
      }
      const dados = await API.post('/api/agente/chat-sync/', carga);
      aoEvento({ tipo: 'inicio', conversa_id: dados.conversa_id });
      const msg = dados.mensagem || {};
      // O fallback devolve tudo de uma vez; traduzimos para os mesmos eventos
      // do SSE para que o resto do fluxo (prints, feedback) não se importe com
      // qual caminho respondeu.
      if (msg.fontes && msg.fontes.length) {
        aoEvento({ tipo: 'fontes', fontes: msg.fontes, prints: msg.prints || {} });
      } else if (msg.prints) {
        aoEvento({ tipo: 'fontes', fontes: [], prints: msg.prints });
      }
      if (msg.conteudo) aoEvento({ tipo: 'token', texto: msg.conteudo });
      if (msg.erro) aoEvento({ tipo: 'erro', mensagem: msg.erro });
      aoEvento({ tipo: 'fim', mensagem_id: msg.id, tem_erro: Boolean(msg.erro) });
      return;
    }

    const leitor = resposta.body.getReader();
    const decodificador = new TextDecoder();
    let buffer = '';

    while (true) {
      const { done, value } = await leitor.read();
      if (done) break;
      buffer += decodificador.decode(value, { stream: true });
      const blocos = buffer.split('\n\n');
      buffer = blocos.pop();
      for (const bloco of blocos) {
        const linha = bloco.split('\n').find((l) => l.startsWith('data:'));
        if (!linha) continue;
        try { aoEvento(JSON.parse(linha.slice(5).trim())); } catch (_) { /* parcial */ }
      }
    }
  }

  /* ====================================================================== */
  /*  DIVISÓRIA CHAT × COMPARAÇÃO                                           */
  /* ====================================================================== */
  // A mecânica de arrastar mora em comum.js — a tela do consultor usa a mesma.
  const configurarDivisorPainel = () =>
    configurarDivisor({
      area: '#area-painel',
      divisor: '#divisor',
      chave: 'sancon_largura_chat',
    });

  /* ====================================================================== */
  /*  LIGHTBOX DO PRINT                                                     */
  /* ====================================================================== */
  /**
   * 76 de cada 100 imagens da base são miniaturas do MadCap Flare
   * (`…_thumb_0_48.png`). No Flare o arquivo cheio é o mesmo caminho sem o
   * sufixo — ampliar a miniatura entregaria um borrão, que é justamente a dor
   * que o lightbox veio resolver. Se o palpite falhar, o onerror volta para a
   * miniatura: pior caso é o comportamento de antes.
   */
  function urlAmpliada(url) {
    return String(url || '').replace(/_thumb_\d+_\d+(?=\.[a-z]+$)/i, '');
  }

  function abrirLightbox(ancora) {
    const original = ancora.getAttribute('href') || '';
    const img = $('#imagem-print');
    const ampliada = urlAmpliada(original);

    // O link começa no endereço que sabemos existir e só é promovido para o
    // ampliado quando a imagem carrega — assim ele nunca aponta para uma URL
    // adivinhada que o próprio onerror já provou não existir.
    $('#link-print').href = original;
    img.onload = () => { $('#link-print').href = img.src; };
    img.onerror = () => {
      img.onerror = null;
      img.src = original; // o Flare nem sempre publica a versão cheia
    };
    img.src = ampliada;

    const legenda = ancora.querySelector('img');
    $('#legenda-print').textContent = (legenda && legenda.alt) || '';

    $('#modal-print').classList.remove('hidden');
    $('#modal-print').classList.add('flex');
  }

  function fecharModais() {
    $$('.overlay-modal').forEach((m) => {
      m.classList.add('hidden');
      m.classList.remove('flex');
    });
    // O #modal-nota é anterior ao padrão .overlay-modal.
    $('#modal-nota').classList.add('hidden');
    $('#modal-nota').classList.remove('flex');
  }

  /* ====================================================================== */
  /*  FEEDBACK DA RESPOSTA                                                  */
  /* ====================================================================== */
  const MOTIVOS = [
    ['tela_errada', 'Tela errada'],
    ['sem_fundamento', 'Sem fundamento'],
    ['incompleta', 'Faltou divergência'],
    ['formato', 'Formato ruim'],
    ['outro', 'Outro'],
  ];

  /**
   * Os botões vivem numa div IRMÃ de `.corpo-resposta`: o corpo é reescrito a
   * cada token do streaming e levaria junto qualquer elemento interativo.
   */
  function renderizarAcoes(bolha, mensagemId, avaliacaoAtual) {
    const area = bolha.querySelector('.area-acoes');
    if (!area || !mensagemId) return;

    area.dataset.mensagemId = String(mensagemId);
    area.innerHTML = `
      <button class="btn-feedback btn-avaliar${avaliacaoAtual === 1 ? ' ativo-positivo' : ''}"
              data-valor="1" title="Resposta útil">👍</button>
      <button class="btn-feedback btn-avaliar${avaliacaoAtual === -1 ? ' ativo-negativo' : ''}"
              data-valor="-1" title="Resposta ruim">👎</button>
      <span class="area-motivo"></span>`;
  }

  /** O 👎 abre os motivos: "não gostei" sem o porquê não vira correção. */
  function pedirMotivo(area) {
    const alvo = area.querySelector('.area-motivo');
    if (!alvo) return;
    alvo.innerHTML =
      '<span class="ml-1 text-[10px] text-aco-400">o que saiu errado?</span> ' +
      MOTIVOS.map(
        ([valor, rotulo]) =>
          `<button class="btn-feedback btn-motivo ml-1" data-motivo="${valor}">${rotulo}</button>`
      ).join('');
  }

  async function avaliar(area, valor, motivo) {
    const id = area.dataset.mensagemId;
    if (!id) return;

    const botoes = Array.from(area.querySelectorAll('.btn-avaliar'));
    botoes.forEach((b) => (b.disabled = true));
    try {
      await API.post(`/api/agente/mensagens/${id}/avaliacao/`, {
        valor,
        motivo: motivo || '',
      });
      botoes.forEach((b) => {
        const meu = Number(b.dataset.valor) === valor;
        b.classList.toggle('ativo-positivo', meu && valor === 1);
        b.classList.toggle('ativo-negativo', meu && valor === -1);
      });
      if (valor === -1 && !motivo) {
        pedirMotivo(area);
      } else {
        const alvo = area.querySelector('.area-motivo');
        if (alvo) { alvo.innerHTML = '<span class="ml-1 text-[10px] text-aco-400">obrigado!</span>'; }
      }
    } catch (erro) {
      toast(erro.message || 'Não consegui registrar sua avaliação.', 'erro');
    } finally {
      botoes.forEach((b) => (b.disabled = false));
    }
  }

  /* ====================================================================== */
  /*  HISTÓRICO DE CONVERSAS                                                */
  /* ====================================================================== */
  function cartaoConversa(conversa) {
    const quando = formatarData(conversa.atualizado_em);
    const contexto = conversa.tem_contexto
      ? '<span class="rounded-full bg-navy-50 px-1.5 py-0.5 text-[10px] text-navy-700">com comparação</span>'
      : '<span class="rounded-full bg-aco-100 px-1.5 py-0.5 text-[10px] text-aco-500">sem contexto</span>';
    const plural = conversa.total_mensagens === 1 ? 'mensagem' : 'mensagens';

    return `
      <div class="flex items-center gap-2 rounded-lg border border-aco-200 p-2.5 transition hover:border-navy-300 hover:bg-navy-50/40">
        <button class="abrir-conversa min-w-0 flex-1 text-left" data-id="${conversa.id}">
          <p class="truncate text-xs font-medium text-aco-800">${escaparHtml(conversa.titulo)}</p>
          <p class="mt-0.5 flex items-center gap-1.5 text-[10px] text-aco-400">
            ${quando} · ${conversa.total_mensagens} ${plural} ${contexto}
          </p>
        </button>
        <button class="excluir-conversa flex-none rounded p-1 text-aco-300 transition hover:bg-erro/10 hover:text-erro"
                data-id="${conversa.id}" data-titulo="${escaparHtml(conversa.titulo)}"
                title="Excluir conversa">
          <svg class="h-3.5 w-3.5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round"
                  d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/>
          </svg>
        </button>
      </div>`;
  }

  async function carregarConversas() {
    const area = $('#lista-conversas');
    area.innerHTML = '<p class="p-4 text-center text-xs text-aco-400">Carregando…</p>';
    $('#modal-conversas').classList.remove('hidden');
    $('#modal-conversas').classList.add('flex');

    try {
      const conversas = await API.get('/api/agente/conversas/?limite=50');
      area.innerHTML = conversas.length
        ? conversas.map(cartaoConversa).join('')
        : '<div class="rounded-lg border border-dashed border-aco-300 p-6 text-center text-xs text-aco-400">Nenhuma conversa ainda. As que você tiver aqui aparecem depois da primeira pergunta ao agente.</div>';
    } catch (erro) {
      area.innerHTML = `<p class="p-4 text-center text-xs text-erro">${escaparHtml(erro.message || 'Falha ao carregar.')}</p>`;
    }
  }

  /**
   * Reabre uma conversa: repõe as bolhas, as fontes, os prints e o estado dos
   * botões de feedback.
   *
   * Cada resposta é renderizada com o SEU mapa de prints (`m.prints`) — a
   * numeração recomeça a cada resposta, então usar o mapa global do streaming
   * faria uma resposta antiga exibir o print de outra.
   */
  async function abrirConversa(id) {
    // Trocar de conversa no meio do streaming descartaria a resposta em
    // andamento sem cancelar o stream — os tokens continuariam chegando e
    // escrevendo numa bolha que não existe mais.
    if (estado.enviando) {
      toast('Aguarde o agente terminar de responder.', 'aviso');
      return;
    }

    try {
      const dados = await API.get(`/api/agente/conversas/${id}/`);
      estado.conversaId = dados.id;
      $('#mensagens').innerHTML = '';

      // Ressincronizar o contexto da aba com o da conversa reaberta. Sem isto,
      // a próxima pergunta iria com o lote/comparação que estava aberto na aba
      // e o servidor RE-VINCULARIA a conversa a ele: resposta gerada sobre o
      // relatório errado e o vínculo original perdido no banco.
      estado.comparacaoId = dados.comparacao_id || null;
      estado.lote.id = dados.lote_id || null;
      estado.lote.consolidado = null;

      (dados.mensagens || []).forEach((m) => {
        if (m.papel === 'usuario') {
          // Os botões de análise mandam um prompt longo para o modelo e
          // mostram uma frase curta na tela; no replay vale o que foi mostrado.
          adicionarBolha('usuario', m.rotulo || m.conteudo);
          return;
        }
        const bolha = adicionarBolha('agente', '', {
          html: renderizarMarkdown(m.conteudo, m.prints || {}),
        });
        if (m.fontes && m.fontes.length) renderizarFontes(bolha, m.fontes);
        // Resposta que falhou não é avaliável — o caminho ao vivo já não
        // oferece os botões nesse caso.
        if (!m.erro) renderizarAcoes(bolha, m.id, m.avaliacao);
      });

      liberarChat(dados.contexto_ativo ? 'conversa reaberta' : '');
      if (!dados.contexto_ativo) {
        // Sem isto, o badge continuaria anunciando a comparação da aba, que não
        // tem nada a ver com a conversa que acabou de ser aberta.
        $('#badge-contexto').classList.add('hidden');
        toast(
          'Conversa reaberta sem contexto: a comparação original não está mais disponível.',
          'aviso',
          7000
        );
      }
      fecharModais();
      $('#mensagens').scrollTop = $('#mensagens').scrollHeight;
    } catch (erro) {
      toast(erro.message || 'Não consegui abrir a conversa.', 'erro');
    }
  }

  async function excluirConversa(id, elemento) {
    try {
      await API.delete(`/api/agente/conversas/${id}/`);
      elemento.remove();
      if (estado.conversaId === id) estado.conversaId = null;
      toast('Conversa excluída.', 'sucesso', 3000);
    } catch (erro) {
      toast(erro.message || 'Não consegui excluir.', 'erro');
    }
  }

  /* ====================================================================== */
  /*  PROVEDORES                                                            */
  /* ====================================================================== */
  /**
   * O modelo é escolhido uma vez em Configurações, não a cada conversa —
   * trocar de modelo no meio da análise só produz respostas inconsistentes.
   * Aqui apenas mostramos qual está em uso.
   */
  async function carregarProvedores() {
    try {
      const dados = await API.get('/api/agente/provedores/');
      const indicador = $('#indicador-modelo');
      const emUso =
        (dados.provedores || []).find((p) => p.id === dados.padrao_id) ||
        (dados.provedores || [])[0];

      if (!emUso) {
        indicador.textContent = 'nenhum modelo configurado';
        // Âmbar SÓLIDO com texto charcoal (on-warning do DS): o indicador vive
        // no cabeçalho navy, onde fundo translúcido claro some e texto escuro
        // fica ilegível.
        indicador.className =
          'ml-3 hidden rounded-full bg-atencao px-3 py-1 text-[11px] font-semibold text-aco-800 sm:inline-block';
        toast('Nenhum modelo de IA configurado. Vá em Configurações.', 'aviso', 9000);
      } else {
        indicador.textContent = emUso.modelo_label || emUso.modelo;
      }
    } catch (_) { /* silencioso */ }
  }

  /* ====================================================================== */
  /*  EVENTOS                                                               */
  /* ====================================================================== */
  function configurarEventos() {
    // --- lote -------------------------------------------------------------
    $('#btn-parear').addEventListener('click', parearLote);
    $('#btn-comparar-lote').addEventListener('click', compararLote);
    $('#btn-vincular').addEventListener('click', vincularManual);
    configurarSelecaoSemPar();
    $('#btn-ver-sem-par').addEventListener('click', () =>
      $('#area-sem-par').classList.toggle('hidden')
    );
    $('#ordem-pares').addEventListener('change', (e) => {
      estado.lote.ordem = e.target.value;
      renderizarPareamento();
    });

    $('#btn-enviar-lote-agente').addEventListener('click', () => {
      if (!estado.lote.consolidado) { toast('Rode a comparação primeiro.', 'aviso'); return; }
      const p = estado.lote.consolidado.placar;
      // O consultor vê uma frase curta no chat; o modelo recebe a instrução
      // completa, e o relatório com todas as divergências chega pelo lote_id
      // já no servidor — nada disso aparece na tela.
      enviarMensagem(
        `Comparei ${p.notas_comparadas} nota(s) emitidas nos dois sistemas. O relatório ` +
          `consolidado com as ${p.total_causas} causa(s) recorrente(s) está anexado. Me diga, ` +
          'em ordem de prioridade, o que preciso ajustar na parametrização do Senior para que ' +
          'as notas passem a sair no mesmo padrão fiscal do sistema atual do cliente.',
        { rotuloUsuario: 'Analise as divergências' }
      );
    });

    $('#btn-relatorio-detalhado').addEventListener('click', () => {
      if (!estado.lote.id) { toast('Rode a comparação primeiro.', 'aviso'); return; }
      // Documento gerado pelo comparador (sem IA) — abre em aba nova e o
      // consultor imprime em PDF pelo próprio navegador.
      window.open(`/api/comparador/lotes/${estado.lote.id}/relatorio/`, '_blank', 'noopener');
    });

    $$('.aba-resultado').forEach((botao) => {
      botao.addEventListener('click', () => {
        $$('.aba-resultado').forEach((b) => {
          const ativo = b === botao;
          b.className =
            'aba-resultado border-b-2 px-3 py-1.5 text-xs font-medium ' +
            (ativo ? 'border-navy-500 text-navy-700' : 'border-transparent text-aco-500 hover:text-aco-700');
        });
        $$('.vista-resultado').forEach((vista) =>
          vista.classList.toggle('hidden', vista.dataset.vista !== botao.dataset.vista)
        );
      });
    });

    $('#btn-fechar-modal').addEventListener('click', () => {
      $('#modal-nota').classList.add('hidden');
      $('#modal-nota').classList.remove('flex');
    });
    $('#modal-nota').addEventListener('click', (e) => {
      if (e.target === $('#modal-nota')) {
        $('#modal-nota').classList.add('hidden');
        $('#modal-nota').classList.remove('flex');
      }
    });

    $('#btn-limpar-tudo').addEventListener('click', () => location.reload());

    // --- nota a nota ------------------------------------------------------
    $('#btn-comparar').addEventListener('click', comparar);

    $('#btn-enviar-agente').addEventListener('click', () => {
      if (!estado.comparacaoId) { toast('Execute uma comparação primeiro.', 'aviso'); return; }
      enviarMensagem(
        'Analise o relatório de comparação anexado e me diga, em ordem de prioridade, o que ' +
          'preciso ajustar na parametrização do Senior para que a nota saia no mesmo padrão ' +
          'fiscal do sistema atual do cliente.',
        { rotuloUsuario: '📋 Analisar o resultado da comparação' }
      );
    });

    $('#btn-relatorio-unico').addEventListener('click', () => {
      if (!estado.comparacaoId) { toast('Execute uma comparação primeiro.', 'aviso'); return; }
      window.open(`/api/comparador/${estado.comparacaoId}/relatorio/`, '_blank', 'noopener');
    });

    $$('.filtro-sev').forEach((botao) => {
      botao.addEventListener('click', () => {
        estado.filtroSeveridade = botao.dataset.sev;
        $$('.filtro-sev').forEach((b) => {
          const ativo = b === botao;
          b.className =
            'filtro-sev rounded-full px-2.5 py-0.5 text-[11px] ' +
            (ativo
              ? 'border border-navy-300 bg-navy-50 font-medium text-navy-700'
              : 'border border-aco-200 text-aco-600');
        });
        renderizarDivergencias();
      });
    });

    $('#busca-divergencia').addEventListener('input', (e) => {
      estado.busca = e.target.value;
      renderizarDivergencias();
    });

    // --- chat -------------------------------------------------------------
    $('#btn-enviar').addEventListener('click', () => enviarMensagem());

    const entrada = $('#entrada-mensagem');
    entrada.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); enviarMensagem(); }
    });
    entrada.addEventListener('input', () => {
      entrada.style.height = 'auto';
      entrada.style.height = Math.min(entrada.scrollHeight, 160) + 'px';
    });

    $('#btn-nova-conversa').addEventListener('click', () => {
      estado.conversaId = null;
      $('#mensagens').innerHTML = '';
      adicionarBolha('agente', 'Nova conversa iniciada. O contexto da comparação continua anexado.');
    });

    // --- histórico --------------------------------------------------------
    $('#btn-historico').addEventListener('click', carregarConversas);
    $('#btn-fechar-conversas').addEventListener('click', fecharModais);
    $('#modal-conversas').addEventListener('click', (e) => {
      if (e.target === $('#modal-conversas')) fecharModais();
    });

    $('#lista-conversas').addEventListener('click', (e) => {
      const abrir = e.target.closest('.abrir-conversa');
      if (abrir) { abrirConversa(abrir.dataset.id); return; }

      const excluir = e.target.closest('.excluir-conversa');
      if (excluir) {
        // A exclusão é definitiva e leva as mensagens junto (cascata), e o
        // histórico é da equipe inteira — quem apaga pode não ser quem
        // perguntou. Sem confirmação, um clique errado na lixeira (que fica a
        // poucos pixels do "abrir") não tem volta.
        const titulo = excluir.dataset.titulo || 'esta conversa';
        if (!confirm(`Excluir "${titulo}"?\n\nA conversa e todas as suas mensagens serão apagadas para toda a equipe. Não dá para desfazer.`)) return;
        excluirConversa(excluir.dataset.id, excluir.parentElement);
      }
    });

    // --- lightbox e feedback (delegação) ----------------------------------
    // Precisa ser delegado: `.corpo-resposta` é reescrito a cada token e o
    // histórico recria as bolhas — handler preso ao elemento morreria junto.
    $('#mensagens').addEventListener('click', (e) => {
      const print = e.target.closest('.bloco-print');
      if (print) {
        e.preventDefault(); // não abrir a aba nova: agora amplia aqui
        abrirLightbox(print);
        return;
      }

      const area = e.target.closest('.area-acoes');
      if (!area) return;

      const voto = e.target.closest('.btn-avaliar');
      if (voto) { avaliar(area, Number(voto.dataset.valor)); return; }

      const motivo = e.target.closest('.btn-motivo');
      if (motivo) avaliar(area, -1, motivo.dataset.motivo);
    });

    $('#btn-fechar-print').addEventListener('click', fecharModais);
    $('#modal-print').addEventListener('click', (e) => {
      // Clicar na própria imagem também fecha (cursor zoom-out sinaliza isso).
      if (e.target === $('#modal-print') || e.target === $('#imagem-print')) fecharModais();
    });

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') fecharModais();
    });
  }

  /* ------------------------------------------------------------- início -- */
  document.addEventListener('DOMContentLoaded', () => {
    configurarModos();
    configurarDropzones();
    configurarEventos();
    configurarDivisorPainel();
    carregarProvedores();
  });
})();
