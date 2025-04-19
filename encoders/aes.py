# encoders/aes.py

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64

def aes_encrypt(payload: str, key: str) -> str:
    """
    Payload'ı AES ile şifreler (CBC mode, Base64 ile encode edilmiş halde döner).

    :param payload: Orijinal payload
    :param key: 16, 24, ya da 32 byte uzunluğunda AES anahtarı
    :return: Base64 encoded AES şifreli payload
    """
    key_bytes = key.encode('utf-8').ljust(32, b'\0')[:32]  # 256-bit key
    iv = get_random_bytes(16)
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(payload.encode(), AES.block_size))
    return base64.b64encode(iv + ciphertext).decode()

def aes_decrypt(encoded: str, key: str) -> str:
    """
    AES ile şifrelenmiş payload'ı çözer.

    :param encoded: Base64 encoded AES çıktısı
    :param key: AES anahtarı
    :return: Orijinal payload
    """
    key_bytes = key.encode('utf-8').ljust(32, b'\0')[:32]
    raw = base64.b64decode(encoded)
    iv = raw[:16]
    ciphertext = raw[16:]
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(ciphertext), AES.block_size).decode()
