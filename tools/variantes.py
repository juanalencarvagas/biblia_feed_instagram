"""Variações de uma mesma cena: dia, amanhecer, entardecer e noite.

Cada função de cena recebe (s, t). O desenho base é o "dia"; as demais variações aplicam uma
camada de cor/luz por cima e, em algumas, espelham a composição.
"""
from svglib import H, W, fullmoon, stars

NAMES = ('dia', 'amanhecer', 'entardecer', 'noite')


class Variant:
    def __init__(self, v):
        self.v = v % 4
        self.name = NAMES[self.v]
        self.mirror = self.v == 2

    def overlay(self):
        v = self.v
        if v == 0:
            return ''
        if v == 1:  # amanhecer: rosa no alto, dourado no horizonte
            return ('<defs><linearGradient id="ovl" x2="0" y2="1"><stop offset="0" stop-color="#f08aa8" stop-opacity=".34"/>'
                    '<stop offset=".7" stop-color="#ffc98a" stop-opacity=".30"/><stop offset="1" stop-color="#ffe3b0" stop-opacity=".18"/></linearGradient></defs>'
                    f'<rect width="{W}" height="{H}" fill="url(#ovl)"/>')
        if v == 2:  # entardecer: roxo no alto, laranja forte embaixo
            return ('<defs><linearGradient id="ovl" x2="0" y2="1"><stop offset="0" stop-color="#5a3a8a" stop-opacity=".40"/>'
                    '<stop offset=".6" stop-color="#ff7a3a" stop-opacity=".34"/><stop offset="1" stop-color="#a8431f" stop-opacity=".32"/></linearGradient></defs>'
                    f'<rect width="{W}" height="{H}" fill="url(#ovl)"/>')
        # noite: azul profundo + estrelas e lua
        return ('<defs><linearGradient id="ovl" x2="0" y2="1"><stop offset="0" stop-color="#0b1233"/><stop offset="1" stop-color="#1c2a5a"/></linearGradient></defs>'
                f'<rect width="{W}" height="{H}" fill="url(#ovl)" opacity=".62"/>'
                + stars(46, 10, 300, '#fff4cd', 3, .85) + fullmoon(1020, 130, 44, '#e8e2cc'))
