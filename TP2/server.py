import socket

HOST = "127.0.0.1"
PORT = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind((HOST, PORT))

print("Serveur UDP en écoute...")

data, addr = sock.recvfrom(1024)
print("Message reçu :", data.decode())

sock.sendto("Message reçu par le serveur".encode(), addr)
