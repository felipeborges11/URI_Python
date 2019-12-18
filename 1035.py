from PIL import Image, ImageFilter
#Read image
im = Image.open( 'img/1035.jpg' )
#Display image
im.show()

arr = input()
var = list(map(int,arr.split(' ')))
A = var[0]
B = var[1]
C = var[2]
D = var[3]
if(B > C and D > A and (C + D) > (A + B) and C >= 0 and D >= 0 and A % 2 == 0):
    print('Valores aceitos')
else:
    print('Valores nao aceitos')D =