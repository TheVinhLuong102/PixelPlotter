#!/usr/bin/python
# This is the converter between the LEGO Mindstorms EV3-G system Pixel Plotter API to the ev3dev Pixel Plotter API.
# To use, reference this file instead of the old ev3dev ssh commands
 
import os,time,sys
#os.system('python exec.py')
#os.system('python exec.py')
#os.system('python exec.py')

#while True:
print sys.argv[1]
if "mono" in sys.argv[1]:     
	print "sendandprint.py mono"
#	os.system('convert image.jpg -rotate 90 -negate -flop -resize 132 -monochrome image2.jpg;echo success')
#	os.system('convert image.jpg -rotate 90 -negate -flop -resize 132 -monochrome image2.jpg;echo success')
	os.system('convert image.jpg -rotate 90 -negate -flop -resize 132 -monochrome image.jpg;echo success')
else:
	print "sendandprint col"
#        os.system("convert image.jpg -rotate 90 -flop -colors 2 -morphology Thinning:-1 'LineEnds:-1;Peaks:1.5' -depth 1 image.jpg")
#        os.system("convert image.jpg -rotate 90  image.jpg")
#        os.system("convert image.jpg -flop  image.jpg")
#        os.system("convert image.jpg -rotate 90 -flop -colors 2 -morphology Thinning:-1 'Skeleton:1;Corners;LineEnds:-1;Peaks:1.5' -depth 1 image.jpg")
	print "d"
time.sleep(0.5)
os.system('	./pixel2ev3.py image.jpg > image.rtf')
#os.system('less -~ -E image.rtf')
os.system('sshpass -p "Just a bit off the block!" scp   -o "StrictHostKeyChecking no"  image.rtf root@192.168.8.200:~/lms2012/prjs/plotter_ppwi/image.rtf')
os.system('sshpass -p "Just a bit off the block!" scp  -o "StrictHostKeyChecking no"   image.rtf root@192.168.8.200:~/lms2012/prjs/plotter_ppwi/image2.rtf')
os.system("sshpass -p 'Just a bit off the block!' ssh -y -o 'StrictHostKeyChecking no'  root@192.168.8.200 'echo 1 > ~/lms2012/prjs/plotter_ppwi/lock.rtf'") 
donee = "0"
print "hi"
time.sleep(5)

while donee != "1":
	os.system('sshpass -p "Just a bit off the block!" scp  -o "StrictHostKeyChecking no"  root@192.168.8.200:~/lms2012/prjs/plotter_ppwi/done.rtf donee.rtf')
	done = os.popen('less donee.rtf -E -~ | fgrep -v M').read()
#	print donee
	time.sleep(0.1)
	if "1" in done:
		print "I am done!"
		donee = "1"
#	print "Done: " +str(donee)
	sys.stdout.flush()
