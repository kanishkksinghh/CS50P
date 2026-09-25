import sys

from PIL import image

images = []

for arg in sys.argv:
    image = Image.open(arg)
    image.append(image)
    
images[0].save(
    "costumes.gif", save_all=True, append_images=[images[1]], duartion=200, loop=0
    )