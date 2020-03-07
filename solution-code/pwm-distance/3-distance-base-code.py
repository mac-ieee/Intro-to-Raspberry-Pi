#############################
#   Displaying distance  
#   from distance sensor.
############################


import RPi.GPIO as GPIO 
import time 

#Things to consider: 
#-use IDLE (for python 3.X) rather than Thonny 
#-use 5v pin on RPi (pins 2 & 4) NOT 3.3v 

#CAUTION: do not sent 5v into RPi! use voltage divider 
 
GPIO.setmode(GPIO.BOARD) #physical numbering scheme 
trig = 40 
echo = 38 

GPIO.setup(trig, GPIO.OUT) #set pin 38 as output 
GPIO.setup(echo, GPIO.IN) #set pin 40 as input 

GPIO.output(trig, False) #start trig at 0 
time.sleep(1) # delay for setup 

def distance(): 
    GPIO.output(trig, True) #LED on 
    time.sleep(0.00001) #figure out how much time this is 
    GPIO.output(trig, False) #LED off 
    
    while GPIO.input(echo)==0: 
        start = time.time() 
    
    while GPIO.input(echo)==1: 
        stop = time.time() 
        distance = 17014.5*(stop-start) 
    
    return distance #in centimeters 
    
scanON = True 
while (scanON): 
    dist = distance() # function call 
    time.sleep(1) 

    if dist < 1000: # print condition 
        print(dist) 
    if dist < 2: # exit condition 
        scanON = False
        
GPIO.cleanup()