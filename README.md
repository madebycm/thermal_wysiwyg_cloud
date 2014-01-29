thermal_wysiwyg_cloud
=====================

A WYSIWYG editor that prints pure HTML to a thermal printer, from the cloud. It works by using PhantomJS to headlessly generate a capture.png file from the markup which it then can print.

Example implementation using a simple shell script (after hosting the server):

```
#!/bin/sh
# generate the capture on backend
wget -O /dev/null http://localhost:9911/cap # this URL should be kept secret

# delete cache
rm -f capture.png

# get the new capture
wget http://sky.madebycm.no:9911/capture.png

# sky.py wils use this and print
python sky.py
```

Where sky.py looks like:
```
# https://github.com/adafruit/Python-Thermal-Printer
from Adafruit_Thermal import *
import Image

printer = Adafruit_Thermal("/dev/ttyAMA0", 19200, timeout=5)
img = Image.open('capture.png')

printer.printImage(img, True)
printer.feed(4)

# It's that simple!
```
