import socket
import xml.etree.ElementTree as ET

HOST = "127.0.0.1"
PORT = 12345

serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur.bind((HOST, PORT))
serveur.listen(1)

print(f"Serveur lancé sur {HOST}:{PORT}")
print("En attente d'un client...")

client_socket, adresse = serveur.accept()
print("Client connecté :", adresse)

data = client_socket.recv(1024).decode()
print("Message reçu :")
print(data)

root = ET.fromstring(data)

nom = root.find("nom").text
date_connexion = root.find("date_connexion").text
lieu = root.find("lieu").text

print("Nom :", nom)
print("Date de connexion :", date_connexion)
print("Lieu :", lieu)

client_socket.close()
serveur.close()
