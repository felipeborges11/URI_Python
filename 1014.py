from PIL import Image, ImageFilter
#Read image
im = Image.open( 'img/1014.jpg' )
#Display image
im.show()

X = int(input())
Y = float(input())
print('%0.3f km/l' %(X / Y))