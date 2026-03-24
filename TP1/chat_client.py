import socket
import threading

HOST = "127.0.0.1"
PORT = 12345

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            print("\nMessage reçu :", message)
        except:
            break

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    thread = threading.Thread(target=receive_messages, args=(client,))
    thread.start()

    while True:
        message = input()
        client.send(message.encode())

if __name__ == "__main__":
    start_client()
