from PIL import Image, ImageFilter
#Read image
im = Image.open( 'img/1019.jpg' )
#Display image
im.show()

N = int(input())
hora = N // 3600
minutos = (N - (hora * 3600)) // 60
segundos = (N - (hora * 3600 + minutos * 60)) // 1
print('%d:%d:%d'%(hora,minutos,segundos))