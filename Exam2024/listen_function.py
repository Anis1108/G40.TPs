import socket

def listen(self):

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind(("0.0.0.0", 1234))

    server_socket.listen(self.max_gamers)

    while len(self.players) < self.max_gamers:

        client_socket, addr = server_socket.accept()

        self.players.append(client_socket)
