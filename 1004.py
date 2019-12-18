from PIL import Image, ImageFilter
#Read image
im = Image.open( 'img/1004.jpg' )
#Display image
im.show()

A = int(input())
B = int(input())
PROD = A * B
print('PROD =', PROD)