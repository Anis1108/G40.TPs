from http.server import BaseHTTPRequestHandler, HTTPServer

HOST = "127.0.0.1"
PORT = 8080

class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        # Si l'utilisateur demande index.html
        if self.path == "/" or self.path == "/index.html":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            with open("index.html", "r") as f:
                self.wfile.write(f.read().encode())

        else:
            # Sinon erreur 404
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            with open("error404.html", "r") as f:
                self.wfile.write(f.read().encode())


# Lancer le serveur
server = HTTPServer((HOST, PORT), MyHandler)

print(f"Serveur lancé sur http://{HOST}:{PORT}")
server.serve_forever()
