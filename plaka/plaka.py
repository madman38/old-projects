import os

def cls():
    os.system("cls")

def label():
    print("""=====================
Şehir - Plaka bulucu
=====================
""")

plaka = {1: 'adana', 2: 'adıyaman', 3: 'afyonkarahisar', 4: 'ağrı', 5: 'amasya', 6: 'ankara', 7: 'antalya', 8: 'artvin', 9: 'aydın', 10: 'balikesir', 11: 'bilecik', 12: 'bingöl', 13: 'bitlis', 14: 'bolu', 15: 'burdur', 16: 'bursa', 17: 'çankkale', 18: 'çankırı', 19: 'çorum', 20: 'denizli', 21: 'diyarbakır', 22: 'edirne', 23: 'elazığ', 24: 'erzincan', 25: 'erzurum', 26: 'eskişehir', 27: 'gaziantep', 28: 'giresun', 29: 'gümüşhane', 30: 'hakkari', 31: 'hatay', 32: 'isparta', 33: 'mersin', 34: 'istanbul', 35: 'izmir', 36: 'kars', 37: 'kastamonu', 38: 'kayseri', 39: 'kırklareli', 40: 'kırşehir', 41: 'kocaeli', 42: 'konya', 43: 'kütahya', 44: 'malatya', 45: 'manisa', 46: 'kahramanmaraş', 47: 'mardin', 48: 'muğla', 49: 'muş', 50: 'nevşehir', 51: 'niğde', 52: 'ordu', 53: 'rize', 54: 'sakarya', 55: 'samsun', 56: 'siirt', 57: 'sinop', 58: 'sivas', 59: 'tekirdağ', 60: 'tokat', 61: 'trabzon', 62: 'tunceli', 63: 'şanlıurfa', 64: 'uşak', 65: 'van', 66: 'yozgat', 67: 'zonguldak', 68: 'aksaray', 69: 'bayburt', 70: 'karaman', 71: 'kırıkkale', 72: 'batman', 73: 'şırnak', 74: 'bartın', 75: 'ardahan', 76: 'iğdır', 77: 'yalova', 78: 'karabük', 79: 'kilis', 80: 'osmaniye', 81: 'düzce'}
plaka2 = {'adana': 1, 'adıyaman': 2, 'afyonkarahisar': 3, 'ağrı': 4, 'amasya': 5, 'ankara': 6, 'antalya': 7, 'artvin': 8, 'aydın': 9, 'balikesir': 10, 'bilecik': 11, 'bingöl': 12, 'bitlis': 13, 'bolu': 14, 'burdur': 15, 'bursa': 16, 'çankkale': 17, 'çankırı': 18, 'çorum': 19, 'denizli': 20, 'diyarbakır': 21, 'edirne': 22, 'elazığ': 23, 'erzincan': 24, 'erzurum': 25, 'eskişehir': 26, 'gaziantep': 27, 'giresun': 28, 'gümüşhane': 29, 'hakkari': 30, 'hatay': 31, 'isparta': 32, 'mersin': 33, 'istanbul': 34, 'izmir': 35, 'kars': 36, 'kastamonu': 37, 'kayseri': 38, 'kırklareli': 39, 'kırşehir': 40, 'kocaeli': 41, 'konya': 42, 'kütahya': 43, 'malatya': 44, 'manisa': 45, 'kahramanmaraş': 46, 'mardin': 47, 'muğla': 48, 'muş': 49, 'nevşehir': 50, 'niğde': 51, 'ordu': 52, 'rize': 53, 'sakarya': 54, 'samsun': 55, 'siirt': 56, 'sinop': 57, 'sivas': 58, 'tekirdağ': 59, 'tokat': 60, 'trabzon': 61, 'tunceli': 62, 'şanlıurfa': 63, 'uşak': 64, 'van': 65, 'yozgat': 66, 'zonguldak': 67, 'aksaray': 68, 'bayburt': 69, 'karaman': 70, 'kırıkkale': 71, 'batman': 72, 'şırnak': 73, 'bartın': 74, 'ardahan': 75, 'iğdır': 76, 'yalova': 77, 'karabük': 78, 'kilis': 79, 'osmaniye': 80, 'düzce': 81}

while True:
    while True:
        cls()
        label()

        veri = input("Bir plaka kodu veya bir şehir adı girin: ")
        veri = veri.lower()

        cls()
        label()

        if veri == "":
            break

        try:
            veri = int(veri)

            if veri > 81 or veri < 1:
                input("Hata! Plaka numarası 1 ile 81 arasında olmalıdır.\n\nGeri dönmek için Enter tuşuna basın.")
                break

            input(f"{veri} numaralı şehrimizin adı: {plaka[veri].capitalize()}\n\nYeniden başlatmak için Enter tuşuna basın.")
            break

        except:
            if veri not in plaka2:
                input("Hata! Girdiğiniz şehir Türkiye'de bulunmamaktadır. Yazım yanlışı yapmış olabilir misiniz?\n\nGeri dönmek için Enter tuşuna basın.")
                break

            input(f"{veri.capitalize()} isimli şehrimizin plakası: {plaka2[veri]}\n\nYeniden başlatmak için Enter tuşuna basın.")
            break
