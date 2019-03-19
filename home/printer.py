#!/usr/bin/python3
# -*- coding: utf-8 -*-
#import python packages

#install --> (sudo) apt-get install python-pip --> (sudo) pip install pillow python-ev3dev
#running --> run (sudo) python pythonfilename.py imagefilename.png (jpg will work along with others types) -->
#            you will be given a dialogue --> just type "" and return/enter to continue

from PIL import Image, ImageFilter
import ev3dev.ev3 as ev3
import time
import os
import sys
from termcolor import colored


# paper resolution
vert_move = 15;
horiz_move = 15;
#res = (horiz_deg/horiz_move);
false = 0
true = 1
#function to ensure the motor has stopped before moving on
xxx = 0
def waitformotor(motor):
    while motor.state != []:
        xxx = 0
# define motors and use brake mode

paper = ev3.MediumMotor('outA')
pen1 = ev3.MediumMotor('outB')
pen2 = ev3.MediumMotor('outD')
head = ev3.MediumMotor('outC')

pen1.stop_action = "brake"
pen2.stop_action = "brake"
head.stop_action = "brake"
paper.stop_action = "brake"
head.reset()
pen1.reset()
pen2.reset()
paper.reset()


#move paper until color sensor recieves >50 reading

#paper.speed_regulation_enabled=u'on'
pen1.run_to_rel_pos(speed_sp=-400, position_sp=-53)
pen2.run_to_rel_pos(speed_sp=400, position_sp=53)
waitformotor(pen1)
waitformotor(pen2)
pen1.reset()
pen2.reset()
print("Init printer")


def resetMotors():
    paper.run_to_abs_pos(position_sp=0, speed_sp=1000)
    head.run_to_abs_pos(position_sp=0, speed_sp=1000)
    pen1.run_to_abs_pos(position_sp=0, speed_sp=1000)
    pen2.run_to_abs_pos(position_sp=0, speed_sp=1000)
    waitformotor(paper)
    waitformotor(head)
    waitformotor(pen1)
    waitformotor(pen2)

#make a function to make a dot on the page
def makedot(pen,dir):
    pen.run_to_rel_pos(speed_sp=400*dir, position_sp=55*dir)
    waitformotor(pen) #double check if motor is stopped before raising pen
    pen.run_to_rel_pos(speed_sp=-400*dir, position_sp=-53*dir)
    waitformotor(pen) #double check if motor is stopped before raising pen

#resize and flip image
#filename = sys.argv[1]

def printer(filename):
    w = 0
    h = 0
    l = 0
    img2 = Image.open(filename) #open image
    img=img2.convert("RGBA")
    width, height = img.size # get image size

    #define variables
    array = []
    w = width-1 #define starting width counter
    print(width," x ",height)
    r_array=[]
    g_array = []
    b_array = []
    bl_array = []

    #different colors: (in rgba -- remove last number in set to convert to rgb)
    #red = (255,0,0,0) eg. in rgb -- (255,0,0)
    #green = (0,255,0,0)
    #blue = (0,0,255,0)
    #black = (0,0,0,0)
    #white = (255,255,255,0)

    print(img.getpixel((w,h)))

#    r_array = [[255]*width]*height
#    g_array = [[255]*width]*height
#    b_array = [[255]*width]*height
#    bl_array = [[255]*width]*height
    r_array = []
    g_array = []
    b_array = []
    bl_array = []
    e4col = false
    while h != height:
            r_array.append([255]*width)
            g_array.append([255]*width)
            b_array.append([255]*width)
            bl_array.append([255]*width)
            while w < width:
                    array.append(img.getpixel((w, h))) #get rgba black or white of each pixel and write to full array
                    r,g,b,a = img.getpixel((w, h)) #get rgba of each pixel
                    #check if red, green, or blue is greatest in rgb values --- check if black or white also --> then append array differently for each switch case
                    if r > g and r > b :
                        e4col = true
                        r_array[h][w] = 0
#                        g_array[h][w] = 255
#                        b_array[h][w] = 255
#                        bl_array[h][w] = 255
                        print("R", end="")
                    elif g > r and g > b :
                        e4col = true
                        g_array[h][w] = 0
#                        r_array[h][w] = 255
#                        b_array[h][w] = 255
#                        bl_array[h][w] = 255
                        print("G", end="")
                    elif b > r and b > g :
                        b_array[h][w] = 0
#                        g_array[h][w] = 255
#                        r_array[h][w] = 255
#                        bl_array[h][w] = 255
                        print("B", end="")
                    elif b < 50 and r < 50 and g < 50 :
#                        b_array[h][w] = 255
#                        g_array[h][w] = 255
#                        r_array[h][w] = 255
                        bl_array[h][w] = 0
                        print("D", end="")
                    else:
#                        b_array[h][w] = 255
#                        g_array[h][w] = 255
#                        r_array[h][w] = 255
#                        bl_array[h][w] = 255
                        print(" ", end="")
                    w = w+1 #move to next pixel -- use -1 to flip image -> make images not backward when printed
            print(" "+str(h))
            w = 0 #reset width counter
            h = h+1 #move to next row



    x = input('Is this picture ok? Press enter to continue...') #wait for dialogue to be answered then start printing

    initial = time.time()
    
    xd = 0
    yd = 0
    xda = 0 
    while yd < height:
        while xd != 0:
            if bl_array[yd][xd] == 0: #is pixel black?
                print("D", end="") #print block if black pixel
                head.run_to_abs_pos(position_sp=horiz_move*xd, speed_sp=400, ramp_down_sp=500)
                waitformotor(head)
                # lower and raise pen
                makedot(pen1,-1)
                # move pen left	
            elif b_array[yd][max([0,xd-21])] == 0:
                print("B", end="") #print block if red pixel
                head.run_to_abs_pos(position_sp=(horiz_move*xd), speed_sp=400, ramp_down_sp=500)
                waitformotor(head)
                # lower and raise pen
                makedot(pen2,1)
            else:
                print(" ", end="")
                #move pen left
            xd = xd - 1
            xda = xda + 1

        print("; PCT: "+str(int(100*xda/(width*height)))+"% ; Time Remaining: "+str(int((100-100*xda/(width*height))*(time.time()-initial)/(100*xda/(width*height)))))
        yd = yd + 1
        xd = width-1
        # move paper forward
        paper.run_to_abs_pos(position_sp=vert_move*(yd), speed_sp=250,ramp_down_sp=500)
        # reset pen location
        waitformotor(paper)

    #reset paper location
    resetMotors()

    if e4col == true:
        x = input('Ready to print red/green? Press enter to continue...') #wait for dialogue to be answered then start printing

        initial = time.time()
    
        xd = 0
        yd = 0
        xda = 0 
        while yd < height:
            while xd != 0:
                if r_array[yd][xd] == 0: #is pixel black?
                    print("R", end="") #print block if black pixel
                    head.run_to_abs_pos(position_sp=horiz_move*xd, speed_sp=400, ramp_down_sp=500)
                    waitformotor(head)
                    # lower and raise pen
                    makedot(pen1,-1)
                    # move pen left	
                elif g_array[yd][max([0,xd-21])] == 0:
                    print("G", end="") #print block if red pixel
                    head.run_to_abs_pos(position_sp=(horiz_move*xd), speed_sp=400, ramp_down_sp=500)
                    waitformotor(head)
                    # lower and raise pen
                    makedot(pen2,1)
                else:
                    print(" ", end="")
                    #move pen left
                xd = xd - 1
                xda = xda + 1

            print("; PCT: "+str(int(100*xda/(width*height)))+"% ; Time Remaining: "+str(int(((100-100*xda/(width*height))*(time.time()-initial)/(100*xda/(width*height)))))+"s")
            yd = yd + 1
            xd = width - 1
            # move paper forward
            paper.run_to_abs_pos(position_sp=vert_move*(yd), speed_sp=250,ramp_down_sp=500)
            # reset pen location
            waitformotor(paper)

        #reset paper location
        resetMotors()
        
    
"""
img2 = Image.open("ev3screen.jpg")
raw = img2.tobytes()
image = Image.frombytes(img2.mode, img2.size, raw)
lcd = ev3.Screen()
lcd._img.paste(image, (0, 0))
lcd.update()
"""
