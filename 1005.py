from PIL import Image, ImageFilter
#Read image
im = Image.open( 'img/1005.jpg' )
#Display image
im.show()

A = float(input())
B = float(input())
MEDIA = (A * 3.5 + B * 7.5)/11
print('MEDIA = %0.5f' %MEDIA)