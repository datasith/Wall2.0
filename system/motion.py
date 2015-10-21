#!/usr/bin/env python
"""\
Simple g-code streaming script for grbl
"""
 
import serial
import time
 
class motion():
    def __init__(self):
        # Open grbl serial port
        self.s = serial.Serial('/dev/ttyUSB0',115200)
        # Wake up grbl
        self.s.write("\r\n\r\n")
        time.sleep(2)   # Wait for grbl to initialize
        self.s.flushInput()  # Flush startup text in serial input        
        self.send("g91")
 
    def send(self, cmd): 
        print 'Sending: ' + cmd
        self.s.write(cmd + '\n') # Send g-code block to grbl
        grbl_out = self.s.readline() # Wait for grbl response with carriage return
        print 'Response: ' + grbl_out.strip()

    def fwd(self):
        self.send("g1 x1 f400")

    def bwd(self):
        self.send("g1 x-1 f400")

    def disconnect(self):
        # Close file and serial port
        self.s.close()
