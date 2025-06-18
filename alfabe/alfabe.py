import os
import random

def cls():
    os.system("cls")

def label():
    print("""===============
Alfabe listesi
===============
""")

alfabe = ['a', 'b', 'c', 'ç', 'd', 'e', 'f', 'g', 'ğ', 'h', 'ı', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'ö', 'p', 'r', 's', 'ş', 't', 'u', 'ü', 'v', 'y', 'z']

cls()
label()

harf = input("Harf: ")

while True:
    while True:
        cls()
        label()

        harf = harf.lower()
        cls()
        label()

        if harf == "":
            harf = random.choice(alfabe)

        if harf not in alfabe:
            input("Hata! Girdiğiniz karakter(ler) Türkçe alfabesinde bulunmuyor.\n\nGeri dönmek için Enter tuşuna basın.")
            break

        if len(harf) > 1:
            input("Hata! Aynı anda sadece bir harf tanımlayabilirsiniz.\n\nGeri dönmek için Enter tuşuna basın.")
            break

        print(f"{harf.upper()} harfi alfabenin {alfabe.index(harf)+1}. sırasındadır.\n")
        harf = input("Harf: ")