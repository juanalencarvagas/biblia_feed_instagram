"""Cenas de Animais: todas as criaturas terrestres, aves, peixes e rebanhos."""
from registry import scene, legacy
from svglib import *
from comuns import *

# ---- Legados de animais e rebanhos ------------------------------------------
legacy('pastor', 'pastor e ovelhas', 'pastor* ovelha* rebanho* cordeiro* abel davi', 2)
legacy('peixe', 'pesca', 'peixe* pescador* pescadores rede redes genesare galileia pedro tiago andre', 2)
legacy('pomba', 'pomba e Espírito', 'pomba* espirito batiz* batism* jonas', 2)


def pasto(s, sky=('#74b5e6', '#d1ebf7'), g1='#8cc36f', g2='#5da048', sunpos=(980, 170)):
    s.sky(*sky)
    s.add(sun(sunpos[0], sunpos[1], 66, '#fff3c4', .9), cloud(260, 200, 1), ridge(g1, 560, 30, 4), ridge(g2, 660, 30, 7), grass(660, '#2f6b3a', 3, 150))


@scene('cavalo', 'cavalo', 'cavalo* cavalos egua cavaleiro* carro* carros corcel', 2)
def _(s):
    pasto(s)
    s.add(quad(430, 800, 'horse', 2.1, '#6b3f22', False, '#4a2a16'), quad(930, 760, 'horse', 1.1, '#e8e0d0', True, '#c9bfae'))


@scene('jumento', 'jumento', 'jumento* asno* asna* burro* jumentinho', 2.4)
def _(s):
    pasto(s, ('#f3c58a', '#fbe6bf'), '#c9a56a', '#a88a52', (240, 200))
    s.add(quad(560, 800, 'donkey', 2.2, '#8a7a6a', False, '#6a5a4a'), tree(1010, 790, 460, 'palm', '#2f7a3a'), tree(1120, 800, 330, 'palm', '#3f8a3a'))


@scene('camelo', 'camelo', 'camelo* camelos dromedario*', 2.4)
def _(s):
    s.sky('#f2a65a', '#fbd8a2', '#fdeccc')
    s.add(sun(260, 250, 80, '#fff3c4', .9), ridge('#e3b872', 620, 40, 3), ridge('#c99a52', 740, 30, 5), quad(620, 810, 'camel', 2.4, '#b88a4f', False, '#8a6334'),
          quad(1030, 770, 'camel', 1.0, '#a87a42', True, '#7a5530'))


@scene('boi', 'boi e gado', 'boi bois vaca* gado bezerro* novilho* touro* rebanho-de-bois', 2.2)
def _(s):
    pasto(s, ('#8fc2e6', '#d9ecf6'), '#8cc36f', '#5da048')
    s.add(quad(450, 800, 'ox', 2.3, '#8a5a34', False, '#5a3a20'), quad(940, 750, 'ox', 1.3, '#f1e6d2', True, '#c9b99a'))


@scene('cabra', 'cabras e bodes', 'cabra* cabrito* bode* bodes cabras', 2.2)
def _(s):
    s.sky('#9fc4e0', '#e0eef5')
    s.add(cloud(300, 200, 1), peaks('#7d8a8f', 560, 300, 4, 5), '<rect y="560" width="1200" height="340" fill="#7b8a5a"/>', rocks(240, 680, 1.4), rocks(980, 710, 1.6),
          quad(480, 820, 'goat', 3.2, '#ece6da', False, '#cfc8b8'), quad(850, 760, 'goat', 2, '#5a4a3e', True, '#3a2e26'))


@scene('cervo', 'corça e cervo', 'cervo* corca* cerva* gazela* gazelas veado* antilope', 2.4)
def _(s):
    s.sky('#7aa68a', '#d6e6c8')
    s.add(s.glow(900, 200, 320, '#fff6cf', .8), ridge('#3f6b4a', 500, 40, 3), tree(140, 700, 460, 'pine', '#27503a'), tree(1060, 690, 430, 'pine', '#27503a'),
          ridge('#5da048', 720, 30, 4), grass(720, '#2f6b3a', 5, 120), quad(560, 820, 'deer', 3.1, '#a8703a', False, '#7a4e26'))


@scene('lobo', 'lobo', 'lobo* lobos lobinho chacal* raposa* raposas', 2.2)
def _(s):
    s.sky('#101830', '#2b3a63')
    s.add(stars(50, 4, 400), fullmoon(900, 220, 90), ridge('#1b2542', 620, 60, 5), ridge('#0c1224', 740, 40, 8), tree(180, 770, 340, 'pine', '#08101c'),
          quad(560, 840, 'wolf', 3.2, '#6e7480', False, '#4a505c'))


@scene('leao', 'leão', 'leao leoes leoa* lea', 2.4)
def _(s):
    s.sky('#f2a65a', '#fbd8a2', '#fdeccc')
    s.add(sun(900, 260, 100, '#fff3c4', .9), ridge('#d9ad6a', 640, 30, 2), '<rect y="690" width="1200" height="210" fill="#c99a52"/>', tree(220, 700, 300, 'cypress', '#6b7a3a'),
          quad(560, 840, 'lion', 3.2, '#d29a4a', False, '#a8742e'))


@scene('urso', 'urso', 'urso* ursa', 2.2)
def _(s):
    s.sky('#9cc3a0', '#d9ead3')
    s.add(ridge('#4a7a5a', 520, 50, 3), tree(120, 760, 520, 'pine', '#1f4a38'), tree(1080, 760, 560, 'pine', '#1f4a38'), ridge('#5a8a4a', 760, 30, 6), grass(760, '#2f6b3a', 4, 130),
          quad(580, 850, 'bear', 3.3, '#5a3a26', False, '#3a2416'))


@scene('passaros', 'aves do céu', 'passaro* passarinho* passaros ave aves andorinha* pardal* pardais voar voou voam asa* asas ninho* ninhos', 2)
def _(s):
    s.sky('#5aa0dc', '#cfe8f5', '#fdf2d4')
    s.add(sun(260, 200, 70, '#fff3c4', .9), cloud(800, 260, 1.4), flock(14, 3, 100, 1100, 100, 520, '#233045', .6, 1.8), ridge('#6aa65e', 780, 30, 2),
          tree(950, 800, 420, 'round', '#3f7f45'), '<ellipse cx="930" cy="480" rx="38" ry="14" fill="#7a5230"/>', bird(930, 462, .6, '#233045'))


@scene('aguia', 'águia', 'aguia* falcao gaviao abutre* voo-de-aguia', 2.4)
def _(s):
    s.sky('#3f8fd6', '#a9d4f0', '#f6e8c8')
    s.add(cloud(250, 650, 1.6, op=.9), cloud(1000, 700, 1.8, op=.9), peaks('#7d8a9f', 840, 200, 4, 7, '#fff', .8), eagle(600, 360, 2.2, '#3a2a1e'), sun(950, 160, 60, '#fff3c4', .9))


@scene('corvo', 'corvos', 'corvo* corvos', 2.4)
def _(s):
    s.sky('#3a3550', '#8a7a8c', '#d9b89a')
    s.add(ridge('#4a3f55', 650, 60, 3), '<path d="M0 560Q300 500 600 560T1200 530V900H0Z" fill="#2a2433"/>', tree(300, 800, 420, 'dead', '#141018'),
          raven(340, 480, 1.6), raven(250, 420, 1.1, flip=True), flock(6, 3, 600, 1100, 150, 400, '#15151c', .8, 1.4))


@scene('serpente', 'serpente', 'serpente* cobra* cobras vibora* serpentes dragao', 2.5)
def _(s):
    s.sky('#6b7a3a', '#c9cf8a')
    s.add(ridge('#3f5a30', 600, 40, 4), '<rect y="640" width="1200" height="260" fill="#4a5a2c"/>', grass(640, '#2f4a24', 3, 160), tree(150, 740, 420, 'fig', '#2f6b3a'),
          snake(680, 800, 2.4, '#4f7a3a'))


@scene('baleia', 'grande peixe', 'baleia* monstro-marinho ventre abismo profundezas abismos profundeza', 2.5)
def _(s):
    s.sky('#17304f', '#2a5a82', '#4a86a8')
    s.add('<rect y="300" width="1200" height="600" fill="#1d4d6e" opacity=".55"/>', waves(300, 3, '#9fd6ee', .45, 40, 8, 14), beams(700, 300, 300, '#cfe9f3', .12, 5),
          whale(560, 600, 2), fish(180, 750, .9, '#7fb0c9'), fish(1020, 450, .7, '#7fb0c9', True), '<rect y="840" width="1200" height="60" fill="#0f2740"/>')


@scene('abelha', 'abelhas e mel', 'abelha* mel favo* favos', 2.5)
def _(s):
    s.sky('#f6d57a', '#fbeab0')
    hexs = ''.join(f'<polygon transform="translate({x} {y})" points="0,-48 42,-24 42,24 0,48 -42,24 -42,-24" fill="{c}" stroke="#b8860b" stroke-width="6"/>'
                   for x, y, c in ((430, 420, '#f4b942'), (510, 468, '#f6c453'), (510, 372, '#f4b942'), (590, 420, '#f6c453'), (590, 516, '#f4b942'), (670, 468, '#f4b942'), (670, 372, '#f6c453'), (750, 420, '#f4b942'), (430, 516, '#f6c453'), (510, 564, '#f4b942')))
    s.add(s.glow(600, 450, 480, '#fff3c4', .8), hexs, bee(300, 300, 2), bee(880, 300, 1.5), bee(820, 650, 1.8), bee(240, 640, 1.2), jar(1050, 850, .9, '#d9962e'),
          ridge('#8fa84a', 820, 25, 3))


@scene('gafanhoto', 'gafanhotos', 'gafanhoto* praga* pragas locusta*', 2.5)
def _(s):
    s.sky('#8a7a4a', '#d9c27a', '#efe0a8')
    r = __import__('random').Random(5)
    wheat_field = ''.join(wheat(x, 860 + r.randint(-20, 30), r.randint(120, 200), '#a89a50', '#7a6a30') for x in range(20, 1200, 60))
    s.add(sun(700, 220, 90, '#fff3c4', .7), scatter(locust, 28, 4, 60, 1140, 120, 640, .8, 2.4), ridge('#6b5a30', 760, 30, 3), wheat_field)


@scene('ovelhaperdida', 'ovelha perdida', 'perdida perdido perdi extraviada extraviad* desgarrad* procura* achar achei encontr* resgat*', 2.2)
def _(s):
    s.sky('#2b3a63', '#7a6a8a', '#f2b27a')
    s.add(sun(700, 640, 90, '#ffe3a8', .9), ridge('#3a3558', 640, 70, 8), ridge('#26203a', 740, 40, 4), sheep(380, 800, 1.5), person(840, 830, 1.5, '#6b3f2a', staff=True, cloth='#2a1f1a'),
          star(180, 140, 14), star(1000, 120, 10), stars(30, 3, 300))


@scene('ras', 'rãs', 'ra ras sapo* sapos', 2)
def _(s):
    s.sky('#9cc7a0', '#d6e9c4')
    s.add(ridge('#4a7a4a', 560, 30, 3), '<rect y="600" width="1200" height="300" fill="#3a8a8a"/>', waves(650, 4, '#bfe6e0', .45, 55, 8, 14),
          ''.join(f'<ellipse cx="{x}" cy="{y}" rx="70" ry="22" fill="#4f9a45"/>' for x, y in ((240, 760), (620, 700), (940, 780))), frog(620, 700, 1.8), frog(240, 760, 1.3), frog(940, 780, 1.5))


@scene('gado', 'o gado e o rebanho', 'boi bois novilho novilhos bezerro bezerros vaca vacas touro touros gado cabrito cabritos bode bodes cabra cabras', 1.8, 4)
def _(s, t=0):
    s.sky('#6aa0e0', '#bfd8f0', '#fdf2d4')
    s.add(sun(180, 160, 70, '#fff3c4', .9), cloud(780, 180, 1.4), ridge('#a8c8a0', 560, 25, 3), ridge('#7aa65a', 650, 20, 4), '<rect y="700" width="1200" height="200" fill="#6aa04a"/>', grass(710, '#3f7a3a', 3, 140),
          quad(300, 760, 'ox', 1.2, '#7a5a3a'), quad(640, 790, 'ox', 1.4, '#a8845a', flip=True), quad(980, 770, 'ox', 1.1, '#5a3a26'), quad(470, 880, 'goat', 1.3, '#d9cdb0'), quad(850, 890, 'goat', 1.2, '#b8a888', flip=True),
          person(130, 880, 1.2, '#7a4a2e', staff=True), tree(1110, 700, 300, 'olive', '#7f9a5a', '#5a4a38'))
