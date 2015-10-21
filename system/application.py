from pysixad import *       #Import the PS3 library
from motion import *

print "Initializing"
p=pysixad()     #Create a PS3 object
m=motion()
print "Done"
s=150   #Initialize
run=0
flag=0
while True:
    p.update()          #Read the ps3 values
    if p.up:            #If UP is pressed move forward
        m.fwd()
        print "fwd"
    elif p.down:        #If DOWN is pressed go back
        m.bwd()
        print "bwd"
    elif p.left:        #If LEFT is pressed turn left
        if run:
            pass
            #left()
            flag=1
        print "left"
    elif p.right:       #If RIGHT is pressed move right
        if run:
            pass
            #right()
            flag=1
        print "right"
    elif p.cross:       #If CROSS is pressed stop
        if run:
            pass
            #stop()
        print "cross"
    else:
        if flag:        #If LEFT or RIGHT key was last pressed start moving forward again 
            pass
            #fwd()       
            print "flag"
    if p.l2:            #Increase the speed if L2 is pressed
        s+=2
        if s>255:
            s=255
    if p.r2:            #Decrease the speed if R2 is pressed
        s-=2
        if s<0:
            s=0
    x=(p.a_joystick_left_x+1)*90
    #print int(x)
    if run:
        print "servo"
        #servo(int(x))   #Turn servo a/c to left joy movement
    time.sleep(.01)
