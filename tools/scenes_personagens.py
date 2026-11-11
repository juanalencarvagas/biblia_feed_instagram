"""Cenas de Personagens Bíblicos: patriarcas, reis, profetas, discípulos e figuras históricas."""
from registry import scene
from svglib import *
from comuns import *

V = 4


# ---- Jesus e Apóstolos ------------------------------------------------------
@scene('jesus_ensina', 'Jesus ensina a multidão', 'jesus mestre ensinar ensinou ensinava ensinando ensino ensinos parabola parabolas sermao doutrina', 3.0, V)
def _(s, t=0):
    s.sky('#6aa0e0', '#bfd8f0', '#fdf2d4')
    s.add(sun(940, 170, 70, '#fff3c4', .9), cloud(240, 190, 1.3, op=.9), peaks('#9db4c8', 600, 260, 4, 5), ridge('#a8c8a0', 590, 25, 3), ridge('#7aa65a', 680, 25, 4),
          grass(700, '#4f8a3f', 2, 140), tree(110, 700, 380, 'olive', '#7f9a5a', '#5a4a38'), tree(1090, 700, 360, 'olive', '#7f9a5a', '#5a4a38'),
          crowd(8, 5, 740, 880, 30, 470, (.45, .62)), crowd(8, 6, 740, 880, 730, 1170, (.45, .62)),
          rocks(600, 700, 2.4), beams(600, 330, 200, '#fff6cf', .18, 5, 700), person(600, 690, 1.6, ROBE, pose='point', cloth='#5a3b22', halo='#fff3c4'))


@scene('discipulos', 'os discípulos', 'discipulos discipulo apostolo apostolos doze companheiros companhia seguidores irmaos irmao irmaos-fe amigos-jesus', 2.8, V)
def _(s, t=0):
    s.sky('#27336b', '#c06a8a', '#ffd9a0')
    s.add(sun(600, 560, 100, '#fffbe8', .95), rays(600, 560, 140, 800, 22, '#fff3c4', .2, 12), ridge('#3a3a6a', 640, 40, 3), ridge('#232850', 740, 30, 6), '<rect y="780" width="1200" height="120" fill="#1e2244"/>')
    for i in range(12):
        if i == 6:
            continue
        x = 70 + i * 96
        s.add(person(x, 830 - (i % 2) * 30, .95, COLORS[i % 8], cloth=['#3a2a20', '#2a2a2a', '#6b4a2a'][i % 3], pose=['stand', 'point', 'stand', 'pray'][i % 4]))
    s.add(person(600, 850, 1.6, ROBE, pose='stand', cloth='#5a3b22', halo='#fff3c4'))


@scene('samaria_poco', 'a samaritana no poço', 'samaritano samaritana samaritanos samaria sicar jaco-poco poco-agua agua-viva sede-agua balde cantaro', 3.0, V)
def _(s, t=0):
    s.sky('#8ec5e8', '#e6f0f4', '#fdf2d4')
    s.add(sun(960, 150, 90, '#fff7d6', .95), ridge('#d9c9a0', 520, 25, 3), ridge('#c9b58a', 600, 22, 5), '<rect y="640" width="1200" height="260" fill="#d9b97a"/>',
          tree(120, 700, 340, 'palm', '#3f7a3a'), tree(1080, 690, 360, 'olive', '#7f9a5a', '#5a4a38'), well(600, 760, 2.4),
          person(400, 840, 1.5, COLORS[2], pose='stand', cloth='#e8dcc0'), jar(480, 850, .6), person(810, 850, 1.5, ROBE, pose='sit', cloth='#5a3b22', halo='#fff3c4'))


# ---- Patriarcas e Histórias dos Pais ----------------------------------------
@scene('caim_abel', 'Caim e Abel', 'caim abel fratricida primicias', 3.0, V)
def _(s, t=0):
    s.sky('#6aa0e0', '#bfd8f0', '#fdf2d4')
    s.add(ridge('#a8c8a0', 560, 25, 3), '<rect y="650" width="1200" height="250" fill="#7aa65a"/>', grass(660, '#4f8a3f', 2, 120), altar(300, 810, 1.7), altar(900, 810, 1.7),
          '<path d="M300 560C270 480 330 420 300 300C290 240 310 160 300 100" stroke="#f4efe2" stroke-width="22" fill="none" stroke-linecap="round" opacity=".6"/>',
          '<path d="M900 560C960 520 880 460 960 400C1020 360 960 300 1040 260" stroke="#6a6a6a" stroke-width="22" fill="none" stroke-linecap="round" opacity=".55"/>',
          person(140, 860, 1.7, '#3b5a7a', pose='pray', cloth='#3a2a20'), sheep(80, 880, .8), person(1070, 860, 1.7, '#8a2f3c', pose='stand', cloth='#14100c'), wheat(1130, 880, 110), wheat(1150, 890, 100))


@scene('rebeca_poco', 'Rebeca no poço', 'rebeca raquel lea labao hagar miriam noemi jezabel hanna', 3.0, V)
def _(s, t=0):
    s.sky('#f08a5d', '#f9d6a0', '#fdf0d4')
    s.add(sun(940, 260, 80, '#fff3c4', .9), ridge('#c9b58a', 600, 25, 3), '<rect y="700" width="1200" height="200" fill="#d9b97a"/>', tree(120, 760, 360, 'palm', '#3f7a3a'), well(560, 820, 2.0),
          quad(920, 860, 'camel', 1.0, '#b8935a', flip=True), quad(1100, 850, 'camel', .8, '#a8835a', flip=True), person(360, 860, 1.8, '#6b4a8a', cloth='#e8dcc0', pose='stand'), jar(300, 700, .5),
          person(780, 870, 1.5, '#7a4a2e', cloth='#3a2a20', pose='point'))


@scene('jose_sonhos', 'José e os sonhos', 'jose tunica tunicas espiga espigas feixe feixes ismaelitas potifar mercadores sonhador sonhou', 3.4, V)
def _(s, t=0):
    s.sky('#27336b', '#6a5a9a', '#f0c58a')
    s.add(sun(260, 190, 62, '#fff1b8', .95), moon(520, 150, 40), ''.join(star(700 + (i % 6) * 70, 110 + (i // 6) * 90, 16, '#ffe9a0') for i in range(11)),
          ridge('#7a8a5a', 620, 25, 3), '<rect y="640" width="1200" height="260" fill="#c9a24a"/>', grass(650, '#9a8a3a', 4, 70))
    for i in range(10):
        s.add(sheaf(180 + i * 86 if i < 5 else 640 + (i - 5) * 86, 800 + (i % 2) * 20, 120, 2 if i < 5 else -2))
    s.add(sheaf(600, 790, 210), person(1060, 850, 1.5, '#c0392b', pose='up', cloth='#3a2a20'))


@scene('tribos_israel', 'as doze tribos', 'tribo tribos ruben simeao levi juda dan naftali gade aser issacar zebulom efraim manasses benjamim gileade', 3.0, V)
def _(s, t=0):
    s.sky('#f4b183', '#fce6c4', '#fff4e0')
    s.add(sun(180, 180, 70, '#fff3c4', .9), ridge('#c9b58a', 600, 25, 3), '<rect y="640" width="1200" height="260" fill="#d9b97a"/>', tent(600, 760, 260, 190, '#e8dcc0'))
    cols = ['#8a2f3c', '#3b5a7a', '#5a7a3b', '#b88a3f', '#6b4a8a', '#2f6b6b', '#c0392b', '#e0b040', '#4a8a3a', '#a85a8a', '#3a7a9a', '#7a4a2e']
    for i, c in enumerate(cols):
        s.add(banner(80 + i * 96, 760 + (i % 2) * 70, 240 - (i % 2) * 40, c, 70, i >= 6))
    s.add(crowd(14, 3, 820, 890, 100, 1100, (.35, .5)))


# ---- Sacerdócio, Juízes e Profetas ------------------------------------------
@scene('arao_sacerdote', 'Arão e o tabernáculo', 'arao mitra efode peitoral amendoeira incensario propiciatorio', 3.0, V)
def _(s, t=0):
    s.sky('#6a9ad8', '#c5dcf2', '#fdf2d4')
    s.add(ridge('#c9b58a', 620, 25, 3), '<rect y="700" width="1200" height="200" fill="#d9b97a"/>', tent(280, 740, 320, 230, '#e8dcc0'), tent(920, 740, 320, 230, '#e8dcc0'),
          '<rect x="450" y="520" width="300" height="230" fill="#8a2f3c"/><path d="M430 520L600 420L770 520Z" fill="#6a2330"/><rect x="560" y="610" width="80" height="140" fill="#2a1410"/>',
          altar(240, 860, 1.0), person(600, 870, 2.0, ROBE, pose='stand', cloth='#e0b040', halo='#fff3c4', staff=True),
          ''.join(f'<circle cx="{652 + dx}" cy="{560 - dy}" r="9" fill="#f4c2d0"/>' for dx, dy in ((0, 0), (20, 22), (-12, 36), (28, 60))))


@scene('samuel_chamado', 'Samuel é chamado', 'samuel eli silo vidente videntes', 3.2, V)
def _(s, t=0):
    s.sky('#07070e', '#1c1530', '#33264a')
    s.add(s.glow(600, 520, 520, '#ffd9a0', .5), '<path d="M200 800V280Q600 100 1000 280V800Z" fill="#14100c"/>', columns(600, 800, 4, 260, 520, '#3a2f26'),
          beams(600, 60, 260, '#fff6cf', .22, 5, 800), '<rect y="800" width="1200" height="100" fill="#2a2018"/>', lamp(220, 760, 1.4), lamp(980, 760, 1.4),
          person(840, 850, 1.7, '#8a6a4a', pose='sit', cloth='#e8dcc0'), person(480, 850, 1.1, ROBE, pose='kneel', cloth='#3a2a20', halo='#fff3c4'), sound_waves(560, 300, 60, 4, '#fff3c4', .7, 20, 160))


@scene('sansao', 'Sansão', 'sansao dalila nazireu nazireus cabelo cabelos tosquiar tosquiou gaza dagom', 3.2, V)
def _(s, t=0):
    s.sky('#2a1a14', '#6a3a24', '#d9703a')
    s.add(s.glow(600, 480, 520, '#ffd9a0', .5), columns(600, 780, 2, 560, 560, '#d8c9a8'), '<rect x="140" y="170" width="920" height="46" fill="#c9b99a"/>', cloud(300, 300, 2.0, '#8a7a6a', .6), cloud(900, 280, 2.0, '#8a7a6a', .6),
          crowd(18, 5, 220, 330, 160, 1040, (.35, .45)), '<rect y="780" width="1200" height="120" fill="#4a3322"/>', rocks(330, 830, 1.8), rocks(850, 830, 1.8), rocks(600, 850, 1.4),
          person(600, 800, 2.3, '#a8703a', pose='up', cloth='#14100c'), rays(600, 560, 170, 520, 18, '#fff3c4', .2, 10))


@scene('profeta', 'o profeta', 'isaias jeremias ezequiel oseias amos miqueias habacuque sofonias ageu zacarias malaquias abdias naum profeta profetas', 3.0, V)
def _(s, t=0):
    s.sky('#27336b', '#c06a8a', '#ffd9a0')
    s.add(sun(180, 560, 90, '#fffbe8', .95), rays(180, 560, 130, 800, 20, '#fff3c4', .18, 12), ridge('#3a3a6a', 600, 40, 3), wall(660, 1200, 690, 90), tower(760, 700, 110, 280), tower(1050, 700, 110, 300),
          flame(1050, 380, .8), '<path d="M0 900L0 700Q400 640 900 760L1200 900Z" fill="#2a2850"/>', scroll(380, 440, 1.2), person(500, 850, 2.3, '#8a6a4a', pose='point', cloth='#2a2018', halo='#fff3c4'),
          crowd(10, 7, 860, 890, 700, 1180, (.4, .5)))


@scene('elias_carmelo', 'Elias no Carmelo', 'elias carmelo baal baalins jezabel acabe', 3.4, V)
def _(s, t=0):
    s.sky('#2a2a3a', '#6a5a6a', '#d9a06a')
    s.add(cloud(220, 180, 2.8, '#4a4a5a', .95), cloud(900, 150, 3.0, '#3a3a4a', .95), peaks('#8a7a6a', 700, 260, 3, 8), '<rect y="740" width="1200" height="160" fill="#7a6a58"/>',
          stone_heap(180, 840, .9), stone_heap(1020, 840, .9), altar(600, 830, 2.6), lightning(560, 20, 3.4), lightning(660, 90, 2.4), s.glow(600, 560, 340, '#ffcf66', .7),
          person(860, 860, 1.7, ROBE, pose='up', cloth='#3a2a20'), crowd(12, 2, 830, 890, 80, 420, (.45, .6)))


@scene('daniel_leoes', 'Daniel e os leões', 'daniel leoes leao cova covas dario medos sadraque misaque abednego', 3.6, V)
def _(s, t=0):
    s.sky('#0a0810', '#1e1822', '#3a2e30')
    s.add('<path d="M0 0H1200V900H0Z" fill="#2a2420"/><ellipse cx="600" cy="90" rx="190" ry="60" fill="#8ec5e8" opacity=".9"/>', beams(600, 90, 160, '#fff6cf', .35, 5, 820),
          ''.join(f'<path d="M{x} 0L{x + 22} 900" stroke="#1a1612" stroke-width="3" opacity=".6"/>' for x in range(60, 1200, 120)), '<rect y="800" width="1200" height="100" fill="#4a3a2a"/>',
          quad(240, 820, 'lion', 1.4, '#c9a36b'), quad(960, 820, 'lion', 1.4, '#b8935a', flip=True), quad(420, 860, 'lion', 1.0, '#c9a36b', flip=True),
          s.glow(600, 700, 260, '#fff3c4', .6), person(600, 840, 2.0, ROBE, pose='pray', cloth='#3a2a20', halo='#fff3c4'))


# ---- Reis e Palácio ---------------------------------------------------------
@scene('davi_golias', 'Davi e Golias', 'golias funda fundas filisteu filisteus campeao gigante elah', 3.6, V)
def _(s, t=0):
    s.sky('#6aa0e0', '#bfd8f0', '#fdf2d4')
    s.add(cloud(240, 160, 1.4), ridge('#a8c8a0', 560, 25, 3), tent(120, 620, 200, 150, '#a8845a'), tent(1080, 620, 200, 150, '#8a6a4a'), ridge('#7aa65a', 700, 20, 4), '<rect y="760" width="1200" height="140" fill="#c9a36b"/>',
          person(940, 830, 3.5, '#6a6a72', cloth='#2a2a30', skin='#c9a07a'), shield(1060, 640, 1.5, '#5a5a62', '#9a9aa2'), '<rect x="780" y="380" width="10" height="460" fill="#6a4a2e"/><path d="M777 380L785 330L793 380Z" fill="#cfd6dd"/>',
          person(300, 850, 1.3, '#7a4a2e', cloth='#3a2a20', pose='stand'), sling(360, 700, 1.1, 20), rocks(210, 880, .6), rocks(250, 890, .5), sheep(110, 880, .7))


@scene('davi_harpa', 'Davi e a harpa', 'harpa harpas citara citaras alaude alaudes musica musicos cantor cantores cantico canticos instrumento instrumentos salmista tocar', 3.0, V)
def _(s, t=0):
    s.sky('#1c1a40', '#4a3a6a', '#d9703a')
    s.add(stars(40, 5, 340), fullmoon(940, 180, 56, '#d8d2c0'), ridge('#2a2038', 640, 40, 3), ridge('#1e1830', 720, 30, 5), '<rect y="790" width="1200" height="110" fill="#1a1420"/>',
          s.glow(540, 640, 340, '#ffd9a0', .45), rocks(560, 840, 2.6), person(540, 790, 1.9, '#7a4a2e', pose='sit', cloth='#3a2a20'), harp(700, 640, 1.2),
          notes(780, 360, 5), sheep(200, 850, 1.0), sheep(330, 870, .9), sheep(1000, 860, .9), tree(110, 760, 340, 'olive', '#4a6a3a', '#3a2a1c'))


@scene('salomao_sabedoria', 'Salomão e a sabedoria', 'salomao proverbios eclesiastes cantares prudente', 3.2, V)
def _(s, t=0):
    s.sky('#6a9ad8', '#c5dcf2', '#fdf2d4')
    s.add(columns(600, 780, 8, 150, 480, '#efe4cc'), s.glow(600, 400, 400, '#fff3c4', .45), '<rect y="780" width="1200" height="120" fill="#c9b99a"/>', '<rect x="480" y="520" width="240" height="260" fill="#e0b040"/><rect x="460" y="500" width="280" height="30" fill="#ffd166"/>',
          person(600, 780, 1.8, '#8a2f3c', cloth='#14100c', pose='sit'), crown(600, 440, .5), scales(330, 640, .7), book(870, 720, .8), person(240, 870, 1.3, '#7a4a2e', pose='kneel'), person(960, 870, 1.3, '#3b5a7a', pose='kneel'),
          tree(100, 780, 380, 'cedar', '#2f5a3a'), tree(1100, 780, 380, 'cedar', '#2f5a3a'))


@scene('absalao_rebeliao', 'Absalão', 'absalao joabe abner amnon adonias aitofel rebeliao rebelou rebelde rebeldes conspiracao conspirou', 3.0, V)
def _(s, t=0):
    s.sky('#6aa0e0', '#bfd8f0', '#fdf2d4')
    s.add(ridge('#a8c8a0', 560, 25, 3), ridge('#7aa65a', 660, 22, 4), '<rect y="760" width="1200" height="140" fill="#b5a47a"/>', tree(100, 760, 400, 'round', '#3f7a3a'), tree(1100, 760, 380, 'round', '#3f7a3a'),
          crowd(14, 5, 790, 890, 40, 440, (.5, .7)), crowd(14, 6, 790, 890, 760, 1160, (.5, .7)), chariot(520, 840, 1.2, '#e0b040'), quad(820, 830, 'donkey', 1.5, '#8a7a68'),
          person(830, 720, 1.0, '#8a2f3c', pose='sit', cloth='#14100c'), crown(830, 505, .4), banner(250, 760, 300, '#8a2f3c', 110))


@scene('reino_dividido', 'o reino dividido', 'roboao jeroboao ezequias josias manasses uzias jeoiaquim zedequias josafa amazias acaz jotao omri', 3.0, V)
def _(s, t=0):
    s.sky('#6a9ad8', '#c5dcf2', '#fdf2d4')
    s.add(cloud(220, 180, 1.4), cloud(980, 150, 1.4), ridge('#b5c89a', 560, 25, 3), '<rect y="640" width="1200" height="260" fill="#8aa660"/>', '<path d="M600 620L560 700L630 760L580 830L620 900" stroke="#2a1c10" stroke-width="16" fill="none"/>',
          banner(260, 700, 340, '#3b5a7a', 140), banner(940, 700, 340, '#8a2f3c', 140, True), crown(260, 340, 1.1), crown(940, 340, 1.1, '#e0b040', '#48cae4'),
          tower(120, 760, 120, 300), tower(1080, 760, 120, 300), crowd(10, 2, 800, 880, 120, 500, (.5, .7)), crowd(10, 3, 800, 880, 700, 1080, (.5, .7)))


@scene('ester_palacio', 'Ester no palácio', 'ester mardoqueu hama vasti persa persas assuero purim edito rainha rainhas palacio palacios', 3.2, V)
def _(s, t=0):
    s.sky('#3a2a5a', '#7a5a8a', '#f0c58a')
    s.add(columns(600, 780, 7, 150, 460, '#efe4cc'), s.glow(600, 400, 460, '#fff3c4', .45), '<rect y="780" width="1200" height="120" fill="#8a2f3c"/><rect x="260" y="760" width="680" height="24" fill="#b84a5a"/>',
          '<rect x="250" y="420" width="130" height="340" fill="#e0b040"/><path d="M250 420Q315 380 380 420Z" fill="#ffd166"/>', person(315, 760, 1.4, '#3b5a7a', cloth='#14100c', pose='sit'), crown(315, 520, .4),
          person(560, 850, 1.7, '#8a2f3c', cloth='#14100c', pose='kneel'), crown(560, 640, .38), person(760, 850, 1.5, '#e8dcc0', cloth='#3a2a20', pose='stand'),
          scroll(900, 840, .5), chalice(1000, 850, .5), lamp(130, 760, 1.2), lamp(1070, 760, 1.2))


# ---- Período Pós-Exílio e Líderes -------------------------------------------
@scene('neemias_reconstrucao', 'reconstruindo os muros', 'neemias esdras zorobabel reconstruir reconstruiu reconstruida reedificar reedificou edificar edificou edificaram edificado obreiros operarios construir construiu construiram', 2.6, V)
def _(s, t=0):
    s.sky('#f4b183', '#fce6c4', '#fff4e0')
    s.add(sun(900, 220, 80, '#fff3c4', .9), ridge('#c9b58a', 560, 25, 3), wall(0, 700, 700, 130), '<rect x="700" y="570" width="300" height="130" fill="#9b8468" opacity=".85"/>',
          ladder(780, 780, 330, 80, 8), ladder(520, 780, 300, 80, -6), '<rect y="780" width="1200" height="120" fill="#c9a36b"/>', stone_heap(1050, 850, 1.0), basket(300, 870, 1.0),
          person(640, 700, .9, '#7a4a2e', cloth='#3a2a20'), person(860, 780, 1.1, '#3b5a7a', cloth='#3a2a20', pose='point'), person(410, 870, 1.4, '#5a7a3b', cloth='#3a2a20'),
          person(150, 880, 1.2, '#8a2f3c', cloth='#3a2a20', pose='up'), sword(1110, 790, .5, 18))


@scene('jo_provacao', 'perseverança na provação', 'paciencia perseveranca perseverar perseverou suportar suportou suportam provacao provacoes provar provou provado provados aflito aflitos cinza cinzas', 2.6, V)
def _(s, t=0):
    s.sky('#3a3a4a', '#6a6a7a', '#c9b99a')
    s.add(cloud(240, 160, 2.8, '#4a4a5a', .95), cloud(900, 140, 2.6, '#5a5a6a', .95), s.glow(600, 330, 340, '#fff3c4', .55), beams(600, 200, 170, '#fff6cf', .22, 5, 800), ridge('#5a5048', 640, 40, 3),
          '<path d="M0 900L0 700Q600 640 1200 710L1200 900Z" fill="#8a7a6a"/>', rocks(160, 820, 1.8), rocks(1050, 830, 1.6), tree(1060, 760, 400, 'dead', '#2a2018'),
          person(560, 840, 2.0, '#6a6a5a', pose='sit', cloth='#8a8a7a'), person(960, 780, .7, '#4a4f6a', pose='stand'), person(1080, 790, .7, '#6b4a8a', pose='stand'))


@scene('principes_conselho', 'príncipes e chefes', 'principe principes chefe chefes capitao capitaes governador governadores autoridade autoridades magistrados juizes anciaos', 1.8, V)
def _(s, t=0):
    s.sky('#f4b183', '#fce6c4', '#fff4e0')
    s.add(sun(940, 200, 70, '#fff3c4', .9), ridge('#c9b58a', 540, 25, 3), wall(0, 330, 700, 180), wall(870, 1200, 700, 180), tower(360, 720, 130, 460), tower(840, 720, 130, 460),
          '<rect y="720" width="1200" height="180" fill="#c9a36b"/>', '<rect x="420" y="600" width="360" height="130" fill="#9b8468"/>')
    for i, c in enumerate(['#8a2f3c', '#3b5a7a', '#5a7a3b', '#6b4a8a', '#b88a3f']):
        s.add(person(380 + i * 110, 880 - (i % 2) * 20, 1.5, c, pose='sit', cloth='#3a2a20'))
    s.add(banner(180, 880, 300, '#8a2f3c', 100), banner(1020, 880, 300, '#3b5a7a', 100, True))


@scene('mensageiro', 'o mensageiro', 'enviou enviar enviei enviaram mensageiro mensageiros mensagem embaixador embaixadores recado correio', 1.6, V)
def _(s, t=0):
    s.sky('#f08a5d', '#f9d6a0', '#fdf0d4')
    s.add(sun(260, 250, 80, '#fff3c4', .9), ridge('#c9b58a', 570, 25, 3), '<path d="M0 900L0 720Q600 640 1200 700L1200 900Z" fill="#d9b97a"/>', '<path d="M0 860Q500 760 1200 780L1200 840Q500 820 0 900Z" fill="#c4a064"/>',
          cloud(520, 810, 1.0, '#e8d9c0', .5), cloud(420, 840, 1.2, '#e8d9c0', .5), person(660, 820, 1.8, '#3b5a7a', pose='walk', cloth='#3a2a20'), scroll(610, 640, .6), tower(1070, 700, 120, 320), wall(930, 1200, 700, 90))


@scene('povos_vizinhos', 'os povos vizinhos', 'moabe moabitas edom edomitas amom amonitas cananeus amorreus heteus jebuseus sidom tiro damasco siria', 2.8, V)
def _(s, t=0):
    s.sky('#f4b183', '#fce6c4', '#fff4e0')
    s.add(sun(180, 200, 70, '#fff3c4', .9), peaks('#b59a72', 600, 280, 4, 7), '<rect y="620" width="1200" height="280" fill="#d9b97a"/>', tent(200, 760, 280, 200, '#a8845a'), tent(600, 780, 300, 210, '#6a4a3a'), tent(1000, 760, 280, 200, '#c9a36b'),
          banner(360, 700, 260, '#8a2f3c', 100), banner(780, 700, 260, '#3b5a7a', 100), banner(1160, 690, 260, '#4a8a3a', 100, True), quad(450, 880, 'camel', .8, '#b8935a'), quad(880, 880, 'camel', .7, '#a8835a', flip=True))
