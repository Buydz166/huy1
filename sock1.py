import os

print("""
\x1b[38;2;255;20;147m HỆ THỐNG KHỞI ĐỘNG THIẾT BỊ !
\x1b[38;2;255;20;147m MÃ HÓA
\x1b[38;2;255;20;147m MỘT SỐ INFO \x1b[38;2;0;255;58m>( Ddos By Code Tuan Anh?)
\x1b[38;2;0;255;58m>( MUSILA VER 4.5 ADR)
\x1b[38;2;255;20;147m╔═╦═╗ ╔═╦═╗ ╔═╦═╗ ╔═╦═╗ ╔═╦═╗
\x1b[38;2;255;20;147m -Facebook : https://www.facebook.com/xxxj8          
\x1b[38;2;255;20;147m -Zalo : 0834446837
\x1b[38;2;255;20;147m -Info Cụ Thể : https://thanhtoan1s.com/Inftuanah
\x1b[38;2;255;20;147m -Discord Ddos : https://discord.gg/rAntGKQv
\x1b[38;2;255;20;147m ╚╩═╩╝ ╚╩═╩╝ ╚╩═╩╝ ╚╩═╩╝ ╚╩═╩╝
""") 

print("""[0] pip\n[1] pip3\CHON {1}?""")

c = input(">>>: ")
if c == "0":
    os.system("pip install cloudscraper")
    os.system("pip install socks")
    os.system("pip install pysocks")
    os.system("pip install colorama")
    os.system("pip install undetected_chromedriver")
    os.system("pip install httpx")

elif c == "1":
    os.system("pip3 install cloudscraper")
    os.system("pip3 install socks")
    os.system("pip3 install pysocks")
    os.system("pip3 install colorama")
    os.system("pip3 install undetected_chromedriver")
    os.system("pip3 install httpx")
if os.name == "nt":
    pass
else:
    os.system("wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb")
    os.system("apt-get install ./google-chrome-stable_current_amd64.deb")

print("KHỞI ĐỘNG FIE TOOL VÀ CHẠY.")
