from Adafruit_Thermal import *
import Image, urllib, os, sys

API = 'http://localhost:9911'
CAPFILE = 'capture.png'

try:
  urllib.urlopen(API + '/cap')
except IOError:
  print "Could not reach API ({API})".format(API=API)
  sys.exit()

if os.path.isfile(CAPFILE):
  os.remove(CAPFILE)

# Get newly captured capture
urllib.urlretrieve(API + '/' + CAPFILE, CAPFILE)  

# Get the printer ready
printer = Adafruit_Thermal("/dev/ttyAMA0", 19200, timeout=5)

# Open 'CAPFILE' and print it
img = Image.open(CAPFILE)
printer.printImage(img, True)
printer.feed(4)