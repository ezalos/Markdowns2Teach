# ABOUTME: Password-protected HTTP file server using stdlib only.
# ABOUTME: Wraps SimpleHTTPRequestHandler with HTTP Basic Auth on every request.

import argparse
import base64
import os
import sys
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer


class AuthHandler(SimpleHTTPRequestHandler):
    """HTTP handler that requires Basic Auth with a configured password."""

    password = "HelloWorld"

    def do_GET(self):
        if not self._check_auth():
            return
        super().do_GET()

    def do_HEAD(self):
        if not self._check_auth():
            return
        super().do_HEAD()

    def _check_auth(self):
        """Return True if request has valid credentials, send 401 otherwise."""
        auth_header = self.headers.get("Authorization")
        if auth_header and auth_header.startswith("Basic "):
            try:
                decoded = base64.b64decode(auth_header[6:]).decode("utf-8")
                # Accept any username, check password only
                _, _, pwd = decoded.partition(":")
                if pwd == self.password:
                    return True
            except Exception:
                pass
        self.send_response(401)
        self.send_header("WWW-Authenticate", 'Basic realm="Slides"')
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"401 Unauthorized\n")
        return False

    def log_message(self, format, *args):
        # Prefix log lines with the server address for clarity
        sys.stderr.write(
            f"[serve-auth] {self.address_string()} - {format % args}\n"
        )


def main():
    parser = argparse.ArgumentParser(
        description="Password-protected static file server"
    )
    parser.add_argument(
        "directory",
        nargs="?",
        default=os.getcwd(),
        help="Directory to serve (default: cwd)",
    )
    parser.add_argument(
        "--port", type=int, default=3901, help="Port to listen on (default: 3901)"
    )
    parser.add_argument(
        "--password",
        default="HelloWorld",
        help="Required password (default: HelloWorld)",
    )
    args = parser.parse_args()

    AuthHandler.password = args.password
    handler = partial(AuthHandler, directory=args.directory)

    server = ThreadingHTTPServer(("0.0.0.0", args.port), handler)
    print(f"Serving {args.directory} on http://0.0.0.0:{args.port} (password-protected)")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down.")
        server.shutdown()


if __name__ == "__main__":
    main()
