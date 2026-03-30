import socket
import json
from datetime import datetime

HOST = "127.0.0.1"
PORT = 12360

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

nom = input("Nom : ")
lieu = input("Lieu : ")

print("\nChoisir le type de message :")
print("1 - identification")
print("2 - client_connecte")
print("3 - client_deconnecte")
print("4 - client_ecrit")
print("5 - etat")

choix = input("Votre choix : ")

if choix == "1":
    message = {
        "type": "identification",
        "nom": nom,
        "date_connexion": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "lieu": lieu
    }

elif choix == "2":
    message = {
        "type": "notification",
        "event": "client_connecte",
        "nom": nom
    }

elif choix == "3":
    message = {
        "type": "notification",
        "event": "client_deconnecte",
        "nom": nom
    }

elif choix == "4":
    message = {
        "type": "notification",
        "event": "client_ecrit",
        "nom": nom
    }

elif choix == "5":
    etat = input("Entrer l'etat (LIBRE / OCCUPE / INACTIF) : ")
    message = {
        "type": "etat",
        "nom": nom,
        "valeur": etat
    }

else:
    print("Choix invalide")
    client.close()
    exit()

message_json = json.dumps(message)
client.send(message_json.encode())

print("\nMessage envoyé :")
print(message_json)

client.close()
