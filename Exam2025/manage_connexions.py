import socket

def manage_connexions(self):

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind((self.ip_address, self.port))

    server_socket.listen(self.max_client)

    while True:

        client_socket, addr = server_socket.accept()

        self.clients.append(client_socket)
