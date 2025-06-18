import qrcode

print("""
==============
QR Code Maker
==============
""")

link = input("Link: ")
result = str(link)
image = qrcode.make(result)
image.save("qrcode.png")