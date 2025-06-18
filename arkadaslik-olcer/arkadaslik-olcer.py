import random
import time

print("""
=================
ARKADAŞLIK ÖLÇER
=================
""")

while True:
        isim = input("Adın: ")

        isim2 = input("Arkadaşının adı: ")

        print("Arkadaşlığınızın yakınlığını ölçmek için Enter tuşuna basın.")

        enter = input()

        if enter == "":
                print("Hesaplanıyor...")
                time.sleep(2)

                sayi = random.randint(0,100)

                print(isim, "♥", "%", sayi, "♥", isim2)

                print("""
Arkadaşlık seviyenin açıklamasını kontrol etmek için 1,
Yeni oyuna geçmek için Enter tuşuna basın.
""")
                secim = input()

                if secim == "1":print("""
0-20: Çok kötü. Gerçekten arkadaş olduğunuza emin misin?

21-40: Kötü. Sanırım arkadaşınla az görüşüyorsun.

41-60: Orta derece. Arkadaşın olabilir ama bir dost kadar yakının değil.

61-80: İyi. Muhtemelen ikiniz de birbirinizi yakın arkadaş görüyorsunuz.

81-100: Çok iyi. İkiniz birbirinizin dostusunuz ve uzun zamanlar boyunca arkadaş olarak kalacaksınız.
""")

                if secim == "2":
                        print("\n")
