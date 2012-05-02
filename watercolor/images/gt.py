import os
import Image
list = os.listdir("fullscreen")
for line in list:
  if line.find('.res.')>=0:
    im = Image.open("fullscreen/"+line)
    im.thumbnail((60,60),Image.ANTIALIAS)
    im.save("thumbnails/"+line)
