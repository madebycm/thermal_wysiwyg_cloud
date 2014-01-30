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

urllib.urlretrieve(API + '/' + CAPFILE, CAPFILE)

printer = Adafruit_Thermal("/dev/ttyAMA0", 19200, timeout=5)

try:
  img = Image.open(CAPFILE)
  printer.printImage(img, True)
  printer.feed(4)
except IOError as e:
  print "I/O error ({0}): {1}".format(e.errno, e.strerror)
  print "(does " + CAPFILE + " exist?)"