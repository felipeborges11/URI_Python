from PIL import Image, ImageFilter
#Read image
im = Image.open( 'img/1009.jpg' )
#Display image
im.show()

vendedor = input()
salario = float(input())
montante = float(input())
print('TOTAL = R$ %.02f' %(salario +  15 / 100 * montante))