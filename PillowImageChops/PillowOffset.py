from PIL import Image
from PIL import ImageChops

im1 = Image.open("origin.jpg")
# return a copy of the image with pixel offset
im = ImageChops.offset(im1,0,50)
im.show()