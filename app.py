#!/usr/bin/env python3
"""Bíblia Feed 3.0: leitor bíblico local com layout inspirado no Instagram."""
import json
import os
import threading
import urllib.request
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parent
DATA_PT = ROOT / 'almeida-livre.json'
DATA_EN = ROOT / 'kjv.json'
SOURCES_PT = [
    'https://raw.githubusercontent.com/midvash/bible-data/main/versions/pt/almeida-livre/almeida-livre.json',
]
SOURCES_EN = [
    'https://raw.githubusercontent.com/midvash/bible-data/main/versions/en/kjv/kjv.json',
    'https://raw.githubusercontent.com/midvash/bible-data/main/versions/en/king-james/king-james.json',
    'https://raw.githubusercontent.com/midvash/bible-data/main/versions/en/king-james-version/king-james-version.json',
]
PT_BOOKS = 'Gênesis|Êxodo|Levítico|Números|Deuteronômio|Josué|Juízes|Rute|1 Samuel|2 Samuel|1 Reis|2 Reis|1 Crônicas|2 Crônicas|Esdras|Neemias|Ester|Jó|Salmos|Provérbios|Eclesiastes|Cânticos|Isaías|Jeremias|Lamentações|Ezequiel|Daniel|Oséias|Joel|Amós|Obadias|Jonas|Miqueias|Naum|Habacuque|Sofonias|Ageu|Zacarias|Malaquias|Mateus|Marcos|Lucas|João|Atos|Romanos|1 Coríntios|2 Coríntios|Gálatas|Efésios|Filipenses|Colossenses|1 Tessalonicenses|2 Tessalonicenses|1 Timóteo|2 Timóteo|Tito|Filemom|Hebreus|Tiago|1 Pedro|2 Pedro|1 João|2 João|3 João|Judas|Apocalipse'.split('|')
EN_BOOKS = 'Genesis|Exodus|Leviticus|Numbers|Deuteronomy|Joshua|Judges|Ruth|1 Samuel|2 Samuel|1 Kings|2 Kings|1 Chronicles|2 Chronicles|Ezra|Nehemiah|Esther|Job|Psalms|Proverbs|Ecclesiastes|Song of Songs|Isaiah|Jeremiah|Lamentations|Ezekiel|Daniel|Hosea|Joel|Amos|Obadiah|Jonah|Micah|Nahum|Habakkuk|Zephaniah|Haggai|Zechariah|Malachi|Matthew|Mark|Luke|John|Acts|Romans|1 Corinthians|2 Corinthians|Galatians|Ephesians|Philippians|Colossians|1 Thessalonians|2 Thessalonians|1 Timothy|2 Timothy|Titus|Philemon|Hebrews|James|1 Peter|2 Peter|1 John|2 John|3 John|Jude|Revelation'.split('|')

_cache = None
_lock = threading.Lock()


def download_first(urls):
    last_error = None
    for url in urls:
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'BibliaFeed/3.0'})
            with urllib.request.urlopen(req, timeout=45) as response:
                return response.read()
        except Exception as exc:  # pragma: no cover - depends on network
            last_error = exc
    if last_error:
        raise last_error
    raise RuntimeError('Nenhuma fonte configurada')


def normalize(raw, names):
    books = raw.get('books', [])
    if len(books) != 66:
        raise ValueError('Fonte não retornou os 66 livros esperados')
    result = []
    for n, b in enumerate(books):
        result.append({
            'id': b.get('bookId', n + 1),
            'name': names[n],
            'chapters': [
                {
                    'number': c.get('chapter', i + 1),
                    'verses': [
                        {'number': v['number'], 'text': v['text']}
                        for v in c.get('verses', [])
                    ],
                }
                for i, c in enumerate(b.get('chapters', []))
            ],
        })
    return result


def load_json(path, urls, names, required=True):
    if not path.exists():
        if not urls:
            if required:
                raise RuntimeError('Fonte não configurada')
            return None
        data = download_first(urls)
        raw = json.loads(data)
        normalized = normalize(raw, names)
        path.write_text(json.dumps({'books': normalized}, ensure_ascii=False), encoding='utf-8')
        return {'books': normalized}
    raw = json.loads(path.read_text(encoding='utf-8'))
    if len(raw.get('books', [])) != 66:
        if required:
            raise ValueError('Arquivo bíblico inválido')
        return None
    return raw


def get_bibles():
    global _cache
    with _lock:
        if _cache is not None:
            return _cache
        pt = load_json(DATA_PT, SOURCES_PT, PT_BOOKS, required=True)
        en_error = None
        try:
            en = load_json(DATA_EN, SOURCES_EN, EN_BOOKS, required=False)
        except Exception as exc:  # pragma: no cover
            en = {'books': []}
            en_error = str(exc)
        payload = {'books': pt['books'], 'booksEn': en.get('books', [])}
        if en_error:
            payload['warningEn'] = en_error
        _cache = json.dumps(payload, ensure_ascii=False).encode('utf-8')
        return _cache


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = urlsplit(self.path).path
        if path == '/api/bible':
            try:
                body = get_bibles()
                status = 200
            except Exception as exc:
                body = json.dumps({'error': str(exc)}, ensure_ascii=False).encode('utf-8')
                status = 503
            ctype = 'application/json; charset=utf-8'
        elif path in ('/', '/index.html'):
            body = (ROOT / 'index.html').read_bytes()
            status = 200
            ctype = 'text/html; charset=utf-8'
        elif path in ('/style.css', '/app.js') or (path.startswith('/assets/') and '..' not in path):
            file_path = ROOT / path.lstrip('/')
            if file_path.is_file():
                body = file_path.read_bytes()
                status = 200
                if path.endswith('.css'):
                    ctype = 'text/css'
                elif path.endswith('.js'):
                    ctype = 'text/javascript'
                elif path.endswith('.svg'):
                    ctype = 'image/svg+xml'
                elif path.endswith('.json'):
                    ctype = 'application/json; charset=utf-8'
                else:
                    ctype = 'image/png'
            else:
                body = b'Not Found'
                status = 404
                ctype = 'text/plain'
        else:
            body = b'Not Found'
            status = 404
            ctype = 'text/plain'
        self.send_response(status)
        self.send_header('Content-Type', ctype)
        self.send_header('Content-Length', str(len(body)))
        self.send_header('Cache-Control', 'no-store')
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):
        pass


if __name__ == '__main__':
    port = int(os.environ.get('PORT', '8765'))
    server = ThreadingHTTPServer(('127.0.0.1', port), Handler)
    url = f'http://127.0.0.1:{port}'
    print('Bíblia Feed 3.0 iniciado em', url, '\nPressione Ctrl+C para encerrar.')
    threading.Timer(0.8, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
