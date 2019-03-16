#!/usr/bin/python


import glob,os,time,sys
import os.path
from lockfile import LockFile
ip = "192.168.8.2"
print('hi2')
while True:
  sys.stdout.flush()
  lock = LockFile("lock/lock")
#  print "MONO:waiting for lock"
  time.sleep(0.5)
  lock.acquire()
#  print "got lock"
  time.sleep(5)
  array = sorted(glob.glob("files/*.png"))
  if array != []:
   sys.stdout.flush()
   print array[0]
   os.system('rm "'+array[0]+'"')
   lock.release()
   print "released and printing"
   time.sleep(0)
   lock2 = LockFile("lockcolor2/lock")
   print "waiting for COL2"
   sys.stdout.flush()
   name = array[0].split('-')[1]
   print name
   lock2.acquire()
   print "MONOCHROME ACTIVATED2"
   print "printmo2"
   sys.stdout.flush()
   os.system('cp /var/www/html/uploads/'+name.replace("\n", "?")+' ./image.jpg')
   os.system('python print.py image.jpg')
   lock2.release()
   print "done"
