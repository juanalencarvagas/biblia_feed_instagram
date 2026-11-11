"""Cenas de Objetos: artefatos, armas, construções, templos, vestes, alimentos e ferramentas."""
import math
from registry import scene, legacy
from svglib import *
from comuns import *

# ---- Legados de objetos e construções ----------------------------------------
legacy('tabuas', 'tábuas da Lei', 'moises mandamento* tabua* sinai lei alianca', 2.5)
legacy('tenda', 'tenda e patriarcas', 'tenda* tabernaculo acampamento abraao isaque jaco sara patriarca* peregrin*', 2)
legacy('trigo', 'trigo e colheita', 'trigo pao paes seara ceifa colheita semente* celeiro rute boaz', 2)
legacy('trono', 'trono e reino', 'rei reis reino* trono* coroa salomao ester saul farao cetro', 1.5)
legacy('cruz', 'cruz', 'cruz crucific* calvario ressurrei* ressuscit* sangue sepulcro pascoa', 2.5)
legacy('luz', 'luz e lâmpada', 'luz lampada* candeia candelabro resplandec* brilh* isaias', 1.6)
legacy('casa', 'casa e família', 'casa casas familia lar telhado maria marta debora porta mae filho filhos', 1)
legacy('cidade', 'cidade e muralhas', 'cidade* jerusalem siao nineve sodoma jerico roma', 1.5)


# ---- Incenso e Culto --------------------------------------------------------
@scene('incenso', 'incenso e fumaça', 'incenso fumaca perfume* aroma cheiro cheiroso turibulo', 2.2)
def _(s):
    s.sky('#1a1020', '#3a2540', '#5a3a58')
    sm = ''.join(f'<path d="M{600 + dx} 640C{560 + dx} 560 {660 + dx} 500 {600 + dx} 420C{540 + dx} 340 {660 + dx} 280 {610 + dx} 160" stroke="#e8dcd0" stroke-width="{w}" fill="none" stroke-linecap="round" opacity="{o}"/>'
                 for dx, w, o in ((0, 22, .35), (-40, 14, .25), (50, 12, .22)))
    s.add(s.glow(600, 640, 250, '#ffb25a', .5), sm, '<path d="M520 640Q600 720 680 640Z" fill="#b8860b"/><rect x="590" y="715" width="20" height="60" fill="#8a6508"/><ellipse cx="600" cy="790" rx="70" ry="14" fill="#8a6508"/>',
          '<path d="M0 810H1200V900H0Z" fill="#0f0a14"/>')


@scene('templo', 'templo', 'templo templos santuario santuarios santo santos santa santidade santificar santificado santifica sagrado consagrar consagrado consagracao casa-de-deus', 2.0)
def _(s):
    s.sky('#6a9ad8', '#c5dcf2', '#fdf2d4')
    s.add(cloud(220, 180, 1.3, op=.9), cloud(980, 240, 1.2, op=.9), sun(940, 140, 60, '#fff3c4', .9), ridge('#b5c89a', 700, 25, 4), columns(600, 780, 6, 120, 280, '#f1e8d2'),
          '<rect x="330" y="780" width="540" height="30" fill="#d9ceb4"/><rect x="300" y="810" width="600" height="30" fill="#c9bea4"/><rect x="270" y="840" width="660" height="60" fill="#b9ae94"/>')


@scene('sinagoga', 'sinagoga', 'sinagoga sinagogas escriba escribas fariseu fariseus doutor doutores rabi rabino ler leu leitura leram lido mestres-lei', 2.6, 4)
def _(s, t=0):
    room(s, ('#3a2a1e', '#7a5a3a'), 740, ('#8a6a44', '#4a3322'))
    s.add(beams(300, 80, 220, '#fff6cf', .16, 4, 760), columns(600, 760, 5, 230, 520, '#d8c9a8'), '<rect x="440" y="610" width="320" height="140" fill="#5a3b22"/><rect x="420" y="596" width="360" height="24" fill="#7a5230"/>',
          scroll(600, 560, 1.2), lamp(300, 740, 1.1), lamp(900, 740, 1.1), person(220, 840, 1.3, '#7a4a2e', pose='sit'), person(340, 850, 1.3, '#3b5a7a', pose='sit'),
          person(860, 850, 1.3, '#8a2f3c', pose='sit'), person(980, 840, 1.3, '#5a7a3b', pose='sit'), person(600, 740, 1.2, ROBE, pose='stand', cloth='#5a3b22', halo='#fff3c4'))


@scene('jerusalem_muros', 'muros e portas', 'muro muros muralha muralhas porta portas portao portoes entrada entrar entrou entrai abrir abriu abri aberta fechar fechou chave chaves bater bate batei', 2.0)
def _(s):
    s.sky('#f08a5d', '#f9d6a0', '#fdf0d4')
    s.add(sun(260, 240, 80, '#fff3c4', .9), ridge('#b5a87a', 640, 25, 3), wall(0, 330, 760, 160), wall(870, 1200, 760, 160), tower(340, 780, 130, 440), tower(860, 780, 130, 440),
          '<rect x="400" y="560" width="400" height="220" fill="#8a7560"/>', door(600, 780, 170, 250), '<rect y="780" width="1200" height="120" fill="#b5a47a"/>')


@scene('vila_nazare', 'vila na colina', 'nazare belem betania cafarnaum jerico emaus aldeia aldeias vila vilas povoado cidadezinha carpinteiro carpinteiros', 2.4, 4)
def _(s, t=0):
    s.sky('#f08a5d', '#f9d6a0', '#fdf0d4')
    s.add(sun(260, 250, 80, '#fff3c4', .9), ridge('#c9b58a', 520, 30, 3), '<path d="M0 900L0 560Q300 470 600 540Q900 610 1200 500L1200 900Z" fill="#b5a47a"/>')
    cols = ['#e8d4a8', '#dcc597', '#f0dcb4', '#d4b988']
    for i, (x, y, w, h) in enumerate(((150, 640, 190, 120), (390, 600, 160, 110), (610, 650, 210, 140), (850, 610, 170, 120), (1060, 660, 190, 130),
                                      (270, 780, 220, 140), (520, 800, 180, 120), (760, 790, 230, 150), (1010, 820, 200, 130))):
        s.add(house(x, y, w, h, cols[i % 4], '#a8845a'))
    s.add(tree(80, 800, 300, 'olive', '#7f9a5a', '#5a4a38'), tree(1130, 640, 240, 'olive', '#7f9a5a', '#5a4a38'), person(640, 880, 1.0, '#7a4a2e', staff=True))


# ---- Armas e Guerra ---------------------------------------------------------
@scene('guerra', 'guerra e batalha', 'guerra guerras batalha batalhas combate combater combatei exercito exercitos soldado soldados guerreiro guerreiros inimigo inimigos inimiga adversario adversarios armas arma espada espadas lanca lancas flecha flechas arco arcos escudos escudo cavalaria vencer vencedor venceu vitoria derrota derrotar lutar luta lutou conquistar', 2.4)
def _(s):
    s.sky('#3a1c1c', '#a04a36', '#e69a5a')
    s.add(sun(900, 330, 90, '#ffd9a0', .8), cloud(300, 260, 1.8, '#5a3030', .8), ridge('#4a2a24', 640, 50, 3), '<rect y="700" width="1200" height="200" fill="#2a1612"/>',
          sword(320, 760, 2.0, -18), sword(880, 760, 2.0, 18), shield(600, 600, 2.2), crowd(8, 3, 720, 740, 120, 1080, (.3, .4)))


@scene('escudo', 'proteção e escudo', 'protecao proteger protegeu protege guardar guarda guardou guardai defender defesa defensor socorro socorrer ajuda ajudar ajudador auxilio salvar salvou salva salvacao salvador libertar libertou liberta livramento livrar livrai resgate resgatar redimir redencao redentor', 2.2)
def _(s):
    s.sky('#27406b', '#4a78b0', '#cfe3f2')
    s.add(cloud(220, 200, 1.4, op=.8), cloud(980, 260, 1.6, op=.8), ridge('#3a5a7a', 700, 40, 5), '<rect y="780" width="1200" height="120" fill="#243a54"/>', s.glow(600, 400, 360, '#fff3c4', .6), shield(600, 440, 4.2, '#3a5a9a', '#e0b040'),
          '<path d="M460 440Q600 280 740 440" stroke="#fff3c4" stroke-width="6" fill="none" opacity=".6"/>')


@scene('armadura', 'elmo e armadura', 'elmo couraca armadura armaduras lanca lancas capacete', 1.8, 4)
def _(s, t=0):
    s.sky('#2a2a3a', '#6a5a6a', '#d9a06a')
    s.add(cloud(220, 180, 2.6, '#4a4a5a', .95), cloud(940, 150, 2.8, '#3a3a4a', .95), ridge('#5a5048', 680, 40, 3), '<rect y="780" width="1200" height="120" fill="#4a3a2a"/>', helmet(600, 460, 2.2), shield(320, 680, 1.4),
          shield(880, 680, 1.4, '#3b5a7a'), sword(480, 790, 1.1, -14), sword(720, 790, 1.1, 14), '<rect x="1060" y="300" width="9" height="480" fill="#6a4a2e"/><path d="M1055 300L1064 230L1073 300Z" fill="#cfd6dd"/>',
          '<rect x="130" y="300" width="9" height="480" fill="#6a4a2e"/><path d="M125 300L134 230L143 300Z" fill="#cfd6dd"/>')


@scene('carros_guerra', 'carros de guerra', 'carro carros carruagem carruagens cavaleiro cavaleiros', 2.0, 4)
def _(s, t=0):
    s.sky('#f08a5d', '#f9d6a0', '#fdf0d4')
    s.add(sun(950, 230, 80, '#fff3c4', .9), ridge('#b5a87a', 560, 25, 3), '<rect y="720" width="1200" height="180" fill="#c9a36b"/>', cloud(300, 790, 1.8, '#e8d9c0', .6), cloud(700, 830, 1.6, '#e8d9c0', .55),
          quad(280, 800, 'horse', .9, '#6a4a2e'), chariot(160, 760, 1.1), quad(660, 840, 'horse', 1.0, '#3a2a1e'), chariot(540, 800, 1.2), quad(1000, 780, 'horse', .8, '#8a6a4a'), banner(800, 880, 300, '#8a2f3c', 100))


@scene('coroa_espinhos', 'coroa de espinhos', 'espinhos-coroa flagelar flagelado zombar zombaram zombador escarnecer escarneceu escarnio humilhado traicao traiu trair traidor traidores denegar negou', 2.4)
def _(s):
    s.sky('#2a1f2a', '#5a3a4a', '#a0705a')
    s.add(s.glow(600, 400, 380, '#ffd9a0', .45), thorns(600, 380, 210, '#3a2a18', 36), thorns(600, 380, 170, '#4a3a22', 30), heart(600, 560, 1.5, '#9a1c2c', .85), '<rect y="800" width="1200" height="100" fill="#1a1018"/>')


# ---- Livros e Cartas --------------------------------------------------------
@scene('carta_escritura', 'cartas e Escrituras', 'carta cartas escrevo escrevi escreveu escrever escrevi-vos escrito escritos escritura escrituras evangelho evangelhos livro livros pergaminho pergaminhos tinta pena', 2.6, 4)
def _(s, t=0):
    room(s, ('#2a1a14', '#4a3020'), 640, ('#7a5230', '#3a2616'))
    s.add(s.glow(600, 480, 520, '#ffd9a0', .5), '<rect x="140" y="170" width="920" height="26" fill="#5a3b22"/><rect x="140" y="360" width="920" height="26" fill="#5a3b22"/>',
          ''.join(scroll(190 + i * 120, 140, .42, rod='#6a4524') + scroll(190 + i * 120, 330, .42, rod='#6a4524') for i in range(8)),
          '<rect x="100" y="620" width="1000" height="40" fill="#8a5a34"/><rect x="130" y="660" width="40" height="240" fill="#6a4524"/><rect x="1030" y="660" width="40" height="240" fill="#6a4524"/>',
          scroll(480, 590, 1.9), book(820, 612, 1.1), lamp(260, 612, 1.3), '<path d="M700 600L760 520" stroke="#efe4c8" stroke-width="7" stroke-linecap="round"/>')


# ---- Alimentos, Utensílios e Metais -----------------------------------------
@scene('fome', 'fome e alimento', 'fome faminto famintos comer comeu comei comida alimento alimentar alimentou banquete mesa ceia refeicao festim jantar almoco mantimento mantimentos saciar saciou sacia saciados', 2.2)
def _(s):
    s.sky('#3a2412', '#7a4a22', '#d99a4a')
    s.add(s.glow(600, 520, 420, '#ffe3a8', .7), '<rect y="560" width="1200" height="340" fill="#6b4226"/>', '<rect y="560" width="1200" height="30" fill="#8a5a34"/>',
          bread(420, 640, 1.6), bread(760, 650, 1.5), chalice(600, 640, 1.5), fish(250, 660, 1.0), fish(950, 660, 1.0, '#e9c46a', True), grapes(180, 760, 1.0), grapes(1030, 760, 1.0))


@scene('sede', 'sede e água viva', 'sede sedento sedentos beber bebeu bebei bebida taca calice copo agua-viva fonte-de-agua', 2.3)
def _(s):
    s.sky('#f3b66b', '#fbe0ac', '#fdf2d4')
    s.add(sun(950, 200, 80, '#fff3c4', .9), ridge('#d9ad6a', 640, 30, 2), '<rect y="680" width="1200" height="220" fill="#c99a52"/>', chalice(380, 760, 2.2), jar(780, 780, 2.2),
          '<path d="M780 600C770 640 790 650 780 690" stroke="#6fc0e0" stroke-width="12" fill="none" stroke-linecap="round"/><ellipse cx="780" cy="730" rx="70" ry="14" fill="#6fc0e0" opacity=".7"/>')


@scene('alimentos', 'leite, mel e frutos', 'leite mel farinha azeite oleo fruto frutos figo figos romas tamaras comida alimento alimentos cevada lentilhas', 1.6, 4)
def _(s, t=0):
    s.sky('#2a1a14', '#5a3a24', '#d9a06a')
    s.add(s.glow(600, 450, 520, '#ffd9a0', .55), '<rect y="640" width="1200" height="260" fill="#6a4a30"/><rect x="100" y="620" width="1000" height="36" fill="#8a5a34"/>', jar(260, 620, 1.1, '#e8dcc0'), jar(420, 620, 1.0, '#d9a830'),
          jar(780, 620, 1.1, '#c98a3f'), bread(600, 600, 1.0), grapes(940, 620, 1.2), ''.join(f'<circle cx="{510 + i * 40}" cy="{540 - (i % 2) * 20}" r="22" fill="{["#7b4b94", "#d62839", "#e0a030"][i % 3]}"/>' for i in range(6)),
          wheat(150, 880, 160), wheat(1050, 880, 170), lamp(600, 890, 1.0))


@scene('riqueza', 'riquezas e ouro', 'riqueza riquezas rico ricos ouro prata tesouro tesouros dinheiro moeda moedas mamom ganancia avareza avarento comprar vender vendeu comprou preco', 2.2)
def _(s):
    s.sky('#2a1d10', '#5a3a1a', '#a0702a')
    s.add(s.glow(600, 640, 480, '#ffd166', .6), '<rect y="700" width="1200" height="200" fill="#3a2810"/>', ''.join(coin(x, y, r) for x, y, r in ((330, 780, 60), (460, 820, 52), (600, 760, 70), (760, 810, 56), (880, 770, 62), (540, 700, 50), (690, 690, 48), (400, 700, 40))),
          crown(600, 560, 2.2), jar(150, 860, 1.4, '#c98a3a'), jar(1050, 860, 1.4, '#c98a3a'))


@scene('metais', 'ouro, prata e bronze', 'ouro prata bronze ferro cobre metal metais estanho chumbo ourives fundir fundiu', 1.8, 4)
def _(s, t=0):
    s.sky('#2a1a14', '#5a3a24', '#d9a06a')
    s.add(s.glow(600, 500, 560, '#ffd9a0', .6), '<rect y="740" width="1200" height="160" fill="#3a2616"/>')
    for i in range(5):
        s.add(f'<path d="M{300 + i * 12} {840 - i * 34}L{660 - i * 12} {840 - i * 34}L{640 - i * 14} {806 - i * 34}L{320 + i * 14} {806 - i * 34}Z" fill="{["#ffd166", "#f0c040", "#e0b040", "#d9a830", "#c9972c"][i]}"/>')
    s.add(chalice(800, 840, 1.0), jar(940, 840, .9, '#c9a040'), jar(220, 840, .9, '#b5733a'), ''.join(coin(120 + i * 40, 860 - (i % 2) * 18, 24, ['#ffd166', '#cfd6dd', '#c9763a'][i % 3]) for i in range(4)),
          crown(530, 600, 1.0), shield(330, 640, .9, '#b5733a', '#ffd166'), sword(930, 700, .8, 20, '#cfd6dd', '#c9a040'))


@scene('pedras', 'pedras e monumento', 'pedra pedras pedreira marco marcos monumento pilar pilares apedrejar apedrejado', 1.8, 4)
def _(s, t=0):
    s.sky('#6aa0e0', '#bfd8f0', '#fdf2d4')
    s.add(sun(960, 170, 70, '#fff3c4', .9), cloud(230, 190, 1.4), ridge('#a8c8a0', 590, 25, 3), '<rect y="700" width="1200" height="200" fill="#8aa660"/>', grass(710, '#4f8a3f', 2, 120))
    for i in range(12):
        a = math.radians(200 + i * 140 / 11)
        s.add(standing_stone(600 + 420 * math.cos(a), 820 + 70 * math.sin(a) + 40, 74, 150 + (i % 3) * 14))
    s.add(altar(600, 800, 1.3), person(600, 880, 1.2, ROBE, pose='pray', cloth='#5a3b22'))


@scene('madeira', 'madeira e carpintaria', 'madeira madeiro lenha carpinteiro machado machados serra serrar cedros acacia tabua tabuas', 1.8, 4)
def _(s, t=0):
    s.sky('#8ec5e8', '#d6ecf5', '#fdf2d4')
    s.add(sun(180, 160, 70, '#fff3c4', .9), ridge('#6a8a5a', 580, 30, 3), tree(130, 800, 560, 'cedar', '#2f5a3a'), tree(1080, 800, 520, 'cedar', '#2f5a3a'), '<rect y="760" width="1200" height="140" fill="#7a5a38"/>',
          logs(300, 850, 4, 1.1), logs(900, 850, 3, 1.1), '<rect x="440" y="800" width="360" height="26" fill="#a8703a"/><rect x="440" y="826" width="360" height="12" fill="#6a4524"/>',
          person(620, 800, 1.5, '#7a4a2e', pose='point', cloth='#3a2a20'), axe(560, 810, 1.3, -20))


@scene('roupas', 'roupas e tecidos', 'roupa roupas veste vestes vestido vestidos vestir vestiu manto mantos tunica linho tecido tecidos tear cinto', 1.8, 4)
def _(s, t=0):
    s.sky('#f4b183', '#fce6c4', '#fff4e0')
    s.add(sun(960, 190, 70, '#fff3c4', .9), ridge('#c9b58a', 580, 25, 3), '<rect y="740" width="1200" height="160" fill="#d9b97a"/>', house(160, 740, 260, 200, '#e8d4a8'), house(1060, 740, 240, 180, '#dcc597'),
          robe_line(260, 940, 420, ['#8a2f3c', '#3b5a7a', '#f4efe2', '#b88a3f', '#6b4a8a', '#5a7a3b']), person(600, 880, 1.2, '#7a4a2e', pose='stand', cloth='#3a2a20'))


@scene('sete_candelabro', 'o candelabro de sete braços', 'sete candelabro lampadas numero contados contou', 1.8, 4)
def _(s, t=0):
    s.sky('#1c130d', '#3a2616', '#6a4a2e')
    s.add(s.glow(600, 400, 560, '#ffd9a0', .7), '<rect x="240" y="120" width="720" height="700" fill="#14100c" opacity=".55"/>', columns(600, 820, 3, 360, 640, '#8a6a44'), '<rect y="820" width="1200" height="80" fill="#4a3322"/>',
          menorah(600, 800, 2.3), beams(600, 100, 260, '#fff6cf', .12, 5, 820))


@scene('tributo_dizimo', 'dízimos e tributos', 'dizimo dizimos tributo tributos imposto impostos primicia primicias', 1.8, 4)
def _(s, t=0):
    s.sky('#2a1a14', '#5a3a24', '#d9a06a')
    s.add(s.glow(600, 460, 520, '#ffd9a0', .5), '<rect y="760" width="1200" height="140" fill="#4a3322"/>', basket(250, 860, 1.5), basket(450, 880, 1.3), wheat(650, 880, 140), wheat(690, 880, 140), jar(850, 860, 1.0), jar(960, 870, .9, '#c9a040'),
          sheaf(1070, 880, 130), '<path d="M530 860Q560 760 600 760Q640 760 670 860Z" fill="#8a6420"/><circle cx="600" cy="800" r="12" fill="#ffd166"/>', coin(430, 730, 34), coin(560, 700, 30), coin(690, 730, 34), altar(800, 760, 1.0))


@scene('idolos_bezerro', 'ídolos e o bezerro de ouro', 'idolo idolos deuses imagem imagens esculpida esculpidas bezerro adorar adoraram adorou', 2.8, 4)
def _(s, t=0):
    s.sky('#2a0a08', '#8a2a10', '#ff9f1c')
    s.add(peaks('#6a3a2a', 640, 300, 3, 5), '<rect y="740" width="1200" height="160" fill="#5a3a24"/>', ''.join(flame(120 + i * 240, 770, .9) for i in range(5)), idol_calf(600, 780, 1.5),
          crowd(26, 4, 790, 890, 40, 1160, (.4, .55)), person(300, 880, 1.2, '#8a2f3c', pose='up', cloth='#14100c'), person(900, 880, 1.2, '#3b5a7a', pose='up', cloth='#14100c'),
          '<path d="M1090 340L1140 420L1090 500" stroke="#f4efe2" stroke-width="10" fill="none"/>')
