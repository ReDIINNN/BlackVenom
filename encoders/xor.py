# encoders/xor.py

def xor_encrypt(payload: str, key: str) -> str:
    """
    XOR algoritmasıyla payload'ı encode eder.

    :param payload: Orijinal payload stringi
    :param key: XOR şifreleme anahtarı
    :return: XOR ile encode edilmiş (hex olarak) string
    """
    encrypted = []
    for i in range(len(payload)):
        encrypted_char = ord(payload[i]) ^ ord(key[i % len(key)])
        encrypted.append(format(encrypted_char, '02x'))  # hex formatında
    return ''.join(encrypted)

def xor_decrypt(encrypted_payload: str, key: str) -> str:
    """
    XOR algoritmasıyla encode edilmiş (hex) payload'ı çözer.

    :param encrypted_payload: Hex formatında payload
    :param key: XOR şifreleme anahtarı
    :return: Orijinal payload stringi
    """
    decrypted = []
    for i in range(0, len(encrypted_payload), 2):
        hex_char = encrypted_payload[i:i+2]
        char = int(hex_char, 16)
        decrypted_char = char ^ ord(key[(i//2) % len(key)])
        decrypted.append(chr(decrypted_char))
    return ''.join(decrypted)
