"""Cenas da Natureza: céu, clima, relevo, águas e botânica."""
from registry import scene, legacy
from svglib import *
from comuns import *

# ---- Legados de natureza ----------------------------------------------------
legacy('ceu', 'céu e nuvens', 'ceu* nuvem* nuve* firmamento aurora', 1)
legacy('chuva', 'orvalho e chuva', 'orvalho chuva* chov* gota* chuveiro', 1.4)
legacy('deserto', 'deserto', 'deserto* areia sequidao ermo', 1.4)
legacy('floresta', 'floresta e árvores', 'arvore* florest* bosque folha* ramo* ramos', 1)
legacy('fogo', 'fogo', 'fogo* chama* brasa* brasas incendi*', 1.4)
legacy('jardim', 'jardim e flores', 'jardim jardins flor flores roseira eden', 1.4)
legacy('mar', 'mar e ondas', 'mar mares onda* tempestade navio navios', 1.4)
legacy('montanhas', 'montanhas', 'monte montes montanha* serra', 1.2)
legacy('noite', 'noite e estrelas', 'noite* escuridao trevas', 1.2)
legacy('rio', 'rio e água', 'rio rios ribeiro* agua* corrente*', 1)


# ---- Céu e Clima ------------------------------------------------------------
@scene('amanhecer', 'amanhecer', 'amanhecer alvorada madrugada manha amanhece* alva', 2)
def _(s):
    s.sky('#3a4a7c', '#e58a6a', '#fbd48a')
    s.add(s.glow(600, 600, 460, '#ffe6a0', .9), sun(600, 590, 92, '#fff3c4', .95),
          ridge('#6b4a6e', 600, 40, 3, .9), ridge('#3f3558', 690, 40, 5), flock(6, 4, 150, 1050, 150, 320, '#4a3550'),
          ridge('#26203a', 790, 30, 8))


@scene('entardecer', 'entardecer', 'entardecer poente ocaso crepusculo', 2)
def _(s):
    s.sky('#3e2b63', '#d9544f', '#f9a65a')
    s.add(s.glow(820, 560, 420, '#ffd08a', .9), sun(820, 560, 85, '#ffe3a8', .95), ridge('#6b3a5e', 600, 60, 11, .9),
          ridge('#3a2347', 680, 50, 12), tree(220, 760, 330, 'cypress', '#1e1530'), tree(300, 770, 240, 'cypress', '#1e1530'),
          ridge('#1e1530', 800, 30, 14), flock(5, 6, 200, 700, 160, 330, '#3a2347'))


@scene('sol', 'sol', 'sol solar calor meiodia', 1.2)
def _(s):
    s.sky('#3f95d6', '#a9d8f2', '#e8f6fb')
    s.add(sun(600, 230, 110, '#fff2a8', .98), rays(600, 230, 150, 250, 20, '#fff2a8', .4, 12),
          ridge('#5fa05a', 640, 50, 4), ridge('#3f7f45', 720, 40, 5), grass(740, '#2f6b3a', 2, 140), cloud(220, 200, .8), cloud(980, 330, .6))


@scene('lua', 'lua', 'lua luar', 1.4)
def _(s):
    s.sky('#080d26', '#1f2c5e', '#3a4580')
    s.add(stars(70, 5, 520), moon(820, 230, 110), ridge('#141a3a', 700, 70, 9), ridge('#0b0f26', 800, 40, 3), tree(260, 800, 300, 'pine', '#080b1c'))


@scene('estrelas', 'estrelas', 'estrela* estrelado', 2)
def _(s):
    s.sky('#050a1f', '#14235a', '#3a3f80')
    s.add(stars(140, 8, 640), s.glow(600, 280, 190, '#fff1b8', .8), star(600, 280, 78, '#fff3c4', 8, .38), rays(600, 280, 100, 200, 8, '#fff3c4', .6, 6),
          ridge('#0c1233', 760, 50, 4))


@scene('nuvens', 'nuvens', 'nuvem nuvens', 2)
def _(s):
    s.sky('#4f9be0', '#9fd0f2', '#e6f4fb')
    s.add(cloud(280, 260, 1.5), cloud(820, 200, 1.9, op=.95), cloud(560, 480, 2.2, op=.9), cloud(1020, 560, 1.2), cloud(140, 640, 1.1, op=.8),
          beams(700, 80, 600, '#ffffff', .12))


@scene('tempestade', 'tempestade', 'tempestade* raio raios trovao trovoes relampago* tormenta temporal', 2.5)
def _(s):
    s.sky('#161d2b', '#39465c', '#59677d')
    s.add(cloud(220, 180, 2.2, '#2b3446', .95), cloud(700, 140, 2.6, '#222a3a', .95), cloud(1020, 230, 1.8, '#303a4e', .95), lightning(640, 230, 1.5),
          rain(120, 3), waves(700, 4, '#8aa4bb', .5, 60, 12, 36), '<rect y="810" width="1200" height="90" fill="#0f1620" opacity=".8"/>')


@scene('vento', 'vento', 'vento* sopro folego respiro soprar assopr*', 2)
def _(s):
    s.sky('#7fb8de', '#cfe8f4', '#f1f8fb')
    sw = ''.join(f'<path d="M{x} {y}C{x + 120} {y - 60} {x + 240} {y + 60} {x + 360} {y - 20}C{x + 420} {y - 60} {x + 470} {y - 10} {x + 440} {y + 20}" fill="none" stroke="#fff" stroke-width="{w}" stroke-linecap="round" opacity=".8"/>'
                 for x, y, w in ((60, 240, 9), (300, 360, 12), (80, 470, 8), (520, 190, 8)))
    s.add(sw, ridge('#6aa65e', 740, 30, 3), tree(300, 800, 260, 'round', '#3f7f45'), tree(900, 790, 220, 'round', '#3f7f45'), bird(760, 300, 1.2, '#fff'))


@scene('arcoiris', 'arco-íris', 'arco-iris arcoiris', 3)
def _(s):
    s.sky('#6aa4d8', '#b7dbef', '#e8f4f8')
    s.add(rainbow(600, 700, 470, 26), ridge('#5da05a', 700, 40, 7), ridge('#3f7f45', 790, 40, 3), cloud(160, 600, 1.2, op=.9), cloud(1040, 620, 1.2, op=.9))


@scene('neve', 'neve e gelo', 'neve gelo geada frio frios granizo nevar branco', 2)
def _(s):
    s.sky('#8da4c4', '#c9d9e9', '#eef4fa')
    s.add(peaks('#9fb4cc', 560, 340, 4, 4, '#ffffff', .9), peaks('#7f98b8', 640, 250, 5, 9, '#ffffff'),
          tree(180, 810, 260, 'pine', '#27465a'), tree(1010, 830, 300, 'pine', '#27465a'), tree(110, 850, 190, 'pine', '#2e5568'), snowfall(100, 4))


# ---- Relevo e Paisagem ------------------------------------------------------
@scene('vale', 'vale', 'vale vales sombra-da-morte', 2.5)
def _(s):
    s.sky('#f0b56e', '#f7dca4', '#fdf2d4')
    s.add(s.glow(600, 430, 360, '#fff6cf', .9),
          '<path d="M0 220L0 900L560 900L420 620Q260 420 0 220Z" fill="#3f4a3a"/>', '<path d="M1200 180L1200 900L640 900L780 620Q940 400 1200 180Z" fill="#2f3b33"/>',
          '<path d="M520 900L590 640L610 640L700 900Z" fill="#c9a36b"/>', ridge('#59704a', 650, 25, 3, .8, bottom=900), tree(180, 640, 220, 'cypress', '#1f2b24'),
          beams(600, 300, 380, '#fff6cf', .18))


@scene('colina', 'colina', 'colina* outeiro* outeiros', 2)
def _(s):
    s.sky('#6fb2e3', '#c5e4f5')
    s.add(cloud(300, 220, 1), cloud(900, 170, 1.2), ridge('#7fb86a', 600, 90, 2, 1, 260), ridge('#5da05a', 700, 80, 3, 1, 260), ridge('#3f7f45', 810, 50, 8),
          tree(620, 560, 260, 'round', '#2f6b3a'), grass(700, '#2f6b3a', 4, 100))


@scene('campo', 'campo e pasto', 'campo campos pasto pastos prado erva relva verdejante planicie planice', 1.4)
def _(s):
    s.sky('#74b5e6', '#d1ebf7')
    s.add(cloud(250, 200, 1), ridge('#8cc36f', 520, 25, 6), ridge('#74b35a', 620, 25, 4), ridge('#5da048', 730, 20, 2), grass(640, '#2f6b3a', 8, 220, 30),
          ''.join(flower(x, y, 55, c) for x, y, c in ((160, 800, '#f4a8c0'), (330, 780, '#ffffff'), (520, 830, '#f4d35e'), (760, 790, '#f4a8c0'), (940, 835, '#ffffff'), (1090, 790, '#f4d35e'))))


@scene('ilha', 'ilha', 'ilha ilhas costa litoral', 2)
def _(s):
    s.sky('#58a8e0', '#bfe3f4')
    s.add(sun(960, 190, 70, '#fff3c4', .9), s.glow(0, 0, 0, '#fff'), '<rect y="520" width="1200" height="380" fill="#1c6ea4"/>', waves(580, 4, '#9fd6ee', .5, 80, 10, 20),
          '<path d="M340 600Q460 500 600 520Q760 500 860 600Q600 640 340 600Z" fill="#e5cf95"/>', '<path d="M400 590Q520 520 640 535Q760 530 820 590Z" fill="#5da048"/>',
          tree(560, 580, 260, 'palm', '#2f7a3a'), tree(690, 590, 200, 'palm', '#2f7a3a'))


@scene('praia', 'praia', 'praia* margem margens orla porto conchas', 2)
def _(s):
    s.sky('#f6b36c', '#fbd9a0', '#fdeccc')
    s.add(sun(300, 300, 85, '#fff1b8', .95), '<rect y="440" width="1200" height="200" fill="#2a7da8"/>', waves(500, 3, '#bfe6f2', .6, 50, 10, 18),
          '<path d="M0 640Q300 600 600 640T1200 620V900H0Z" fill="#ead29a"/>', '<path d="M0 640Q300 600 600 640T1200 620" fill="none" stroke="#fff" stroke-width="12" opacity=".7"/>',
          boat(900, 520, .5), '<ellipse cx="300" cy="780" rx="38" ry="24" fill="#f3d6c4"/><ellipse cx="760" cy="820" rx="30" ry="20" fill="#e8b79c"/>')


@scene('caverna', 'caverna', 'caverna* gruta* cova covas esconderijo esconder* rocha-fendida', 2)
def _(s):
    s.sky('#0b0a10', '#241c2c')
    s.add(s.glow(600, 520, 420, '#ffd89a', .85),
          '<path d="M0 0H1200V900H0Z M600 220C380 220 270 420 250 640L220 900H980L950 640C930 420 820 220 600 220Z" fill="#2a2430" fill-rule="evenodd"/>',
          '<path d="M0 900L0 0H1200V900H980L950 640C930 420 820 220 600 220C380 220 270 420 250 640L220 900Z" fill="#17131c"/>',
          ''.join(f'<path d="M{x} 230L{x + 26} 230L{x + 13} {y}Z" fill="#3b3140"/>' for x, y in ((330, 330), (420, 300), (520, 280), (610, 300), (700, 285), (790, 310), (880, 340))),
          rocks(430, 820, 1.2, '#2f2733', '#463a4e'), rocks(780, 830, 1.5, '#2f2733', '#463a4e'), flame(600, 790, 1.1))


@scene('oasis', 'oásis', 'oasis tamareira* palmeira* palmeiras sombra-fresca', 2)
def _(s):
    s.sky('#f2a65a', '#fbd8a2', '#fdeccc')
    s.add(sun(260, 260, 80, '#fff3c4', .9), ridge('#e3b872', 600, 40, 2), '<ellipse cx="620" cy="760" rx="300" ry="50" fill="#3a9fc2"/><ellipse cx="620" cy="755" rx="240" ry="30" fill="#7fd0e6" opacity=".7"/>',
          ridge('#c99a52', 800, 25, 5, .9), tree(470, 760, 420, 'palm', '#2f7a3a'), tree(760, 750, 360, 'palm', '#2f7a3a'), tree(900, 780, 260, 'palm', '#3f8a3a'))


@scene('terra', 'terra e barro', 'terra terras chao po barro argila solo terreno', 1.2)
def _(s):
    s.sky('#cfa97a', '#e9d3ac')
    s.add(ridge('#8a5a34', 560, 25, 3), '<rect y="580" width="1200" height="320" fill="#6e4426"/>', '<path d="M0 700Q300 670 600 705T1200 690V900H0Z" fill="#573519"/>',
          '<path d="M0 800Q300 775 600 805T1200 790V900H0Z" fill="#40260f"/>', rocks(240, 620, .9, '#7a6a5a', '#9a8a78'), rocks(960, 640, .7, '#7a6a5a', '#9a8a78'),
          '<path d="M600 580Q604 520 590 480M600 520Q640 500 660 470M598 540Q560 515 545 485" stroke="#5da048" stroke-width="9" fill="none" stroke-linecap="round"/>',
          '<ellipse cx="600" cy="560" rx="22" ry="8" fill="#7a4a28"/>')


@scene('cachoeira', 'cachoeira', 'cachoeira* torrente* torrentes catarata* aguas-grandes enchente enxurrada', 2.2)
def _(s):
    s.sky('#9fd0e8', '#d9eef6')
    s.add(peaks('#5c7a5e', 480, 220, 4, 3),
          '<path d="M0 250L420 250L400 900L0 900Z" fill="#4b5f4f"/><path d="M800 250L1200 250L1200 900L800 900Z" fill="#4b5f4f"/>',
          '<path d="M420 250L800 250L860 900L370 900Z" fill="#eaf6fb"/>', ''.join(f'<path d="M{x} 270L{x + 8} 880" stroke="#9fcfe3" stroke-width="10" opacity=".5"/>' for x in range(470, 780, 52)),
          '<ellipse cx="615" cy="880" rx="330" ry="46" fill="#cfe9f3" opacity=".9"/>', tree(120, 400, 260, 'round', '#2f6b3a'), tree(1080, 380, 280, 'round', '#2f6b3a'))


@scene('poco', 'poço e cisterna', 'poco pocos cisterna* fonte-viva', 2.2)
def _(s):
    s.sky('#f3b66b', '#fbe0ac')
    s.add(sun(940, 230, 70, '#fff3c4', .9), ridge('#d9ad6a', 620, 35, 1), '<rect y="650" width="1200" height="250" fill="#c99a52"/>', well(600, 760, 1.9), tree(180, 700, 260, 'palm', '#2f7a3a'), person(900, 800, .8, '#8a2f3c'))


@scene('lago', 'lago', 'lago lagos lagoa tanque tanques reflexo', 2)
def _(s):
    s.sky('#f2b27a', '#f9dcae', '#fdf0d4')
    s.add(sun(600, 330, 80, '#fff3c4', .9), peaks('#6e6a8a', 500, 230, 5, 6), '<rect y="500" width="1200" height="400" fill="#4a8fb0"/>',
          '<g transform="translate(0 1000) scale(1 -1)" opacity=".28">' + peaks('#6e6a8a', 500, 230, 5, 6) + '</g>', waves(620, 5, '#cfe9f3', .35, 55, 6, 10),
          ''.join(f'<path d="M{x} 520L{x + 6} 440M{x + 12} 520L{x + 14} 430" stroke="#4b6a3a" stroke-width="5"/>' for x in (80, 140, 1020, 1090)))


@scene('terremoto', 'terremoto', 'terremoto* tremor tremer tremeu abalo abalou sacudi* tremeram', 2.5)
def _(s):
    s.sky('#6b5646', '#c49a6a', '#e8cfa0')
    s.add(peaks('#5a4638', 520, 240, 4, 8), '<rect y="600" width="1200" height="300" fill="#4a3628"/>',
          '<path d="M520 600L560 680L520 760L580 840L560 900L650 900L640 830L690 760L630 690L670 620L620 600Z" fill="#150d08"/>',
          '<path d="M580 640L610 700L580 770L620 830" stroke="#ff8a3d" stroke-width="5" fill="none"/>', rocks(300, 700, 1.1), rocks(920, 740, 1.3), rocks(240, 540, .5), rocks(980, 480, .45),
          '<ellipse cx="600" cy="560" rx="500" ry="70" fill="#cfa97a" opacity=".35"/>', cloud(200, 200, 1.2, '#b89a7a', .6), cloud(960, 260, 1.4, '#b89a7a', .6))


@scene('rocha', 'rocha e fortaleza', 'rocha rochas rochedo* fortaleza* refugio* abrigo baluarte escudo-forte penhasco* firme', 2)
def _(s):
    s.sky('#6e8bb5', '#cbd9ea')
    s.add(cloud(250, 200, 1.2), cloud(980, 150, 1), '<path d="M300 900L340 520L440 360L560 300L700 330L830 450L880 900Z" fill="#6f6a64"/>',
          '<path d="M560 300L700 330L830 450L880 900L640 900L620 520Z" fill="#8b857c" opacity=".7"/><path d="M440 360L560 300L600 520L520 700L360 640Z" fill="#59544f" opacity=".6"/>',
          ridge('#4f7a4a', 840, 30, 6), grass(830, '#355e3a', 7, 100))


# ---- Botânica e Plantas -----------------------------------------------------
@scene('cedro', 'cedros do Líbano', 'cedro cedros libano', 3)
def _(s):
    s.sky('#8db6d8', '#dbe9f1')
    s.add(peaks('#7d93ab', 460, 240, 4, 2, '#ffffff', .9), ridge('#486f56', 620, 40, 3), tree(300, 800, 560, 'cedar', '#1f5a3a'), tree(640, 820, 650, 'cedar', '#1f5a3a'),
          tree(920, 800, 480, 'cedar', '#2a6b44'), tree(90, 790, 380, 'cedar', '#2a6b44'))


@scene('oliveira', 'oliveira e azeite', 'oliveira* oliva* azeite* azeitona* oleo oleos unc* ungi* unguento*', 2.2)
def _(s):
    s.sky('#f0c27b', '#f9e2b0', '#fdf2d4')
    s.add(sun(950, 210, 70, '#fff3c4', .9), ridge('#b8a76a', 600, 40, 5), ridge('#8f9a5a', 700, 30, 8), tree(300, 800, 430, 'olive', '#7f9a5a', '#5a4a38'), tree(720, 810, 520, 'olive', '#6f8a4f', '#5a4a38'),
          tree(1000, 790, 360, 'olive', '#7f9a5a', '#5a4a38'), jar(110, 880, 1))


@scene('figueira', 'figueira', 'figueira* figo figos', 3)
def _(s):
    s.sky('#8fc2e6', '#d9ecf6')
    s.add(cloud(220, 200, 1), ridge('#7fb06a', 700, 30, 3), tree(600, 800, 620, 'fig', '#3f8a45', '#5a4a38'), grass(780, '#2f6b3a', 4, 120))


@scene('videira', 'videira e uvas', 'videira* vinha* vinhas uva uvas vinho* vindima lagar', 2.2)
def _(s):
    s.sky('#f2c27f', '#faeacb')
    s.add(sun(180, 180, 70, '#fff3c4', .9), ridge('#a58a5a', 560, 30, 3), ridge('#7fa05a', 650, 30, 7),
          ''.join(f'<path d="M{x} 900L{x} 640M{x - 90} 650Q{x} 600 {x + 90} 650" stroke="#6b4a2a" stroke-width="9" fill="none"/>' for x in (200, 520, 840)),
          '<path d="M80 650C300 600 500 700 700 640S1000 600 1150 650" stroke="#3f7a3a" stroke-width="12" fill="none"/>',
          grapes(250, 760, 1.5), grapes(560, 770, 1.7), grapes(880, 760, 1.5), grapes(1070, 790, 1.1))


@scene('palmeira', 'palmeiras', 'palma palmas tamara', 1.2)
def _(s):
    s.sky('#5aa8e0', '#bfe3f4')
    s.add(sun(900, 180, 70, '#fff3c4', .9), ridge('#e5cf95', 760, 25, 2), tree(300, 800, 560, 'palm', '#2f7a3a'), tree(640, 820, 640, 'palm', '#3f8a3a'), tree(960, 800, 480, 'palm', '#2f7a3a'))


@scene('espinhos', 'espinhos', 'espinho espinhos cardo cardos abrolho abrolhos sarca sarcas urtiga', 2.5)
def _(s):
    s.sky('#b8a284', '#e0d0b0')
    t = ''
    import random as _r
    r = _r.Random(5)
    for i in range(14):
        x = 120 + i * 75
        t += f'<path d="M{x} 840Q{x + r.randint(-60, 60)} {640 - r.randint(0, 120)} {x + r.randint(-120, 120)} {480 + r.randint(0, 140)}" stroke="#4a3a22" stroke-width="8" fill="none"/>'
        for k in range(6):
            px, py = x + r.randint(-80, 80), 560 + r.randint(0, 260)
            t += f'<path d="M{px} {py}l{r.randint(-24, 24)} {r.randint(-26, -8)}" stroke="#4a3a22" stroke-width="4" stroke-linecap="round"/>'
    s.add(ridge('#8f7a58', 760, 20, 3), t, grass(840, '#6b7a3a', 2, 60), thorns(600, 330, 120))


@scene('semeador', 'semeador', 'semeador semear semeou semeia sementeira lavrador lavoura arar arado plantar plantou', 2.5)
def _(s):
    s.sky('#f3c58a', '#fbe6bf')
    s.add(sun(930, 220, 75, '#fff3c4', .9), ridge('#b88a52', 540, 25, 4),
          ''.join(f'<path d="M0 {y}Q600 {y - 40} 1200 {y}" stroke="#5a381c" stroke-width="{10 + i * 3}" fill="none" opacity=".8"/>' for i, y in enumerate((620, 690, 770, 860))),
          '<rect y="590" width="1200" height="310" fill="#7a4a28" opacity=".55"/>', person(430, 780, 1.5, '#8a5a34', cloth='#e8dcc0', pose='point'),
          ''.join(f'<circle cx="{560 + i * 38}" cy="{600 + (i % 3) * 20 + i * 8}" r="5" fill="#e9c46a"/>' for i in range(9)), flock(5, 9, 600, 1000, 140, 340, '#3a2a20'))


@scene('lirios', 'lírios do campo', 'lirio lirios', 3)
def _(s):
    s.sky('#9fd0ea', '#e5f3f8')
    s.add(cloud(300, 200, 1), ridge('#8ec26e', 560, 25, 2), ridge('#6aa955', 680, 25, 3),
          ''.join(lily(x, 880 - (x % 7) * 20, 150 + (x % 5) * 30) for x in range(100, 1150, 110)), grass(760, '#2f6b3a', 5, 80))


@scene('raiz', 'raiz e broto', 'raiz raizes broto brotar brotou renovo ramo-novo tronco semente-viva fundamento fundamentos', 2.2)
def _(s):
    s.sky('#b6dcef', '#e8f4f8')
    rt = ''.join(f'<path d="M600 640C{600 + a} 700 {600 + b} 760 {600 + c} 880" stroke="#8a5a34" stroke-width="{w}" fill="none" stroke-linecap="round"/>'
                 for a, b, c, w in ((-70, -170, -260, 12), (60, 160, 280, 12), (-10, -40, -80, 9), (20, 90, 140, 8), (-40, -100, -150, 6)))
    s.add(ridge('#7fb06a', 600, 10, 2), '<rect y="630" width="1200" height="270" fill="#5a381c"/>', rt,
          '<path d="M600 640Q604 500 590 380" stroke="#4a8a40" stroke-width="16" fill="none" stroke-linecap="round"/>', '<ellipse cx="540" cy="400" rx="60" ry="26" fill="#5da048" transform="rotate(-30 540 400)"/><ellipse cx="660" cy="340" rx="64" ry="28" fill="#6fbf58" transform="rotate(25 660 340)"/>')
