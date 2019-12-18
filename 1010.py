from PIL import Image, ImageFilter
#Read image
im = Image.open( 'img/1010.jpg' )
#Display image
im.show()

arr = input()
l = list(map(float,arr.split(' ')))
arr2 = input()
l2 = list(map(float,arr2.split(' ')))
print('VALOR A PAGAR: R$ %0.2f' %(l[1] * l[2] + l2[1] * l2[2]))