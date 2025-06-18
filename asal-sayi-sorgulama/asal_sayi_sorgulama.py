def asal_sayi_mi(sayi):
    if (sayi > 1):
        for i in range(2, sayi):
            if (sayi % i == 0):
                return False
        return True
    else:
        return False

while True:
    if(asal_sayi_mi(int(input("Bir sayı girin : ")))):
        print("Girdiğiniz sayı asaldır\n")

    else:
        print("Girdiğiniz sayı asal değildir\n")