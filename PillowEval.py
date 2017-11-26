from PIL import Image
im = Image.open("origin.jpg")
im2 = Image.eval(im , lambda px:px/5)
im2.show();