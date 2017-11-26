from PIL import Image

# The second image. Must have the same mode and size as the first image.

im1 = Image.new("RGBA",(500,541),"yellow")
im2 = Image.open("origin.png")

im = Image.alpha_composite(im1,im2)

im.show()