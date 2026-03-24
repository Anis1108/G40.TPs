import socket

HOST = "127.0.0.1"
PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

client_socket.send("Bonjour serveur".encode())

reponse = client_socket.recv(1024).decode()
print("Réponse du serveur :", reponse)

client_socket.close()
