from PIL import Image
from PIL import ImageChops

im1 = Image.new("RGB",(300,300))
# Fill a channel with a given grey level.
im = ImageChops.constant(im1,240)
im.show()