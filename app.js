'use strict';

const $ = id => document.getElementById(id);
const PT_TO_EN = {
  'Gênesis':'Genesis','Êxodo':'Exodus','Levítico':'Leviticus','Números':'Numbers','Deuteronômio':'Deuteronomy','Josué':'Joshua','Juízes':'Judges','Rute':'Ruth','1 Samuel':'1 Samuel','2 Samuel':'2 Samuel','1 Reis':'1 Kings','2 Reis':'2 Kings','1 Crônicas':'1 Chronicles','2 Crônicas':'2 Chronicles','Esdras':'Ezra','Neemias':'Nehemiah','Ester':'Esther','Jó':'Job','Salmos':'Psalms','Provérbios':'Proverbs','Eclesiastes':'Ecclesiastes','Cânticos':'Song of Songs','Isaías':'Isaiah','Jeremias':'Jeremiah','Lamentações':'Lamentations','Ezequiel':'Ezekiel','Daniel':'Daniel','Oséias':'Hosea','Joel':'Joel','Amós':'Amos','Obadias':'Obadiah','Jonas':'Jonah','Miqueias':'Micah','Naum':'Nahum','Habacuque':'Habakkuk','Sofonias':'Zephaniah','Ageu':'Haggai','Zacarias':'Zechariah','Malaquias':'Malachi','Mateus':'Matthew','Marcos':'Mark','Lucas':'Luke','João':'John','Atos':'Acts','Romanos':'Romans','1 Coríntios':'1 Corinthians','2 Coríntios':'2 Corinthians','Gálatas':'Galatians','Efésios':'Ephesians','Filipenses':'Philippians','Colossenses':'Colossians','1 Tessalonicenses':'1 Thessalonians','2 Tessalonicenses':'2 Thessalonians','1 Timóteo':'1 Timothy','2 Timóteo':'2 Timothy','Tito':'Titus','Filemom':'Philemon','Hebreus':'Hebrews','Tiago':'James','1 Pedro':'1 Peter','2 Pedro':'2 Peter','1 João':'1 John','2 João':'2 John','3 João':'3 John','Judas':'Jude','Apocalipse':'Revelation'
};
const people = [
  ['Moisés','moises',2,3,'Líder de Israel'],['Davi','davi',19,23,'Rei e salmista'],['Ester','ester',17,4,'Rainha corajosa'],
  ['Paulo','paulo',45,8,'Apóstolo de Jesus'],['Maria','maria',42,1,'Mãe de Jesus'],['Daniel','daniel',27,6,'Fiel a Deus'],
  ['João','joao',43,1,'Discípulo amado'],['Pedro','pedro',60,1,'Pescador de almas'],['Rute','rute',8,1,'Exemplo de lealdade'],
  ['Isaías','isaias',23,53,'Profeta do Senhor'],['Débora','debora',7,4,'Juíza e profetisa'],['Timóteo','timoteo',54,4,'Jovem na fé']
];
const templates = ['classic','editorial','carousel','portrait','community','feature'];
const backgrounds = ['tone-1','tone-2','tone-3','tone-4','tone-5','tone-6'];
const hooks = ['Palavra do dia','Para refletir','Leitura da manhã','Verso para guardar','Pausa com Deus','Meditação bíblica'];
const prompts = ['O que Deus está te mostrando aqui?','Qual palavra mais falou com você?','Ore com base neste trecho.','Leve este versículo para o seu dia.','Guarde esta verdade no coração.','Compartilhe esta leitura com alguém.'];
const sponsorLines = ['Plano bíblico em 7 dias','Comece sua jornada diária','Leitura guiada para esta semana','Devocional com continuidade automática'];

let books = [], booksEn = [], enIndex = new Map(), entries = [], onlySaved = false;
let likes = new Set(safeJSON('bf_likes', [])), saved = new Set(safeJSON('bf_saved', []));
let opts = safeJSON('bf_settings', {book: 41, chapter: 7, mode: 'group', font: 0});

function safeJSON(k, d){ try { return JSON.parse(localStorage.getItem(k)) ?? d; } catch { return d; } }
function save(k,v){ localStorage.setItem(k, JSON.stringify(v)); }
function esc(v){ return String(v).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c])); }
function toast(s){ $('toast').textContent = s; $('toast').style.display='block'; clearTimeout(toast.timer); toast.timer = setTimeout(()=>$('toast').style.display='none', 2400); }
function ref(v){ return `${v.book} ${v.chapter}:${v.first}${v.last!==v.first?'–'+v.last:''}`; }
function refEn(v){ const name = PT_TO_EN[v.book] || v.book; return `${name} ${v.chapter}:${v.first}${v.last!==v.first?'-'+v.last:''}`; }
function key(v){ return `${v.bookId}:${v.chapter}:${v.first}:${v.last}`; }
function textOf(v){ return v.items.map(x=>x.text).join(' '); }
function verseHtml(v){ return v.items.map(x => `<span class="vnum">v${x.number}</span> ${esc(x.text)}`).join(' '); }
function textWithVerseNums(v){ return v.items.map(x => `v${x.number} ${x.text}`).join(' '); }
function enTextOf(v){ return (v.itemsEn || []).map(x=>x.text).join(' '); }
function hash(str){ let h = 0; for (let i=0;i<str.length;i++) h = ((h<<5)-h) + str.charCodeAt(i), h |= 0; return Math.abs(h); }
function stats(v){ const h = hash(key(v)); const likes = (h % 3200) + 80; return { likes, likesText: likes.toLocaleString('pt-BR'), comments: (h % 240) + 8 }; }
function themeFor(i,v){ return { template: templates[i % templates.length], bg: backgrounds[(i + v.bookId) % backgrounds.length], hook: hooks[(i + v.chapter) % hooks.length], prompt: prompts[(i + v.first) % prompts.length], sponsor: sponsorLines[(i + v.last) % sponsorLines.length] }; }

function buildEnIndex(){
  enIndex = new Map();
  for (const b of booksEn) {
    for (const c of b.chapters || []) {
      for (const verse of c.verses || []) {
        enIndex.set(`${b.id}:${c.number}:${verse.number}`, verse.text);
      }
    }
  }
}

function buildEntries(){
  entries = [];
  const b = books.find(x => x.id === Number(opts.book)); if (!b) return;
  const c = b.chapters[Number(opts.chapter)-1]; if (!c) return;
  const n = opts.mode === 'verse' ? 1 : opts.mode === 'five' ? 5 : 3;
  for (let i=0; i<c.verses.length; i+=n) {
    const chunk = c.verses.slice(i, i+n);
    const chunkEn = chunk.map(v => ({ number: v.number, text: enIndex.get(`${b.id}:${c.number}:${v.number}`) || '' }));
    entries.push({ bookId:b.id, book:b.name, chapter:c.number, first:chunk[0].number, last:chunk.at(-1).number, items:chunk, itemsEn:chunkEn });
  }
  if (onlySaved) entries = entries.filter(v => saved.has(key(v)));
}

function renderCountLine(v, meta){
  if (meta.template === 'community') return `<div class="socialline">Curtido por <strong>comunidade_biblica</strong> e outras ${esc(meta.stats.likesText)} pessoas</div>`;
  if (meta.template === 'feature') return `<div class="socialline">Destaque · ${esc(meta.sponsor)}</div>`;
  return `<div class="socialline">Curtido por <strong>palavra_do_dia</strong> e outras ${esc(meta.stats.likesText)} pessoas</div>`;
}

function renderFooterTranslation(v){
  const items = (v.itemsEn || []).filter(x => x.text && x.text.trim());
  if (!items.length) return `<div class="translationbox warning"><div class="translationhead"><span>English comparison</span><b>KJV</b></div><div class="translationtext">A tradução KJV será baixada automaticamente na primeira execução com internet disponível.</div></div>`;
  const formatted = items.map(x => `<span class="vnum">v${x.number}</span> ${esc(x.text)}`).join(' ');
  return `<div class="translationbox"><div class="translationhead"><span>English comparison</span><b>KJV</b></div><div class="translationtext">${formatted}</div><div class="translationref">${esc(refEn(v))}</div></div>`;
}

// Seleção da cena: cada cena do manifesto (assets/scenes/manifest.json) pontua pelas palavras
// que aparecem nos primeiros termos do trecho; a variação (dia/amanhecer/entardecer/noite) vem do hash.
const SCENE_WINDOW = 30;
const STOP = new Set(('a o as os um uma uns umas de do da dos das em no na nos nas por para com sem sob sobre entre ate e ou mas que se como quando onde quem qual quais porque pois porem nem ja ainda tambem so mais menos muito muita muitos muitas todo toda todos todas tudo nada ele ela eles elas eu tu vos voce meu minha meus minhas teu tua teus tuas seu sua seus suas nosso nossa vosso vossa este esta isto esse essa isso aquele aquela aquilo ao aos pelo pela pelos pelas num numa dele dela deles delas me te lhe lhes mim ti si ser sou es somos sao era eram foi foram sera seja fosse ter tem tenho temos tinha teve haver ha havia houve estar esta estao estava fazer faz fez ir vai vao vir veio disse dizer nao sim ai aqui ali la ca entao assim depois antes cada outro outra outros outras mesmo mesma tal tanto tao nenhum nenhuma dar deu eis'.split(' ')));
const FALLBACK_SCENES = ['ceu','montanhas','rio','campo','jardim','mar','nuvens','colina','lago','floresta'];
let sceneExact = new Map(), scenePrefix = new Map(), sceneInfo = new Map();

function norm(w){ return w.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, ''); }
function buildSceneIndex(manifest){
  sceneExact = new Map(); scenePrefix = new Map(); sceneInfo = new Map();
  for (const m of manifest) {
    sceneInfo.set(m.key, m);
    for (const w of m.words) {
      const map = w.endsWith('*') ? scenePrefix : sceneExact;
      const k = w.replace('*', '');
      if (!map.has(k)) map.set(k, []);
      map.get(k).push(m);
    }
  }
}
function matchesFor(token){
  const out = [...(sceneExact.get(token) || [])];
  for (let n = 2; n <= token.length; n++) out.push(...(scenePrefix.get(token.slice(0, n)) || []));
  return out;
}
function sceneFor(v){
  const tokens = (norm(textOf(v)).match(/[a-z]+/g) || []).filter(w => w.length > 2 && !STOP.has(w)).slice(0, SCENE_WINDOW);
  const score = new Map();
  tokens.forEach((tk, i) => {
    const w = 1 + (SCENE_WINDOW - i) / (2 * SCENE_WINDOW);   // termos iniciais pesam um pouco mais
    for (const m of new Set(matchesFor(tk))) score.set(m.key, (score.get(m.key) || 0) + m.prio * w);
  });
  let best = null, bestScore = 0;
  for (const [k, sc] of score) if (sc > bestScore || (sc === bestScore && hash(k + key(v)) % 2)) { best = k; bestScore = sc; }
  const h = hash(key(v));
  if (!best) best = FALLBACK_SCENES[h % FALLBACK_SCENES.length];
  const info = sceneInfo.get(best);
  const variants = info ? info.variants || 1 : 1;
  const vi = Math.floor(h / 7) % variants;
  return { label: info ? info.label : best, url: `/assets/scenes/${best}${vi ? '_v' + vi : ''}.svg` };
}
function renderCardInner(v, meta){
  const txt = verseHtml(v);
  const scene = sceneFor(v);
  const imgstyle = `style="--scene-image:url('${scene.url}')"`;
  const verse = `<div class="versecontent"><div class="refupper">${esc(ref(v))}</div><div class="versewords" style="--font-adjust:${Number(opts.font)||0}px">${txt}</div><div class="refbottom">${esc(ref(v))}</div></div>`;
  const id = (meta.entryIndex || 0) % 6;
  // Every sixth post is a different *composition*, not a recoloring of the same square.
  if(id===0) return `<div class="art art-photo scene-a" ${imgstyle}><div class="art-image" role="img" aria-label="Imagem temática: ${esc(scene.label)}"></div><span class="art-pill">Leitura bíblica</span>${verse}</div>`;
  if(id===1) return `<div class="art art-editorial"><div class="editorial-top"><span>BÍBLIA FEED / PALAVRA VIVA</span><span>02 — REFLEXÃO</span></div><div class="editorial-body"><div class="editorial-side">${esc(v.book)} · ${v.chapter}</div>${verse}</div><div class="editorial-landscape" ${imgstyle}><span>LEITURA • REFLEXÃO • FÉ</span></div></div>`;
  if(id===2) return `<div class="art art-carousel" data-slide="0" ${imgstyle}><div class="slide slide-photo"><div class="art-image scene-b" role="img" aria-label="Imagem temática: ${esc(scene.label)}"></div>${verse}</div><div class="slide slide-paper" hidden><div class="slide-kicker">VERSÃO ORIGINAL DO FEED</div>${verse}</div><div class="slide slide-portrait" hidden><div class="portrait-frame"><img src="${scene.url}" alt="Ilustração temática: ${esc(scene.label)}"></div>${verse}</div><div class="slide-arrows"><button class="prev-slide" aria-label="Slide anterior">‹</button><button class="next-slide" aria-label="Próximo slide">›</button></div><span class="slide-count">1/3</span></div>`;
  if(id===3) return `<div class="art art-portrait"><div class="portrait-visual"><img src="${scene.url}" alt="Ilustração temática: ${esc(scene.label)}"><span>${esc(scene.label).toUpperCase()}</span></div><div class="portrait-text">${verse}</div></div>`;
  if(id===4) return `<div class="art art-collage"><div class="collage-grid"><div class="collage-one"><img src="${scene.url}" alt="Imagem temática"></div><div class="collage-two"><img src="${scene.url}" alt="Imagem temática"></div><div class="collage-three"><img src="${scene.url}" alt="Imagem temática"></div></div><div class="collage-verse">${verse}</div><span class="collage-label">Caderno de leitura</span></div>`;
  return `<div class="art art-feature"><div class="feature-head"><span>✧ BÍBLIA FEED</span><span>DESTAQUE DA LEITURA</span></div><div class="feature-center"><div class="feature-label">Uma palavra para o seu dia</div>${verse}</div><div class="feature-beams" ${imgstyle} role="img" aria-label="Imagem temática: ${esc(scene.label)}"></div><div class="feature-bottom">CONHECER · REFLETIR · PRATICAR</div></div>`;
}
function renderCaption(v, meta){
  const txt = textOf(v);
  const line = meta.template === 'sponsored'
    ? `Siga um plano de leitura e continue meditando em ${esc(ref(v))}.`
    : meta.template === 'community'
      ? `Muitos irmãos têm refletido sobre ${esc(ref(v))} hoje.`
      : meta.template === 'devotional'
        ? `${esc(meta.prompt)}`
        : `O que Deus está falando ao seu coração em ${esc(ref(v))}?`;
  return `
    <div class="caption"><strong>palavra_do_dia</strong>${esc(ref(v))} — ${esc(txt)}</div>
    <div class="microcopy">${line}</div>
    <div class="smallmuted">${esc(v.book)} · Capítulo ${v.chapter} · Almeida Livre</div>
    ${renderFooterTranslation(v)}`;
}

function postChrome(meta){
  if (meta.template === 'feature') {
    return `<div class="posthead"><div class="postavatar brand">✧</div><div><strong>bibliafeed_oficial</strong><small>Destaque · ${esc(meta.sponsor)}</small></div><button class="menu" aria-label="Opções de leitura">···</button></div>`;
  }
  if (meta.template === 'community') {
    return `<div class="posthead"><div class="postavatar community">☰</div><div><strong>comunidade_em_palavra</strong><small>Leitura compartilhada · ${esc(meta.hook)}</small></div><button class="menu" aria-label="Opções de leitura">···</button></div>`;
  }
  return `<div class="posthead"><div class="postavatar">✝</div><div><strong>palavra_do_dia</strong><small>Lendo a Bíblia juntos · ${esc(vBookAndChapter(meta.entry))}</small></div><button class="menu" aria-label="Opções de leitura">···</button></div>`;
}
function vBookAndChapter(v){ return `${v.book} ${v.chapter}`; }

function createPost(v, index){
  const id = key(v), txt = textOf(v), meta = themeFor(index, v); meta.stats = stats(v); meta.entry = v;
  meta.entryIndex = index;
  const card = document.createElement('article');
  card.className = `post post-${meta.template}`;
  card.innerHTML = `
    ${postChrome(meta)}
    ${renderCardInner(v, meta)}
    <div class="bar">
      <button class="action heart ${likes.has(id)?'liked':''}" aria-label="Curtir">${likes.has(id)?'♥':'♡'}</button>
      <button class="action comment" aria-label="Comentar">◌</button>
      <button class="action share" aria-label="Compartilhar">➤</button>
      <button class="action bookmark ${saved.has(id)?'saved':''}" aria-label="Salvar">${saved.has(id)?'▣':'⌑'}</button>
    </div>
    <div class="engagement"><span>${esc(meta.stats.likesText)} curtidas</span><span>${esc(String(meta.stats.comments))} comentários</span></div>
    ${renderCountLine(v, meta)}
    ${renderCaption(v, meta)}
    `;

  const update = () => {
    card.querySelector('.heart').textContent = likes.has(id) ? '♥' : '♡';
    card.querySelector('.heart').classList.toggle('liked', likes.has(id));
    card.querySelector('.bookmark').textContent = saved.has(id) ? '▣' : '⌑';
    card.querySelector('.bookmark').classList.toggle('saved', saved.has(id));
  };
  card.querySelector('.heart').onclick = () => { likes.has(id) ? likes.delete(id) : likes.add(id); save('bf_likes', [...likes]); update(); };
  card.querySelector('.bookmark').onclick = () => { saved.has(id) ? saved.delete(id) : saved.add(id); save('bf_saved', [...saved]); update(); toast(saved.has(id) ? 'Passagem salva' : 'Removido dos salvos'); };
  card.querySelector('.share').onclick = () => share(`${txt}\n— ${ref(v)}`);
  card.querySelector('.menu').onclick = () => share(`${txt}\n— ${ref(v)}`);
  card.querySelector('.comment').onclick = () => card.querySelector('.translationbox')?.scrollIntoView({behavior:'smooth', block:'center'});
  const cta = card.querySelector('[data-jump="chooser"]'); if (cta) cta.onclick = chooser;

  const carousel = card.querySelector('.art-carousel');
  if(carousel){
    let slide = 0;
    const panels = [...carousel.querySelectorAll('.slide')];
    const change = delta => { slide = (slide + delta + panels.length) % panels.length; panels.forEach((p,i)=>{p.hidden=i!==slide;}); carousel.querySelector('.slide-count').textContent = `${slide+1}/${panels.length}`; };
    carousel.querySelector('.prev-slide').onclick = ()=>change(-1);
    carousel.querySelector('.next-slide').onclick = ()=>change(1);
  }
  return card;
}

function showFeed(){
  buildEntries();
  $('posts').replaceChildren();
  if (!entries.length) {
    $('posts').innerHTML = '<div class="loading">Nenhuma passagem encontrada. Escolha outro capítulo ou salve um versículo.</div>';
    return;
  }
  const frag = document.createDocumentFragment();
  entries.forEach((e, i) => frag.append(createPost(e, i)));
  $('posts').append(frag);
}

async function share(text){
  try {
    if (navigator.share) await navigator.share({text});
    else { await navigator.clipboard.writeText(text); toast('Passagem copiada para compartilhar'); }
  } catch (e) { if (e.name !== 'AbortError') toast('Não foi possível compartilhar'); }
}

function jump(book, chapter){ opts.book = book; opts.chapter = chapter; onlySaved = false; save('bf_settings', opts); showFeed(); window.scrollTo({top:0, behavior:'smooth'}); }

function renderPeople(){
  for (const [name, asset, b, c] of people.slice(0,6)) {
    const btn = document.createElement('button');
    btn.className = 'story';
    btn.innerHTML = `<span class="ring"><img src="/assets/${asset}.png" alt="Retrato ilustrativo de ${name}"></span><label>${name}</label>`;
    btn.onclick = () => jump(b, c);
    $('stories').append(btn);
  }
  for (const [name, asset, b, c, description] of people.slice(6)) {
    const line = document.createElement('div');
    line.className = 'suggestion';
    line.innerHTML = `<img src="/assets/${asset}.png" alt="Retrato ilustrativo de ${name}"><div class="person"><b>${name}</b><small>${description}</small></div><button>Abrir</button>`;
    line.querySelector('button').onclick = () => jump(b, c);
    $('suggestions').append(line);
  }
}

function openDialog(title, html, setup){ $('dialogTitle').textContent = title; $('dialogBody').innerHTML = html; $('backdrop').classList.add('open'); if (setup) setup(); }
function closeDialog(){ $('backdrop').classList.remove('open'); }

function chooser(){
  openDialog('Minha leitura',
    `<p class="version-dialog">Bíblia Feed · versão 5.1</p><p>Selecione um livro e um capítulo. O feed alterna estilos de posts, mas mantém a leitura do capítulo escolhido.</p>
     <label for="book">Livro bíblico</label><select id="book"></select>
     <label for="chapter">Capítulo</label><select id="chapter"></select>
     <label for="mode">Tamanho das passagens</label>
     <select id="mode"><option value="verse">1 versículo por publicação</option><option value="group">3 versículos por publicação</option><option value="five">5 versículos por publicação</option></select>
     <label for="font">Tamanho da fonte</label><input id="font" type="range" min="-7" max="12" value="${opts.font||0}">
     <div class="buttons"><button class="btn primary" id="start">Abrir leitura</button><button class="btn" id="resume">Continuar leitura</button></div>`,
    ()=>{
      books.forEach(b => $('book').add(new Option(b.name,b.id)));
      $('book').value = opts.book; $('mode').value = opts.mode;
      const chapters = ()=>{
        const b = books.find(x=>x.id===Number($('book').value));
        $('chapter').replaceChildren();
        if (b) b.chapters.forEach(c => $('chapter').add(new Option('Capítulo ' + c.number, c.number)));
        $('chapter').value = Math.min(opts.chapter, b?.chapters.length || 1);
      };
      chapters();
      $('book').onchange = ()=>{ opts.chapter=1; chapters(); };
      $('start').onclick = ()=>{ opts = {book:Number($('book').value), chapter:Number($('chapter').value), mode:$('mode').value, font:Number($('font').value)}; save('bf_settings',opts); closeDialog(); showFeed(); scrollTo({top:0, behavior:'smooth'}); };
      $('resume').onclick = ()=>{ const x = safeJSON('bf_position',null); if (!x) return toast('Nenhuma leitura anterior registrada'); closeDialog(); jump(x.book,x.chapter); };
    }
  );
}

function explore(){
  openDialog('Explorar a Bíblia',
    '<p>Busque palavras e abra capítulos diretamente no seu feed.</p><label for="q">Buscar no texto bíblico</label><input id="q" placeholder="Ex.: amor, fé, esperança"><div class="results" id="results"></div>',
    ()=>{
      let timer;
      $('q').addEventListener('input', ()=>{ clearTimeout(timer); timer = setTimeout(search, 180); });
      function search(){
        const q = $('q').value.trim().toLocaleLowerCase('pt-BR');
        const results = $('results'); results.replaceChildren();
        if (q.length < 2) return;
        let count = 0;
        outer: for (const b of books) for (const c of b.chapters) for (const verse of c.verses) {
          if (verse.text.toLocaleLowerCase('pt-BR').includes(q)) {
            const row = document.createElement('button');
            row.textContent = `${b.name} ${c.number}:${verse.number} — ${verse.text.slice(0,105)}…`;
            row.onclick = ()=>{ closeDialog(); jump(b.id, c.number); };
            results.append(row);
            if (++count >= 35) break outer;
          }
        }
        if (!count) results.textContent = 'Nenhum resultado nesta pesquisa.';
      }
    }
  );
}

function action(which){
  document.querySelectorAll('.navitem').forEach(x => x.classList.toggle('active', x.dataset.action===which));
  if (which==='home'){ onlySaved = false; showFeed(); scrollTo(0,0); }
  if (which==='saved'){ onlySaved = true; showFeed(); scrollTo(0,0); }
  if (which==='search') explore();
  if (which==='settings' || which==='read') chooser();
  if (which==='random'){ const b = books[Math.floor(Math.random()*books.length)]; jump(b.id, 1); }
}

$('pick').onclick = chooser;
$('closeDialog').onclick = closeDialog;
$('backdrop').onclick = e => { if (e.target === $('backdrop')) closeDialog(); };
document.addEventListener('keydown', e => { if (e.key === 'Escape') closeDialog(); });
document.querySelectorAll('[data-action]').forEach(b => b.onclick = ()=>action(b.dataset.action));
$('allPeople').onclick = ()=>openDialog('Personagens bíblicos','<p>Escolha um personagem no topo da página ou na lista de sugestões. Cada perfil leva a uma passagem relacionada à história dele.</p>');
$('profileSwitch').onclick = e => { e.preventDefault(); chooser(); };
renderPeople();

async function init(){
  try {
    const res = await fetch('/api/bible');
    const data = await res.json();
    if (!res.ok) throw Error(data.error);
    try { buildSceneIndex(await (await fetch('/assets/scenes/manifest.json')).json()); } catch (e) { console.warn('manifesto de cenas indisponível', e); }
    books = data.books || [];
    booksEn = data.booksEn || [];
    buildEnIndex();
    if (data.warningEn) console.warn(data.warningEn);
    if (!books.some(x => x.id === opts.book)) { opts.book = 41; opts.chapter = 7; }
    if (!books.find(x => x.id === opts.book)?.chapters[opts.chapter-1]) opts.chapter = 1;
    showFeed();
    window.addEventListener('scroll', ()=>{
      clearTimeout(init.t);
      init.t = setTimeout(()=>save('bf_position', {book:opts.book, chapter:opts.chapter}), 200);
    }, {passive:true});
  } catch (e) {
    $('posts').innerHTML = `<div class="loading"><h2>Não foi possível carregar a Bíblia</h2><p>${esc(e.message || 'Verifique sua conexão na primeira abertura.')}</p><button class="btn" onclick="location.reload()">Tentar novamente</button></div>`;
  }
}

init();
