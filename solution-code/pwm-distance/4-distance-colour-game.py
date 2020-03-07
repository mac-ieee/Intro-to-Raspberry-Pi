#############################
#   Change LED colours   
#   depending on distance
#   from sensor.
############################

import RPi.GPIO as GPIO 
import time 

#Things to consider: 
#-use IDLE (for python 3.X) rather than Thonny 
#-use 5v pin on RPi (pins 2 & 4) NOT 3.3v 
#CAUTION: do not send 5v into RPi! use voltage divider
 
#Distance sensor pin setup 
GPIO.setmode(GPIO.BOARD) #physical numbering scheme 
trig = 40 
echo = 38 

GPIO.setup(trig, GPIO.OUT) #set pin 38 as output 
GPIO.setup(echo, GPIO.IN) #set pin 40 as input 

GPIO.output(trig, False) #start trig at 0 
time.sleep(1) # delay for setup 

#LED (PWM) Setup 
led_R = 11 
led_G = 12 
led_B = 13 

GPIO.setmode(GPIO.BOARD) #numbering scheme 
GPIO.setup(led_R, GPIO.OUT) #set pin 11 as output 
GPIO.setup(led_G, GPIO.OUT) #set pin 11 as output 
GPIO.setup(led_B, GPIO.OUT) #set pin 11 as output 

pwm_R = GPIO.PWM(led_R, 5000) #enable PWM, specify frequency of 1kHz 
pwm_G = GPIO.PWM(led_G, 5000) 
pwm_B = GPIO.PWM(led_B, 5000) 

#variables to detemine the colour (out of 100) 
R = 0.0 
G = 0.0 
B = 0.0 

pwm_R.start(R) #start PWM at 0% duty cycle (off) 
pwm_G.start(G) 
pwm_B.start(B) 

#set bounds for our sensor, in cm's 
middle = 20 
max_distance = 40 
min_distance = 3 
tolerance = 1 

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
    time.sleep(0.1) 
    
    if dist>100: 
        continue 
    elif dist > max_distance: # print condition 
        B = 100 
        R = 0 
    elif dist < min_distance: # exit condition 
        scanON = False 
        B = 0 
        R = 100 
    elif abs(dist-middle) <= tolerance: 
        B = 0 
        R = 0 
    elif dist < middle: 
        B = 0 
        R = (middle - dist)*(100/middle) 
    
    else: 
        R = 0 
        B = (dist - middle)*(100/middle) 
        pwm_R.ChangeDutyCycle(float(R)) #apply our colour changes 
        pwm_B.ChangeDutyCycle(float(B))
        
GPIO.cleanup()