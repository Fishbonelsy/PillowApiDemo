from PIL import Image
im = Image.open("origin.jpg")
R,G,B = im.split()
d = Image.merge("RGB",(R,G,B))
d.show()