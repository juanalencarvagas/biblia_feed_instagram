"""Cenas de Narrativas e Episódios Bíblicos: milagres, eventos históricos e momentos marcantes."""
import math
from registry import scene, legacy
from svglib import *
from comuns import *

V = 4

# ---- Legados de Narrativas --------------------------------------------------
legacy('anjo', 'anjos', 'anjo* gabriel miguel querubim querubins serafim serafins sonho* visao visoes', 2)
legacy('arca', 'arca e dilúvio', 'noe arca diluvio', 3)


# ---- Narrativas do Antigo Testamento ----------------------------------------
@scene('eden_fruto', 'o Éden e o fruto', 'adao eva eden paraiso proibido proibida desobedeceu desobediencia costela', 3.4, V)
def _(s, t=0):
    s.sky('#8ec5e8', '#d6ecf5', '#fdf2d4')
    s.add(sun(180, 160, 70, '#fff3c4', .9), ridge('#a8c8a0', 560, 25, 3), '<rect y="640" width="1200" height="260" fill="#6aa04a"/>', grass(650, '#3f7a3a', 2, 140), tree(600, 780, 600, 'round', '#3f8a3a'),
          ''.join(f'<circle cx="{600 + dx}" cy="{y}" r="16" fill="#d62839"/>' for dx, y in ((-60, 380), (50, 350), (-10, 300), (90, 420), (-100, 440))), snake(480, 840, 1.3, '#4f7a3a'),
          person(220, 860, 1.7, '#4a8a3a', pose='stand', cloth='#3a2a20'), person(980, 860, 1.7, '#5a9a4a', pose='stand', cloth='#8a4a2a'),
          ''.join(flower(60 + i * 130, 880, 50 + (i % 3) * 14, ['#f4a8c0', '#ffd166', '#c8a8f0'][i % 3]) for i in range(9)))


@scene('torre_babel', 'a torre de Babel', 'babel torre torres tijolo tijolos betume confundiu confusao dispersou dispersaram idioma idiomas', 3.2, V)
def _(s, t=0):
    s.sky('#6aa0e0', '#bfd8f0', '#fdf2d4')
    s.add(cloud(220, 200, 1.6), cloud(950, 140, 1.8), cloud(600, 260, 1.2, op=.8), brick_tower(600, 800, 420, 640, 7), ridge('#c9b58a', 800, 20, 3), '<rect y="800" width="1200" height="100" fill="#d9b97a"/>',
          crowd(26, 4, 810, 890, 40, 1160, (.35, .5)), ''.join(rocks(120 + i * 220, 850, .7) for i in range(5)), flock(7, 3, 200, 1000, 150, 400))


@scene('sodoma_fogo', 'Sodoma', 'sodoma gomorra enxofre sal estatua fugiu fugir fugiram arruinou destruicao destruidas ló', 3.0, V)
def _(s, t=0):
    s.sky('#2a0a08', '#8a2a10', '#ff9f1c')
    s.add(cloud(240, 160, 2.8, '#3a1a14', .95), cloud(940, 130, 3.0, '#3a1a14', .95), ''.join(flame(120 + i * 140, 90 + (i % 3) * 40, .7) for i in range(9)),
          '<rect y="640" width="1200" height="260" fill="#4a2a1c"/>', wall(0, 640, 700, 150, '#6a4a38', '#4a2a1c'), tower(200, 710, 130, 340, '#6a4a38', '#4a2a1c'), tower(520, 710, 120, 300, '#6a4a38', '#4a2a1c'),
          flame(200, 400, 2.0), flame(520, 430, 1.8), flame(360, 560, 1.4), s.glow(360, 520, 420, '#ff7a1c', .5),
          person(840, 850, 1.7, '#7a4a2e', pose='walk', cloth='#3a2a20'), person(960, 860, 1.4, '#3b5a7a', cloth='#3a2a20'), person(1080, 840, 1.7, '#e9eef0', skin='#e9eef0', cloth='#e9eef0', pose='stand'))


@scene('moria_carneiro', 'o monte Moriá', 'moria isaque lenha cutelo abraao carneiro carneiros', 3.0, V)
def _(s, t=0):
    s.sky('#f4b183', '#fce6c4', '#fff4e0')
    s.add(beams(600, 0, 300, '#fff6cf', .3, 6, 800), peaks('#a8845a', 700, 420, 3, 6), '<rect y="760" width="1200" height="140" fill="#8a6a44"/>', altar(600, 780, 2.2),
          ''.join(f'<rect x="{510 + i * 30}" y="{610 - (i % 2) * 8}" width="80" height="10" fill="#6a4a2e" transform="rotate({-12 + i * 9} {550 + i * 30} 615)"/>' for i in range(5)),
          person(360, 850, 1.8, '#7a4a2e', pose='point', cloth='#3a2a20'), person(240, 870, 1.0, '#c9b79a', cloth='#3a2a20'), tree(940, 800, 280, 'dead', '#4a3a28'), sheep(950, 820, .9), dove(960, 330, .9))


@scene('escada_jaco', 'a escada de Jacó', 'escada escadas betel peniel jaboque travesseiro', 3.4, V)
def _(s, t=0):
    s.sky('#07102e', '#1c2a6a', '#3a4f9a')
    s.add(stars(90, 3, 520), fullmoon(240, 140, 46, '#d8d2c0'), s.glow(780, 160, 360, '#fff3c4', .8), beams(800, 120, 220, '#fff6cf', .22, 5, 600),
          ridge('#0e1830', 700, 40, 3), '<rect y="790" width="1200" height="110" fill="#14102a"/>', ladder(640, 740, 640, 110, 16, '#e8d9b0'),
          person(640, 700, .35, '#ffffff', pose='stand', cloth='#fff3c4', halo='#fff3c4'), person(700, 600, .35, '#ffffff', pose='stand', cloth='#fff3c4', halo='#fff3c4'),
          person(790, 450, .35, '#ffffff', pose='stand', cloth='#fff3c4', halo='#fff3c4'), rocks(300, 820, 1.4), lying(300, 830, 1.2))


@scene('egito_nilo', 'o Egito e o Nilo', 'egito egipcio egipcios nilo piramide piramides esfinge', 3.0, V)
def _(s, t=0):
    s.sky('#f08a5d', '#f9d6a0', '#fdf0d4')
    s.add(sun(850, 300, 90, '#fff3c4', .9), pyramid(300, 640, 460, 300), pyramid(700, 650, 320, 210), '<rect y="640" width="1200" height="260" fill="#d9b97a"/><path d="M0 760Q300 700 600 750T1200 740L1200 900L0 900Z" fill="#3f86ad"/>',
          waves(790, 4, '#d6edf5', .4, 40, 7, 10), boat(300, 830, .7, '#8a6a3a'), boat(800, 840, .6, '#8a6a3a'), tree(100, 750, 380, 'palm', '#3f7a3a'), tree(1090, 750, 360, 'palm', '#3f7a3a'), flock(5, 4, 100, 700, 120, 260))


@scene('sarca_ardente', 'a sarça ardente', 'sarca sarcas ardia ardendo arde horebe descalco sandalias pastoreava', 3.4, V)
def _(s, t=0):
    s.sky('#27336b', '#c06a8a', '#ffd9a0')
    s.add(peaks('#8a6a5a', 700, 360, 3, 5), '<rect y="740" width="1200" height="160" fill="#a88a5a"/>', s.glow(700, 620, 380, '#ffcf66', .8), beams(700, 380, 160, '#fff6cf', .22, 5, 800),
          tree(700, 820, 300, 'round', '#4f7a2a'), ''.join(flame(620 + i * 40, 760 - (i % 3) * 60, 1.1 + (i % 2) * .4) for i in range(5)), rocks(180, 850, 1.4),
          person(360, 860, 1.8, '#7a4a2e', pose='kneel', cloth='#3a2a20', staff=True), sheep(130, 880, .8), sheep(1050, 880, .8))


@scene('pragas_egito', 'as pragas do Egito', 'praga pragas granizo mosca moscas sapos primogenito primogenitos ferida feridas', 3.0, V)
def _(s, t=0):
    s.sky('#2a2a30', '#5a4a40', '#a87a52')
    s.add(cloud(220, 170, 2.6, '#4a4a52', .95), cloud(920, 140, 2.8, '#3a3a42', .95), lightning(560, 10, 2.2), pyramid(260, 640, 420, 260, '#b89a62', '#8a7242'), pyramid(560, 650, 300, 190, '#b89a62', '#8a7242'),
          '<rect y="640" width="1200" height="260" fill="#8a7a58"/><path d="M0 760Q300 720 600 770T1200 760L1200 900L0 900Z" fill="#7a1c1c"/>', snowfall(80, 9, '#e8f0f4', .8),
          scatter(frog, 7, 3, 80, 1100, 800, 880, .8, 1.3), scatter(locust, 10, 4, 100, 1100, 180, 560, .8, 1.4), scatter(bee, 9, 6, 100, 1100, 220, 600, .6, 1.0))


@scene('exodo_mar', 'a travessia do mar', 'exodo israelitas israelita dividiu dividiram divididas atravessaram passagem perseguiu perseguidores cavaleiros', 3.2, V)
def _(s, t=0):
    s.sky('#27336b', '#7a6a9a', '#f4c58a')
    s.add(cloud(600, 190, 2.8, '#ffffff', .9), beams(600, 240, 120, '#fff6cf', .3, 4, 900), '<rect y="260" width="1200" height="640" fill="#1f5a82"/>',
          '<path d="M0 260L470 260L540 900L0 900Z" fill="#0f3a62"/><path d="M730 260L1200 260L1200 900L660 900Z" fill="#0f3a62"/>',
          waves(300, 7, '#8fd0ea', .35, 80, 8, 26), '<path d="M500 900L585 260L615 260L700 900Z" fill="#d9b97a"/>',
          crowd(30, 4, 450, 880, 520, 690, (.22, .5)), s.glow(600, 600, 300, '#fff3c4', .35), person(600, 330, .5, ROBE, pose='up', cloth='#5a3b22'))


@scene('mana_codornizes', 'maná no deserto', 'mana codorniz codornizes recolher recolhiam recolheram porcao', 3.0, V)
def _(s, t=0):
    s.sky('#f4b183', '#fce6c4', '#fff4e0')
    s.add(sun(940, 190, 80, '#fff3c4', .9), ridge('#c9b58a', 600, 25, 3), '<rect y="640" width="1200" height="260" fill="#d9b97a"/>', tent(180, 720, 240, 180, '#e8dcc0'), tent(1050, 720, 240, 180, '#e8dcc0'),
          snowfall(110, 4, '#fff6d6', .9), flock(10, 5, 150, 1050, 120, 420, '#8a6a4a'), basket(380, 880, 1.2), basket(820, 880, 1.2), crowd(10, 6, 790, 890, 200, 1000, (.45, .7)), person(600, 860, 1.5, '#7a4a2e', pose='up'))


@scene('josue_jerico', 'os muros de Jericó', 'josue jerico derrubou derrubados cercaram cercou conquistou conquista gibeao', 3.4, V)
def _(s, t=0):
    s.sky('#f08a5d', '#f9d6a0', '#fdf0d4')
    s.add(sun(960, 200, 80, '#fff3c4', .9), ridge('#b5a87a', 600, 25, 3), wall(0, 520, 640, 160), wall(780, 1200, 640, 160), tower(520, 650, 140, 360), tower(780, 650, 140, 360),
          rocks(560, 790, 2.2), rocks(660, 800, 1.8), rocks(760, 790, 2.0), cloud(520, 700, 2.4, '#e8d9c0', .8), cloud(760, 710, 2.4, '#e8d9c0', .8),
          '<rect y="800" width="1200" height="100" fill="#b5a47a"/>', sound_waves(300, 720, 60, 4, '#fff6cf', .5, -50, 50), shofar(180, 800, .6),
          crowd(14, 7, 820, 890, 60, 520, (.5, .7)), person(380, 850, 1.7, ROBE, pose='up', cloth='#5a3b22'))


@scene('gideao_cantaros', 'Gideão e as tochas', 'gideao midianitas midianita midia cantaros cantaro tochas tocha lamparas trezentos amalequitas amalec', 3.2, V)
def _(s, t=0):
    s.sky('#05050f', '#14183a', '#2a2f5a')
    s.add(stars(70, 4, 380), fullmoon(240, 170, 54, '#d8d2c0'), ridge('#0e1028', 520, 40, 2), '<rect y="680" width="1200" height="220" fill="#14102a"/>',
          tent(300, 800, 220, 160, '#5a4a3a'), tent(560, 820, 240, 170, '#5a4a3a'), tent(840, 800, 220, 160, '#5a4a3a'), tent(1060, 830, 200, 150, '#5a4a3a'))
    for i in range(16):
        x, y = 60 + i * 72, 500 + (i % 3) * 40
        s.add(person(x, y + 70, .55, '#3b3a5a', cloth='#14102a', pose='up'), flame(x - 20, y - 70, .35), flame(x + 20, y - 70, .35), jar(x - 38, y - 30, .2))
    s.add(sound_waves(600, 380, 60, 3, '#fff3c4', .35, -70, 70), shofar(600, 360, .5))


@scene('elias_carro', 'o carro de fogo', 'eliseu redemoinho arrebatado', 3.2, V)
def _(s, t=0):
    s.sky('#27336b', '#c06a8a', '#ffd9a0')
    s.add(rays(600, 330, 110, 800, 22, '#fff3c4', .2, 12), cloud(220, 260, 2.2, '#ffffff', .7), cloud(980, 220, 2.2, '#ffffff', .7), s.glow(600, 330, 340, '#ffcf66', .8),
          quad(470, 430, 'horse', .8, '#ff9f1c', dark='#e8741c'), quad(740, 440, 'horse', .8, '#ff9f1c', flip=True, dark='#e8741c'), chariot(600, 400, 1.4, '#ffcf66'),
          ''.join(flame(200 + i * 100, 480 + (i % 3) * 20, .5) for i in range(9)), ridge('#3a3a6a', 740, 40, 3), '<rect y="800" width="1200" height="100" fill="#1e2244"/>',
          person(300, 860, 1.5, '#8a6a4a', pose='up', cloth='#3a2a20'))


@scene('fornalha_ardente', 'a fornalha ardente', 'fornalha fornalhas ardente estatua atados queimar queimado queimou', 3.2, V)
def _(s, t=0):
    s.sky('#2a0a08', '#8a2a10', '#ff9f1c')
    s.add(s.glow(600, 600, 560, '#ffd166', .7), '<path d="M300 860V420Q600 260 900 420V860Z" fill="#14080a"/><path d="M360 860V460Q600 330 840 460V860Z" fill="#ff7a1c"/>',
          ''.join(flame(330 + i * 70, 860, 1.3 + (i % 3) * .4) for i in range(9)), person(500, 850, 1.3, ROBE, pose='stand', cloth='#e0b040', halo='#fff3c4'),
          person(600, 850, 1.5, '#ffffff', pose='stand', cloth='#fff3c4', halo='#fff3c4'), person(700, 850, 1.3, ROBE, pose='stand', cloth='#e0b040', halo='#fff3c4'),
          person(110, 840, 1.6, '#6b3f2a', cloth='#e0b040', pose='point'), crown(110, 600, .7))


@scene('exilio_babilonia', 'o exílio na Babilônia', 'exilio exilados exilado nabucodonosor caldeus caldeia assirios assiria senaqueribe salgueiros ceifaram deportados deportado babilonia', 3.2, V)
def _(s, t=0):
    s.sky('#1c1a40', '#4a3a6a', '#d9703a')
    s.add(fullmoon(930, 170, 48, '#d8d2c0'), brick_tower(240, 640, 300, 420, 5), ridge('#2a2038', 640, 30, 3), '<rect y="640" width="1200" height="260" fill="#2f5a7a"/>', waves(680, 5, '#9fd0ea', .3, 54, 8, 14),
          '<rect y="780" width="1200" height="120" fill="#4a4030"/>', tree(160, 800, 360, 'olive', '#4a6a5a', '#2a2018'), tree(1040, 800, 380, 'olive', '#4a6a5a', '#2a2018'), harp(170, 560, .5), harp(1030, 540, .5),
          person(500, 860, 1.4, '#6a6a7a', pose='sit', cloth='#2a2a30'), person(700, 870, 1.4, '#7a5a5a', pose='sit', cloth='#2a2a30'), person(850, 860, 1.3, '#5a6a7a', pose='kneel', cloth='#2a2a30'))


# ---- Narrativas do Evangelho e Novo Testamento ------------------------------
@scene('natividade', 'a natividade', 'manjedoura manjedouras estrebaria estalagem magos reis-magos pastores-noite oriente presente-ouro incenso-mirra mirra estrela-oriente nasceu-belem', 3.2, V)
def _(s, t=0):
    s.sky('#050a1f', '#14235a', '#2a3f80')
    s.add(stars(90, 7, 500), s.glow(600, 150, 320, '#fff3c4', .8), star(600, 150, 50, '#fff7d6', 8, .35), beams(600, 190, 150, '#fff6cf', .22, 4, 700), ridge('#0e1830', 640, 40, 3),
          '<path d="M280 780V520L600 380L920 520V780Z" fill="#3a2a1c"/><path d="M250 530L600 370L950 530L920 500L600 350L280 500Z" fill="#6a4a2c"/><rect y="780" width="1200" height="120" fill="#1c1410"/>',
          s.glow(600, 700, 300, '#ffd9a0', .6), manger(600, 770, 1.9), person(430, 840, 1.5, '#3b5a7a', pose='kneel', cloth='#e8dcc0'), person(790, 830, 1.5, '#7a4a2e', staff=True),
          sheep(250, 850, .8), sheep(1000, 860, .8), quad(150, 640, 'camel', .35, '#6a4a2a'), quad(250, 650, 'camel', .3, '#6a4a2a'))


@scene('batismo_jordao', 'batismo no Jordão', 'jordao batista batismo batismos batizar batizou batizado batizados batizando arrependimento-batismo', 3.2, V)
def _(s, t=0):
    s.sky('#8ec5e8', '#cfe8f2', '#fdf2d4')
    s.add(sun(180, 170, 60, '#fff3c4', .9), ridge('#b5c89a', 520, 25, 2), ridge('#7aa65a', 580, 20, 3), '<rect y="590" width="1200" height="310" fill="#3f86ad"/>',
          waves(620, 5, '#d6edf5', .45, 56, 8, 14), tree(110, 610, 360, 'palm', '#3f7a3a'), tree(1090, 610, 340, 'palm', '#3f7a3a'),
          person(520, 690, 1.5, '#d9c9a5', cloth='#5a3b22', pose='stand'), person(690, 700, 1.5, ROBE, pose='pray', cloth='#5a3b22'),
          waves(690, 2, '#d6edf5', .7, 30, 10, 10), beams(640, 150, 200, '#fff6cf', .22, 5, 650), dove(640, 190, 1.2))


@scene('tentacao', 'tentação no deserto', 'tentacao tentacoes tentar tentado tentador tentou satanas diabo demonio demonios imundo imundos espirito-imundo jejum jejuar jejuou', 3.0, V)
def _(s, t=0):
    s.sky('#1a1020', '#5a2a3a', '#d9703a')
    s.add(fullmoon(930, 170, 50, '#d8d2c0'), peaks('#3a2a38', 640, 380, 4, 4), ridge('#2a1a22', 700, 30, 3), '<rect y="770" width="1200" height="130" fill="#241418"/>',
          s.glow(860, 520, 200, '#ff3a2a', .45), person(870, 640, 1.6, '#14080c', skin='#3a1a1a', cloth='#14080c', pose='point'),
          '<circle cx="852" cy="470" r="6" fill="#ff4a3a"/><circle cx="880" cy="470" r="6" fill="#ff4a3a"/>',
          rocks(300, 840, 1.2), rocks(440, 850, .8, '#7a6a58'), bread(360, 800, .5), person(540, 860, 1.7, ROBE, pose='pray', cloth='#5a3b22', halo='#fff3c4'))


@scene('cura', 'Jesus cura os enfermos', 'curou curar cura curas curado curados sarar sarou sarado sara enfermo enfermos enfermidade enfermidades doente doentes doenca doencas leproso leprosos lepra paralitico paralitica febre aleijado', 3.0, V)
def _(s, t=0):
    s.sky('#f4b183', '#fce6c4', '#fff4e0')
    s.add(sun(950, 200, 80, '#fff3c4', .9), ridge('#c9b58a', 560, 30, 3), house(250, 700, 330, 230, '#e8d4a8'), house(1000, 690, 220, 160, '#dcc597'),
          '<rect y="700" width="1200" height="200" fill="#c9a36b"/>', grass(710, '#9a8a50', 4, 60),
          person(430, 830, 1.0, '#7a4a2e', pose='stand'), person(530, 835, 1.7, ROBE, pose='point', cloth='#5a3b22', halo='#fff3c4'),
          s.glow(655, 600, 170, '#fff3c4', .85), beams(655, 520, 120, '#fff6cf', .3, 5, 840),
          person(740, 830, 1.5, '#4a4f6a', pose='sit', cloth='#c9b79a'), '<path d="M830 840L860 640" stroke="#6b4a2a" stroke-width="9" stroke-linecap="round"/>',
          person(940, 835, 1.0, '#3b5a7a', pose='kneel'))


@scene('cego', 'o cego que vê', 'cego cegos cegueira vista enxergar enxergou enxergam ver-luz luminar abrir-olhos guia guias', 2.8, V)
def _(s, t=0):
    s.sky('#6aa0e0', '#bfd8f0', '#fdf2d4')
    s.add(sun(600, 260, 110, '#fff7d6', .95), rays(600, 260, 150, 900, 28, '#fff3c4', .22, 14), peaks('#c9b58a', 600, 200, 4, 9), ridge('#c9a36b', 650, 30, 3),
          '<path d="M0 780Q400 700 700 650Q950 620 1200 640L1200 900L0 900Z" fill="#d9b97a"/>', tree(1030, 650, 360, 'palm', '#3f7a3a'), tree(130, 700, 300, 'palm', '#3f7a3a'),
          person(470, 800, 1.7, '#7a4a2e', staff=True, cloth='#c9b79a'), person(740, 790, 1.7, ROBE, pose='point', cloth='#5a3b22', halo='#fff3c4', flip=True),
          s.glow(470, 640, 120, '#fff3c4', .8))


@scene('multiplicacao', 'pães e peixes para a multidão', 'multidao multidoes cesto cestos cestas alimentar alimentou saciar saciados saciou fartar fartaram sobras sobraram fome-multidao milagre milagres sinal sinais', 3.0, V)
def _(s, t=0):
    s.sky('#86b9e8', '#cfe3f0', '#fdf2d4')
    s.add(sun(1000, 150, 60, '#fff3c4', .9), cloud(200, 180, 1.2, op=.9), ridge('#a8c8a0', 520, 25, 3), ridge('#7aa65a', 600, 20, 4), '<rect y="620" width="1200" height="280" fill="#5f9a47"/>',
          crowd(34, 3, 650, 880, 0, 1200, (.28, .42)), person(600, 620, 1.5, ROBE, pose='up', cloth='#5a3b22', halo='#fff3c4'),
          basket(320, 880, 1.1), basket(480, 890, 1.0), basket(720, 890, 1.0), basket(880, 880, 1.1),
          '<rect x="500" y="620" width="200" height="14" fill="#8a5a34"/>', bread(560, 618, .35), fish(630, 612, .7, '#7fa4b8'))


@scene('barco_galileia', 'barco no mar da Galileia', 'barco barcos nau naus remar remou remaram afundar afundando duvidar duvidou duvida atravessar atravessou travessia margem lago-galileia pescaria', 2.6, V)
def _(s, t=0):
    s.sky('#f4b183', '#fce6c4', '#fff4e0')
    s.add(sun(900, 260, 90, '#fff3c4', .9), peaks('#b5a8c0', 520, 200, 4, 3), ridge('#8aa0a8', 540, 20, 4), '<rect y="540" width="1200" height="360" fill="#4a90b8"/>', waves(580, 6, '#e0f2f6', .4, 56, 8, 16),
          boat(360, 700, 1.5), person(300, 705, .9, '#3b5a7a', pose='stand'), person(400, 705, .9, '#8a2f3c', pose='up'),
          person(850, 740, 1.2, ROBE, pose='stand', cloth='#5a3b22', halo='#fff3c4'), waves(740, 2, '#e8f6fa', .8, 24, 10, 10), flock(5, 2, 500, 1000, 120, 300))


@scene('hosana', 'hosana e bênçãos', 'hosana bendito benditos bendita bendizer bendizei bendisse bendigo bendiga bencao bencaos abencoar abencoou abencoados abencoado aclamar aclamavam', 2.8, V)
def _(s, t=0):
    s.sky('#6aa0e0', '#bfd8f0', '#fdf2d4')
    s.add(sun(180, 160, 70, '#fff3c4', .9), cloud(780, 170, 1.4, op=.9), ridge('#b5a47a', 520, 25, 3), wall(0, 460, 560, 140), tower(500, 580, 140, 380), '<path d="M0 900L0 700Q600 600 1200 700L1200 900Z" fill="#c9a36b"/>',
          tree(120, 740, 400, 'palm', '#3f7a3a'), tree(1090, 740, 420, 'palm', '#3f7a3a'), '<ellipse cx="420" cy="860" rx="120" ry="24" fill="#8a2f3c"/><ellipse cx="800" cy="850" rx="110" ry="22" fill="#3b5a7a"/>',
          crowd(8, 2, 760, 880, 20, 360, (.55, .7)), crowd(8, 3, 760, 880, 840, 1180, (.55, .7)), quad(600, 870, 'donkey', 1.2, '#8a7a68'),
          person(600, 740, 1.2, ROBE, pose='sit', cloth='#5a3b22', halo='#fff3c4'), ''.join(palm_leaf(60 + i * 60, 740, .8) for i in range(5)), ''.join(palm_leaf(900 + i * 60, 740, .8) for i in range(5)))


@scene('lava_pes', 'lavar os pés', 'pes lavar lavou lavais lavai lavado lavados lavamento bacia toalha servir serviu servico servo-humilde humildemente sandalias', 2.8, V)
def _(s, t=0):
    room(s, ('#2a1a14', '#5a3a24'), 700, ('#6a4a30', '#3a2616'))
    s.add(s.glow(600, 450, 520, '#ffd9a0', .5), '<path d="M380 700V300Q600 140 820 300V700Z" fill="#1c130d" opacity=".7"/>', lamp(220, 640, 1.2), lamp(980, 640, 1.2),
          person(780, 810, 1.7, '#7a4a2e', pose='sit', cloth='#3a2a20'), '<ellipse cx="560" cy="830" rx="110" ry="26" fill="#b5683a"/><ellipse cx="560" cy="822" rx="92" ry="17" fill="#6fb0c8"/>',
          person(430, 840, 1.7, ROBE, pose='kneel', cloth='#5a3b22', halo='#fff3c4'), '<path d="M470 700Q560 740 620 760" stroke="#e8dcc0" stroke-width="22" fill="none" stroke-linecap="round"/>')


@scene('ceia', 'a última ceia', 'ceia mesa mesas calice calices vinho vinhos comer comeu comei comemos comida convidados convidado banquete jantar', 2.8, V)
def _(s, t=0):
    room(s, ('#2a1a14', '#5a3a24'), 700, ('#6a4a30', '#3a2616'))
    s.add(s.glow(600, 360, 520, '#ffd9a0', .55), '<path d="M330 660V250Q600 80 870 250V660Z" fill="#1c130d"/><path d="M360 660V270Q600 120 840 270V660Z" fill="#e8b878" opacity=".5"/>')
    for i in range(9):
        x = 190 + i * 102
        s.add(person(x, 650, 1.05 if i != 4 else 1.25, COLORS[i % 8] if i != 4 else ROBE, pose='stand', cloth='#3a2a20', halo='#fff3c4' if i == 4 else None))
    s.add('<rect x="120" y="610" width="960" height="30" fill="#8a5a34"/><rect x="130" y="640" width="940" height="140" fill="#e8dcc0"/><path d="M130 700H1070" stroke="#c9b79a" stroke-width="4"/>',
          bread(420, 606, .5), chalice(600, 606, .6), bread(780, 606, .5), jar(240, 606, .45), jar(960, 606, .45))


@scene('getsemani', 'Getsêmani', 'getsemani horto agonia vigiar vigiai vigiem velai velar dormir dormiam dormindo adormecidos angustia-noite traicao-noite', 3.0, V)
def _(s, t=0):
    s.sky('#05050f', '#14183a', '#2a2f5a')
    s.add(stars(50, 4, 380), fullmoon(980, 150, 54, '#d8d2c0'), ridge('#0e1028', 660, 40, 2), tree(160, 800, 520, 'olive', '#2f4a3a', '#1c1410'), tree(1060, 800, 560, 'olive', '#2f4a3a', '#1c1410'),
          tree(620, 700, 300, 'olive', '#2f4a3a', '#1c1410'), '<rect y="800" width="1200" height="100" fill="#0a0a14"/>', rocks(520, 830, 1.8, '#3a3a4a', '#4a4a5a'),
          s.glow(520, 740, 260, '#fff3c4', .35), person(520, 830, 1.6, ROBE, pose='kneel', cloth='#3a2a20', halo='#fff3c4'),
          person(860, 880, 1.0, '#3b5a7a', pose='sit'), person(960, 890, 1.0, '#8a2f3c', pose='sit'), person(1050, 880, 1.0, '#5a7a3b', pose='sit'),
          ''.join(flame(150 + i * 36, 600 + (i % 2) * 10, .22) for i in range(4)))


@scene('tumulo_vazio', 'o túmulo vazio', 'tumulo tumulos sepulcro sepulcros sepultura sepulturas sepultado sepultados sepultar sepultou sepultamento ressurreicao ressuscitou ressuscitado pedra-removida mulheres-sepulcro madrugada', 3.4, V)
def _(s, t=0):
    s.sky('#27336b', '#c06a8a', '#ffd9a0')
    s.add(sun(880, 640, 90, '#fffbe8', .95), rays(880, 640, 130, 700, 20, '#fff3c4', .2, 12), ridge('#3a3a6a', 640, 40, 2), ridge('#232850', 720, 30, 5),
          cross(1000, 440, 170, '#14102a'), cross(1070, 470, 130, '#14102a'), '<rect y="780" width="1200" height="120" fill="#1e2244"/>',
          s.glow(380, 700, 280, '#fff3c4', .6), tomb(380, 790, 1.5), person(780, 830, 1.5, '#ffffff', pose='stand', cloth='#ffffff', halo='#fff3c4'),
          person(620, 850, 1.0, '#6b4a8a', pose='kneel', cloth='#2a1f3a'), person(700, 860, 0.9, '#8a2f3c', pose='kneel', cloth='#2a1f3a'))


@scene('ascensao', 'a ascensão', 'ascender ascendeu ascensao subir subiu subiram subindo elevado elevou elevar levantado exaltado exaltou ceus-subiu nuvem-subiu', 2.8, V)
def _(s, t=0):
    s.sky('#6aa0e0', '#bfd8f0', '#fdf2d4')
    s.add(beams(600, 120, 360, '#fff6cf', .22, 7, 700), cloud(300, 300, 2.2), cloud(900, 260, 2.2), ridge('#a8c8a0', 700, 25, 3), '<path d="M0 900L0 740Q600 680 1200 740L1200 900Z" fill="#6aa04a"/>',
          s.glow(600, 340, 240, '#fff3c4', .9), cloud(600, 470, 2.6, '#ffffff', .95), person(600, 420, 1.5, '#ffffff', pose='up', cloth='#fff3c4', halo='#fff3c4'),
          person(360, 860, 1.3, '#7a4a2e', pose='up'), person(480, 880, 1.3, '#3b5a7a', pose='up'), person(720, 880, 1.3, '#8a2f3c', pose='up'), person(840, 860, 1.3, '#5a7a3b', pose='up'),
          tree(100, 780, 320, 'olive', '#7f9a5a', '#5a4a38'), tree(1100, 780, 320, 'olive', '#7f9a5a', '#5a4a38'))


@scene('pentecostes', 'Pentecostes', 'pentecostes consolador espirito-santo linguas chamas-linguas cheios-espirito cheio-espirito vento-forte poder-do-alto receberam-espirito', 3.0, V)
def _(s, t=0):
    room(s, ('#2a1a2a', '#8a3a2a'), 760, ('#7a5230', '#3a2616'))
    s.add(s.glow(600, 200, 600, '#fff3c4', .8), beams(600, 40, 540, '#fff6cf', .2, 9, 800), columns(600, 770, 4, 330, 560, '#d8c9a8'), dove(600, 180, 1.5))
    for i in range(9):
        x = 110 + i * 122
        s.add(person(x, 850 - (i % 2) * 20, 1.1, COLORS[i % 8], cloth=['#3a2a20', '#2a2a2a'][i % 2], pose=['up', 'stand', 'pray'][i % 3]), flame(x, 850 - (i % 2) * 20 - 270, .5))


@scene('igreja', 'a primeira igreja', 'igreja igrejas congregacao congregacoes assembleia assembleias comunhao reuniao reunidos reunir reuniram unidos unidade membros corpo-cristo santos-igreja', 2.6, V)
def _(s, t=0):
    s.sky('#1c1a40', '#4a3a6a', '#d9703a')
    s.add(stars(40, 5, 300), ridge('#2a2038', 640, 40, 3), '<rect y="740" width="1200" height="160" fill="#2a2018"/>', s.glow(600, 600, 520, '#ffd9a0', .5),
          house(600, 740, 560, 360, '#d9c49a', '#8a6a44'), '<rect x="500" y="460" width="70" height="90" fill="#ffd166"/><rect x="640" y="460" width="70" height="90" fill="#ffd166"/>',
          tree(120, 800, 380, 'olive', '#4a6a3a', '#3a2a1c'), tree(1090, 800, 340, 'olive', '#4a6a3a', '#3a2a1c'),
          crowd(12, 8, 790, 880, 160, 1040, (.55, .75)), lamp(180, 760, .8), lamp(1020, 760, .8))


@scene('arrependimento', 'arrependimento e conversão', 'arrepender arrependei arrependeu arrependimento arrependam arrependido converter converteu convertei conversao convertido publicano publicanos pecadores-arrependidos contrito contrita', 2.8, V)
def _(s, t=0):
    room(s, ('#1c1a28', '#4a4458'), 700, ('#6a6258', '#3a362e'))
    s.add(columns(220, 720, 2, 140, 520, '#b9ae94'), columns(980, 720, 2, 140, 520, '#b9ae94'), beams(600, 0, 200, '#fff6cf', .3, 5, 800), s.glow(600, 700, 300, '#fff3c4', .55),
          chain(250, 790, 5, '#7a838b', 50, broken_at=3), coin(900, 840, 26), coin(960, 860, 22), coin(1010, 835, 24), person(600, 840, 2.0, '#7a4a2e', pose='kneel', cloth='#2a2018'))


@scene('salvacao', 'salvação e resgate', 'salvacao salvador salvar salvou salvo salvos salva salvai redencao redentor redimir redimiu resgatar resgate resgatou livramento livrar livrou libertador', 3.0, V)
def _(s, t=0):
    s.sky('#3a4a68', '#7a8aa8', '#f0d9a8')
    s.add(beams(560, 0, 320, '#fff6cf', .22, 6, 760), cloud(200, 140, 2.2, '#5a6a88', .95), cloud(980, 120, 2.4, '#6a7a98', .95), '<rect y="560" width="1200" height="340" fill="#2a5a7e"/>',
          waves(580, 5, '#bfe0ee', .45, 60, 9, 22), '<path d="M0 900L0 420Q120 380 260 450L360 520L420 900Z" fill="#4a463e"/><path d="M0 420Q120 380 260 450L200 470L90 430Z" fill="#6a645a"/>',
          person(300, 440, 1.7, ROBE, pose='kneel', cloth='#5a3b22', halo='#fff3c4'), '<path d="M360 330Q470 340 560 560" stroke="#c9a36b" stroke-width="9" fill="none" stroke-dasharray="14 8" stroke-linecap="round"/>',
          person(620, 720, 1.3, '#7a4a2e', pose='up', cloth='#3a2a20'), waves(724, 2, '#bfe0ee', .8, 28, 10, 12), anchor(980, 700, .7))


@scene('juizo', 'o juízo', 'juizo juizos juiz juizes julgar julgou julgado julgamento julgamentos condenar condenacao condenado sentenca castigo castigar castigou tribunal', 2.6, V)
def _(s, t=0):
    s.sky('#1c1228', '#5a2a3a', '#d9703a')
    s.add(beams(600, 30, 360, '#fff6cf', .16, 7, 900), '<path d="M380 440L820 440L860 700L340 700Z" fill="#c9a34a"/><rect x="520" y="300" width="160" height="150" fill="#e0b84a"/><rect x="500" y="280" width="200" height="30" fill="#e0b84a"/>',
          '<rect x="300" y="700" width="600" height="40" fill="#8a7a58"/><rect x="260" y="740" width="680" height="40" fill="#7a6a4a"/><rect x="220" y="780" width="760" height="120" fill="#6a5a3c"/>',
          person(600, 520, 1.5, ROBE, pose='stand', cloth='#fff3c4', halo='#fff3c4'), scales(300, 600, .6), book(900, 640, .6),
          crowd(24, 2, 810, 890, 100, 1100, (.4, .55)))


@scene('trono_celeste', 'o trono celestial', 'anciaos cordeiro apocalipse revelacao selo selos trombeta trombetas besta dragao viventes seres-viventes candeeiros vestes-brancas multidao-vestes jerusalem-nova', 2.8, V)
def _(s, t=0):
    s.sky('#07102e', '#1c2a6a', '#3a4f9a')
    s.add(stars(70, 3, 520), s.glow(600, 440, 460, '#fff3c4', .95), rainbow(600, 560, 440, 24, .8), '<rect x="520" y="400" width="160" height="170" rx="14" fill="#fff3c4"/><rect x="500" y="380" width="200" height="30" fill="#ffe08a"/>',
          ''.join(f'<circle cx="{n(600 + 330 * math.cos(math.radians(a)))}" cy="{n(600 + 190 * math.sin(math.radians(a)) - 60)}" r="24" fill="#e0b84a" stroke="#fff3c4" stroke-width="4"/>'
                  for a in range(190, 360, 15)),
          ''.join(flame(330 + i * 90, 400, .5) for i in range(7)), '<rect y="700" width="1200" height="200" fill="#4a7ab8" opacity=".7"/>',
          waves(730, 3, '#e0f0ff', .5, 60, 8, 14), sheep(600, 800, 1.1, '#ffffff'))
