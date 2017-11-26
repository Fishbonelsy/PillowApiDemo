from PIL import Image

# The second image. Must have the same mode and size as the first image.

im1 = Image.new("RGBA",(500,541),"yellow")
im2 = Image.open("origin.png")
# out = image1 * (1.0 - alpha) + image2 * alpha
im = Image.blend(im1,im2 , 0.9)

im.show()