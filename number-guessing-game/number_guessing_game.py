import random
import time

print("""=======================
Sayı Tahmin Etme Oyunu
=======================

[1] Kolay (1-10)
[2] Orta (1-50)
[3] Zor (1-100)
""")

secim = input("Zorluk seviyesini seçin: ")

zorluk_seviyeleri = {
    "1": (1, 10),
    "2": (1, 50),
    "3": (1, 100)
}

if secim in zorluk_seviyeleri:
    alt_sinir, ust_sinir = zorluk_seviyeleri[secim]
    sayi_sec = random.randint(alt_sinir, ust_sinir)

    while True:
        tahmin = int(input("Tahmin: "))

        if tahmin == sayi_sec:
            print("""
------------
Kazandın!
------------""")
            time.sleep(3)
            quit()

        if sayi_sec < tahmin:
            print("Seçilen sayı tahmin ettiğin sayıdan küçük.\n")

        if sayi_sec > tahmin:
            print("Seçilen sayı tahmin ettiğin sayıdan büyük.\n")
