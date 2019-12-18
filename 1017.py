from PIL import Image, ImageFilter
#Read image
im = Image.open( 'img/1017.jpg' )
#Display image
im.show()

tempo = int(input())
velocidade = int(input())
print('%0.3f' %(tempo * velocidade / 12))