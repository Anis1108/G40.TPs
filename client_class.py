import socket

class Client:

    def __init__(self, host="127.0.0.1", port=12345):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        self.client_socket.connect((self.host, self.port))

        self.client_socket.send("Bonjour serveur".encode())

        response = self.client_socket.recv(1024).decode()
        print("Réponse du serveur :", response)

        self.client_socket.close()


if __name__ == "__main__":
    client = Client()
    client.start()
