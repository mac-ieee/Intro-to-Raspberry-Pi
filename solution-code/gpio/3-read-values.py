
import RPi.GPIO as GPIO
from time import sleep 


GPIO.setmode(GPIO.BOARD)
start =12 #read from pins 12 and 16
stop =16 #Declare the pins as inputs and “attach” the pull_up resistors to them

GPIO.setup(start,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(stop,GPIO.IN,pull_up_down=GPIO.PUD_UP)

end = False 
while(notend):
    if GPIO.input(start)==0:
        print(‘Start was pressed’)
        sleep(0.5)
    
    if GPIO.input(stop)==0:
        print(‘Stop was pressed’)
        sleep(0.5)
    
    if GPIO.input(start)==0 and GPIO.input(stop)==0:
        print(‘Make up your mind!’)
        end =True
    
GPIO.cleanup()#clear out pin assignments