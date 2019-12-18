from PIL import Image, ImageFilter
im = Image.open('img/1036.jpg')
im.show()

import math
arr = input()
var = list(map(float,arr.split(' ')))
A = var[0]
B = var[1]
C = var[2]
if ((B ** 2 - 4 * A * C) >= 0 and A != 0.0):
    print('R1 = %0.5f' %((-B + math.sqrt(B ** 2 - 4 * A * C)) / (2 * A)))
    print('R2 = %0.5f' %((-B - math.sqrt(B ** 2 - 4 * A * C)) / (2 * A)))
else:
    print('Impossivel calcular')