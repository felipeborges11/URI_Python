from PIL import Image, ImageFilter
#Read image
im = Image.open( 'img/1011.jpg' )
#Display image
im.show()

R = int(input())
print('VOLUME = %0.3f' %(4.0/3*3.14159*R**3))