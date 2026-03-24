import socket
import threading

HOST = "127.0.0.1"
PORT = 12345

clients = []

def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            client.send(message)

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break
            broadcast(message, client_socket)
        except:
            break

    clients.remove(client_socket)
    client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print("Serveur de chat en écoute...")

    while True:
        client_socket, addr = server.accept()
        print("Nouvelle connexion :", addr)

        clients.append(client_socket)

        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()

if __name__ == "__main__":
    start_server()
