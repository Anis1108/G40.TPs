import socket
import json

HOST = "127.0.0.1"
PORT = 12360

serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur.bind((HOST, PORT))
serveur.listen(5)

print("Serveur chat démarré...")

while True:
    client_socket, addr = serveur.accept()
    print("\nConnexion de :", addr)

    data = client_socket.recv(1024).decode()
    message = json.loads(data)

    if message["type"] == "identification":
        print("Type : identification")
        print("Nom :", message["nom"])
        print("Date :", message["date_connexion"])
        print("Lieu :", message["lieu"])

    elif message["type"] == "notification":
        print("Type : notification")
        print("Evenement :", message["event"])
        print("Nom :", message["nom"])

    elif message["type"] == "etat":
        print("Type : etat")
        print("Nom :", message["nom"])
        print("Valeur :", message["valeur"])

    else:
        print("Type de message inconnu")

    client_socket.close()
