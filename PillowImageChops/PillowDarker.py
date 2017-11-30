from PIL import Image
from PIL import ImageChops

im1 = Image.open("origin.jpg")
im2 = Image.open("origin2.jpg")

# pixel(im) = min(pixel(im1) , pixel(im2))
im = ImageChops.darker(im1,im2 )
im.show()