from pysixad import *       #Import the PS3 library
from motion import *

print "Initializing"
p=pysixad()     #Create a PS3 object
m=motion()
print "Done"
up_counter=1
down_counter=1
sensitivity=7
while True:
    p.update()          #Read the ps3 values
    if p.up:            #If UP is pressed move forward
        up_counter+=1
    elif p.down:        #If DOWN is pressed go back
        down_counter+=1
    elif p.left:        #If LEFT is pressed turn left
        print "left"
    elif p.right:       #If RIGHT is pressed move right
        print "right"
    elif p.cross:       #If CROSS is pressed stop
        cross_counter+=1
    else:
        up_counter = 1
        down_counter = 1
        cross_counter = 1
    if not (up_counter % sensitivity):
        m.fwd()
    if not (down_counter % sensitivity):
        m.bwd()
    if not (cross_counter % sensitivity):
        m.get_current_position()
    time.sleep(.01)
