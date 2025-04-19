# core/obfuscator.py

import base64
import random
import string
import textwrap

def random_var_name(length=8):
    return ''.join(random.choices(string.ascii_letters, k=length))


def obfuscate_bash(payload: str) -> str:
    """
    Bash payload içindeki değişken adlarını rastgeleleştirir.
    """
    lines = payload.split('\n')
    obfuscated_lines = []

    for line in lines:
        if "=" in line and not line.strip().startswith("#"):
            var, rest = line.split("=", 1)
            new_var = random_var_name()
            payload = payload.replace(var.strip(), new_var)
            obfuscated_lines.append(f"{new_var}={rest}")
        else:
            obfuscated_lines.append(line)

    return '\n'.join(obfuscated_lines)


def obfuscate_python_base64(payload: str) -> str:
    """
    Python payload'ı base64 ile encode edip, çalıştırılabilir hale getirir.
    """
    encoded = base64.b64encode(payload.encode()).decode()
    wrapper = f"""
import base64
exec(base64.b64decode('{encoded}').decode('utf-8'))
"""
    return textwrap.dedent(wrapper)
