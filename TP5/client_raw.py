import socket
import struct
import random

# Fonction pour calculer le checksum
def checksum(data):
    if len(data) % 2 == 1:
        data += b'\x00'

    s = 0
    for i in range(0, len(data), 2):
        word = (data[i] << 8) + data[i+1]
        s += word

    while s >> 16:
        s = (s & 0xFFFF) + (s >> 16)

    return ~s & 0xFFFF

# Fonction pour créer l'entête IP
def create_ip_header(source_ip, dest_ip, payload_len):
    version = 4
    ihl = 5
    ip_ver_ihl = (version << 4) + ihl
    tos = 0
    total_len = 20 + 20 + payload_len
    identification = random.randint(0, 65535)
    ttl = 255
    protocol = socket.IPPROTO_TCP
    header_checksum = 0
    source = socket.inet_aton(source_ip)
    dest = socket.inet_aton(dest_ip)

    ip_header = struct.pack(
        "!BBHHHBBH4s4s",
        ip_ver_ihl, tos, total_len, identification, 0, ttl, protocol, header_checksum, source, dest
    )

    header_checksum = checksum(ip_header)
    ip_header = struct.pack(
        "!BBHHHBBH4s4s",
        ip_ver_ihl, tos, total_len, identification, 0, ttl, protocol, header_checksum, source, dest
    )

    return ip_header

# Fonction pour créer l'entête TCP
def create_tcp_header(source_ip, dest_ip, source_port, dest_port, message):
    seq = random.randint(0, 0xFFFFFFFF)
    ack_seq = 0
    data_offset = 5
    reserved = 0
    tcp_flags = 2
    window = socket.htons(5840)
    check = 0
    urg_ptr = 0

    tcp_header = struct.pack(
        "!HHLLBBHHH",
        source_port,
        dest_port,
        seq,
        ack_seq,
        (data_offset << 4) + reserved,
        tcp_flags,
        window,
        check,
        urg_ptr
    )

    source_addr = socket.inet_aton(source_ip)
    dest_addr = socket.inet_aton(dest_ip)
    placeholder = 0
    protocol = socket.IPPROTO_TCP
    tcp_length = len(tcp_header) + len(message)

    pseudo_header = struct.pack(
        "!4s4sBBH",
        source_addr,
        dest_addr,
        placeholder,
        protocol,
        tcp_length
    )

    check = checksum(pseudo_header + tcp_header + message)
    tcp_header = struct.pack(
        "!HHLLBBHHH",
        source_port,
        dest_port,
        seq,
        ack_seq,
        (data_offset << 4) + reserved,
        tcp_flags,
        window,
        check,
        urg_ptr
    )

    return tcp_header

# Fonction principale du client
def main():
    source_ip = "127.0.0.1"
    dest_ip = "127.0.0.1"
    source_port = 12345
    dest_port = 12345

    message = input("Message à envoyer : ").encode()

    ip_header = create_ip_header(source_ip, dest_ip, len(message))
    tcp_header = create_tcp_header(source_ip, dest_ip, source_port, dest_port, message)

    packet = ip_header + tcp_header + message

    # Création d'une socket raw
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
    s.sendto(packet, (dest_ip, 0))

    print("[+] Paquet envoyé")

if __name__ == "__main__":
    main()