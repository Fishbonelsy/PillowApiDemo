from PIL import Image
from PIL import ImageChops

im1 = Image.open("origin.jpg")
im2 = Image.open("origin2.jpg")
scale = 2.5
offset = 50
# pixel(im) = ( pixel(im1) + pixel(im2) ) / scale
im = ImageChops.add(im1,im2 , scale,offset)
im.show()