#!/usr/bin/env python
from pysixad import *      #Import the PS3 library
from motion import *
import sys, time

print "Initializing"

while True:
    try:
        p=pysixad()
        p.check_pad()
    except OSError:
        continue
        sys.exit()
    except IOError:
        continue
        sys.exit()
    break
p.initialize()
m=motion()

print "Done"

isMoving = False
isRecording = False
isPlaying = False
isChangingMode = False

while True:
    p.update()

    if ( abs(p.a_joystick_left_x)>.1 or
         abs(p.a_joystick_left_y)>.1 ):

        m.move(cmp(p.a_joystick_left_x,0),
               cmp(p.a_joystick_left_y,0))
        isMoving = True
        time.sleep(0.1)
    elif ( p.cross ):
        isRecording = True
    elif ( p.circle ):
        isPlaying = True
    elif ( p.square ):
        isChangingMode = True
    else:
        if isMoving:
            m.stop()
            isMoving = False
        if isRecording:
            m.record_current_position()
            isRecording = False
        if isPlaying:
            m.playback_saved_positions()
            isPlaying = False
        if isChangingMode:
            m.changeMode()
            isChangingMode = False
