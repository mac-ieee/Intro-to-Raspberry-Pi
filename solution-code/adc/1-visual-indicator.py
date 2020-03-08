#############################
#   Displaying ADC values
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

        if int(str(serialData)[2:-5]) >= int(1023/10): 
            GPIO.output(40,True) 
        else: 
            GPIO.output(40,False) 
        
        if int(str(serialData)[2:-5]) >= 2*int(1023/10): 
            GPIO.output(38,True) 
        else: 
            GPIO.output(38,False) 
        
        if int(str(serialData)[2:-5]) >= 3*int(1023/10): 
            GPIO.output(37,True) 
        else: 
            GPIO.output(37,False) 
        
        if int(str(serialData)[2:-5]) >= 4*int(1023/10): 
            GPIO.output(36,True) 
        else: 
            GPIO.output(36,False) 
        
        if int(str(serialData)[2:-5]) >= 5*int(1023/10): 
            GPIO.output(35,True) 
        else: 
            GPIO.output(35,False) 
            
        if int(str(serialData)[2:-5]) >= 6*int(1023/10): 
            GPIO.output(33,True) 
        else: 
            GPIO.output(33,False) 
        
        if int(str(serialData)[2:-5]) >= 7*int(1023/10): 
            GPIO.output(32,True) 
        else: 
            GPIO.output(32,False)

        if int(str(serialData)[2:-5]) >= 8*int(1023/10): 
            GPIO.output(31,True) 
        else: 
            GPIO.output(31,False)
        
        if int(str(serialData)[2:-5]) >= 9*int(1023/10): 
            GPIO.output(29,True) 
        else: 
            GPIO.output(29,False) 
        
        if int(str(serialData)[2:-5]) >= 1023: 
            GPIO.output(22,True) 
        else: 
            GPIO.output(22,False)