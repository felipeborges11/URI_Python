from PIL import Image, ImageFilter
#Read image
im = Image.open( 'img/1002.jpg' )
#Display image
im.show()
R = float(input())
print('A=%0.4f' %(R*R*3.14159))
