import random
import os
import sys
import colorama
from colorama import Fore

colorama.init(autoreset=True)

def cls():
    os.system("cls")

def label():
    print("""========
TOMBALA
========
""")

numaralar = [i+1 for i in range(100)]

kart1 = []
kartbot = []

while not len(kart1) == 15:
    generate = random.choice(numaralar)

    while generate not in kart1:
        kart1.append(generate)

while not len(kartbot) == 15:
    generate = random.choice(numaralar)

    while generate not in kartbot:
        kartbot.append(generate)

while True:
    while True:
        cls()

        if kart1 == [] and kartbot == []:
            input("==========\nBerabere!\n==========\n\nKapatmak için Enter tuşuna basın.")
            sys.exit(1)
            
        if kart1 == []:
            input("==========\nKazandın!\n==========\n\nKapatmak için Enter tuşuna basın.")
            sys.exit(1)
        
        if kartbot == []:
            input("===========\nKaybettin!\n===========\n\nKapatmak için Enter tuşuna basın.")
            sys.exit(1)

        label()
        print(f"Sen:\n{kart1}\n\nBot:\n{kartbot}")
        torba = random.choice(numaralar)
        numaralar.remove(torba)

        if torba in kart1 and torba in kartbot:
            kart1.remove(torba)
            kartbot.remove(torba)
            renk = Fore.LIGHTBLUE_EX

        elif torba in kart1:
            kart1.remove(torba)
            renk = Fore.GREEN

        elif torba in kartbot:
            kartbot.remove(torba)
            renk = Fore.RED

        else:
            renk = Fore.WHITE

        input(f"\nÇıkan sayı: {renk}{torba}{Fore.WHITE}\n\nSayı çekmek için Enter tuşuna basın.")