from PIL import Image, ImageFilter
#Read image
im = Image.open( 'img/1012.jpg' )
#Display image
im.show()

arr = input()
l = list(map(float,arr.split(' ')))
print('TRIANGULO: %0.3f' %(l[0] * l[2] / 2))
print('CIRCULO: %0.3f' %(l[2] * l[2] * 3.14159))
print('TRAPEZIO: %0.3f' %((l[0] + l[1]) * l[2] / 2))
print('QUADRADO: %0.3f' %(l[1] * l[1]))
print('RETANGULO: %0.3f' %(l[0] * l[1]))