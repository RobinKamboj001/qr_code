# import qrcode 
# from PIL import Image
# import qrcode.constants

# qr = qrcode.QRCode(version=1, 
#                    error_correction=qrcode.constants.ERROR_CORRECT_H, 
#                    box_size=10, 
#                    border=4,)

# qr.add_data("http://markettown.in/")
# qr.make(fit=True)
# img = qr.make_image(fill_color="black", back_color="yellow")
# img.save("Web.png")


import qrcode
from PIL import Image
import qrcode.constants

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   border=4,
                   box_size=10)

qr.add_data("http://markettown.in/")
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="yellow")
img.save("Web.png")