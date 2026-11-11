"""Primitivas de desenho para gerar as cenas SVG (canvas 1200x900).

Todas as funções devolvem strings SVG. Não há dependências externas.
"""
import math
import random
import re

W, H = 1200, 900


def n(v):
    """Formata número de forma compacta."""
    v = round(float(v), 1)
    return str(int(v)) if v == int(v) else str(v)


class Scene:
    """Acumula defs (gradientes) e elementos de uma cena."""

    def __init__(self, key):
        self.key = re.sub(r'[^a-z0-9]', '', key.lower())
        self.defs = []
        self.parts = []
        self._i = 0

    def _id(self):
        self._i += 1
        return f'{self.key}{self._i}'

    def grad(self, *stops, x2=0, y2=1):
        """Gradiente linear. stops: cores igualmente espaçadas ou (offset, cor)."""
        gid = self._id()
        k = len(stops)
        out = ''
        for i, st in enumerate(stops):
            off, col = st if isinstance(st, tuple) else (i / max(k - 1, 1), st)
            out += f'<stop offset="{n(off)}" stop-color="{col}"/>'
        self.defs.append(f'<linearGradient id="{gid}" x2="{x2}" y2="{y2}">{out}</linearGradient>')
        return f'url(#{gid})'

    def glow(self, x, y, r, col, op=.85):
        gid = self._id()
        self.defs.append(
            f'<radialGradient id="{gid}"><stop offset="0" stop-color="{col}" stop-opacity="{op}"/>'
            f'<stop offset="1" stop-color="{col}" stop-opacity="0"/></radialGradient>')
        return f'<circle cx="{n(x)}" cy="{n(y)}" r="{n(r)}" fill="url(#{gid})"/>'

    def sky(self, *cols):
        self.parts.append(f'<rect width="{W}" height="{H}" fill="{self.grad(*cols)}"/>')

    def add(self, *items):
        self.parts.extend(items)

    def fillrect(self, y, *cols, op=1):
        self.parts.append(
            f'<rect y="{n(y)}" width="{W}" height="{n(H - y)}" fill="{self.grad(*cols)}" opacity="{op}"/>')

    def render(self, mirror=False):
        body = ''.join(self.parts)
        if mirror:
            body = f'<g transform="translate({W} 0) scale(-1 1)">{body}</g>'
        return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">'
                f'<defs>{"".join(self.defs)}</defs>{body}</svg>')


# ---------------------------------------------------------------- céu e clima
def sun(x, y, r, c='#ffdf9e', op=.8, halo=True):
    s = ''
    if halo:
        s += f'<circle cx="{n(x)}" cy="{n(y)}" r="{n(r * 1.7)}" fill="{c}" opacity="{n(op * .22)}"/>'
    return s + f'<circle cx="{n(x)}" cy="{n(y)}" r="{n(r)}" fill="{c}" opacity="{op}"/>'


def rays(x, y, r0, r1, k=16, c='#fff1b8', op=.35, w=10, rot=0):
    d = ''
    for i in range(k):
        a = math.radians(rot + i * 360 / k)
        d += f'M{n(x + r0 * math.cos(a))} {n(y + r0 * math.sin(a))}L{n(x + r1 * math.cos(a))} {n(y + r1 * math.sin(a))}'
    return f'<path d="{d}" stroke="{c}" stroke-width="{w}" stroke-linecap="round" opacity="{op}" fill="none"/>'


def beams(x, y, spread=420, c='#fff6cf', op=.28, k=7, y1=H):
    """Feixes de luz descendo de (x,y) até y1."""
    out = ''
    for i in range(k):
        t = (i / (k - 1) - .5) * 2
        xe = x + t * spread
        out += f'<path d="M{n(x - 6)} {n(y)}L{n(x + 6)} {n(y)}L{n(xe + 40)} {n(y1)}L{n(xe - 40)} {n(y1)}Z" fill="{c}" opacity="{op}"/>'
    return out


def moon(x, y, r, c='#fff1c9', op=.95):
    return (f'<circle cx="{n(x)}" cy="{n(y)}" r="{n(r * 1.8)}" fill="{c}" opacity=".10"/>'
            f'<path d="M{n(x)} {n(y - r)}A{n(r)} {n(r)} 0 0 0 {n(x)} {n(y + r)}A{n(r * 1.45)} {n(r * 1.45)} 0 0 1 {n(x)} {n(y - r)}Z" fill="{c}" opacity="{op}"/>')


def fullmoon(x, y, r, c='#fff1c9'):
    return (f'<circle cx="{n(x)}" cy="{n(y)}" r="{n(r * 1.6)}" fill="{c}" opacity=".12"/>'
            f'<circle cx="{n(x)}" cy="{n(y)}" r="{n(r)}" fill="{c}" opacity=".95"/>'
            f'<circle cx="{n(x - r * .3)}" cy="{n(y - r * .2)}" r="{n(r * .18)}" fill="#e6d7a8" opacity=".6"/>'
            f'<circle cx="{n(x + r * .35)}" cy="{n(y + r * .3)}" r="{n(r * .25)}" fill="#e6d7a8" opacity=".5"/>')


def stars(k=40, seed=1, ymax=420, c='#fff4cd', rmax=4, op=.85):
    r = random.Random(seed)
    return ''.join(
        f'<circle cx="{r.randint(10, W - 10)}" cy="{r.randint(10, ymax)}" r="{r.choice([1.5, 2, 3, rmax])}" fill="{c}" opacity="{op}"/>'
        for _ in range(k))


def star(x, y, r, c='#ffe9a0', k=5, inner=.45, op=1):
    pts = []
    for i in range(k * 2):
        rr = r if i % 2 == 0 else r * inner
        a = -math.pi / 2 + i * math.pi / k
        pts.append(f'{n(x + rr * math.cos(a))},{n(y + rr * math.sin(a))}')
    return f'<polygon points="{" ".join(pts)}" fill="{c}" opacity="{op}"/>'


def cloud(x, y, s=1, c='#ffffff', op=.9):
    return (f'<g opacity="{op}" fill="{c}" transform="translate({n(x)} {n(y)}) scale({n(s)})">'
            '<ellipse cx="0" cy="0" rx="120" ry="34"/><circle cx="-50" cy="-26" r="42"/>'
            '<circle cx="10" cy="-44" r="54"/><circle cx="65" cy="-20" r="38"/></g>')


def lightning(x, y, s=1, c='#fff6a8'):
    return (f'<polygon transform="translate({n(x)} {n(y)}) scale({n(s)})" fill="{c}" '
            'points="0,0 -40,120 -5,115 -30,230 55,90 15,95 45,0"/>')


def rainbow(x, y, R, w=22, op=.75, cols=('#e63946', '#f4a261', '#f4d35e', '#6bbf6b', '#4ea8de', '#7b5ea7')):
    out = ''
    for i, c in enumerate(cols):
        r = R - i * w
        out += (f'<path d="M{n(x - r)} {n(y)}A{n(r)} {n(r)} 0 0 1 {n(x + r)} {n(y)}" fill="none" '
                f'stroke="{c}" stroke-width="{w + 1}" opacity="{op}"/>')
    return out


def rain(k=70, seed=2, c='#cfe6f3', op=.55, y0=0, y1=700):
    r = random.Random(seed)
    d = ''
    for _ in range(k):
        x, y = r.randint(0, W), r.randint(y0, y1)
        d += f'M{x} {y}l-14 38'
    return f'<path d="{d}" stroke="{c}" stroke-width="3" stroke-linecap="round" opacity="{op}"/>'


def snowfall(k=90, seed=3, c='#ffffff', op=.85):
    r = random.Random(seed)
    return ''.join(f'<circle cx="{r.randint(0, W)}" cy="{r.randint(0, H)}" r="{r.choice([2, 3, 4, 5])}" fill="{c}" opacity="{op}"/>'
                   for _ in range(k))


# ---------------------------------------------------------------------- terreno
def ridge(c, base, amp, seed, op=1, step=170, bottom=H):
    r = random.Random(seed)
    pts = [(x, base + r.uniform(-amp, amp)) for x in range(-step, W + 2 * step, step)]
    d = f'M{n(pts[0][0])} {bottom}L{n(pts[0][0])} {n(pts[0][1])}'
    for i in range(1, len(pts) - 1):
        mx, my = (pts[i][0] + pts[i + 1][0]) / 2, (pts[i][1] + pts[i + 1][1]) / 2
        d += f'Q{n(pts[i][0])} {n(pts[i][1])} {n(mx)} {n(my)}'
    d += f'L{n(pts[-1][0])} {n(pts[-1][1])}L{n(pts[-1][0])} {bottom}Z'
    return f'<path d="{d}" fill="{c}" opacity="{op}"/>'


def peaks(c, base, h, k, seed, snow=None, op=1, spread=None):
    r = random.Random(seed)
    out = ''
    xs = [(i + .5) * W / k + r.uniform(-60, 60) for i in range(k)]
    for x in xs:
        top = base - h * r.uniform(.55, 1)
        hw = (base - top) * r.uniform(.8, 1.25)
        out += f'<path d="M{n(x - hw)} {n(base + 4)}L{n(x)} {n(top)}L{n(x + hw)} {n(base + 4)}Z" fill="{c}" opacity="{op}"/>'
        if snow:
            sh = (base - top) * .28
            sw = sh * hw / (base - top)
            out += (f'<path d="M{n(x)} {n(top)}L{n(x - sw)} {n(top + sh)}L{n(x - sw * .45)} {n(top + sh * .72)}'
                    f'L{n(x)} {n(top + sh * 1.1)}L{n(x + sw * .45)} {n(top + sh * .72)}L{n(x + sw)} {n(top + sh)}Z" fill="{snow}"/>')
    out += f'<rect y="{n(base)}" width="{W}" height="{n(H - base)}" fill="{c}" opacity="{op}"/>'
    return out


def waves(y0, k=3, c='#a8d8e8', op=.5, gap=70, w=12, amp=30, seed=0):
    out = ''
    for i in range(k):
        y = y0 + i * gap
        ww = w + i * 5
        out += (f'<path d="M0 {n(y)}Q150 {n(y - amp)} 300 {n(y)}T600 {n(y)}T900 {n(y)}T1200 {n(y)}" '
                f'fill="none" stroke="{c}" stroke-width="{ww}" opacity="{op}"/>')
    return out


def grass(y, c='#3f7a3a', seed=1, k=120, h=26, x0=0, x1=W, op=1):
    r = random.Random(seed)
    d = ''
    for _ in range(k):
        x = r.uniform(x0, x1)
        yy = y + r.uniform(0, 140)
        hh = h * r.uniform(.6, 1.3)
        d += f'M{n(x)} {n(yy)}L{n(x + 3)} {n(yy - hh)}L{n(x + 7)} {n(yy)}Z'
    return f'<path d="{d}" fill="{c}" opacity="{op}"/>'


def rocks(x, y, s=1, c='#6f6a64', c2='#8b857c'):
    return (f'<g transform="translate({n(x)} {n(y)}) scale({n(s)})"><path d="M-70 0L-55 -45L-15 -70L30 -55L70 -10L80 0Z" fill="{c}"/>'
            f'<path d="M-15 -70L30 -55L70 -10L10 -20Z" fill="{c2}" opacity=".7"/></g>')


def flower(x, y, h=70, petal='#f4a8c0', center='#ffd166', stem='#3f7a3a'):
    out = f'<path d="M{n(x)} {n(y)}L{n(x)} {n(y - h)}" stroke="{stem}" stroke-width="5"/>'
    for i in range(6):
        a = math.radians(i * 60)
        out += f'<circle cx="{n(x + 13 * math.cos(a))}" cy="{n(y - h + 13 * math.sin(a))}" r="9" fill="{petal}"/>'
    return out + f'<circle cx="{n(x)}" cy="{n(y - h)}" r="8" fill="{center}"/>'


def lily(x, y, h=110, c='#fff6e4', stem='#3f7a3a'):
    return (f'<path d="M{n(x)} {n(y)}Q{n(x + 6)} {n(y - h / 2)} {n(x)} {n(y - h)}" stroke="{stem}" stroke-width="6" fill="none"/>'
            f'<path d="M{n(x - 24)} {n(y - h - 28)}Q{n(x - 6)} {n(y - h + 6)} {n(x)} {n(y - h)}Q{n(x + 6)} {n(y - h + 6)} {n(x + 24)} {n(y - h - 28)}'
            f'Q{n(x)} {n(y - h - 8)} {n(x - 24)} {n(y - h - 28)}Z" fill="{c}"/>'
            f'<path d="M{n(x)} {n(y - h)}L{n(x)} {n(y - h - 22)}" stroke="#f4b942" stroke-width="3"/>')


def wheat(x, y, h, c='#e9c46a', st='#b8923a'):
    g = f'<path d="M{n(x)} {n(y)}L{n(x + 4)} {n(y - h)}" stroke="{st}" stroke-width="5" fill="none"/>'
    for i in range(6):
        yy = y - h + i * 16
        g += (f'<ellipse cx="{n(x - 4)}" cy="{n(yy)}" rx="6" ry="13" fill="{c}" transform="rotate(-25 {n(x - 4)} {n(yy)})"/>'
              f'<ellipse cx="{n(x + 12)}" cy="{n(yy + 6)}" rx="6" ry="13" fill="{c}" transform="rotate(25 {n(x + 12)} {n(yy + 6)})"/>')
    return g + f'<ellipse cx="{n(x + 4)}" cy="{n(y - h - 14)}" rx="6" ry="15" fill="{c}"/>'


def tree(x, y, h, kind='round', c='#2f6b3a', trunk='#5a3b22', op=1):
    g = f'<g opacity="{op}">'
    tw = h * .07
    if kind == 'round':
        g += (f'<rect x="{n(x - tw / 2)}" y="{n(y - h * .5)}" width="{n(tw)}" height="{n(h * .5)}" fill="{trunk}"/>'
              f'<circle cx="{n(x)}" cy="{n(y - h * .68)}" r="{n(h * .3)}" fill="{c}"/>'
              f'<circle cx="{n(x - h * .2)}" cy="{n(y - h * .55)}" r="{n(h * .2)}" fill="{c}"/>'
              f'<circle cx="{n(x + h * .2)}" cy="{n(y - h * .55)}" r="{n(h * .22)}" fill="{c}"/>')
    elif kind == 'cypress':
        g += (f'<rect x="{n(x - tw / 2)}" y="{n(y - h * .15)}" width="{n(tw)}" height="{n(h * .15)}" fill="{trunk}"/>'
              f'<ellipse cx="{n(x)}" cy="{n(y - h * .55)}" rx="{n(h * .11)}" ry="{n(h * .45)}" fill="{c}"/>')
    elif kind == 'pine':
        g += f'<rect x="{n(x - tw / 2)}" y="{n(y - h * .2)}" width="{n(tw)}" height="{n(h * .2)}" fill="{trunk}"/>'
        for i in range(3):
            top = y - h + i * h * .22
            wd = h * (.16 + i * .08)
            g += f'<path d="M{n(x)} {n(top)}L{n(x - wd)} {n(top + h * .38)}L{n(x + wd)} {n(top + h * .38)}Z" fill="{c}"/>'
    elif kind == 'palm':
        g += f'<path d="M{n(x)} {n(y)}Q{n(x + h * .12)} {n(y - h * .5)} {n(x + h * .04)} {n(y - h * .9)}" stroke="{trunk}" stroke-width="{n(h * .06)}" fill="none" stroke-linecap="round"/>'
        tx, ty = x + h * .04, y - h * .9
        for a in (-160, -130, -100, -70, -40, -10, 20):
            ar = math.radians(a)
            ex, ey = tx + h * .42 * math.cos(ar), ty + h * .3 * math.sin(ar) + h * .12
            g += f'<path d="M{n(tx)} {n(ty)}Q{n((tx + ex) / 2)} {n(ty - h * .2)} {n(ex)} {n(ey)}" stroke="{c}" stroke-width="{n(h * .05)}" fill="none" stroke-linecap="round"/>'
        g += f'<circle cx="{n(tx)}" cy="{n(ty + 8)}" r="{n(h * .035)}" fill="#8a5a2a"/><circle cx="{n(tx + 12)}" cy="{n(ty + 14)}" r="{n(h * .03)}" fill="#8a5a2a"/>'
    elif kind == 'olive':
        g += (f'<path d="M{n(x - h * .05)} {n(y)}Q{n(x - h * .12)} {n(y - h * .3)} {n(x)} {n(y - h * .45)}Q{n(x + h * .1)} {n(y - h * .3)} {n(x + h * .06)} {n(y)}Z" fill="{trunk}"/>'
              f'<ellipse cx="{n(x - h * .18)}" cy="{n(y - h * .52)}" rx="{n(h * .22)}" ry="{n(h * .12)}" fill="{c}"/>'
              f'<ellipse cx="{n(x + h * .16)}" cy="{n(y - h * .58)}" rx="{n(h * .24)}" ry="{n(h * .13)}" fill="{c}"/>'
              f'<ellipse cx="{n(x)}" cy="{n(y - h * .68)}" rx="{n(h * .22)}" ry="{n(h * .12)}" fill="{c}"/>')
    elif kind == 'cedar':
        g += f'<rect x="{n(x - tw / 2)}" y="{n(y - h * .6)}" width="{n(tw)}" height="{n(h * .6)}" fill="{trunk}"/>'
        for i, (dx, dy, rx) in enumerate([(0, .78, .34), (-.1, .6, .3), (.12, .45, .28), (0, .92, .2)]):
            g += f'<ellipse cx="{n(x + dx * h)}" cy="{n(y - dy * h)}" rx="{n(rx * h)}" ry="{n(h * .07)}" fill="{c}"/>'
    elif kind == 'fig':
        g += (f'<rect x="{n(x - tw / 2)}" y="{n(y - h * .45)}" width="{n(tw * 1.3)}" height="{n(h * .45)}" fill="{trunk}"/>'
              f'<ellipse cx="{n(x)}" cy="{n(y - h * .62)}" rx="{n(h * .38)}" ry="{n(h * .26)}" fill="{c}"/>'
              f'<circle cx="{n(x - h * .15)}" cy="{n(y - h * .55)}" r="{n(h * .04)}" fill="#7b4b94"/>'
              f'<circle cx="{n(x + h * .12)}" cy="{n(y - h * .66)}" r="{n(h * .04)}" fill="#7b4b94"/>')
    elif kind == 'dead':
        g += f'<path d="M{n(x)} {n(y)}L{n(x)} {n(y - h * .6)}M{n(x)} {n(y - h * .3)}L{n(x - h * .25)} {n(y - h * .55)}M{n(x)} {n(y - h * .45)}L{n(x + h * .28)} {n(y - h * .75)}M{n(x)} {n(y - h * .6)}L{n(x - h * .12)} {n(y - h * .85)}M{n(x)} {n(y - h * .6)}L{n(x + h * .08)} {n(y - h * .9)}" stroke="{trunk}" stroke-width="{n(h * .035)}" stroke-linecap="round" fill="none"/>'
    return g + '</g>'


def grapes(x, y, s=1, c='#6a3d9a', leaf='#3f7a3a'):
    out = f'<g transform="translate({n(x)} {n(y)}) scale({n(s)})"><path d="M0 -50L0 -75" stroke="#5a3b22" stroke-width="5"/>'
    out += f'<path d="M0 -70Q40 -100 70 -60Q35 -55 0 -70Z" fill="{leaf}"/>'
    for row, cnt in enumerate([4, 3, 2, 1]):
        for i in range(cnt):
            out += f'<circle cx="{n((i - (cnt - 1) / 2) * 24)}" cy="{n(-45 + row * 22)}" r="12" fill="{c}"/>'
    return out + '</g>'


# ------------------------------------------------------------------ construções
def house(x, y, w=150, h=100, wall='#e0c9a0', roof='#b8946a', door='#5c3a21', lit=True):
    out = f'<rect x="{n(x - w / 2)}" y="{n(y - h)}" width="{n(w)}" height="{n(h)}" fill="{wall}"/>'
    out += f'<rect x="{n(x - w / 2 - 6)}" y="{n(y - h - 12)}" width="{n(w + 12)}" height="14" fill="{roof}"/>'
    out += f'<rect x="{n(x - 14)}" y="{n(y - h * .55)}" width="28" height="{n(h * .55)}" rx="12" fill="{door}"/>'
    if lit:
        out += f'<rect x="{n(x + w * .22)}" y="{n(y - h * .75)}" width="{n(w * .14)}" height="{n(w * .14)}" fill="#ffd166"/>'
    return out


def tent(x, y, w=240, h=190, c='#c9a36b'):
    return (f'<path d="M{n(x - w / 2)} {n(y)}L{n(x)} {n(y - h)}L{n(x + w / 2)} {n(y)}Z" fill="{c}"/>'
            f'<path d="M{n(x)} {n(y - h)}L{n(x - 22)} {n(y)}L{n(x + 22)} {n(y)}Z" fill="#1b130c"/>'
            f'<path d="M{n(x - w / 2)} {n(y)}L{n(x)} {n(y - h)}L{n(x)} {n(y)}Z" fill="#000" opacity=".12"/>')


def tower(x, y, w=110, h=300, c='#8a7560', top='#6e5a48'):
    out = f'<rect x="{n(x - w / 2)}" y="{n(y - h)}" width="{n(w)}" height="{n(h)}" fill="{c}"/>'
    for i in range(4):
        out += f'<rect x="{n(x - w / 2 + i * w / 3.4)}" y="{n(y - h - 22)}" width="{n(w / 5)}" height="24" fill="{top}"/>'
    out += f'<rect x="{n(x - 9)}" y="{n(y - h * .7)}" width="18" height="46" rx="9" fill="#1b130c"/>'
    out += f'<rect x="{n(x - 14)}" y="{n(y - 56)}" width="28" height="56" rx="14" fill="#2a1c12"/>'
    return out


def wall(x0, x1, y, h=90, c='#9b8468', top='#7e6a52'):
    out = f'<rect x="{n(x0)}" y="{n(y - h)}" width="{n(x1 - x0)}" height="{n(h)}" fill="{c}"/>'
    x = x0
    while x < x1:
        out += f'<rect x="{n(x)}" y="{n(y - h - 18)}" width="28" height="20" fill="{top}"/>'
        x += 56
    return out


def columns(x, y, k=5, gap=80, h=220, c='#e6dcc6'):
    out = ''
    for i in range(k):
        cx = x + (i - (k - 1) / 2) * gap
        out += (f'<rect x="{n(cx - 14)}" y="{n(y - h)}" width="28" height="{n(h)}" fill="{c}"/>'
                f'<rect x="{n(cx - 22)}" y="{n(y - h - 12)}" width="44" height="14" fill="{c}"/>'
                f'<rect x="{n(cx - 20)}" y="{n(y - 6)}" width="40" height="8" fill="{c}"/>')
    tw = (k - 1) * gap + 90
    out += f'<rect x="{n(x - tw / 2)}" y="{n(y - h - 36)}" width="{n(tw)}" height="26" fill="{c}"/>'
    out += f'<path d="M{n(x - tw / 2)} {n(y - h - 36)}L{n(x)} {n(y - h - 100)}L{n(x + tw / 2)} {n(y - h - 36)}Z" fill="{c}"/>'
    return out


def cross(x, y, h, c='#1a1020'):
    return (f'<rect x="{n(x - h * .04)}" y="{n(y)}" width="{n(h * .08)}" height="{n(h)}" fill="{c}"/>'
            f'<rect x="{n(x - h * .25)}" y="{n(y + h * .22)}" width="{n(h * .5)}" height="{n(h * .08)}" fill="{c}"/>')


def door(x, y, w=150, h=250, frame='#5a3b22', panel='#8a5a34', glow='#ffe7a0'):
    return (f'<rect x="{n(x - w / 2 - 14)}" y="{n(y - h - 14)}" width="{n(w + 28)}" height="{n(h + 14)}" rx="{n(w / 2 + 10)}" fill="{frame}"/>'
            f'<rect x="{n(x - w / 2)}" y="{n(y - h)}" width="{n(w)}" height="{n(h)}" rx="{n(w / 2)}" fill="{panel}"/>'
            f'<path d="M{n(x)} {n(y - h)}L{n(x)} {n(y)}" stroke="{frame}" stroke-width="5"/>'
            f'<circle cx="{n(x + 20)}" cy="{n(y - h * .45)}" r="7" fill="#e0b040"/>')


def well(x, y, s=1):
    return (f'<g transform="translate({n(x)} {n(y)}) scale({n(s)})"><ellipse cx="0" cy="-6" rx="80" ry="22" fill="#6e6258"/>'
            '<path d="M-80 -6L-80 -60Q0 -30 80 -60L80 -6Z" fill="#8c7f72"/><ellipse cx="0" cy="-60" rx="80" ry="22" fill="#2a2a30"/>'
            '<ellipse cx="0" cy="-58" rx="62" ry="15" fill="#2e5878"/>'
            '<rect x="-84" y="-190" width="10" height="140" fill="#5a3b22"/><rect x="74" y="-190" width="10" height="140" fill="#5a3b22"/>'
            '<rect x="-90" y="-196" width="180" height="12" fill="#5a3b22"/><path d="M0 -184L0 -90" stroke="#3a2a1a" stroke-width="4"/>'
            '<path d="M-14 -90L14 -90L10 -64L-10 -64Z" fill="#8a5a34"/></g>')


# ------------------------------------------------------------------- objetos
def flame(x, y, s=1, c1='#ff9f1c', c2='#ffe08a'):
    p = 'M0 0C-42 -4 -52 -52 -20 -92C-18 -66 -2 -62 6 -84C36 -56 44 -4 0 0Z'
    return (f'<g transform="translate({n(x)} {n(y)}) scale({n(s)})"><path d="{p}" fill="{c1}"/>'
            f'<g transform="translate(0 -4) scale(.55)"><path d="{p}" fill="{c2}"/></g></g>')


def heart(x, y, s=1, c='#e63946', op=1):
    return (f'<path transform="translate({n(x)} {n(y)}) scale({n(s)})" opacity="{op}" fill="{c}" '
            'd="M0 -20C-10 -45 -50 -40 -50 -10C-50 20 -10 40 0 55C10 40 50 20 50 -10C50 -40 10 -45 0 -20Z"/>')


def book(x, y, s=1, page='#f1e6c8', edge='#8a5a34', lines=True):
    out = (f'<g transform="translate({n(x)} {n(y)}) scale({n(s)})"><path d="M-95 12L0 24L95 12L95 -4L0 8L-95 -4Z" fill="{edge}"/>'
           f'<path d="M-90 -2L0 10L0 -86L-90 -98Z" fill="{page}"/><path d="M90 -2L0 10L0 -86L90 -98Z" fill="{page}" opacity=".9"/>')
    if lines:
        for i in range(6):
            yy = -80 + i * 13
            out += f'<path d="M-76 {yy - 6}L-14 {yy + 4}M14 {yy + 4}L76 {yy - 6}" stroke="#9c8a68" stroke-width="3"/>'
    return out + '</g>'


def scroll(x, y, s=1, page='#efe0b8', rod='#8a5a34'):
    return (f'<g transform="translate({n(x)} {n(y)}) scale({n(s)})"><rect x="-90" y="-50" width="180" height="100" fill="{page}"/>'
            f'<rect x="-100" y="-58" width="16" height="116" rx="8" fill="{rod}"/><rect x="84" y="-58" width="16" height="116" rx="8" fill="{rod}"/>'
            + ''.join(f'<path d="M-68 {-30 + i * 18}L68 {-30 + i * 18}" stroke="#a5906a" stroke-width="4"/>' for i in range(5))
            + '</g>')


def crown(x, y, s=1, c='#ffd166', gem='#e63946'):
    return (f'<g transform="translate({n(x)} {n(y)}) scale({n(s)})"><path d="M-70 0L-80 -70L-40 -35L0 -90L40 -35L80 -70L70 0Z" fill="{c}"/>'
            f'<rect x="-70" y="-2" width="140" height="18" fill="{c}"/><circle cx="0" cy="-60" r="9" fill="{gem}"/>'
            '<circle cx="-80" cy="-74" r="7" fill="#48cae4"/><circle cx="80" cy="-74" r="7" fill="#48cae4"/></g>')


def thorns(x, y, R=90, c='#4a3a22', k=26):
    out = f'<ellipse cx="{n(x)}" cy="{n(y)}" rx="{n(R)}" ry="{n(R * .32)}" fill="none" stroke="{c}" stroke-width="9"/>'
    for i in range(k):
        a = i * 2 * math.pi / k
        px, py = x + R * math.cos(a), y + R * .32 * math.sin(a)
        out += f'<path d="M{n(px)} {n(py)}L{n(px + 16 * math.cos(a + .6))} {n(py + 16 * math.sin(a + .6))}" stroke="{c}" stroke-width="4" stroke-linecap="round"/>'
    return out


def sword(x, y, s=1, rot=0, blade='#cfd6dd', hilt='#8a5a34'):
    return (f'<g transform="translate({n(x)} {n(y)}) rotate({n(rot)}) scale({n(s)})"><path d="M0 -190L12 -40L-12 -40Z" fill="{blade}"/>'
            f'<rect x="-40" y="-42" width="80" height="12" rx="5" fill="{hilt}"/><rect x="-6" y="-32" width="12" height="55" fill="{hilt}"/>'
            f'<circle cx="0" cy="26" r="9" fill="#e0b040"/></g>')


def shield(x, y, s=1, c='#8a1f2c', rim='#d9b24a'):
    return (f'<path transform="translate({n(x)} {n(y)}) scale({n(s)})" d="M-60 -70L60 -70L60 0Q60 70 0 100Q-60 70 -60 0Z" fill="{c}" stroke="{rim}" stroke-width="10"/>'
            f'<path transform="translate({n(x)} {n(y)}) scale({n(s)})" d="M0 -70L0 100M-60 -10L60 -10" stroke="{rim}" stroke-width="7"/>')


def lamp(x, y, s=1, body='#a8703a'):
    return (f'<g transform="translate({n(x)} {n(y)}) scale({n(s)})"><path d="M-55 0Q-60 -36 -20 -38L30 -38Q64 -38 80 -52Q76 -20 56 0Z" fill="{body}"/>'
            f'<ellipse cx="0" cy="-38" rx="34" ry="8" fill="#6e4524"/></g>' + flame(x + 82 * s, y - 50 * s, .5 * s))


def bread(x, y, s=1):
    out = f'<g transform="translate({n(x)} {n(y)}) scale({n(s)})"><ellipse cx="0" cy="0" rx="80" ry="34" fill="#c98a3f"/>'
    out += '<path d="M-40 -18L-28 18M-8 -26L4 26M24 -22L36 22" stroke="#9a6325" stroke-width="6" stroke-linecap="round"/>'
    return out + '</g>'


def chalice(x, y, s=1, c='#e0b040'):
    return (f'<g transform="translate({n(x)} {n(y)}) scale({n(s)})"><path d="M-60 -100L60 -100Q60 -40 0 -30Q-60 -40 -60 -100Z" fill="{c}"/>'
            f'<rect x="-8" y="-32" width="16" height="50" fill="{c}"/><ellipse cx="0" cy="22" rx="45" ry="11" fill="{c}"/>'
            '<ellipse cx="0" cy="-100" rx="60" ry="10" fill="#7a1c2e"/></g>')


def jar(x, y, s=1, c='#b5683a'):
    return (f'<path transform="translate({n(x)} {n(y)}) scale({n(s)})" d="M-24 -120L24 -120L28 -96Q70 -60 60 -10Q55 22 0 24Q-55 22 -60 -10Q-70 -60 -28 -96Z" fill="{c}"/>'
            f'<path transform="translate({n(x)} {n(y)}) scale({n(s)})" d="M-52 -50Q0 -36 52 -50" stroke="#7a3f1f" stroke-width="6" fill="none"/>')


def harp(x, y, s=1, c='#b07a3a'):
    out = f'<g transform="translate({n(x)} {n(y)}) scale({n(s)})"><path d="M-70 120Q-90 -60 20 -120Q60 -60 60 120" fill="none" stroke="{c}" stroke-width="12" stroke-linecap="round"/>'
    for i in range(7):
        t = i / 6
        out += f'<path d="M{n(-48 + t * 100)} {n(110 - t * 20)}L{n(-12 + t * 50)} {n(-90 + t * 70)}" stroke="#f2e4b6" stroke-width="3"/>'
    return out + '</g>'


def shofar(x, y, s=1, c='#c9a56a'):
    return (f'<path transform="translate({n(x)} {n(y)}) scale({n(s)})" d="M-140 40Q-60 70 20 20Q100 -30 120 -110L160 -120Q150 -20 60 50Q-40 110 -150 70Z" fill="{c}"/>'
            f'<ellipse transform="translate({n(x)} {n(y)}) scale({n(s)})" cx="140" cy="-116" rx="22" ry="12" fill="#6e4f26" />')


def altar(x, y, s=1):
    out = f'<g transform="translate({n(x)} {n(y)}) scale({n(s)})"><rect x="-120" y="-40" width="240" height="40" fill="#7d746a"/>'
    out += '<rect x="-100" y="-80" width="200" height="40" fill="#8f867b"/><rect x="-70" y="-115" width="140" height="35" fill="#6f665c"/>'
    out += '<path d="M-110 -40L110 -40M-90 -80L90 -80" stroke="#4e463e" stroke-width="3"/></g>'
    return out + flame(x - 28 * s, y - 112 * s, 1.2 * s) + flame(x + 22 * s, y - 112 * s, .9 * s)


def ladder(x, y, h=420, w=90, rot=14, c='#8a5a34'):
    out = f'<g transform="translate({n(x)} {n(y)}) rotate({n(rot)})">'
    out += f'<path d="M{n(-w / 2)} 0L{n(-w / 2)} {n(-h)}M{n(w / 2)} 0L{n(w / 2)} {n(-h)}" stroke="{c}" stroke-width="9"/>'
    for i in range(1, 10):
        out += f'<path d="M{n(-w / 2)} {n(-i * h / 10)}L{n(w / 2)} {n(-i * h / 10)}" stroke="{c}" stroke-width="7"/>'
    return out + '</g>'


def anchor(x, y, s=1, c='#d9e2ea'):
    return (f'<g transform="translate({n(x)} {n(y)}) scale({n(s)})" fill="none" stroke="{c}" stroke-width="12" stroke-linecap="round">'
            '<circle cx="0" cy="-110" r="18"/><path d="M0 -92L0 90M-40 -60L40 -60M-90 30Q-70 100 0 100Q70 100 90 30"/>'
            '<path d="M-90 30L-72 52M90 30L72 52"/></g>')


def scales(x, y, s=1, c='#e0b040'):
    return (f'<g transform="translate({n(x)} {n(y)}) scale({n(s)})" stroke="{c}" stroke-width="9" fill="none" stroke-linecap="round">'
            '<path d="M0 120L0 -100M-130 -80L130 -80M-60 120L60 120"/>'
            f'<path d="M-130 -80L-170 20M-130 -80L-90 20M130 -80L90 20M130 -80L170 20" stroke-width="4"/>'
            f'<path d="M-185 20Q-130 70 -75 20Z M75 20Q130 70 185 20Z" fill="{c}"/></g>')


def chain(x, y, k=6, c='#9aa3ab', gap=44, vertical=False, broken_at=None):
    out = ''
    for i in range(k):
        if broken_at is not None and i == broken_at:
            continue
        cx, cy = (x, y + i * gap) if vertical else (x + i * gap, y)
        rot = 0 if i % 2 == 0 else 90
        out += (f'<ellipse cx="{n(cx)}" cy="{n(cy)}" rx="{20 if i % 2 == 0 else 8}" ry="{10 if i % 2 == 0 else 14}" '
                f'fill="none" stroke="{c}" stroke-width="8" transform="rotate({90 if vertical else 0} {n(cx)} {n(cy)})"/>')
    return out


def coin(x, y, r=40, c='#ffd166'):
    return (f'<circle cx="{n(x)}" cy="{n(y)}" r="{n(r)}" fill="{c}"/><circle cx="{n(x)}" cy="{n(y)}" r="{n(r * .72)}" fill="none" stroke="#c9972c" stroke-width="{n(r * .1)}"/>'
            f'<path d="M{n(x)} {n(y - r * .4)}L{n(x)} {n(y + r * .4)}" stroke="#c9972c" stroke-width="{n(r * .12)}"/>')


def manger(x, y, s=1):
    return (f'<g transform="translate({n(x)} {n(y)}) scale({n(s)})"><path d="M-110 -60L110 -60L80 20L-80 20Z" fill="#7a5230"/>'
            '<path d="M-100 -62Q0 -100 100 -62Z" fill="#d9b86a"/><ellipse cx="0" cy="-70" rx="55" ry="22" fill="#f4efe2"/>'
            '<circle cx="-34" cy="-80" r="17" fill="#f2cfa5"/><path d="M-90 20L-110 70M90 20L110 70" stroke="#5a3b22" stroke-width="12"/></g>')


def boat(x, y, s=1, hull='#5c3a21', sail='#f4efe2'):
    return (f'<g transform="translate({n(x)} {n(y)}) scale({n(s)})"><path d="M-180 0L180 0L130 70L-130 70Z" fill="{hull}"/>'
            f'<rect x="-5" y="-210" width="10" height="210" fill="#3a2414"/><path d="M8 -200L150 -30L8 -30Z" fill="{sail}"/>'
            f'<path d="M-8 -180L-110 -30L-8 -30Z" fill="{sail}" opacity=".85"/></g>')


def tomb(x, y, s=1, rock='#7d7468'):
    return (f'<g transform="translate({n(x)} {n(y)}) scale({n(s)})"><path d="M-260 0Q-250 -230 0 -250Q250 -230 260 0Z" fill="{rock}"/>'
            '<path d="M-90 0L-90 -110Q0 -190 90 -110L90 0Z" fill="#14100c"/>'
            '<circle cx="-170" cy="-40" r="105" fill="#968b7c"/><circle cx="-170" cy="-40" r="80" fill="none" stroke="#7a7064" stroke-width="8"/></g>')


# ------------------------------------------------------------------- pessoas
def person(x, y, s=1, robe='#7a4a2e', skin='#e0b48a', pose='stand', staff=False, cloth='#3a2a20', halo=None,
           flip=False, arms=True):
    """Pessoa estilizada. (x,y) = pés; altura ~ 215*s. pose: stand|pray|up|kneel|sit|walk|point"""
    sx = -s if flip else s
    g = f'<g transform="translate({n(x)} {n(y)}) scale({n(sx)} {n(s)})">'
    if staff:
        g += '<path d="M52 -215L52 0" stroke="#6b4a2a" stroke-width="7" stroke-linecap="round"/><path d="M52 -215Q70 -222 66 -200" stroke="#6b4a2a" stroke-width="7" fill="none" stroke-linecap="round"/>'
    if pose in ('kneel', 'sit'):
        g += f'<path d="M-52 0Q-44 -108 0 -128Q44 -108 52 0Z" fill="{robe}"/>'
        hx, hy = (8, -150) if pose == 'kneel' else (0, -152)
        arm = ''
        if arms:
            arm = (f'<path d="M-10 -118L24 -132" stroke="{robe}" stroke-width="15" stroke-linecap="round"/>' if pose == 'kneel'
                   else f'<path d="M-18 -112L-30 -70M18 -112L30 -70" stroke="{robe}" stroke-width="14" stroke-linecap="round"/>')
        g += arm
    else:
        g += f'<path d="M-26 -158Q0 -174 26 -158L42 0L-42 0Z" fill="{robe}"/>'
        hx, hy = 0, -186
        if arms:
            if pose == 'pray':
                g += f'<path d="M-22 -150L-4 -122M22 -150L4 -122" stroke="{robe}" stroke-width="14" stroke-linecap="round"/><circle cx="0" cy="-124" r="8" fill="{skin}"/>'
            elif pose == 'up':
                g += f'<path d="M-24 -150L-66 -230M24 -150L66 -230" stroke="{robe}" stroke-width="14" stroke-linecap="round"/><circle cx="-68" cy="-234" r="8" fill="{skin}"/><circle cx="68" cy="-234" r="8" fill="{skin}"/>'
            elif pose == 'point':
                g += f'<path d="M-24 -150L-34 -90M24 -150L74 -208" stroke="{robe}" stroke-width="14" stroke-linecap="round"/><circle cx="77" cy="-212" r="8" fill="{skin}"/>'
            else:
                g += f'<path d="M-24 -150L-38 -84M24 -150L38 -84" stroke="{robe}" stroke-width="14" stroke-linecap="round"/><circle cx="-38" cy="-80" r="8" fill="{skin}"/><circle cx="38" cy="-80" r="8" fill="{skin}"/>'
    if halo:
        g += f'<circle cx="{hx}" cy="{hy - 4}" r="44" fill="{halo}" opacity=".35"/><circle cx="{hx}" cy="{hy - 4}" r="34" fill="none" stroke="{halo}" stroke-width="6"/>'
    g += (f'<path d="M{hx - 25} {hy + 2}Q{hx - 27} {hy - 30} {hx} {hy - 30}Q{hx + 27} {hy - 30} {hx + 25} {hy + 2}Q{hx + 28} {hy + 34} {hx + 20} {hy + 34}L{hx - 20} {hy + 34}Q{hx - 28} {hy + 34} {hx - 25} {hy + 2}Z" fill="{cloth}"/>'
          f'<circle cx="{hx + 2}" cy="{hy + 2}" r="17" fill="{skin}"/></g>')
    return g


def crowd(k, seed, y0, y1, x0=0, x1=W, scale=(.35, .6)):
    r = random.Random(seed)
    cols = ['#7a4a2e', '#3b5a7a', '#8a2f3c', '#5a7a3b', '#b88a3f', '#6b4a8a', '#c9b79a', '#2f6b6b']
    items = sorted([(r.uniform(y0, y1), r.uniform(x0, x1)) for _ in range(k)])
    return ''.join(person(x, y, r.uniform(*scale), robe=r.choice(cols), cloth=r.choice(['#3a2a20', '#2a2a2a', '#6b4a2a', '#e8dcc0']),
                          pose=r.choice(['stand', 'stand', 'up', 'pray'])) for y, x in items)


# ------------------------------------------------------------------- animais
def sheep(x, y, k=1, c='#f4efe2', flip=False):
    sx = -k if flip else k
    return (f'<g transform="translate({n(x)} {n(y)}) scale({n(sx)} {n(k)})"><rect x="-28" y="20" width="8" height="34" fill="#3a2f2a"/><rect x="18" y="20" width="8" height="34" fill="#3a2f2a"/>'
            f'<ellipse cx="0" cy="0" rx="48" ry="32" fill="{c}"/><circle cx="-26" cy="-14" r="20" fill="{c}"/><circle cx="20" cy="-18" r="20" fill="{c}"/>'
            f'<circle cx="-4" cy="-26" r="18" fill="{c}"/><ellipse cx="58" cy="-6" rx="17" ry="14" fill="#3a2f2a"/><ellipse cx="46" cy="-18" rx="7" ry="11" fill="#3a2f2a" transform="rotate(-30 46 -18)"/></g>')


# configuração dos quadrúpedes: rx, ry, leg, neck(dx,dy), head(len, r), ears, extras
_Q = {
    'horse': dict(rx=100, ry=42, leg=100, nw=30, nd=(62, -92), hl=64, hr=17, ear='point', tail='long', lw=11),
    'donkey': dict(rx=84, ry=40, leg=80, nw=30, nd=(50, -62), hl=60, hr=17, ear='long', tail='thin', lw=11),
    'camel': dict(rx=100, ry=42, leg=118, nw=22, nd=(70, -128), hl=48, hr=14, ear='tiny', tail='thin', hump=2, lw=10),
    'ox': dict(rx=100, ry=50, leg=70, nw=44, nd=(58, 4), hl=52, hr=26, ear='flat', tail='thin', horn=True, hump=1, lw=15),
    'goat': dict(rx=62, ry=28, leg=62, nw=18, nd=(38, -52), hl=36, hr=12, ear='flat', tail='tuft', horn='back', beard=True, lw=8),
    'deer': dict(rx=76, ry=30, leg=92, nw=16, nd=(48, -86), hl=44, hr=11, ear='point', tail='tuft', antler=True, lw=7),
    'wolf': dict(rx=70, ry=27, leg=62, nw=22, nd=(52, -22), hl=50, hr=12, ear='point', tail='long', lw=9),
    'lion': dict(rx=90, ry=38, leg=62, nw=34, nd=(56, -26), hl=44, hr=22, ear='flat', tail='lion', mane=48, lw=15),
    'bear': dict(rx=86, ry=52, leg=44, nw=44, nd=(56, -4), hl=40, hr=24, ear='round', tail='tuft', lw=22),
}


def quad(x, y, kind='horse', s=1, col='#5a3a26', flip=False, dark=None):
    p = _Q[kind]
    dark = dark or col
    rx, ry, leg = p['rx'], p['ry'], p['leg']
    cy = -(leg + ry * .6)
    lw = p['lw']
    sx = -s if flip else s
    g = f'<g transform="translate({n(x)} {n(y)}) scale({n(sx)} {n(s)})">'
    for lx, c in ((-.62, dark), (.5, dark), (-.45, col), (.66, col)):
        g += f'<rect x="{n(lx * rx - lw / 2)}" y="{n(cy)}" width="{lw}" height="{n(-cy)}" rx="{n(lw / 3)}" fill="{c}"/>'
    # cauda
    t = p['tail']
    tx, ty = -rx * .92, cy - ry * .2
    if t == 'long':
        g += f'<path d="M{n(tx)} {n(ty)}Q{n(tx - 46)} {n(ty + 20)} {n(tx - 34)} {n(ty + 100)}" stroke="{dark}" stroke-width="16" fill="none" stroke-linecap="round"/>'
    elif t == 'thin':
        g += f'<path d="M{n(tx)} {n(ty)}Q{n(tx - 20)} {n(ty + 30)} {n(tx - 14)} {n(ty + 80)}" stroke="{dark}" stroke-width="7" fill="none" stroke-linecap="round"/>'
    elif t == 'tuft':
        g += f'<ellipse cx="{n(tx - 6)}" cy="{n(ty + 4)}" rx="9" ry="14" fill="{dark}"/>'
    elif t == 'lion':
        g += f'<path d="M{n(tx)} {n(ty)}Q{n(tx - 50)} {n(ty - 10)} {n(tx - 56)} {n(ty + 60)}" stroke="{dark}" stroke-width="8" fill="none" stroke-linecap="round"/><ellipse cx="{n(tx - 56)}" cy="{n(ty + 66)}" rx="11" ry="18" fill="#6b3f1f"/>'
    g += f'<ellipse cx="0" cy="{n(cy)}" rx="{rx}" ry="{ry}" fill="{col}"/>'
    for i in range(p.get('hump', 0)):
        hx = (-.1 + i * .45) * rx if p.get('hump') == 2 else -.2 * rx
        g += f'<ellipse cx="{n(hx)}" cy="{n(cy - ry * .85)}" rx="{n(ry * .6)}" ry="{n(ry * .7)}" fill="{col}"/>'
    nx0, ny0 = rx * .62, cy - ry * .25
    nx1, ny1 = nx0 + p['nd'][0], ny0 + p['nd'][1]
    g += f'<path d="M{n(nx0)} {n(ny0)}L{n(nx1)} {n(ny1)}" stroke="{col}" stroke-width="{p["nw"]}" stroke-linecap="round"/>'
    if p.get('mane'):
        g += f'<circle cx="{n(nx1)}" cy="{n(ny1)}" r="{p["mane"]}" fill="#6b3f1f"/>'
    hl, hr = p['hl'], p['hr']
    hxx, hyy = nx1 + hl * .35, ny1 + hl * .2
    g += f'<ellipse cx="{n(hxx)}" cy="{n(hyy)}" rx="{n(hl * .5)}" ry="{hr}" fill="{col}" transform="rotate(28 {n(hxx)} {n(hyy)})"/>'
    g += f'<circle cx="{n(nx1 + hl * .12)}" cy="{n(ny1 - 2)}" r="3.5" fill="#1a1410"/>'
    ear = p['ear']
    ex, ey = nx1 - 4, ny1 - hr * .7
    if ear == 'point':
        g += f'<path d="M{n(ex)} {n(ey)}L{n(ex - 10)} {n(ey - 26)}L{n(ex + 12)} {n(ey - 6)}Z" fill="{dark}"/>'
    elif ear == 'long':
        g += f'<path d="M{n(ex)} {n(ey)}L{n(ex - 14)} {n(ey - 52)}L{n(ex + 14)} {n(ey - 10)}Z" fill="{dark}"/>'
    elif ear == 'tiny':
        g += f'<circle cx="{n(ex)}" cy="{n(ey)}" r="5" fill="{dark}"/>'
    elif ear == 'flat':
        g += f'<ellipse cx="{n(ex - 12)}" cy="{n(ey + 6)}" rx="14" ry="6" fill="{dark}" transform="rotate(-20 {n(ex - 12)} {n(ey + 6)})"/>'
    elif ear == 'round':
        g += f'<circle cx="{n(ex)}" cy="{n(ey - 2)}" r="9" fill="{dark}"/>'
    if p.get('horn') is True:
        g += f'<path d="M{n(ex + 2)} {n(ey)}Q{n(ex - 12)} {n(ey - 30)} {n(ex + 14)} {n(ey - 40)}" stroke="#efe4c8" stroke-width="7" fill="none" stroke-linecap="round"/>'
    elif p.get('horn') == 'back':
        g += f'<path d="M{n(ex + 4)} {n(ey)}Q{n(ex - 4)} {n(ey - 30)} {n(ex - 26)} {n(ey - 30)}" stroke="#efe4c8" stroke-width="6" fill="none" stroke-linecap="round"/>'
    if p.get('antler'):
        d = f'M{n(ex + 4)} {n(ey)}L{n(ex - 6)} {n(ey - 56)}M{n(ex - 2)} {n(ey - 30)}L{n(ex + 22)} {n(ey - 52)}M{n(ex - 6)} {n(ey - 56)}L{n(ex - 26)} {n(ey - 78)}M{n(ex - 6)} {n(ey - 56)}L{n(ex + 6)} {n(ey - 82)}'
        g += f'<path d="{d}" stroke="#d9c7a0" stroke-width="5" fill="none" stroke-linecap="round"/>'
    if p.get('beard'):
        g += f'<path d="M{n(hxx + hl * .3)} {n(hyy + hr * .8)}L{n(hxx + hl * .2)} {n(hyy + hr * 2.4)}L{n(hxx + hl * .05)} {n(hyy + hr * .9)}Z" fill="{dark}"/>'
    return g + '</g>'


def bird(x, y, s=1, c='#2a2a35', w=3):
    return (f'<path d="M{n(x - 30 * s)} {n(y)}Q{n(x - 15 * s)} {n(y - 22 * s)} {n(x)} {n(y)}Q{n(x + 15 * s)} {n(y - 22 * s)} {n(x + 30 * s)} {n(y)}" '
            f'fill="none" stroke="{c}" stroke-width="{n(w * s)}" stroke-linecap="round"/>')


def flock(k, seed, x0, x1, y0, y1, c='#2a2a35', smin=.5, smax=1.2):
    r = random.Random(seed)
    return ''.join(bird(r.uniform(x0, x1), r.uniform(y0, y1), r.uniform(smin, smax), c) for _ in range(k))


def eagle(x, y, s=1, c='#3a2a1e'):
    return (f'<g transform="translate({n(x)} {n(y)}) scale({n(s)})" fill="{c}">'
            '<path d="M0 0Q-60 -50 -190 -34Q-140 -4 -170 40Q-90 10 -30 40L0 70L30 40Q90 10 170 40Q140 -4 190 -34Q60 -50 0 0Z"/>'
            '<circle cx="0" cy="-10" r="17"/><path d="M12 -12L34 -4L12 2Z" fill="#e0a030"/>'
            '<path d="M-14 66L0 110L14 66Z"/></g>')


def dove(x, y, s=1, c='#ffffff'):
    return (f'<g transform="translate({n(x)} {n(y)}) scale({n(s)})" fill="{c}"><ellipse cx="0" cy="0" rx="62" ry="30"/>'
            '<circle cx="52" cy="-30" r="20"/><path d="M68 -33L92 -24L68 -18Z" fill="#f4a261"/><path d="M-50 0L-150 18L-84 -34Z"/>'
            '<path d="M-10 -14Q-60 -120 -170 -150Q-130 -50 -60 -8Z"/><path d="M10 -14Q40 -110 150 -160Q120 -50 56 -8Z" opacity=".9"/>'
            '<circle cx="58" cy="-33" r="3" fill="#222"/></g>')


def fish(x, y, s=1, c='#f4a261', flip=False):
    sx = -s if flip else s
    return (f'<g transform="translate({n(x)} {n(y)}) scale({n(sx)} {n(s)})"><path d="M-40 0Q0 -28 40 0Q0 28 -40 0Z" fill="{c}"/>'
            f'<path d="M38 0L64 -20L64 20Z" fill="{c}"/><circle cx="-22" cy="-4" r="3.5" fill="#222"/></g>')


def whale(x, y, s=1, c='#35566e'):
    return (f'<g transform="translate({n(x)} {n(y)}) scale({n(s)})"><path d="M-200 0Q-200 -90 -80 -100Q80 -110 190 -30Q230 -60 270 -100Q280 -40 250 -5Q290 20 300 60Q240 40 200 20Q120 90 -80 80Q-200 70 -200 0Z" fill="{c}"/>'
            '<path d="M-190 25Q-60 70 100 40" fill="none" stroke="#9fb7c7" stroke-width="8" opacity=".5"/><circle cx="-140" cy="-20" r="6" fill="#111"/>'
            '<path d="M-120 -104L-130 -170M-120 -104L-90 -160M-120 -104L-160 -150" stroke="#cfe8f5" stroke-width="7" stroke-linecap="round"/></g>')


def snake(x, y, s=1, c='#4f7a3a', rise=True):
    return (f'<g transform="translate({n(x)} {n(y)}) scale({n(s)})"><path d="M-170 0C-110 0 -110 -44 -50 -44S10 0 70 -20S110 -100 112 -150" stroke="{c}" stroke-width="22" fill="none" stroke-linecap="round"/>'
            f'<ellipse cx="118" cy="-160" rx="26" ry="18" fill="{c}" transform="rotate(-70 118 -160)"/><circle cx="112" cy="-168" r="4" fill="#ffd166"/>'
            '<path d="M124 -182L132 -204M132 -204L122 -212M132 -204L144 -210" stroke="#d62828" stroke-width="3" fill="none"/></g>')


def bee(x, y, s=1):
    out = f'<g transform="translate({n(x)} {n(y)}) scale({n(s)})"><ellipse cx="-8" cy="-14" rx="16" ry="9" fill="#dff1ff" opacity=".8" transform="rotate(-25 -8 -14)"/><ellipse cx="8" cy="-14" rx="16" ry="9" fill="#dff1ff" opacity=".8" transform="rotate(25 8 -14)"/>'
    out += '<ellipse cx="0" cy="0" rx="26" ry="16" fill="#f4c20d"/>'
    for dx in (-8, 4, 14):
        ry = 16 * math.sqrt(max(0, 1 - (dx / 26) ** 2))
        out += f'<ellipse cx="{dx}" cy="0" rx="3.5" ry="{n(ry)}" fill="#1a1410"/>'
    return out + '<circle cx="-26" cy="-2" r="9" fill="#1a1410"/></g>'


def locust(x, y, s=1, c='#7a9a2f'):
    return (f'<g transform="translate({n(x)} {n(y)}) scale({n(s)})"><ellipse cx="0" cy="0" rx="28" ry="9" fill="{c}"/><circle cx="30" cy="-3" r="8" fill="{c}"/>'
            f'<path d="M-6 6L-14 -20L-34 6M2 6L8 20M12 6L20 20" stroke="{c}" stroke-width="3" fill="none"/><path d="M-10 -4Q-40 -20 -50 -2Z" fill="#b8c76a" opacity=".8"/></g>')


def raven(x, y, s=1, c='#15151c', flip=False):
    sx = -s if flip else s
    return (f'<g transform="translate({n(x)} {n(y)}) scale({n(sx)} {n(s)})" fill="{c}"><ellipse cx="0" cy="-20" rx="30" ry="16" transform="rotate(-15 0 -20)"/>'
            '<circle cx="28" cy="-38" r="12"/><path d="M38 -40L58 -34L38 -30Z" fill="#555"/><path d="M-26 -14L-64 4L-34 -4Z"/>'
            '<path d="M-6 -4L-8 14M8 -4L10 14" stroke="#555" stroke-width="3"/></g>')


def frog(x, y, s=1, c='#5a9a3a'):
    return (f'<g transform="translate({n(x)} {n(y)}) scale({n(s)})" fill="{c}"><ellipse cx="0" cy="-14" rx="30" ry="18"/><circle cx="-12" cy="-34" r="9"/><circle cx="12" cy="-34" r="9"/>'
            '<circle cx="-12" cy="-35" r="3.5" fill="#111"/><circle cx="12" cy="-35" r="3.5" fill="#111"/><ellipse cx="-30" cy="-2" rx="16" ry="6"/><ellipse cx="30" cy="-2" rx="16" ry="6"/></g>')


def scatter(fn, k, seed, x0, x1, y0, y1, smin=.6, smax=1.1, **kw):
    r = random.Random(seed)
    return ''.join(fn(r.uniform(x0, x1), r.uniform(y0, y1), r.uniform(smin, smax), **kw) for _ in range(k))
