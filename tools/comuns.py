"""Desenhos auxiliares compartilhados pelos módulos de cenas."""
from svglib import *

ROBE = '#f4efe2'
COLORS = ['#7a4a2e', '#3b5a7a', '#8a2f3c', '#5a7a3b', '#b88a3f', '#6b4a8a', '#c9b79a', '#2f6b6b']


def pyramid(x, y, w, h, c='#d9b97a', c2='#b8955a'):
    return (f'<path d="M{n(x - w / 2)} {n(y)}L{n(x)} {n(y - h)}L{n(x + w / 2)} {n(y)}Z" fill="{c}"/>'
            f'<path d="M{n(x)} {n(y - h)}L{n(x + w / 2)} {n(y)}L{n(x + w * .12)} {n(y)}Z" fill="{c2}"/>')


def banner(x, y, h=220, c='#8a2f3c', w=90, flip=False):
    d = -1 if flip else 1
    return (f'<rect x="{n(x - 3)}" y="{n(y - h)}" width="6" height="{n(h)}" fill="#5a3b22"/>'
            f'<path d="M{n(x + 3 * d)} {n(y - h)}L{n(x + (3 + w) * d)} {n(y - h + 10)}L{n(x + (3 + w * .8) * d)} {n(y - h + 40)}'
            f'L{n(x + (3 + w) * d)} {n(y - h + 70)}L{n(x + 3 * d)} {n(y - h + 60)}Z" fill="{c}"/>'
            f'<circle cx="{n(x)}" cy="{n(y - h)}" r="7" fill="#e0b040"/>')


def hand(x, y, s=1, c='#e0b48a', rot=0, flip=False):
    sx = -s if flip else s
    fingers = ''.join(f'<rect x="{fx}" y="{-fh}" width="18" height="{fh + 16}" rx="9" fill="{c}"/>'
                      for fx, fh in ((-42, 62), (-21, 80), (0, 86), (21, 68)))
    return (f'<g transform="translate({n(x)} {n(y)}) rotate({n(rot)}) scale({n(sx)} {n(s)})">{fingers}'
            f'<rect x="-46" y="-6" width="90" height="92" rx="26" fill="{c}"/>'
            f'<rect x="-68" y="20" width="20" height="58" rx="10" fill="{c}" transform="rotate(-35 -58 48)"/>'
            '<path d="M-30 30Q0 50 30 30" stroke="#b88a66" stroke-width="4" fill="none" opacity=".6"/></g>')


def eye(x, y, s=1, iris='#5a3b22'):
    return (f'<g transform="translate({n(x)} {n(y)}) scale({n(s)})"><path d="M-110 0Q0 -88 110 0Q0 88 -110 0Z" fill="#fbf6ea" stroke="#3a2a1e" stroke-width="7"/>'
            f'<circle r="46" fill="{iris}"/><circle r="22" fill="#14100c"/><circle cx="-14" cy="-14" r="9" fill="#fff"/></g>')


def footprints(x, y, k=6, dx=40, dy=-60, c='#6a4a2e', op=.7):
    out = ''
    for i in range(k):
        side = -16 if i % 2 == 0 else 16
        sc = 1 - i * .06
        out += (f'<g transform="translate({n(x + i * dx + side)} {n(y + i * dy)}) scale({n(sc)})" fill="{c}" opacity="{op}">'
                '<ellipse cx="0" cy="12" rx="12" ry="20"/><ellipse cx="0" cy="-16" rx="10" ry="9"/></g>')
    return out


def brick_tower(x, y, w=420, h=560, tiers=6, c1='#c9a36b', c2='#b58a52'):
    out = ''
    th = h / tiers
    for i in range(tiers):
        tw = w * (1 - i * .13)
        out += f'<rect x="{n(x - tw / 2)}" y="{n(y - (i + 1) * th)}" width="{n(tw)}" height="{n(th + 2)}" fill="{c1 if i % 2 == 0 else c2}"/>'
        for j in range(3):
            out += f'<rect x="{n(x - tw / 2 + tw * (.2 + j * .3))}" y="{n(y - (i + .7) * th)}" width="{n(tw * .09)}" height="{n(th * .38)}" rx="6" fill="#3a2a1a"/>'
    out += f'<path d="M{n(x - w / 2)} {n(y)}L{n(x + w * .3)} {n(y - h)}" stroke="#7a5a32" stroke-width="10" opacity=".5"/>'
    return out


def sound_waves(x, y, r0=60, k=4, c='#ffffff', op=.6, a0=-40, a1=40, step=46, w=8):
    out = ''
    for i in range(k):
        r = r0 + i * step
        p0 = (x + r * math.cos(math.radians(a0)), y + r * math.sin(math.radians(a0)))
        p1 = (x + r * math.cos(math.radians(a1)), y + r * math.sin(math.radians(a1)))
        out += (f'<path d="M{n(p0[0])} {n(p0[1])}A{n(r)} {n(r)} 0 0 1 {n(p1[0])} {n(p1[1])}" fill="none" stroke="{c}" stroke-width="{w}" '
                f'stroke-linecap="round" opacity="{n(op * (1 - i * .18))}"/>')
    return out


def basket(x, y, s=1):
    loaves = ''.join(f'<ellipse cx="{dx}" cy="-54" rx="16" ry="9" fill="#c98a3f"/>' for dx in (-20, 0, 20))
    return (f'<g transform="translate({n(x)} {n(y)}) scale({n(s)})"><path d="M-50 0L50 0L38 -50L-38 -50Z" fill="#b8892f"/>'
            f'<ellipse cx="0" cy="-50" rx="40" ry="10" fill="#8a6420"/>{loaves}<path d="M-40 -20L40 -20" stroke="#8a6420" stroke-width="4"/></g>')


def stone_heap(x, y, s=1, c='#7a746a', c2='#9a948a'):
    return (rocks(x - 70 * s, y, 1.0 * s, c, c2) + rocks(x + 60 * s, y, 1.1 * s, c, c2) + rocks(x - 5 * s, y - 40 * s, .9 * s, c, c2))


def chariot(x, y, s=1, body='#c9a36b'):
    return (f'<g transform="translate({n(x)} {n(y)}) scale({n(s)})"><path d="M-80 -60L70 -60L90 -20L-60 -20Z" fill="{body}"/>'
            '<path d="M-80 -60L-100 -110M70 -60L110 -100" stroke="#8a6a3a" stroke-width="9"/>'
            '<circle cx="-10" cy="0" r="44" fill="none" stroke="#5a3b22" stroke-width="10"/><circle cx="-10" cy="0" r="8" fill="#5a3b22"/>'
            '<path d="M-10 -44L-10 44M-54 0L34 0M-41 -31L21 31M-41 31L21 -31" stroke="#5a3b22" stroke-width="4"/></g>')


def sling(x, y, s=1, rot=0):
    return (f'<g transform="translate({n(x)} {n(y)}) rotate({n(rot)}) scale({n(s)})"><path d="M0 0Q-70 -30 -90 -90M0 0Q40 -50 60 -110" stroke="#8a6a3a" stroke-width="6" fill="none"/>'
            '<circle cx="0" cy="0" r="14" fill="#7a746a"/></g>')


def hill_town(x, y, s=1, wall='#d9c49a', roof='#b8946a'):
    out = f'<g transform="translate({n(x)} {n(y)}) scale({n(s)})">'
    for dx, w, h in ((-110, 110, 90), (0, 130, 130), (110, 100, 100)):
        out += f'<rect x="{dx - w / 2}" y="{-h}" width="{w}" height="{h}" fill="{wall}"/><rect x="{dx - w / 2 - 5}" y="{-h - 10}" width="{w + 10}" height="12" fill="{roof}"/>'
    out += '<rect x="-14" y="-60" width="28" height="60" rx="14" fill="#4a3a28"/></g>'
    return out


def sheaf(x, y, h=130, lean=0):
    return ''.join(wheat(x + (i - 2) * 9 + lean * i, y, h + (i % 2) * 14) for i in range(5)) + f'<path d="M{n(x - 24)} {n(y - h * .35)}L{n(x + 28)} {n(y - h * .35)}" stroke="#8a6420" stroke-width="7"/>'


def menorah(x, y, s=1, c='#e0b040'):
    g = f'<g transform="translate({n(x)} {n(y)}) scale({n(s)})" fill="none" stroke="{c}" stroke-width="12" stroke-linecap="round"><path d="M-70 0L70 0M0 0L0 -270"/>'
    for k in (1, 2, 3):
        w = k * 60
        g += f'<path d="M0 {-30 - k * 22}Q{-w} {-30 - k * 22} {-w} {-110 - k * 22}L{-w} -270M0 {-30 - k * 22}Q{w} {-30 - k * 22} {w} {-110 - k * 22}L{w} -270"/>'
    g += '</g>'
    return g + ''.join(flame(x + k * 60 * s, y - 272 * s, .42 * s) for k in range(-3, 4))


def axe(x, y, s=1, rot=0):
    return (f'<g transform="translate({n(x)} {n(y)}) rotate({n(rot)}) scale({n(s)})"><rect x="-6" y="-150" width="12" height="190" rx="5" fill="#8a5a34"/>'
            '<path d="M6 -150L60 -170L60 -100L6 -112Z" fill="#cfd6dd"/><path d="M6 -150L-6 -150L-6 -112L6 -112Z" fill="#7d8790"/></g>')


def logs(x, y, k=3, s=1, c='#8a5a34'):
    out = ''
    for i in range(k):
        for j in range(k - i):
            cx, cy = x + (j - (k - i - 1) / 2) * 70 * s, y - i * 60 * s
            out += (f'<circle cx="{n(cx)}" cy="{n(cy)}" r="{n(36 * s)}" fill="{c}"/><circle cx="{n(cx)}" cy="{n(cy)}" r="{n(24 * s)}" fill="#c9a36b"/>'
                    f'<circle cx="{n(cx)}" cy="{n(cy)}" r="{n(10 * s)}" fill="{c}"/>')
    return out


def robe_line(x0, x1, y, cols):
    out = f'<path d="M{n(x0)} {n(y)}Q{n((x0 + x1) / 2)} {n(y + 40)} {n(x1)} {n(y)}" stroke="#5a3b22" stroke-width="6" fill="none"/>'
    k = len(cols)
    for i, c in enumerate(cols):
        px = x0 + (i + .5) * (x1 - x0) / k
        py = y + 30 - abs(i - k / 2) * 3
        out += f'<path d="M{n(px - 40)} {n(py)}L{n(px + 40)} {n(py)}L{n(px + 52)} {n(py + 180)}L{n(px - 52)} {n(py + 180)}Z" fill="{c}"/><path d="M{n(px - 40)} {n(py)}L{n(px - 76)} {n(py + 70)}L{n(px - 46)} {n(py + 84)}Z" fill="{c}"/><path d="M{n(px + 40)} {n(py)}L{n(px + 76)} {n(py + 70)}L{n(px + 46)} {n(py + 84)}Z" fill="{c}"/>'
    return out


def idol_calf(x, y, s=1):
    return (f'<rect x="{n(x - 150 * s)}" y="{n(y - 20 * s)}" width="{n(300 * s)}" height="{n(30 * s)}" fill="#8a7a58"/>'
            + quad(x, y - 20 * s, 'ox', 1.3 * s, '#e0b040', dark='#c9972c')
            + s_glow(x, y - 130 * s, 260 * s))


def s_glow(x, y, r, col='#ffe08a', op=.55):
    return (f'<circle cx="{n(x)}" cy="{n(y)}" r="{n(r)}" fill="{col}" opacity="{n(op * .35)}"/>'
            f'<circle cx="{n(x)}" cy="{n(y)}" r="{n(r * .6)}" fill="{col}" opacity="{n(op * .3)}"/>')


def helmet(x, y, s=1, c='#9aa3ab'):
    return (f'<g transform="translate({n(x)} {n(y)}) scale({n(s)})"><path d="M-60 0Q-62 -80 0 -92Q62 -80 60 0L40 0L40 -26L-40 -26L-40 0Z" fill="{c}"/>'
            '<path d="M0 -92L0 -150" stroke="#8a1f2c" stroke-width="14"/><path d="M-12 -150Q0 -190 12 -150Z" fill="#8a1f2c"/>'
            '<rect x="-46" y="-30" width="92" height="10" fill="#6e7780"/></g>')


def bone(x, y, ln=120, rot=0, c='#efe6d0'):
    h = ln / 2
    return (f'<g transform="translate({n(x)} {n(y)}) rotate({n(rot)})"><rect x="{n(-h)}" y="-7" width="{n(ln)}" height="14" rx="7" fill="{c}"/>'
            f'<circle cx="{n(-h)}" cy="-8" r="11" fill="{c}"/><circle cx="{n(-h)}" cy="8" r="11" fill="{c}"/><circle cx="{n(h)}" cy="-8" r="11" fill="{c}"/><circle cx="{n(h)}" cy="8" r="11" fill="{c}"/></g>')


def skull(x, y, s=1, c='#efe6d0'):
    return (f'<g transform="translate({n(x)} {n(y)}) scale({n(s)})"><circle cx="0" cy="-30" r="40" fill="{c}"/><rect x="-24" y="-8" width="48" height="34" rx="10" fill="{c}"/>'
            '<circle cx="-15" cy="-30" r="10" fill="#2a2018"/><circle cx="15" cy="-30" r="10" fill="#2a2018"/><path d="M-5 -12L5 -12L0 -2Z" fill="#2a2018"/></g>')


def standing_stone(x, y, w=70, h=170, c='#8a847a', c2='#a39d92'):
    return (f'<path d="M{n(x - w / 2)} {n(y)}L{n(x - w * .42)} {n(y - h * .85)}Q{n(x)} {n(y - h * 1.1)} {n(x + w * .42)} {n(y - h * .85)}L{n(x + w / 2)} {n(y)}Z" fill="{c}"/>'
            f'<path d="M{n(x + w * .1)} {n(y)}L{n(x + w * .15)} {n(y - h * .95)}Q{n(x + w * .3)} {n(y - h * .92)} {n(x + w * .42)} {n(y - h * .85)}L{n(x + w / 2)} {n(y)}Z" fill="{c2}" opacity=".55"/>')


def notes(x, y, k=5, c='#fff3c4'):
    out = ''
    for i in range(k):
        nx, ny = x + i * 46, y - (i % 3) * 22
        out += (f'<ellipse cx="{n(nx)}" cy="{n(ny)}" rx="11" ry="8" fill="{c}" transform="rotate(-20 {n(nx)} {n(ny)})"/>'
                f'<path d="M{n(nx + 9)} {n(ny)}L{n(nx + 9)} {n(ny - 44)}L{n(nx + 26)} {n(ny - 34)}" stroke="{c}" stroke-width="4" fill="none"/>')
    return out


def lying(x, y, s=1, robe='#7a4a2e', skin='#e0b48a'):
    return (f'<g transform="translate({n(x)} {n(y)}) scale({n(s)})"><ellipse cx="0" cy="-16" rx="86" ry="22" fill="{robe}"/>'
            f'<circle cx="-92" cy="-26" r="19" fill="{skin}"/><path d="M-112 -30Q-92 -58 -72 -30Z" fill="#3a2a20"/></g>')


def palm_leaf(x, y, s=1, c='#4a8a3a'):
    return (f'<g transform="translate({n(x)} {n(y)}) scale({n(s)})"><path d="M0 0Q-30 -50 -10 -90M0 0Q10 -55 36 -86M0 0Q-2 -60 14 -110" stroke="{c}" stroke-width="7" fill="none" stroke-linecap="round"/></g>')


def room(s, wall=('#3a2a1e', '#6a4a2e'), floor_y=760, floor=('#7a5a3a', '#4a3322')):
    s.sky(*wall)
    s.fillrect(floor_y, *floor)
