from pysixad import *      #Import the PS3 library
from motion import *
import sys

print "Initializing"
p=pysixad()    #Create a PS3 object
m=motion()
print "Done"

isMoving = False
while True:
    p.update()

    if ( abs(p.a_joystick_left_x)>.1 or
         abs(p.a_joystick_left_y)>.1 ):

        m.move(cmp(p.a_joystick_left_x,0),
               cmp(p.a_joystick_left_y,0))
        isMoving = True
        time.sleep(0.1)

    else:
        if isMoving:
            m.stop()
            isMoving = False
