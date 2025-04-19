<p align="center">
  <img src="https://raw.githubusercontent.com/ReDIINNN/CTF-WebRecon/main/webrecon.png" alt="WebRecon Logo" width="300"/>
</p>

<h1 align="center">🕷️ BlackVenom</h1>
<p align="center"><b>Custom Payload Framework</b> — FUD'a yakın, şık ve ölümcül sızma aracı</p>

---

## 🐍 Nedir Bu?

**BlackVenom**, pentesterlar ve CTF meraklıları için hazırlanmış, Python & Shell tabanlı özel bir **payload üretici, obfuscator ve listener** framework'üdür.  
FUD'a yaklaşmayı hedefleyen yapısıyla, güvenlik testlerinde stealth modda saldırı imkanı sunar.

---

## 🚀 Özellikler

- 🎯 **Platform Seçimi:** Linux, Windows, Custom
- 🧪 **Payload Generator:** bash, nc, powershell, python, perl
- 🕵️‍♂️ **Encode & Obfuscation:** base64, xor, AES, random bash vars
- 💧 **Stager Oluşturucu:** curl | bash tarzı minimal tetikleyiciler
- 🛰️ **Listener:** BlackVenom içinde çalışan özel Python listener
- 📡 **venom.sh:** Shell üzerinden hızlı payload üretimi & dinleyici
- 🧾 **Loglama Sistemi:** Tüm operasyonlar kayda geçer

---

## 🔧 Kurulum

> Gereksinimler:
- Python 3.6+
- `pycryptodome` (AES için)

```bash
pip install pycryptodome
chmod +x venom.sh

GUI Tarzı Python Arayüz (BlackVenom.py):

python3 BlackVenom.py

Shell Terminal Aracı (venom.sh):

./venom.sh

		Proje Yapısı

BlackVenom/
├── payloads/         → Shell script üreticileri
├── encoders/         → Obfuscation modülleri
├── stagers/          → Mini tetikleyiciler
├── core/             → Ana mantık modülleri
├── utils/            → Log ve yapılandırmalar
├── BlackVenom.py     → Ana Python scripti
├── venom.sh          → Shell aracı
└── README.md


		❗ Uyarı

Bu araç sadece eğitim ve yetkili güvenlik testleri için kullanılmalıdır. Geliştiriciler, kötüye kullanım durumlarında sorumluluk kabul etmez.


