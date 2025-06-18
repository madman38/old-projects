import random, os, cv2
from PIL import Image, ImageFont, ImageDraw

characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

while True:
    while True:
        result = ""

        for i in range(6):
            generate = random.choice(characters)
            result = result + generate

        card = Image.open("backgrounds/" + random.choice(["t1.png", "t2.png", "t3.png"]))

        draw = ImageDraw.Draw(card)
        font = ImageFont.truetype("fonts/" + random.choice(["f1.ttf"]), random.randint(50,80))

        draw.text((random.randint(20, 313), random.randint(30, 105)), result, (153, 146, 145), font = font)

        card.save("card.png")

        image = cv2.imread("card.png")

        os.remove("card.png")

        os.system("cls")

        print("""==============
Bot Doğrulama
==============

Not: Yeniden kod oluşturulmasını istiyorsanız Enter tuşuna basın.
""")

        cv2.imshow("CAPTCHA", image)
        cv2.waitKey(1)
        x = input("Resimde gördüğünüz kodu yazın: ")
        x = x.lower()

        if x == "":
            break

        if x == result:
            input("Doğru!\n\nYeniden yapmak için Enter tuşuna basın.")

        else:
            input("Yanlış!\n\nYeniden denemek için Enter tuşuna basın.")