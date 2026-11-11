"""Cenas de Conceitos: virtudes, sentimentos, teologia e expressões humanas universais."""
from registry import scene, legacy
from svglib import *
from comuns import *

# ---- Legados de conceitos ---------------------------------------------------
legacy('caminho', 'caminho', 'caminho* vereda* estrada* passos jornada emaus paulo saulo timoteo', 1.6)


# ---- Virtudes, Emoções e Vida Cristã ----------------------------------------
@scene('amor', 'amor', 'amor amar amou amados amado amada amai amais amamos amavel caridade querido querida amizade amigo amigos', 2.6)
def _(s):
    s.sky('#f6a5b5', '#fbd5c8', '#fff0dc')
    s.add(s.glow(600, 430, 420, '#fff3e0', .9), heart(600, 420, 4.2, '#d62839'), heart(260, 300, 1.4, '#e8566b', .8), heart(960, 250, 1.1, '#e8566b', .8),
          heart(180, 620, .8, '#f08aa0', .8), heart(1030, 640, 1.0, '#f08aa0', .8), heart(780, 760, .6, '#e8566b', .7), heart(380, 780, .7, '#e8566b', .7))


@scene('alegria', 'alegria e festa', 'alegria alegre alegrar alegrai alegrou alegrem regozij* regozijo festa* festejar celebr* cantai cantar dancar danca jubilo jubilar riso rir feliz felicidade bem-aventurado bem-aventurados', 2.4)
def _(s):
    s.sky('#ffd166', '#ffb36b', '#ff8a6b')
    s.add(rays(600, 400, 120, 900, 24, '#fff3c4', .28, 18), sun(600, 400, 120, '#fff7d6', .95), crowd(14, 5, 700, 860, 60, 1140, (.55, .75)),
          ''.join(star(x, y, r, c) for x, y, r, c in ((160, 160, 26, '#fff'), (1040, 200, 30, '#fff'), (320, 300, 18, '#ffe9a0'), (900, 340, 20, '#ffe9a0'), (80, 440, 14, '#fff'), (1120, 460, 16, '#fff'))))


@scene('paz', 'paz e quietude', 'paz pacifico pacificador pacificadores sossego quietude calma tranquil* repouso repousar descanso descansar descansai aquieta* sabado', 2.4)
def _(s):
    s.sky('#9ccbe8', '#d6ecf5', '#f6f1dc')
    s.add(sun(850, 230, 70, '#fff3c4', .9), cloud(260, 220, 1.1, op=.85), ridge('#a8c8a0', 560, 30, 3), '<rect y="580" width="1200" height="320" fill="#6fb0c8"/>',
          waves(640, 5, '#e0f2f6', .5, 55, 6, 8), dove(500, 360, 1.2), tree(1060, 600, 340, 'round', '#4a8a50'))


@scene('tristeza', 'tristeza e choro', 'tristeza triste tristes chorar chorou choro chorai lagrima* lamento lamentar lamentacao lamentacoes luto lutar pranto prantear gemido gemer gemidos angustia aflicao aflicoes afliccao afligir dor dores sofrimento sofrer soframos', 2.4)
def _(s):
    s.sky('#4a5568', '#7a8aa0', '#aab7c4')
    s.add(cloud(220, 170, 2.4, '#5b6678', .95), cloud(840, 140, 2.8, '#505b6c', .95), rain(90, 6, '#d6e6f2', .5), ridge('#3a4658', 700, 40, 3), '<rect y="760" width="1200" height="140" fill="#2a3340"/>',
          person(600, 790, 1.8, '#4a4f6a', pose='kneel', cloth='#1f2330'), '<path d="M590 600Q586 640 590 660" stroke="#9fd0ea" stroke-width="5" fill="none"/>')


@scene('medo', 'medo e temor', 'medo temor temer temei temes temeu temia assust* tremer tremor terror pavor espanto', 2.2)
def _(s):
    s.sky('#07070e', '#1c1530', '#33264a')
    s.add(fullmoon(930, 200, 70, '#d8d2c0'), ridge('#0a0814', 700, 50, 3), tree(220, 800, 480, 'dead', '#050308'), tree(1020, 800, 420, 'dead', '#050308'),
          '<path d="M0 820H1200V900H0Z" fill="#050308"/>', person(620, 830, 1.5, '#2a2640', pose='up', cloth='#0e0a18'),
          '<circle cx="410" cy="640" r="12" fill="#ffd166"/><circle cx="440" cy="640" r="12" fill="#ffd166"/><circle cx="860" cy="560" r="10" fill="#ffd166"/><circle cx="886" cy="560" r="10" fill="#ffd166"/>')


@scene('esperanca', 'esperança', 'esperanca esperar esperei esperamos esperanca* aguardar aguardo confiar confiai confio confianca promessa* promessas futuro porvir', 2.4)
def _(s):
    s.sky('#27336b', '#c06a8a', '#ffd9a0')
    s.add(s.glow(600, 640, 520, '#fff0c0', .95), sun(600, 640, 90, '#fffbe8', .95), rays(600, 640, 130, 700, 20, '#fff3c4', .25, 14, 9),
          ridge('#3a3a6a', 660, 50, 3), '<path d="M520 900L580 640L620 640L700 900Z" fill="#c9a36b"/>', ridge('#232850', 800, 40, 6), person(610, 700, .9, '#6b3f2a', cloth='#2a1f1a'))


@scene('fe', 'fé', 'fe fiel fieis fidelidade crer cri cre creu crente crentes creem acreditar certeza', 2.2)
def _(s):
    s.sky('#6aa0e0', '#bfd8f0', '#fdf2d4')
    s.add(cloud(220, 260, 1.2, op=.85), cloud(960, 200, 1.4, op=.85), beams(600, 40, 500, '#fff6cf', .22, 7, 820), peaks('#8aa0c0', 700, 340, 3, 4), ridge('#6a8aa0', 760, 25, 5),
          person(600, 800, 1.6, '#f0e6d2', pose='up', cloth='#3a2a20', skin='#e0b48a'))


@scene('perdao', 'perdão e misericórdia', 'perdao perdoar perdoou perdoai perdoa perdoados perdoado misericordia misericordioso compaixao compadecer compadecido piedade clemencia gracia graca graciosa favor', 2.4)
def _(s):
    s.sky('#f3d6a0', '#fbeacb', '#fffaf0')
    s.add(s.glow(600, 360, 460, '#fffbe8', .95), beams(600, 80, 500, '#fff6cf', .22, 7, 820), '<rect y="740" width="1200" height="160" fill="#c9b184"/>',
          person(430, 800, 1.7, '#f0e6d2', pose='kneel', cloth='#3a2a20'), person(780, 830, 2.1, '#7a4a2e', pose='point', cloth='#2a1f1a', halo='#fff3c4'), chain(900, 770, 4, '#8a929a', 44, False, 1))


@scene('justica', 'justiça e juízo', 'justica justo justos injustica injusto juiz juiz* julgar julgou julgai julgamento juizo sentenca sentenciar condenar condenacao retidao equidade direito', 2.3)
def _(s):
    s.sky('#2e3a5c', '#6a7aa0', '#d9c9a0')
    s.add(columns(600, 840, 7, 130, 330, '#e9e0cc'), scales(600, 560, 1.8), '<rect y="840" width="1200" height="60" fill="#bdb199"/>')


@scene('sabedoria', 'sabedoria e entendimento', 'sabedoria sabio sabios sabia sabias entendimento entender inteligencia prudencia prudente ensino ensinar ensinou ensinai mestre mestres aprender aprendei conhecimento ciencia instrucao conselho conselhos discipulo discipulos', 2.2)
def _(s):
    s.sky('#2a2f55', '#4a4a80', '#a07a8a')
    s.add(stars(40, 6, 340), s.glow(600, 560, 380, '#ffd89a', .7), '<rect y="700" width="1200" height="200" fill="#4a3322"/>', book(600, 690, 2.5), lamp(260, 700, 1.4), lamp(1000, 700, 1.4),
          '<path d="M0 0H1200V120H0Z" fill="#1d2038" opacity=".5"/>')


@scene('oracao', 'oração', 'oracao oracoes orar orai oro oramos orou orando suplica suplicas suplicar suplicai clamar clamo clamei clamor rogar rogo rogai pedir pedi pedis pedido intercessao jejum jejuar', 2.8)
def _(s):
    s.sky('#1d2548', '#4a4a7a', '#e9a77a')
    s.add(s.glow(600, 330, 420, '#ffe3a8', .8), beams(600, 110, 360, '#fff3c4', .16, 7, 700), ridge('#2a2f55', 700, 40, 6), '<rect y="760" width="1200" height="140" fill="#1a1f3a"/>',
          person(600, 800, 2.4, '#7a4a2e', pose='kneel', cloth='#2a1f1a'), stars(26, 5, 260))


@scene('louvor', 'louvor e adoração', 'louvor louvar louvai louvarei louvou louvores adoracao adorar adorai adoro adorou cantico canticos hino hinos salmo salmos cantem cantai harpa* lira instrumento tambor tamboril trombeta* musica', 2.5)
def _(s):
    s.sky('#5b3a8a', '#e08a7a', '#ffd9a0')
    s.add(rays(600, 520, 100, 900, 22, '#fff3c4', .22, 16), sun(600, 520, 110, '#fff7d6', .9), ridge('#3a2858', 680, 40, 4), '<rect y="740" width="1200" height="160" fill="#2a1d40"/>',
          harp(360, 700, 2.1), person(780, 820, 2.0, '#f0e6d2', pose='up', cloth='#3a2a20', halo='#fff3c4'), shofar(560, 460, .5), star(180, 200, 24, '#fff'), star(1040, 240, 20, '#fff'))


@scene('palavra', 'a Palavra', 'palavra palavras escritura escrituras livro livros escrito escreveu escrevi escrevei escrever carta cartas rolo ler leia lede leitura profecia profecias profetizar evangelho testemunho testemunhar testamento', 2.3)
def _(s):
    s.sky('#3a2a20', '#7a5a3a', '#d9b27a')
    s.add(s.glow(600, 520, 460, '#ffe9b0', .85), '<rect y="740" width="1200" height="160" fill="#4a3322"/>', book(600, 700, 3.0), scroll(240, 740, 1.2), scroll(960, 740, 1.2), beams(600, 100, 420, '#fff3c4', .12, 7, 700))


@scene('liberdade', 'liberdade', 'liberdade livre livres libertado libertados libertacao cativeiro cativo cativos prisao preso presos prisioneiro prisioneiros grilhoes algemas escravo escravos escravidao servidao jugo', 2.4)
def _(s):
    s.sky('#41588f', '#e69a7a', '#ffd9a0')
    s.add(sun(600, 500, 100, '#fff3c4', .9), ridge('#3a3a6a', 640, 60, 3), '<rect y="760" width="1200" height="140" fill="#1f2040"/>',
          chain(80, 780, 5, '#8a929a', 46), chain(1120, 780, 5, '#8a929a', -46), flock(8, 4, 300, 1000, 150, 420, '#1f2040', .8, 1.7), person(600, 820, 1.7, '#f0e6d2', pose='up', cloth='#3a2a20'))


@scene('nascimento', 'nascimento', 'nascimento nascer nasceu nasce nascido nascidos menino meninos crianca criancas infancia bebe bebes gerar gerou geracao geracoes genealogia concebeu conceber gravida gravidez ventre parto filhinho', 2.4)
def _(s):
    s.sky('#0c1230', '#243a78', '#3a5a9a')
    s.add(stars(60, 7, 420), s.glow(600, 180, 280, '#fff3c4', .8), star(600, 190, 70, '#fff3c4', 8, .38), rays(600, 190, 90, 200, 8, '#fff3c4', .5, 6), ridge('#1a2a4a', 700, 40, 3),
          '<rect x="340" y="560" width="520" height="340" fill="#4a3322"/><path d="M310 560L600 380L890 560Z" fill="#6b4a2a"/><path d="M360 900L360 600L840 600L840 900Z" fill="#2a1d14"/>',
          s.glow(600, 760, 220, '#ffd89a', .8), manger(600, 800, 1.5))


@scene('morte', 'morte e sepulcro', 'morte morto mortos morrer morreu morrem morri morrerei morremos matar matou mataram assassinar assassino sepultura sepultar sepultado tumba tumulo sepulcros cova covas cinza cinzas defunto defuntos', 2.3)
def _(s):
    s.sky('#171a2a', '#3a3f5a', '#7a7a8a')
    s.add(fullmoon(920, 200, 70, '#d8d6cc'), ridge('#2a2f45', 660, 40, 6), '<rect y="740" width="1200" height="160" fill="#14172a"/>', tomb(600, 780, 1.6, '#4a4a58'), tree(150, 800, 400, 'dead', '#0a0c18'), tree(1060, 810, 360, 'dead', '#0a0c18'))


@scene('vida', 'vida e ressurreição', 'vida vidas viver viveu vive vivei vivemos vivo vivos viva vivificar vivificou vivente viventes respirar alma almas', 1.3)
def _(s):
    s.sky('#f2c27f', '#fbe6bf', '#fffbe8')
    s.add(s.glow(600, 360, 500, '#fff7d6', .9), rays(600, 360, 90, 800, 22, '#fff3c4', .28, 14), ridge('#8cc36f', 640, 25, 3), ridge('#5da048', 740, 25, 6),
          tree(600, 780, 600, 'round', '#3f8a45'), ''.join(flower(x, 840, 60, c) for x, c in ((180, '#f4a8c0'), (320, '#ffffff'), (880, '#f4d35e'), (1040, '#f4a8c0'))), flock(5, 3, 200, 1000, 150, 300, '#3a4a50', .8, 1.2))


@scene('pecado', 'pecado e trevas', 'pecado pecados pecador pecadores pecar pecou pequei pecamos iniquidade iniquidades maldade maldades mal malvado malvados impio impios transgressao transgressoes culpa culpado culpados vergonha engano enganar mentira mentiras mentir mentiroso tentacao tentar tentou ladrao roubar roubo furto adulterio', 2.2)
def _(s):
    s.sky('#0a070e', '#1f1230', '#3a1c2e')
    s.add(fullmoon(240, 180, 50, '#9a8a8a'), ridge('#150c1c', 640, 70, 3), ridge('#0a060f', 760, 50, 5), tree(300, 800, 520, 'dead', '#050308'), tree(900, 810, 480, 'dead', '#050308'),
          snake(640, 840, 1.6, '#3a4a30'), '<circle cx="690" cy="690" r="9" fill="#d62828"/><circle cx="716" cy="690" r="9" fill="#d62828"/>')


@scene('ira', 'ira de Deus', 'irado irados furor furioso indignacao indignar castigo castigar castigou castigos juizos vingar vinganca vingador retribuir retribuicao ferir feriu maldicao maldito malditos amaldicoar', 2.2)
def _(s):
    s.sky('#2a0c0c', '#8a2a1c', '#e0662a')
    s.add(cloud(240, 170, 2.2, '#3a1612', .95), cloud(900, 140, 2.6, '#2a0f0c', .95), lightning(620, 200, 1.7, '#ffe08a'), peaks('#2a1410', 640, 260, 4, 3), ridge('#150906', 760, 40, 4), flame(220, 800, 2.0), flame(980, 800, 2.4), flame(620, 810, 1.6, '#ff6b1c', '#ffd166'))


@scene('humildade', 'humildade e servo', 'humildade humilde humildes humilhar humilhou servo servos servir serviu servico servical servicais obediencia obedecer obedeceu obedientes submeter sujeitar pequeninos pequenino pequeno pequenos pobre pobres pobreza necessitado necessitados mendigo mendigos viuva viuvas orfao orfaos estrangeiro estrangeiros', 2.1)
def _(s):
    s.sky('#9fb4d6', '#dfe6ef', '#f6efdc')
    s.add(ridge('#a8b890', 620, 30, 2), '<rect y="700" width="1200" height="200" fill="#a58a5a"/>', '<rect x="360" y="780" width="480" height="40" rx="14" fill="#6a8aa8"/>', person(430, 770, 1.5, '#5a3a22', pose='kneel', cloth='#2a1f1a'),
          person(780, 770, 2.0, '#f0e6d2', pose='kneel', cloth='#3a2a20'), '<ellipse cx="600" cy="790" rx="110" ry="20" fill="#6a8aa8"/>')


@scene('forca', 'força e poder', 'forca forcas forte fortes fortalecer fortalece fortaleceu fortaleza poder poderes poderoso poderosa poderosos poderio valente valentes valor coragem corajoso animo animai esforcai esforco gigante gigantes', 2.2)
def _(s):
    s.sky('#3a6ab0', '#8ab4e0', '#e8d6a8')
    s.add(cloud(250, 220, 1.3, op=.85), peaks('#6a7a8a', 650, 380, 3, 3, '#fff', .9), '<rect y="650" width="1200" height="250" fill="#5a4a3a"/>', rocks(240, 740, 1.8), rocks(980, 760, 2.0),
          person(600, 830, 2.6, '#8a2f3c', pose='up', cloth='#2a1f1a'), eagle(920, 280, .9))


@scene('casamento', 'casamento e aliança', 'casamento casar casou casaram casai marido maridos esposa esposas esposo noiva noivo noivos nupcias bodas matrimonio matrimonios mulher mulheres varao varoes homem homens adao eva', 2.1)
def _(s):
    s.sky('#f6c5a8', '#fbe0cc', '#fff3e4')
    s.add(s.glow(600, 360, 420, '#fffbe8', .9), ridge('#b5d4a0', 620, 25, 3), ridge('#8cc36f', 720, 25, 5),
          '<path d="M480 440Q600 300 720 440" stroke="#8cc36f" stroke-width="16" fill="none"/>', ''.join(flower(x, y, 40, '#f4a8c0') for x, y in ((500, 430), (560, 380), (640, 380), (700, 430))),
          person(480, 820, 2.0, '#f4efe2', cloth='#3a2a20'), person(740, 820, 2.0, '#3b4a6a', cloth='#2a1f1a'), heart(600, 250, 1.1, '#e8566b', .9))


@scene('sacrificio', 'sacrifício e altar', 'sacrificio sacrificios sacrificar sacrificou oferta ofertas oferecer ofereceu oferecei holocausto holocaustos altar altares sacerdote sacerdotes sacerdocio levita levitas oblacao expiacao incenso-do-altar', 2.2)
def _(s):
    s.sky('#1c1228', '#5a2a3a', '#d9703a')
    incenso_smoke = ''.join(f'<path d="M{600 + dx} 430C{570 + dx} 360 {640 + dx} 300 {600 + dx} 200" stroke="#e8dcd0" stroke-width="{w}" fill="none" stroke-linecap="round" opacity=".28"/>' for dx, w in ((0, 18), (-30, 12), (36, 10)))
    s.add(fullmoon(210, 170, 40, '#d8d2c0'), ridge('#2a1a2a', 700, 40, 3), '<rect y="760" width="1200" height="140" fill="#1a1018"/>', altar(600, 800, 2.8), sheep(280, 820, 1.1), person(900, 850, 1.7, '#f0e6d2', pose='up', cloth='#3a2a20'), incenso_smoke)


@scene('estrada_emaus', 'viajantes', 'viajar viajou viajante viajantes andar andou andai andaram andando seguir seguiu segui seguimos seguem seguidores peregrino peregrinos peregrinacao jornada-longa', 1.9)
def _(s):
    s.sky('#f4b183', '#fce6c4', '#fff4e0')
    s.add(sun(840, 340, 90, '#fff3c4', .9), ridge('#b5c89a', 560, 25, 3), ridge('#7aa65a', 650, 25, 4), '<path d="M0 760Q500 640 1200 600L1200 900L0 900Z" fill="#c9a36b"/>',
          person(300, 790, 1.4, '#7a4a2e', staff=True), person(430, 760, 1.3, '#3b5a7a', staff=True), person(560, 735, 1.2, '#8a2f3c', staff=True), tree(1000, 640, 340, 'olive', '#7f9a5a', '#5a4a38'))


@scene('mundo', 'o mundo', 'mundo mundos universo criacao criar criou criador criaturas criatura principio comeco genesis fundacao natureza nacoes nacao povo povos gentios', 1.1)
def _(s):
    s.sky('#050a1f', '#14235a', '#2a3f80')
    s.add(stars(120, 11, 800), s.glow(600, 450, 420, '#7fb4ff', .35), '<circle cx="600" cy="450" r="260" fill="#2b68b0"/>',
          '<path d="M470 330Q520 280 580 320Q620 360 560 410Q500 400 470 330Z M610 450Q690 410 740 470Q720 540 650 560Q600 520 610 450Z M440 500Q480 470 510 520Q480 570 440 540Z" fill="#4a9a58"/>',
          '<circle cx="600" cy="450" r="260" fill="none" stroke="#9fd0ff" stroke-width="6" opacity=".4"/>')


# ---- Corpo, Fala e Ações Humanas (4 variações cada) ------------------------
V = 4


@scene('maos', 'as mãos', 'mao maos dedo dedos palma palmas punho braco bracos', 1.8, V)
def _(s, t=0):
    s.sky('#f4b183', '#fce6c4', '#fff4e0')
    s.add(sun(600, 200, 80, '#fff3c4', .9), rays(600, 200, 120, 800, 24, '#fff3c4', .2, 12), beams(600, 200, 240, '#fff6cf', .22, 6, 700), cloud(200, 190, 1.3), cloud(1000, 240, 1.3),
          hand(600, 650, 3.0), hand(250, 780, 1.4, rot=-24), hand(950, 780, 1.4, rot=24, flip=True), dove(600, 330, .9))


@scene('olhos', 'os olhos', 'olho olhos vista olhar olhou olhai olhando vigia viu vendo', 1.6, V)
def _(s, t=0):
    s.sky('#07102e', '#1c2a6a', '#3a4f9a')
    s.add(stars(70, 5, 500), rays(600, 430, 280, 900, 28, '#fff3c4', .16, 14), s.glow(600, 430, 520, '#fff3c4', .6), eye(600, 430, 2.2, '#4a7a9a'), ridge('#0e1830', 760, 40, 3),
          '<rect y="830" width="1200" height="70" fill="#0a1028"/>', person(250, 840, 1.1, '#3b5a7a', pose='up'), person(930, 840, 1.1, '#8a2f3c', pose='pray'))


@scene('coracao', 'o coração', 'coracao coracoes peito entranhas intimo', 1.8, V)
def _(s, t=0):
    s.sky('#f6a5b5', '#fbd5c8', '#fff0dc')
    s.add(s.glow(600, 420, 520, '#fff3e0', .9), rays(600, 420, 200, 700, 24, '#fff3c4', .18, 10), heart(600, 410, 5.2, '#d62839'), heart(600, 410, 3.4, '#e8566b', .7),
          hand(400, 790, 1.8, rot=-20), hand(800, 790, 1.8, rot=20, flip=True), dove(250, 250, .7), dove(960, 230, .7, '#fff6f0'))


@scene('voz', 'a voz', 'voz vozes boca bocas labios lingua clamor gritar gritou grito clamar clamou', 1.8, V)
def _(s, t=0):
    s.sky('#3a4a68', '#7a8aa8', '#f0d9a8')
    s.add(cloud(200, 170, 2.2, '#6a7a98', .95), cloud(980, 150, 2.4, '#5a6a88', .95), peaks('#8a9ab0', 640, 300, 3, 4), ridge('#6a7a60', 720, 25, 3), '<rect y="780" width="1200" height="120" fill="#5a6a48"/>',
          person(300, 800, 2.0, ROBE, pose='up', cloth='#3a2a20'), sound_waves(380, 560, 90, 5, '#ffffff', .75, -35, 35, 56, 9), shofar(820, 520, .7), sound_waves(900, 470, 70, 4, '#fff3c4', .6, -40, 40, 50, 8),
          crowd(10, 3, 810, 890, 640, 1160, (.5, .7)))


@scene('ouvido', 'ouvir e escutar', 'ouvido ouvidos ouvir ouviu ouvi ouvis ouvindo ouviram escutar escutou escutai atenta atencao', 1.6, V)
def _(s, t=0):
    s.sky('#6aa0e0', '#bfd8f0', '#fdf2d4')
    s.add(sun(180, 160, 70, '#fff3c4', .9), cloud(700, 170, 1.5), ridge('#a8c8a0', 560, 25, 3), '<path d="M0 900L0 700Q600 560 1200 640L1200 900Z" fill="#7aa65a"/>', grass(700, '#4f8a3f', 2, 120),
          sound_waves(930, 330, 90, 5, '#ffffff', .6, 130, 230, 56, 8), person(950, 380, 1.1, ROBE, pose='stand', cloth='#5a3b22', halo='#fff3c4'),
          crowd(24, 6, 740, 890, 60, 800, (.5, .8)), tree(90, 700, 340, 'olive', '#7f9a5a', '#5a4a38'))


@scene('pes_caminho', 'os pés no caminho', 'pe pes pegadas calcanhar calcanhares sandalia sandalias descalco', 1.6, V)
def _(s, t=0):
    s.sky('#f08a5d', '#f9d6a0', '#fdf0d4')
    s.add(sun(850, 330, 90, '#fff3c4', .9), peaks('#b59a72', 620, 260, 4, 7), '<path d="M0 900L0 700Q500 640 1200 660L1200 900Z" fill="#d9b97a"/>', '<path d="M360 900L560 700L620 700L900 900Z" fill="#c4a064"/>',
          footprints(480, 880, 7, 38, -52, '#6a4a2e', .75), rocks(150, 800, 1.6), rocks(1050, 790, 1.4), tree(1010, 700, 300, 'palm', '#3f7a3a'))


@scene('rosto', 'o rosto', 'cabeca cabecas rosto rostos face faces fronte cabelo cabelos barba testa', 1.6, V)
def _(s, t=0):
    s.sky('#27336b', '#c06a8a', '#ffd9a0')
    s.add(rays(600, 300, 140, 900, 30, '#fff3c4', .16, 12), s.glow(600, 280, 480, '#fff3c4', .85), person(600, 1060, 4.6, '#7a4a2e', pose='stand', cloth='#2a1c14', halo='#fff3c4'))


@scene('ossos', 'os ossos secos', 'osso ossos esqueleto secos carne carnes corpo corpos', 1.6, V)
def _(s, t=0):
    s.sky('#3a3a4a', '#7a6a6a', '#d9b99a')
    s.add(cloud(220, 160, 2.4, '#5a5a6a', .9), cloud(940, 130, 2.6, '#6a6a7a', .9), ridge('#8a7a68', 600, 30, 3), '<rect y="680" width="1200" height="220" fill="#b59a72"/>',
          ''.join(bone(120 + (i * 143) % 1000, 760 + (i * 37) % 120, 90 + (i % 3) * 30, (i * 47) % 180) for i in range(14)),
          ''.join(skull(180 + i * 240, 830 - (i % 2) * 30, .8) for i in range(5)), s.glow(600, 480, 360, '#fff3c4', .55), dove(600, 380, 1.3), person(860, 700, 1.1, '#8a6a4a', pose='up', cloth='#2a2018'))


@scene('familia', 'a família', 'pai pais filha filhas irma irmas avo neto netos familia familias parente parentes', 1.8, V)
def _(s, t=0):
    s.sky('#f08a5d', '#f9d6a0', '#fdf0d4')
    s.add(sun(940, 240, 80, '#fff3c4', .9), ridge('#c9b58a', 600, 25, 3), '<rect y="740" width="1200" height="160" fill="#d9b97a"/>', house(300, 740, 440, 300, '#e8d4a8'), tree(1070, 760, 340, 'olive', '#7f9a5a', '#5a4a38'),
          person(560, 880, 1.7, '#3b5a7a', cloth='#3a2a20'), person(700, 880, 1.6, '#8a2f3c', cloth='#e8dcc0'), person(810, 890, 1.1, '#5a7a3b', cloth='#3a2a20'), person(890, 890, .9, '#b88a3f', cloth='#e8dcc0'),
          person(960, 890, .7, '#6b4a8a', cloth='#3a2a20'), person(210, 880, 1.2, '#8a6a4a', pose='sit', cloth='#e8dcc0'))


@scene('tempo_dias', 'os dias e os anos', 'dia dias ano anos mes meses semana semanas hoje amanha tarde manha tempo tempos hora horas estacao', 1.2, V)
def _(s, t=0):
    s.sky('#6aa0e0', '#bfd8f0', '#fdf2d4')
    s.add('<path d="M100 640Q600 -80 1100 640" stroke="#fff3c4" stroke-width="5" fill="none" stroke-dasharray="14 12" opacity=".7"/>', sun(220, 520, 54, '#ffd166', .95), sun(600, 150, 70, '#fff3c4', .95), sun(980, 520, 50, '#f08a5d', .95),
          moon(1090, 220, 36), ridge('#a8c8a0', 700, 25, 3), '<rect y="760" width="1200" height="140" fill="#7aa65a"/>', grass(770, '#4f8a3f', 2, 120), tree(130, 790, 320, 'olive', '#7f9a5a', '#5a4a38'), wheat(900, 880, 150), wheat(940, 880, 150),
          person(600, 880, 1.4, '#7a4a2e', pose='stand', staff=True))


@scene('subir_monte', 'subir ao monte', 'subir subiu subiram subindo subi sobe suba desceu desceram descer descendo desce', 1.4, V)
def _(s, t=0):
    s.sky('#6aa0e0', '#bfd8f0', '#fdf2d4')
    s.add(sun(950, 150, 70, '#fff3c4', .9), cloud(240, 170, 1.4), '<path d="M-100 900L560 120L1300 900Z" fill="#8a7a68"/><path d="M560 120L430 300L520 270L560 340L610 270L700 300Z" fill="#fdfdfd"/>',
          '<path d="M180 900Q620 820 380 720Q140 640 520 560Q780 500 540 420Q400 370 560 300" stroke="#d9c49a" stroke-width="36" fill="none" stroke-linecap="round"/>',
          person(300, 770, .5, '#7a4a2e', pose='walk'), person(400, 650, .4, '#3b5a7a', pose='walk'), person(520, 570, .34, '#8a2f3c', pose='walk'), person(560, 420, .28, ROBE, pose='walk'), ridge('#5a7a48', 860, 20, 4))


@scene('retorno', 'o retorno', 'voltar voltou voltaram voltei volta retornar retornou regressar regressou', 1.4, V)
def _(s, t=0):
    s.sky('#27336b', '#c06a8a', '#ffd9a0')
    s.add(sun(260, 600, 90, '#fffbe8', .95), ridge('#3a3a6a', 620, 40, 3), house(980, 700, 240, 170, '#e8d4a8'), '<path d="M0 900L0 760Q500 700 1200 740L1200 900Z" fill="#6a5a44"/>',
          '<path d="M0 860Q500 780 940 740" stroke="#c9a36b" stroke-width="40" fill="none" stroke-linecap="round" opacity=".7"/>', person(480, 810, 1.5, '#7a4a2e', pose='walk', staff=True, cloth='#3a2a20'),
          person(600, 800, 1.2, '#3b5a7a', pose='walk', cloth='#3a2a20'), person(1080, 800, 1.3, '#8a2f3c', pose='up', cloth='#e8dcc0'), sheep(330, 850, .8), tree(130, 760, 340, 'olive', '#4a6a5a', '#2a2018'))


@scene('presente_dadiva', 'entregar um presente', 'entregar entregou entregaram entregue presente presentes dadiva dadivas', 1.6, V)
def _(s, t=0):
    s.sky('#f4b183', '#fce6c4', '#fff4e0')
    s.add(sun(940, 200, 70, '#fff3c4', .9), ridge('#c9b58a', 580, 25, 3), '<rect y="740" width="1200" height="160" fill="#d9b97a"/>', tent(180, 760, 260, 190, '#e8dcc0'), person(400, 880, 2.0, '#3b5a7a', pose='point', cloth='#3a2a20'),
          person(800, 880, 2.0, '#8a2f3c', pose='stand', cloth='#e8dcc0'), jar(560, 640, .8, '#c9a040'), coin(640, 560, 36), chalice(700, 650, .7), hand(600, 800, 1.0, rot=0))


@scene('levantar', 'levantar-se', 'levantar levantou levantaram levanta levantai erguer ergueu ergueram erguido', 1.4, V)
def _(s, t=0):
    s.sky('#27336b', '#c06a8a', '#ffd9a0')
    s.add(sun(600, 620, 110, '#fffbe8', .95), rays(600, 620, 150, 800, 24, '#fff3c4', .2, 12), ridge('#3a3a6a', 660, 40, 3), '<rect y="800" width="1200" height="100" fill="#1e2244"/>', person(420, 850, 1.3, '#7a4a2e', pose='kneel', cloth='#2a1f3a'),
          person(640, 850, 1.7, ROBE, pose='up', cloth='#5a3b22', halo='#fff3c4'), hand(520, 700, .8, rot=-40), banner(1030, 880, 420, '#8a2f3c', 120), banner(120, 880, 380, '#3b5a7a', 120))


@scene('dialogo', 'conversa e ordem', 'respondeu responderam responder perguntou ordenou mandou mandado mandar mandaram falou', 1.2, V)
def _(s, t=0):
    s.sky('#6aa0e0', '#bfd8f0', '#fdf2d4')
    s.add(sun(950, 170, 70, '#fff3c4', .9), cloud(240, 180, 1.4), ridge('#a8c8a0', 570, 25, 3), '<rect y="740" width="1200" height="160" fill="#8aa660"/>', grass(750, '#4f8a3f', 2, 110), tree(1090, 760, 340, 'olive', '#7f9a5a', '#5a4a38'),
          person(400, 860, 1.9, '#7a4a2e', pose='point', cloth='#3a2a20'), person(780, 860, 1.9, ROBE, pose='stand', cloth='#5a3b22'), sound_waves(480, 560, 60, 3, '#ffffff', .7, -30, 30, 44, 8), sound_waves(710, 560, 60, 3, '#ffffff', .7, 150, 210, 44, 8))


@scene('pacto_estatutos', 'pacto e estatutos', 'pacto pactos juramento jurou jurar jurei estatutos estatuto ordenancas decretos preceitos', 1.8, V)
def _(s, t=0):
    s.sky('#27336b', '#7a6a9a', '#f4c58a')
    s.add(peaks('#6a5a7a', 720, 380, 3, 6), '<rect y="780" width="1200" height="120" fill="#3a3248"/>', s.glow(600, 480, 420, '#fff3c4', .7), scroll(600, 470, 2.0), hand(300, 760, 1.8, rot=-18), hand(900, 760, 1.8, rot=18, flip=True),
          rainbow(600, 360, 340, 18, .55), rays(600, 470, 200, 700, 16, '#fff3c4', .14, 10))


@scene('heranca_limites', 'a herança e os limites', 'heranca herancas herdar herdou herdeiro herdeiros porcao limite limites fronteira termo', 1.8, V)
def _(s, t=0):
    s.sky('#8ec5e8', '#d6ecf5', '#fdf2d4')
    s.add(sun(180, 170, 70, '#fff3c4', .9), ridge('#a8c8a0', 540, 25, 3), '<rect y="620" width="1200" height="280" fill="#8aa660"/>', '<path d="M0 760L1200 700M0 840L1200 820M300 620L400 900M780 620L980 900" stroke="#5a7a3b" stroke-width="10" opacity=".7"/>',
          standing_stone(300, 770, 60, 120), standing_stone(770, 780, 60, 120), standing_stone(110, 840, 60, 120), standing_stone(1060, 850, 60, 120), wheat(460, 870, 140), wheat(500, 880, 140), sheep(900, 870, .9), grapes(640, 840, 1.0))


@scene('servo_servico', 'o servo', 'servo servos serva servas criado criados escravo escrava', 1.8, V)
def _(s, t=0):
    s.sky('#f4b183', '#fce6c4', '#fff4e0')
    s.add(sun(940, 210, 70, '#fff3c4', .9), ridge('#c9b58a', 580, 25, 3), '<rect y="740" width="1200" height="160" fill="#d9b97a"/>', house(220, 740, 340, 240, '#e8d4a8'), well(780, 800, 1.7),
          person(560, 880, 1.7, '#7a4a2e', pose='walk', cloth='#3a2a20'), jar(520, 640, .6, '#b5683a'), person(960, 880, 1.6, '#8a2f3c', pose='stand', cloth='#e8dcc0'), jar(930, 810, .5), tree(1100, 770, 320, 'palm', '#3f7a3a'))


@scene('nome_gloria', 'o nome e a glória', 'nome nomes gloria honra fama renome majestade esplendor', 1.6, V)
def _(s, t=0):
    s.sky('#07102e', '#1c2a6a', '#3a4f9a')
    s.add(stars(60, 8, 500), s.glow(600, 360, 560, '#fff3c4', .95), rays(600, 360, 120, 900, 36, '#fff3c4', .16, 12), crown(600, 440, 2.6), star(600, 150, 46, '#fff7d6', 8, .35),
          ridge('#0e1830', 760, 40, 3), '<rect y="830" width="1200" height="70" fill="#0a1028"/>', crowd(16, 3, 800, 880, 60, 1140, (.5, .7)))


@scene('verdade_luz', 'a verdade', 'verdade verdadeiro verdadeira verdadeiros veracidade', 1.6, V)
def _(s, t=0):
    s.sky('#05050f', '#14183a', '#2a2f5a')
    s.add(stars(40, 6, 380), ridge('#0e1028', 700, 40, 2), '<rect y="780" width="1200" height="120" fill="#0a0a14"/>', '<path d="M420 900L560 700L640 700L900 900Z" fill="#3a3a58" opacity=".7"/>', beams(600, 520, 260, '#fff6cf', .3, 6, 900),
          s.glow(600, 520, 340, '#ffd9a0', .8), lamp(540, 560, 2.6), book(600, 880, 1.3), person(200, 850, 1.5, '#3b5a7a', pose='point'), person(1000, 850, 1.5, '#8a2f3c', pose='stand'))


@scene('bondade', 'a bondade', 'bem bom boa bondade benigno benignidade bondoso bondosa bons boas melhor', 1.2, V)
def _(s, t=0):
    s.sky('#f6a5b5', '#fbd5c8', '#fff0dc')
    s.add(sun(950, 190, 80, '#fff3c4', .9), s.glow(500, 520, 420, '#fff3e0', .8), ridge('#c9b58a', 600, 25, 3), '<rect y="760" width="1200" height="140" fill="#d9b97a"/>', tree(110, 770, 320, 'olive', '#7f9a5a', '#5a4a38'),
          person(420, 880, 1.9, ROBE, pose='point', cloth='#5a3b22'), bread(560, 700, .5), person(780, 890, 1.4, '#6a6a5a', pose='kneel', cloth='#8a8a7a'), person(920, 890, 1.1, '#7a5a5a', pose='sit', cloth='#8a8a7a'), heart(500, 330, 1.2, '#d62839', .85))
