import socket
import argparse

HOST = "127.0.0.1"
PORT = 12345


class Application:
    def start(self):
        raise NotImplementedError("Cette méthode doit être redéfinie")


class Server(Application):
    def start(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((HOST, PORT))

        print("Serveur UDP en écoute...")

        data, addr = sock.recvfrom(1024)
        print("Message reçu :", data.decode())

        sock.sendto("Message reçu par le serveur".encode(), addr)
        sock.close()


class Client(Application):
    def start(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        import sys
        print("Entrez un message : ")
        message = sys.stdin.readline().strip()
        sock.sendto(message.encode(), (HOST, PORT))

        data, server = sock.recvfrom(1024)
        print("Réponse :", data.decode())

        sock.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["server", "client"])
    args = parser.parse_args()

    if args.mode == "server":
        app = Server()
    else:
        app = Client()

    app.start()
