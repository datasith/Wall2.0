from ps3 import *       #Import the PS3 library

print "Initializing"
p=ps3()     #Create a PS3 object
print "Done"
s=150   #Initialize
run=0
flag=0
while True:
    if run:
        #set_speed(s)    #Update the speed
        #print "run"
        pass
    p.update()          #Read the ps3 values
    if p.up:            #If UP is pressed move forward
        if run:
            pass
            #fwd()
        print "run"
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
    elif p.down:        #If DOWN is pressed go back
        if run:
            pass
            #bwd()
        print "down"
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
