#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os, time,sys
import glob
import printer
sys.stdout.buffer.write(chr(9986).encode('utf8'))

print("Welcome to Pixel Plotter. To print, use the web interface by connecting via USB or Bluetooth and opening a web browser to http://192.168.0.1/.")
print("Images to print:")
l = 0

z = 0
path_to_watch = "/var/www/html/uploads"
before = dict ([(f, None) for f in os.listdir (path_to_watch)])

while 1:
  sys.stdout.flush()
  time.sleep (2)
  after = dict ([(f, None) for f in os.listdir (path_to_watch)])
  added = [f for f in after if not f in before]
  removed = [f for f in before if not f in after]
  if added:
    x=0
    while x != len(added):
      z = z+1
      print(added[x])
      name = added[x]
      if "pi" in name or "mono" in name:
#        os.system('convert /var/www/html/uploads/'+added[x]+' -rotate 90 -negate -flop -monochrome print.png')
        os.system('convert /var/www/html/uploads/'+added[x]+' -rotate 90 -negate -resize 132 -monochrome print.png')
        save = added[x]
        added[x] = 'print.png'
        added[x] = added[x].replace (" ", "\ ")
      if "photo" in name:
        print("Processing...")
        os.system('convert "/var/www/html/uploads/'+added[x]+'" -negate -resize 132 -monochrome print.png')
#        os.system('convert "/var/www/html/uploads/'+added[x]+'" -negate -flop -monochrome print.png')
        save = added[x]
        added[x] = 'print.png'
        added[x] = added[x].replace (" ", "\ ")
      if "color" in name:
        os.system('cp "/var/www/html/uploads/'+added[x]+'" print.png')
        save = added[x]
        added[x] = 'print.png'
        added[x] = added[x].replace (" ", "\ ")
      x = x + 1
      printer.printer("print.png")
    before = after
