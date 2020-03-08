#############################
#   Reading ADC values
#   and displaying
#   binary equivalent
#   on LEDs.
############################

import serial 
import RPi.GPIO as GPIO 

GPIO.setmode(GPIO.BOARD) 
GPIO.setwarnings(False) 

chan_list = [40,22,29,31,32,33,35,36,37,38] 
GPIO.setup(chan_list,GPIO.OUT) 

arduinoData = serial.Serial('/dev/ttyACM0',9600) 

while True: 
    if arduinoData.inWaiting() > 0: 
        serialData = arduinoData.readline() 
        in_value = int(str(serialData)[2:-5]) 
        
        if in_value%2 == 1: 
            GPIO.output(22,True) 
        else: 
            GPIO.output(22,False) 
            in_value = int(in_value/2) 

        if in_value%2 == 1: 
            GPIO.output(29,True) 
        else: 
            GPIO.output(29,False) 
            in_value = int(in_value/2) 
        
        if in_value%2 == 1: 
            GPIO.output(31,True) 
        else: 
            GPIO.output(31,False) 
            in_value = int(in_value/2) 
            
        if in_value%2 == 1: 
            GPIO.output(32,True) 
        else: 
            GPIO.output(32,False) 
            in_value = int(in_value/2) 
            
        if in_value%2 == 1: 
            GPIO.output(33,True) 
        else: 
            GPIO.output(33,False) 
            in_value = int(in_value/2) 
        
        if in_value%2 == 1: 
            GPIO.output(35,True) 
        else: 
            GPIO.output(35,False)
            in_value = int(in_value/2) 
            
        if in_value%2 == 1: 
            GPIO.output(36,True) 
        else: 
            GPIO.output(36,False) 
            in_value = int(in_value/2) 
            
        if in_value%2 == 1: 
            GPIO.output(37,True) 
        else: 
            GPIO.output(37,False) 
            in_value = int(in_value/2) 
            
        if in_value%2 == 1: 
            GPIO.output(38,True) 
        else: 
            GPIO.output(38,False) 
            in_value = int(in_value/2) 
            
        if in_value == 1: 
            GPIO.output(40,True) 
        else: 
            GPIO.output(40,False)