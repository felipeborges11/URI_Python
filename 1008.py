from PIL import Image, ImageFilter
#Read image
im = Image.open( 'img/1008.jpg' )
#Display image
im.show()

num_funcionario = int(input())
num_trabalhada = int(input())
qtd_horas_trabalhadas = float(input())
print('NUMBER =', num_funcionario)
print('SALARY = U$ %.02f' %(num_trabalhada * qtd_horas_trabalhadas))