import socket

HOST = "127.0.0.1"
PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print("Serveur en écoute...")

client_socket, addr = server_socket.accept()
print("Connexion depuis", addr)

message = client_socket.recv(1024).decode()
print("Message reçu :", message)

client_socket.send("Bonjour client".encode())

client_socket.close()
server_socket.close()
