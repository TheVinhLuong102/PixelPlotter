import glob,os,time,sys
import os.path
from lockfile import LockFile
ip = "192.168.150.3"
print "hicr2"
while True:
  sys.stdout.flush()
#  print "color: waiting for lock"
#  print "color: got lock"
  time.sleep(5)
  array = sorted(glob.glob("color/*.png"))
  if array != []:
   print array[0]
   os.system('rm "'+array[0]+'"')
   print "COL2 Activated"
   time.sleep(0)
   lock2 = LockFile("lockcolor2/lock")
   print "waiting for 2MONOCHROME"
   sys.stdout.flush()
   name = array[0].split('-')[1]
   print name
   lock2.acquire()
   print "2COLOR ACTIVATED"
   sys.stdout.flush()
   os.system('cp "/var/www/html/uploads/'+name+'" image.jpg')
   os.system('cp "/var/www/html/uploads/'+name+'" imagetest.jpg')
   os.system('python print.py image.jpg')
   lock2.release()
   print "done"
