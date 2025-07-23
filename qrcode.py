# import qrcode
# img = qrcode.make(
#     "https://www.youtube.com/embed/p2EdDiiVHh4?si=wYi_sZDvVss3u05A"
# )
# img.save('myQRcode.png')
# img.show

# basic_qrcode.py

# import segno

# qrcode = segno.make_qr("Hello, World")
# qrcode.save("basic_qrcode.png")

import pyqrcode
from pyqrcode import QRCode
s = "https://www.youtube.com/embed/16fl0l4I2No?si=neCQ2gcENR-p_cKH" 
url = pyqrcode.create(s)
url.svg("instasamka.svg", scale=10)
