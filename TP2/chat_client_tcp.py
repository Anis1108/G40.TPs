import socket
import threading

HOST = "127.0.0.1"
PORT = 12345

def receive_messages(client):
    while True:
        try:
            message = client.recv(1024).decode()
            print(message)
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

start_client()
