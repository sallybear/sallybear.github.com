import os
list = os.listdir("fullscreen")
files = []
for line in list:
  if line.find('.res.')<0:
    print '<li><a href="pages/'+line+'.html"><img src="thumbnails/'+line+'.res.png" alt="" /></a></li>'
