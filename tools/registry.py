"""Registro das cenas: chave, rótulo, palavras-chave e função de desenho.

words: palavras em minúsculas, SEM acento, separadas por espaço.
  - "ovelh*"  -> prefixo (casa ovelha, ovelhas, ovelhinha...)
  - "mar"     -> palavra exata
prio: peso da cena quando há empate entre temas (personagens > animais/objetos > conceitos).
variants: nº de variações (dia, amanhecer, entardecer, noite). A função recebe (s, t) com t = Variant.
  Arquivos: <key>.svg (variação 0) e <key>_v1.svg, <key>_v2.svg ...
"""
from svglib import Scene

REGISTRY = []


def _clean(words):
    """Só palavras ASCII sem hífen (o texto é tokenizado por letras), sem repetições."""
    out = []
    for w in words.split():
        if '-' in w or not w.replace('*', '').isascii() or w in out:
            continue
        out.append(w)
    return out


def scene(key, label, words, prio=1, variants=1):
    def deco(fn):
        REGISTRY.append(dict(key=key, label=label, words=_clean(words), prio=prio, fn=fn, variants=variants))
        return fn
    return deco


def legacy(key, label, words, prio=1):
    """Cena cujo SVG já existe em assets/scenes (não é regenerada)."""
    REGISTRY.append(dict(key=key, label=label, words=_clean(words), prio=prio, fn=None, variants=1))


def filename(key, v=0):
    return f'{key}.svg' if v == 0 else f'{key}_v{v}.svg'


def build(item, v=0):
    s = Scene(item['key'] + (f'v{v}' if v else ''))
    if item['variants'] > 1:
        from variantes import Variant
        t = Variant(v)
        item['fn'](s, t)
        s.add(t.overlay())
        return s.render(mirror=t.mirror)
    item['fn'](s)
    return s.render()
