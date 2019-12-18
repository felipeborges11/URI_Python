from PIL import Image, ImageFilter
#Read image
im = Image.open( 'img/1021.jpg' )
#Display image
im.show()

valor = float(input())
valor +=0.001
cem = valor // 100
cinquenta = (valor - cem * 100) // 50
vinte = (valor - cem * 100 - cinquenta * 50) // 20
dez = (valor - cem * 100 - cinquenta * 50 - vinte * 20) // 10
cinco = (valor - cem * 100 - cinquenta * 50 - vinte * 20 - dez * 10) // 5
dois = (valor - cem * 100 - cinquenta * 50 - vinte * 20 - dez * 10 - cinco * 5) // 2
um = (valor - cem * 100 - cinquenta * 50 - vinte * 20 - dez * 10 - cinco * 5 - dois * 2)
moeda = valor % 1
cinquenta_moeda = moeda // 0.50
vinteCinco_moeda = (moeda - (cinquenta_moeda * 0.50)) // 0.25
dez_moeda = (moeda - (cinquenta_moeda * 0.50) - vinteCinco_moeda * 0.25) // 0.10
cinco_moeda = (moeda - (cinquenta_moeda * 0.50) - vinteCinco_moeda * 0.25 - dez_moeda * 0.10) // 0.05
um_moeda = (moeda - (cinquenta_moeda * 0.50) - vinteCinco_moeda * 0.25 - dez_moeda * 0.10 - cinco_moeda * 0.05) // 0.01
print('NOTAS:')
print('%d nota(s) de R$ 100.00' %cem)
print('%d nota(s) de R$ 50.00' %cinquenta)
print('%d nota(s) de R$ 20.00' %vinte)
print('%d nota(s) de R$ 10.00' %dez)
print('%d nota(s) de R$ 5.00' %cinco)
print('%d nota(s) de R$ 2.00' %dois)
print('MOEDAS:')
print('%d moeda(s) de R$ 1.00' %um)
print('%d moeda(s) de R$ 0.50' %cinquenta_moeda)
print('%d moeda(s) de R$ 0.25' %vinteCinco_moeda)
print('%d moeda(s) de R$ 0.10' %dez_moeda)
print('%d moeda(s) de R$ 0.05' %cinco_moeda)
print('%d moeda(s) de R$ 0.01' %um_moeda)