import socket
import json

HOST = "127.0.0.1"
PORT = 12350

serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur.bind((HOST, PORT))
serveur.listen(1)

print("Serveur JSON démarré")

client_socket, addr = serveur.accept()
print("Connexion de :", addr)

data = client_socket.recv(1024).decode()

message = json.loads(data)

print("Nom :", message["nom"])
print("Date :", message["date_connexion"])
print("Lieu :", message["lieu"])

client_socket.close()
serveur.close()
