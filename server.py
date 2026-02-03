from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


class LandingPageHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith("/"):
            index_path = Path(self.directory, self.path.lstrip("/"), "index.html")
            if index_path.exists():
                self.path = f"{self.path}index.html"
        super().do_GET()


def run(port: int = 8000) -> None:
    server = ThreadingHTTPServer(("", port), LandingPageHandler)
    print(f"Serving on http://localhost:{port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped")
    finally:
        server.server_close()


if __name__ == "__main__":
    run()
