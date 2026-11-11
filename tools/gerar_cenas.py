"""Gera assets/scenes/*.svg a partir dos módulos scenes_*.py.

Uso:  python3 tools/gerar_cenas.py            # gera tudo + valida
      python3 tools/gerar_cenas.py --sheet    # também cria /tmp/gen/sheet_N.svg (folhas de contato)
"""
import json
import pathlib
import sys
import xml.dom.minidom

sys.path.insert(0, str(pathlib.Path(__file__).parent))

import registry  # noqa: E402
import scenes_natureza  # noqa: F401,E402
import scenes_animais  # noqa: F401,E402
import scenes_objetos  # noqa: F401,E402
import scenes_conceitos  # noqa: F401,E402
import scenes_personagens  # noqa: F401,E402
import scenes_narrativas  # noqa: F401,E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / 'assets' / 'scenes'


def main():
    sheet = '--sheet' in sys.argv
    built = 0
    keys = set()
    for item in registry.REGISTRY:
        if item['key'] in keys:
            raise SystemExit(f"chave duplicada: {item['key']}")
        keys.add(item['key'])
        if item['fn'] is None:
            if not (OUT / f"{item['key']}.svg").exists():
                raise SystemExit(f"svg legado ausente: {item['key']}")
            continue
        for v in range(item['variants']):
            svg = registry.build(item, v)
            xml.dom.minidom.parseString(svg)
            (OUT / registry.filename(item['key'], v)).write_text(svg, encoding='utf-8')
            built += 1
    # manifesto para o app.js (servido em /assets/scenes/manifest.json) e para os testes
    manifest = [dict(key=i['key'], label=i['label'], words=i['words'], prio=i['prio'], variants=i['variants'])
                for i in registry.REGISTRY]
    (ROOT / 'tools' / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=1), encoding='utf-8')
    (OUT / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')
    total = sum(i['variants'] for i in registry.REGISTRY)
    print(f'{built} svgs gerados, {len(registry.REGISTRY)} cenas, {total} imagens no total')
    if sheet:
        pathlib.Path('/tmp/gen').mkdir(exist_ok=True)
        files = [registry.filename(i['key'], v) for i in registry.REGISTRY for v in range(i['variants'])]
        per, cols = 20, 4
        for p in range(0, len(files), per):
            chunk = files[p:p + per]
            cw, ch = 400, 300
            rows = (len(chunk) + cols - 1) // cols
            body = ''
            for i, f in enumerate(chunk):
                x, y = (i % cols) * cw, (i // cols) * (ch + 22)
                inner = (OUT / f).read_text(encoding='utf-8')
                inner = inner.replace(' width="1200" height="900"', ' width="%d" height="%d"' % (cw - 6, ch - 6), 1)
                inner = inner.replace('id="', f'id="s{i}_').replace('url(#', f'url(#s{i}_')
                body += f'<g transform="translate({x} {y})">{inner}<text x="6" y="{ch + 14}" font-size="16" font-family="Helvetica" fill="#111">{f[:-4]}</text></g>'
            sv = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{cols * cw}" height="{rows * (ch + 22)}">'
                  f'<rect width="100%" height="100%" fill="#fff"/>{body}</svg>')
            pathlib.Path(f'/tmp/gen/sheet_{p // per}.svg').write_text(sv, encoding='utf-8')


main()
