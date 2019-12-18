from PIL import Image, ImageFilter
#Read image
im = Image.open( 'img/1018.jpg' )
#Display image
im.show()

valor = int(input())
cem = valor // 100
cinquenta = (valor - cem * 100) // 50
vinte = (valor - cem * 100 - cinquenta * 50) // 20
dez = (valor - cem * 100 - cinquenta * 50 - vinte * 20) // 10
cinco = (valor - cem * 100 - cinquenta * 50 - vinte * 20 - dez * 10) // 5
dois = (valor - cem * 100 - cinquenta * 50 - vinte * 20 - dez * 10 - cinco * 5) // 2
um = (valor - cem * 100 - cinquenta * 50 - vinte * 20 - dez * 10 - cinco * 5 - dois * 2)
print('NOTAS:')
print('%d nota(s) de R$ 100,00' %cem)
print('%d nota(s) de R$ 50,00' %cinquenta)
print('%d nota(s) de R$ 20,00' %vinte)
print('%d nota(s) de R$ 10,00' %dez)
print('%d nota(s) de R$ 5,00' %cinco)
print('%d nota(s) de R$ 2,00' %dois)
print('%d nota(s) de R$ 1,00' %um)