from PIL import Image, ImageFilter
#Read image
im = Image.open( 'img/1001.jpg' )
#Display image
im.show()

num1 = int(input())
num2 = int(input())
 
print ('X =', num1/num2)