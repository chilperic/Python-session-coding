import barcode
import pyqrcode
from barcode.writer import ImageWriter
ean = barcode.get('ean13', '123456789102', writer=ImageWriter())
filename = ean.save('ean13')
filename
u'ean13.png'


url = pyqrcode.create('http://uca.edu')
url.svg('christelle.png', scale=8)
print(url.terminal(quiet_zone=1))