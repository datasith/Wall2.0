from pysixad import *       #Import the PS3 library
from motion import *

print "Initializing"
p=pysixad()     #Create a PS3 object
m=motion()
print "Done"

up_counter=1
down_counter=1
left_counter=1
right_counter=1
cross_counter = 1
circle_counter = 1

sensitivity=7

while True:
    p.update()          #Read the ps3 values
    if p.up:            #If UP is pressed move forward
        up_counter+=1
    elif p.down:        #If DOWN is pressed go back
        down_counter+=1
    elif p.left:        #If LEFT is pressed turn left
        left_counter+=1
    elif p.right:       #If RIGHT is pressed move right
        right_counter+=1
    elif p.cross:       #If CROSS is pressed record position
        cross_counter+=1
    elif p.circle:      #If CIRCLE is pressed playback positions
        circle_counter+=1
    else:
        up_counter = 1
        down_counter = 1
        left_counter = 1
        right_counter = 1
        cross_counter = 1
        circle_counter = 1
    if not (up_counter % sensitivity):
        m.fwd()
    if not (down_counter % sensitivity):
        m.bwd()
    if not (left_counter % sensitivity):
        m.left()
    if not (right_counter % sensitivity):
        m.right()
    if not (cross_counter % sensitivity):
        m.record_current_position()
    if not (circle_counter % sensitivity):
        m.playback_saved_positions()
    time.sleep(.01)
