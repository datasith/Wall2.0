#!/usr/bin/env python
"""\
Simple g-code streaming script for grbl
"""
 
import serial
import time
import json
from multiprocessing import Process
 
class motion():
    def __init__(self):
        self.serial_reader = Process(target=self.get_response,args=())
        # Open grbl serial port
        #self.s = serial.Serial("/dev/ttyUSB0",baudrate=115200,xonxoff=True,timeout=1)
        self.s = serial.Serial("/dev/ttyUSB0",baudrate=115200,timeout=0.1,rtscts=True,xonxoff=False)

        self.rsp=''
        self.posx=0.0
        self.posy=0.0

        # Wake up grbl
        self.s.write("\r\n\r\n")
        time.sleep(2)   # Wait for grbl to initialize
        self.s.flushInput()  # Flush startup text in serial input        
        # set origin offset
        self.send("g92 x0 y0")
        # feedrate speed
        self.send("f400")
        #self.send("g91")

        self.serial_reader.start()
 
    def send(self, cmd): 
        print 'Sending: ' + cmd
        self.s.write(cmd + '\n') # Send g-code block to grbl

    def get_response(self):
        while(1):
            tmp = self.s.readline()
            tmp = tmp.strip()
            if tmp is not '':
                tmp = json.loads(tmp)
                self.rsp=tmp
                if 'sr' in tmp.keys():
                    if 'posx' in tmp['sr'].keys():
                        self.posx=tmp['sr']['posx']
                        print 'pos: '+str(self.posx)
            else:
                time.sleep(.2)

    def get_current_position(self):
        self.send("sr")
        # Check if serial_reader is running?
        print "get_current_position()"
        print 'pos: '+str(self.posx)

    def fwd(self):
        self.send("g1 x1")

    def bwd(self):
        self.send("g1 x-1")

    def disconnect(self):
        # Close file and serial port
        self.s.close()
