import socket

HOST = "127.0.0.1"
PORT = 8080   # ⚠️ pas 80 (il faut sudo pour 80)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print(f"Serveur lancé sur http://{HOST}:{PORT}")

while True:
    client_socket, addr = server.accept()
    print(f"Connexion de {addr}")

    request = client_socket.recv(1024).decode()
    print(request)

    # Vérifier si GET /index.html
    if "GET / " in request or "GET /index.html" in request:
        with open("index.html", "r") as f:
            body = f.read()

        response = f"""HTTP/1.1 200 OK
Content-Type: text/html

{body}
"""
    else:
        with open("error404.html", "r") as f:
            body = f.read()

        response = f"""HTTP/1.1 404 Not Found
Content-Type: text/html

{body}
"""

    client_socket.sendall(response.encode())
    client_socket.close()
