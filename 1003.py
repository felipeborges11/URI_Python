from PIL import Image, ImageFilter
#Read image
im = Image.open( 'img/1003.jpg' )
#Display image
im.show()

A = int(input())
B = int(input())
SOMA = A + B
print('SOMA =', SOMA)