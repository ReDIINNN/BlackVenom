# encoders/base64.py

import base64

def encode(payload: str) -> str:
    """
    Payload'ı base64 ile encode eder.
    
    :param payload: Orijinal payload stringi
    :return: Base64 ile encode edilmiş string
    """
    encoded_bytes = base64.b64encode(payload.encode("utf-8"))
    return encoded_bytes.decode("utf-8")

def decode(encoded_payload: str) -> str:
    """
    Base64 ile encode edilmiş payload'ı çözer.
    
    :param encoded_payload: Base64 kodlu payload
    :return: Orijinal payload stringi
    """
    decoded_bytes = base64.b64decode(encoded_payload.encode("utf-8"))
    return decoded_bytes.decode("utf-8")
