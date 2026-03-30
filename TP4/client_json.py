import socket
import json
from datetime import datetime

HOST = "127.0.0.1"
PORT = 12350

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

nom = input("Nom : ")
lieu = input("Lieu : ")

message = {
    "nom": nom,
    "date_connexion": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
    "lieu": lieu
}

client.send(json.dumps(message).encode())

print("Message JSON envoyé")

client.close()
