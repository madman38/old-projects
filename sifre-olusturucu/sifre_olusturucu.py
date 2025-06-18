import random, os, colorama
from colorama import Fore

colorama.init(autoreset=True)

def cls():
    os.system("cls")

def label():
    print("""======================
Güçlü Şifre Oluşturma
======================
""")

characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '*', '!', '#', '?', '@', '.']

label()
length = int(input("Şifre uzunluğu: "))

while True:
    cls()
    label()

    password = ""

    for i in range(length):
        generated = random.choice(characters)

        try:
            zar = random.randint(0,1)

            if zar == 0:
                pass

            if zar == 1:
                generated = generated.upper()

        except:
            pass

        password = password + generated

    input(f"Şifreniz: {Fore.LIGHTBLUE_EX}{password}\n\n{Fore.WHITE}Yeniden oluşturmak için Enter tuşuna basın.")