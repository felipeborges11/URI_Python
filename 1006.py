from PIL import Image, ImageFilter
#Read image
im = Image.open( 'img/1006.jpg' )
#Display image
im.show()

A = float(input())
B = float(input())
C = float(input())
MEDIA = (A * 2 + B * 3 + C * 5)/10
print('MEDIA = %0.1f' %MEDIA)