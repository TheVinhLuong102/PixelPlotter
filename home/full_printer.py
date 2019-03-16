#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os, time,sys
import glob
import printer
sys.stdout.buffer.write(chr(9986).encode('utf8'))

print("Click on each button to control the printer(s).\nOnce you click on a button, be patient. The command will take a moment. \nYou will be notified once finished (~10 seconds).")
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
        os.system('convert /var/www/html/uploads/'+added[x]+' -rotate 90 -negate -flop -resize 132 -monochrome print.png')
        save = added[x]
        added[x] = 'print.png'
        added[x] = added[x].replace (" ", "\ ")
      if "photo" in name:
        print("Processing...")
        os.system('convert "/var/www/html/uploads/'+added[x]+'" -negate -flop -resize 132 -monochrome print.png')
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
