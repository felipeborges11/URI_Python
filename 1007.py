from PIL import Image, ImageFilter
#Read image
im = Image.open( 'img/1007.jpg' )
#Display image
im.show()

A = int(input())
B = int(input())
C = int(input())
D = int(input())
DIFERENCA = A * B - C * D
print('DIFERENCA =', DIFERENCA)