import socket

HOST = "127.0.0.1"
PORT = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = "Bonjour serveur UDP"
sock.sendto(message.encode(), (HOST, PORT))

data, server = sock.recvfrom(1024)
print("Réponse :", data.decode())
