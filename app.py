"""Run the local Python web app: python app.py (standard library only)."""
import argparse
import json
import re
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse

from engine import ROOT, full_report, load_config, validate_config
from reporting import save_report


def handler_for(default_config):
    class Handler(BaseHTTPRequestHandler):
        def send(self, status, body, content_type='application/json; charset=utf-8'):
            if not isinstance(body, bytes):
                body = body.encode('utf-8')
            self.send_response(status)
            self.send_header('Content-Type', content_type)
            self.send_header('Content-Length', str(len(body)))
            self.send_header('Cache-Control', 'no-store')
            self.send_header('X-Content-Type-Options', 'nosniff')
            self.end_headers()
            self.wfile.write(body)

        def do_GET(self):
            path = urlparse(self.path).path
            if path == '/api/health':
                self.send(200, '{"status":"ok"}')
            elif path == '/api/results':
                self.send(200, json.dumps(full_report(default_config), allow_nan=False))
            elif path in ('/', '/index.html'):
                self.send(200, (ROOT / 'static/index.html').read_bytes(), 'text/html; charset=utf-8')
            elif path == '/favicon.ico':
                self.send(204, b'')
            else:
                self.send(404, '{"error":"Not found"}')

        def do_POST(self):
            if urlparse(self.path).path != '/api/analyze':
                self.send(404, '{"error":"Not found"}')
                return
            try:
                size = int(self.headers.get('Content-Length', '0'))
                if not 0 < size <= 20000:
                    raise ValueError('Request must be between 1 and 20000 bytes.')
                config = json.loads(self.rfile.read(size))
                if not isinstance(config, dict):
                    raise ValueError('Request must be a configuration object.')
                validate_config(config)
                result = full_report(config)
                self.send(200, json.dumps(result, allow_nan=False))
            except (ValueError, KeyError, TypeError) as error:
                self.send(400, json.dumps({'error': str(error)}))

        def log_message(self, format, *args):
            pass
    return Handler


def main():
    parser = argparse.ArgumentParser(description='ETF Portfolio Committee Dashboard; Python 3.10+; no installation needed.')
    parser.add_argument('--export', action='store_true', help='Save decision output and memo, then exit.')
    parser.add_argument('--snapshot', help='Save a new immutable output folder with this label, then exit; existing labels are refused.')
    parser.add_argument('--config', help='Use a separately saved JSON configuration.')
    parser.add_argument('--port', type=int, default=8766)
    args = parser.parse_args()
    if args.snapshot and not re.fullmatch(r'[A-Za-z0-9_-]{1,64}', args.snapshot):
        parser.error('Snapshot labels allow 1–64 letters, digits, underscores or hyphens.')
    config = load_config(args.config)
    if args.export or args.snapshot:
        folder = save_report(full_report(config), snapshot=args.snapshot)
        print(f'Saved decision numbers: {folder / "decision-output.md"}')
        return
    # Starting the app does not rewrite frozen outputs or any personal evidence.
    server = ThreadingHTTPServer(('127.0.0.1', args.port), handler_for(config))
    print(f'ETF Portfolio Committee Dashboard: http://127.0.0.1:{server.server_port}', flush=True)
    print('Open that address in a browser. Ctrl+C stops the app. No network or API key required.', flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == '__main__':
    main()
