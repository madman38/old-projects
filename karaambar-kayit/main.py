from PIL import Image, ImageFont, ImageDraw
import random


img = Image.open("assets/template.jpg")
font = ImageFont.truetype("assets/calibri-regular.ttf", 11)

draw = ImageDraw.Draw(img)

name = input("Adın: ")
surname = input("Soyadın: ")

number = f"{random.randint(0, 999):05}"

draw.text((44,108), name, (0, 0, 0), font=font)
draw.text((65,118), surname, (0,0,0), font=font)
draw.text((68,128), number, (0,0,0), font=font)

im2 = Image.open("assets/image.png")
img.paste(im2.resize((63, 88)), (171, 52))

img.save("card.png")

print("\nBaşarıyla kayıt oldunuz!")

close = input("Programı kapatmak için Enter tuşuna basın.")

if close == "":
    quit()
