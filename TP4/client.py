import socket
from datetime import datetime

HOST = "127.0.0.1"
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

nom = input("Entrer votre nom : ")
lieu = input("Entrer votre lieu : ")
date_connexion = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

message_xml = f"""<client>
    <nom>{nom}</nom>
    <date_connexion>{date_connexion}</date_connexion>
    <lieu>{lieu}</lieu>
</client>"""

client.send(message_xml.encode())

print("Message XML envoyé :")
print(message_xml)

client.close()
