import random
import os

def cls():
    os.system("cls")

def label():
    print("""===========
Kura Çekme
===========

NOT: "bitti" yazıp Enter'a basarak kura çekmeyi sonlandırabilirsiniz.""")

list = []
label()
while True:
    listrange = len(list)
    add = str(input("\nisim: "))
    list.append(add)
    cls()
    label()
    print(f"\n{add} listeye eklendi. Güncel liste:\n{list}")

    if add == "":
        cls()
        label()
        list.remove("")
        print(f"\nBoşluk listeye eklenemez. Seçim kaldırıldı. Güncel liste:\n{list}")

    if add == "bitti".lower():
        list.remove("bitti")
        cls()
        for repeats in range(listrange):
            cls()
            x = random.choice(list)
            list.remove(x)
            label()
            input(f"\nÇıkan kişi: {x}\n\nGüncel liste:\n{list}\n\nDöndürmek için Enter tuşuna basın.\n")
            cls()
            label()