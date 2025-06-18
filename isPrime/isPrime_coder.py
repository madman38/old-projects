import time

def isPrime(sayi):
    if (sayi > 1):
        for i in range(2, sayi):
            if (sayi % i == 0):
                return False
        return True
    else:
        return False

def checkpoint():
    try:
        file = open("isPrime.py", "r")
        checkpoint = len(file.readlines())-1
        file.close()
        return checkpoint
    except:
        file = open("isPrime.py", "w")
        file.write("sayi = int(input('sayi gir: '))\n")
        file.close()

checkpoint()
cont = int(checkpoint())

gamer = int(input(f"Toplam eklenen satır sayısı: {cont}\nprograma kaç numara ekleneceğini gir: "))
print("DO NOT PANIC IF IT LOOKS STUCK")

file = open("isPrime.py", "a")

time1 = time.time()
for i in range(gamer):
    if isPrime(cont+i+1): result = "Girdiginiz sayi asaldir"
    else: result = "Girdiginiz sayi asal degildir"
    file.write(f"if sayi == {cont+i+1}: print('{result}')\n")

time2 = time.time()
res_time = time2-time1

try: ratio = round(gamer/res_time, 1)
except: ratio = "*programın hızını hesap edemediği kadar fazla*"

input(f"\nprograma {gamer} satır kod eklendi! harcanan zaman: {(round(res_time, 1))} saniye - Bu, saniyede {ratio} satır kod demek!\n\nProgramı kapatmak için Enter tuşuna basın.")