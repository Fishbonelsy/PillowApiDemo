from PIL import Image
im = Image.open("origin.jpg")
im.rotate(45).show()