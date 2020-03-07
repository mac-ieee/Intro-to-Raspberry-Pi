#############################
#   Using PWM to cycle  
#   through colors of an
#   LED.
############################

import RPi.GPIO as GPIO 
import time 

#GPIO pin 2 to 27 are PWM compatible 
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
R = 100 #We start with YELLOW 
G = 100 
B = 0 

pwm_R.start(R) #start PWM at 0% duty cycle (off) 
pwm_G.start(G) 
pwm_B.start(B) 
phase = 1 

print("Yellow") 
time.sleep(5) 

while(True): 
    if(phase == 1): #Cyan 
        R-=1 
        B+=1 
        
        if(B==100): 
            print("Cyan") 
            phase+=1 
            time.sleep(5) 
    
    if(phase == 2): #Magenta 
        G-=1 
        R+=1 
        
        if(G==0): 
            print("Magenta") 
            phase+=1 
            time.sleep(5) 
    
    if(phase == 3): #Yellow 
        G+=1 
        B-=1 
        
        if(G==100): 
            print("Yellow") 
            phase=1 
            time.sleep(5) 
    
    pwm_R.ChangeDutyCycle(float(R)) #apply our changes 
    pwm_G.ChangeDutyCycle(float(G)) 
    pwm_B.ChangeDutyCycle(float(B)) 
    
    time.sleep(0.05) # delay for effect 
    #print(phase,R,G,B) 
     
GPIO.cleanup()