import os
list = os.listdir("fullscreen")
files = []
for line in list:
  if line.find('.res.')<0:
    files.append(line)
for fid in range(len(files)):
  f = open("pages/"+files[fid]+".html","w")
  prev = "#"
  if fid > 0:
    prev = files[fid-1]+".html"
  next = "#"
  if fid < len(files)-1:
    next = files[fid+1]+".html"
  f.write('''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
<head>
<title>Water Color Result</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<link rel="stylesheet" href="main.css" type="text/css" media="screen" charset="utf-8" />
</head>
<body>
<div class="main">
<div class="block">
<center><a href="../index.html" alt="back to home"><span class="ui-icon ui-icon-home"/></a></center>
</div>
<div class="block">
<center><img style="padding:5px;border:1px dashed #021a40" src="../fullscreen/'''+files[fid]+'''.res.png" class="domroll ../fullscreen/'''+files[fid]+'''">
</center>
</div>
<div class="block">
<div style="width:20%;float:left;"><a href="'''+prev+'''"><span class="ui-icon ui-icon-back" style="float:right"/></a></div>
<div style="width:60%;float:left;"><center><p>'''+files[fid]+'''</p></center></div>
<div style="width:20%;float:left;"><a href="'''+next+'''"><span class="ui-icon ui-icon-forward"/></a></div>
</center>
</div>
</div>

<script src="dom_image_rollover_hover.js">
</script>
</body>
</html>''')
  f.close()
