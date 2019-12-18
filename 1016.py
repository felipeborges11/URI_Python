from PIL import Image, ImageFilter
#Read image
im = Image.open( 'img/1016.jpg' )
#Display image
im.show()

distancia = int(input())
print('%d minutos' %(distancia * 2))