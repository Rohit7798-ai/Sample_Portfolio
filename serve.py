"""Local development HTTP server.
Ensures correct MIME types for .mjs, .woff2, and .webp, and handles clean SPA-style routing.
"""

import http.server
import mimetypes
import os
import socketserver
import sys

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

mimetypes.add_type("application/javascript", ".mjs")
mimetypes.add_type("font/woff2", ".woff2")
mimetypes.add_type("image/webp", ".webp")
mimetypes.add_type("video/mp4", ".mp4")


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        super().end_headers()

    def do_GET(self):
        clean = self.path.split("?")[0].rstrip("/")
        if clean in ["/home", "/work", "/my-story", "/about"]:
            self.path = "/index.html"
        return super().do_GET()

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        data = self.rfile.read(length) if length > 0 else b""
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.end_headers()
        self.wfile.write(b'{"ok": true, "status": "received"}')


def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else PORT
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("127.0.0.1", port), Handler) as httpd:
        print(f"Serving at http://localhost:{port}/")
        httpd.serve_forever()


if __name__ == "__main__":
    main()
