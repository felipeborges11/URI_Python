from PIL import Image, ImageFilter
#Read image
im = Image.open( 'img/1013.jpg' )
#Display image
im.show()

arr = input()
lista = list(map(int,arr.split(' ')))
MaiorAB = (lista[0] + lista[1] + abs(lista[0] - lista[1])) / 2
MaiorTodos = (lista[2] + MaiorAB  + abs(lista[2] - MaiorAB)) / 2
print('%d eh o maior' %MaiorTodos)