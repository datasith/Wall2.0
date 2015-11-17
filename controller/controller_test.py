from ps3 import *       #Import the PS3 library

print "Initializing"
p=ps3()     #Create a PS3 object
print "Done"
s=150   #Initialize
run=0
flag=0
while True:
    p.update()          #Read the ps3 values
    if p.up:            #If UP is pressed
        print "up"
    elif p.left:        #If LEFT is pressed
        print "left"
    elif p.right:       #If RIGHT is pressed
        print "right"
    elif p.down:        #If DOWN is pressed
        print "down"
    elif p.cross:       #If CROSS is pressed
        print "cross"
    if p.l2:            #Increase the speed if L2 is pressed
        s+=2
        if s>255:
            s=255
    if p.r2:            #Decrease the speed if R2 is pressed
        s-=2
        if s<0:
            s=0
    x=(p.a_joystick_left_x+1)*90
    time.sleep(.01)
