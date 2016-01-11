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
isIncSpeed = False
isDecSpeed = False
isIncInterval = False
isDecInterval = False

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
    elif ( p.up ):
        isIncSpeed = True
    elif ( p.down ):
        isDecSpeed = True
    elif ( p.right ):
        isIncInterval = True
    elif ( p.left ):
        isDecInterval = True
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
        if isIncSpeed:
            m.update_feedrate(100)
            isIncSpeed = False
        if isDecSpeed:
            m.update_feedrate(-100)
            isDecSpeed = False
        if isIncInterval:
            m.update_interval(1)
            isIncInterval = False
        if isDecInterval:
            m.update_interval(-1)
            isDecInterval = False
