import socket

class Server:

    def __init__(self, host="127.0.0.1", port=12345):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(1)

        print("Serveur en écoute...")

        client_socket, addr = self.server_socket.accept()
        print("Connexion depuis", addr)

        message = client_socket.recv(1024).decode()
        print("Message reçu :", message)

        client_socket.send("Bonjour client".encode())

        client_socket.close()
        self.server_socket.close()


if __name__ == "__main__":
    server = Server()
    server.start()
