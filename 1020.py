from PIL import Image, ImageFilter
#Read image
im = Image.open( 'img/1020.jpg' )
#Display image
im.show()

tempo = int(input())
ano = tempo // 365
mes = (tempo - ano * 365) // 30
dia = (tempo - (ano * 365 + mes * 30))
print('%d ano(s)' %ano)
print('%d mes(es)' %mes)
print('%d dia(s)' %dia)