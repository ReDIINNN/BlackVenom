# payloads/custom/custom_reverse_shell.py

def build_custom_shell(template: str, ip: str, port: int) -> str:
    """
    Kullanıcının verdiği shell template'ini IP ve port ile doldurur.
    
    Template içinde {{IP}} ve {{PORT}} değişkenleri olmalıdır.
    
    :param template: Kullanıcının verdiği payload kodu
    :param ip: Saldırganın IP adresi
    :param port: Bağlantı portu
    :return: Kullanıma hazır payload stringi
    """
    if "{{IP}}" not in template or "{{PORT}}" not in template:
        return "# ERROR: Template must contain {{IP}} and {{PORT}} placeholders."

    filled = template.replace("{{IP}}", ip).replace("{{PORT}}", str(port))
    return filled
