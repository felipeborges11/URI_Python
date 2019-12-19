from PIL import Image, ImageFilter
im = Image.open('img/1036.jpg')
im.show()

arr = input()
var = list(map(float,arr.split(' ')))
if var[0] == 1:
    print('Total: R$ %0.2f' %(4.00 * var[1]))
elif var[0] == 2:
    print('Total: R$ %0.2f' %(4.50 * var[1]))
elif var[0] == 3:
    print('Total: R$ %0.2f' %(5.00 * var[1]))
elif var[0] == 4:
    print('Total: R$ %0.2f' %(2.00 * var[1]))
elif var[0] == 5:
    print('Total: R$ %0.2f' %(1.50 * var[1]))