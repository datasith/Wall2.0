#!/usr/bin/env python
"""\
Simple g-code streaming script for grbl
"""
 
import serial
import time
import json
import RPi.GPIO as GPIO
from multiprocessing import Process, Queue
class motion():
    def __init__(self):
        # Open grbl serial port
        #self.s = serial.Serial("/dev/ttyUSB0",baudrate=115200,xonxoff=True,timeout=1)
        self.s = serial.Serial("/dev/ttyUSB0",
                               baudrate=115200,
                               timeout=0.1,
                               rtscts=True,
                               xonxoff=False)
        self.rsp=''
        self.posx=0.0
        self.posy=0.0
        self.positions_file = 'positions.csv'
        self.mode = 'delay'
        self.sensor_pin = 3
        GPIO.setmode(GPIO.BOARD)
#        GPIO.setup(self.sensor_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.sensor_pin, GPIO.IN)

        # Wake up grbl
        self.s.write("\r\n\r\n")
        time.sleep(2)   # Wait for grbl to initialize
        self.s.flushInput()  # Flush startup text in serial input        
        # set origin offset
        self.send("g92 x0 y0")
        # feedrate speed
        self.send("f100")
        # relative mode 
        self.send("g91")

        with open(self.positions_file,'w') as f:
            f.write('posx,posy\n')

        self.pos_queue = Queue()
        self.serial_proc = Process(target=self.get_response,
                                   args=(self.pos_queue,))

        self.serial_proc.start()
 
    def send(self, cmd): 
        print 'Sending: ' + cmd
        self.s.write(cmd + '\n') # Send g-code block to grbl

    def move(self,sign_x, sign_y):
        x = "x"+str(sign_x*10)    
        y = "y"+str(sign_y*10)    
        #self.send("%")
        self.send(" ".join(["g1",x,y]))

    def stop(self):
        self.send("!")
        self.send("%")

    def disconnect(self):
        # Close file and serial port
        self.s.close()

    def get_response(self, q):
        while(1):
            tmp = self.s.readline()
            tmp = tmp.strip()
            if tmp is not '':
                tmp = json.loads(tmp)
                print tmp
                if 'r' in tmp.keys():
                    if 'sr' in tmp['r'].keys():
                        tmp = tmp['r']
                if 'sr' in tmp.keys():
                    if 'posx' in tmp['sr'].keys():
                        self.posx=tmp['sr']['posx']
                    if 'posy' in tmp['sr'].keys():
                        self.posy=tmp['sr']['posy']
                    q.put((self.posx, self.posy))
                    print 'pos1: '+str((self.posx, self.posy))
            else:
                time.sleep(.2)

    def record_current_position(self):
        self.send('{"sr":null}')
        print "Saving"
        # TODO: Check if serial_proc is running?
        self.update_current_position()
        with open(self.positions_file,'a') as f:
            f.write(str(self.posx)+','+str(self.posy)+'\n')

    def update_current_position(self):
        while not self.pos_queue.empty():
            self.posx, self.posy = self.pos_queue.get()

    def getTrigger(self):
        return GPIO.input(self.sensor_pin)

    def changeMode(self):
        if self.mode == 'delay':
            self.mode = 'sensor'
        elif self.mode == 'sensor':
            self.mode = 'delay'

    def playback_saved_positions(self):
        # absolute mode 
        self.send("g90")
        import csv,time
        self.update_current_position()
        with open(self.positions_file) as f:
            lines = csv.DictReader(f)
            for l in lines:
                print 'x_dst: '+l['posx']+' - '+str(self.posx)
                print 'y_dst: '+l['posy']+' - '+str(self.posy)
                x_dst = float(l['posx'])#-self.posx
                y_dst = float(l['posy'])#-self.posy
                x = ' x'+str((x_dst))
                y = ' y'+str((y_dst))
                print(x,y)
                self.send('g1'+x+y)
                while(1):
                    self.update_current_position()
                    if (self.posx != float(l['posx'])) or \
                       (self.posy != float(l['posy'])):
                       time.sleep(.1)
                    else:
                        break

                if(self.mode == 'delay'):
                    time.sleep(2)
                elif(self.mode == 'sensor'):
                    while(not self.getTrigger()):
                        time.sleep(.01)
        # relative mode 
        self.send("g91")
