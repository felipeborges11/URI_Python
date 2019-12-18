from PIL import Image, ImageFilter
#Read image
im = Image.open( 'img/1015.jpg' )
#Display image
im.show()

import math
arr = input()
p1 = list(map(float,arr.split(' ')))
arr2 = input()
p2 = list(map(float,arr2.split(' ')))
print('%0.4f' %(math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)))