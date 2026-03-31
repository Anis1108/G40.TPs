import socket

HOST = "127.0.0.1"
PORT = 12345

def main():
    # Création de la socket raw
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
    s.bind((HOST, PORT))

    print("Serveur en écoute sur {}:{}".format(HOST, PORT))

    while True:
        data, addr = s.recvfrom(1024)
        print(f"Message reçu : {data.decode()} de {addr}")

if __name__ == "__main__":
    main()