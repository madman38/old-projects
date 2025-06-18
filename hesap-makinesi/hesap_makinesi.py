import os

def cls():
    os.system("cls")

while True:
    print("""===============
Hesap Makinesi
===============

[1] Toplama
[2] Çıkarma
[3] Çarpma
[4] Bölme
[5] Üssünü al
""")
    veri = input("Yapmak istediğiniz işlemi seçin: ")
    cls()

    if veri == "1":
        cls()
        print("""========
Toplama
========
""")
        x = input("1. sayı: ")
        x = float(x)
        y = input("2. sayı: ")
        y = float(y)
        input(f"\nSonuç: {x+y}\nYeniden başlatmak için Enter tuşuna basın.")

    elif veri == "2":
        cls()
        print("""========
Çıkarma
========
""")
        x = input("1. sayı: ")
        x = float(x)
        y = input("2. sayı: ")
        y = float(y)
        input(f"\nSonuç: {x-y}\nYeniden başlatmak için Enter tuşuna basın.")

    elif veri == "3":
        cls()
        print("""=======
Çarpma
=======
""")
        x = input("1. sayı: ")
        x = float(x)
        y = input("2. sayı: ")
        y = float(y)
        input(f"\nSonuç: {x*y}\nYeniden başlatmak için Enter tuşuna basın.")

    elif veri == "4":
        cls()
        print("""======
Bölme
======
""")
        x = input("1. sayı: ")
        x = float(x)
        y = input("2. sayı: ")
        y = float(y)
        input(f"\nSonuç: {x/y}\nYeniden başlatmak için Enter tuşuna basın.")

    elif veri == "5":
        cls()
        print("""============
Üssünü alma
============
""")
        x = input("1. sayı: ")
        x = float(x)
        y = input("2. sayı: ")
        y = float(y)
        input(f"\nSonuç: {x**y}\nYeniden başlatmak için Enter tuşuna basın.")